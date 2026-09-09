from pathlib import Path
import re

p = Path('41.html')
s = p.read_text(encoding='utf-8')

RAW = 'https://raw.githubusercontent.com/hamooddevpng/UI-Ideas/main/'

def replace_between(text, start, end, replacement):
    a = text.find(start)
    if a < 0:
        raise SystemExit(f'missing start marker: {start[:80]}')
    b = text.find(end, a)
    if b < 0:
        raise SystemExit(f'missing end marker: {end[:80]}')
    return text[:a] + replacement + text[b:]

# Header: exact Design 41 information model, compact-on-scroll, real mobile/search controls.
header = r'''<header class="topbar" id="siteHeader" data-depth="3">
  <a href="#top" class="brand"><img src="https://raw.githubusercontent.com/hamooddevpng/UI-Ideas/main/assets/brand/telikom-logo.png" alt="Telikom PNG"><small>Connecting you<br>anywhere anytime</small></a>
  <nav class="nav" id="primaryNav" aria-label="Primary navigation">
    <span class="nav-glider" id="navGlider" aria-hidden="true"></span>
    <a href="#services">Mobile</a><a href="#services">Internet</a><a href="#business">Business</a><a href="#plans">Offers</a><a href="#png-story">About</a>
  </nav>
  <div class="utility"><button class="search-trigger" id="searchTrigger" type="button" aria-haspopup="dialog">Search</button><a href="#support">Support</a><button class="primary self-care-trigger" type="button" data-action="selfcare">Self Care ↗</button><button class="menu" id="menuButton" type="button" aria-label="Open menu" aria-expanded="false">☰</button></div>
</header>
<nav class="mobile-panel" id="mobilePanel" aria-label="Mobile navigation" aria-hidden="true"><a href="#services">Mobile</a><a href="#services">Internet</a><a href="#business">Business</a><a href="#plans">Offers</a><a href="#png-story">About</a><a href="#support">Support</a><button type="button" data-action="selfcare">Self Care ↗</button></nav>
'''
s = replace_between(s, '<header class="topbar" data-depth="3">', '<main id="top">', header + '<main id="top">')

# Hero keeps one primary campaign and Design 10 sculpture, while making the PNG visual clearer.
s = s.replace(
    '<div class="stage-shell" id="stageShell" data-depth="8"><img class="stage-photo" src="https://raw.githubusercontent.com/hamooddevpng/UI-Ideas/main/assets/banners/research/stay-connected-from-png-to-the-world.webp" alt="Stay connected from PNG to the world"><div class="fallback-object"></div><canvas id="sculpture" aria-hidden="true"></canvas></div>',
    '<div class="stage-shell" id="stageShell" data-depth="8"><img class="stage-photo" src="https://raw.githubusercontent.com/hamooddevpng/UI-Ideas/main/assets/banners/research/stay-connected-from-png-to-the-world.webp" alt="Stay connected from PNG to the world" fetchpriority="high"><div class="campaign-label">PRIMARY / PNG CONNECTION</div><div class="fallback-object"></div><canvas id="sculpture" aria-hidden="true"></canvas></div>'
)

# Quick actions: locked primary hierarchy, plus secondary pathways.
quick = r'''<section class="quick-zone" id="quick" aria-label="Quick actions">
  <div class="quick-band">
    <button class="quick-action" type="button" data-action="recharge" data-depth="-7"><span class="quick-icon">↻</span><span><small>QUICK / 01</small><b>Recharge</b><em>Top up mobile credit</em></span><i>↗</i></button>
    <button class="quick-action" type="button" data-action="selfcare" data-depth="8"><span class="quick-icon">◎</span><span><small>QUICK / 02</small><b>Self Care</b><em>Manage your services</em></span><i>↗</i></button>
    <button class="quick-action" type="button" data-action="coverage" data-depth="-9"><span class="quick-icon">⌖</span><span><small>QUICK / 03</small><b>Coverage</b><em>Check availability</em></span><i>↗</i></button>
    <button class="quick-action" type="button" data-action="support" data-depth="7"><span class="quick-icon">?</span><span><small>QUICK / 04</small><b>Support</b><em>Find help quickly</em></span><i>↗</i></button>
  </div>
  <nav class="quick-secondary" aria-label="More quick actions"><button type="button" data-action="store">Find a Store</button><button type="button" data-action="sim">Buy SIM</button><button type="button" data-action="bill">Pay Bill</button><a href="#plans">Internet Plans</a><a href="#news">Service Updates</a><button type="button" data-action="business">Business Enquiries</button></nav>
</section>
'''
s = replace_between(s, '<section class="quick-band" aria-label="Quick actions">', '<div class="ticker"', quick + '<div class="ticker"')

# Offers: one clear feature campaign, one supporting campaign, then generic plan rhythms.
plans = r'''<section class="plans" id="plans">
  <div class="plans-intro reveal" data-depth="-7"><div><div class="micro">01 / OFFERS + PLANS</div><h2>Offers with<br>something to say.</h2></div><p>One clear feature campaign first, supporting commercial pathways second, then simple plan choices without invented pricing.</p></div>
  <div class="campaign-deck">
    <article class="campaign-card feature reveal" data-depth="-8" data-tilt><img src="https://raw.githubusercontent.com/hamooddevpng/UI-Ideas/main/assets/design40/hero/telikom-double-data.jpg" alt="Telikom campaign creative" loading="lazy" decoding="async"><div class="campaign-copy" data-depth="6"><small>FEATURE / MOBILE DATA</small><h3>More room to stay connected.</h3><p>A strong Telikom campaign visual leads the section, while the interaction stays calm and readable.</p><button class="campaign-cta" type="button" data-action="mobile-data">Explore mobile data ↗</button></div></article>
    <article class="campaign-card alt reveal" data-depth="8" data-tilt><img src="https://raw.githubusercontent.com/hamooddevpng/UI-Ideas/main/assets/design40/hero/telikom-device-bundles.jpg" alt="Telikom device bundle campaign creative" loading="lazy" decoding="async"><div class="campaign-copy" data-depth="-6"><small>SUPPORTING / DEVICES</small><h3>Devices + connection.</h3><p>Keep a second pathway visible without competing with the primary campaign.</p><button class="campaign-cta ghost" type="button" data-action="devices">Explore devices ↗</button></div></article>
  </div>
  <div class="ticket-stage" aria-label="Plan rhythms">
    <button type="button" class="ticket one" data-depth="-9" data-action="daily-plan"><div><div class="eyebrow">GUTPELA / DAILY</div><h3>Today.</h3><p>Quick data for the moments that matter now.</p></div><div class="stamp" data-depth="6">FLEXIBLE<br>DATA</div></button>
    <button type="button" class="ticket two" data-depth="8" data-action="weekly-plan"><div><div class="eyebrow">GUTPELA / WEEKLY</div><h3>This week.</h3><p>More room for work, chat and everything in between.</p></div><div class="stamp" data-depth="-5">WEEKLY<br>VALUE</div></button>
    <button type="button" class="ticket three" data-depth="-6" data-action="monthly-plan"><div><div class="eyebrow">GUTPELA / MONTHLY</div><h3>Keep going.</h3><p>A longer-running option for consistent connectivity.</p></div><div class="stamp" data-depth="6">MONTHLY<br>READY</div></button>
  </div>
</section>
'''
s = replace_between(s, '<section class="plans" id="plans">', '<section class="worlds" id="worlds">', plans + '<section class="worlds" id="worlds">')

