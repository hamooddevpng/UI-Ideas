from pathlib import Path
import re

p=Path('42.html')
s=p.read_text()

# Finish the pending copy cleanup from the previous pass if it has not landed yet.
copy_repls={
"A few Telikom service ideas, shuffled each visit so there is always something useful to explore.":"Mobile, home internet, remote connectivity and support offers from Telikom.",
"Explore Telikom through real stories, people and places. Move across the cards to bring each service into focus.":"Mobile, fixed broadband, devices, business services and customer support across Papua New Guinea.",
"Move across the feed to preview what needs attention, then open the item you want.":"Service notices, customer information and public updates from Telikom.",
"Move around the hub or search for what you need.":"Customer Care 1555 · (+675) 7600 3555",
"Suggestions reshuffle on your next visit.":"Mobile · Home · Remote · Support"
}
for old,new in copy_repls.items():
    if old in s:
        s=s.replace(old,new,1)

# Use a verified, non-map PNG island aerial from NASA/Wikimedia, downloaded by the workflow.
old_story='src="assets/common/web-sourced/telikom/mt-kegum.jpg" alt="Papua New Guinea landscape"'
if old_story in s:
    s=s.replace(old_story,'src="assets/design42/louisiade-archipelago-nasa.jpg" alt="Aerial view of the Louisiade Archipelago and coral reefs in Papua New Guinea"',1)

# Avoid a map-like business thumbnail in the randomized offer pool.
s=s.replace("image:'assets/common/web-sourced/telikom/business-data.jpg',alt:'Map of Papua New Guinea',media:'business'","image:'https://images.unsplash.com/photo-1652355076566-eab4a2f9cfe1?auto=format&fit=crop&w=1200&q=82',alt:'Work scene in Papua New Guinea',media:'business'",1)

# Stronger card pop / particle layer for Offers, only if the earlier failed workflow did not land it.
if 'id="offerPopLayer"' not in s:
    anchor='<div class="offer-card-grid" id="personalOfferGrid">'
    if anchor not in s: raise SystemExit('offer grid anchor missing')
    s=s.replace(anchor,'<div class="offer-pop-layer" id="offerPopLayer" aria-hidden="true"></div>'+anchor,1)

