from pathlib import Path
import re

p=Path('42.html')
s=p.read_text()

repls={
"A few Telikom service ideas, shuffled each visit so there is always something useful to explore.":"Mobile, home internet, remote connectivity and support offers from Telikom.",
"Explore Telikom through real stories, people and places. Move across the cards to bring each service into focus.":"Mobile, fixed broadband, devices, business services and customer support across Papua New Guinea.",
"Explore Telikom business connectivity as an interactive network. Move across a service to preview how that service reaches people, offices and remote sites.":"Dedicated data, VSAT, fixed voice, web and hosting services for businesses and government.",
"Move across the feed to preview what needs attention, then open the item you want.":"Service notices, customer information and public updates from Telikom.",
"Move around the hub or search for what you need.":"Customer Care 1555 · (+675) 7600 3555",
"Suggestions reshuffle on your next visit.":"Mobile · Home · Remote · Support"
}
for old,new in repls.items():
    if old not in s:
        raise SystemExit('copy target missing: '+old)
    s=s.replace(old,new,1)

old_img='src="assets/common/web-sourced/telikom/mt-kegum.jpg" alt="Papua New Guinea landscape"'
new_img='src="https://commons.wikimedia.org/wiki/Special:Redirect/file/ISS034-E-5507_-_View_of_Papua_New_Guinea.jpg?width=2400" alt="Aerial view of the Louisiade Archipelago and coral reefs in Papua New Guinea"'
if old_img not in s:
    raise SystemExit('PNG story image target missing')
s=s.replace(old_img,new_img,1)

anchor='<div class="offer-card-grid" id="personalOfferGrid">'
if anchor not in s:
    raise SystemExit('offer grid anchor missing')
s=s.replace(anchor,'<div class="offer-pop-layer" id="offerPopLayer" aria-hidden="true"></div>'+anchor,1)

css=r'''
/* Design 42: cleaner copy + offer pop particles */
.png-live .png-story-photo{object-position:center 48%;filter:saturate(.92) contrast(1.08) brightness(.66)}
.offer-loading-stage{position:relative;isolation:isolate}
.offer-pop-layer{position:absolute;inset:0;z-index:30;pointer-events:none;overflow:hidden;border-radius:30px}
.offer-pop-particle{position:absolute;width:var(--ps,5px);height:var(--ps,5px);left:0;top:0;border-radius:999px;background:var(--pc,#1ca0e8);box-shadow:0 0 10px color-mix(in srgb,var(--pc,#1ca0e8) 68%,transparent);will-change:transform,opacity}
.offer-pop-particle.square{border-radius:2px}
.offer-pop-ring{position:absolute;left:0;top:0;width:28px;height:28px;border:1px solid rgba(28,160,232,.5);border-radius:50%;box-shadow:0 0 24px rgba(28,160,232,.18);will-change:transform,opacity}
#offers.offer-pop-live .personal-offer{will-change:transform,opacity,filter}
#offers.offer-pop-live .personal-offer-media img{will-change:transform}
@media(max-width:820px){.offer-pop-layer{border-radius:22px}}
@media(prefers-reduced-motion:reduce){.offer-pop-layer{display:none}}
'''
if 'Design 42: cleaner copy + offer pop particles' in s:
    raise SystemExit('patch already applied')
pos=s.rfind('</style>')
if pos<0: raise SystemExit('style close missing')
s=s[:pos]+css+s[pos:]

