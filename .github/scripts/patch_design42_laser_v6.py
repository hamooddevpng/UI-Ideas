from pathlib import Path
import json
import re
import xml.etree.ElementTree as ET

HTML = Path('42.html')
SVG = Path('assets/design42/png-admin1-national-light.svg')
html = HTML.read_text(encoding='utf-8')

old_css_marker = '/* Design 42: province laser network v5 */'
if old_css_marker in html:
    before, tail = html.split(old_css_marker, 1)
    if '</style>' in tail:
        _, after = tail.split('</style>', 1)
        html = before + '</style>' + after

old_js_marker = '// Design 42: province laser network v5'
if old_js_marker in html:
    pos = html.find(old_js_marker)
    start = html.rfind('<script', 0, pos)
    end = html.find('</script>', pos)
    if start != -1 and end != -1:
        html = html[:start] + html[end + len('</script>'):]

number = r'[-+]?(?:\d*\.\d+|\d+\.?)(?:[eE][-+]?\d+)?'
token_re = re.compile(r'[A-Za-z]|' + number)
arity = {'M':2,'L':2,'H':1,'V':1,'C':6,'S':4,'Q':4,'T':2,'A':7}

def parse_subpaths(d):
    toks = token_re.findall(d or '')
    i = 0
    cmd = None
    x = y = sx = sy = 0.0
    sub = []
    subs = []
    def finish():
        nonlocal sub
        if len(sub) >= 3:
            clean = [sub[0]]
            for p in sub[1:]:
                if abs(p[0]-clean[-1][0]) > 1e-8 or abs(p[1]-clean[-1][1]) > 1e-8:
                    clean.append(p)
            if len(clean) >= 3:
                subs.append(clean)
        sub = []
    while i < len(toks):
        if toks[i].isalpha():
            cmd = toks[i]
            i += 1
            if cmd in 'Zz':
                if sub:
                    if abs(sub[-1][0]-sx) > 1e-8 or abs(sub[-1][1]-sy) > 1e-8:
                        sub.append((sx, sy))
                    finish()
                x, y = sx, sy
                cmd = None
                continue
        if not cmd:
            continue
        up = cmd.upper()
        rel = cmd.islower()
        if up not in arity:
            raise ValueError(f'Unsupported SVG path command: {cmd}')
        if up == 'M':
            if i + 2 > len(toks):
                break
            nx, ny = float(toks[i]), float(toks[i+1])
            i += 2
            if rel:
                nx += x; ny += y
            finish()
            x, y = nx, ny
            sx, sy = x, y
            sub = [(x, y)]
            cmd = 'l' if rel else 'L'
            continue
        n = arity[up]
        if i + n > len(toks):
            break
        vals = list(map(float, toks[i:i+n]))
        i += n
        ox, oy = x, y
        if up == 'L':
            nx, ny = vals[0], vals[1]
            if rel: nx += ox; ny += oy
        elif up == 'H':
            nx, ny = vals[0] + (ox if rel else 0), oy
        elif up == 'V':
            nx, ny = ox, vals[0] + (oy if rel else 0)
        elif up == 'C':
            nx, ny = vals[4], vals[5]
            if rel: nx += ox; ny += oy
        elif up == 'S':
            nx, ny = vals[2], vals[3]
            if rel: nx += ox; ny += oy
        elif up == 'Q':
            nx, ny = vals[2], vals[3]
            if rel: nx += ox; ny += oy
        elif up == 'T':
            nx, ny = vals[0], vals[1]
            if rel: nx += ox; ny += oy
        elif up == 'A':
            nx, ny = vals[5], vals[6]
            if rel: nx += ox; ny += oy
        x, y = nx, ny
        if not sub:
            sx, sy = x, y
            sub = [(x, y)]
        else:
            sub.append((x, y))
    finish()
    return subs

def signed_area(poly):
    return 0.5 * sum(poly[i][0]*poly[(i+1)%len(poly)][1] - poly[(i+1)%len(poly)][0]*poly[i][1] for i in range(len(poly)))

def centroid(poly):
    s = cx = cy = 0.0
    for i in range(len(poly)):
        x1,y1 = poly[i]; x2,y2 = poly[(i+1)%len(poly)]
        c = x1*y2 - x2*y1
        s += c; cx += (x1+x2)*c; cy += (y1+y2)*c
    if abs(s) < 1e-9:
        return (sum(x for x,_ in poly)/len(poly), sum(y for _,y in poly)/len(poly))
    return (cx/(3*s), cy/(3*s))

def inside(p, poly):
    px,py = p; hit=False; j=len(poly)-1
    for i in range(len(poly)):
        xi,yi=poly[i]; xj,yj=poly[j]
        if (yi>py)!=(yj>py):
            xcross=(xj-xi)*(py-yi)/((yj-yi) or 1e-12)+xi
            if px<xcross: hit=not hit
        j=i
    return hit

def seg_dist2(p,a,b):
    px,py=p; ax,ay=a; bx,by=b; dx=bx-ax; dy=by-ay
    if dx==0 and dy==0: return (px-ax)**2+(py-ay)**2
    t=max(0.0,min(1.0,((px-ax)*dx+(py-ay)*dy)/(dx*dx+dy*dy)))
    qx,qy=ax+t*dx,ay+t*dy
    return (px-qx)**2+(py-qy)**2

