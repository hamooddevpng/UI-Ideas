/*
 * Design 42 shell sync
 * Mirrors the Concise Home navigation, footer destinations and effective metadata
 * while preserving Design 42's own visual system and page behavior.
 */
(()=>{
  const NAV_ITEMS=[
    {
      title:'Home',href:'/',items:[
        {title:'Current Home Page',href:'/'},
        {title:'Concise Home Page',href:'/home-4'},
        {title:'Offer Led Customer Focus',href:'/home-2'},
        {title:'PNG Connectivity',href:'/home-3'}
      ]
    },
    {
      title:'Personal',href:'/personal/mobile',items:[
        {title:'Fixed Services',href:'/personal/fixed/affordable-home-data',subItems:[
          {title:'Affordable Home Data',href:'/personal/fixed/affordable-home-data'},
          {title:'U-TOKMoa Plans',href:'/personal/fixed/u-tokmoa-plans'},
          {title:'Special Home Plans',href:'/personal/fixed/special-home-passes'}
        ]},
        {title:'Mobile Services',href:'/personal/mobile',subItems:[
          {title:'Gutpela Mobile Data Plans',href:'/personal/mobile?cat=gutpela'},
          {title:'MOA Plus Packs',href:'/personal/mobile?cat=moa-combo'},
          {title:'International Call Plans',href:'/personal/mobile?cat=international'},
          {title:'Special Passes',href:'/personal/mobile?cat=special'},
          {title:'Roaming Bundles',href:'/personal/mobile?cat=roaming'}
        ]},
        {title:'Home Entertainment Package',href:'/home-entertainment-package'},
        {title:'Phones & Tablets',href:'/devices'}
      ]
    },
    {
      title:'Business',href:'/business/fixed',items:[
        {title:'Fixed Business Services',href:'/business/fixed',subItems:[
          {title:'Co-Location',href:'/business/fixed?service=co-location#catalog'},
          {title:'Data',href:'/business/fixed?service=data-connectivity#catalog'},
          {title:'Business Systems',href:'/business/fixed?service=business-systems#catalog'},
          {title:'Fixed Consumer Broadband Plans',href:'/business/fixed?service=fixed-broadband#catalog'},
          {title:'ISDN Lines',href:'/business/fixed?service=isdn-lines#catalog'},
          {title:'Radio FWM',href:'/business/fixed?service=radio-fwm#catalog'},
          {title:'SIP Trunk',href:'/business/fixed?service=sip-trunk#catalog'},
          {title:'Telikom VSAT – powered by Kacific',href:'/business/fixed?service=vsat-satellite#catalog'},
          {title:'Web & Hosting Services',href:'/business/fixed?service=web-hosting#catalog'},
          {title:'Fixed Voice Plans',href:'/business/fixed?service=fixed-voice#catalog'}
        ]},
        {title:'Mobile Business Services',href:'/business/mobile',subItems:[
          {title:'Why Telikom for your business?',href:'/business/mobile#why-telikom'},
          {title:'Closed User Group (CUG) / Prepaid User Group (PUG)',href:'/business/mobile?solution=cug-pug#mobile-solutions'},
          {title:'Roaming',href:'/business/mobile?solution=global-roaming#mobile-solutions'}
        ]}
      ]
    },
    {
      title:'News & Media',href:'/news',items:[
        {title:'All News',href:'/news?category=all'},
        {title:'Public Notices',href:'/news?category=notices'},
        {title:'Promotions & Offers',href:'/news?category=promotions'},
        {title:'Network Updates',href:'/news?category=network'},
        {title:'Press Releases',href:'/news?category=press'},
        {title:'Community & CSR',href:'/news?category=csr'},
        {title:'Media Kit & Assets',href:'/news?category=media-kit'}
      ]
    },
    {title:'About Us',href:'/about',items:[]},
    {title:'Store Locator',href:'/locations/retail',items:[]},
    {title:'Career',href:'/careers',items:[]}
  ];

  const FOOTER_COLUMNS=[
    {title:'Consumer',links:[
      {label:'Mobile Plans',href:'/personal/mobile'},
      {label:'Internet',href:'/personal/fixed/affordable-home-data'},
      {label:'Recharge',href:'/support'},
      {label:'Devices',href:'/devices'},
      {label:'Self Care',href:'/support'}
    ]},
    {title:'Business',links:[
      {label:'Solutions',href:'/business/fixed'},
      {label:'Enterprise',href:'/business/fixed'},
      {label:'Data Solutions',href:'/business/fixed?service=data-connectivity#catalog'},
      {label:'Business Support',href:'/contact'}
    ]},
    {title:'Support',links:[
      {label:'Help Centre',href:'/faqs'},
      {label:'FAQs',href:'/faqs'},
      {label:'Contact Us',href:'/contact'},
      {label:'Store Locator',href:'/locations/retail'}
    ]},
    {title:'About Us',links:[
      {label:'Our Story',href:'/about'},
      {label:'Careers',href:'/careers'},
      {label:'News',href:'/news'},
      {label:'Investors',href:'/about'}
    ]}
  ];

  const LEGAL_LINKS=[
    {label:'Privacy Policy',href:'/privacy'},
    {label:'Terms & Conditions',href:'/terms'},
    {label:'Sitemap',href:'/support'}
  ];

  const meta=(attrs)=>{
    const el=document.createElement('meta');
    Object.entries(attrs).forEach(([key,value])=>el.setAttribute(key,value));
    document.head.appendChild(el);
  };
  const link=(attrs)=>{
    const el=document.createElement('link');
    Object.entries(attrs).forEach(([key,value])=>el.setAttribute(key,value));
    document.head.appendChild(el);
  };

  const syncMetadata=()=>{
    document.title='Telikom PNG | Concise Home Page';
    document.head.querySelectorAll('meta:not([charset])').forEach((node)=>{
      if(node.getAttribute('name')!=='viewport')node.remove();
    });
    document.head.querySelectorAll('link[rel="canonical"],link[rel="alternate"],link[rel~="icon"],link[rel="apple-touch-icon"]').forEach(node=>node.remove());

    meta({name:'description',content:'Experience high-speed 4G LTE and reliable telecommunications services across Papua New Guinea.'});
    meta({name:'author',content:'Telikom Limited'});
    meta({name:'publisher',content:'Telikom Limited'});
    meta({name:'application-name',content:'Telikom Limited'});
    meta({name:'robots',content:'noindex, nofollow'});

    link({rel:'canonical',href:'https://www.telikom.com.pg/'});

    meta({property:'og:type',content:'website'});
    meta({property:'og:locale',content:'en_PG'});
    meta({property:'og:url',content:'https://www.telikom.com.pg'});
    meta({property:'og:site_name',content:'Telikom Limited'});
    meta({property:'og:title',content:'Telikom Limited | Mobile, Home & Business Internet Services'});
    meta({property:'og:description',content:'Telikom mobile data plans, home internet, business connectivity, devices, Self Care and support in Papua New Guinea.'});
    meta({property:'og:image',content:'https://www.telikom.com.pg/images/png/png_flag_people_celebration.png'});
    meta({property:'og:image:width',content:'1200'});
    meta({property:'og:image:height',content:'630'});
    meta({property:'og:image:alt',content:'Telikom Limited - Papua New Guinea'});

    meta({name:'twitter:card',content:'summary_large_image'});
    meta({name:'twitter:title',content:'Telikom Limited | Mobile, Home & Business Internet Services'});
    meta({name:'twitter:description',content:'Telikom mobile data plans, home internet, business connectivity, devices, Self Care and support in Papua New Guinea.'});
    meta({name:'twitter:image',content:'https://www.telikom.com.pg/images/png/png_flag_people_celebration.png'});

    link({rel:'icon',type:'image/svg+xml',href:'https://www.telikom.com.pg/telikom-logo.svg'});
    link({rel:'icon',type:'image/png',href:'https://www.telikom.com.pg/telikom-logo.png'});
    link({rel:'shortcut icon',href:'https://www.telikom.com.pg/telikom-logo.png'});
    link({rel:'apple-touch-icon',sizes:'180x180',type:'image/png',href:'https://www.telikom.com.pg/telikom-logo.png'});
  };

  const renderDesktopNavItem=(item)=>{
    const hasChildren=item.items&&item.items.length;
    return `<div class="shell-nav-item${hasChildren?' has-children':''}">
      <div class="shell-nav-main"><a class="shell-nav-link" href="${item.href}">${item.title}</a>${hasChildren?`<button class="shell-nav-toggle" type="button" data-shell-toggle aria-label="Open ${item.title} menu" aria-expanded="false">⌄</button>`:''}</div>
      ${hasChildren?`<div class="shell-nav-dropdown">${item.items.map((sub)=>{
        const hasSub=sub.subItems&&sub.subItems.length;
        return `<div class="shell-nav-subitem${hasSub?' has-children':''}">
          <div class="shell-nav-submain"><a href="${sub.href}">${sub.title}</a>${hasSub?`<button type="button" class="shell-nav-subtoggle" data-shell-subtoggle aria-label="Open ${sub.title} submenu" aria-expanded="false">›</button>`:''}</div>
          ${hasSub?`<div class="shell-nav-flyout">${sub.subItems.map(leaf=>`<a href="${leaf.href}">${leaf.title}</a>`).join('')}</div>`:''}
        </div>`;
      }).join('')}</div>`:''}
    </div>`;
  };

  const renderMobileNavItem=(item)=>{
    const hasChildren=item.items&&item.items.length;
    return `<div class="shell-mobile-item${hasChildren?' has-children':''}">
      <div class="shell-mobile-main"><a href="${item.href}">${item.title}</a>${hasChildren?`<button type="button" data-shell-mobile-toggle aria-label="Open ${item.title} menu" aria-expanded="false">⌄</button>`:''}</div>
      ${hasChildren?`<div class="shell-mobile-children">${item.items.map(sub=>{
        const hasSub=sub.subItems&&sub.subItems.length;
        return `<div class="shell-mobile-subitem${hasSub?' has-children':''}">
          <div class="shell-mobile-submain"><a href="${sub.href}">${sub.title}</a>${hasSub?`<button type="button" data-shell-mobile-subtoggle aria-label="Open ${sub.title} submenu" aria-expanded="false">⌄</button>`:''}</div>
          ${hasSub?`<div class="shell-mobile-leaves">${sub.subItems.map(leaf=>`<a href="${leaf.href}">${leaf.title}</a>`).join('')}</div>`:''}
        </div>`;
      }).join('')}</div>`:''}
    </div>`;
  };

  const syncHeader=()=>{
    const header=document.getElementById('header');
    if(!header)return;
    header.innerHTML=`<div class="header-in">
      <a class="brand" href="/" aria-label="Telikom PNG home"><img src="https://www.telikom.com.pg/assets/misc/TPNGLOGO.png" alt="Telikom, Connecting you Anywhere Anytime"></a>
      <nav class="shell-nav" aria-label="Primary navigation">${NAV_ITEMS.map(renderDesktopNavItem).join('')}</nav>
      <div class="utils shell-utils">
        <button class="icon-btn" id="searchOpen" type="button" aria-label="Search">⌕</button>
        <a class="selfcare shell-desktop-action" href="/support">Self Care</a>
        <a class="contact-btn shell-desktop-action" href="/contact">Contact Us</a>
        <button class="icon-btn menu-btn" id="shellMenuButton" type="button" aria-label="Open menu" aria-controls="shellMobilePanel" aria-expanded="false">☰</button>
      </div>
      <div class="shell-mobile-panel" id="shellMobilePanel" aria-hidden="true">
        <nav aria-label="Mobile navigation">${NAV_ITEMS.map(renderMobileNavItem).join('')}</nav>
        <div class="shell-mobile-actions"><a href="/support">Self Care</a><a href="/contact">Contact Us</a></div>
      </div>
    </div>`;

    const search=document.getElementById('searchOverlay');
    const openSearch=document.getElementById('searchOpen');
    if(search&&openSearch){
      openSearch.addEventListener('click',()=>{search.classList.add('open');search.setAttribute('aria-hidden','false')});
    }

    const closeAllDesktop=()=>{
      header.querySelectorAll('.shell-nav-item.is-open,.shell-nav-subitem.is-open').forEach(el=>el.classList.remove('is-open'));
      header.querySelectorAll('[data-shell-toggle],[data-shell-subtoggle]').forEach(btn=>btn.setAttribute('aria-expanded','false'));
    };
    header.querySelectorAll('[data-shell-toggle]').forEach(btn=>btn.addEventListener('click',(event)=>{
      event.stopPropagation();
      const item=btn.closest('.shell-nav-item');
      const next=!item.classList.contains('is-open');
      closeAllDesktop();
      item.classList.toggle('is-open',next);
      btn.setAttribute('aria-expanded',String(next));
    }));
    header.querySelectorAll('[data-shell-subtoggle]').forEach(btn=>btn.addEventListener('click',(event)=>{
      event.stopPropagation();
      const item=btn.closest('.shell-nav-subitem');
      const next=!item.classList.contains('is-open');
      item.parentElement.querySelectorAll('.shell-nav-subitem.is-open').forEach(el=>{if(el!==item)el.classList.remove('is-open')});
      item.classList.toggle('is-open',next);
      btn.setAttribute('aria-expanded',String(next));
    }));

    const mobilePanel=document.getElementById('shellMobilePanel');
    const menuButton=document.getElementById('shellMenuButton');
    const setMobileOpen=(open)=>{
      mobilePanel.classList.toggle('open',open);
      mobilePanel.setAttribute('aria-hidden',String(!open));
      menuButton.setAttribute('aria-expanded',String(open));
      menuButton.textContent=open?'×':'☰';
    };
    menuButton.addEventListener('click',(event)=>{event.stopPropagation();setMobileOpen(!mobilePanel.classList.contains('open'))});
    header.querySelectorAll('[data-shell-mobile-toggle]').forEach(btn=>btn.addEventListener('click',()=>{
      const item=btn.closest('.shell-mobile-item');
      const next=!item.classList.contains('is-open');
      item.classList.toggle('is-open',next);
      btn.setAttribute('aria-expanded',String(next));
    }));
    header.querySelectorAll('[data-shell-mobile-subtoggle]').forEach(btn=>btn.addEventListener('click',()=>{
      const item=btn.closest('.shell-mobile-subitem');
      const next=!item.classList.contains('is-open');
      item.classList.toggle('is-open',next);
      btn.setAttribute('aria-expanded',String(next));
    }));
    mobilePanel.querySelectorAll('a').forEach(anchor=>anchor.addEventListener('click',()=>setMobileOpen(false)));

    document.addEventListener('click',(event)=>{
      if(!header.contains(event.target)){closeAllDesktop();setMobileOpen(false)}
    });
    document.addEventListener('keydown',(event)=>{
      if(event.key==='Escape'){closeAllDesktop();setMobileOpen(false)}
    });
  };

  const syncFooter=()=>{
    const footer=document.querySelector('footer');
    if(!footer)return;
    footer.innerHTML=`<div class="shell"><div class="footer-top">
      <div class="footer-brand"><div class="footer-logo"><img src="https://www.telikom.com.pg/assets/misc/TPNGLOGO.png" alt="Telikom, Connecting you Anywhere Anytime"></div><p>Connecting you Anywhere Anytime</p><div class="footer-social" aria-label="Telikom social media">
        <a class="footer-social-icon" href="https://www.linkedin.com/company/telikompng" target="_blank" rel="noreferrer" aria-label="LinkedIn" title="LinkedIn"><span class="social-linkedin" aria-hidden="true">in</span></a>
        <a class="footer-social-icon" href="https://www.facebook.com/telikompng" target="_blank" rel="noreferrer" aria-label="Facebook" title="Facebook"><span class="social-facebook" aria-hidden="true">f</span></a>
        <a class="footer-social-icon" href="https://twitter.com/telikompng" target="_blank" rel="noreferrer" aria-label="X" title="X"><span aria-hidden="true">𝕏</span></a>
      </div></div>
      ${FOOTER_COLUMNS.map(column=>`<div class="footer-col"><b>${column.title}</b>${column.links.map(item=>`<a href="${item.href}">${item.label}</a>`).join('')}</div>`).join('')}
    </div><div class="footer-bottom"><div>© ${new Date().getFullYear()} Telikom Limited. All rights reserved.</div><div class="shell-legal-links">${LEGAL_LINKS.map(item=>`<a href="${item.href}">${item.label}</a>`).join('')}</div></div></div>`;
  };

  syncMetadata();
  syncHeader();
  syncFooter();
})();
