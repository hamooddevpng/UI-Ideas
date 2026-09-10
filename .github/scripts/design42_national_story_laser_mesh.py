from pathlib import Path
import re

html_path=Path('42.html')
s=html_path.read_text()
marker='/* Design 42: province laser mesh */'
if marker in s:
    raise SystemExit('province laser mesh already installed')

# Create a National Story-only light variant of the verified 22-province SVG.
# Do not alter the original asset because the approved tower hero uses it.
src_path=Path('assets/design42/png-admin1-simplemaps.svg')
light_path=Path('assets/design42/png-admin1-national-light.svg')
svg=src_path.read_text()
light_style='<style id="telikom-map-theme">path,polygon{fill:#dff7fb!important;stroke:#78bfd2!important;stroke-width:.86!important;stroke-linejoin:round!important;vector-effect:non-scaling-stroke}</style>'
if 'id="telikom-map-theme"' in svg:
    svg=re.sub(r'<style id="telikom-map-theme">.*?</style>',light_style,svg,count=1,flags=re.S)
else:
    svg=svg.replace('<svg ', '<svg '+light_style+' ', 1)
light_path.write_text(svg)

old=re.compile(r'<aside class="national-map-card" id="nationalMapCard".*?</aside>',re.S)
new='''<aside class="national-map-card national-map-mesh" id="nationalMapCard" aria-label="Telikom national connectivity visual across Papua New Guinea's 22 provinces">
    <div class="national-map-head"><div><small>TELIKOM LTD · NATIONAL NETWORK</small><strong>All 22 provinces. One connected network.</strong></div><div class="national-map-counter"><b id="nationalMapCount">22 / 22</b><span>NETWORK LIVE</span></div></div>
    <div class="national-map-stage" id="nationalMapStage">
      <img class="national-map-backdrop" id="nationalMapBackdrop" src="assets/design42/png-admin1-national-light.svg" alt="Papua New Guinea map showing 22 province-level divisions" loading="lazy" decoding="async">
      <object class="national-map-source" id="nationalProvinceMap" type="image/svg+xml" data="assets/design42/png-admin1-national-light.svg" aria-hidden="true" tabindex="-1"></object>
      <svg class="national-map-overlay" id="nationalProvinceOverlay" viewBox="0 0 1000 589" preserveAspectRatio="xMidYMid meet" aria-hidden="true">
        <defs>
          <filter id="nationalLaserGlow" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="2.2" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
        </defs>
        <g id="nationalMeshLinks"></g>
        <g id="nationalMeshPackets"></g>
        <g id="nationalPointerLasers"></g>
        <g id="nationalProvinceNodes"></g>
        <circle class="national-pointer-core" id="nationalPointerCore" r="5" cx="500" cy="295"></circle>
      </svg>
    </div>
    <div class="national-map-foot"><span>22 PROVINCES · LIVE CONNECTIVITY VISUAL</span><span id="nationalMapState">MOVE ACROSS THE NETWORK</span></div>
  </aside>'''
s,n=old.subn(new,s,count=1)
if n!=1:
    raise SystemExit(f'national map markup replacement count {n}')

# Remove the previous sequential province animation script only.
pat=re.compile(r'\n<script>\s*;\(\(\)=>\{\s*const section=document\.getElementById\(\'png-story\'\),obj=document\.getElementById\(\'nationalProvinceMap\'\),overlay=document\.getElementById\(\'nationalProvinceOverlay\'\);.*?</script>\s*',re.S)
s,n=pat.subn('\n',s,count=1)
if n!=1:
    raise SystemExit(f'old national map script removal count {n}')

