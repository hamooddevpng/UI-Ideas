#!/usr/bin/env python3
import csv, json, statistics
from collections import Counter, defaultdict
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT=Path(__file__).resolve().parents[1]
R=ROOT/'research/website-patterns'; G=R/'generated'; README=ROOT/'README.md'
START='<!-- WEBSITE_PATTERN_RESEARCH_START -->'; END='<!-- WEBSITE_PATTERN_RESEARCH_END -->'
SUCCESS={'ok','success','captured','complete'}

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
def pct_num(n,d): return round(n/d*100) if d else 0
def pct(n,d): return f'{pct_num(n,d)}%' if d else 'n/a'
def clean_seq(sections):
    seq=[]
    for q in sections:
        typ=q['type']
        if typ=='capture_partial': continue
        if not seq or seq[-1]!=typ: seq.append(typ)
    return seq

def metadata(cohort):
    root=ROOT/cohort['source_root']; name=cohort.get('metadata_file')
    if not name and (root/'capture-results.json').exists(): name='capture-results.json'
    if not name or not (root/name).exists(): return {},{}
    data=J(root/name)
    results={x['slug']:x for x in data.get('results',[]) if x.get('slug')}
    excluded={x['slug']:x.get('reason','Excluded by capture curation') for x in data.get('excluded',[]) if x.get('slug')}
    return results,excluded

def source_for(root,slug,s,m):
    candidates=[]
    if s and s.get('source_repo_path'): candidates.append(ROOT/s['source_repo_path'])
    candidates.append(root/f'{slug}.png')
    if m and m.get('researchFilename'): candidates.append(root/m['researchFilename'])
    for p in candidates:
        if p.exists(): return p
    return None

def exclusion_reason(slug,s,m,curated_excluded,src):
    if slug in curated_excluded: return curated_excluded[slug]
    if src is None: return 'No usable screenshot file'
    mstatus=str((m or {}).get('status','')).strip().lower()
    if mstatus and mstatus not in SUCCESS: return f'Capture metadata status: {mstatus}'
    sstatus=str((s or {}).get('capture_status','')).strip().lower()
    if sstatus and sstatus not in SUCCESS: return f'Semantic capture status: {sstatus}'
    if s and any(q.get('type')=='capture_partial' for q in s.get('sections',[])): return 'Semantic review marked screenshot as partial / unreliable'
    return None

def inventory(cd,tax):
    cohort=J(cd/'cohort.json'); root=ROOT/cohort['source_root']; meta,curated_excluded=metadata(cohort); semantic={}
    if (cd/'sites').exists():
        for p in sorted((cd/'sites').glob('*.json')):
            s=J(p)['site']; last=-1
            for q in s.get('sections',[]):
                if q['type'] not in tax: raise SystemExit(f'{p}: unknown type {q["type"]}')
                b=q['bounds_normalized']
                if not(0<=b['x']<=1 and 0<=b['y']<=1 and 0<b['width']<=1 and 0<b['height']<=1 and b['x']+b['width']<=1.0001 and b['y']+b['height']<=1.0001 and b['y']>=last): raise SystemExit(f'{p}: invalid bounds')
                last=b['y']
            semantic[s['slug']]=s

    slugs=set(cohort.get('sites',[]))|set(meta)|set(semantic)|set(curated_excluded)
    if not slugs:
        slugs={p.stem for p in root.glob('*.png')}

    out=[]; excluded=[]
    for slug in sorted(slugs):
        s=semantic.get(slug); m=meta.get(slug,{})
        src=source_for(root,slug,s,m)
        reason=exclusion_reason(slug,s,m,curated_excluded,src)
        name=s.get('name') if s else m.get('name') or slug.replace('-',' ').title()
        url=s.get('url') if s else m.get('url') or m.get('requestedUrl') or m.get('finalUrl') or ''
        if reason:
            excluded.append({'slug':slug,'name':name,'url':url,'reason':reason})
            continue
        sections=s.get('sections',[]) if s else []
        out.append({'slug':slug,'name':name,'url':url,'source':src,'sections':sections,'analysis_status':'analyzed' if sections else 'pending','cohort_id':cohort['id'],'cohort_name':cohort.get('name',cohort['id'])})
    return cohort,out,excluded