def interior_anchor(poly):
    xs=[x for x,_ in poly]; ys=[y for _,y in poly]
    minx,maxx,miny,maxy=min(xs),max(xs),min(ys),max(ys)
    for p in (centroid(poly),((minx+maxx)/2,(miny+maxy)/2)):
        if inside(p,poly): return p
    best=None; best_score=-1.0; steps=32
    for gy in range(1,steps):
        py=miny+(maxy-miny)*gy/steps
        for gx in range(1,steps):
            px=minx+(maxx-minx)*gx/steps; p=(px,py)
            if not inside(p,poly): continue
            score=min(seg_dist2(p,poly[k],poly[(k+1)%len(poly)]) for k in range(len(poly)))
            if score>best_score: best,best_score=p,score
    return best or ((minx+maxx)/2,(miny+maxy)/2)

root = ET.fromstring(SVG.read_text(encoding='utf-8'))
anchors=[]
for el in root.iter():
    if not el.tag.endswith('path'): continue
    pid,name,d=el.attrib.get('id'),el.attrib.get('name'),el.attrib.get('d')
    if not pid or not name or not d: continue
    subs=[p for p in parse_subpaths(d) if abs(signed_area(p))>1e-5]
    if not subs: continue
    mainland=max(subs,key=lambda p:abs(signed_area(p)))
    x,y=interior_anchor(mainland)
    anchors.append({'id':pid,'name':name,'x':round(x,1),'y':round(y,1)})

print(f'Province anchors derived: {len(anchors)}')
for a in anchors: print(a)
assert len(anchors)==22, f'Expected 22 province anchors, got {len(anchors)}'
anchors_json=json.dumps(anchors,ensure_ascii=False,separators=(',',':'))

css=r'''
/* Design 42: static province laser network v6 */
.national-story-map #nationalMeshLinks,.national-story-map #nationalMeshPackets,.national-story-map #nationalMeshNodes,.national-story-map #nationalPointerLasers{opacity:0!important}
.province-network-v6{pointer-events:none}
.province-route-glow-v6,.province-route-v6,.province-shot-glow-v6,.province-shot-core-v6{fill:none;stroke-linecap:round;stroke-linejoin:round;vector-effect:non-scaling-stroke}
.province-route-glow-v6{stroke:#4acbf3;stroke-width:7;opacity:.11;filter:url(#nationalLaserGlow)}
.province-route-v6{stroke:#0f8fc7;stroke-width:2.2;opacity:.62;stroke-dasharray:5 5;filter:drop-shadow(0 0 2px rgba(8,117,201,.34))}
.province-node-v6 .halo{fill:rgba(13,170,226,.13);stroke:#2bb6e7;stroke-width:1.4;vector-effect:non-scaling-stroke;opacity:.94}
.province-node-v6 .dot{fill:#0875c9;stroke:#fff;stroke-width:2.25;vector-effect:non-scaling-stroke;filter:url(#nationalLaserGlow)}
.province-node-v6.live .halo{fill:rgba(20,190,239,.24);stroke:#08aee8;stroke-width:2}
.province-node-v6.live .dot{fill:#05b8ed}
.province-shot-glow-v6{stroke:#00baf4;stroke-width:10;opacity:0;filter:blur(2.4px) drop-shadow(0 0 12px rgba(0,174,240,.9));stroke-dasharray:.13 .87;stroke-dashoffset:1}
.province-shot-core-v6{stroke:#fff;stroke-width:3.2;opacity:0;filter:drop-shadow(0 0 5px #33d7ff) drop-shadow(0 0 9px #0875c9);stroke-dasharray:.13 .87;stroke-dashoffset:1}
.province-impact-v6{fill:none;stroke:#05aee8;stroke-width:2.6;vector-effect:non-scaling-stroke;filter:url(#nationalLaserGlow)}
.province-impact-dot-v6{fill:#fff;stroke:#0875c9;stroke-width:2;vector-effect:non-scaling-stroke;filter:url(#nationalLaserGlow)}
@media(prefers-reduced-motion:reduce){.province-route-v6{opacity:.65!important}.province-shot-glow-v6,.province-shot-core-v6,.province-impact-v6,.province-impact-dot-v6{display:none!important}}
'''