css=r'''

/* Design 42: province laser mesh */
.png-live .story-copy{padding-right:54%!important}
.national-map-mesh{
  background:linear-gradient(145deg,rgba(244,253,255,.94),rgba(226,247,250,.91))!important;
  border-color:rgba(111,192,213,.46)!important;
  box-shadow:0 30px 80px rgba(0,31,43,.20),inset 0 1px rgba(255,255,255,.85)!important;
}
.national-map-mesh:before{
  background-image:linear-gradient(rgba(21,126,158,.055) 1px,transparent 1px),linear-gradient(90deg,rgba(21,126,158,.055) 1px,transparent 1px)!important;
  background-size:34px 34px!important;
}
.national-map-mesh .national-map-head{color:#11384a}
.national-map-mesh .national-map-head small{color:#0875c9;font-size:6.8px}
.national-map-mesh .national-map-head strong{font-size:19px;color:#12384a}
.national-map-mesh .national-map-counter{border-color:rgba(20,128,161,.16);background:rgba(255,255,255,.62)}
.national-map-mesh .national-map-counter b{color:#12384a}
.national-map-mesh .national-map-counter span{color:#0a7fad}
.national-map-mesh .national-map-stage{left:14px;right:14px;top:66px;bottom:39px;overflow:hidden;border-radius:22px}
.national-map-backdrop{position:absolute;z-index:1;inset:3%;width:94%;height:94%;object-fit:contain;opacity:.92;filter:drop-shadow(0 12px 25px rgba(22,104,128,.10));pointer-events:none;user-select:none}
.national-map-source{position:absolute;z-index:-1;width:1px;height:1px;left:0;top:0;opacity:0;pointer-events:none;border:0}
.national-map-mesh .national-map-overlay{z-index:4;inset:3%;width:94%;height:94%;pointer-events:none;overflow:visible}
.national-mesh-link{fill:none;stroke:#26a9df;stroke-width:1.15;stroke-linecap:round;vector-effect:non-scaling-stroke;opacity:.30;stroke-dasharray:2 8;animation:nationalMeshFlow 2.8s linear infinite;filter:url(#nationalLaserGlow)}
.national-mesh-link.long{stroke:#0875c9;opacity:.20;stroke-dasharray:12 16;animation-duration:4.8s}
.national-mesh-link.surge{opacity:.88;stroke:#65d7ff;stroke-width:2.1;stroke-dasharray:10 6;animation-duration:.82s}
@keyframes nationalMeshFlow{to{stroke-dashoffset:-40}}
.national-mesh-node .node-halo{fill:rgba(37,169,223,.08);stroke:#53bfe7;stroke-width:1;vector-effect:non-scaling-stroke;opacity:.48}
.national-mesh-node .node-dot{fill:#0875c9;stroke:#e9fbff;stroke-width:1.8;vector-effect:non-scaling-stroke;filter:url(#nationalLaserGlow)}
.national-mesh-node.hot .node-halo{opacity:1;animation:nationalNodeBurst 1s ease-out infinite}
.national-mesh-node.hot .node-dot{fill:#16bced}
@keyframes nationalNodeBurst{to{r:16;opacity:0}}
.national-packet{fill:#fff;stroke:#25b6eb;stroke-width:1;filter:url(#nationalLaserGlow);opacity:.95}
.national-pointer-laser{stroke:#13bdf4;stroke-width:1.8;stroke-linecap:round;vector-effect:non-scaling-stroke;opacity:0;filter:url(#nationalLaserGlow);stroke-dasharray:7 5;transition:opacity .15s}
.national-pointer-laser.live{opacity:.88;animation:pointerLaserDash .58s linear infinite}
@keyframes pointerLaserDash{to{stroke-dashoffset:-24}}
.national-pointer-core{fill:#fff;stroke:#19b7ed;stroke-width:2;vector-effect:non-scaling-stroke;filter:url(#nationalLaserGlow);opacity:0;transition:opacity .14s}
.national-pointer-core.live{opacity:1}
.national-map-mesh .national-map-foot{color:#377084;font-size:6.5px}
.national-map-mesh .national-map-foot span:last-child{color:#0875c9}
.national-map-mesh:after{content:"";position:absolute;z-index:2;inset:62px 12px 34px;background:radial-gradient(260px circle at var(--national-x,50%) var(--national-y,50%),rgba(68,202,242,.14),transparent 68%);pointer-events:none;opacity:.72}
@media(max-width:820px){
  .png-live .story-copy{padding-right:0!important}
  .national-map-mesh .national-map-stage{left:8px;right:8px;top:61px;bottom:37px}
  .national-map-mesh .national-map-overlay,.national-map-backdrop{inset:1%;width:98%;height:98%}
  .national-map-mesh .national-map-head strong{font-size:15px}
  .national-map-mesh .national-map-counter{min-width:70px;padding:8px}
  .national-mesh-link{stroke-width:1}
}
@media(prefers-reduced-motion:reduce){.national-mesh-link,.national-mesh-node.hot .node-halo,.national-pointer-laser.live{animation:none!important}}
'''
if '</style>' not in s:
    raise SystemExit('style close not found')
