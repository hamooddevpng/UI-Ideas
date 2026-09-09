#!/usr/bin/env python3
import csv, json
from collections import Counter
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT=Path(__file__).resolve().parents[1]
R=ROOT/'research/website-patterns'; G=R/'generated'; README=ROOT/'README.md'
START='<!-- WEBSITE_PATTERN_RESEARCH_START -->'; END='<!-- WEBSITE_PATTERN_RESEARCH_END -->'

def J(p): return json.loads(Path(p).read_text(encoding='utf-8'))
def F(n,b=False):
    p=Path('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf' if b else '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf')
    return ImageFont.truetype(str(p),n) if p.exists() else ImageFont.load_default()
def fit(im,w,h):
    x=im.copy(); x.thumbnail((w,h),Image.Resampling.LANCZOS); return x
def box(im,b):
    w,h=im.size
    return (round(b['x']*w),round(b['y']*h),min(w,round((b['x']+b['width'])*w)),min(h,round((b['y']+b['height'])*h)))
def ell(d,xy,text,width,f,fill):
    s=str(text)
    while s and d.textbbox((0,0),s,font=f)[2]>width: s=s[:-1]
    if s!=text and len(s)>3: s=s[:-3].rstrip()+'...'
    d.text(xy,s,font=f,fill=fill)

def metadata(cohort):
    root=ROOT/cohort['source_root']; name=cohort.get('metadata_file')
    if not name and (root/'capture-results.json').exists(): name='capture-results.json'
    if not name or not (root/name).exists(): return {}
    return {x['slug']:x for x in J(root/name).get('results',[]) if x.get('slug')}

def inventory(cd,tax):
    cohort=J(cd/'cohort.json'); root=ROOT/cohort['source_root']; meta=metadata(cohort); semantic={}
    if (cd/'sites').exists():
        for p in sorted((cd/'sites').glob('*.json')):
            s=J(p)['site']; last=-1
            for q in s.get('sections',[]):
                if q['type'] not in tax: raise SystemExit(f'{p}: unknown type {q["type"]}')
                b=q['bounds_normalized']
                if not(0<=b['x']<=1 and 0<=b['y']<=1 and 0<b['width']<=1 and 0<b['height']<=1 and b['x']+b['width']<=1.0001 and b['y']+b['height']<=1.0001 and b['y']>=last): raise SystemExit(f'{p}: invalid bounds')
                last=b['y']
            semantic[s['slug']]=s
    out=[]
    for src in sorted(root.glob('*.png')):
        slug=src.stem; s=semantic.get(slug); m=meta.get(slug,{})
        out.append({'slug':slug,'name':s.get('name') if s else m.get('name') or slug.replace('-',' ').title(),'url':s.get('url') if s else m.get('url') or m.get('requestedUrl') or m.get('finalUrl') or '','source':src,'sections':s.get('sections',[]) if s else [],'analysis_status':'analyzed' if s and s.get('sections') else 'pending','cohort_id':cohort['id'],'cohort_name':cohort.get('name',cohort['id'])})
    return cohort,out

def summary(cohort,items):
    analyzed=[x for x in items if x['analysis_status']=='analyzed']; sc=Counter(); pres=Counter(); tr=Counter()
    for x in analyzed:
        seq=[q['type'] for q in x['sections']]; sc.update(seq); pres.update(set(seq)); tr.update(zip(seq,seq[1:]))
    return {'cohort':cohort['id'],'name':cohort.get('name',cohort['id']),'reference_site_count':len(items),'analyzed_site_count':len(analyzed),'pending_site_count':len(items)-len(analyzed),'section_counts':dict(sc),'site_presence':dict(pres),'transitions':[{'from':a,'to':b,'count':n} for (a,b),n in tr.most_common()]}

