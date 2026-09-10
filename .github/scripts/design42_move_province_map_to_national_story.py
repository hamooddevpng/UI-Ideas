from pathlib import Path
import re

p=Path('42.html')
s=p.read_text()

# Restore the original approved hero copy from before the business-feedback hero pass.
s=s.replace("body:'A nationally owned network connecting customers and communities across Papua New Guinea\\'s 22 provinces.'","body:'Mobile, fixed, business and remote telecommunications services for customers across Papua New Guinea.'",1)

marker='/* Design 42: business feedback hero clarity + 22 province network + readability */'
idx=s.find(marker)
if idx<0:
    raise SystemExit('business feedback marker not found')
end=s.find('</style>',idx)
if end<0:
    raise SystemExit('style close not found')

replacement=r'''/* Design 42: business feedback readability only */
/* Quick Actions: clearer copy, no softness */
.quick-launchpad .quick-card{height:108px!important;padding:13px 15px 12px!important}
.quick-launchpad .q-num{font-size:7.2px!important;color:#607b89!important;letter-spacing:.11em!important}
.quick-launchpad .quick-card h3{font-size:18.5px!important;margin:9px 0 3px!important;color:#17384a!important}
.quick-launchpad .quick-card p{font-size:8.8px!important;line-height:1.35!important;color:#4d6978!important;font-weight:600!important;white-space:normal!important;overflow:visible!important;text-overflow:clip!important;max-width:94%}
.quick-launchpad .quick-card:hover,.quick-launchpad .quick-card:focus-visible{transform:none!important;filter:none!important}
.quick-launchpad.quick-focused .quick-card:not(.quick-hot){transform:none!important;filter:none!important;opacity:.74!important}

/* News preview: keep headline and supporting copy comfortably above the bottom edge */
.updates-live .news-feature{align-items:stretch!important}
.updates-live .news-copy{justify-content:center!important;padding:28px 34px 66px!important}
.updates-live .news-copy h3{margin:8px 0 9px!important;line-height:.98!important}
.updates-live .news-copy p{margin:0 0 12px!important;line-height:1.55!important}
.updates-live .news-copy a{margin-top:5px!important;align-self:flex-start!important}

/* National Story: verified 22-province network visualization */
.png-live .png-story-route,.png-live .png-beacon,.png-live .png-sweep{display:none!important}
.png-live .story-copy{width:min(1380px,calc(100% - 80px));padding-right:54%;pointer-events:none}
.png-live .story-copy>*{pointer-events:auto}
.png-live .story-copy p{max-width:465px}
.national-map-card{position:absolute;z-index:7;right:max(38px,calc((100vw - 1380px)/2));top:50%;width:min(50vw,720px);height:min(66vh,540px);min-height:430px;transform:translateY(-50%);border:1px solid rgba(185,236,255,.25);border-radius:30px;background:linear-gradient(145deg,rgba(5,35,48,.78),rgba(5,57,69,.58));backdrop-filter:blur(15px);box-shadow:0 30px 80px rgba(0,16,24,.28),inset 0 1px rgba(255,255,255,.08);overflow:hidden;isolation:isolate}
.national-map-card:before{content:"";position:absolute;inset:0;background-image:linear-gradient(rgba(160,227,250,.04) 1px,transparent 1px),linear-gradient(90deg,rgba(160,227,250,.04) 1px,transparent 1px);background-size:36px 36px;pointer-events:none}
.national-map-head{position:absolute;z-index:8;left:18px;right:18px;top:16px;display:flex;align-items:flex-start;justify-content:space-between;gap:18px;color:#fff}
.national-map-head small{display:block;font-size:6px;font-weight:800;letter-spacing:.16em;color:#9ae8ff;margin-bottom:5px}
.national-map-head strong{display:block;font-family:"Space Grotesk";font-size:18px;letter-spacing:-.03em}
.national-map-counter{min-width:82px;padding:9px 11px;border:1px solid rgba(173,232,255,.18);border-radius:14px;background:rgba(255,255,255,.07);text-align:right}
.national-map-counter b{display:block;font-family:"Space Grotesk";font-size:18px;line-height:1;color:#fff}
.national-map-counter span{font-size:6px;font-weight:800;letter-spacing:.12em;color:#92dff9}
.national-map-stage{position:absolute;z-index:3;left:15px;right:15px;top:62px;bottom:42px}
.national-map-object,.national-map-overlay{position:absolute;inset:0;width:100%;height:100%;border:0;pointer-events:none}
.national-map-object{opacity:.84;filter:drop-shadow(0 10px 26px rgba(0,0,0,.22)) saturate(.9) brightness(1.14)}
.national-map-overlay{z-index:3;overflow:visible}
.national-province-link{fill:none;stroke:#83ddff;stroke-width:1.1;stroke-linecap:round;vector-effect:non-scaling-stroke;opacity:.1}
.national-province-link.active{opacity:.88;stroke-width:2;stroke-dasharray:7 10;animation:nationalRoute 1.1s linear infinite;filter:drop-shadow(0 0 6px rgba(110,222,255,.72))}
@keyframes nationalRoute{to{stroke-dashoffset:-34}}
.national-province-node circle:first-child{fill:rgba(121,222,255,.08);stroke:#91e5ff;stroke-width:1;vector-effect:non-scaling-stroke;opacity:.38}
.national-province-node circle:last-child{fill:#e8fbff;stroke:#26b7ef;stroke-width:1.2;vector-effect:non-scaling-stroke;filter:drop-shadow(0 0 6px #58cef7)}
.national-province-node.active circle:first-child{opacity:.95;animation:nationalPulse 1.2s ease-out infinite}
.national-province-node.active circle:last-child{fill:#fff;filter:drop-shadow(0 0 12px #78e0ff)}
@keyframes nationalPulse{to{r:14;opacity:0}}
.national-hub-ring{fill:rgba(141,230,255,.1);stroke:#b9f2ff;stroke-width:1.3;vector-effect:non-scaling-stroke;animation:nationalHub 1.9s ease-out infinite}
.national-hub-core{fill:#fff;filter:drop-shadow(0 0 11px #73dcff)}
@keyframes nationalHub{70%,100%{r:23;opacity:0}}
.national-map-foot{position:absolute;z-index:8;left:18px;right:18px;bottom:14px;display:flex;justify-content:space-between;align-items:center;gap:15px;color:#a6d6e7;font-size:6px;font-weight:800;letter-spacing:.11em}
.national-map-foot span:last-child{color:#fff}
.national-map-progress{position:absolute;z-index:7;left:18px;right:18px;bottom:35px;height:1px;background:rgba(185,236,255,.12);overflow:hidden}
.national-map-progress i{display:block;width:0;height:100%;background:linear-gradient(90deg,#58cef7,#b9f2ff);box-shadow:0 0 8px rgba(88,206,247,.8);transition:width .38s var(--ease)}

@media(max-width:1050px) and (min-width:821px){
  .quick-launchpad .quick-card{height:106px!important}
  .quick-launchpad .quick-card p{font-size:8px!important}
  .national-map-card{right:24px;width:52vw;height:min(62vh,500px)}
  .png-live .story-copy{padding-right:55%}
}
@media(max-width:820px){
  .quick-launchpad .quick-card p{font-size:8px!important;max-width:100%}
  .updates-live .news-copy{padding:28px 26px 54px!important}
  .png-live{display:block!important;min-height:850px!important}
  .png-live .story-copy{width:calc(100% - 34px);padding:68px 0 0!important}
  .png-live .story-copy h2{font-size:clamp(48px,14vw,72px)}
  .national-map-card{position:absolute;left:17px;right:17px;top:auto;bottom:28px;width:auto;height:390px;min-height:0;transform:none;border-radius:24px}
  .national-map-stage{top:58px;bottom:38px;left:9px;right:9px}
}
@media(prefers-reduced-motion:reduce){.national-province-link.active,.national-province-node.active circle:first-child,.national-hub-ring{animation:none!important}}
'''

