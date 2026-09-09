#!/usr/bin/env python3
import csv,json,argparse
from collections import Counter
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
ROOT=Path(__file__).resolve().parents[1]; R=ROOT/'research/website-patterns'; G=R/'generated'
def j(p): return json.loads(Path(p).read_text(encoding='utf-8'))
def font(n,b=False):
 p=Path('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf' if b else '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'); return ImageFont.truetype(str(p),n) if p.exists() else ImageFont.load_default()
def fit(im,w,h):
 c=im.copy(); c.thumbnail((w,h),Image.Resampling.LANCZOS); return c
def bounds(im,b):
 w,h=im.size; x=round(b['x']*w); y=round(b['y']*h); return (x,y,min(w,round((b['x']+b['width'])*w)),min(h,round((b['y']+b['height'])*h)))
def render(cd,tax):
 docs=[]
 for p in sorted((cd/'sites').glob('*.json')):
  d=j(p); s=d['site']; last=-1
  for q in s['sections']:
   if q['type'] not in tax: raise SystemExit(f'{p}: unknown type {q["type"]}')
   b=q['bounds_normalized'];
   if not(0<=b['y']<=1 and 0<b['height']<=1 and b['y']+b['height']<=1.0001 and b['y']>=last): raise SystemExit(f'{p}: invalid bounds')
   last=b['y']
  src=ROOT/s['source_repo_path'];
  if not src.exists(): raise SystemExit(f'Missing source screenshot: {src}')
  docs.append((s,Image.open(src).convert('RGB')))
 cid=j(cd/'cohort.json')['id']; sc=Counter(); pr=Counter(); tr=Counter()
 for s,im in docs:
  seq=[q['type'] for q in s['sections']]; sc.update(seq); pr.update(set(seq)); tr.update(zip(seq,seq[1:]))
 G.mkdir(parents=True,exist_ok=True)
 summary={'cohort':cid,'site_count':len(docs),'section_counts':dict(sc),'site_presence':dict(pr),'transitions':[{'from':a,'to':b,'count':n} for (a,b),n in tr.most_common()]}; (G/f'{cid}-summary.json').write_text(json.dumps(summary,indent=2))
 with (G/f'{cid}-transitions.csv').open('w',newline='') as f:
  w=csv.writer(f); w.writerow(['from','to','count']); [w.writerow([a,b,n]) for (a,b),n in tr.most_common()]
 W=4700; RH=700; H=250+RH*len(docs); out=Image.new('RGB',(W,H),'white'); d=ImageDraw.Draw(out); d.text((40,30),'MODERN TELECOM COHORT · WEBSITE PATTERN ATLAS',font=font(44,True),fill='#111'); d.text((40,90),'Screenshot → semantic crops → structure sequence → aggregate evidence',font=font(24),fill='#475569')
 for i,(s,im) in enumerate(docs):
  y0=200+i*RH; d.text((40,y0+10),s['name'],font=font(24,True),fill='#111'); full=fit(im,210,600); out.paste(full,(40,y0+55)); x=290
  for k,q in enumerate(s['sections']):
   cx=x+(k%5)*510; cy=y0+55+(k//5)*285; col=tax[q['type']]['color']; d.rounded_rectangle((cx,cy,cx+490,cy+265),radius=10,fill='white',outline='#CBD5E1',width=2); d.rectangle((cx,cy,cx+9,cy+265),fill=col); cr=fit(im.crop(bounds(im,q['bounds_normalized'])),460,175); out.paste(cr,(cx+15+(460-cr.width)//2,cy+10)); d.text((cx+18,cy+195),tax[q['type']]['label'],font=font(15,True),fill=col); d.text((cx+18,cy+220),q['label'][:56],font=font(14),fill='#475569')
  sx=2860; sy=y0+55; d.text((sx,sy),'STRUCTURE',font=font(18,True),fill='#111'); sy+=35
  for q in s['sections']:
   info=tax[q['type']]; d.rounded_rectangle((sx,sy,sx+420,sy+35),radius=6,fill=info['color']); d.text((sx+10,sy+8),info['label'],font=font(14),fill='white'); sy+=41
  rx=3370; ry=y0+55; d.text((rx,ry),'TRANSITIONS',font=font(18,True),fill='#111'); ry+=34
  for a,b in zip(s['sections'],s['sections'][1:]): d.text((rx,ry),f"{tax[a['type']]['label']} → {tax[b['type']]['label']}",font=font(14),fill='#334155'); ry+=23
 out.save(G/f'{cid}-atlas.png',optimize=True); return summary
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--cohort'); a=ap.parse_args(); tax=j(R/'taxonomy.json')['section_types']; dirs=[R/'cohorts'/a.cohort] if a.cohort else [p for p in (R/'cohorts').iterdir() if p.is_dir() and (p/'cohort.json').exists()]; all=[render(p,tax) for p in dirs]; G.mkdir(exist_ok=True); (G/'all-cohorts-summary.json').write_text(json.dumps(all,indent=2)); print(f'Rendered {len(all)} cohort(s).')
if __name__=='__main__': main()