def row(canvas,d,item,tax,y0,rh,cohort_label=False):
    if (y0//rh)%2==0: d.rectangle((0,y0,3980,y0+rh-2),fill='#F8FAFC')
    title=(item['cohort_name']+' · ' if cohort_label else '')+item['name']; ell(d,(35,y0+13),title,1900,F(20,True),'#111827')
    if item['url']: ell(d,(35,y0+41),item['url'],1900,F(12),'#64748B')
    im=Image.open(item['source']).convert('RGB'); full=fit(im,180,330); canvas.paste(full,(38+(180-full.width)//2,y0+73)); d.rectangle((38,y0+73,218,y0+403),outline='#CBD5E1',width=2); d.text((38,y0+407),f'{im.width}×{im.height}',font=F(10),fill='#64748B')
    sec=item['sections']; cx0=245; cw=395; ch=157
    if sec:
        for i,q in enumerate(sec):
            rr,cc=divmod(i,6); x=cx0+cc*407; y=y0+72+rr*169; info=tax[q['type']]
            d.rounded_rectangle((x,y,x+cw,y+ch),radius=9,fill='white',outline='#CBD5E1',width=1); d.rectangle((x,y,x+8,y+ch),fill=info['color'])
            cr=fit(im.crop(box(im,q['bounds_normalized'])),cw-28,90); canvas.paste(cr,(x+14+(cw-28-cr.width)//2,y+8)); ell(d,(x+15,y+106),info['label'],cw-28,F(11,True),info['color']); ell(d,(x+15,y+129),q['label'],cw-28,F(10),'#475569')
    else:
        d.rounded_rectangle((cx0,y0+88,2678,y0+352),radius=13,fill='#F1F5F9',outline='#CBD5E1',width=2); d.text((cx0+32,y0+142),'SEMANTIC ANALYSIS PENDING',font=F(23,True),fill='#64748B'); d.text((cx0+32,y0+188),'Screenshot included. Add JSON to unlock crops, structure and statistics.',font=F(15),fill='#475569')
    sx=2710; sy=y0+72; d.text((sx,sy),'STRUCTURE CODE',font=F(15,True),fill='#111827'); sy+=29
    if sec:
        for q in sec[:11]:
            info=tax[q['type']]; d.rounded_rectangle((sx,sy,sx+500,sy+27),radius=5,fill=info['color']); ell(d,(sx+8,sy+6),info['label'],482,F(10),'white'); sy+=32
    else: d.text((sx,sy),'Pending JSON',font=F(13),fill='#94A3B8')
    tx=3240; ty=y0+72; d.text((tx,ty),'PAGE FLOW',font=F(15,True),fill='#111827'); ty+=30
    if sec:
        for a,b in zip(sec,sec[1:]):
            ell(d,(tx,ty),tax[a['type']]['label']+' → '+tax[b['type']]['label'],715,F(10),'#334155'); ty+=24
            if ty>y0+rh-20: break
    else: d.text((tx,ty),'Pending semantic analysis',font=F(12),fill='#94A3B8')
    im.close()

def global_panel(d,sums,tax):
    x,y,w=4005,28,955; total=sum(s['reference_site_count'] for s in sums); analyzed=sum(s['analyzed_site_count'] for s in sums); pres=Counter(); tr=Counter()
    for s in sums:
        pres.update(s['site_presence'])
        for z in s['transitions']: tr[(z['from'],z['to'])]+=z['count']
    d.rounded_rectangle((x,y,x+w,y+1490),radius=18,fill='#F1F5F9',outline='#CBD5E1',width=2); d.text((x+27,y+24),'ALL RESEARCH · SUMMARY',font=F(22,True),fill='#111827'); d.text((x+27,y+64),f'{total} screenshots in inventory',font=F(15),fill='#334155'); d.text((x+27,y+91),f'{analyzed} analyzed · {total-analyzed} pending',font=F(15),fill='#334155'); yy=y+140; d.text((x+27,yy),'COHORT COVERAGE',font=F(15,True),fill='#111827'); yy+=30
    for s in sums:
        ell(d,(x+27,yy),f'{s["name"]}: {s["analyzed_site_count"]}/{s["reference_site_count"]} analyzed',w-54,F(12),'#334155'); yy+=25
    yy+=16; d.text((x+27,yy),'MOST COMMON SECTIONS',font=F(15,True),fill='#111827'); yy+=29
    for typ,n in pres.most_common(12):
        if typ=='capture_partial': continue
        ell(d,(x+27,yy),tax.get(typ,{}).get('label',typ),w-120,F(11),'#334155'); d.text((x+w-28,yy),str(n),font=F(11,True),fill='#111827',anchor='ra'); yy+=22
    yy+=16; d.text((x+27,yy),'MOST COMMON TRANSITIONS',font=F(15,True),fill='#111827'); yy+=29
    for (a,b),n in tr.most_common(12):
        ell(d,(x+27,yy),tax.get(a,{}).get('label',a)+' → '+tax.get(b,{}).get('label',b),w-115,F(10),'#334155'); d.text((x+w-28,yy),str(n),font=F(10,True),fill='#111827',anchor='ra'); yy+=21
    yy+=18; d.text((x+27,yy),'NOTE',font=F(15,True),fill='#111827'); yy+=28; d.text((x+27,yy),'Percentages use analyzed sites only.',font=F(11),fill='#64748B'); d.text((x+27,yy+22),'Pending screenshots remain visible.',font=F(11),fill='#64748B')

def render(items,title,path,tax,sums=None,cohort_label=False):
    W=5000; H0=205; RH=430; H=H0+RH*len(items)+35; c=Image.new('RGB',(W,H),'white'); d=ImageDraw.Draw(c); d.text((35,28),title.upper(),font=F(36,True),fill='#111827'); analyzed=sum(x['analysis_status']=='analyzed' for x in items); d.text((35,80),f'{len(items)} screenshots visible · {analyzed} analyzed · {len(items)-analyzed} pending',font=F(19),fill='#475569'); d.text((35,114),'Screenshot → semantic crops → structure code → page flow',font=F(16),fill='#64748B')
    for i,item in enumerate(items): row(c,d,item,tax,H0+i*RH,RH,cohort_label)
    if sums: global_panel(d,sums,tax)
    c.save(path,'JPEG',quality=70,optimize=True,progressive=True); c.close()

def write_files(cohort,s):
    G.mkdir(parents=True,exist_ok=True); cid=cohort['id']; (G/f'{cid}-summary.json').write_text(json.dumps(s,indent=2),encoding='utf-8')
    with (G/f'{cid}-transitions.csv').open('w',newline='',encoding='utf-8') as f:
        w=csv.writer(f); w.writerow(['from','to','count']); [w.writerow([z['from'],z['to'],z['count']]) for z in s['transitions']]

def pct(n,d): return f'{round(n/d*100)}%' if d else 'n/a'
def readme_block(sums,tax):
    total=sum(s['reference_site_count'] for s in sums); analyzed=sum(s['analyzed_site_count'] for s in sums); L=[START,'','## Website Pattern Research','', '> Auto-generated from screenshot inventory + semantic JSON. Screenshots remain visible even when analysis is pending.','',f'**{total} reference screenshots tracked · {analyzed} semantically analyzed · {total-analyzed} pending**','', '[Open the all-reference atlas](./research/website-patterns/generated/all-reference-atlas.jpg) · [All cohort summaries](./research/website-patterns/generated/all-cohorts-summary.json)','', '[![All website research atlas](./research/website-patterns/generated/all-reference-atlas.jpg)](./research/website-patterns/generated/all-reference-atlas.jpg)','','### Analysis coverage','','| Cohort | References | Analyzed | Pending |','| --- | ---: | ---: | ---: |']
    for s in sums: L.append(f'| {s["name"]} | {s["reference_site_count"]} | {s["analyzed_site_count"]} | {s["pending_site_count"]} |')
    L.append('')
    for s in sums:
        cid=s['cohort']; a=s['analyzed_site_count']; L += [f'### {s["name"]}','',f'**{s["reference_site_count"]} screenshots · {a} analyzed · {s["pending_site_count"]} pending**','',f'[Open cohort atlas](./research/website-patterns/generated/{cid}-atlas.jpg) · [Summary JSON](./research/website-patterns/generated/{cid}-summary.json) · [Transitions CSV](./research/website-patterns/generated/{cid}-transitions.csv)','']
        if a:
            L += ['| Pattern | Analyzed sites | Coverage of analyzed sites |','| --- | ---: | ---: |']
            for typ,n in sorted(s['site_presence'].items(),key=lambda z:(-z[1],tax.get(z[0],{}).get('label',z[0]))):
                if typ!='capture_partial': L.append(f'| {tax.get(typ,{}).get("label",typ)} | {n}/{a} | {pct(n,a)} |')
            L += ['','**Most common page-flow transitions among analyzed sites**','','| Transition | Count |','| --- | ---: |']
            for z in s['transitions'][:8]: L.append(f'| {tax.get(z["from"],{}).get("label",z["from"])} → {tax.get(z["to"],{}).get("label",z["to"])} | {z["count"]} |')
        else: L.append('_Semantic crop JSON is pending. The screenshots are already visible in the atlas._')
        L.append('')
    L += [END,'']; return '\n'.join(L)
def update_readme(sums,tax):
    block=readme_block(sums,tax); old=README.read_text(encoding='utf-8') if README.exists() else '# UI Ideas\n'
    if START in old and END in old:
        before,rest=old.split(START,1); _,after=rest.split(END,1); new=before.rstrip()+'\n\n'+block+after
    else:
        lines=old.splitlines(); new=(lines[0]+'\n\n'+block+'\n'.join(lines[1:]).lstrip()) if lines and lines[0].startswith('# ') else block+old.lstrip()
    README.write_text(new.rstrip()+'\n',encoding='utf-8')

def main():
    tax=J(R/'taxonomy.json')['section_types']; dirs=sorted(p for p in (R/'cohorts').iterdir() if p.is_dir() and (p/'cohort.json').exists()); sums=[]; all_items=[]; G.mkdir(parents=True,exist_ok=True)
    for cd in dirs:
        cohort,items=inventory(cd,tax); s=summary(cohort,items); sums.append(s); all_items.extend(items); write_files(cohort,s); render(items,cohort.get('name',cohort['id'])+' · Pattern Atlas',G/f'{cohort["id"]}-atlas.jpg',tax)
    render(all_items,'PNG + Telecom · All Website Research Atlas',G/'all-reference-atlas.jpg',tax,sums,True); (G/'all-cohorts-summary.json').write_text(json.dumps(sums,indent=2),encoding='utf-8'); update_readme(sums,tax); print(f'Tracked {len(all_items)} screenshots across {len(sums)} cohorts; {sum(s["analyzed_site_count"] for s in sums)} analyzed.')
if __name__=='__main__': main()