# Remove the feedback pass that changed all hero scenes and put the province network inside the hero.
s=s[:idx]+replacement+'\n'+s[end:]

# Remove the province-network script that was injected into the tower hero scene.
pat=r'\n<script>\s*;\(\(\)=>\{\s*const scene=document\.querySelector\(\'\.scene-enterprise\'\);\s*if\(!scene \|\| scene\.querySelector\(\'\.province-network\'\)\) return;.*?</script>\s*(?=</body>)'
s,n=re.subn(pat,'\n',s,count=1,flags=re.S)
if n!=1:
    raise SystemExit(f'hero province script removal count {n}')

# Install the province map card in National Story, using the existing verified admin-1 SVG.
needle='<div class="png-story-glow"></div>'
if needle not in s:
    raise SystemExit('national story glow insertion point missing')
map_markup='''<div class="png-story-glow"></div>\n  <aside class="national-map-card" id="nationalMapCard" aria-label="Telikom national network across Papua New Guinea's 22 provinces">\n    <div class="national-map-head"><div><small>TELIKOM LTD · NATIONAL NETWORK</small><strong>Connecting all 22 provinces</strong></div><div class="national-map-counter"><b id="nationalMapCount">01 / 22</b><span>PROVINCE LINK</span></div></div>\n    <div class="national-map-stage"><object class="national-map-object" id="nationalProvinceMap" type="image/svg+xml" data="assets/design42/png-admin1-simplemaps.svg" aria-label="Papua New Guinea province map"></object><svg class="national-map-overlay" id="nationalProvinceOverlay" viewBox="0 0 1000 589" preserveAspectRatio="xMidYMid meet" aria-hidden="true"><g id="nationalProvinceLinks"></g><g id="nationalProvinceNodes"></g></svg></div>\n    <div class="national-map-progress"><i id="nationalMapProgress"></i></div>\n    <div class="national-map-foot"><span>22 PROVINCE-LEVEL CONNECTIONS</span><span id="nationalMapState">NATIONAL COVERAGE STORY</span></div>\n  </aside>'''
s=s.replace(needle,map_markup,1)

