from pathlib import Path

p=Path('42.html')
s=p.read_text()

old='<div class="scene scene-enterprise"><div class="enterprise-atmos" aria-hidden="true"></div></div>'
new='<div class="scene scene-enterprise"><img class="hero-atmos hero-map" src="assets/design42/png-admin1-simplemaps.svg" alt="" aria-hidden="true"></div>'
if old not in s:
    raise SystemExit('enterprise scene target missing')
s=s.replace(old,new,1)

anchor='</div><div class="feed-meter"><span></span><i></i><b>RECEIVING</b></div></div>'
replacement='</div><div class="live-news-stream" id="liveNewsStream" aria-live="polite"></div><div class="feed-meter"><span></span><i></i><b>RECEIVING</b></div></div>'
if anchor not in s:
    raise SystemExit('updates feed anchor missing')
s=s.replace(anchor,replacement,1)

css=r'''
/* Design 42: timed live-news carousel */
.live-news-stream{position:relative;height:164px;margin-top:9px;overflow:hidden;border-top:1px solid var(--line);padding-top:8px}
.live-feed-card{position:relative;height:48px;margin:0 0 6px;padding:5px 8px 5px 5px;border:1px solid rgba(16,43,60,.09);border-radius:13px;background:linear-gradient(90deg,#f8fcfe,#fff);display:grid;grid-template-columns:52px minmax(0,1fr) auto;align-items:center;gap:9px;cursor:pointer;box-shadow:0 7px 18px rgba(19,63,84,.045);overflow:hidden;transform-origin:50% 100%}
.live-feed-card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:2px;background:linear-gradient(#8ee5ff,#0875c9);opacity:.85}
.live-feed-card.entering{animation:liveFeedIn .72s var(--spring) both}
.live-feed-card.leaving{pointer-events:none;animation:liveFeedOut .42s ease-in both}
@keyframes liveFeedIn{0%{opacity:0;transform:translate3d(0,30px,0) scale(.91);filter:blur(5px)}58%{opacity:1;transform:translate3d(0,-4px,0) scale(1.025);filter:blur(0)}100%{opacity:1;transform:none;filter:none}}
@keyframes liveFeedOut{to{opacity:0;transform:translate3d(-36px,-8px,0) scale(.94);filter:blur(3px)}}
.live-feed-thumb{width:52px;height:36px;border-radius:9px;overflow:hidden;background:#dceff7}.live-feed-thumb img{width:100%;height:100%;display:block;object-fit:cover;transition:transform .45s var(--spring)}.live-feed-card:hover .live-feed-thumb img{transform:scale(1.08)}
.live-feed-copy{min-width:0}.live-feed-copy small{display:flex;align-items:center;gap:6px;color:var(--blue);font-size:5.5px;font-weight:800;letter-spacing:.11em;text-transform:uppercase}.live-feed-copy small:before{content:"";width:5px;height:5px;border-radius:50%;background:#20a957;box-shadow:0 0 0 3px rgba(32,169,87,.1)}.live-feed-copy b{display:block;margin-top:3px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;font-size:8px;line-height:1.15;color:var(--ink)}
.live-feed-now{align-self:start;margin-top:2px;padding:4px 6px;border-radius:999px;background:#e8f6fc;color:#0875c9;font-size:5px;font-weight:800;letter-spacing:.08em}.live-feed-card:hover{border-color:rgba(8,117,201,.25);box-shadow:0 10px 24px rgba(19,63,84,.09)}
.updates-live .updates-console{overflow:hidden}.updates-live .notice-row{padding:12px 5px}.updates-live .notice-body{font-size:9px}.updates-console-head small.live-count-flash{animation:liveCountFlash .5s var(--spring)}@keyframes liveCountFlash{50%{color:#0875c9;transform:scale(1.06)}}
@media(max-width:820px){.live-news-stream{height:164px}.live-feed-card{grid-template-columns:48px minmax(0,1fr) auto}.live-feed-thumb{width:48px}}
@media(prefers-reduced-motion:reduce){.live-feed-card.entering,.live-feed-card.leaving{animation:none!important}}
'''
if 'Design 42: timed live-news carousel' in s:
    raise SystemExit('live news patch already applied')
pos=s.rfind('</style>')
if pos<0: raise SystemExit('style close missing')
s=s[:pos]+css+s[pos:]

