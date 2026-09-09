from pathlib import Path


def inject(path, css, js):
    p=Path(path)
    s=p.read_text()
    marker='/* D40-D41 CRAZY ENHANCEMENTS */'
    if marker in s:
        raise SystemExit(f'{path} already enhanced')
    s=s.replace('</style>', f'\n{marker}\n{css}\n</style>', 1)
    idx=s.rfind('</script>')
    if idx < 0:
        raise SystemExit(f'no script in {path}')
    s=s[:idx] + '\n' + js + '\n' + s[idx:]
    p.write_text(s)

css40=r'''
/* D40-D41 CRAZY ENHANCEMENTS */
@media(min-width:901px){
  #services.section{padding:54px 0 58px}
  #services .section-head{margin-bottom:24px}
  #services .service-stories{display:flex;grid-template-columns:none;gap:10px;height:min(49vh,445px);min-height:360px;overflow:visible}
  #services .service-story{position:relative;flex:.86 1 0;min-width:0;height:100%;border-radius:20px;overflow:hidden;background:#102b3c;box-shadow:0 14px 35px rgba(16,43,60,.08);isolation:isolate;transition:flex .78s cubic-bezier(.16,1,.3,1),transform .62s cubic-bezier(.16,1,.3,1),box-shadow .62s,filter .62s;transform:translateY(0)}
  #services .service-story.active-story{flex:2.45 1 0;transform:translateY(-6px);box-shadow:0 26px 58px rgba(16,43,60,.18)}
  #services .service-story:not(.active-story){filter:saturate(.72) brightness(.88)}
  #services .service-story img{position:absolute;inset:0;width:100%;height:100%;aspect-ratio:auto;border-radius:0;margin:0;object-fit:cover;transform:scale(1.04) translate3d(var(--story-x,0px),var(--story-y,0px),0);transition:transform .8s cubic-bezier(.16,1,.3,1),filter .7s;z-index:-2}
  #services .service-story:after{content:"";position:absolute;inset:0;z-index:-1;background:linear-gradient(180deg,rgba(6,25,37,.02) 22%,rgba(6,25,37,.42) 58%,rgba(6,25,37,.94) 100%);transition:background .65s}
  #services .service-story.active-story:after{background:linear-gradient(180deg,rgba(6,25,37,0) 14%,rgba(6,25,37,.24) 53%,rgba(6,25,37,.91) 100%)}
  #services .service-story .eyebrow,#services .service-story h3,#services .service-story p,#services .service-story a{position:absolute;left:20px;right:18px;color:#fff;z-index:2}
  #services .service-story .eyebrow{bottom:92px;color:#bdeaff;font-size:7px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
  #services .service-story .eyebrow:before{background:#7bd8ff}
  #services .service-story h3{bottom:39px;margin:0;font-size:clamp(17px,1.55vw,25px);line-height:1.03;letter-spacing:-.035em;max-width:420px;transition:bottom .6s cubic-bezier(.16,1,.3,1),font-size .6s}
  #services .service-story p{bottom:48px;margin:0;max-width:470px;font-size:9.5px;line-height:1.55;color:#d7e7ee;opacity:0;transform:translateY(12px);pointer-events:none;transition:opacity .4s,transform .55s cubic-bezier(.16,1,.3,1)}
  #services .service-story a{bottom:18px;font-size:8.5px;color:#9edfff;opacity:0;transform:translateY(8px);transition:opacity .4s .06s,transform .55s .06s cubic-bezier(.16,1,.3,1)}
  #services .service-story.active-story h3{bottom:112px;font-size:clamp(25px,2.35vw,36px)}
  #services .service-story.active-story p,#services .service-story.active-story a{opacity:1;transform:none}
  #services .service-story.active-story .eyebrow{bottom:164px}
}
#offers .plan-card{position:relative;transform-style:preserve-3d;transform:perspective(900px) rotateX(var(--plan-rx,0deg)) rotateY(var(--plan-ry,0deg)) translateY(var(--plan-lift,0px));transition:transform .22s ease-out,box-shadow .35s,border-color .35s}
#offers .plan-card:after{content:"";position:absolute;inset:0;border-radius:inherit;pointer-events:none;background:radial-gradient(260px circle at var(--plan-x,50%) var(--plan-y,50%),rgba(29,158,211,.13),transparent 64%);opacity:0;transition:opacity .3s}
#offers .plan-card:hover:after{opacity:1}#offers .plan-card:hover{--plan-lift:-7px;box-shadow:0 25px 55px rgba(23,49,66,.13)}
.png-art{position:relative;overflow:hidden}.png-signal-scan{position:absolute;inset:0;pointer-events:none;opacity:0;transition:opacity .35s;background:radial-gradient(145px circle at var(--scan-x,50%) var(--scan-y,50%),rgba(128,227,255,.36),rgba(8,117,201,.12) 34%,transparent 72%)}.png-art.scan-live .png-signal-scan{opacity:1}.png-signal-scan:after{content:"";position:absolute;left:var(--scan-x,50%);top:0;bottom:0;width:1px;background:linear-gradient(transparent,rgba(152,234,255,.8),transparent);box-shadow:0 0 12px rgba(83,198,243,.45);transform:translateX(-50%)}
.png-hotspot{position:absolute;width:9px;height:9px;border-radius:50%;background:#aeeaff;box-shadow:0 0 0 0 rgba(126,218,255,.5);pointer-events:none;opacity:.9;animation:d40Ping 2.1s ease-out infinite}.png-hotspot.h1{left:28%;top:35%}.png-hotspot.h2{left:58%;top:52%;animation-delay:.65s}.png-hotspot.h3{left:74%;top:30%;animation-delay:1.25s}@keyframes d40Ping{70%,100%{box-shadow:0 0 0 18px rgba(126,218,255,0);opacity:.42}}
@media(prefers-reduced-motion:reduce){#offers .plan-card{transform:none!important}.png-hotspot{animation:none!important}}
'''