js=r'''
;(()=>{
  const section=document.getElementById('offers');
  const stage=document.getElementById('offerLoadingStage');
  const layer=document.getElementById('offerPopLayer');
  const loader=document.getElementById('offerLoader');
  const cards=[...document.querySelectorAll('#personalOfferGrid .personal-offer')];
  if(!section||!stage||!layer||!cards.length)return;
  const reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
  let armed=false,popped=false;
  const colors=['#1ca0e8','#0875c9','#20a957','#9ce8ff','#ffffff'];
  function burst(card,index){
    if(reduce)return;
    const sr=stage.getBoundingClientRect(),cr=card.getBoundingClientRect();
    const x=cr.left-sr.left+cr.width/2,y=cr.top-sr.top+cr.height*.48;
    const ring=document.createElement('i');
    ring.className='offer-pop-ring';ring.style.left=x+'px';ring.style.top=y+'px';layer.appendChild(ring);
    const ra=ring.animate([
      {transform:'translate(-50%,-50%) scale(.1)',opacity:.9},
      {transform:'translate(-50%,-50%) scale(4.4)',opacity:0}
    ],{duration:720,easing:'cubic-bezier(.16,1,.3,1)'});ra.onfinish=()=>ring.remove();
    const count=innerWidth<820?10:18;
    for(let i=0;i<count;i++){
      const p=document.createElement('i');
      p.className='offer-pop-particle'+(i%4===0?' square':'');
      const a=(Math.PI*2*i/count)+(Math.random()-.5)*.38;
      const d=34+Math.random()*(innerWidth<820?48:88);
      const dx=Math.cos(a)*d,dy=Math.sin(a)*d-(8+Math.random()*22);
      const size=2.5+Math.random()*4.5;
      p.style.left=x+'px';p.style.top=y+'px';p.style.setProperty('--ps',size+'px');p.style.setProperty('--pc',colors[(i+index)%colors.length]);
      layer.appendChild(p);
      const pa=p.animate([
        {transform:'translate(-50%,-50%) scale(.2) rotate(0deg)',opacity:0},
        {offset:.16,transform:'translate(-50%,-50%) scale(1)',opacity:1},
        {transform:`translate(calc(-50% + ${dx}px),calc(-50% + ${dy}px)) scale(.25) rotate(${90+Math.random()*210}deg)`,opacity:0}
      ],{duration:620+Math.random()*260,delay:Math.random()*45,easing:'cubic-bezier(.17,.67,.25,1)'});
      pa.onfinish=()=>p.remove();
    }
  }
  function popCards(){
    if(popped)return;popped=true;section.classList.add('offer-pop-live');
    cards.forEach((card,i)=>setTimeout(()=>{
      const dir=i===0?-1:i===2?1:0;
      const anim=card.animate([
        {transform:`translate3d(${dir*38}px,70px,0) scale(.08) rotate(${dir*-7}deg)`,opacity:0,filter:'blur(8px)'},
        {offset:.48,transform:`translate3d(${dir*8}px,-18px,0) scale(1.09) rotate(${dir*1.5}deg)`,opacity:1,filter:'blur(0px)'},
        {offset:.72,transform:'translate3d(0,7px,0) scale(.97) rotate(0deg)',opacity:1,filter:'blur(0px)'},
        {transform:'translate3d(0,0,0) scale(1) rotate(0deg)',opacity:1,filter:'blur(0px)'}
      ],{duration:1120,easing:'cubic-bezier(.16,1,.3,1)',fill:'both'});
      const img=card.querySelector('.personal-offer-media img');
      if(img){const ia=img.animate([{transform:'scale(1.18)'},{transform:'scale(1)'}],{duration:1250,easing:'cubic-bezier(.16,1,.3,1)',fill:'both'});ia.finished.then(()=>ia.cancel()).catch(()=>{})}
      burst(card,i);
      anim.finished.then(()=>anim.cancel()).catch(()=>{});
    },i*230));
  }
  function waitForCards(){
    const started=performance.now();
    const tick=()=>{
      const lop=loader?parseFloat(getComputedStyle(loader).opacity||'1'):0;
      const visible=cards.some(c=>parseFloat(getComputedStyle(c).opacity||'0')>.2);
      if((lop<.3&&visible)||performance.now()-started>3000)popCards();else setTimeout(tick,70)
    };tick();
  }
  function maybeArm(){
    if(armed||scrollY<=0)return;
    const r=section.getBoundingClientRect();
    if(r.top<innerHeight*.84&&r.bottom>innerHeight*.16){armed=true;waitForCards()}
  }
  addEventListener('scroll',maybeArm,{passive:true});
  new IntersectionObserver(()=>maybeArm(),{threshold:.18}).observe(section);
})();
'''
pos=s.rfind('</script>')
if pos<0: raise SystemExit('script close missing')
s=s[:pos]+js+s[pos:]

p.write_text(s)
