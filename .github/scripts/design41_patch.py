from pathlib import Path

p = Path('41.html')
s = p.read_text()

s = s.replace('<title>Telikom PNG — Homepage Design 10</title>', '<title>Telikom PNG — Design 41 / Telikom Alive</title>')
s = s.replace('https://www.telikom.com.pg/assets/misc/TPNGLOGO.png', 'https://raw.githubusercontent.com/hamooddevpng/UI-Ideas/main/assets/brand/telikom-logo.png')

extra_css = r'''
/* DESIGN 41 CONTENT LAYER. Motion remains Design 10's original engine. */
.stage-photo{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:.14;filter:saturate(.9) contrast(.95);mix-blend-mode:multiply;z-index:0;transition:opacity .6s var(--ease),scale 2.8s var(--ease);scale:1.03}.stage-shell:hover .stage-photo{opacity:.22;scale:1.08}.stage-shell .fallback-object{z-index:1}.stage-shell canvas{z-index:2}
.quick-band{position:relative;z-index:12;margin:-30px 5vw 92px;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));border:1px solid rgba(8,45,70,.14);border-radius:22px;background:rgba(255,255,255,.86);backdrop-filter:blur(18px);box-shadow:0 22px 52px rgba(32,81,111,.09);overflow:hidden}.quick-action{min-height:106px;padding:19px 22px;display:flex;align-items:center;justify-content:space-between;gap:18px;border-right:1px solid var(--line);transition:background .35s var(--ease),color .35s var(--ease);will-change:translate}.quick-action:last-child{border-right:0}.quick-action small{font:500 8px DM Mono,monospace;letter-spacing:.14em;color:#7692a5;display:block;margin-bottom:8px}.quick-action b{font-size:17px;letter-spacing:-.02em}.quick-action i{font-style:normal;width:38px;height:38px;border:1px solid var(--line);border-radius:50%;display:grid;place-items:center;transition:.35s var(--ease)}.quick-action:hover{background:var(--ink);color:#fff}.quick-action:hover small{color:#9fc4d8}.quick-action:hover i{border-color:rgba(255,255,255,.3);translate:3px -3px}
.campaign-deck{display:grid;grid-template-columns:1.35fr .65fr;gap:14px;margin:46px 0 50px}.campaign-card{position:relative;min-height:470px;border-radius:30px;overflow:hidden;border:1px solid rgba(8,45,70,.13);background:var(--ink);box-shadow:0 28px 60px rgba(30,88,123,.1);isolation:isolate;will-change:translate}.campaign-card img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;z-index:-2;transition:scale 2.4s var(--ease),filter .8s var(--ease);scale:1.01}.campaign-card:after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(3,31,48,.02),rgba(3,31,48,.15) 44%,rgba(3,31,48,.86));z-index:-1}.campaign-card:hover img{scale:1.06}.campaign-card .campaign-copy{position:absolute;left:28px;right:28px;bottom:28px;color:#fff}.campaign-card .campaign-copy small{font:500 9px DM Mono,monospace;letter-spacing:.14em;color:#b9e2f6}.campaign-card h3{font-size:clamp(38px,4vw,72px);line-height:.9;letter-spacing:-.055em;margin:10px 0 12px;max-width:680px}.campaign-card p{font-size:13px;line-height:1.55;max-width:470px;color:#d7e8f1;margin:0}.campaign-card.alt h3{font-size:clamp(32px,3vw,54px)}
.png-story{padding:120px 5vw 160px;position:relative;overflow:hidden}.png-story-grid{display:grid;grid-template-columns:.78fr 1.22fr;gap:22px;align-items:stretch}.png-story-copy{padding:34px 2vw 34px 0;display:flex;flex-direction:column;justify-content:center;will-change:translate}.png-story-copy h2{font-size:clamp(64px,8.4vw,126px);line-height:.82;letter-spacing:-.075em;margin:18px 0 26px}.png-story-copy h2 span{color:var(--blue)}.png-story-copy p{max-width:540px;font-size:16px;line-height:1.75;color:#58768a}.png-story-image{position:relative;min-height:650px;border-radius:34px;overflow:hidden;border:1px solid rgba(8,45,70,.13);will-change:translate}.png-story-image img{width:100%;height:100%;object-fit:cover;position:absolute;inset:0;scale:1.02;transition:scale 3s var(--ease)}.png-story-image:hover img{scale:1.08}.png-story-image:after{content:"PNG / ANYWHERE / ANYTIME";position:absolute;left:22px;bottom:20px;padding:9px 12px;border-radius:999px;background:rgba(255,255,255,.78);backdrop-filter:blur(12px);font:500 8px DM Mono,monospace;letter-spacing:.12em;color:var(--ink)}
.notice-strip{margin:0 0 46px;border:1px solid rgba(124,207,238,.25);border-radius:18px;display:grid;grid-template-columns:auto 1fr auto;gap:18px;align-items:center;padding:16px 18px;background:rgba(255,255,255,.05);will-change:translate}.notice-strip .live{font:500 8px DM Mono,monospace;letter-spacing:.12em;color:#7ccfee}.notice-strip b{font-size:13px}.notice-strip a{font:500 9px DM Mono,monospace;color:#7ccfee}
.support-hub{padding:120px 5vw 150px;display:grid;grid-template-columns:.72fr 1.28fr;gap:50px;align-items:center;position:relative}.support-copy h2{font-size:clamp(62px,8vw,118px);line-height:.84;letter-spacing:-.07em;margin:16px 0 24px}.support-copy p{font-size:15px;line-height:1.7;color:#5c788b;max-width:460px}.support-actions{display:grid;grid-template-columns:1fr 1fr;gap:9px;margin-top:28px}.support-link{border:1px solid var(--line);border-radius:16px;padding:17px 18px;display:flex;justify-content:space-between;align-items:center;font-size:12px;font-weight:800;background:#fff;transition:.35s var(--ease);will-change:translate}.support-link:hover{background:var(--ink);color:#fff;border-color:var(--ink)}
@media(max-width:900px){.quick-band{grid-template-columns:1fr 1fr}.quick-action:nth-child(2){border-right:0}.quick-action:nth-child(-n+2){border-bottom:1px solid var(--line)}.campaign-deck,.png-story-grid,.support-hub{grid-template-columns:1fr}.campaign-card{min-height:420px}.png-story-image{min-height:520px}.support-hub{gap:18px}}
@media(max-width:560px){.quick-band{margin:-12px 18px 68px}.quick-action{min-height:88px;padding:14px}.quick-action b{font-size:14px}.campaign-deck{grid-template-columns:1fr}.campaign-card{min-height:360px}.support-actions{grid-template-columns:1fr}.png-story{padding-left:18px;padding-right:18px}.plans,.worlds,.business,.news{padding-left:18px;padding-right:18px}}
'''
s = s.replace('</style>', extra_css + '\n</style>', 1)