def positional_patterns(analyzed):
    by_pos=defaultdict(Counter)
    for x in analyzed:
        for i,typ in enumerate(clean_seq(x['sections'])): by_pos[i][typ]+=1
    out=[]
    n=len(analyzed)
    for pos in sorted(by_pos):
        candidates=[{'type':typ,'count':count,'coverage_pct':pct_num(count,n)} for typ,count in by_pos[pos].most_common()]
        out.append({'position':pos+1,'candidates':candidates})
    return out

def summary(cohort,items,excluded):
    analyzed=[x for x in items if x['analysis_status']=='analyzed']; sc=Counter(); pres=Counter(); tr=Counter()
    for x in analyzed:
        seq=clean_seq(x['sections']); sc.update(seq); pres.update(set(seq)); tr.update(zip(seq,seq[1:]))
    pos=positional_patterns(analyzed)
    rec=[{'position':p['position'],**p['candidates'][0]} for p in pos if p['candidates']]
    return {
        'cohort':cohort['id'],'name':cohort.get('name',cohort['id']),
        'candidate_site_count':len(items)+len(excluded),'reference_site_count':len(items),'excluded_site_count':len(excluded),
        'excluded_sites':excluded,'analyzed_site_count':len(analyzed),'pending_site_count':len(items)-len(analyzed),
        'section_counts':dict(sc),'site_presence':dict(pres),
        'position_patterns':pos,'recommended_structure':rec,
        'transitions':[{'from':a,'to':b,'count':n} for (a,b),n in tr.most_common()]
    }

def balanced_recommendation(sums,tax):
    usable=[s for s in sums if s['analyzed_site_count']]
    total=sum(s['analyzed_site_count'] for s in usable)
    excluded=sum(s['excluded_site_count'] for s in sums)
    max_pos=max((len(s['position_patterns']) for s in usable),default=0)
    structure=[]
    for pos in range(1,max_pos+1):
        score=Counter(); raw=Counter()
        for s in usable:
            n=s['analyzed_site_count']
            p=next((x for x in s['position_patterns'] if x['position']==pos),None)
            if not p: continue
            for c in p['candidates']:
                score[c['type']]+=c['count']/n
                raw[c['type']]+=c['count']
        if not score: continue
        typ,_=score.most_common(1)[0]
        balanced=round(score[typ]/len(usable)*100)
        raw_count=raw[typ]
        raw_pct=pct_num(raw_count,total)
        if balanced<20: continue
        structure.append({
            'position':pos,'type':typ,'label':tax.get(typ,{}).get('label',typ),
            'balanced_cohort_support_pct':balanced,'raw_site_support_pct':raw_pct,
            'supporting_sites_at_position':raw_count,'eligible_analyzed_sites':total
        })

    footer_scores=[]; footer_raw=0
    for s in usable:
        n=s['analyzed_site_count']; c=s['site_presence'].get('footer',0)
        footer_scores.append(c/n); footer_raw+=c
    footer_bal=round(sum(footer_scores)/len(footer_scores)*100) if footer_scores else 0
    if footer_bal>=50 and not any(x['type']=='footer' for x in structure):
        structure.append({
            'position':len(structure)+1,'type':'footer','label':tax.get('footer',{}).get('label','Footer'),
            'balanced_cohort_support_pct':footer_bal,'raw_site_support_pct':pct_num(footer_raw,total),
            'supporting_sites_at_position':footer_raw,'eligible_analyzed_sites':total,'note':'Appended from strong site-presence consensus'
        })

    dedup=[]
    for x in structure:
        if dedup and dedup[-1]['type']==x['type']: continue
        dedup.append(x)
    foot=[x for x in dedup if x['type']=='footer']; dedup=[x for x in dedup if x['type']!='footer']
    if foot:
        f=max(foot,key=lambda x:x['balanced_cohort_support_pct']); dedup.append(f)
    for i,x in enumerate(dedup,1): x['position']=i

    presence=Counter()
    for s in usable:
        n=s['analyzed_site_count']
        for typ,count in s['site_presence'].items(): presence[typ]+=count/n
    optional=[]
    for typ,score in presence.items():
        if typ in {'capture_partial'} or any(x['type']==typ for x in dedup): continue
        bal=round(score/len(usable)*100)
        if bal>=25:
            optional.append({'type':typ,'label':tax.get(typ,{}).get('label',typ),'balanced_cohort_presence_pct':bal})
    optional.sort(key=lambda x:-x['balanced_cohort_presence_pct'])
    return {
        'method':'Equal-weight each cohort, then choose the most common section at each ordinal page position. Only clean, successful captures are eligible.',
        'eligible_analyzed_sites':total,'excluded_capture_sites':excluded,'cohort_count':len(usable),
        'final_structure':dedup,'optional_sections':optional
    }

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
        d.rounded_rectangle((cx0,y0+88,2678,y0+352),radius=13,fill='#F1F5F9',outline='#CBD5E1',width=2); d.text((cx0+32,y0+142),'SEMANTIC ANALYSIS PENDING',font=F(23,True),fill='#64748B'); d.text((cx0+32,y0+188),'Clean screenshot included. Add JSON to unlock crops, structure and statistics.',font=F(15),fill='#475569')
    sx=2710; sy=y0+72; d.text((sx,sy),'STRUCTURE CODE',font=F(15,True),fill='#111827'); sy+=29
    if sec:
        for q in sec[:11]:
            info=tax[q['type']]; d.rounded_rectangle((sx,sy,sx+500,sy+27),radius=5,fill=info['color']); ell(d,(sx+8,sy+6),info['label'],482,F(10),'white'); sy+=32
    else: d.text((sx,sy),'Pending JSON',font=F(13),fill='#94A3B8')
    tx=3240; ty=y0+72; d.text((tx,ty),'PAGE FLOW',font=F(15,True),fill='#111827'); ty+=30
    if sec:
        clean=[q for q in sec if q['type']!='capture_partial']
        for a,b in zip(clean,clean[1:]):
            ell(d,(tx,ty),tax[a['type']]['label']+' → '+tax[b['type']]['label'],715,F(10),'#334155'); ty+=24
            if ty>y0+rh-20: break
    else: d.text((tx,ty),'Pending semantic analysis',font=F(12),fill='#94A3B8')
    im.close()