# Update National Story copy, without altering any hero copy.
s=s.replace('Telikom serves Papua New Guineans with mobile, fixed, business and remote telecommunications services.','A nationally owned network connecting people, communities and services across Papua New Guinea’s 22 provinces.',1)

national_js=r'''
<script>
;(()=>{
  const section=document.getElementById('png-story'),obj=document.getElementById('nationalProvinceMap'),overlay=document.getElementById('nationalProvinceOverlay');
  const linksG=document.getElementById('nationalProvinceLinks'),nodesG=document.getElementById('nationalProvinceNodes'),count=document.getElementById('nationalMapCount'),progress=document.getElementById('nationalMapProgress');
  if(!section||!obj||!overlay||!linksG||!nodesG)return;
  const NS='http://www.w3.org/2000/svg';
  let routes=[],nodes=[],features=[],current=0,timer=null,visible=false;
  const setProvince=i=>{
    if(!routes.length)return;
    current=(i+routes.length)%routes.length;
    routes.forEach((r,n)=>r.classList.toggle('active',n===current));
    nodes.forEach((r,n)=>r.classList.toggle('active',n===current));
    features.forEach((el,n)=>{
      el.style.setProperty('fill',n===current?'#168ab2':'#0b6388','important');
      el.style.setProperty('stroke',n===current?'#d9f8ff':'#8edbff','important');
      el.style.setProperty('stroke-width',n===current?'1.35':'.72','important');
    });
    if(count)count.textContent=String(current+1).padStart(2,'0')+' / '+String(routes.length).padStart(2,'0');
    if(progress)progress.style.width=((current+1)/routes.length*100).toFixed(2)+'%';
  };
  const start=()=>{if(timer||!visible||document.hidden||!routes.length)return;setProvince(current);timer=setInterval(()=>setProvince(current+1),1050)};
  const stop=()=>{if(timer){clearInterval(timer);timer=null}};
  const build=()=>{
    let doc;
    try{doc=obj.contentDocument}catch(e){return}
    if(!doc)return;
    let raw=[...doc.querySelectorAll('#features > path, #features > polygon')].filter(el=>{try{const b=el.getBBox();return b.width>1&&b.height>1}catch(e){return false}});
    // This Simplemaps admin-1 asset is expected to contain the 22 province-level divisions.
    // If extra decorative geometries ever appear, keep the 22 largest province geometries.
    raw=raw.map(el=>({el,b:el.getBBox()})).sort((a,b)=>(b.b.width*b.b.height)-(a.b.width*a.b.height)).slice(0,22);
    features=raw.map(x=>x.el);
    linksG.replaceChildren();nodesG.replaceChildren();routes=[];nodes=[];
    const hub=[470,515];
    raw.forEach(({b},i)=>{
      const x=b.x+b.width/2,y=b.y+b.height/2;
      const path=document.createElementNS(NS,'path');
      const mx=(hub[0]+x)/2,my=(hub[1]+y)/2-Math.min(34,Math.abs(x-hub[0])*.025);
      path.setAttribute('d',`M${hub[0]} ${hub[1]} Q${mx.toFixed(1)} ${my.toFixed(1)} ${x.toFixed(1)} ${y.toFixed(1)}`);
      path.setAttribute('class','national-province-link');linksG.appendChild(path);routes.push(path);
      const g=document.createElementNS(NS,'g');g.setAttribute('class','national-province-node');g.setAttribute('transform',`translate(${x.toFixed(1)} ${y.toFixed(1)})`);
      const ring=document.createElementNS(NS,'circle');ring.setAttribute('r','7');
      const dot=document.createElementNS(NS,'circle');dot.setAttribute('r','3.8');g.append(ring,dot);nodesG.appendChild(g);nodes.push(g);
    });
    const hubG=document.createElementNS(NS,'g');hubG.setAttribute('transform',`translate(${hub[0]} ${hub[1]})`);
    const hr=document.createElementNS(NS,'circle');hr.setAttribute('class','national-hub-ring');hr.setAttribute('r','11');
    const hc=document.createElementNS(NS,'circle');hc.setAttribute('class','national-hub-core');hc.setAttribute('r','5.5');hubG.append(hr,hc);nodesG.appendChild(hubG);
    setProvince(0);start();
  };
  obj.addEventListener('load',build,{once:true});
  if(obj.contentDocument?.documentElement)build();
  const io=new IntersectionObserver(([entry])=>{visible=entry.isIntersecting;if(visible)start();else stop()},{threshold:.18});io.observe(section);
  document.addEventListener('visibilitychange',()=>document.hidden?stop():start());
})();
</script>
'''
s=s.replace('</body>',national_js+'\n</body>',1)

p.write_text(s)
print('Moved 22-province network from hero to National Story and restored approved hero')