js40=r'''
(()=>{
  const fine=matchMedia('(hover:hover) and (pointer:fine)').matches;
  const stories=[...document.querySelectorAll('#services .service-story')];
  if(stories.length){
    let active=0;
    const setActive=i=>{active=i;stories.forEach((c,n)=>c.classList.toggle('active-story',n===i));};
    setActive(0);
    stories.forEach((card,i)=>{
      card.tabIndex=0;
      card.addEventListener('mouseenter',()=>setActive(i));
      card.addEventListener('focusin',()=>setActive(i));
      if(fine)card.addEventListener('pointermove',e=>{
        const r=card.getBoundingClientRect(),x=(e.clientX-r.left)/r.width-.5,y=(e.clientY-r.top)/r.height-.5;
        card.style.setProperty('--story-x',(x*-10).toFixed(2)+'px');
        card.style.setProperty('--story-y',(y*-7).toFixed(2)+'px');
      });
      card.addEventListener('pointerleave',()=>{card.style.setProperty('--story-x','0px');card.style.setProperty('--story-y','0px');});
    });
  }
  if(fine)document.querySelectorAll('#offers .plan-card').forEach(card=>{
    card.addEventListener('pointermove',e=>{
      const r=card.getBoundingClientRect(),x=(e.clientX-r.left)/r.width,y=(e.clientY-r.top)/r.height;
      card.style.setProperty('--plan-x',(x*100).toFixed(1)+'%');card.style.setProperty('--plan-y',(y*100).toFixed(1)+'%');
      card.style.setProperty('--plan-rx',((.5-y)*4.5).toFixed(2)+'deg');card.style.setProperty('--plan-ry',((x-.5)*5.5).toFixed(2)+'deg');
    });
    card.addEventListener('pointerleave',()=>{card.style.setProperty('--plan-rx','0deg');card.style.setProperty('--plan-ry','0deg');});
  });
  const art=document.querySelector('.png-art');
  if(art){
    const scan=document.createElement('div');scan.className='png-signal-scan';
    scan.innerHTML='<i class="png-hotspot h1"></i><i class="png-hotspot h2"></i><i class="png-hotspot h3"></i>';
    art.appendChild(scan);
    if(fine){
      art.addEventListener('pointerenter',()=>art.classList.add('scan-live'));
      art.addEventListener('pointerleave',()=>art.classList.remove('scan-live'));
      art.addEventListener('pointermove',e=>{const r=art.getBoundingClientRect();art.style.setProperty('--scan-x',((e.clientX-r.left)/r.width*100).toFixed(1)+'%');art.style.setProperty('--scan-y',((e.clientY-r.top)/r.height*100).toFixed(1)+'%');});
    }
  }
})();
'''