def global_panel(d,sums,tax,recommendation):
    x,y,w=4005,28,955; total=sum(s['reference_site_count'] for s in sums); excluded=sum(s['excluded_site_count'] for s in sums); pres=Counter(); tr=Counter()
    for s in sums:
        pres.update(s['site_presence'])
        for z in s['transitions']: tr[(z['from'],z['to'])]+=z['count']
    d.rounded_rectangle((x,y,x+w,y+1800),radius=18,fill='#F1F5F9',outline='#CBD5E1',width=2); d.text((x+27,y+24),'ALL RESEARCH · SUMMARY',font=F(22,True),fill='#111827'); d.text((x+27,y+64),f'{total} clean screenshots included',font=F(15),fill='#334155'); d.text((x+27,y+91),f'{excluded} failed / partial captures excluded',font=F(15),fill='#334155')
    yy=y+140; d.text((x+27,yy),'RECOMMENDED FINAL STRUCTURE',font=F(15,True),fill='#111827'); yy+=34
    for z in recommendation['final_structure'][:11]:
        info=tax.get(z['type'],{'color':'#64748B','label':z['type']})
        d.rounded_rectangle((x+27,yy,x+w-27,yy+34),radius=6,fill=info['color'])
        ell(d,(x+38,yy+8),f'{z["position"]}. {info["label"]}',w-235,F(11,True),'white')
        d.text((x+w-40,yy+8),f'{z["balanced_cohort_support_pct"]}%',font=F(11,True),fill='white',anchor='ra'); yy+=40
    yy+=16; d.text((x+27,yy),'COHORT COVERAGE',font=F(15,True),fill='#111827'); yy+=30
    for s in sums:
        ell(d,(x+27,yy),f'{s["name"]}: {s["analyzed_site_count"]} analyzed, {s["excluded_site_count"]} excluded',w-54,F(11),'#334155'); yy+=24
    yy+=14; d.text((x+27,yy),'MOST COMMON SECTIONS',font=F(15,True),fill='#111827'); yy+=29
    for typ,n in pres.most_common(8):
        if typ=='capture_partial': continue
        ell(d,(x+27,yy),tax.get(typ,{}).get('label',typ),w-120,F(11),'#334155'); d.text((x+w-28,yy),str(n),font=F(11,True),fill='#111827',anchor='ra'); yy+=22
    yy+=14; d.text((x+27,yy),'MOST COMMON TRANSITIONS',font=F(15,True),fill='#111827'); yy+=29
    for (a,b),n in tr.most_common(8):
        ell(d,(x+27,yy),tax.get(a,{}).get('label',a)+' → '+tax.get(b,{}).get('label',b),w-115,F(10),'#334155'); d.text((x+w-28,yy),str(n),font=F(10,True),fill='#111827',anchor='ra'); yy+=21
    yy+=18; d.text((x+27,yy),'METHOD',font=F(15,True),fill='#111827'); yy+=28
    d.text((x+27,yy),'Final structure uses equal cohort weighting.',font=F(10),fill='#64748B'); d.text((x+27,yy+20),'Failed, partial, blocked or unreliable captures are excluded.',font=F(10),fill='#64748B')

