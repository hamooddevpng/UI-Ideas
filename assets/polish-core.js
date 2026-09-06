(() => {
  const run = () => {
    const title = document.title || '';
    const variant = title.includes('Consumer Services Hub') ? 'consumer' :
      title.includes('Connected Nation') ? 'nation' :
      title.includes('Balanced Corporate') ? 'corporate' :
      title.includes('National Connectivity') ? 'human' : 'executive';

    const logoSrc = 'https://www.telikom.com.pg/assets/misc/TPNGLOGO.png';
    const imgBase = 'https://telikom-frontend.vercel.app/images/png/';

    const style = document.createElement('style');
    style.textContent = `
      :root{--p-blue:#0875c9;--p-blue2:#1599d4;--p-navy:#062f4d;--p-deep:#031f34;--p-ink:#102b43;--p-muted:#667b8b;--p-line:#d8e4ec;--p-sky:#eaf5fd;--p-ease:cubic-bezier(.22,.61,.36,1)}
      html{scroll-behavior:smooth} body{font-size:16px!important}
      body p,body li,body td,body input,body button,body a{font-size:14px}
      body small{font-size:12px}
      .view:after,.institutional-link:after{content:' →'}
      .view{white-space:nowrap}
      .btn{cursor:pointer}

      /* shared institutional hero; different visual treatment per concept */
      .institutional-hero{position:relative;overflow:hidden;color:#fff;background:#062f4d;border-bottom:1px solid rgba(255,255,255,.08)}
      .institutional-hero .inst-slide{display:none;min-height:610px;position:relative;isolation:isolate}
      .institutional-hero .inst-slide.active{display:block;animation:instFade .58s var(--p-ease)}
      .institutional-hero .inst-bg{position:absolute;inset:0;z-index:-2;background-size:cover;background-position:center;transform:scale(1.015)}
      .institutional-hero .inst-bg:after{content:'';position:absolute;inset:0;background:linear-gradient(90deg,rgba(2,32,52,.96),rgba(3,47,76,.80) 45%,rgba(3,47,76,.20) 78%)}
      .institutional-hero.nation .inst-bg:after{background:linear-gradient(90deg,rgba(1,29,48,.98),rgba(3,47,76,.91) 50%,rgba(8,117,201,.20))}
      .institutional-hero.corporate .inst-bg:after{background:linear-gradient(90deg,rgba(5,42,65,.92),rgba(6,66,103,.68) 52%,rgba(6,66,103,.10))}
      .institutional-hero.human .inst-bg:after{background:linear-gradient(90deg,rgba(4,38,62,.87),rgba(4,38,62,.48) 52%,rgba(4,38,62,.10))}
      .institutional-hero.executive .inst-bg:after{background:linear-gradient(90deg,rgba(3,31,52,.98),rgba(5,55,88,.90) 55%,rgba(8,117,201,.18))}
      .institutional-hero:before{content:'';position:absolute;inset:0;pointer-events:none;background-image:linear-gradient(rgba(255,255,255,.022) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.022) 1px,transparent 1px);background-size:48px 48px;opacity:.55}
      .inst-wrap{max-width:1360px;margin:auto;padding:78px 32px 96px;display:grid;grid-template-columns:minmax(0,1.2fr) minmax(360px,.8fr);gap:48px;align-items:end;min-height:610px;position:relative;z-index:2}
      .inst-copy{max-width:780px}.inst-kicker{display:inline-flex;align-items:center;gap:9px;padding:8px 12px;border:1px solid rgba(255,255,255,.25);border-radius:999px;background:rgba(255,255,255,.08);backdrop-filter:blur(8px);font-size:12px!important;font-weight:800;letter-spacing:.08em;text-transform:uppercase}
      .inst-kicker:before{content:'';width:7px;height:7px;border-radius:50%;background:#53c2ff;box-shadow:0 0 0 5px rgba(83,194,255,.12)}
      .inst-copy h1{font:800 clamp(48px,5.7vw,76px)/.98 Manrope,Inter,sans-serif;letter-spacing:-2.5px;margin:20px 0 18px;max-width:880px}.inst-copy p{font-size:18px!important;line-height:1.7;max-width:710px;color:#d9ebf5;margin:0 0 28px}
      .inst-actions{display:flex;gap:12px;flex-wrap:wrap}.inst-actions a{display:inline-flex;align-items:center;justify-content:center;gap:8px;min-height:48px;padding:12px 19px;border-radius:8px;text-decoration:none;font-weight:800;font-size:14px!important;background:#0b87d8;color:#fff;border:1px solid #2fa7f0;box-shadow:0 10px 28px rgba(1,28,46,.24)}.inst-actions a.alt{background:rgba(255,255,255,.08);border-color:rgba(255,255,255,.36);backdrop-filter:blur(10px)}
      .inst-proof{align-self:end;background:rgba(3,39,63,.78);border:1px solid rgba(255,255,255,.16);border-radius:16px;padding:24px;box-shadow:0 24px 60px rgba(0,0,0,.22);backdrop-filter:blur(14px)}.inst-proof .proof-label{font-size:11px!important;letter-spacing:.09em;text-transform:uppercase;color:#9edbff;font-weight:800}.inst-proof h3{font:800 23px Manrope;margin:8px 0 16px}.inst-proof-grid{display:grid;grid-template-columns:1fr 1fr;gap:9px}.inst-proof-grid div{padding:13px;border-radius:9px;background:rgba(255,255,255,.055);border:1px solid rgba(255,255,255,.10)}.inst-proof-grid b{display:block;font-size:14px!important}.inst-proof-grid small{color:#bdd5e4!important;font-size:12px!important}
      .inst-controls{position:absolute;z-index:5;left:50%;transform:translateX(-50%);bottom:24px;display:flex;align-items:center;gap:12px}.inst-dots{display:flex;gap:7px}.inst-dots button{width:28px;height:4px;padding:0;border:0;border-radius:999px;background:rgba(255,255,255,.38);cursor:pointer;transition:.25s}.inst-dots button.active{width:48px;background:#fff}.inst-arrow{width:38px;height:38px;border-radius:50%;border:1px solid rgba(255,255,255,.28);background:rgba(3,38,61,.55);color:#fff;display:grid;place-items:center;cursor:pointer;font-size:18px;backdrop-filter:blur(8px)}
      @keyframes instFade{from{opacity:.25;transform:scale(1.004)}to{opacity:1;transform:none}}

      /* proof bar */
      .national-proof-strip{background:#fff;border-bottom:1px solid var(--p-line);box-shadow:0 10px 28px rgba(7,46,73,.05)}.national-proof-inner{max-width:1360px;margin:auto;padding:0 32px;display:grid;grid-template-columns:repeat(5,1fr)}.national-proof-item{padding:18px 16px;border-right:1px solid #e9eff3;display:flex;gap:12px;align-items:center}.national-proof-item:first-child{border-left:1px solid #e9eff3}.national-proof-icon{width:37px;height:37px;border-radius:10px;background:#eaf5fd;color:#0875c9;display:grid;place-items:center;font-weight:900}.national-proof-item b{display:block;font-size:14px!important;color:#15344a}.national-proof-item small{display:block;color:#6d8090!important;font-size:12px!important;margin-top:2px}

      /* latest frontend content spotlight */
      .current-portfolio{padding:66px 28px;background:linear-gradient(180deg,#f7fafc,#eef4f7);border-block:1px solid #e1eaf0}.cp-inner{max-width:1260px;margin:auto}.cp-head{display:flex;align-items:end;justify-content:space-between;gap:24px;margin-bottom:24px}.cp-head small{font-size:11px!important;letter-spacing:.1em;text-transform:uppercase;color:#0875c9;font-weight:800}.cp-head h2{font:800 34px Manrope;margin:6px 0 0;letter-spacing:-.9px}.cp-head p{max-width:720px;color:#687b8a;margin:7px 0 0}.cp-grid{display:grid;grid-template-columns:1.15fr .85fr .85fr;gap:14px}.cp-card{min-height:260px;border-radius:14px;border:1px solid #d7e3eb;background:#fff;padding:24px;position:relative;overflow:hidden;box-shadow:0 10px 28px rgba(8,44,68,.055);transition:.28s var(--p-ease)}.cp-card:hover{transform:translateY(-4px);box-shadow:0 18px 38px rgba(8,44,68,.11)}.cp-card.hero-card{min-height:390px;color:#fff;display:flex;align-items:flex-end;background:linear-gradient(180deg,rgba(3,40,63,.08),rgba(3,40,63,.92)),url('${imgBase}png_starlink_dish_horizon.png') center/cover}.cp-card .cp-kicker{font-size:11px!important;letter-spacing:.08em;text-transform:uppercase;color:#0875c9;font-weight:800}.cp-card.hero-card .cp-kicker{color:#92d8ff}.cp-card h3{font:800 22px Manrope;margin:8px 0}.cp-card.hero-card h3{font-size:31px}.cp-card p{color:#6b7e8d;font-size:14px!important;line-height:1.6}.cp-card.hero-card p{color:#d6e8f2}.cp-card a{display:inline-flex;margin-top:13px;text-decoration:none;color:#0875c9;font-weight:800;font-size:14px!important}.cp-card.hero-card a{color:#fff}.cp-stack{display:grid;gap:14px}.cp-mini{border:1px solid #d7e3eb;border-radius:14px;background:#fff;padding:20px;min-height:188px}.cp-mini b{display:block;font:800 18px Manrope;margin-bottom:6px}.cp-mini p{font-size:13px!important;color:#6c7f8e;margin:0 0 10px}.cp-mini a{color:#0875c9;text-decoration:none;font-weight:800;font-size:13px!important}

      /* public/company navigation additions */
      .company-gateway{padding:62px 28px;background:#fff}.cg-inner{max-width:1260px;margin:auto}.cg-head{margin-bottom:22px}.cg-head small{font-size:11px!important;letter-spacing:.1em;color:#0875c9;font-weight:800}.cg-head h2{font:800 31px Manrope;margin:6px 0}.cg-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:12px}.cg-card{border:1px solid #d9e4eb;border-radius:12px;padding:20px;background:linear-gradient(180deg,#fff,#f9fbfc);min-height:155px;position:relative}.cg-card:after{content:'→';position:absolute;right:17px;bottom:15px;color:#0875c9;font-weight:900}.cg-card b{display:block;font:800 17px Manrope;margin-bottom:6px}.cg-card p{font-size:13px!important;color:#6b7e8e;margin:0 0 22px;line-height:1.55}

      /* scroll polish */
      .reveal{opacity:0;transform:translateY(16px);transition:opacity .68s var(--p-ease),transform .68s var(--p-ease)}.reveal.is-visible{opacity:1;transform:none}.reveal-delay-1{transition-delay:.06s}.reveal-delay-2{transition-delay:.12s}.reveal-delay-3{transition-delay:.18s}
      .panel,.plan,.device,.svc,.tile,.service,.story,.box,.metric,.action,.public-card,.fresh-nav-card{transition:transform .24s var(--p-ease),box-shadow .24s var(--p-ease),border-color .24s var(--p-ease)}
      .panel:hover,.plan:hover,.device:hover,.svc:hover,.tile:hover,.service:hover,.story:hover,.box:hover,.action:hover{transform:translateY(-2px)}
      img[loading='lazy']{content-visibility:auto}
      @media(prefers-reduced-motion:reduce){*,*:before,*:after{animation-duration:.01ms!important;transition-duration:.01ms!important;scroll-behavior:auto!important}.reveal{opacity:1!important;transform:none!important}}
      @media(max-width:1050px){.inst-wrap{grid-template-columns:1fr;align-items:center}.inst-proof{max-width:620px}.national-proof-inner{grid-template-columns:repeat(3,1fr)}.cp-grid{grid-template-columns:1fr 1fr}.cp-card.hero-card{grid-column:span 2}.cg-grid{grid-template-columns:1fr 1fr}}
      @media(max-width:700px){.inst-wrap{padding:56px 20px 84px}.institutional-hero .inst-slide{min-height:680px}.inst-copy h1{font-size:44px}.inst-copy p{font-size:16px!important}.inst-proof-grid{grid-template-columns:1fr 1fr}.national-proof-inner{grid-template-columns:1fr 1fr;padding:0 18px}.cp-grid,.cg-grid{grid-template-columns:1fr}.cp-card.hero-card{grid-column:auto}.current-portfolio,.company-gateway{padding-left:18px;padding-right:18px}}
    `;
    document.head.appendChild(style);

    const slideSets = {
      consumer: [
        {k:'PNG National Pride & 4G LTE Network',t:'Connecting Papua New Guinea',s:'Proudly PNG owned. Connecting people and communities.',d:'A clear gateway to mobile services, home connectivity, devices, account tools and support across Papua New Guinea.',p:'Explore Personal Services',q:'Recharge & Self Care',img:'png_flag_people_celebration.png'},
        {k:'Unlimited Broadband',t:'Home connectivity built for everyday life',s:'Affordable Home Data, U-TOKMoa and entertainment options.',d:'Bring fixed services to the forefront so households can quickly discover the right home plan and understand what Telikom offers today.',p:'Explore Home & Fixed',q:'View U-TOKMoa',img:'png_coastal_volcano_landscape.png'},
        {k:'Phones, tablets & connectivity hardware',t:'Devices that keep PNG connected',s:'Make product discovery part of the homepage journey.',d:'Surface phones, tablets, MiFi, routers and current offers alongside store locations and support.',p:'Browse Devices',q:'Find a Store',img:'png_devices_routers_banner.png'}
      ],
      nation: [
        {k:'National telecommunications infrastructure',t:'One network serving every sector',s:'People, businesses, government and communities.',d:'Present Telikom as a national operator with mobile, fixed, enterprise and remote connectivity capability.',p:'Explore Services',q:'View Network Updates',img:'png_highlands_landscape.png'},
        {k:'Enterprise Solutions',t:'Infrastructure for PNG organisations',s:'Business Data, Co-Location, Business Systems and managed connectivity.',d:'Give organisations an immediate route into Telikom fixed business and mobile business services.',p:'Business Services',q:'Contact Sales',img:'png_coastal_volcano_landscape.png'},
        {k:'Remote connectivity',t:'Starlink Enterprise & Telikom VSAT',s:'Current remote-connectivity options for difficult locations.',d:'Telikom’s new frontend specifically surfaces Starlink Enterprise integration alongside VSAT powered by Kacific for remote facilities.',p:'Explore Satellite',q:'Business Enquiry',img:'png_starlink_dish_horizon.png'}
      ],
      corporate: [
        {k:'Fast, reliable, local',t:'Connecting Papua New Guinea with confidence',s:'A balanced corporate gateway for personal and business customers.',d:'A clear, executive-friendly homepage that directs visitors to current Telikom services without making them hunt.',p:'Personal Services',q:'Business Services',img:'png_flag_people_celebration.png'},
        {k:'Enterprise Business Cloud',t:'Powering PNG business and public services',s:'Scalable data, fixed, mobile and remote connectivity.',d:'Bring Business Data, Business Systems, Co-Location, CUG/PUG and satellite options into a stronger corporate story.',p:'Explore Business',q:'Request a Quote',img:'png_highlands_landscape.png'},
        {k:'Triple-play home experience',t:'Home Entertainment, broadband and voice',s:'One route into the current home portfolio.',d:'The new frontend includes Home Entertainment Packages alongside Affordable Home Data, U-TOKMoa and Special Home Passes.',p:'Explore Home Packages',q:'View Coverage',img:'png_coastal_volcano_landscape.png'}
      ],
      human: [
        {k:'PNG National Pride',t:'Together, wherever life takes you',s:'Connectivity with a distinctly Papua New Guinean identity.',d:'Lead with people and place, then make the paths to mobile, home, business and support immediately visible.',p:'Find My Service',q:'Check Coverage',img:'png_flag_people_celebration.png'},
        {k:'Connecting remote communities',t:'From highlands to islands',s:'VSAT and Starlink Enterprise extend the reach of digital access.',d:'Use remote-connectivity imagery and current product pathways to tell a stronger national inclusion story.',p:'Remote Connectivity',q:'Business Services',img:'png_starlink_dish_horizon.png'},
        {k:'Home & community connectivity',t:'More ways for households to connect',s:'Affordable Home Data, U-TOKMoa and Home Entertainment.',d:'Show current home services in a human context instead of treating them as secondary product pages.',p:'Explore Home',q:'Find a Store',img:'png_coastal_volcano_landscape.png'}
      ],
      executive: [
        {k:'Digital self-service',t:'Your Telikom services, easier to reach',s:'Account tools and high-priority destinations in one place.',d:'Self Care, plan discovery, support, stores and current service categories are surfaced as a practical digital dashboard.',p:'Open Self Care',q:'View Plans',img:'png_devices_routers_banner.png'},
        {k:'Business & enterprise',t:'Connectivity for complex organisations',s:'Fixed business, mobile business and enterprise satellite solutions.',d:'A direct path into Data, Co-Location, Business Systems, CUG/PUG, roaming, VSAT and Starlink Enterprise integration.',p:'Explore Business',q:'Contact Sales',img:'png_highlands_landscape.png'},
        {k:'Network reach',t:'Remote connectivity without the guesswork',s:'Make satellite options visible from the first screen.',d:'The current frontend explicitly highlights VSAT powered by Kacific and Starlink Enterprise integration for remote sites.',p:'Satellite Services',q:'Check Support',img:'png_starlink_dish_horizon.png'}
      ]
    };

    const slides = slideSets[variant];
    const hero = document.createElement('section');
    hero.className = `institutional-hero ${variant}`;
    hero.innerHTML = slides.map((s,i)=>`<article class="inst-slide ${i===0?'active':''}" data-index="${i}"><div class="inst-bg" style="background-image:url('${imgBase}${s.img}')"></div><div class="inst-wrap"><div class="inst-copy"><span class="inst-kicker">${s.k}</span><h1>${s.t}</h1><p><strong style="display:block;color:#fff;margin-bottom:6px">${s.s}</strong>${s.d}</p><div class="inst-actions"><a href="#">${s.p}</a><a class="alt" href="#">${s.q}</a></div></div><aside class="inst-proof"><span class="proof-label">Telikom at a glance</span><h3>${variant==='nation'?'National capability':'Clear pathways from the homepage'}</h3><div class="inst-proof-grid"><div><b>Personal</b><small>Mobile & fixed services</small></div><div><b>Business</b><small>Fixed & mobile solutions</small></div><div><b>Remote</b><small>VSAT & Starlink Enterprise</small></div><div><b>Support</b><small>Stores, FAQs & Self Care</small></div></div></aside></div></article>`).join('') + `<div class="inst-controls"><button class="inst-arrow inst-prev" aria-label="Previous slide">‹</button><div class="inst-dots">${slides.map((_,i)=>`<button class="${i===0?'active':''}" aria-label="Go to slide ${i+1}" data-to="${i}"></button>`).join('')}</div><button class="inst-arrow inst-next" aria-label="Next slide">›</button></div>`;

    const originalHero = document.querySelector('.hero, header.hero, .heroRow, .welcome');
    if (originalHero) {
      const heroContainer = originalHero.classList?.contains('heroRow') ? originalHero : originalHero;
      heroContainer.insertAdjacentElement('beforebegin',hero);
      if (heroContainer.classList?.contains('heroRow')) heroContainer.remove(); else originalHero.remove();
    } else {
      const nav = document.querySelector('nav');
      if (nav) nav.insertAdjacentElement('afterend',hero);
    }

    const proof = document.createElement('div');
    proof.className='national-proof-strip';
    proof.innerHTML=`<div class="national-proof-inner"><div class="national-proof-item"><span class="national-proof-icon">PNG</span><div><b>Proudly PNG Owned</b><small>National telecommunications company</small></div></div><div class="national-proof-item"><span class="national-proof-icon">4G</span><div><b>Mobile & Data</b><small>Personal service pathways</small></div></div><div class="national-proof-item"><span class="national-proof-icon">⌂</span><div><b>Home & Fixed</b><small>U-TOKMoa, data & entertainment</small></div></div><div class="national-proof-item"><span class="national-proof-icon">✦</span><div><b>Remote Connectivity</b><small>VSAT & Starlink Enterprise</small></div></div><div class="national-proof-item"><span class="national-proof-icon">?</span><div><b>Support & Stores</b><small>FAQs, locations and account help</small></div></div></div>`;
    hero.insertAdjacentElement('afterend',proof);

    /* Current-project content spotlight derived from supplied frontend */
    const portfolio = document.createElement('section');
    portfolio.className='current-portfolio';
    portfolio.innerHTML=`<div class="cp-inner"><div class="cp-head"><div><small>From the current Telikom frontend</small><h2>Current services worth surfacing on the homepage</h2><p>The newer project contains several important destinations that were under-represented in our earlier mocks. These are now promoted as first-class homepage journeys.</p></div></div><div class="cp-grid"><article class="cp-card hero-card"><div><span class="cp-kicker">Remote connectivity</span><h3>Starlink Enterprise & Telikom VSAT</h3><p>Starlink Enterprise integration sits alongside Telikom VSAT powered by Kacific in the current business fixed experience, especially for remote facilities.</p><a href="#">Explore remote connectivity →</a></div></article><div class="cp-stack"><div class="cp-mini"><b>U-TOKMoa Home Voice & Data</b><p>Dedicated current frontend pages for U-TOKMoa fixed voice and data combo plans.</p><a href="#">View U-TOKMoa →</a></div><div class="cp-mini"><b>Home Entertainment Package</b><p>Residential broadband data, Telikom TV access and fixed voice packaged together.</p><a href="#">Explore entertainment →</a></div></div><div class="cp-stack"><div class="cp-mini"><b>International & Roaming</b><p>International Call Plans, roaming bundles and business roaming are explicit current service categories.</p><a href="#">View mobile categories →</a></div><div class="cp-mini"><b>CUG / PUG Business Mobile</b><p>Closed User Group and Prepaid User Group solutions for organisational fleets and staff.</p><a href="#">Explore business mobile →</a></div></div></div></div>`;

    const insertionTarget = document.querySelector('.fresh-nav-hub') || proof;
    insertionTarget.insertAdjacentElement('afterend', portfolio);

    const companyGateway = document.createElement('section');
    companyGateway.className='company-gateway';
    companyGateway.innerHTML=`<div class="cg-inner"><div class="cg-head"><small>Company & service information</small><h2>Important pages should be visible, not hidden</h2></div><div class="cg-grid"><article class="cg-card"><b>News & Media</b><p>All News, Public Notices, Promotions & Offers, Network Updates, Press Releases, Community & CSR and Media Kit.</p></article><article class="cg-card"><b>Store Locator</b><p>Dedicated retail-location journey for customers who need a Telikom store or service point.</p></article><article class="cg-card"><b>About Telikom</b><p>Company overview, executive leadership, board, CSR, subsidiaries and the Telikom Foundation.</p></article><article class="cg-card"><b>Careers</b><p>Current job openings, application process and reasons to build a career with Telikom.</p></article></div></div>`;

    const footer = document.querySelector('footer');
    if (footer) footer.insertAdjacentElement('beforebegin',companyGateway);

    /* Load the source-truth navigation hub on every mock, even older HTML files */
    if (!document.querySelector('script[data-fresh-nav]')) {
      const s=document.createElement('script'); s.src='assets/fresh-nav.js'; s.defer=true; s.dataset.freshNav='1'; document.body.appendChild(s);
    }

    /* Slider controls */
    let current=0, timer=null;
    const show=(i)=>{const els=[...hero.querySelectorAll('.inst-slide')],dots=[...hero.querySelectorAll('.inst-dots button')];current=(i+els.length)%els.length;els.forEach((e,j)=>e.classList.toggle('active',j===current));dots.forEach((d,j)=>d.classList.toggle('active',j===current));};
    hero.querySelector('.inst-prev')?.addEventListener('click',()=>show(current-1));hero.querySelector('.inst-next')?.addEventListener('click',()=>show(current+1));hero.querySelectorAll('.inst-dots button').forEach(b=>b.addEventListener('click',()=>show(+b.dataset.to)));
    const start=()=>{timer=setInterval(()=>show(current+1),6500)}; const stop=()=>{if(timer)clearInterval(timer)}; start(); hero.addEventListener('mouseenter',stop); hero.addEventListener('mouseleave',start);

    /* lazy images + reveal */
    document.querySelectorAll('img').forEach((img,i)=>{if(!img.alt)img.alt=i===0?'Telikom PNG':'Telikom content image';if(img.src!==logoSrc&&!img.closest('.institutional-hero')){img.loading='lazy';img.decoding='async'}else img.fetchPriority='high'});
    const revealTargets=[...document.querySelectorAll('section,.dock,.quick,.panel,.plan,.device,.story,.news,.biz,.svc,.tile,.metric,.solution,.tool,.action,.box,.service')].filter(e=>!e.closest('.institutional-hero'));
    revealTargets.forEach((el,i)=>{el.classList.add('reveal');if(i%4)el.classList.add(`reveal-delay-${i%4}`)});
    if('IntersectionObserver' in window){const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('is-visible');io.unobserve(e.target)}}),{rootMargin:'0px 0px -6% 0px',threshold:.06});revealTargets.forEach(el=>io.observe(el))}else revealTargets.forEach(el=>el.classList.add('is-visible'));

    /* remove literal arrows where CSS supplies them */
    document.querySelectorAll('.view,.institutional-link').forEach(a=>{a.textContent=a.textContent.replace(/\s*[→➜➝]+\s*$/,'')});
  };
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',run,{once:true});else run();
})();