# Service categories become the Design 41 responsive service index.
services = r'''<section class="worlds" id="services">
  <div class="worlds-head reveal" data-depth="-6"><div><div class="micro">02 / SERVICE CATEGORIES</div><h2>Services that<br>react with you.</h2></div><p>Same service taxonomy, now presented as an interactive index. Hover, focus or tap a service to change the supporting story.</p></div>
  <div class="service-index reveal" data-depth="-3">
    <div class="service-list" role="tablist" aria-label="Telikom service categories">
      <button class="service-item active" type="button" role="tab" aria-selected="true" data-service="mobile" data-depth="-4"><span>01</span><b>Mobile</b><em>Prepaid, data and SIM services</em><i>↗</i></button>
      <button class="service-item" type="button" role="tab" aria-selected="false" data-service="internet" data-depth="5"><span>02</span><b>Home Internet</b><em>Availability, setup and support</em><i>↗</i></button>
      <button class="service-item" type="button" role="tab" aria-selected="false" data-service="systems" data-depth="-5"><span>03</span><b>Business Systems</b><em>Voice and workplace communication</em><i>↗</i></button>
      <button class="service-item" type="button" role="tab" aria-selected="false" data-service="data" data-depth="4"><span>04</span><b>Business Data</b><em>Connectivity between teams and sites</em><i>↗</i></button>
      <button class="service-item" type="button" role="tab" aria-selected="false" data-service="remote" data-depth="-4"><span>05</span><b>Regional + Remote</b><em>Connectivity beyond the usual reach</em><i>↗</i></button>
    </div>
    <div class="service-visual" data-depth="9">
      <img id="serviceImage" src="https://raw.githubusercontent.com/hamooddevpng/UI-Ideas/main/assets/common/png-people/young-professionals.jpg" alt="Young people in Papua New Guinea using connected devices" loading="lazy" decoding="async">
      <div class="service-visual-shade"></div><div class="service-code" id="serviceCode">MOBILE / 01</div>
      <div class="service-detail"><h3 id="serviceTitle">Everyday connection.</h3><p id="serviceText">Prepaid, data and SIM pathways that keep everyday communication simple.</p><button class="btn service-cta" id="serviceCta" type="button" data-action="mobile">Explore mobile ↗</button></div>
    </div>
  </div>
</section>
'''
s = replace_between(s, '<section class="worlds" id="worlds">', '<section class="business" id="business">', services + '<section class="business" id="business">')

# Business + Government gets explicit switchable states and a large visual split.
business = r'''<section class="business" id="business">
  <div class="business-head reveal" data-depth="-6"><div><div class="micro">03 / BUSINESS + GOVERNMENT</div><h2>Built around<br>your operation.</h2></div><p>Enterprise credibility stays clear, but the visual and copy respond as the user moves between Business and Government.</p></div>
  <div class="business-split reveal">
    <div class="segment-copy" data-depth="-5">
      <div class="segment-tabs" role="tablist" aria-label="Business and Government"><button class="segment-tab active" type="button" role="tab" aria-selected="true" data-segment="business">Business</button><button class="segment-tab" type="button" role="tab" aria-selected="false" data-segment="government">Government</button></div>
      <div class="segment-code" id="segmentCode">BUSINESS / CONNECTIVITY</div><h3 id="segmentTitle">Infrastructure for organisations that need dependable reach.</h3><p id="segmentText">Data, broadband, voice, hosting and remote connectivity brought into one practical enterprise pathway.</p>
      <div class="segment-points" id="segmentPoints"><span>Business Data</span><span>Broadband</span><span>Voice + SIP</span><span>Hosting</span><span>Remote / VSAT</span></div>
      <button class="btn fill" type="button" id="segmentCta" data-action="business">Explore business solutions ↗</button>
    </div>
    <div class="segment-visual" data-depth="8"><img id="segmentImage" src="https://raw.githubusercontent.com/hamooddevpng/UI-Ideas/main/assets/common/web-sourced/telikom/business-systems.jpg" alt="Telikom business communication systems" loading="lazy" decoding="async"><div class="segment-grid"></div><svg class="segment-lines" viewBox="0 0 700 560" aria-hidden="true"><path d="M80 410 C210 250 330 390 460 170 S610 130 650 80"/><path d="M80 170 C220 260 320 100 450 260 S590 390 650 330"/></svg><div class="segment-badge" id="segmentBadge">BUSINESS / PNG</div></div>
  </div>
</section>
'''
s = replace_between(s, '<section class="business" id="business">', '<section class="png-story" id="png-story">', business + '<section class="png-story" id="png-story">')

# PNG story: cinematic image crop plus restrained signal motif.
png_story = r'''<section class="png-story" id="png-story">
  <div class="png-story-grid">
    <div class="png-story-copy reveal" data-depth="-6"><div class="micro">04 / PNG + NATIONAL STORY</div><h2>One network.<br><span>Many lives.</span></h2><p>Connection is a call home, a classroom online, a business transaction, a health service reaching further and a community becoming easier to reach. The story stays human, not statistical.</p><div class="story-points"><span>People</span><span>Homes</span><span>Work</span><span>Communities</span></div><div class="mini-rule"></div><div class="micro">CONNECTING YOU ANYWHERE ANYTIME</div></div>
    <div class="png-story-image reveal" data-depth="8"><img src="https://raw.githubusercontent.com/hamooddevpng/UI-Ideas/main/assets/common/png-people/community-harbour.jpg" alt="Papua New Guinea community near the harbour" loading="lazy" decoding="async"><svg class="story-signal" viewBox="0 0 900 650" preserveAspectRatio="none" aria-hidden="true"><path d="M-20 520 C170 330 260 560 430 360 S680 190 930 250"/><circle cx="205" cy="405" r="7"/><circle cx="470" cy="320" r="7"/><circle cx="720" cy="225" r="7"/></svg></div>
  </div>
</section>
'''
s = replace_between(s, '<section class="png-story" id="png-story">', '<section class="news" id="news">', png_story + '<section class="news" id="news">')

# Practical two-part notices + news layer.
news = r'''<section class="news" id="news">
  <div class="news-head reveal" data-depth="-5"><div><div class="micro" style="color:#7ccfee">05 / NOTICES + NEWS</div><h2>Useful before<br>it is decorative.</h2></div><a href="#support">GET SUPPORT ↗</a></div>
  <div class="updates-layout">
    <div class="notice-board reveal" data-depth="4"><div class="notice-board-head"><span>SERVICE NOTICES</span><small>Practical information</small></div>
      <button class="notice-row" type="button" aria-expanded="false"><span class="notice-dot"></span><span><b>Check current network information</b><em>Open the service-status pathway before troubleshooting or travel.</em><small class="notice-detail">This concept does not invent live outage data. The production version should connect this row to verified Telikom service information.</small></span><i>+</i></button>
      <button class="notice-row" type="button" aria-expanded="false"><span class="notice-dot"></span><span><b>Need help with your service?</b><em>Move directly from an update into support.</em><small class="notice-detail">Recharge, account help, coverage and support remain one tap away.</small></span><i>+</i></button>
    </div>
    <div class="news-feed reveal" data-depth="-4"><div class="news-feed-head"><span>LATEST NEWS</span><small>Telikom stories and announcements</small></div>
      <a href="#news" class="news-card" data-depth="-4"><img src="https://raw.githubusercontent.com/hamooddevpng/UI-Ideas/main/assets/common/web-sourced/telikom/news-05.jpg" alt="Telikom news visual" loading="lazy" decoding="async"><span><small>NEWS / 01</small><b>Network updates and public advisories</b><em>Important information for customers and communities.</em></span><i>↗</i></a>
      <a href="#news" class="news-card" data-depth="4"><img src="https://raw.githubusercontent.com/hamooddevpng/UI-Ideas/main/assets/common/web-sourced/telikom/news-06.jpg" alt="Telikom community news visual" loading="lazy" decoding="async"><span><small>NEWS / 02</small><b>Telikom in communities across PNG</b><em>Stories about connection, service and national reach.</em></span><i>↗</i></a>
      <a href="#news" class="news-card" data-depth="-3"><img src="https://raw.githubusercontent.com/hamooddevpng/UI-Ideas/main/assets/common/web-sourced/telikom/news-03.jpg" alt="Telikom business news visual" loading="lazy" decoding="async"><span><small>NEWS / 03</small><b>Business and service announcements</b><em>Capabilities, offers and developments from Telikom.</em></span><i>↗</i></a>
    </div>
  </div>
</section>
'''
s = replace_between(s, '<section class="news" id="news">', '<section class="support-hub" id="support">', news + '<section class="support-hub" id="support">')

