from pathlib import Path

p=Path('42.html')
s=p.read_text()
marker='/* Design 42: business feedback hero clarity + 22 province network + readability */'
if marker in s:
    raise SystemExit('feedback pass already present')

old_body="body:'Mobile, fixed, business and remote telecommunications services for customers across Papua New Guinea.'"
new_body="body:'A nationally owned network connecting customers and communities across Papua New Guinea\\'s 22 provinces.'"
if old_body in s:
    s=s.replace(old_body,new_body,1)

css=r'''

/* Design 42: business feedback hero clarity + 22 province network + readability */
/* Hero image clarity */
.scene-phone{
  background:linear-gradient(115deg,#092b3b 0%,#0b3b50 48%,#17617b 100%)!important;
}
.scene-phone .hero-people{
  opacity:.48!important;
  object-position:70% 48%!important;
  filter:saturate(1.02) contrast(1.02) brightness(.88)!important;
  transform:scale(1.01)!important;
  -webkit-mask-image:linear-gradient(90deg,transparent 2%,rgba(0,0,0,.45) 30%,#000 58%)!important;
  mask-image:linear-gradient(90deg,transparent 2%,rgba(0,0,0,.45) 30%,#000 58%)!important;
}
.scene-phone:after{
  background:linear-gradient(90deg,rgba(5,31,43,.72) 0%,rgba(5,31,43,.48) 34%,rgba(5,31,43,.12) 62%,rgba(5,31,43,.03) 100%)!important;
}

.scene-remote{
  background:linear-gradient(180deg,#87b8c7 0%,#b5d3d6 47%,#d8d3ad 100%)!important;
}
.scene-remote .hero-island{
  opacity:.72!important;
  object-position:center 52%!important;
  filter:saturate(1.04) contrast(1.03) brightness(.91)!important;
  transform:scale(1.012)!important;
}
.scene-remote .ridge{display:none!important}
.scene-remote:after{
  background:linear-gradient(90deg,rgba(4,34,46,.62) 0%,rgba(4,34,46,.42) 31%,rgba(4,34,46,.13) 54%,rgba(4,34,46,.02) 76%)!important;
}

/* PNG Network: verified province map remains the geography source; overlay only supplies network routes. */
.hero[data-scene-index="2"] .scene-art[data-art="2"] .grid-plane,
.hero[data-scene-index="2"] .scene-art[data-art="2"] .network-svg{display:none!important}
.hero .hero-map{
  right:1.5%!important;
  top:6%!important;
  width:64%!important;
  height:86%!important;
  object-fit:contain!important;
  object-position:center!important;
  opacity:.52!important;
  filter:drop-shadow(0 0 24px rgba(46,183,239,.23))!important;
  mix-blend-mode:screen!important;
  transform:none!important;
  -webkit-mask-image:none!important;
  mask-image:none!important;
}
.province-network{
  position:absolute;
  z-index:3;
  right:1.5%;
  top:6%;
  width:64%;
  height:86%;
  overflow:visible;
  pointer-events:none;
}
.province-link{
  fill:none;
  stroke:#74d8ff;
  stroke-width:1.2;
  vector-effect:non-scaling-stroke;
  stroke-linecap:round;
  opacity:.11;
  transition:opacity .35s,stroke-width .35s;
}
.province-link.active{
  opacity:.88;
  stroke-width:2.1;
  stroke-dasharray:8 10;
  animation:provinceRoute 1.05s linear infinite;
  filter:drop-shadow(0 0 7px rgba(104,217,255,.72));
}
@keyframes provinceRoute{to{stroke-dashoffset:-36}}
.province-node .province-dot{fill:#dff9ff;stroke:#2bb7ef;stroke-width:1.6;vector-effect:non-scaling-stroke;filter:drop-shadow(0 0 6px rgba(78,201,246,.8))}
.province-node .province-ring{fill:none;stroke:#79ddff;stroke-width:1;vector-effect:non-scaling-stroke;opacity:.18}
.province-node.active .province-dot{fill:#fff;stroke:#9cecff;filter:drop-shadow(0 0 12px #78dfff)}
.province-node.active .province-ring{opacity:.8;animation:provincePulse 1.15s ease-out infinite}
@keyframes provincePulse{to{r:15;opacity:0}}
.province-hub-ring{fill:rgba(126,225,255,.08);stroke:#b6efff;stroke-width:1.4;vector-effect:non-scaling-stroke;animation:provinceHub 1.9s ease-out infinite}
.province-hub-core{fill:#fff;filter:drop-shadow(0 0 12px #70dcff)}
@keyframes provinceHub{70%,100%{r:22;opacity:0}}
.province-network-status{
  position:absolute;
  z-index:5;
  right:4%;
  top:13%;
  width:190px;
  padding:11px 13px;
  border:1px solid rgba(164,230,255,.22);
  border-radius:15px;
  background:rgba(5,34,47,.62);
  backdrop-filter:blur(14px);
  box-shadow:0 15px 35px rgba(0,0,0,.16);
  pointer-events:none;
}
.province-network-status small{display:block;color:#8fdfff;font-size:6.5px;font-weight:800;letter-spacing:.15em;text-transform:uppercase}
.province-network-status strong{display:block;font-family:"Space Grotesk";font-size:17px;line-height:1;margin:5px 0 4px;color:#fff}
.province-network-status span{display:block;color:#c4dce6;font-size:7px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}

/* Quick Actions: clearer copy, no softness */
.quick-launchpad .quick-card{height:108px!important;padding:13px 15px 12px!important}
.quick-launchpad .q-num{font-size:7.2px!important;color:#607b89!important;letter-spacing:.11em!important}
.quick-launchpad .quick-card h3{font-size:18.5px!important;margin:9px 0 3px!important;color:#17384a!important}
.quick-launchpad .quick-card p{
  font-size:8.8px!important;
  line-height:1.35!important;
  color:#4d6978!important;
  font-weight:600!important;
  white-space:normal!important;
  overflow:visible!important;
  text-overflow:clip!important;
  max-width:94%;
}
.quick-launchpad .quick-card:hover,.quick-launchpad .quick-card:focus-visible{transform:none!important;filter:none!important}
.quick-launchpad.quick-focused .quick-card:not(.quick-hot){transform:none!important;filter:none!important;opacity:.74!important}

/* News preview: keep headline and supporting copy comfortably above the bottom edge */
.updates-live .news-feature{align-items:stretch!important}
.updates-live .news-copy{
  justify-content:center!important;
  padding:28px 34px 66px!important;
}
.updates-live .news-copy h3{margin:8px 0 9px!important;line-height:.98!important}
.updates-live .news-copy p{margin:0 0 12px!important;line-height:1.55!important}
.updates-live .news-copy a{margin-top:5px!important;align-self:flex-start!important}

@media(max-width:1050px) and (min-width:821px){
  .quick-launchpad .quick-card{height:106px!important}
  .quick-launchpad .quick-card p{font-size:8px!important}
  .province-network-status{right:2%;top:12%;width:166px}
  .province-network-status strong{font-size:15px}
}
@media(max-width:820px){
  .scene-phone .hero-people{opacity:.38!important;object-position:64% 47%!important}
  .scene-remote .hero-island{opacity:.55!important;object-position:62% 51%!important}
  .hero .hero-map,.province-network{right:-14%!important;top:19%!important;width:92%!important;height:65%!important}
  .province-network-status{right:17px;top:auto;bottom:118px;width:158px;padding:9px 10px}
  .province-network-status strong{font-size:14px}
  .province-network-status span{font-size:6.3px}
  .quick-launchpad .quick-card p{font-size:8px!important;max-width:100%}
  .updates-live .news-copy{padding:28px 26px 54px!important}
}
@media(prefers-reduced-motion:reduce){
  .province-link.active,.province-node.active .province-ring,.province-hub-ring{animation:none!important}
}
'''