css41=r'''
/* D40-D41 CRAZY ENHANCEMENTS */
#offers .offer-deck{perspective:1200px;transform-style:preserve-3d}
#offers .offer-feature,#offers .offer-card{transform-style:preserve-3d;will-change:transform;transform:perspective(950px) rotateX(var(--offer-rx,0deg)) rotateY(var(--offer-ry,0deg)) translate3d(var(--offer-tx,0px),var(--offer-ty,0px),var(--offer-z,0px));transition:transform .24s ease-out,box-shadow .55s var(--ease),filter .55s,opacity .55s}
#offers .offer-deck.offer-focus .offer-feature:not(.offer-active),#offers .offer-deck.offer-focus .offer-card:not(.offer-active){filter:saturate(.72) brightness(.95);opacity:.72}
#offers .offer-feature.offer-active,#offers .offer-card.offer-active{--offer-z:34px;box-shadow:0 35px 80px rgba(8,45,70,.18)}
.service-photo{position:relative;overflow:hidden;transform-style:preserve-3d;transform:perspective(950px) rotateX(var(--service-rx,0deg)) rotateY(var(--service-ry,0deg));transition:transform .22s ease-out,box-shadow .55s var(--ease);box-shadow:0 24px 55px rgba(8,45,70,.1)}
.service-photo:after{content:"";position:absolute;inset:0;pointer-events:none;background:radial-gradient(210px circle at var(--service-x,50%) var(--service-y,50%),rgba(156,232,255,.28),transparent 65%);mix-blend-mode:screen;opacity:.25;transition:opacity .3s}.service-photo:hover:after{opacity:.72}.service-photo img{transform:scale(1.03) translate3d(var(--service-img-x,0px),var(--service-img-y,0px),0);transition:transform .25s ease-out,filter 1.2s var(--ease)}
.signal .data-packet{fill:#fff;filter:drop-shadow(0 0 8px #77d9ff);opacity:.96}.signal .data-packet.green{fill:#baf2cd;filter:drop-shadow(0 0 8px #75d09a)}
.story-main,.story-small,.story-badge{will-change:transform;transition:transform .28s ease-out,filter .55s var(--ease)}
.story-collage.story-shuffle .story-main{animation:d41MainShuffle .72s cubic-bezier(.16,1,.3,1)}.story-collage.story-shuffle .story-small{animation:d41SmallShuffle .72s .05s cubic-bezier(.16,1,.3,1)}.story-collage.story-shuffle .story-badge{animation:d41BadgeShuffle .72s .08s cubic-bezier(.16,1,.3,1)}
@keyframes d41MainShuffle{0%{transform:translate3d(var(--story-main-x,0px),var(--story-main-y,0px),0) rotate(0)}42%{transform:translate3d(calc(var(--story-main-x,0px) - 26px),calc(var(--story-main-y,0px) + 12px),0) rotate(-2.2deg) scale(.975)}100%{transform:translate3d(var(--story-main-x,0px),var(--story-main-y,0px),0) rotate(0)}}
@keyframes d41SmallShuffle{0%{transform:translate3d(var(--story-small-x,0px),var(--story-small-y,0px),0) rotate(0)}45%{transform:translate3d(calc(var(--story-small-x,0px) + 28px),calc(var(--story-small-y,0px) - 16px),0) rotate(3.1deg) scale(1.035)}100%{transform:translate3d(var(--story-small-x,0px),var(--story-small-y,0px),0) rotate(0)}}
@keyframes d41BadgeShuffle{50%{transform:translate3d(calc(var(--story-badge-x,0px) - 10px),calc(var(--story-badge-y,0px) - 18px),0) rotate(-8deg) scale(1.08)}}
@media(prefers-reduced-motion:reduce){#offers .offer-feature,#offers .offer-card,.service-photo,.story-main,.story-small,.story-badge{transform:none!important}.story-collage.story-shuffle>*{animation:none!important}}
'''

