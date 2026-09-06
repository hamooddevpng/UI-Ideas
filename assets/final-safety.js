(()=>{
  'use strict';
  if(window.__telikomFinalSafety) return;
  window.__telikomFinalSafety=true;

  const title=document.title||'';
  const variant=title.includes('Consumer Services Hub')?'consumer':title.includes('Connected Nation')?'nation':title.includes('Balanced Corporate')?'corporate':title.includes('National Connectivity')?'human':title.includes('Digital Self Service')?'executive':title.includes('Living Network')?'living':null;
  if(variant) document.body.dataset.feedbackVariant=variant;

  const css=document.createElement('style');
  css.textContent=`
    html,body{max-width:100%;overflow-x:hidden}img,video,canvas,svg{max-width:100%}img{height:auto}
    .w,.wrap,.inst-wrap,.fresh-nav-inner,.ap-inner,.cp-inner,.cg-inner,.glance-wrap{min-width:0}
    h1,h2,h3,h4,p,a,b,strong,small,span,li,td,th{overflow-wrap:break-word}
    .institutional-hero,.hero{isolation:isolate}

    /* Brand treatment requested in review */
    header img[src*='TPNGLOGO'],nav img[src*='TPNGLOGO'],.nav img[src*='TPNGLOGO'],.top img[src*='TPNGLOGO']{width:auto!important;max-width:225px!important;max-height:74px!important;object-fit:contain!important;filter:none!important;opacity:1!important}
    .telikom-brand-lockup{display:flex!important;align-items:center;gap:12px;min-width:max-content}
    .telikom-brand-slogan{display:block;font:700 10px/1.25 Inter,Arial,sans-serif;letter-spacing:.025em;color:#0875c9;max-width:142px;text-transform:none}
    footer img[src*='TPNGLOGO'],.footer img[src*='TPNGLOGO'],.foot img[src*='TPNGLOGO']{filter:none!important;opacity:1!important;background:#fff!important;padding:7px 10px!important;border-radius:8px!important;object-fit:contain!important;max-width:215px!important;height:auto!important;max-height:66px!important}

    /* Keep imagery much clearer: use brand-blue accents, not a heavy blue wash. */
    .institutional-hero .inst-bg{filter:saturate(1.02) brightness(1.12)!important}
    .institutional-hero .inst-bg:after{background:linear-gradient(90deg,rgba(8,20,28,.58) 0%,rgba(8,24,34,.26) 48%,rgba(0,0,0,.02) 82%)!important}
    .institutional-hero.consumer .inst-bg:after{background:linear-gradient(90deg,rgba(9,23,31,.56),rgba(9,30,42,.20) 50%,rgba(0,0,0,.01) 84%)!important}
    .institutional-hero.nation .inst-bg:after{background:linear-gradient(102deg,rgba(8,20,28,.62) 0 38%,rgba(8,117,201,.17) 58%,rgba(255,255,255,.02) 82%)!important}
    .institutional-hero.corporate .inst-bg:after{background:linear-gradient(90deg,rgba(17,24,29,.52),rgba(21,36,45,.18) 56%,rgba(0,0,0,0) 86%)!important}
    .institutional-hero.human .inst-bg:after{background:linear-gradient(90deg,rgba(7,19,25,.44),rgba(7,25,34,.12) 52%,rgba(0,0,0,0) 88%)!important}
    .institutional-hero.executive .inst-bg:after{background:linear-gradient(90deg,rgba(8,20,28,.57),rgba(8,117,201,.13) 53%,rgba(0,0,0,.01) 85%)!important}

    /* Make the five shared homepage heroes visibly different in composition, not just colour. */
    body[data-feedback-variant='consumer'] .institutional-hero{margin:18px 24px 0!important;border-radius:26px!important;overflow:hidden!important;box-shadow:0 22px 70px rgba(9,41,61,.15)}
    body[data-feedback-variant='consumer'] .institutional-hero .inst-wrap{grid-template-columns:1.1fr .7fr!important;align-items:end!important}
    body[data-feedback-variant='consumer'] .institutional-hero .inst-copy{padding-bottom:24px}
    body[data-feedback-variant='nation'] .institutional-hero{margin:0!important;border-radius:0!important;border-bottom:5px solid #0797dc!important}
    body[data-feedback-variant='nation'] .institutional-hero .inst-wrap{grid-template-columns:.82fr 1.18fr!important;min-height:590px!important}
    body[data-feedback-variant='nation'] .institutional-hero .inst-proof{justify-self:end!important;align-self:end!important;margin-bottom:44px!important;border-radius:2px!important}
    body[data-feedback-variant='corporate'] .institutional-hero{margin:28px auto!important;max-width:1380px!important;border-radius:4px!important;overflow:hidden!important;border-bottom:8px solid #0875c9!important}
    body[data-feedback-variant='corporate'] .institutional-hero .inst-wrap{grid-template-columns:1.25fr .55fr!important;min-height:520px!important}
    body[data-feedback-variant='human'] .institutional-hero{min-height:680px!important}
    body[data-feedback-variant='human'] .institutional-hero .inst-wrap{grid-template-columns:1fr!important;align-items:end!important;min-height:680px!important;padding-bottom:72px!important}
    body[data-feedback-variant='human'] .institutional-hero .inst-copy{max-width:760px!important;background:rgba(5,18,24,.36);backdrop-filter:blur(5px);padding:26px 28px;border-left:4px solid #0797dc}
    body[data-feedback-variant='human'] .institutional-hero .inst-proof{display:none!important}
    body[data-feedback-variant='executive'] .institutional-hero{margin:16px 16px 10px!important;border-radius:12px!important;overflow:hidden!important;min-height:455px!important}
    body[data-feedback-variant='executive'] .institutional-hero .inst-wrap{grid-template-columns:.9fr 1.1fr!important;min-height:455px!important;padding-top:44px!important;padding-bottom:54px!important}
    body[data-feedback-variant='executive'] .institutional-hero .inst-proof{align-self:stretch!important;border-radius:8px!important}

    /* Design 2 section: neutral blue-grey, no green. */
    body[data-unique-variant='nation'] .ux-nation{background:#eef3f7!important;color:#17364a!important;border-top:1px solid #d7e2ea!important;border-bottom:1px solid #d7e2ea!important}
    body[data-unique-variant='nation'] .ux-nation .ux-kicker{color:#0875c9!important}
    body[data-unique-variant='nation'] .ux-nation .ux-copy,body[data-unique-variant='nation'] .ux-ledger-row p{color:#647987!important}
    body[data-unique-variant='nation'] .ux-ledger{border-top-color:#cbd8e1!important}.ux-nation .ux-ledger-row{border-bottom-color:#cbd8e1!important}
    body[data-unique-variant='nation'] .ux-ledger-num{color:#0875c9!important}
    body[data-unique-variant='nation'] .ux-ledger-row h3,body[data-unique-variant='nation'] .ux-ledger-row a{color:#17364a!important}
    body[data-unique-variant='nation'] .ux-ledger-row a{background:#fff!important;border-color:#bdccd6!important}
    body[data-unique-variant='nation'] .ux-nation-note{background:#fff!important;color:#587080!important;border-left-color:#0797dc!important}

    /* Design 6: retain premium feel while allowing the background photography to breathe. */
    body[data-feedback-variant='living'] .hero-bg{filter:brightness(1.12) saturate(1.03)!important}
    body[data-feedback-variant='living'] .hero:after{opacity:.42!important}
    body[data-feedback-variant='living'] .hero-panel{background:rgba(4,20,31,.66)!important}

    /* Design 1 interactive chatbot */
    .telikom-chatbot{position:fixed;right:22px;bottom:22px;z-index:9999;width:min(330px,calc(100vw - 30px));font-family:Inter,Arial,sans-serif;filter:drop-shadow(0 18px 40px rgba(4,36,55,.25))}
    .telikom-chatbot .chat-pop{background:#fff;border:1px solid #dce8ef;border-radius:18px 18px 4px 18px;padding:14px 16px;margin:0 0 10px auto;width:265px;color:#17364a;font-size:13px;line-height:1.45;animation:chatIn .45s ease both}
    .telikom-chatbot .chat-pop b{display:block;color:#0875c9;margin-bottom:3px}.telikom-chatbot .chat-actions{display:none;background:#fff;border:1px solid #dce8ef;border-radius:16px;padding:10px;margin-bottom:10px}.telikom-chatbot.open .chat-actions{display:grid;gap:7px}.telikom-chatbot .chat-actions a{padding:10px 12px;border-radius:10px;background:#f3f8fb;color:#17364a;text-decoration:none;font-size:12px;font-weight:700}.telikom-chatbot .chat-actions a:hover{background:#e6f4fb;color:#0875c9}.telikom-chatbot button{margin-left:auto;width:58px;height:58px;border:0;border-radius:50%;background:linear-gradient(135deg,#0875c9,#0797dc);color:#fff;font-size:24px;display:grid;place-items:center;cursor:pointer;box-shadow:0 12px 28px rgba(8,117,201,.3)}
    @keyframes chatIn{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:none}}

    @media(max-width:900px){
      .telikom-brand-slogan{display:none}.telikom-brand-lockup{min-width:0}header img[src*='TPNGLOGO'],nav img[src*='TPNGLOGO'],.nav img[src*='TPNGLOGO']{max-width:170px!important;max-height:60px!important}
      body[data-feedback-variant='consumer'] .institutional-hero,body[data-feedback-variant='corporate'] .institutional-hero,body[data-feedback-variant='executive'] .institutional-hero{margin:8px!important;border-radius:14px!important}
      body[data-feedback-variant='consumer'] .institutional-hero .inst-wrap,body[data-feedback-variant='nation'] .institutional-hero .inst-wrap,body[data-feedback-variant='corporate'] .institutional-hero .inst-wrap,body[data-feedback-variant='executive'] .institutional-hero .inst-wrap{grid-template-columns:1fr!important}
      body[data-feedback-variant='human'] .institutional-hero,body[data-feedback-variant='human'] .institutional-hero .inst-wrap{min-height:560px!important}
      .telikom-chatbot{right:14px;bottom:14px}.telikom-chatbot .chat-pop{width:235px}
    }
  `;
  document.head.appendChild(css);

  const addBrandLockups=()=>{
    document.querySelectorAll('header img[src*="TPNGLOGO"],nav img[src*="TPNGLOGO"],.nav img[src*="TPNGLOGO"],.top img[src*="TPNGLOGO"]').forEach(img=>{
      if(img.closest('footer')||img.dataset.brandLockup)return;
      img.dataset.brandLockup='1';
      const parent=img.parentElement;if(!parent)return;
      parent.classList.add('telikom-brand-lockup');
      if(!parent.querySelector('.telikom-brand-slogan')){
        const s=document.createElement('span');s.className='telikom-brand-slogan';s.textContent='Connecting you anywhere anytime';parent.appendChild(s);
      }
    });
  };

  const addChatbot=()=>{
    if(variant!=='consumer'||document.querySelector('.telikom-chatbot'))return;
    const box=document.createElement('div');box.className='telikom-chatbot';box.innerHTML=`<div class="chat-pop"><b>Hello 👋</b>Need help with anything?</div><div class="chat-actions"><a href="#">Top Up & Buy Data</a><a href="#">Home Internet</a><a href="#">Business Services</a><a href="#">Contact Support</a></div><button type="button" aria-label="Open Telikom help">✦</button>`;
    const btn=box.querySelector('button');btn.addEventListener('click',()=>box.classList.toggle('open'));
    document.body.appendChild(box);
  };

  const fallback='https://blog.apnic.net/wp-content/uploads/2016/04/Goroka-EHP.jpg';
  const protectImages=()=>document.querySelectorAll('img').forEach(img=>{if(img.dataset.safeImage)return;img.dataset.safeImage='1';const isLogo=/TPNGLOGO|telikom/i.test(img.src||'')||/telikom/i.test(img.alt||'');if(isLogo)return;img.addEventListener('error',()=>{if(img.dataset.fallbackTried)return;img.dataset.fallbackTried='1';img.src=fallback},{once:true})});
  const sanitizeFakeStatus=()=>{document.querySelectorAll('.inst-network-console i,.gn-track i').forEach(el=>{el.removeAttribute('style');el.style.width='100%';el.style.opacity='.55'});document.querySelectorAll('.gn-status').forEach(el=>el.textContent='Service portfolio overview');document.querySelectorAll('.topline').forEach(el=>{el.innerHTML=el.innerHTML.replace(/Network Status:\s*Operational\s*&nbsp;\s*•\s*&nbsp;\s*/i,'')})};

  addBrandLockups();addChatbot();protectImages();sanitizeFakeStatus();
  const observer=new MutationObserver(()=>{addBrandLockups();protectImages();sanitizeFakeStatus()});observer.observe(document.documentElement,{childList:true,subtree:true});
})();