if '</style>' not in s:
    raise SystemExit('style close not found')
s=s.replace('</style>',css+'\n</style>',1)

js=r'''
<script>
;(()=>{
  const scene=document.querySelector('.scene-enterprise');
  if(!scene || scene.querySelector('.province-network')) return;
  const provinces=[
    ['Central',430,470],['Simbu',292,287],['Eastern Highlands',319,290],['East New Britain',769,185],
    ['East Sepik',204,137],['Enga',209,254],['Gulf',345,405],['Madang',346,238],['Manus',443,44],
    ['Milne Bay',651,547],['Morobe',424,329],['New Ireland',673,77],['Oro',506,454],['Bougainville',926,250],
    ['Southern Highlands',206,294],['Western',177,472],['Western Highlands',244,277],['West New Britain',630,258],
    ['Sandaun',52,84],['National Capital District',455,500],['Hela',160,276],['Jiwaka',268,279]
  ];
  const NS='http://www.w3.org/2000/svg',hub=[455,500];
  const svg=document.createElementNS(NS,'svg');
  svg.setAttribute('class','province-network');
  svg.setAttribute('viewBox','0 0 1000 589');
  svg.setAttribute('preserveAspectRatio','xMidYMid meet');
  svg.setAttribute('aria-hidden','true');
  const links=document.createElementNS(NS,'g');links.setAttribute('class','province-links');
  const nodes=document.createElementNS(NS,'g');nodes.setAttribute('class','province-nodes');
  provinces.forEach(([name,x,y],i)=>{
    const path=document.createElementNS(NS,'path');
    const mx=(hub[0]+x)/2, my=(hub[1]+y)/2 - Math.min(42,Math.abs(x-hub[0])*.035);
    path.setAttribute('d',`M${hub[0]} ${hub[1]} Q${mx.toFixed(1)} ${my.toFixed(1)} ${x} ${y}`);
    path.setAttribute('class','province-link');
    path.dataset.province=name;
    links.appendChild(path);
    const g=document.createElementNS(NS,'g');g.setAttribute('class','province-node');g.dataset.province=name;g.setAttribute('transform',`translate(${x} ${y})`);
    const ring=document.createElementNS(NS,'circle');ring.setAttribute('class','province-ring');ring.setAttribute('r','7');
    const dot=document.createElementNS(NS,'circle');dot.setAttribute('class','province-dot');dot.setAttribute('r',i===19?'5.2':'3.8');
    g.append(ring,dot);nodes.appendChild(g);
  });
  const hubG=document.createElementNS(NS,'g');hubG.setAttribute('transform',`translate(${hub[0]} ${hub[1]})`);
  const hr=document.createElementNS(NS,'circle');hr.setAttribute('class','province-hub-ring');hr.setAttribute('r','11');
  const hc=document.createElementNS(NS,'circle');hc.setAttribute('class','province-hub-core');hc.setAttribute('r','5.5');
  hubG.append(hr,hc);nodes.appendChild(hubG);
  svg.append(links,nodes);
  const status=document.createElement('div');status.className='province-network-status';status.setAttribute('aria-hidden','true');
  status.innerHTML='<small>TELIKOM LTD · NATIONAL NETWORK</small><strong>22 PROVINCES</strong><span id="provinceActiveName">National Capital District</span>';
  scene.append(svg,status);

  const routeEls=[...svg.querySelectorAll('.province-link')],nodeEls=[...svg.querySelectorAll('.province-node[data-province]')],label=status.querySelector('#provinceActiveName');
  let current=19,timer=null;
  const activate=i=>{
    current=(i+provinces.length)%provinces.length;
    routeEls.forEach((el,n)=>el.classList.toggle('active',n===current));
    nodeEls.forEach((el,n)=>el.classList.toggle('active',n===current));
    if(label)label.textContent=provinces[current][0];
  };
  const start=()=>{if(timer)return;activate(current);timer=setInterval(()=>activate(current+1),1250)};
  const stop=()=>{if(timer){clearInterval(timer);timer=null}};
  const hero=document.getElementById('top');
  const sync=()=>{if(hero?.dataset.sceneIndex==='2'&&!document.hidden)start();else stop()};
  new MutationObserver(sync).observe(hero,{attributes:true,attributeFilter:['data-scene-index']});
  document.addEventListener('visibilitychange',sync);
  sync();
})();
</script>
'''
if '</body>' not in s:
    raise SystemExit('body close not found')
s=s.replace('</body>',js+'\n</body>',1)
p.write_text(s)
print('patched 42.html')