def render(items,title,path,tax,sums=None,recommendation=None,cohort_label=False):
    W=5000; H0=205; RH=430; H=max(H0+RH*len(items)+35,1900 if sums else 0); c=Image.new('RGB',(W,H),'white'); d=ImageDraw.Draw(c); d.text((35,28),title.upper(),font=F(36,True),fill='#111827'); analyzed=sum(x['analysis_status']=='analyzed' for x in items); d.text((35,80),f'{len(items)} clean screenshots visible · {analyzed} analyzed · {len(items)-analyzed} pending',font=F(19),fill='#475569'); d.text((35,114),'Screenshot → semantic crops → structure code → page flow → consensus structure',font=F(16),fill='#64748B')
    for i,item in enumerate(items): row(c,d,item,tax,H0+i*RH,RH,cohort_label)
    if sums and recommendation: global_panel(d,sums,tax,recommendation)
    c.save(path,'JPEG',quality=70,optimize=True,progressive=True); c.close()

def write_files(cohort,s):
    G.mkdir(parents=True,exist_ok=True); cid=cohort['id']; (G/f'{cid}-summary.json').write_text(json.dumps(s,indent=2),encoding='utf-8')
    with (G/f'{cid}-transitions.csv').open('w',newline='',encoding='utf-8') as f:
        w=csv.writer(f); w.writerow(['from','to','count']); [w.writerow([z['from'],z['to'],z['count']]) for z in s['transitions']]
    with (G/f'{cid}-recommended-structure.csv').open('w',newline='',encoding='utf-8') as f:
        w=csv.writer(f); w.writerow(['position','type','coverage_pct','count']); [w.writerow([z['position'],z['type'],z['coverage_pct'],z['count']]) for z in s['recommended_structure']]