business_html=r'''<section class="business business-dual" id="business" data-focus="business">
  <div class="shell business-dual-shell">
    <div class="business-dual-head reveal">
      <div><div class="kicker">Business &amp; Government</div><h2 class="title">One network.<br>Two missions.</h2></div>
      <p class="lead">Secure data, voice, collaboration, hosting and remote connectivity for organisations across Papua New Guinea.</p>
    </div>

    <div class="business-dual-stage" id="businessDualStage">
      <article class="dual-world business-world active" data-dual-world="business" tabindex="0" aria-label="Business connectivity">
        <div class="dual-world-top"><span>01 / BUSINESS</span><b>ENTERPRISE NETWORK</b></div>
        <div class="dual-art-wrap">
          <svg class="dual-art business-campus" viewBox="0 0 560 320" role="img" aria-label="Connected corporate buildings">
            <defs>
              <linearGradient id="bizGlass" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#9ce9ff" stop-opacity=".9"/><stop offset=".45" stop-color="#2d8eba" stop-opacity=".55"/><stop offset="1" stop-color="#092b3c" stop-opacity=".95"/></linearGradient>
              <linearGradient id="bizSteel" x1="0" x2="1"><stop offset="0" stop-color="#d9f5ff"/><stop offset="1" stop-color="#4f8398"/></linearGradient>
              <filter id="bizGlow"><feGaussianBlur stdDeviation="4" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
            </defs>
            <ellipse class="dual-ground" cx="280" cy="282" rx="245" ry="25"/>
            <g class="campus-building branch-a">
              <path d="M58 262V157L112 126l58 24v112z" fill="url(#bizGlass)" stroke="#7edcff" stroke-opacity=".4"/>
              <path d="M58 157l54-31 58 24-53 29z" fill="#b8edff" fill-opacity=".18"/>
              <g class="building-windows" fill="#bdefff"><rect x="76" y="174" width="18" height="8"/><rect x="105" y="166" width="18" height="8"/><rect x="134" y="174" width="18" height="8"/><rect x="76" y="198" width="18" height="8"/><rect x="105" y="190" width="18" height="8"/><rect x="134" y="198" width="18" height="8"/><rect x="76" y="222" width="18" height="8"/><rect x="105" y="214" width="18" height="8"/><rect x="134" y="222" width="18" height="8"/></g>
            </g>
            <g class="campus-building hq">
              <path d="M194 265V89l77-39 83 32v183z" fill="url(#bizGlass)" stroke="#9be7ff" stroke-opacity=".52"/>
              <path d="M194 89l77-39 83 32-76 44z" fill="#d7f7ff" fill-opacity=".2"/>
              <g class="building-windows" fill="#d9f8ff"><rect x="217" y="112" width="20" height="8"/><rect x="250" y="99" width="20" height="8"/><rect x="285" y="108" width="20" height="8"/><rect x="318" y="120" width="20" height="8"/><rect x="217" y="143" width="20" height="8"/><rect x="250" y="132" width="20" height="8"/><rect x="285" y="141" width="20" height="8"/><rect x="318" y="152" width="20" height="8"/><rect x="217" y="175" width="20" height="8"/><rect x="250" y="164" width="20" height="8"/><rect x="285" y="173" width="20" height="8"/><rect x="318" y="184" width="20" height="8"/><rect x="217" y="207" width="20" height="8"/><rect x="250" y="196" width="20" height="8"/><rect x="285" y="205" width="20" height="8"/><rect x="318" y="216" width="20" height="8"/></g>
              <path d="M272 50v-23" stroke="url(#bizSteel)" stroke-width="5" stroke-linecap="round"/><circle cx="272" cy="23" r="5" fill="#bdf3ff" filter="url(#bizGlow)"/>
              <path class="signal-arc" d="M248 26Q272 4 296 26"/><path class="signal-arc delay" d="M235 18Q272-14 309 18"/>
            </g>
            <g class="campus-building data-centre">
              <path d="M390 266V174l99-19 35 21v90z" fill="url(#bizGlass)" stroke="#72d6ff" stroke-opacity=".38"/>
              <path d="M390 174l99-19 35 21-99 23z" fill="#bcefff" fill-opacity=".14"/>
              <g class="server-lights" fill="#8ce4ff"><circle cx="421" cy="211" r="4"/><circle cx="447" cy="205" r="4"/><circle cx="473" cy="200" r="4"/><circle cx="499" cy="195" r="4"/><circle cx="421" cy="236" r="4"/><circle cx="447" cy="230" r="4"/><circle cx="473" cy="225" r="4"/><circle cx="499" cy="220" r="4"/></g>
            </g>
            <path id="corpLink1" class="dual-link" d="M143 148 C205 103 225 108 272 112"/>
            <path id="corpLink2" class="dual-link" d="M319 127 C374 126 404 150 440 176"/>
            <path id="corpLink3" class="dual-link faint" d="M125 228 C230 285 370 284 454 235"/>
            <circle class="dual-packet" r="5"><animateMotion dur="2.6s" repeatCount="indefinite"><mpath href="#corpLink1"/></animateMotion></circle>
            <circle class="dual-packet secondary" r="3"><animateMotion begin=".7s" dur="2.6s" repeatCount="indefinite"><mpath href="#corpLink2"/></animateMotion></circle>
            <circle class="dual-packet mini" r="3"><animateMotion begin="1.1s" dur="3.4s" repeatCount="indefinite"><mpath href="#corpLink3"/></animateMotion></circle>
            <g class="core-node" transform="translate(272 112)"><circle r="18"/><circle r="6"/></g>
          </svg>
        </div>
        <div class="dual-world-copy"><small>IP VPN · MPLS · SIP · BUSINESS SYSTEMS</small><h3>Your offices.<br>One network.</h3><p>Managed connectivity, secure private networks, collaboration and voice systems for organisations of every size.</p><div class="dual-stats"><span><b>99%</b><small>IP VLAN availability</small></span><span><b>900 Mbps</b><small>MPLS bandwidth up to</small></span><span><b>100K+</b><small>MX-ONE users supported</small></span></div></div>
      </article>

      <article class="dual-world government-world" data-dual-world="government" tabindex="0" aria-label="Government and public service connectivity">
        <div class="dual-world-top"><span>02 / GOVERNMENT</span><b>PUBLIC CONNECTION</b></div>
        <div class="dual-art-wrap">
          <svg class="dual-art civic-network" viewBox="0 0 560 320" role="img" aria-label="Government building connecting to people">
            <defs><linearGradient id="govStone" x1="0" x2="1"><stop offset="0" stop-color="#b9f3dc" stop-opacity=".92"/><stop offset=".5" stop-color="#3c9c85" stop-opacity=".58"/><stop offset="1" stop-color="#082e34" stop-opacity=".96"/></linearGradient><filter id="govGlow"><feGaussianBlur stdDeviation="4" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs>
            <ellipse class="dual-ground" cx="280" cy="282" rx="245" ry="25"/>
            <g class="civic-building">
              <path d="M176 255V166h208v89z" fill="url(#govStone)" stroke="#a6f2dc" stroke-opacity=".42"/>
              <path d="M160 166l120-78 120 78z" fill="#83d8bd" fill-opacity=".28" stroke="#a6f2dc" stroke-opacity=".48"/>
              <path d="M280 88v-28" stroke="#c8ffed" stroke-width="5"/><circle cx="280" cy="56" r="6" fill="#c8ffed" filter="url(#govGlow)"/>
              <g class="civic-columns" fill="#c5f4e6" fill-opacity=".58"><rect x="198" y="178" width="14" height="62" rx="4"/><rect x="236" y="178" width="14" height="62" rx="4"/><rect x="274" y="178" width="14" height="62" rx="4"/><rect x="312" y="178" width="14" height="62" rx="4"/><rect x="350" y="178" width="14" height="62" rx="4"/></g>
              <path class="signal-arc gov" d="M252 56Q280 27 308 56"/><path class="signal-arc gov delay" d="M235 49Q280 5 325 49"/>
            </g>
            <path id="govLink1" class="dual-link gov-link" d="M225 190 C172 170 131 150 88 127"/>
            <path id="govLink2" class="dual-link gov-link" d="M335 190 C405 165 438 144 482 117"/>
            <path id="govLink3" class="dual-link gov-link faint" d="M280 210 C272 245 245 260 205 274"/>
            <path id="govLink4" class="dual-link gov-link faint" d="M310 212 C340 246 375 260 418 273"/>
            <circle class="dual-packet gov-packet" r="5"><animateMotion dur="2.8s" repeatCount="indefinite"><mpath href="#govLink1"/></animateMotion></circle>
            <circle class="dual-packet gov-packet secondary" r="4"><animateMotion begin=".65s" dur="2.8s" repeatCount="indefinite"><mpath href="#govLink2"/></animateMotion></circle>
            <circle class="dual-packet gov-packet mini" r="3"><animateMotion begin="1.1s" dur="3.1s" repeatCount="indefinite"><mpath href="#govLink3"/></animateMotion></circle>
            <circle class="dual-packet gov-packet mini" r="3"><animateMotion begin="1.5s" dur="3.1s" repeatCount="indefinite"><mpath href="#govLink4"/></animateMotion></circle>
            <g class="people-cluster pc1" transform="translate(82 112)"><circle cx="0" cy="0" r="10"/><path d="M-17 30Q0 9 17 30"/><circle cx="-23" cy="10" r="7"/><path d="M-35 31Q-23 17-12 31"/><circle cx="23" cy="10" r="7"/><path d="M12 31Q23 17 35 31"/></g>
            <g class="people-cluster pc2" transform="translate(483 102)"><circle cx="0" cy="0" r="10"/><path d="M-17 30Q0 9 17 30"/><circle cx="-23" cy="10" r="7"/><path d="M-35 31Q-23 17-12 31"/><circle cx="23" cy="10" r="7"/><path d="M12 31Q23 17 35 31"/></g>
            <g class="people-cluster pc3" transform="translate(195 265)"><circle cx="0" cy="0" r="8"/><path d="M-14 25Q0 8 14 25"/></g>
            <g class="people-cluster pc4" transform="translate(425 265)"><circle cx="0" cy="0" r="8"/><path d="M-14 25Q0 8 14 25"/></g>
            <g class="core-node gov-core" transform="translate(280 190)"><circle r="18"/><circle r="6"/></g>
          </svg>
        </div>
        <div class="dual-world-copy"><small>DATA · VSAT · VOICE · HOSTING · CO-LOCATION</small><h3>Public services.<br>Closer to people.</h3><p>Enterprise-grade connectivity can link offices, remote sites and citizen-facing services through one Telikom portfolio.</p><div class="dual-stats government-stats"><span><b>VSAT</b><small>Remote connectivity</small></span><span><b>Secure</b><small>Co-location &amp; backup</small></span><span><b>Voice + Data</b><small>Integrated communications</small></span></div></div>
      </article>
      <div class="dual-spine" aria-hidden="true"><span></span><i></i><b>T</b></div>
    </div>

    <div class="business-portfolio reveal" id="businessPortfolio">
      <div class="portfolio-detail"><small>BUSINESS PORTFOLIO</small><b id="portfolioTitle">Business Data</b><span id="portfolioDetail">IP VPN · MPLS up to 900 Mbps · managed network · 99% IP VLAN availability</span></div>
      <div class="portfolio-strip" role="tablist" aria-label="Telikom business services">
        <button class="portfolio-chip active" type="button" data-portfolio="0" data-side="business"><b>Business Data</b><small>IP VPN · MPLS</small></button>
        <button class="portfolio-chip" type="button" data-portfolio="1" data-side="business"><b>Business Systems</b><small>MiVoice · MiCollab</small></button>
        <button class="portfolio-chip" type="button" data-portfolio="2" data-side="business"><b>SIP Trunk</b><small>Voice over IP</small></button>
        <button class="portfolio-chip" type="button" data-portfolio="3" data-side="government"><b>Co-Location</b><small>Secure infrastructure</small></button>
        <button class="portfolio-chip" type="button" data-portfolio="4" data-side="government"><b>VSAT</b><small>Remote sites</small></button>
        <button class="portfolio-chip" type="button" data-portfolio="5" data-side="business"><b>Web &amp; Hosting</b><small>Hosting · email · backup</small></button>
        <button class="portfolio-chip" type="button" data-portfolio="6" data-side="business"><b>CUG / PUG</b><small>Business mobile groups</small></button>
      </div>
    </div>
  </div>
</section>'''