# Help/support/stores becomes a command layer with real interactive controls.
support = r'''<section class="support-hub" id="support">
  <div class="support-copy reveal" data-depth="-5"><div class="micro">06 / HELP + SUPPORT + STORES</div><h2>One move<br>from help.</h2><p>Practical actions stay immediate. Every command responds to hover, focus and tap, while the store field remains visual rather than pretending to be a live map.</p><div class="support-actions"><button class="support-link" type="button" data-action="recharge" data-depth="4">Recharge <span>↗</span></button><button class="support-link" type="button" data-action="selfcare" data-depth="-4">Self Care <span>↗</span></button><button class="support-link" type="button" data-action="coverage" data-depth="4">Coverage <span>↗</span></button><button class="support-link" type="button" data-action="support" data-depth="-3">Get support <span>↗</span></button><button class="support-link wide" type="button" data-action="store" data-depth="3">Find a Telikom store <span>↗</span></button></div></div>
  <div class="coordinate-field" id="coordinateField" data-depth="7"><span class="axis y">PNG / SERVICE COORDINATES</span><span class="axis x">TELIKOM / RETAIL NETWORK</span><i class="locator l1" data-label="PORT MORESBY" data-depth="-7"></i><i class="locator l2" data-label="LAE" data-depth="7"></i><i class="locator l3" data-label="MADANG" data-depth="-5"></i><i class="locator l4" data-label="MT HAGEN" data-depth="6"></i><div class="store-note">STORE FINDER / PROTOTYPE</div></div>
</section>
'''
s = replace_between(s, '<section class="support-hub" id="support">', '</main>', support + '</main>')

footer = r'''<footer>
  <div class="foot-top"><div class="foot-brand" data-depth="-1"><img src="https://raw.githubusercontent.com/hamooddevpng/UI-Ideas/main/assets/brand/telikom-logo.png" alt="Telikom PNG"><p>Connecting people, homes, businesses and communities across Papua New Guinea.</p></div><div class="foot-col"><b>Personal</b><a href="#services">Mobile</a><a href="#services">Internet</a><a href="#plans">Offers</a></div><div class="foot-col"><b>Business</b><a href="#business">Business</a><a href="#business">Government</a><a href="#business">Remote connectivity</a></div><div class="foot-col"><b>Help</b><a href="#support">Support</a><button type="button" data-action="store">Stores</button><a href="#news">Service notices</a></div></div>
  <div class="foot-bottom"><span>TELIKOM PNG</span><span>CONNECTING YOU ANYWHERE ANYTIME</span></div>
</footer>'''
s = replace_between(s, '<footer>', '<div class="chat" id="chat">', footer + '\n<div class="chat" id="chat">')

# Prototype interaction layers. No fake back-end state, but every important control does something.
overlays = r'''<div class="chat" id="chat"><div class="chat-panel"><div class="chat-head"><span>✦</span><div><b>Telikom Assistant</b><small>How can we help?</small></div></div><div class="chat-body">Choose a common task or ask about Telikom services.</div><div class="chat-actions"><button type="button" data-action="recharge">Top up</button><button type="button" data-action="bill">Pay bill</button><button type="button" data-action="mobile-data">Find a plan</button><button type="button" data-action="support">Get support</button></div></div><button class="chat-launch" id="chatLaunch" type="button" aria-label="Open Telikom assistant" aria-expanded="false">✦</button></div>
<div class="search-overlay" id="searchOverlay" role="dialog" aria-modal="true" aria-labelledby="searchTitle" aria-hidden="true"><div class="search-card"><button class="overlay-close" type="button" data-close-search aria-label="Close search">×</button><div class="micro">SEARCH TELIKOM</div><h2 id="searchTitle">What do you need?</h2><input id="searchInput" type="search" placeholder="Try recharge, coverage, internet..." autocomplete="off"><div class="search-suggestions"><button type="button" data-action="recharge">Recharge</button><button type="button" data-action="coverage">Coverage</button><button type="button" data-action="selfcare">Self Care</button><button type="button" data-action="support">Support</button></div></div></div>
<div class="action-drawer" id="actionDrawer" role="dialog" aria-modal="true" aria-labelledby="drawerTitle" aria-hidden="true"><button class="drawer-backdrop" type="button" data-close-drawer aria-label="Close"></button><aside><button class="overlay-close" type="button" data-close-drawer aria-label="Close panel">×</button><div class="micro" id="drawerCode">TELIKOM / ACTION</div><h2 id="drawerTitle">Start here.</h2><p id="drawerText">This interaction is ready to connect to the final Telikom destination.</p><div class="drawer-actions"><button class="btn fill" type="button" data-close-drawer>Continue</button><button class="btn" type="button" data-close-drawer>Back</button></div></aside></div>
'''
s = re.sub(r'<div class="chat" id="chat">.*?</div>\n<script>\n\(\(\)=>\{', overlays + '<script>\n(()=>{', s, count=1, flags=re.S)