header = r'''<header class="topbar" data-depth="3">
  <a href="#top" class="brand"><img src="https://raw.githubusercontent.com/hamooddevpng/UI-Ideas/main/assets/brand/telikom-logo.png" alt="Telikom PNG"><small>Connecting you<br>anywhere anytime</small></a>
  <nav class="nav" aria-label="Primary navigation"><a href="#plans">Offers</a><a href="#worlds">Services</a><a href="#business">Business + Government</a><a href="#news">Updates</a><a href="#support">Support</a></nav>
  <div class="utility"><a href="#support">Top up</a><a href="#support">Pay bill</a><a href="#worlds" class="primary">Explore Telikom ↗</a><button class="menu" aria-label="Menu">☰</button></div>
</header>'''
a = s.index('<header class="topbar"')
b = s.index('</header>', a) + len('</header>')
s = s[:a] + header + s[b:]

main = r'''<main id="top">
<section class="hero">
  <div class="hero-copy" data-depth="-10">
    <div class="hero-index" data-depth="-5">TELIKOM / PAPUA NEW GUINEA / 41</div>
    <h1><span data-depth="-6">Make</span><span class="outline" data-depth="-12">distance</span><span class="blue" data-depth="9">disappear.</span></h1>
    <div class="hero-sub" data-depth="-5"><div class="hero-number">00</div><div><p>Mobile, home, business and government connectivity designed around how Papua New Guinea actually moves, works and stays in touch.</p><div class="hero-actions"><a class="btn fill" href="#plans">See current offers <i>↗</i></a><a class="btn" href="#worlds">Explore services</a></div></div></div>
  </div>
  <div class="hero-stage" id="heroStage" data-depth="12">
    <div class="hero-orbit o1" data-depth="20"></div><div class="hero-orbit o2" data-depth="-16"></div>
    <div class="stage-shell" id="stageShell" data-depth="8"><img class="stage-photo" src="https://raw.githubusercontent.com/hamooddevpng/UI-Ideas/main/assets/banners/research/stay-connected-from-png-to-the-world.webp" alt="Stay connected from PNG to the world"><div class="fallback-object"></div><canvas id="sculpture" aria-hidden="true"></canvas></div>
    <div class="float-tag tag-a" data-depth="-24"><small>PERSONAL / 01</small><b>Mobile + data</b></div>
    <div class="float-tag tag-b" data-depth="21"><small>ENTERPRISE / 03</small><b>Built to scale</b></div>
    <div class="float-tag tag-c" data-depth="-15"><small>PNG / 04</small><b>Reach further</b></div>
  </div>
  <div class="scroll-signal" data-depth="-7">MOVE / SCROLL / EXPLORE <span></span></div>
</section>
<section class="quick-band" aria-label="Quick actions">
  <a class="quick-action" href="#support" data-depth="-8"><div><small>QUICK / 01</small><b>Recharge</b></div><i>↗</i></a>
  <a class="quick-action" href="#plans" data-depth="10"><div><small>QUICK / 02</small><b>Buy data</b></div><i>↗</i></a>
  <a class="quick-action" href="#support" data-depth="-12"><div><small>QUICK / 03</small><b>Self Care</b></div><i>↗</i></a>
  <a class="quick-action" href="#support" data-depth="9"><div><small>QUICK / 04</small><b>Find a store</b></div><i>↗</i></a>
</section>
<div class="ticker" aria-hidden="true"><div class="ticker-track"><span>MOBILE</span><b>✦</b><span>HOME INTERNET</span><b>✦</b><span>BUSINESS</span><b>✦</b><span>GOVERNMENT</span><b>✦</b><span>REMOTE CONNECTIVITY</span><b>✦</b><span>MOBILE</span><b>✦</b><span>HOME INTERNET</span><b>✦</b><span>BUSINESS</span><b>✦</b><span>GOVERNMENT</span><b>✦</b><span>REMOTE CONNECTIVITY</span><b>✦</b></div></div>
<section class="plans" id="plans">
  <div class="plans-intro reveal" data-depth="-9"><div><div class="micro">01 / OFFERS + PLANS</div><h2>Something<br>worth opening.</h2></div><p>Campaigns first, details second. Large visual offers give customers a reason to stop, then the plan choices stay simple underneath.</p></div>
  <div class="campaign-deck">
    <a href="#" class="campaign-card reveal" data-depth="-13"><img src="https://raw.githubusercontent.com/hamooddevpng/UI-Ideas/main/assets/banners/research/stay-connected-from-png-to-the-world.webp" alt="Stay connected from PNG to the world"><div class="campaign-copy" data-depth="10"><small>TELIKOM / FEATURED CAMPAIGN</small><h3>From PNG to the world.</h3><p>Connection that keeps people, families and work moving beyond distance.</p></div></a>
    <a href="#" class="campaign-card alt reveal" data-depth="14"><img src="https://raw.githubusercontent.com/hamooddevpng/UI-Ideas/main/assets/banners/research/festive-png-telecom-deals.webp" alt="Telikom festive PNG telecom deals"><div class="campaign-copy" data-depth="-11"><small>LIMITED / OFFER</small><h3>More data.<br>More PNG.</h3><p>Simple promotional value presented as a real campaign, not another tiny card.</p></div></a>
  </div>
  <div class="ticket-stage">
    <article class="ticket one" data-depth="-14"><div><div class="eyebrow">GUTPELA / DAILY</div><h3>Today.</h3><p>Quick data for the moments that matter now.</p></div><div class="stamp" data-depth="10">FLEXIBLE<br>DATA</div></article>
    <article class="ticket two" data-depth="11"><div><div class="eyebrow">GUTPELA / WEEKLY</div><h3>This week.</h3><p>More room for work, chat and everything in between.</p></div><div class="stamp" data-depth="-8">WEEKLY<br>VALUE</div></article>
    <article class="ticket three" data-depth="-7"><div><div class="eyebrow">GUTPELA / MONTHLY</div><h3>Keep going.</h3><p>A longer-running option for consistent connectivity.</p></div><div class="stamp" data-depth="12">MONTHLY<br>READY</div></article>
  </div>
</section>
<section class="worlds" id="worlds">
  <div class="worlds-head reveal" data-depth="-8"><div><div class="micro">02 / SERVICE CATEGORIES</div><h2>Different needs.<br>One Telikom.</h2></div><p>Get to the right service by what you are trying to do, not by how the network is built.</p></div>
  <div class="world-grid">
    <article class="world-card w1 reveal" data-depth="-9"><div class="num">01 / MOBILE</div><div data-depth="-5"><h3>Everyday connection.</h3><p>Prepaid, mobile data and straightforward ways to stay connected wherever the day takes you.</p><a class="btn" href="#plans">Mobile services ↗</a></div><div class="shape" data-depth="20"></div></article>
    <article class="world-card w2 reveal" data-depth="10"><div class="num">02 / HOME + DEVICES</div><div data-depth="5"><h3>Home,<br>always on.</h3><p>Home internet, routers and devices gathered into one clear destination.</p><a class="btn" href="#plans" style="border-color:rgba(255,255,255,.45);color:#fff">Home services ↗</a></div><div class="shape" data-depth="-18"></div></article>
    <article class="world-card w3 reveal" data-depth="-6"><div data-depth="-7"><div class="num">03 / ENTERPRISE + SUPPORT</div><h3>Infrastructure for ambition.</h3></div><div data-depth="8"><p>Data, voice, broadband, hosting, remote connectivity and support for organisations operating across PNG.</p><a class="btn fill" href="#business">Business solutions ↗</a></div><div class="signal-river" data-depth="14"><svg viewBox="0 0 1000 120" preserveAspectRatio="none"><path d="M0 70 C170 8 260 112 420 45 S710 115 1000 30"/><path d="M0 42 C220 110 340 2 530 78 S790 10 1000 88"/></svg></div></article>
  </div>
</section>
<section class="business" id="business">
  <div class="business-head reveal" data-depth="-8"><div><div class="micro">03 / BUSINESS + GOVERNMENT</div><h2>Built around your operation.</h2></div><p>One visual system for enterprise, government and institutions that need dependable communication, hosting and reach across locations.</p></div>
  <div class="network-diagram reveal" id="networkDiagram" data-depth="4">
    <svg class="wire" viewBox="0 0 1000 610" preserveAspectRatio="none" aria-hidden="true"><line x1="500" y1="305" x2="160" y2="125"/><line x1="500" y1="305" x2="840" y2="125"/><line x1="500" y1="305" x2="150" y2="500"/><line x1="500" y1="305" x2="850" y2="490"/><line x1="500" y1="305" x2="500" y2="105"/><circle cx="500" cy="305" r="5"/></svg>
    <div class="core" data-depth="10"><div><b>TELIKOM</b><small>PNG CONNECTIVITY CORE</small></div></div>
    <div class="node n1" data-depth="-17"><b>Enterprise Data</b><span>Reliable connectivity between teams and locations.</span></div>
    <div class="node n2" data-depth="18"><b>Government</b><span>Connectivity pathways for public-sector operations.</span></div>
    <div class="node n3" data-depth="-13"><b>Voice & SIP</b><span>Clear communication across your organisation.</span></div>
    <div class="node n4" data-depth="14"><b>Remote / VSAT</b><span>Extend connectivity beyond conventional reach.</span></div>
    <div class="node n5" data-depth="-10"><b>Hosting</b><span>Digital infrastructure closer to home.</span></div>
  </div>
</section>
<section class="png-story" id="png-story">
  <div class="png-story-grid">
    <div class="png-story-copy reveal" data-depth="-10"><div class="micro">04 / PNG + NATIONAL STORY</div><h2>One network.<br><span>Many lives.</span></h2><p>Connection is a call home, a classroom online, a business transaction, a health service reaching further and a community becoming easier to reach. Telikom belongs inside that national story.</p><div class="mini-rule"></div><div class="micro">CONNECTING YOU ANYWHERE ANYTIME</div></div>
    <div class="png-story-image reveal" data-depth="13"><img src="https://raw.githubusercontent.com/hamooddevpng/UI-Ideas/main/assets/banners/research/stay-connected-from-png-to-the-world.webp" alt="Telikom connecting Papua New Guinea to the world"></div>
  </div>
</section>
<section class="news" id="news">
  <div class="news-head reveal" data-depth="-9"><div><div class="micro" style="color:#7ccfee">05 / NOTICES + NEWS</div><h2>Know what<br>is moving.</h2></div><a href="#">VIEW ALL UPDATES ↗</a></div>
  <div class="notice-strip reveal" data-depth="10"><span class="live">SERVICE NOTICE / LIVE</span><b>Check current service information before you travel or troubleshoot.</b><a href="#">VIEW STATUS ↗</a></div>
  <div class="news-list">
    <a href="#" class="story reveal" data-depth="-7"><div class="id">N/01</div><div><h3>Network updates and public advisories</h3><p>Important information for customers and communities.</p></div><div class="arrow" data-depth="12">↗</div></a>
    <a href="#" class="story reveal" data-depth="8"><div class="id">N/02</div><div><h3>Telikom in communities across PNG</h3><p>Stories about connection, service and national reach.</p></div><div class="arrow" data-depth="-10">↗</div></a>
    <a href="#" class="story reveal" data-depth="-6"><div class="id">N/03</div><div><h3>Business, government and service announcements</h3><p>New capabilities, offers and developments from Telikom.</p></div><div class="arrow" data-depth="9">↗</div></a>
  </div>
</section>
<section class="support-hub" id="support">
  <div class="support-copy reveal" data-depth="-10"><div class="micro">06 / HELP + SUPPORT + STORES</div><h2>Your next<br>move.</h2><p>Recharge, manage an account, check coverage, find a store or reach Telikom support without hunting through the site.</p><div class="support-actions"><a class="support-link" href="#" data-depth="7">Recharge <span>↗</span></a><a class="support-link" href="#" data-depth="-8">Self Care <span>↗</span></a><a class="support-link" href="#" data-depth="10">Coverage <span>↗</span></a><a class="support-link" href="#" data-depth="-6">Get support <span>↗</span></a></div></div>
  <div class="coordinate-field" id="coordinateField" data-depth="12"><span class="axis y">PNG / SERVICE COORDINATES</span><span class="axis x">TELIKOM / RETAIL NETWORK</span><i class="locator l1" data-label="PORT MORESBY" data-depth="-16"></i><i class="locator l2" data-label="LAE" data-depth="18"></i><i class="locator l3" data-label="MADANG" data-depth="-11"></i><i class="locator l4" data-label="MT HAGEN" data-depth="15"></i></div>
</section>
</main>'''
a = s.index('<main id="top">')
b = s.index('</main>', a) + len('</main>')
s = s[:a] + main + s[b:]

s = s.replace('<div class="foot-col" data-depth="5"><b>Company</b><a href="#">News</a><a href="#">Careers</a><a href="#">Contact</a></div>', '<div class="foot-col" data-depth="5"><b>Help</b><a href="#support">Support</a><a href="#support">Stores</a><a href="#news">Notices</a></div>')
s = s.replace("document.querySelectorAll('a,button,.world-card,.ticket,.node,.story,.coordinate-field')", "document.querySelectorAll('a,button,.world-card,.ticket,.node,.story,.coordinate-field,.campaign-card,.quick-action,.support-link')")

p.write_text(s)