js=r'''
<script>
// Design 42: static province laser network v6
(()=>{
  const section=document.querySelector('.national-story-map');
  const overlay=document.getElementById('nationalProvinceOverlay');
  if(!section||!overlay||document.getElementById('provinceNetworkV6'))return;
  const NS='http://www.w3.org/2000/svg';
  const points=__ANCHORS__;
  const reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
  const make=(tag,attrs={})=>{const el=document.createElementNS(NS,tag);Object.entries(attrs).forEach(([k,v])=>el.setAttribute(k,String(v)));return el};
  const dist=(a,b)=>Math.hypot(a.x-b.x,a.y-b.y);
  const key=(a,b)=>a<b?`${a}-${b}`:`${b}-${a}`;
  const buildEdges=()=>{
    const edges=[],keys=new Set(),used=new Set([0]);
    while(used.size<points.length){let best=null;used.forEach(a=>points.forEach((_,b)=>{if(used.has(b))return;const d=dist(points[a],points[b]);if(!best||d<best.d)best={a,b,d}}));if(!best)break;edges.push(best);keys.add(key(best.a,best.b));used.add(best.b)}
    const extras=[];points.forEach((p,a)=>{const near=points.map((q,b)=>({a,b,d:dist(p,q)})).filter(e=>e.b!==a).sort((x,y)=>x.d-y.d);for(const e of near.slice(0,2)){const k=key(e.a,e.b);if(!keys.has(k)&&e.d<185){extras.push(e);keys.add(k);break}}});
    extras.sort((a,b)=>a.d-b.d);return edges.concat(extras.slice(0,8));
  };
  const routeD=(a,b,index)=>{const dx=b.x-a.x,dy=b.y-a.y,len=Math.max(1,Math.hypot(dx,dy)),nx=-dy/len,ny=dx/len,bend=Math.min(17,Math.max(4,len*.025))*(index%2?1:-1),mx=(a.x+b.x)/2+nx*bend,my=(a.y+b.y)/2+ny*bend;return `M ${a.x} ${a.y} Q ${mx.toFixed(1)} ${my.toFixed(1)} ${b.x} ${b.y}`};
  const layer=make('g',{id:'provinceNetworkV6',class:'province-network-v6'}),under=make('g'),routes=make('g'),shots=make('g'),nodes=make('g');layer.append(under,routes,shots,nodes);overlay.appendChild(layer);
  const edges=buildEdges().map((e,i)=>({...e,path:routeD(points[e.a],points[e.b],i)}));
  edges.forEach(e=>{under.appendChild(make('path',{class:'province-route-glow-v6',d:e.path}));routes.appendChild(make('path',{class:'province-route-v6',d:e.path}))});
  const nodeEls=points.map(p=>{const g=make('g',{class:'province-node-v6','data-province':p.name,transform:`translate(${p.x} ${p.y})`});g.append(make('circle',{class:'halo',r:'9'}),make('circle',{class:'dot',r:'4.5'}));nodes.appendChild(g);return g});
  if(reduce)return;
  let visible=true;if('IntersectionObserver'in window){visible=false;new IntersectionObserver(([entry])=>{visible=entry.isIntersecting},{threshold:.05}).observe(section)}
  const animatePath=(el,dur)=>el.animate([{strokeDashoffset:'1',opacity:0,offset:0},{strokeDashoffset:'.82',opacity:1,offset:.08},{strokeDashoffset:'-.03',opacity:1,offset:.88},{strokeDashoffset:'-.17',opacity:0,offset:1}],{duration:dur,easing:'cubic-bezier(.18,.72,.2,1)',fill:'forwards'});
  const fire=()=>{if(!visible||document.hidden||!edges.length)return;const ei=Math.floor(Math.random()*edges.length),e=edges[ei],forward=Math.random()>.5,fromIndex=forward?e.a:e.b,toIndex=forward?e.b:e.a,from=points[fromIndex],to=points[toIndex],d=forward?e.path:routeD(from,to,ei+1),dur=1150+Math.random()*420,glow=make('path',{class:'province-shot-glow-v6',d,pathLength:'1'}),core=make('path',{class:'province-shot-core-v6',d,pathLength:'1'});shots.append(glow,core);nodeEls[fromIndex].classList.add('live');animatePath(glow,dur);animatePath(core,dur);setTimeout(()=>{nodeEls[toIndex].classList.add('live');const ring=make('circle',{class:'province-impact-v6',cx:to.x,cy:to.y,r:'4'}),dot=make('circle',{class:'province-impact-dot-v6',cx:to.x,cy:to.y,r:'5'});shots.append(ring,dot);ring.animate([{r:4,opacity:1},{r:23,opacity:0}],{duration:720,easing:'ease-out',fill:'forwards'});dot.animate([{r:5,opacity:1},{r:2.5,opacity:0}],{duration:720,easing:'ease-out',fill:'forwards'});setTimeout(()=>{ring.remove();dot.remove();nodeEls[toIndex].classList.remove('live')},760)},dur*.78);setTimeout(()=>{glow.remove();core.remove();nodeEls[fromIndex].classList.remove('live')},dur+120)};
  const tick=()=>{if(visible&&!document.hidden){fire();if(Math.random()>.45)setTimeout(fire,260)}setTimeout(tick,900+Math.random()*620)};setTimeout(()=>{fire();setTimeout(fire,320);tick()},300);
})();
</script>
'''.replace('__ANCHORS__',anchors_json)

html=html.replace('</style>',css+'\n</style>',1)
html=html.replace('</body>',js+'\n</body>',1)
HTML.write_text(html,encoding='utf-8')

for p in [Path('.github/workflows/design42-laser-static-v6.yml'),Path('.github/scripts/patch_design42_laser_v6.py')]:
    if p.exists(): p.unlink()