# CSS rules layer. These override the Design 10 baseline without destroying its visual DNA.
css = r'''
/* DESIGN 41 RULES PASS */
:root{--ease-soft:cubic-bezier(.2,.72,.24,1);--focus:0 0 0 3px rgba(36,155,232,.25)}
button{color:inherit}.topbar{transition:top .35s var(--ease-soft),padding .35s var(--ease-soft),background .35s var(--ease-soft),box-shadow .35s var(--ease-soft),border-radius .35s var(--ease-soft)}.topbar.scrolled{top:8px;padding-top:8px;padding-bottom:8px;background:rgba(255,255,255,.94);box-shadow:0 18px 46px rgba(24,74,103,.11)}.topbar.scrolled .brand img{height:36px}.brand img{transition:height .35s var(--ease-soft)}
.nav{position:relative}.nav-glider{position:absolute;left:0;bottom:3px;height:2px;width:0;border-radius:99px;background:var(--blue);opacity:0;transition:translate .38s var(--ease-soft),width .38s var(--ease-soft),opacity .2s}.nav a{position:relative;z-index:1;background:transparent!important}.utility button{border:0;background:transparent;padding:10px 12px;border-radius:10px;font-size:10px;font-weight:800;cursor:pointer}.utility .primary{background:var(--ink);color:#fff;min-height:44px}.search-trigger:hover{background:var(--soft)}
.mobile-panel{display:none;position:fixed;z-index:88;left:12px;right:12px;top:78px;padding:12px;border:1px solid var(--line);border-radius:18px;background:rgba(255,255,255,.96);backdrop-filter:blur(18px);box-shadow:0 26px 70px rgba(22,69,97,.16);transform-origin:top;opacity:0;translate:0 -8px;transition:opacity .28s var(--ease-soft),translate .28s var(--ease-soft)}.mobile-panel.open{opacity:1;translate:0 0}.mobile-panel a,.mobile-panel button{display:flex;width:100%;min-height:48px;align-items:center;padding:0 14px;border:0;border-bottom:1px solid var(--line);background:transparent;text-align:left;font-weight:800}.mobile-panel>*:last-child{border-bottom:0;color:var(--blue)}
.campaign-label{position:absolute;z-index:4;right:18px;top:18px;padding:8px 10px;border:1px solid rgba(255,255,255,.42);border-radius:999px;background:rgba(8,45,70,.45);backdrop-filter:blur(10px);color:#fff;font:500 8px DM Mono,monospace;letter-spacing:.12em}.stage-photo{opacity:.54;filter:saturate(.96) contrast(.96);mix-blend-mode:normal}.stage-shell:hover .stage-photo{opacity:.66}.stage-shell canvas{opacity:.58;mix-blend-mode:multiply}.three-ready .fallback-object{opacity:0}
.quick-zone{position:relative;z-index:12;margin:-30px 5vw 92px}.quick-band{margin:0;overflow:visible}.quick-action{border:0;border-right:1px solid var(--line);text-align:left;cursor:pointer;min-height:118px;position:relative}.quick-action>span:nth-child(2){flex:1}.quick-action em{display:block;margin-top:5px;font-size:9px;font-style:normal;color:#7890a0}.quick-action:hover em{color:#b6cfdd}.quick-icon{width:42px;height:42px;border:1px solid var(--line);border-radius:50%;display:grid;place-items:center;font-size:17px;transition:scale .32s var(--ease-soft),translate .32s var(--ease-soft),background .32s}.quick-action:hover .quick-icon{translate:0 -5px;scale:1.06;background:rgba(255,255,255,.1)}.quick-action:active{scale:.985}.quick-secondary{display:flex;justify-content:center;gap:4px 18px;flex-wrap:wrap;padding:15px 12px 0}.quick-secondary a,.quick-secondary button{border:0;background:transparent;padding:8px 4px;color:#668095;font-size:9px;font-weight:800;cursor:pointer}.quick-secondary a:hover,.quick-secondary button:hover{color:var(--blue)}
.campaign-deck{grid-template-columns:1.42fr .58fr}.campaign-card{transform-style:preserve-3d;transition:transform .45s var(--ease-soft),box-shadow .45s var(--ease-soft),border-color .45s var(--ease-soft)}.campaign-card.feature{min-height:520px}.campaign-card.alt{min-height:520px}.campaign-card:focus-within{box-shadow:var(--focus),0 28px 60px rgba(30,88,123,.1)}.campaign-cta{margin-top:18px;min-height:44px;padding:10px 14px;border-radius:999px;border:1px solid #fff;background:#fff;color:var(--ink);font-size:10px;font-weight:800;cursor:pointer}.campaign-cta.ghost{background:rgba(8,45,70,.72);color:#fff;border-color:rgba(255,255,255,.55)}.ticket{cursor:pointer;text-align:left;color:var(--ink)}.ticket:focus-visible{outline:none;box-shadow:var(--focus),0 35px 80px rgba(37,92,124,.12)}
.service-index{display:grid;grid-template-columns:.88fr 1.12fr;gap:14px;align-items:stretch}.service-list{display:flex;flex-direction:column;border-top:1px solid var(--line)}.service-item{display:grid;grid-template-columns:46px 1fr auto;grid-template-areas:'num title arrow' 'num desc arrow';align-items:center;column-gap:16px;min-height:105px;padding:18px 12px;border:0;border-bottom:1px solid var(--line);background:transparent;color:var(--ink);text-align:left;cursor:pointer;transition:padding .38s var(--ease-soft),background .38s var(--ease-soft),color .38s var(--ease-soft)}.service-item>span{grid-area:num;font:500 9px DM Mono,monospace;color:#7892a4}.service-item>b{grid-area:title;font-size:clamp(22px,2.4vw,36px);letter-spacing:-.04em}.service-item>em{grid-area:desc;font-size:10px;font-style:normal;color:#738c9d}.service-item>i{grid-area:arrow;font-style:normal;width:42px;height:42px;border:1px solid var(--line);border-radius:50%;display:grid;place-items:center;transition:rotate .35s var(--ease-soft),background .35s}.service-item.active,.service-item:hover,.service-item:focus-visible{padding-left:22px;background:#fff}.service-item.active b{color:var(--blue)}.service-item.active i{background:var(--ink);color:#fff;rotate:-25deg}.service-visual{position:relative;min-height:590px;border-radius:30px;overflow:hidden;background:var(--ink);isolation:isolate}.service-visual img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;transition:opacity .34s var(--ease-soft),scale 1.15s var(--ease-soft);scale:1.02}.service-visual.is-changing img{opacity:.2;scale:1.06}.service-visual-shade{position:absolute;inset:0;background:linear-gradient(180deg,rgba(3,31,48,.02),rgba(3,31,48,.16) 44%,rgba(3,31,48,.9));z-index:1}.service-code{position:absolute;z-index:2;right:20px;top:18px;padding:8px 10px;border:1px solid rgba(255,255,255,.34);border-radius:999px;color:#fff;font:500 8px DM Mono,monospace;letter-spacing:.12em}.service-detail{position:absolute;z-index:2;left:28px;right:28px;bottom:28px;color:#fff}.service-detail h3{font-size:clamp(40px,5vw,74px);line-height:.9;letter-spacing:-.055em;margin:0 0 12px;max-width:650px}.service-detail p{max-width:520px;color:#d6e5ee;line-height:1.6;font-size:12px}.service-detail .btn{border-color:rgba(255,255,255,.65);color:#fff}
.business-split{display:grid;grid-template-columns:.78fr 1.22fr;gap:14px;align-items:stretch}.segment-copy{padding:34px 24px 34px 0;display:flex;flex-direction:column;justify-content:center}.segment-tabs{display:flex;gap:8px;margin-bottom:34px}.segment-tab{min-height:44px;padding:0 16px;border:1px solid var(--line);border-radius:999px;background:#fff;font-size:10px;font-weight:800;cursor:pointer}.segment-tab.active{background:var(--ink);color:#fff;border-color:var(--ink)}.segment-code{font:500 8px DM Mono,monospace;letter-spacing:.13em;color:var(--blue)}.segment-copy h3{font-size:clamp(38px,4.6vw,72px);line-height:.93;letter-spacing:-.055em;margin:14px 0 18px}.segment-copy p{font-size:13px;line-height:1.7;color:#607d90;max-width:540px}.segment-points{display:flex;gap:7px;flex-wrap:wrap;margin:22px 0 28px}.segment-points span{padding:8px 10px;border-radius:999px;background:var(--soft);font-size:9px;font-weight:800;color:#567286}.segment-visual{position:relative;min-height:610px;border-radius:30px;overflow:hidden;background:var(--ink);isolation:isolate}.segment-visual img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;transition:opacity .36s var(--ease-soft),scale 1.2s var(--ease-soft);scale:1.02}.segment-visual.is-changing img{opacity:.2;scale:1.06}.segment-visual:after{content:'';position:absolute;inset:0;background:linear-gradient(180deg,rgba(8,45,70,.08),rgba(8,45,70,.58));z-index:1}.segment-grid{position:absolute;inset:0;z-index:2;background-image:linear-gradient(rgba(255,255,255,.08) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.08) 1px,transparent 1px);background-size:48px 48px;mask-image:linear-gradient(to bottom,rgba(0,0,0,.7),transparent)}.segment-lines{position:absolute;inset:0;width:100%;height:100%;z-index:3}.segment-lines path{fill:none;stroke:#7ccfee;stroke-width:1.5;stroke-dasharray:8 11;animation:dash 14s linear infinite;opacity:.75}.segment-lines path:nth-child(2){animation-direction:reverse;opacity:.42}.segment-badge{position:absolute;z-index:4;left:20px;bottom:18px;padding:8px 10px;border-radius:999px;background:rgba(255,255,255,.8);backdrop-filter:blur(10px);font:500 8px DM Mono,monospace;letter-spacing:.12em;color:var(--ink)}
.story-points{display:flex;gap:7px;flex-wrap:wrap;margin:18px 0}.story-points span{padding:7px 10px;border:1px solid var(--line);border-radius:999px;font-size:9px;font-weight:800}.story-signal{position:absolute;inset:0;width:100%;height:100%;z-index:3}.story-signal path{fill:none;stroke:#fff;stroke-width:2;stroke-dasharray:8 12;animation:dash 18s linear infinite;filter:drop-shadow(0 0 6px rgba(8,45,70,.28))}.story-signal circle{fill:#fff;stroke:var(--blue);stroke-width:3}
.updates-layout{display:grid;grid-template-columns:.78fr 1.22fr;gap:28px;position:relative;z-index:2}.notice-board,.news-feed{border-top:1px solid rgba(255,255,255,.18)}.notice-board-head,.news-feed-head{display:flex;justify-content:space-between;align-items:center;padding:18px 0;border-bottom:1px solid rgba(255,255,255,.14)}.notice-board-head span,.news-feed-head span{font:500 9px DM Mono,monospace;letter-spacing:.12em;color:#7ccfee}.notice-board-head small,.news-feed-head small{color:#9eb8c8;font-size:9px}.notice-row{width:100%;display:grid;grid-template-columns:16px 1fr auto;gap:12px;align-items:start;padding:22px 8px;border:0;border-bottom:1px solid rgba(255,255,255,.14);background:transparent;color:#fff;text-align:left;cursor:pointer}.notice-dot{width:7px;height:7px;border-radius:50%;background:#7ccfee;margin-top:5px}.notice-row b{display:block;font-size:14px}.notice-row em{display:block;margin-top:6px;font-size:10px;font-style:normal;color:#a9c2d1;line-height:1.5}.notice-row>i{font-style:normal;font-size:20px;color:#7ccfee;transition:rotate .3s}.notice-detail{display:grid;grid-template-rows:0fr;overflow:hidden;color:#d8e6ee;font-size:10px;line-height:1.55;transition:grid-template-rows .35s var(--ease-soft),margin .35s}.notice-row[aria-expanded=true] .notice-detail{grid-template-rows:1fr;margin-top:12px}.notice-row[aria-expanded=true]>i{rotate:45deg}.news-card{display:grid;grid-template-columns:92px 1fr auto;gap:18px;align-items:center;padding:14px 0;border-bottom:1px solid rgba(255,255,255,.14)}.news-card img{width:92px;height:82px;border-radius:12px;object-fit:cover;transition:scale .55s var(--ease-soft)}.news-card:hover img{scale:1.04}.news-card small{display:block;color:#7ccfee;font:500 8px DM Mono,monospace;letter-spacing:.1em}.news-card b{display:block;font-size:18px;line-height:1.15;margin-top:5px}.news-card em{display:block;font-style:normal;color:#9fb9c9;font-size:10px;margin-top:5px}.news-card>i{font-style:normal;width:42px;height:42px;border:1px solid rgba(255,255,255,.2);border-radius:50%;display:grid;place-items:center}
.support-actions{grid-template-columns:1fr 1fr}.support-link{cursor:pointer;color:var(--ink);text-align:left;min-height:54px}.support-link.wide{grid-column:1/-1}.store-note{position:absolute;right:16px;top:16px;padding:7px 9px;border-radius:999px;background:rgba(255,255,255,.82);font:500 8px DM Mono,monospace;letter-spacing:.1em}.locator{animation:none}.coordinate-field.in-view .locator{animation:pulse-once .75s var(--ease-soft) 1}.foot-col button{display:block;border:0;background:transparent;padding:0;color:#6b8495;font-size:11px;margin-top:11px;cursor:pointer}.foot-col a,.foot-col button{position:relative}.foot-col a:after,.foot-col button:after{content:'';position:absolute;left:0;bottom:-3px;width:100%;height:1px;background:var(--blue);scale:0 1;transform-origin:left;transition:scale .28s}.foot-col a:hover:after,.foot-col button:hover:after{scale:1 1}
.search-overlay{position:fixed;inset:0;z-index:300;display:grid;place-items:start center;padding:110px 18px 18px;background:rgba(8,45,70,.3);backdrop-filter:blur(12px);opacity:0;visibility:hidden;transition:opacity .28s}.search-overlay.open{opacity:1;visibility:visible}.search-card{position:relative;width:min(760px,100%);padding:30px;border-radius:26px;background:#fff;box-shadow:0 35px 100px rgba(8,45,70,.22)}.search-card h2,.action-drawer h2{font-size:clamp(38px,6vw,70px);line-height:.92;letter-spacing:-.06em;margin:10px 0 22px}.search-card input{width:100%;min-height:58px;padding:0 18px;border:1px solid var(--line);border-radius:14px;font:600 16px Manrope}.search-suggestions{display:flex;gap:8px;flex-wrap:wrap;margin-top:14px}.search-suggestions button{min-height:44px;padding:0 14px;border:1px solid var(--line);border-radius:999px;background:var(--soft);font-weight:800;cursor:pointer}.overlay-close{position:absolute;right:16px;top:14px;width:44px;height:44px;border:1px solid var(--line);border-radius:50%;background:#fff;font-size:24px;cursor:pointer}.action-drawer{position:fixed;inset:0;z-index:320;visibility:hidden}.action-drawer.open{visibility:visible}.drawer-backdrop{position:absolute;inset:0;border:0;background:rgba(8,45,70,.34);opacity:0;transition:opacity .3s}.action-drawer.open .drawer-backdrop{opacity:1}.action-drawer aside{position:absolute;right:0;top:0;height:100%;width:min(520px,94vw);padding:88px 34px 34px;background:#fff;box-shadow:-28px 0 80px rgba(8,45,70,.18);translate:100% 0;transition:translate .42s var(--ease-soft)}.action-drawer.open aside{translate:0 0}.action-drawer p{font-size:14px;line-height:1.7;color:#607d90}.drawer-actions{display:flex;gap:8px;margin-top:26px}
:where(a,button,input):focus-visible{outline:none;box-shadow:var(--focus)}.btn:active,.campaign-cta:active,.segment-tab:active,.support-link:active,.search-suggestions button:active{scale:.985}
@keyframes pulse-once{0%{scale:.75;opacity:.45}55%{scale:1.14;opacity:1}100%{scale:1;opacity:1}}
@media(max-width:1050px){.mobile-panel{display:block}.utility .search-trigger{display:none}.service-index,.business-split,.updates-layout{grid-template-columns:1fr}.service-visual,.segment-visual{min-height:520px}.segment-copy{padding-right:0}.campaign-deck{grid-template-columns:1fr 1fr}}
@media(max-width:700px){.topbar .utility .primary{display:none}.quick-zone{margin:-12px 18px 68px}.quick-band{grid-template-columns:1fr 1fr}.quick-action{min-height:104px;padding:15px}.quick-action:nth-child(2){border-right:0}.quick-action:nth-child(-n+2){border-bottom:1px solid var(--line)}.quick-action em{display:none}.quick-icon{width:34px;height:34px}.campaign-deck{display:grid;grid-auto-flow:column;grid-template-columns:84vw 84vw;overflow-x:auto;scroll-snap-type:x proximity;padding-bottom:8px}.campaign-card{scroll-snap-align:start}.campaign-card.feature,.campaign-card.alt{min-height:420px}.service-index{display:block}.service-list{overflow-x:auto;flex-direction:row;scroll-snap-type:x proximity}.service-item{min-width:78vw;scroll-snap-align:start;grid-template-columns:38px 1fr auto}.service-visual{min-height:480px;margin-top:12px}.business-head{margin-bottom:42px}.segment-visual{min-height:470px}.updates-layout{gap:26px}.news-card{grid-template-columns:72px 1fr auto}.news-card img{width:72px;height:72px}.news-card em{display:none}.support-actions{grid-template-columns:1fr}.support-link.wide{grid-column:auto}.search-overlay{padding-top:86px}.search-card{padding:26px 18px}.action-drawer aside{padding:82px 22px 24px}.stage-shell canvas{opacity:.38}}
@media(prefers-reduced-motion:reduce){[data-depth]{translate:0 0!important}.stage-shell canvas{display:none}.ticker-track,.segment-lines path,.story-signal path{animation:none!important}.campaign-card{transform:none!important}.service-visual img,.segment-visual img{transition:none!important}}
'''
s = s.replace('</style>', css + '\n</style>', 1)