pat=re.compile(r'<section class="business business-command" id="business">.*?</section>\s*(?=<section class="png-story)',re.S)
if not pat.search(s):
    raise SystemExit('old business section not found')
s=pat.sub(business_html+'\n',s,count=1)

css=r'''
/* Design 42: premium Business + Government dual world */
.business-dual{position:relative;padding:34px 0 28px!important;background:radial-gradient(circle at 50% 48%,rgba(32,167,218,.09),transparent 32%),linear-gradient(135deg,#031720 0%,#072a39 48%,#062c2c 100%);color:#fff;overflow:hidden;isolation:isolate}
.business-dual:before{content:"";position:absolute;inset:0;background-image:linear-gradient(rgba(126,219,255,.035) 1px,transparent 1px),linear-gradient(90deg,rgba(126,219,255,.035) 1px,transparent 1px);background-size:46px 46px;mask-image:radial-gradient(ellipse at 50% 45%,#000 15%,transparent 78%);pointer-events:none}
.business-dual-shell{position:relative;z-index:2;height:min(78vh,720px);min-height:650px;display:grid;grid-template-rows:auto minmax(0,1fr) auto;gap:18px}
.business-dual-head{display:grid;grid-template-columns:1fr .72fr;align-items:end;gap:42px}.business-dual-head .kicker{color:#8edbff}.business-dual-head .title{font-size:clamp(42px,4.9vw,68px);line-height:.88;margin-top:9px}.business-dual-head .lead{justify-self:end;color:#a8c1cc;max-width:500px;font-size:12px;line-height:1.65;margin:0}
.business-dual-stage{position:relative;display:flex;gap:14px;min-height:0;perspective:1300px}.dual-world{--wrx:0deg;--wry:0deg;position:relative;flex:1;min-width:0;border:1px solid rgba(160,226,255,.14);border-radius:30px;overflow:hidden;background:linear-gradient(150deg,rgba(11,53,72,.92),rgba(3,25,36,.96));box-shadow:0 24px 62px rgba(0,0,0,.24),inset 0 1px rgba(255,255,255,.035);transform:perspective(1100px) rotateX(var(--wrx)) rotateY(var(--wry));transform-style:preserve-3d;transition:flex .65s var(--spring),opacity .45s,border-color .45s,box-shadow .45s,transform .18s ease-out;outline:none}
.government-world{background:linear-gradient(150deg,rgba(10,59,58,.94),rgba(2,30,34,.97));border-color:rgba(157,244,216,.13)}
.business-dual[data-focus="business"] .business-world,.business-dual[data-focus="government"] .government-world{flex:1.08;border-color:rgba(139,226,255,.36);box-shadow:0 32px 84px rgba(0,0,0,.31),0 0 54px rgba(39,169,225,.075),inset 0 1px rgba(255,255,255,.05)}
.business-dual[data-focus="government"] .government-world{border-color:rgba(155,241,214,.35);box-shadow:0 32px 84px rgba(0,0,0,.31),0 0 54px rgba(80,196,157,.075),inset 0 1px rgba(255,255,255,.05)}
.business-dual[data-focus="business"] .government-world,.business-dual[data-focus="government"] .business-world{flex:.92;opacity:.72}
.dual-world-top{position:absolute;z-index:5;left:18px;right:18px;top:15px;display:flex;justify-content:space-between;align-items:center;font-size:6.5px;font-weight:800;letter-spacing:.14em;color:#7fa4b5}.business-world .dual-world-top b{color:#84ddff}.government-world .dual-world-top b{color:#9beacb}.dual-art-wrap{position:absolute;inset:29px 6px 105px;display:grid;place-items:center;transform:translateZ(24px)}.dual-art{width:100%;height:100%;overflow:visible}.dual-ground{fill:rgba(100,204,243,.055)}.government-world .dual-ground{fill:rgba(111,226,188,.05)}
.building-windows>*{opacity:.42;animation:buildingBlink 3.2s ease-in-out infinite alternate}.building-windows>*:nth-child(3n){animation-delay:.8s}.building-windows>*:nth-child(4n){animation-delay:1.5s}.server-lights>*{animation:serverBlink 1.4s ease-in-out infinite alternate}.server-lights>*:nth-child(2n){animation-delay:.45s}@keyframes buildingBlink{to{opacity:.96;filter:drop-shadow(0 0 6px #9feaff)}}@keyframes serverBlink{to{opacity:.25}}
.signal-arc{fill:none;stroke:#a9efff;stroke-width:2;stroke-linecap:round;stroke-dasharray:5 6;opacity:.28;animation:signalArc 2.1s ease-in-out infinite alternate}.signal-arc.delay{animation-delay:.55s}.signal-arc.gov{stroke:#b0f5da}@keyframes signalArc{to{opacity:.9;stroke-dashoffset:-18}}
.dual-link{fill:none;stroke:#71d6ff;stroke-width:2.2;stroke-linecap:round;stroke-dasharray:8 10;opacity:.46;filter:drop-shadow(0 0 5px rgba(91,210,255,.58));animation:dualRoute 1.55s linear infinite}.dual-link.faint{opacity:.18}.dual-link.gov-link{stroke:#8fe7c8;filter:drop-shadow(0 0 5px rgba(111,222,185,.55))}@keyframes dualRoute{to{stroke-dashoffset:-36}}.dual-packet{fill:#eaffff;filter:drop-shadow(0 0 8px #65d9ff)}.dual-packet.secondary{fill:#71d6ff}.dual-packet.mini{opacity:.68}.dual-packet.gov-packet{fill:#dcfff2;filter:drop-shadow(0 0 8px #70dfbb)}
.core-node>circle:first-child{fill:rgba(67,188,235,.12);stroke:#88e3ff;stroke-width:1.5;animation:corePulse 1.8s ease-out infinite}.core-node>circle:last-child{fill:#dff9ff;filter:drop-shadow(0 0 9px #72dcff)}.gov-core>circle:first-child{stroke:#9befd1;fill:rgba(84,198,159,.11)}.gov-core>circle:last-child{fill:#e1fff4;filter:drop-shadow(0 0 9px #83e9c5)}@keyframes corePulse{70%,100%{r:27;opacity:0}}
.people-cluster{fill:#b9f2df;stroke:#b9f2df;stroke-width:2;opacity:.58;animation:peopleGlow 2.7s ease-in-out infinite alternate}.pc2{animation-delay:.6s}.pc3{animation-delay:1.1s}.pc4{animation-delay:1.6s}@keyframes peopleGlow{to{opacity:1;filter:drop-shadow(0 0 8px rgba(130,234,198,.55))}}
.dual-world-copy{position:absolute;z-index:5;left:20px;right:20px;bottom:16px;transform:translateZ(38px)}.dual-world-copy>small{display:block;font-size:6px;letter-spacing:.13em;color:#79bad7;font-weight:800}.government-world .dual-world-copy>small{color:#7ecab1}.dual-world-copy h3{font-family:"Space Grotesk";font-size:clamp(24px,2.45vw,36px);line-height:.92;letter-spacing:-.045em;margin:6px 0 5px}.dual-world-copy>p{font-size:8.5px;line-height:1.45;color:#91adba;max-width:390px;margin:0}.government-world .dual-world-copy>p{color:#92b7ac}.dual-stats{position:absolute;right:0;bottom:0;display:flex;gap:7px}.dual-stats span{width:88px;padding:8px 9px;border:1px solid rgba(141,221,255,.12);border-radius:12px;background:rgba(255,255,255,.035);backdrop-filter:blur(10px)}.dual-stats b{display:block;font-family:"Space Grotesk";font-size:11px;color:#dff8ff}.dual-stats small{display:block;font-size:5px;line-height:1.25;color:#7599a9;margin-top:2px}.government-stats span{border-color:rgba(145,236,204,.12)}.government-stats b{color:#dffff3}.government-stats small{color:#769e91}
.dual-spine{position:absolute;z-index:8;left:50%;top:12%;bottom:12%;width:1px;background:linear-gradient(transparent,rgba(132,226,255,.28) 16%,rgba(132,226,255,.3) 84%,transparent);pointer-events:none}.dual-spine span{position:absolute;left:50%;top:0;width:1px;height:31%;background:linear-gradient(transparent,#b9f2ff,transparent);transform:translateX(-50%);animation:spineTravel 2.8s ease-in-out infinite}.dual-spine i{position:absolute;left:50%;top:50%;width:28px;height:28px;border:1px solid rgba(146,232,255,.32);border-radius:50%;transform:translate(-50%,-50%);box-shadow:0 0 0 10px rgba(95,208,247,.025),0 0 25px rgba(95,208,247,.14)}.dual-spine b{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);width:18px;height:18px;border-radius:50%;display:grid;place-items:center;background:#dff9ff;color:#063044;font-size:8px}@keyframes spineTravel{0%{top:-10%;opacity:0}20%{opacity:1}80%{opacity:.9}100%{top:78%;opacity:0}}
.business-portfolio{display:grid;grid-template-columns:250px 1fr;gap:16px;align-items:stretch;min-height:76px}.portfolio-detail{padding:12px 15px;border:1px solid rgba(155,224,255,.12);border-radius:19px;background:rgba(255,255,255,.035);display:flex;flex-direction:column;justify-content:center}.portfolio-detail small{font-size:6px;letter-spacing:.14em;color:#7297a7;font-weight:800}.portfolio-detail b{font-family:"Space Grotesk";font-size:14px;margin:3px 0;color:#e8faff}.portfolio-detail span{font-size:6.5px;line-height:1.35;color:#8faab6}.portfolio-strip{display:grid;grid-template-columns:repeat(7,1fr);gap:6px;min-width:0}.portfolio-chip{position:relative;border:1px solid rgba(255,255,255,.09);border-radius:17px;background:rgba(255,255,255,.025);color:#bdd0d8;padding:8px 8px;text-align:left;cursor:pointer;overflow:hidden;transition:.28s var(--spring)}.portfolio-chip:before{content:"";position:absolute;inset:0;background:linear-gradient(135deg,rgba(31,166,225,.16),transparent 60%);opacity:0;transition:.28s}.portfolio-chip>*{position:relative}.portfolio-chip b{display:block;font-size:7.4px}.portfolio-chip small{display:block;font-size:5.4px;color:#6f909d;margin-top:3px}.portfolio-chip:hover,.portfolio-chip:focus-visible,.portfolio-chip.active{transform:translateY(-4px);border-color:rgba(123,218,255,.3);color:#fff;outline:none}.portfolio-chip:hover:before,.portfolio-chip:focus-visible:before,.portfolio-chip.active:before{opacity:1}.portfolio-chip.active small{color:#92cce4}.business-dual.portfolio-flash .dual-world.active{animation:portfolioFlash .46s var(--spring)}@keyframes portfolioFlash{50%{filter:brightness(1.15);transform:perspective(1100px) translateY(-3px)}}
@media(max-height:780px) and (min-width:821px){.business-dual{padding-top:24px!important;padding-bottom:22px!important}.business-dual-shell{height:78vh;min-height:600px}.business-dual-head .title{font-size:clamp(38px,4.2vw,58px)}.dual-world-copy h3{font-size:clamp(22px,2.1vw,30px)}.dual-world-copy>p{display:none}.dual-art-wrap{bottom:90px}.business-portfolio{min-height:68px}}
@media(max-width:1080px){.business-dual-head{grid-template-columns:1fr .8fr}.dual-stats span{width:74px;padding:7px}.dual-stats small{display:none}.portfolio-strip{grid-template-columns:repeat(4,1fr);grid-auto-rows:1fr}.business-portfolio{min-height:104px}.business-dual-shell{min-height:690px}}
@media(max-width:820px){.business-dual{padding:64px 0!important;max-height:none}.business-dual-shell{height:auto;min-height:0;display:block}.business-dual-head{grid-template-columns:1fr;gap:18px}.business-dual-head .lead{justify-self:start}.business-dual-stage{display:block;margin-top:28px}.dual-world{height:520px;margin-bottom:14px;transform:none!important;opacity:1!important}.business-dual[data-focus] .dual-world{flex:1}.dual-spine{display:none}.dual-stats{position:static;margin-top:12px}.dual-world-copy>p{max-width:270px}.business-portfolio{display:block;margin-top:20px}.portfolio-detail{margin-bottom:9px}.portfolio-strip{display:flex;overflow-x:auto;scroll-snap-type:x mandatory;padding-bottom:4px}.portfolio-chip{min-width:145px;scroll-snap-align:start}.dual-art-wrap{inset:32px 4px 116px}}
@media(prefers-reduced-motion:reduce){.building-windows>*,.server-lights>*,.signal-arc,.dual-link,.people-cluster,.dual-spine span,.core-node>circle:first-child{animation:none!important}.dual-world{transform:none!important}}

/* Design 42: cleaner copy + stronger offer pop */
.png-live .png-story-photo{object-position:center 48%;filter:saturate(.94) contrast(1.08) brightness(.64)}
.offer-loading-stage{position:relative;isolation:isolate}.offer-pop-layer{position:absolute;inset:0;z-index:30;pointer-events:none;overflow:hidden;border-radius:30px}.offer-pop-particle{position:absolute;width:var(--ps,5px);height:var(--ps,5px);left:0;top:0;border-radius:999px;background:var(--pc,#1ca0e8);box-shadow:0 0 11px color-mix(in srgb,var(--pc,#1ca0e8) 70%,transparent);will-change:transform,opacity}.offer-pop-particle.square{border-radius:2px}.offer-pop-ring{position:absolute;left:0;top:0;width:30px;height:30px;border:1px solid rgba(28,160,232,.55);border-radius:50%;box-shadow:0 0 28px rgba(28,160,232,.2);will-change:transform,opacity}#offers.offer-pop-live .personal-offer{will-change:transform,opacity,filter}#offers.offer-pop-live .personal-offer-media img{will-change:transform}@media(max-width:820px){.offer-pop-layer{border-radius:22px}}@media(prefers-reduced-motion:reduce){.offer-pop-layer{display:none}}
'''
if 'Design 42: premium Business + Government dual world' not in s:
    pos=s.rfind('</style>')
    if pos<0: raise SystemExit('style close missing')
    s=s[:pos]+css+s[pos:]