js41=r'''
(()=>{
  const fine=matchMedia('(hover:hover) and (pointer:fine)').matches;
  const reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
  const deck=document.querySelector('#offers .offer-deck');
  if(deck&&fine){
    const cards=[...deck.querySelectorAll('.offer-feature,.offer-card')];
    cards.forEach(card=>{
      card.addEventListener('pointerenter',()=>{deck.classList.add('offer-focus');cards.forEach(x=>x.classList.toggle('offer-active',x===card));});
      card.addEventListener('pointermove',e=>{const r=card.getBoundingClientRect(),x=(e.clientX-r.left)/r.width,y=(e.clientY-r.top)/r.height;card.style.setProperty('--offer-rx',((.5-y)*5).toFixed(2)+'deg');card.style.setProperty('--offer-ry',((x-.5)*6).toFixed(2)+'deg');card.style.setProperty('--offer-tx',((x-.5)*7).toFixed(2)+'px');card.style.setProperty('--offer-ty',((y-.5)*5).toFixed(2)+'px');});
      card.addEventListener('pointerleave',()=>{card.style.setProperty('--offer-rx','0deg');card.style.setProperty('--offer-ry','0deg');card.style.setProperty('--offer-tx','0px');card.style.setProperty('--offer-ty','0px');});
    });
    deck.addEventListener('pointerleave',()=>{deck.classList.remove('offer-focus');cards.forEach(x=>x.classList.remove('offer-active'));});
  }
  const servicePhoto=document.querySelector('.service-photo');
  if(servicePhoto&&fine){
    servicePhoto.addEventListener('pointermove',e=>{const r=servicePhoto.getBoundingClientRect(),x=(e.clientX-r.left)/r.width,y=(e.clientY-r.top)/r.height;servicePhoto.style.setProperty('--service-x',(x*100).toFixed(1)+'%');servicePhoto.style.setProperty('--service-y',(y*100).toFixed(1)+'%');servicePhoto.style.setProperty('--service-rx',((.5-y)*5).toFixed(2)+'deg');servicePhoto.style.setProperty('--service-ry',((x-.5)*6).toFixed(2)+'deg');servicePhoto.style.setProperty('--service-img-x',((x-.5)*-9).toFixed(2)+'px');servicePhoto.style.setProperty('--service-img-y',((y-.5)*-7).toFixed(2)+'px');});
    servicePhoto.addEventListener('pointerleave',()=>['--service-rx','--service-ry'].forEach(v=>servicePhoto.style.setProperty(v,'0deg')));
  }
  const signal=document.querySelector('.enterprise-media .signal svg');
  if(signal&&!reduce){
    const paths=[...signal.querySelectorAll('path')];
    const NS='http://www.w3.org/2000/svg';
    paths.forEach((path,pi)=>{
      [0,.48].forEach((offset,oi)=>{const c=document.createElementNS(NS,'circle');c.setAttribute('r',oi?'3.2':'4.6');c.setAttribute('class','data-packet'+(pi===1?' green':''));signal.appendChild(c);const len=path.getTotalLength(),speed=pi===0?6800:7600,start=performance.now()+offset*speed;const tick=now=>{const t=((now-start)%speed+speed)%speed/speed,p=path.getPointAtLength(t*len);c.setAttribute('cx',p.x);c.setAttribute('cy',p.y);requestAnimationFrame(tick)};requestAnimationFrame(tick);});
    });
  }
  const collage=document.querySelector('.story-collage');
  if(collage){
    if(fine)collage.addEventListener('pointermove',e=>{const r=collage.getBoundingClientRect(),x=(e.clientX-r.left)/r.width-.5,y=(e.clientY-r.top)/r.height-.5;collage.style.setProperty('--story-main-x',(x*12).toFixed(2)+'px');collage.style.setProperty('--story-main-y',(y*9).toFixed(2)+'px');collage.style.setProperty('--story-small-x',(x*-18).toFixed(2)+'px');collage.style.setProperty('--story-small-y',(y*-13).toFixed(2)+'px');collage.style.setProperty('--story-badge-x',(x*22).toFixed(2)+'px');collage.style.setProperty('--story-badge-y',(y*18).toFixed(2)+'px');const main=collage.querySelector('.story-main'),small=collage.querySelector('.story-small'),badge=collage.querySelector('.story-badge');if(main)main.style.transform=`translate3d(${(x*12).toFixed(2)}px,${(y*9).toFixed(2)}px,0)`;if(small)small.style.transform=`translate3d(${(x*-18).toFixed(2)}px,${(y*-13).toFixed(2)}px,0)`;if(badge)badge.style.transform=`translate3d(${(x*22).toFixed(2)}px,${(y*18).toFixed(2)}px,0) rotate(${(x*3).toFixed(2)}deg)`;});
    document.querySelectorAll('.story-step').forEach(btn=>btn.addEventListener('click',()=>{collage.classList.remove('story-shuffle');void collage.offsetWidth;collage.classList.add('story-shuffle');setTimeout(()=>collage.classList.remove('story-shuffle'),820);}));
  }
})();
'''

inject('40.html',css40,js40)
inject('41.html',css41,js41)