# Replace inline JS with the Design 10 foundation adapted to current Design 41 rules.
js = r'''<script>
(()=>{
  const root=document.documentElement;
  const clamp=(n,a=-1,b=1)=>Math.max(a,Math.min(b,n));
  const reduced=matchMedia('(prefers-reduced-motion: reduce)').matches;
  const fine=matchMedia('(hover:hover) and (pointer:fine)').matches;
  let lastX=innerWidth/2,lastY=innerHeight/2,pointerSeen=false;

  if(!reduced&&window.Lenis){
    const lenis=new Lenis({duration:1.05,smoothWheel:true,syncTouch:false,touchMultiplier:1,wheelMultiplier:.9,easing:t=>1-Math.pow(1-t,4)});
    const raf=t=>{lenis.raf(t);requestAnimationFrame(raf)};requestAnimationFrame(raf);
  }

  const header=document.getElementById('siteHeader');
  const menuButton=document.getElementById('menuButton');
  const mobilePanel=document.getElementById('mobilePanel');
  const updateHeader=()=>header&&header.classList.toggle('scrolled',scrollY>34);
  addEventListener('scroll',updateHeader,{passive:true});updateHeader();
  if(menuButton&&mobilePanel){
    menuButton.addEventListener('click',()=>{const open=!mobilePanel.classList.contains('open');mobilePanel.classList.toggle('open',open);mobilePanel.setAttribute('aria-hidden',String(!open));menuButton.setAttribute('aria-expanded',String(open))});
    mobilePanel.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>{mobilePanel.classList.remove('open');mobilePanel.setAttribute('aria-hidden','true');menuButton.setAttribute('aria-expanded','false')}));
  }

  const nav=document.getElementById('primaryNav'),glider=document.getElementById('navGlider');
  if(nav&&glider){
    const place=el=>{const nr=nav.getBoundingClientRect(),r=el.getBoundingClientRect();glider.style.width=r.width+'px';glider.style.translate=(r.left-nr.left)+'px 0';glider.style.opacity='1'};
    nav.querySelectorAll('a').forEach(a=>{a.addEventListener('pointerenter',()=>place(a));a.addEventListener('focus',()=>place(a))});
    nav.addEventListener('pointerleave',()=>glider.style.opacity='0');
  }

  const search=document.getElementById('searchOverlay'),searchTrigger=document.getElementById('searchTrigger'),searchInput=document.getElementById('searchInput');
  const openSearch=()=>{if(!search)return;search.classList.add('open');search.setAttribute('aria-hidden','false');setTimeout(()=>searchInput&&searchInput.focus(),60)};
  const closeSearch=()=>{if(!search)return;search.classList.remove('open');search.setAttribute('aria-hidden','true');searchTrigger&&searchTrigger.focus()};
  searchTrigger&&searchTrigger.addEventListener('click',openSearch);
  document.querySelectorAll('[data-close-search]').forEach(x=>x.addEventListener('click',closeSearch));
  addEventListener('keydown',e=>{if(e.key==='/'&&!e.metaKey&&!e.ctrlKey&&!e.altKey&&document.activeElement?.tagName!=='INPUT'){e.preventDefault();openSearch()}if(e.key==='Escape'){closeSearch();closeDrawer();if(mobilePanel?.classList.contains('open'))menuButton?.click()}});

  const actionCopy={
    recharge:['RECHARGE / TOP UP','Recharge quickly.','Connect this action to Telikom recharge or top-up services.'],
    selfcare:['SELF CARE / ACCOUNT','Manage your services.','Open the authenticated Self Care pathway for account and service management.'],
    coverage:['COVERAGE / AVAILABILITY','Check what is available.','Connect this to verified mobile or internet availability information.'],
    support:['SUPPORT / HELP','Get the right help.','Route customers to Telikom support without making them search through the site.'],
    store:['STORES / RETAIL','Find Telikom nearby.','Connect this prototype to the verified Telikom store finder.'],
    sim:['SIM / MOBILE','Start with a SIM.','Route to SIM purchase, registration or eSIM information.'],
    bill:['BILL / PAYMENT','Pay a bill.','Connect this action to the verified Telikom bill-payment pathway.'],
    business:['BUSINESS / ENQUIRIES','Talk about your operation.','Route organisations to the right Telikom business enquiry pathway.'],
    'mobile-data':['MOBILE / DATA','Explore mobile data.','Show verified Telikom data options without inventing prices or allowances.'],
    devices:['DEVICES / CONNECTION','Explore devices.','Connect customers to verified Telikom device and bundle options.'],
    'daily-plan':['PLAN / DAILY','A short-term data pathway.','Use verified Telikom daily plan information in production.'],
    'weekly-plan':['PLAN / WEEKLY','A weekly data pathway.','Use verified Telikom weekly plan information in production.'],
    'monthly-plan':['PLAN / MONTHLY','A longer-running data pathway.','Use verified Telikom monthly plan information in production.'],
    mobile:['MOBILE / SERVICES','Explore mobile.','Prepaid, data and SIM pathways for everyday connection.'],internet:['INTERNET / HOME','Explore home internet.','Availability, installation and support pathways for home connectivity.'],systems:['BUSINESS / SYSTEMS','Explore business systems.','Voice and communication services for organisations.'],data:['BUSINESS / DATA','Explore business data.','Connectivity between teams, offices and locations.'],remote:['REMOTE / REGIONAL','Reach further.','Connectivity pathways for regional and remote requirements.']
  };
  const drawer=document.getElementById('actionDrawer'),drawerCode=document.getElementById('drawerCode'),drawerTitle=document.getElementById('drawerTitle'),drawerText=document.getElementById('drawerText');
  function openDrawer(key){if(!drawer)return;const c=actionCopy[key]||['TELIKOM / ACTION','Start here.','This interaction is ready to connect to the final Telikom destination.'];drawerCode.textContent=c[0];drawerTitle.textContent=c[1];drawerText.textContent=c[2];drawer.classList.add('open');drawer.setAttribute('aria-hidden','false')}
  function closeDrawer(){if(!drawer)return;drawer.classList.remove('open');drawer.setAttribute('aria-hidden','true')}
  document.querySelectorAll('[data-action]').forEach(el=>el.addEventListener('click',e=>{e.preventDefault();closeSearch();openDrawer(el.dataset.action)}));
  document.querySelectorAll('[data-close-drawer]').forEach(x=>x.addEventListener('click',closeDrawer));

  const serviceData={
    mobile:{code:'MOBILE / 01',title:'Everyday connection.',text:'Prepaid, data and SIM pathways that keep everyday communication simple.',image:'https://raw.githubusercontent.com/hamooddevpng/UI-Ideas/main/assets/common/png-people/young-professionals.jpg',alt:'Young people in Papua New Guinea using connected devices'},
    internet:{code:'HOME INTERNET / 02',title:'Home, always on.',text:'Availability, installation and support pathways for study, work, streaming and everyday home use.',image:'https://raw.githubusercontent.com/hamooddevpng/UI-Ideas/main/assets/common/web-sourced/telikom/fixed-broadband.jpg',alt:'Telikom fixed broadband connectivity'},
    systems:{code:'BUSINESS SYSTEMS / 03',title:'Communication built for work.',text:'Voice and workplace communication services for organisations that need dependable contact.',image:'https://raw.githubusercontent.com/hamooddevpng/UI-Ideas/main/assets/common/web-sourced/telikom/business-systems.jpg',alt:'Telikom business communication systems'},
    data:{code:'BUSINESS DATA / 04',title:'Keep teams and locations connected.',text:'Data connectivity for organisations that need dependable links between people, sites and systems.',image:'https://raw.githubusercontent.com/hamooddevpng/UI-Ideas/main/assets/common/web-sourced/telikom/business-data.jpg',alt:'Telikom business data connectivity'},
    remote:{code:'REGIONAL + REMOTE / 05',title:'Reach beyond the usual.',text:'Connectivity pathways for communities and organisations operating beyond conventional reach.',image:'https://raw.githubusercontent.com/hamooddevpng/UI-Ideas/main/assets/common/png-people/market-connectivity.jpg',alt:'People using connectivity at a Papua New Guinea market'}
  };
  const serviceImage=document.getElementById('serviceImage'),serviceTitle=document.getElementById('serviceTitle'),serviceText=document.getElementById('serviceText'),serviceCode=document.getElementById('serviceCode'),serviceCta=document.getElementById('serviceCta'),serviceVisual=document.querySelector('.service-visual');
  const setService=key=>{const d=serviceData[key];if(!d)return;document.querySelectorAll('.service-item').forEach(b=>{const active=b.dataset.service===key;b.classList.toggle('active',active);b.setAttribute('aria-selected',String(active))});serviceVisual?.classList.add('is-changing');setTimeout(()=>{if(serviceImage){serviceImage.src=d.image;serviceImage.alt=d.alt}if(serviceTitle)serviceTitle.textContent=d.title;if(serviceText)serviceText.textContent=d.text;if(serviceCode)serviceCode.textContent=d.code;if(serviceCta)serviceCta.dataset.action=key;serviceVisual?.classList.remove('is-changing')},150)};
  document.querySelectorAll('.service-item').forEach(b=>{b.addEventListener('click',()=>setService(b.dataset.service));b.addEventListener('focus',()=>setService(b.dataset.service));if(fine)b.addEventListener('pointerenter',()=>setService(b.dataset.service))});

  const segmentData={business:{code:'BUSINESS / CONNECTIVITY',title:'Infrastructure for organisations that need dependable reach.',text:'Data, broadband, voice, hosting and remote connectivity brought into one practical enterprise pathway.',points:['Business Data','Broadband','Voice + SIP','Hosting','Remote / VSAT'],image:'https://raw.githubusercontent.com/hamooddevpng/UI-Ideas/main/assets/common/web-sourced/telikom/business-systems.jpg',alt:'Telikom business communication systems',badge:'BUSINESS / PNG'},government:{code:'GOVERNMENT / CONNECTIVITY',title:'Connectivity pathways for public-sector operations.',text:'A clear government pathway for communication, data, hosting and remote service requirements across locations.',points:['Government Data','Voice','Hosting','Remote Access','Support'],image:'https://raw.githubusercontent.com/hamooddevpng/UI-Ideas/main/assets/common/png-people/community-harbour.jpg',alt:'Papua New Guinea community near the harbour',badge:'GOVERNMENT / PNG'}};
  const segmentImage=document.getElementById('segmentImage'),segmentTitle=document.getElementById('segmentTitle'),segmentText=document.getElementById('segmentText'),segmentCode=document.getElementById('segmentCode'),segmentPoints=document.getElementById('segmentPoints'),segmentBadge=document.getElementById('segmentBadge'),segmentVisual=document.querySelector('.segment-visual');
  const setSegment=key=>{const d=segmentData[key];if(!d)return;document.querySelectorAll('.segment-tab').forEach(b=>{const active=b.dataset.segment===key;b.classList.toggle('active',active);b.setAttribute('aria-selected',String(active))});segmentVisual?.classList.add('is-changing');setTimeout(()=>{segmentImage.src=d.image;segmentImage.alt=d.alt;segmentTitle.textContent=d.title;segmentText.textContent=d.text;segmentCode.textContent=d.code;segmentPoints.innerHTML=d.points.map(x=>`<span>${x}</span>`).join('');segmentBadge.textContent=d.badge;segmentVisual?.classList.remove('is-changing')},150)};
  document.querySelectorAll('.segment-tab').forEach(b=>{b.addEventListener('click',()=>setSegment(b.dataset.segment));b.addEventListener('focus',()=>setSegment(b.dataset.segment));if(fine)b.addEventListener('pointerenter',()=>setSegment(b.dataset.segment))});

  document.querySelectorAll('.notice-row').forEach(row=>row.addEventListener('click',()=>row.setAttribute('aria-expanded',String(row.getAttribute('aria-expanded')!=='true'))));

  const reveals=[...document.querySelectorAll('.reveal')];
  if('IntersectionObserver' in window&&!reduced){const io=new IntersectionObserver(entries=>entries.forEach(x=>{if(x.isIntersecting){x.target.classList.add('in');io.unobserve(x.target)}}),{threshold:.12,rootMargin:'0px 0px -4%'});reveals.forEach(x=>io.observe(x))}else reveals.forEach(x=>x.classList.add('in'));
  const field=document.getElementById('coordinateField');if(field&&'IntersectionObserver' in window){const fio=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){field.classList.add('in-view');fio.disconnect()}}),{threshold:.3});fio.observe(field)}

  const updateScroll=()=>{const max=Math.max(1,document.documentElement.scrollHeight-innerHeight);root.style.setProperty('--scroll',(scrollY/max).toFixed(4))};addEventListener('scroll',updateScroll,{passive:true});updateScroll();
  const lightField=(el,xName,yName)=>{if(!el||!fine||reduced)return;el.addEventListener('pointermove',e=>{const r=el.getBoundingClientRect();el.style.setProperty(xName,((e.clientX-r.left)/r.width*100).toFixed(1)+'%');el.style.setProperty(yName,((e.clientY-r.top)/r.height*100).toFixed(1)+'%')},{passive:true})};lightField(document.getElementById('coordinateField'),'--fx','--fy');

  const cursor=document.getElementById('cursor');
  if(cursor&&fine&&!reduced){document.addEventListener('pointermove',e=>{pointerSeen=true;lastX=e.clientX;lastY=e.clientY;root.style.setProperty('--cx',e.clientX+'px');root.style.setProperty('--cy',e.clientY+'px');cursor.style.left=e.clientX+'px';cursor.style.top=e.clientY+'px';cursor.style.opacity='1'},{passive:true});document.querySelectorAll('a,button,.campaign-card,.service-item,.news-card,.segment-visual,.coordinate-field').forEach(el=>{el.addEventListener('pointerenter',()=>cursor.classList.add('hot'));el.addEventListener('pointerleave',()=>cursor.classList.remove('hot'))})}else if(cursor)cursor.style.display='none';

  // Design 10 proximity field, rewritten for Design 41: no bounce, no idle drift, slow interpolation, desktop only.
  if(fine&&!reduced){
    const motion=[...document.querySelectorAll('[data-depth]')].map((el,i)=>({el,depth:parseFloat(el.dataset.depth)||0,x:0,y:0,tx:0,ty:0}));
    const motionFrame=()=>{requestAnimationFrame(motionFrame);const vh=innerHeight;motion.forEach(o=>{const r=o.el.getBoundingClientRect();if(r.bottom<-140||r.top>vh+140){o.tx=o.ty=0}else if(pointerSeen){const cx=r.left+r.width/2,cy=r.top+r.height/2,dx=lastX-cx,dy=lastY-cy;const radius=clamp(Math.max(r.width,r.height)*.72+250,300,720);const dist=Math.hypot(dx,dy);const pwr=dist<radius?Math.pow(1-dist/radius,2):0;const nx=clamp(dx/Math.max(180,r.width*.7)),ny=clamp(dy/Math.max(160,r.height*.7));o.tx=nx*o.depth*.72*pwr;o.ty=ny*o.depth*.5*pwr}else{o.tx=o.ty=0}o.x+=(o.tx-o.x)*.065;o.y+=(o.ty-o.y)*.065;o.el.style.translate=`${o.x.toFixed(2)}px ${o.y.toFixed(2)}px`});};requestAnimationFrame(motionFrame);

    document.querySelectorAll('[data-tilt]').forEach(el=>{el.addEventListener('pointermove',e=>{const r=el.getBoundingClientRect(),x=(e.clientX-r.left)/r.width-.5,y=(e.clientY-r.top)/r.height-.5;el.style.transform=`perspective(1000px) rotateX(${(-y*2.4).toFixed(2)}deg) rotateY(${(x*3).toFixed(2)}deg)`},{passive:true});el.addEventListener('pointerleave',()=>el.style.transform='perspective(1000px) rotateX(0deg) rotateY(0deg)')});
  }

  // Keep the single inherited Design 10 abstract hero sculpture. No additional WebGL scenes are introduced.
  const canvas=document.getElementById('sculpture'),shell=document.getElementById('stageShell');
  if(canvas&&shell&&window.THREE&&!reduced){try{const scene=new THREE.Scene(),camera=new THREE.PerspectiveCamera(35,1,.1,100);camera.position.set(0,0,7.2);const renderer=new THREE.WebGLRenderer({canvas,alpha:true,antialias:true});renderer.setPixelRatio(Math.min(devicePixelRatio,1.6));renderer.setClearColor(0x000000,0);const group=new THREE.Group();scene.add(group);const knot=new THREE.Mesh(new THREE.TorusKnotGeometry(1.52,.43,180,24,2,3),new THREE.MeshPhysicalMaterial({color:0x008fd3,roughness:.22,metalness:.12,transmission:.18,transparent:true,opacity:.72,clearcoat:1,clearcoatRoughness:.1}));group.add(knot);const wire=new THREE.LineSegments(new THREE.WireframeGeometry(new THREE.IcosahedronGeometry(2.32,2)),new THREE.LineBasicMaterial({color:0x35b9ef,transparent:true,opacity:.28}));group.add(wire);const inner=new THREE.Mesh(new THREE.IcosahedronGeometry(.7,1),new THREE.MeshBasicMaterial({color:0x3594d1,wireframe:true,transparent:true,opacity:.62}));group.add(inner);scene.add(new THREE.AmbientLight(0xffffff,2));const key=new THREE.DirectionalLight(0xffffff,3.7);key.position.set(4,4,5);scene.add(key);const resize=()=>{const r=shell.getBoundingClientRect();renderer.setSize(Math.max(1,r.width),Math.max(1,r.height),false);camera.aspect=r.width/Math.max(1,r.height);camera.updateProjectionMatrix()};resize();addEventListener('resize',resize,{passive:true});shell.classList.add('three-ready');let mx=0,my=0,tx=0,ty=0,t=0;document.addEventListener('pointermove',e=>{if(!fine)return;tx=(e.clientX/innerWidth-.5)*2;ty=(e.clientY/innerHeight-.5)*2},{passive:true});const draw=()=>{requestAnimationFrame(draw);t+=.006;mx+=(tx-mx)*.045;my+=(ty-my)*.045;group.rotation.y=t*.4+mx*.25;group.rotation.x=.22+my*.18;knot.rotation.z=-t*.2;wire.rotation.z=t*.1;inner.rotation.x=t*.7;inner.rotation.y=-t*.55;camera.position.x=mx*.34;camera.position.y=-my*.26;camera.lookAt(0,0,0);renderer.render(scene,camera)};draw()}catch(err){console.warn('Hero sculpture fallback',err)}}

  const chat=document.getElementById('chat'),launch=document.getElementById('chatLaunch');if(chat&&launch)launch.addEventListener('click',()=>{const open=!chat.classList.contains('open');chat.classList.toggle('open',open);launch.setAttribute('aria-expanded',String(open))});
})();
</script>'''
s = re.sub(r'<script>\s*\(\(\)=>\{.*?</script>', js, s, count=1, flags=re.S)