js=r'''
;(()=>{
  const section=document.getElementById('updates'),stream=document.getElementById('liveNewsStream'),status=document.getElementById('updatesFeedStatus');
  const card=document.getElementById('newsLiveCard'),img=document.getElementById('newsLiveImage'),kicker=document.getElementById('newsLiveKicker'),title=document.getElementById('newsLiveTitle'),text=document.getElementById('newsLiveText');
  if(!section||!stream)return;
  const feed=[
    {id:'mobile',k:'Mobile',t:'Mobile services and bundle information',p:'Mobile plans, data options and account services can be surfaced here as fresh customer updates.',img:'assets/common/web-sourced/telikom/news-01.jpg'},
    {id:'selfcare',k:'Self Care',t:'Manage more from Self Care',p:'Top up, balance checks, post-paid bills, bundles and credit transfer are available through Telikom Self Care.',img:'assets/common/web-sourced/telikom/news-02.jpg'},
    {id:'business',k:'Business',t:'Business connectivity portfolio',p:'Dedicated data, voice, systems, hosting and enterprise connectivity services for organisations in PNG.',img:'assets/common/web-sourced/telikom/news-03.jpg'},
    {id:'remote',k:'Remote',t:'Connectivity beyond the network edge',p:'VSAT and remote telecommunications services support business and communities in harder-to-reach locations.',img:'assets/common/web-sourced/telikom/news-04.jpg'},
    {id:'care',k:'Customer Care',t:'Customer Care is available on 1555',p:'Telikom customers can reach Customer Care on 1555 or (+675) 7600 3555 for assistance.',img:'assets/common/web-sourced/telikom/news-06.jpg'},
    {id:'public',k:'Public Notice',t:'Public notices and opportunities',p:'Corporate notices, careers, tenders and formal Telikom information can rotate through this live feed.',img:'assets/common/web-sourced/telikom/news-07.jpg'},
    {id:'broadband',k:'Fixed Broadband',t:'Home and fixed connectivity',p:'Fixed broadband and home internet information can appear here as plans and service information change.',img:'assets/common/web-sourced/telikom/news-08.jpg'}
  ];
  let visible=false,visibleMs=0,last=performance.now(),initial=0,cycleMs=0,next=0,previewTimer=null;
  const thresholds=[1000,3000,5000];
  const setPreview=d=>{
    if(!card||!img||!kicker||!title||!text)return;
    card.classList.add('switching');clearTimeout(previewTimer);
    previewTimer=setTimeout(()=>{img.src=d.img;img.alt=d.t;kicker.textContent=d.k;title.textContent=d.t+'.';text.textContent=d.p;card.classList.remove('switching')},170);
  };
  const updateStatus=()=>{
    if(!status)return;const n=stream.children.length;status.textContent=String(n).padStart(2,'0')+' LIVE ITEM'+(n===1?'':'S')+' · TELIKOM';status.classList.remove('live-count-flash');void status.offsetWidth;status.classList.add('live-count-flash');
  };
  const makeCard=d=>{
    const el=document.createElement('article');el.className='live-feed-card entering';el.dataset.liveNews=d.id;el.tabIndex=0;
    el.innerHTML='<div class="live-feed-thumb"><img src="'+d.img+'" alt=""></div><div class="live-feed-copy"><small>'+d.k+'</small><b>'+d.t+'</b></div><span class="live-feed-now">JUST NOW</span>';
    const preview=()=>setPreview(d);el.addEventListener('pointerenter',e=>{if(e.pointerType!=='touch')preview()});el.addEventListener('focusin',preview);el.addEventListener('click',preview);return el;
  };
  const addFeed=()=>{
    const d=feed[next%feed.length];next++;
    const insert=()=>{const el=makeCard(d);stream.appendChild(el);setPreview(d);updateStatus();setTimeout(()=>el.classList.remove('entering'),780)};
    if(stream.children.length>=3){const old=stream.firstElementChild;old.classList.add('leaving');setTimeout(()=>{old.remove();insert()},380)}else insert();
  };
  const io=new IntersectionObserver(([entry])=>{visible=entry.isIntersecting&&entry.intersectionRatio>=.28},{threshold:[0,.28,.5]});io.observe(section);
  const tick=now=>{
    const dt=Math.min(100,now-last);last=now;
    if(visible&&!document.hidden){
      if(initial<thresholds.length){visibleMs+=dt;while(initial<thresholds.length&&visibleMs>=thresholds[initial]){addFeed();initial++}}
      else{cycleMs+=dt;if(cycleMs>=3200){cycleMs=0;addFeed()}}
    }
    requestAnimationFrame(tick);
  };
  requestAnimationFrame(tick);
})();
'''
pos=s.rfind('</script>')
if pos<0: raise SystemExit('script close missing')
s=s[:pos]+js+s[pos:]

p.write_text(s)