s=s.replace('</style>',css+'\n</style>',1)

js=r'''
<script>
;(()=>{
  const section=document.getElementById('png-story'),stage=document.getElementById('nationalMapStage'),obj=document.getElementById('nationalProvinceMap'),overlay=document.getElementById('nationalProvinceOverlay');
  const linksG=document.getElementById('nationalMeshLinks'),packetsG=document.getElementById('nationalMeshPackets'),pointerG=document.getElementById('nationalPointerLasers'),nodesG=document.getElementById('nationalProvinceNodes'),pointerCore=document.getElementById('nationalPointerCore'),state=document.getElementById('nationalMapState');
  if(!section||!stage||!obj||!overlay||!linksG||!packetsG||!pointerG||!nodesG)return;
  const NS='http://www.w3.org/2000/svg',reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
  let points=[],nodes=[],links=[],pointerLines=[],surgeTimer=null,built=false;
  const make=(tag,attrs={})=>{const el=document.createElementNS(NS,tag);Object.entries(attrs).forEach(([k,v])=>el.setAttribute(k,String(v)));return el};
  const dist=(a,b)=>Math.hypot(a.x-b.x,a.y-b.y);
  const build=()=>{
    if(built)return;
    let doc;try{doc=obj.contentDocument}catch(e){return}
    if(!doc)return;
    let raw=[...doc.querySelectorAll('#features > path, #features > polygon')].map(el=>{try{return {el,b:el.getBBox()}}catch(e){return null}}).filter(x=>x&&x.b.width>1&&x.b.height>1);
    raw=raw.sort((a,b)=>(b.b.width*b.b.height)-(a.b.width*a.b.height)).slice(0,22);
    if(raw.length<22)return;
    points=raw.map(({b},i)=>({i,x:b.x+b.width/2,y:b.y+b.height/2}));
    linksG.replaceChildren();packetsG.replaceChildren();nodesG.replaceChildren();pointerG.replaceChildren();links=[];nodes=[];pointerLines=[];
    const seen=new Set();
    points.forEach((p,i)=>{
      const nearest=points.filter((_,j)=>j!==i).sort((a,b)=>dist(p,a)-dist(p,b)).slice(0,2);
      nearest.forEach(q=>{
        const key=[i,q.i].sort((a,b)=>a-b).join('-');if(seen.has(key))return;seen.add(key);
        const path=make('path',{id:'nationalMeshLink'+links.length,class:'national-mesh-link',d:`M${p.x.toFixed(1)} ${p.y.toFixed(1)} L${q.x.toFixed(1)} ${q.y.toFixed(1)}`});
        path.style.animationDelay=(-links.length*.13)+'s';linksG.appendChild(path);links.push(path);
      });
    });
    // A handful of longer backbone links keeps island groups visually tied into the mesh.
    const farPairs=[[0,Math.floor(points.length*.45)],[3,14],[6,18],[9,20],[11,21]];
    farPairs.forEach(([a,b])=>{if(!points[a]||!points[b])return;const p=points[a],q=points[b];const path=make('path',{id:'nationalMeshLink'+links.length,class:'national-mesh-link long',d:`M${p.x.toFixed(1)} ${p.y.toFixed(1)} Q${((p.x+q.x)/2).toFixed(1)} ${((p.y+q.y)/2-28).toFixed(1)} ${q.x.toFixed(1)} ${q.y.toFixed(1)}`});linksG.appendChild(path);links.push(path)});
    points.forEach((p,i)=>{
      const g=make('g',{class:'national-mesh-node',transform:`translate(${p.x.toFixed(1)} ${p.y.toFixed(1)})`});
      g.append(make('circle',{class:'node-halo',r:'7'}),make('circle',{class:'node-dot',r:'3.6'}));nodesG.appendChild(g);nodes.push(g);
    });
    for(let i=0;i<4;i++){const line=make('line',{class:'national-pointer-laser',x1:'0',y1:'0',x2:'0',y2:'0'});pointerG.appendChild(line);pointerLines.push(line)}
    if(!reduce){
      links.slice(0,Math.min(12,links.length)).forEach((path,i)=>{
        const c=make('circle',{class:'national-packet',r:i%3===0?'3.3':'2.5'});const am=make('animateMotion',{dur:(3.4+(i%5)*.55)+'s',begin:(i*-.47)+'s',repeatCount:'indefinite'});const mp=make('mpath',{href:'#'+path.id});am.appendChild(mp);c.appendChild(am);packetsG.appendChild(c);
      });
      surgeTimer=setInterval(()=>{
        if(!section.matches(':hover')&&document.hidden)return;
        links.forEach(l=>l.classList.remove('surge'));nodes.forEach(n=>n.classList.remove('hot'));
        const start=Math.floor(Math.random()*links.length);for(let j=0;j<4;j++)links[(start+j*3)%links.length]?.classList.add('surge');
        for(let j=0;j<5;j++)nodes[(start+j*4)%nodes.length]?.classList.add('hot');
      },1700);
    }
    built=true;
  };
  obj.addEventListener('load',build,{once:true});if(obj.contentDocument?.documentElement)build();
  const toSvg=(clientX,clientY)=>{const pt=overlay.createSVGPoint();pt.x=clientX;pt.y=clientY;const m=overlay.getScreenCTM();return m?pt.matrixTransform(m.inverse()):{x:500,y:295}};
  stage.addEventListener('pointermove',e=>{
    if(e.pointerType==='touch'||!built)return;
    const p=toSvg(e.clientX,e.clientY),r=stage.getBoundingClientRect();
    section.style.setProperty('--national-x',((e.clientX-r.left)/r.width*100).toFixed(1)+'%');section.style.setProperty('--national-y',((e.clientY-r.top)/r.height*100).toFixed(1)+'%');
    pointerCore.setAttribute('cx',p.x.toFixed(1));pointerCore.setAttribute('cy',p.y.toFixed(1));pointerCore.classList.add('live');
    const nearest=points.slice().sort((a,b)=>dist(p,a)-dist(p,b)).slice(0,4);
    nodes.forEach(n=>n.classList.remove('hot'));
    pointerLines.forEach((line,i)=>{const q=nearest[i];if(!q){line.classList.remove('live');return}line.setAttribute('x1',q.x.toFixed(1));line.setAttribute('y1',q.y.toFixed(1));line.setAttribute('x2',p.x.toFixed(1));line.setAttribute('y2',p.y.toFixed(1));line.classList.add('live');nodes[q.i]?.classList.add('hot')});
    if(state)state.textContent='POINTER LINK ACTIVE';
  },{passive:true});
  stage.addEventListener('pointerleave',()=>{pointerLines.forEach(l=>l.classList.remove('live'));pointerCore.classList.remove('live');nodes.forEach(n=>n.classList.remove('hot'));section.style.setProperty('--national-x','50%');section.style.setProperty('--national-y','50%');if(state)state.textContent='MOVE ACROSS THE NETWORK'});
})();
</script>
'''
if '</body>' not in s:
    raise SystemExit('body close not found')
s=s.replace('</body>',js+'\n</body>',1)
html_path.write_text(s)
print('Rebuilt National Story province map as light laser mesh; hero untouched')