# Update the planning brief with explicit implementation overrides from the later Design 41 decisions.
brief_path = Path('design_41.md')
if brief_path.exists():
    brief = brief_path.read_text(encoding='utf-8')
    note = '''\n## Implementation overrides, current\n\nThese rules supersede older wording below where there is a conflict.\n\n- `41.html` now starts from the exact Design 10 visual and motion foundation, then applies the locked Design 41 information architecture.\n- Motion must be interpolated and smooth, never bouncy or rubber-band-like.\n- The key Design 10 behavior is proximity response: nearby components shift subtly before direct hover, then settle slowly back to zero.\n- Pointer-linked depth is desktop-only and disabled under reduced motion.\n- The hero remains one primary campaign, not an automatic carousel.\n- The locked section order remains Header → Hero → Quick Actions → Offers/Plans → Service Categories → Business & Government → PNG/National Story → Notices & News → Help/Support/Stores → Footer.\n- Design 41 may preserve the single inherited Design 10 abstract hero WebGL sculpture, but no additional WebGL scenes or Design 42-style 3D showcase systems should be added.\n- Important interactions must work with hover, focus and tap, and important content cannot be hover-only.\n\n'''
    if '## Implementation overrides, current' not in brief:
        brief = brief.replace('## Difficulty level', note + '## Difficulty level', 1)
        brief_path.write_text(brief, encoding='utf-8')

p.write_text(s, encoding='utf-8')
print('Applied Design 41 rules pass')
print('data-depth layers:', s.count('data-depth='))
print('interactive actions:', s.count('data-action='))
print('images:', s.count('<img '))