def readme_block(sums,tax,recommendation):
    total=sum(s['reference_site_count'] for s in sums); analyzed=sum(s['analyzed_site_count'] for s in sums); excluded=sum(s['excluded_site_count'] for s in sums)
    L=[START,'','## Website Pattern Research','', '> Auto-generated from clean screenshot inventory + semantic JSON. Failed, partial, blocked and unreliable captures are excluded from the atlas, statistics and recommendations.','',f'**{total} clean reference screenshots tracked · {analyzed} semantically analyzed · {excluded} captures excluded**','', '[Open the all-reference atlas](./research/website-patterns/generated/all-reference-atlas.jpg) · [Final structure recommendation](./research/website-patterns/generated/final-structure-recommendation.json) · [All cohort summaries](./research/website-patterns/generated/all-cohorts-summary.json)','', '[![All website research atlas](./research/website-patterns/generated/all-reference-atlas.jpg)](./research/website-patterns/generated/all-reference-atlas.jpg)','','### Recommended final page structure','', 'This is a cohort-balanced consensus, so the much larger PNG private-sector cohort does not drown out the telecom or public-service cohorts.','', '| Order | Section | Cohort-balanced support | Raw site support |','| ---: | --- | ---: | ---: |']
    for z in recommendation['final_structure']:
        L.append(f'| {z["position"]} | {z["label"]} | {z["balanced_cohort_support_pct"]}% | {z["raw_site_support_pct"]}% |')
    if recommendation['optional_sections']:
        L += ['','**Optional / secondary sections seen often enough to consider**','', '| Section | Cohort-balanced presence |','| --- | ---: |']
        for z in recommendation['optional_sections'][:10]: L.append(f'| {z["label"]} | {z["balanced_cohort_presence_pct"]}% |')
    L += ['','### Analysis coverage','','| Cohort | Candidates | Included clean captures | Excluded captures | Analyzed | Pending |','| --- | ---: | ---: | ---: | ---: | ---: |']
    for s in sums: L.append(f'| {s["name"]} | {s["candidate_site_count"]} | {s["reference_site_count"]} | {s["excluded_site_count"]} | {s["analyzed_site_count"]} | {s["pending_site_count"]} |')
    L.append('')
    for s in sums:
        cid=s['cohort']; a=s['analyzed_site_count']; L += [f'### {s["name"]}','',f'**{s["reference_site_count"]} clean screenshots · {a} analyzed · {s["excluded_site_count"]} excluded · {s["pending_site_count"]} pending**','',f'[Open cohort atlas](./research/website-patterns/generated/{cid}-atlas.jpg) · [Summary JSON](./research/website-patterns/generated/{cid}-summary.json) · [Recommended structure CSV](./research/website-patterns/generated/{cid}-recommended-structure.csv) · [Transitions CSV](./research/website-patterns/generated/{cid}-transitions.csv)','']
        if a:
            L += ['**Most common section at each page position**','', '| Position | Suggested section | Sites at this exact position |','| ---: | --- | ---: |']
            for z in s['recommended_structure'][:12]: L.append(f'| {z["position"]} | {tax.get(z["type"],{}).get("label",z["type"])} | {z["count"]}/{a} ({z["coverage_pct"]}%) |')
            L += ['','**Section presence across clean analyzed sites**','', '| Pattern | Analyzed sites | Coverage |','| --- | ---: | ---: |']
            for typ,n in sorted(s['site_presence'].items(),key=lambda z:(-z[1],tax.get(z[0],{}).get('label',z[0]))):
                if typ!='capture_partial': L.append(f'| {tax.get(typ,{}).get("label",typ)} | {n}/{a} | {pct(n,a)} |')
            L += ['','**Most common page-flow transitions**','','| Transition | Count |','| --- | ---: |']
            for z in s['transitions'][:8]: L.append(f'| {tax.get(z["from"],{}).get("label",z["from"])} → {tax.get(z["to"],{}).get("label",z["to"])} | {z["count"]} |')
        else: L.append('_No clean semantically analyzed screenshots are currently available for this cohort._')
        if s['excluded_sites']:
            L += ['','**Excluded capture attempts**','', '| Site | Reason |','| --- | --- |']
            for z in s['excluded_sites']: L.append(f'| {z["name"]} | {z["reason"]} |')
        L.append('')
    L += [END,'']; return '\n'.join(L)

def update_readme(sums,tax,recommendation):
    block=readme_block(sums,tax,recommendation); old=README.read_text(encoding='utf-8') if README.exists() else '# UI Ideas\n'
    if START in old and END in old:
        before,rest=old.split(START,1); _,after=rest.split(END,1); new=before.rstrip()+'\n\n'+block+after
    else:
        lines=old.splitlines(); new=(lines[0]+'\n\n'+block+'\n'.join(lines[1:]).lstrip()) if lines and lines[0].startswith('# ') else block+old.lstrip()
    README.write_text(new.rstrip()+'\n',encoding='utf-8')

def main():
    tax=J(R/'taxonomy.json')['section_types']; dirs=sorted(p for p in (R/'cohorts').iterdir() if p.is_dir() and (p/'cohort.json').exists()); sums=[]; all_items=[]; G.mkdir(parents=True,exist_ok=True)
    for cd in dirs:
        cohort,items,excluded=inventory(cd,tax); s=summary(cohort,items,excluded); sums.append(s); all_items.extend(items); write_files(cohort,s); render(items,cohort.get('name',cohort['id'])+' · Pattern Atlas',G/f'{cohort["id"]}-atlas.jpg',tax)
    recommendation=balanced_recommendation(sums,tax)
    render(all_items,'PNG + Telecom · All Website Research Atlas',G/'all-reference-atlas.jpg',tax,sums,recommendation,True)
    (G/'all-cohorts-summary.json').write_text(json.dumps(sums,indent=2),encoding='utf-8')
    (G/'final-structure-recommendation.json').write_text(json.dumps(recommendation,indent=2),encoding='utf-8')
    update_readme(sums,tax,recommendation)
    print(f'Included {len(all_items)} clean screenshots across {len(sums)} cohorts; excluded {sum(s["excluded_site_count"] for s in sums)} failed/partial captures; {sum(s["analyzed_site_count"] for s in sums)} analyzed.')

if __name__=='__main__': main()
