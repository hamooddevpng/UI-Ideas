(() => {
  const ready = () => {
    const title = document.title || '';
    const variant = title.includes('Consumer Services Hub') ? 'consumer' : title.includes('Connected Nation') ? 'nation' : title.includes('Balanced Corporate') ? 'corporate' : title.includes('National Connectivity') ? 'human' : 'executive';

    /* Load the chatbot directly from the homepage bootstrap so it does not depend on the later audience-map chain. */
    if (!document.querySelector('script[data-chatbot-vibes]')) {
      const chat = document.createElement('script');
      chat.src = 'assets/chatbot-vibes.js?v=20260903-1254';
      chat.dataset.chatbotVibes = '1';
      document.body.appendChild(chat);
    }

    const style = document.createElement('style');
    style.textContent = `
      .fresh-nav-hub{padding:62px 28px;background:#fff;border-top:1px solid #edf2f5;border-bottom:1px solid #e5edf3}
      .fresh-nav-inner{max-width:1280px;margin:auto}
      .fresh-nav-head{display:flex;justify-content:space-between;gap:24px;align-items:end;margin-bottom:24px}
      .fresh-nav-head small{display:block;font-size:11px!important;letter-spacing:.11em;text-transform:uppercase;color:#0875c9;font-weight:800;margin-bottom:7px}
      .fresh-nav-head h2{font:800 35px Manrope,Inter,sans-serif;letter-spacing:-1px;margin:0;color:#102b43}
      .fresh-nav-head p{max-width:720px;margin:8px 0 0;color:#667b8a;font-size:15px!important;line-height:1.6}
      .fresh-nav-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:13px}
      .fresh-nav-card{min-height:222px;padding:22px;border:1px solid #d7e3eb;border-radius:14px;background:linear-gradient(180deg,#fff,#f8fbfd);position:relative;overflow:hidden;text-decoration:none;color:#102b43;box-shadow:0 10px 26px rgba(8,44,68,.055);transition:.28s cubic-bezier(.22,.61,.36,1)}
      .fresh-nav-card:hover{transform:translateY(-4px);box-shadow:0 18px 38px rgba(8,44,68,.12);border-color:#a8d2eb}
      .fresh-nav-card:after{content:'→';position:absolute;right:18px;bottom:17px;color:#0875c9;font-weight:900;transition:transform .2s}.fresh-nav-card:hover:after{transform:translateX(4px)}
      .fresh-nav-icon{width:43px;height:43px;border-radius:11px;background:#e9f4fb;color:#0875c9;display:grid;place-items:center;font-weight:900;margin-bottom:25px}
      .fresh-nav-card h3{font:800 19px Manrope,Inter,sans-serif;margin:0 0 8px;letter-spacing:-.3px}.fresh-nav-card p{font-size:14px!important;line-height:1.55;color:#687c8b;margin:0 0 30px}
      .fresh-nav-card.featured{background:linear-gradient(145deg,#073552,#0a4d77);border-color:#0d5e8e;color:#fff}.fresh-nav-card.featured p{color:#c9dfed}.fresh-nav-card.featured .fresh-nav-icon{background:rgba(255,255,255,.1);color:#7fd2ff}.fresh-nav-card.featured:after{color:#fff}
      .fresh-nav-card.new-service{background:linear-gradient(145deg,#082e4a,#096b9d);color:#fff;border-color:#1683b8}.fresh-nav-card.new-service p{color:#d4ebf7}.fresh-nav-card.new-service .fresh-nav-icon{background:rgba(255,255,255,.12);color:#fff}.fresh-nav-card.new-service:after{color:#fff}
      .fresh-subnav{display:flex;gap:8px;flex-wrap:wrap;margin-top:18px}.fresh-subnav a{font-size:13px!important;text-decoration:none;color:#1d4d6d;background:#f1f7fb;border:1px solid #d8e7f0;padding:8px 11px;border-radius:999px;font-weight:700}
      .fresh-new-strip{margin-top:22px;border:1px solid #d9e6ee;border-radius:14px;overflow:hidden;display:grid;grid-template-columns:1.2fr repeat(3,1fr);background:#f8fbfd}.fresh-new-intro{padding:20px 22px;background:#072f4c;color:#fff}.fresh-new-intro small{font-size:11px!important;color:#8bd5ff!important;letter-spacing:.1em;font-weight:800}.fresh-new-intro h3{font:800 21px Manrope;margin:6px 0}.fresh-new-intro p{font-size:13px!important;color:#c7dce8;margin:0}.fresh-new-item{padding:19px 20px;border-left:1px solid #e2ebf0}.fresh-new-item b{display:block;font-size:14px!important;margin-bottom:5px}.fresh-new-item span{font-size:13px!important;color:#6b7e8d}.fresh-new-item a{display:block;margin-top:10px;color:#0875c9;font-size:13px!important;font-weight:800;text-decoration:none}
      .fresh-nav-hub.nation{background:#f3f7fa}.fresh-nav-hub.nation .fresh-nav-card{border-radius:6px;box-shadow:none}.fresh-nav-hub.nation .fresh-nav-grid{gap:8px}.fresh-nav-hub.nation .fresh-nav-card.featured,.fresh-nav-hub.nation .fresh-nav-card.new-service{background:#062f4d}
      .fresh-nav-hub.corporate .fresh-nav-card{border-radius:9px}.fresh-nav-hub.corporate .fresh-nav-card.featured{background:#fff;color:#102b43;border-top:4px solid #0875c9}.fresh-nav-hub.corporate .fresh-nav-card.featured p{color:#687c8b}.fresh-nav-hub.corporate .fresh-nav-card.featured:after{color:#0875c9}.fresh-nav-hub.corporate .fresh-nav-card.featured .fresh-nav-icon{background:#e9f4fb;color:#0875c9}
      .fresh-nav-hub.human{background:#f7f9fa}.fresh-nav-hub.human .fresh-nav-grid{grid-template-columns:1.2fr 1fr 1fr}.fresh-nav-hub.human .fresh-nav-card:first-child{grid-row:span 2;min-height:458px;background:linear-gradient(180deg,rgba(4,38,62,.18),rgba(4,38,62,.92)),url('https://blog.apnic.net/wp-content/uploads/2016/04/Goroka-EHP.jpg') center/cover;color:#fff;display:flex;flex-direction:column;justify-content:flex-end}.fresh-nav-hub.human .fresh-nav-card:first-child p{color:#dbe9f1}.fresh-nav-hub.human .fresh-nav-card:first-child:after{color:#fff}
      .fresh-nav-hub.executive{padding:24px 0;background:transparent;border:0}.fresh-nav-hub.executive .fresh-nav-inner{max-width:none}.fresh-nav-hub.executive .fresh-nav-head{margin-bottom:14px}.fresh-nav-hub.executive .fresh-nav-head h2{font-size:24px}.fresh-nav-hub.executive .fresh-nav-grid{grid-template-columns:repeat(4,1fr);gap:8px}.fresh-nav-hub.executive .fresh-nav-card{min-height:150px;border-radius:8px;padding:16px}.fresh-nav-hub.executive .fresh-nav-icon{margin-bottom:13px}.fresh-nav-hub.executive .fresh-new-strip{display:none}
      @media(max-width:980px){.fresh-nav-grid,.fresh-nav-hub.human .fresh-nav-grid{grid-template-columns:1fr 1fr}.fresh-nav-hub.human .fresh-nav-card:first-child{grid-row:auto;min-height:230px}.fresh-new-strip{grid-template-columns:1fr 1fr}}
      @media(max-width:620px){.fresh-nav-hub{padding:48px 18px}.fresh-nav-grid,.fresh-nav-hub.human .fresh-nav-grid,.fresh-nav-hub.executive .fresh-nav-grid{grid-template-columns:1fr}.fresh-nav-head{display:block}.fresh-new-strip{grid-template-columns:1fr}.fresh-new-item{border-left:0;border-top:1px solid #e2ebf0}}
    `;
    document.head.appendChild(style);

    const hub = `
      <section class="fresh-nav-hub ${variant}">
        <div class="fresh-nav-inner">
          <div class="fresh-nav-head"><div><small>Start here</small><h2>Explore Telikom services</h2><p>Built from the current Telikom frontend structure so customers can immediately find personal, business, device, satellite, support and company pages.</p></div></div>
          <div class="fresh-nav-grid">
            <a class="fresh-nav-card" href="#"><span class="fresh-nav-icon">◉</span><h3>Personal Services</h3><p>Gutpela Mobile Data, MOA Plus Packs, International Call Plans, roaming bundles and special mobile passes.</p></a>
            <a class="fresh-nav-card featured" href="#business"><span class="fresh-nav-icon">▦</span><h3>Business Services</h3><p>Fixed business connectivity, Data, Co-Location, Business Systems, SIP Trunk, Web & Hosting, voice and mobile business solutions.</p></a>
            <a class="fresh-nav-card" href="#"><span class="fresh-nav-icon">⌂</span><h3>Home & Fixed Services</h3><p>Affordable Home Data, U-TOKMoa plans, Special Home Passes and the Home Entertainment Package.</p></a>
            <a class="fresh-nav-card new-service" href="#"><span class="fresh-nav-icon">✦</span><h3>Starlink & VSAT</h3><p>Current enterprise remote-connectivity direction: Starlink Enterprise integration alongside Telikom VSAT powered by Kacific.</p></a>
            <a class="fresh-nav-card" href="#"><span class="fresh-nav-icon">▤</span><h3>Phones & Devices</h3><p>Phones, tablets, MiFi, routers and other Telikom hardware, with store-location support.</p></a>
            <a class="fresh-nav-card" href="#plans"><span class="fresh-nav-icon">⌁</span><h3>Mobile Plans & Offers</h3><p>Daily, weekly and monthly mobile options plus special, international and roaming categories.</p></a>
            <a class="fresh-nav-card" href="#"><span class="fresh-nav-icon">◎</span><h3>News & Network Updates</h3><p>Public Notices, Promotions & Offers, Network Updates, Press Releases, Community & CSR and Media Kit.</p></a>
            <a class="fresh-nav-card" href="#"><span class="fresh-nav-icon">?</span><h3>Support, Stores & Self Care</h3><p>FAQs, retail locations, customer support, account management, billing and service assistance.</p></a>
          </div>
          <div class="fresh-new-strip"><div class="fresh-new-intro"><small>CURRENT SITE HIGHLIGHTS</small><h3>More of Telikom, visible from home.</h3><p>Important destinations from the new frontend should not be buried several clicks deep.</p></div><div class="fresh-new-item"><b>U-TOKMoa</b><span>Fixed voice & data combo plans.</span><a href="#">Explore U-TOKMoa →</a></div><div class="fresh-new-item"><b>Home Entertainment</b><span>Broadband, Telikom TV and fixed voice package.</span><a href="#">View packages →</a></div><div class="fresh-new-item"><b>Careers & Company</b><span>Jobs, About Us and current Telikom updates.</span><a href="#">Explore Telikom →</a></div></div>
          <div class="fresh-subnav"><a href="#">Store Locator</a><a href="#">Career</a><a href="#">About Us</a><a href="#">Public Notices</a><a href="#">Promotions</a><a href="#">Network Updates</a><a href="#">Contact Us</a></div>
        </div>
      </section>`;

    const anchor = document.querySelector('.national-proof-strip, .dock, .quick, .actions');
    if (anchor && !document.querySelector('.fresh-nav-hub')) anchor.insertAdjacentHTML('afterend', hub);
    else if (!document.querySelector('.fresh-nav-hub')) { const hero = document.querySelector('.institutional-hero, .hero, header'); if (hero) hero.insertAdjacentHTML('afterend', hub); }

    const links = document.querySelector('.nav .links, nav .links');
    if (links) { const existing = [...links.querySelectorAll('a')]; const utility = existing.filter(a => /self care|top up|contact|login/i.test(a.textContent)); links.innerHTML = ''; ['Personal','Business','Home & Fixed','Devices','News & Media','Stores'].forEach(label => { const a = document.createElement('a'); a.href='#'; a.textContent=label; links.appendChild(a); }); utility.forEach(a => links.appendChild(a)); }

    if (!document.querySelector('script[data-glance-variants]')) { const glance = document.createElement('script'); glance.src = 'assets/glance-variants.js'; glance.defer = true; glance.dataset.glanceVariants = '1'; document.body.appendChild(glance); }
    if (!document.querySelector('script[data-audience-map]')) { const audience = document.createElement('script'); audience.src = 'assets/audience-map.js?v=20260903-1254'; audience.defer = true; audience.dataset.audienceMap = '1'; document.body.appendChild(audience); }
  };
  if(document.readyState==='loading') document.addEventListener('DOMContentLoaded',ready,{once:true}); else ready();
})();
