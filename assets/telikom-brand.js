(() => {
  const OFFICIAL_LOGO = 'https://www.telikom.com.pg/assets/misc/TPNGLOGO.png';

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

  function installLogo(container) {
    if (!container || container.dataset.officialLogoApplied === '1') return;
    container.dataset.officialLogoApplied = '1';

    const existingImg = container.querySelector('img');
    if (existingImg) {
      const previous = existingImg.getAttribute('src') || '';
      existingImg.classList.add('telikom-official-logo');
      existingImg.alt = 'Telikom — Connecting you Anywhere Anytime';
      existingImg.src = OFFICIAL_LOGO;
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
    img.onerror = () => {
      container.innerHTML = previousMarkup;
    };
    container.replaceChildren(img);
  }

  function apply() {
    const selectors = [
      'header .brand',
      'header .brandmark',
      'header .logo',
      '.topbar .brand',
      '.top .brand',
      '.site-header .brand',
      '.nav-shell .brand',
      '.masthead .brand'
    ];
    const target = selectors.map(s => document.querySelector(s)).find(Boolean);
    if (target) installLogo(target);

    document.querySelectorAll('footer .foot-brand img, footer .footer-brand img, footer .brand img').forEach(img => {
      img.classList.add('telikom-official-logo');
      img.alt = 'Telikom — Connecting you Anywhere Anytime';
      img.src = OFFICIAL_LOGO;
    });
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', apply, {once:true});
  else apply();
})();