js=r'''
// Design 42: Business + Government dual world
(()=>{
  const section=document.getElementById('business'),stage=document.getElementById('businessDualStage');
  if(!section||!stage)return;
  const worlds=[...section.querySelectorAll('[data-dual-world]')],chips=[...section.querySelectorAll('[data-portfolio]')],title=document.getElementById('portfolioTitle'),detail=document.getElementById('portfolioDetail');
  const portfolio=[
    ['Business Data','IP VPN · MPLS up to 900 Mbps · managed network · 99% IP VLAN availability'],
    ['Business Systems','MiVoice Business · MX-ONE · MiCollab · customer experience solutions'],
    ['SIP Trunk','Voice over your data network · use an existing IP PABX · business voice bundles'],
    ['Co-Location','Secure exchange, tower and IT space · backed-up service · outage protection'],
    ['Telikom VSAT','Remote telecommunications connectivity for business, organisations and communities'],
    ['Web & Hosting','Website hosting · business email · file and server backup services'],
    ['CUG / PUG','Telikom 4G SIM · unlimited calls and SMS within the business user group']
  ];
  const setFocus=side=>{section.dataset.focus=side;worlds.forEach(w=>w.classList.toggle('active',w.dataset.dualWorld===side))};
  worlds.forEach(world=>{
    world.addEventListener('pointerenter',e=>{if(e.pointerType!=='touch')setFocus(world.dataset.dualWorld)});
    world.addEventListener('focus',()=>setFocus(world.dataset.dualWorld));
    world.addEventListener('pointermove',e=>{if(e.pointerType==='touch')return;const r=world.getBoundingClientRect(),x=(e.clientX-r.left)/r.width-.5,y=(e.clientY-r.top)/r.height-.5;world.style.setProperty('--wry',(x*3.8).toFixed(2)+'deg');world.style.setProperty('--wrx',(y*-3.1).toFixed(2)+'deg')},{passive:true});
    world.addEventListener('pointerleave',()=>{world.style.setProperty('--wry','0deg');world.style.setProperty('--wrx','0deg')});
  });
  chips.forEach((chip,i)=>{
    const activate=()=>{chips.forEach((c,n)=>c.classList.toggle('active',n===i));title.textContent=portfolio[i][0];detail.textContent=portfolio[i][1];setFocus(chip.dataset.side||'business');section.classList.remove('portfolio-flash');void section.offsetWidth;section.classList.add('portfolio-flash');setTimeout(()=>section.classList.remove('portfolio-flash'),500)};
    chip.addEventListener('pointerenter',e=>{if(e.pointerType!=='touch')activate()});chip.addEventListener('focus',activate);chip.addEventListener('click',activate)
  });
  new IntersectionObserver(([entry])=>{section.classList.toggle('business-dual-live',entry.isIntersecting)},{threshold:.12}).observe(section);
})();

// Design 42: offer cards pop with particles after the two-second loader
(()=>{
  const section=document.getElementById('offers'),stage=document.getElementById('offerLoadingStage'),layer=document.getElementById('offerPopLayer'),loader=document.getElementById('offerLoader'),cards=[...document.querySelectorAll('#personalOfferGrid .personal-offer')];
  if(!section||!stage||!layer||!cards.length)return;
  const reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;let armed=false,popped=false;const colors=['#1ca0e8','#0875c9','#20a957','#9ce8ff','#ffffff'];
  function burst(card,index){if(reduce)return;const sr=stage.getBoundingClientRect(),cr=card.getBoundingClientRect(),x=cr.left-sr.left+cr.width/2,y=cr.top-sr.top+cr.height*.46;const ring=document.createElement('i');ring.className='offer-pop-ring';ring.style.left=x+'px';ring.style.top=y+'px';layer.appendChild(ring);const ra=ring.animate([{transform:'translate(-50%,-50%) scale(.1)',opacity:.9},{transform:'translate(-50%,-50%) scale(5)',opacity:0}],{duration:780,easing:'cubic-bezier(.16,1,.3,1)'});ra.onfinish=()=>ring.remove();const count=innerWidth<820?12:22;for(let j=0;j<count;j++){const q=document.createElement('i');q.className='offer-pop-particle'+(j%4===0?' square':'');const a=Math.PI*2*j/count+(Math.random()-.5)*.42,d=38+Math.random()*(innerWidth<820?55:105),dx=Math.cos(a)*d,dy=Math.sin(a)*d-(10+Math.random()*28),sz=2.4+Math.random()*5;q.style.left=x+'px';q.style.top=y+'px';q.style.setProperty('--ps',sz+'px');q.style.setProperty('--pc',colors[(j+index)%colors.length]);layer.appendChild(q);const qa=q.animate([{transform:'translate(-50%,-50%) scale(.1)',opacity:0},{offset:.14,transform:'translate(-50%,-50%) scale(1.15)',opacity:1},{transform:`translate(calc(-50% + ${dx}px),calc(-50% + ${dy}px)) scale(.18) rotate(${120+Math.random()*260}deg)`,opacity:0}],{duration:680+Math.random()*300,delay:Math.random()*60,easing:'cubic-bezier(.17,.67,.25,1)'});qa.onfinish=()=>q.remove()}}
  function pop(){if(popped)return;popped=true;section.classList.add('offer-pop-live');cards.forEach((card,i)=>setTimeout(()=>{const dir=i===0?-1:i===2?1:0;const ca=card.animate([{transform:`translate3d(${dir*48}px,82px,0) scale(.05) rotate(${dir*-9}deg)`,opacity:0,filter:'blur(10px)'},{offset:.46,transform:`translate3d(${dir*10}px,-24px,0) scale(1.12) rotate(${dir*1.7}deg)`,opacity:1,filter:'blur(0)'},{offset:.72,transform:'translate3d(0,9px,0) scale(.965)',opacity:1,filter:'blur(0)'},{transform:'translate3d(0,0,0) scale(1)',opacity:1,filter:'blur(0)'}],{duration:1240,easing:'cubic-bezier(.16,1,.3,1)',fill:'both'});burst(card,i);ca.finished.then(()=>ca.cancel()).catch(()=>{})},i*260))}
  function wait(){const t=performance.now();const tick=()=>{const loading=section.classList.contains('offers-loading'),loaded=section.classList.contains('offers-loaded'),lop=loader?parseFloat(getComputedStyle(loader).opacity||'1'):0;if((loaded&&!loading)||lop<.25||performance.now()-t>3200)pop();else setTimeout(tick,70)};tick()}
  function arm(){if(armed||scrollY<=1)return;const r=section.getBoundingClientRect();if(r.top<innerHeight*.86&&r.bottom>innerHeight*.12){armed=true;wait()}}
  addEventListener('scroll',arm,{passive:true});new IntersectionObserver(()=>arm(),{threshold:.16}).observe(section)
})();
'''
if 'Design 42: Business + Government dual world' not in s:
    pos=s.rfind('</script>')
    if pos<0: raise SystemExit('script close missing')
    s=s[:pos]+js+s[pos:]

p.write_text(s)
