(() => {
  const OFFICIAL_LOGO = 'https://www.telikom.com.pg/assets/misc/TPNGLOGO.png';

  const PNG_IMAGES = {
    people: 'https://www.fao.org/images/faoraplibraries/default-album/farmers-and-agripreneurs-actively-participate-in-a-hands-on-training-session-provided-by-the-eu-streit-png-programme.jpg?sfvrsn=4cc42070_1',
    youth: 'https://www.pnglng.com/media/PNG-LNG-Media/Media%20Release%20Images/Flying-labs_PNG-LNG-Article.png?ext=.png',
    business: 'https://pngbusinessnews.b-cdn.net/uploads/article/image/3959/large_625349331_1329153339253229_7698291451399085164_n.jpg',
    remote: 'https://blog.apnic.net/wp-content/uploads/2016/04/Goroka-EHP.jpg',
    infrastructure: 'https://www.telikom.com.pg/assets/misc/pabx-connect.jpg',
    telikomBusiness: 'https://www.telikom.com.pg/assets/business/voice-and-data.jpg',
    device: 'https://www.telikom.com.pg/assets/products/RED-X_Quest_Plus.png'
  };

  const BAD_IMAGE = /(images\.unsplash\.com|source\.unsplash\.com|images\.pexels\.com|picsum\.photos|placehold(?:er)?|dummyimage|loremflickr)/i;
  const INTERNAL_COPY = /(prototype|placeholder|experimental\s+(?:homepage\s+)?concept|concept\s*\d+|replace\s+(?:this\s+)?with\s+approved|approved\s+(?:png\s+)?photography|illustrative\s+(?:only|geography|service|map|view|architecture)|not\s+(?:a\s+literal\s+)?(?:coverage|live|operational|network)\s*(?:map|data|view|status)?|demo\s+data|fake\s+live|unvalidated|for\s+stakeholder\s+presentation)/i;

  const style = document.createElement('style');
  style.textContent = `
    .telikom-official-logo {
      display:block !important;
      width:clamp(138px, 13vw, 188px) !important;
      max-width:188px !important;
      height:auto !important;
      max-height:60px !important;
      object-fit:contain !important;
      filter:none !important;
      mix-blend-mode:normal !important;
      opacity:1 !important;
      background:#fff;
      padding:3px 5px;
      border-radius:4px;
    }
    header .brand .brand-copy,
    header .brand .tagline,
    header .brand-copy,
    header .brandmark + .tagline { display:none !important; }
    @media (max-width:760px) {
      .telikom-official-logo { width:144px !important; max-height:52px !important; }
    }
  `;
  document.head.appendChild(style);

  function contextText(el) {
    const scope = el.closest('section, article, header, main, aside, div') || el;
    return `${el.className || ''} ${el.id || ''} ${scope.className || ''} ${scope.id || ''} ${scope.textContent || ''}`.toLowerCase().slice(0, 1800);
  }

  function imageFor(el) {
    const t = contextText(el);
    if (/(device|phone|tablet|product|handset|router)/.test(t)) return PNG_IMAGES.device;
    if (/(tower|network|infrastructure|technology|technical|exchange|facility|fibre|fiber)/.test(t)) return PNG_IMAGES.infrastructure;
    if (/(business|enterprise|office|organisation|organization|corporate)/.test(t)) return PNG_IMAGES.business;
    if (/(remote|rural|satellite|vsat|island|highland|coverage|geograph|terrain)/.test(t)) return PNG_IMAGES.remote;
    if (/(student|school|education|youth|learn)/.test(t)) return PNG_IMAGES.youth;
    if (/(home|family|people|community|customer|personal|mobile)/.test(t)) return PNG_IMAGES.people;
    return PNG_IMAGES.people;
  }

  function altFor(el) {
    const t = contextText(el);
    if (/(device|phone|tablet|product|handset|router)/.test(t)) return 'Telikom connected device';
    if (/(tower|network|infrastructure|technology|technical|exchange|facility)/.test(t)) return 'Telecommunications infrastructure';
    if (/(business|enterprise|office|organisation|organization|corporate)/.test(t)) return 'Papua New Guinean professionals';
    if (/(remote|rural|satellite|vsat|island|highland|coverage|geograph|terrain)/.test(t)) return 'Papua New Guinea landscape';
    if (/(student|school|education|youth|learn)/.test(t)) return 'Papua New Guinean students';
    return 'Papua New Guinean community';
  }

  function clientCopy(el) {
    const t = contextText(el);
    if (/(support|chat|assistant|help)/.test(t)) return 'Choose a service or support option to get started.';
    if (/(business|enterprise|office|organisation|organization|corporate)/.test(t)) return 'Business connectivity for organisations across Papua New Guinea.';
    if (/(remote|rural|satellite|vsat|island|highland|coverage|geograph|terrain)/.test(t)) return 'Connectivity for remote and regional Papua New Guinea.';
    if (/(tower|network|infrastructure|technology|technical|exchange|facility)/.test(t)) return 'Technology supporting Telikom services across Papua New Guinea.';
    if (/(student|school|education|youth|learn|people|community|family)/.test(t)) return 'Connecting people and communities across Papua New Guinea.';
    if (/(device|phone|tablet|product|handset|router)/.test(t)) return 'Devices and connected services from Telikom.';
    return 'Connecting Papua New Guinea.';
  }

  function installLogo(container) {
    if (!container || container.dataset.officialLogoApplied === '1') return;
    container.dataset.officialLogoApplied = '1';
    const existingImg = container.querySelector('img');
    if (existingImg) {
      const previous = existingImg.getAttribute('src') || '';
      existingImg.classList.add('telikom-official-logo');
      if (existingImg.alt !== 'Telikom — Connecting you Anywhere Anytime') existingImg.alt = 'Telikom — Connecting you Anywhere Anytime';
      if (existingImg.getAttribute('src') !== OFFICIAL_LOGO) existingImg.src = OFFICIAL_LOGO;
      existingImg.onerror = () => {
        if (previous && previous !== OFFICIAL_LOGO) {
          existingImg.onerror = null;
          existingImg.src = previous;
        }
      };
      return;
    }
    const previousMarkup = container.innerHTML;
    const img = document.createElement('img');
    img.className = 'telikom-official-logo';
    img.src = OFFICIAL_LOGO;
    img.alt = 'Telikom — Connecting you Anywhere Anytime';
    img.onerror = () => { container.innerHTML = previousMarkup; };
    container.replaceChildren(img);
  }

  function replaceImage(img) {
    if (img.classList.contains('telikom-official-logo')) return;
    const src = img.currentSrc || img.getAttribute('src') || '';
    const alt = img.getAttribute('alt') || '';
    if (!BAD_IMAGE.test(src) && !/(prototype|placeholder|replace with approved)/i.test(alt)) return;
    const replacement = imageFor(img);
    img.removeAttribute('srcset');
    img.removeAttribute('sizes');
    img.src = replacement;
    img.alt = altFor(img);
    img.loading = img.loading || 'lazy';
    img.decoding = 'async';
    img.onerror = () => {
      img.onerror = null;
      img.src = PNG_IMAGES.people;
    };
  }

  function replaceBackground(el) {
    let bg = '';
    try { bg = getComputedStyle(el).backgroundImage || ''; } catch (_) { return; }
    if (!BAD_IMAGE.test(bg)) return;
    const replacement = imageFor(el);
    const cleaned = bg.replace(/url\(["']?[^)"']*(?:unsplash|pexels|picsum|placehold|dummyimage|loremflickr)[^)"']*["']?\)/gi, `url("${replacement}")`);
    el.style.setProperty('background-image', BAD_IMAGE.test(cleaned) ? `url("${replacement}")` : cleaned, 'important');
  }

  function cleanText() {
    const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
    const nodes = [];
    while (walker.nextNode()) nodes.push(walker.currentNode);
    nodes.forEach(node => {
      const parent = node.parentElement;
      if (!parent || /^(SCRIPT|STYLE|NOSCRIPT|TEXTAREA|OPTION)$/.test(parent.tagName)) return;
      const raw = node.nodeValue || '';
      const text = raw.trim();
      if (!text || !INTERNAL_COPY.test(text)) return;
      node.nodeValue = raw.replace(text, clientCopy(parent));
    });
  }

  function normalizeFooterLogo(img) {
    if (!img.classList.contains('telikom-official-logo')) img.classList.add('telikom-official-logo');
    if (img.alt !== 'Telikom — Connecting you Anywhere Anytime') img.alt = 'Telikom — Connecting you Anywhere Anytime';
    if (img.getAttribute('src') !== OFFICIAL_LOGO) img.src = OFFICIAL_LOGO;
  }

  function apply() {
    const selectors = [
      'header .brand','header .brandmark','header .logo','.topbar .brand','.top .brand',
      '.site-header .brand','.nav-shell .brand','.masthead .brand'
    ];
    const target = selectors.map(s => document.querySelector(s)).find(Boolean);
    if (target) installLogo(target);

    document.querySelectorAll('footer .foot-brand img, footer .footer-brand img, footer .brand img').forEach(normalizeFooterLogo);
    document.querySelectorAll('img').forEach(replaceImage);
    document.querySelectorAll('body *').forEach(replaceBackground);
    cleanText();
  }

  let scheduled = false;
  function scheduleApply() {
    if (scheduled) return;
    scheduled = true;
    requestAnimationFrame(() => {
      scheduled = false;
      apply();
    });
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', apply, {once:true});
  else apply();
  setTimeout(apply, 180);

  const observer = new MutationObserver(records => {
    if (records.some(r => r.type === 'childList' || r.type === 'characterData' || (r.type === 'attributes' && /^(src|srcset|style|alt)$/.test(r.attributeName || '')))) scheduleApply();
  });
  if (document.documentElement) observer.observe(document.documentElement, {subtree:true,childList:true,characterData:true,attributes:true,attributeFilter:['src','srcset','style','alt']});
})();
