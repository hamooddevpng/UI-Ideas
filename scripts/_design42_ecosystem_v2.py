from pathlib import Path

path = Path('42.html')
text = path.read_text(encoding='utf-8')
original = text

if 'digital-ecosystem-board' not in text:
    raise SystemExit('Digital ecosystem not found')
if 'Design 42 ecosystem iteration 2' in text:
    raise SystemExit('Iteration 2 already present')

hero_start = original.index('<section class="hero"')
hero_end = original.index('</section>', hero_start) + len('</section>')
hero_before = original[hero_start:hero_end]
services_start = original.index('<section class="services service-stories"')
services_end = original.index('</section>', services_start) + len('</section>')
services_before = original[services_start:services_end]

replacements = {
    'd="M206 302C282 287 340 248 432 221"': 'd="M206 302C286 292 352 260 438 229"',
    'd="M216 160C288 155 357 171 434 200"': 'd="M216 160C292 157 356 169 439 193"',
    'd="M500 204C582 186 644 167 716 170"': 'd="M500 189C579 178 643 164 716 170"',
    'd="M663 319C591 317 528 289 471 257C544 280 650 318 833 319"': 'd="M663 319C596 317 532 292 474 257C548 310 676 337 833 319"',
    '<circle cx="98" cy="14" r="5" fill="#20a957" opacity=".88"/>': '<circle cx="98" cy="14" r="11" class="eco-hub-ring"/><circle cx="98" cy="14" r="5" class="eco-hub-light"/>'
}
for old, new in replacements.items():
    if old not in text:
        raise SystemExit('Expected ecosystem marker missing: ' + old[:70])
    text = text.replace(old, new, 1)

packet_anchor = '''            <circle r="4" class="eco-data-dot"><animateMotion dur="3.8s" repeatCount="indefinite"><mpath href="#ecoNetworkRoute"/></animateMotion></circle>
            <circle r="3" class="eco-data-dot" opacity=".7"><animateMotion dur="3.8s" begin="1.25s" repeatCount="indefinite"><mpath href="#ecoNetworkRoute"/></animateMotion></circle>
            <circle r="4" class="eco-compute-dot"><animateMotion dur="3.3s" repeatCount="indefinite"><mpath href="#ecoComputeRoute"/></animateMotion></circle>
            <circle r="3" class="eco-compute-dot" opacity=".72"><animateMotion dur="3.3s" begin="1.1s" repeatCount="indefinite"><mpath href="#ecoComputeRoute"/></animateMotion></circle>
            <g class="eco-kina-token"><circle r="10"/><text y=".5">K</text><animateMotion dur="4.6s" repeatCount="indefinite"><mpath href="#ecoCashRoute"/></animateMotion></g>'''
packet_new = '''            <circle r="4" class="eco-data-dot"><animateMotion dur="3.45s" repeatCount="indefinite"><mpath href="#ecoNetworkRoute"/></animateMotion></circle>
            <circle r="3" class="eco-data-dot" opacity=".72"><animateMotion dur="3.45s" begin="1.05s" repeatCount="indefinite"><mpath href="#ecoNetworkRoute"/></animateMotion></circle>
            <circle r="2.5" class="eco-data-dot" opacity=".58"><animateMotion dur="3.45s" begin="2.05s" repeatCount="indefinite"><mpath href="#ecoNetworkRoute"/></animateMotion></circle>
            <circle r="3.4" class="eco-starlink-dot"><animateMotion dur="4.2s" repeatCount="indefinite"><mpath href="#ecoStarlinkRoute"/></animateMotion></circle>
            <circle r="2.6" class="eco-starlink-dot" opacity=".62"><animateMotion dur="4.2s" begin="1.65s" repeatCount="indefinite"><mpath href="#ecoStarlinkRoute"/></animateMotion></circle>
            <circle r="4" class="eco-compute-dot"><animateMotion dur="3.05s" repeatCount="indefinite"><mpath href="#ecoComputeRoute"/></animateMotion></circle>
            <circle r="3" class="eco-compute-dot" opacity=".72"><animateMotion dur="3.05s" begin="1.02s" repeatCount="indefinite"><mpath href="#ecoComputeRoute"/></animateMotion></circle>
            <circle r="2.5" class="eco-compute-dot" opacity=".54"><animateMotion dur="3.05s" begin="2.02s" repeatCount="indefinite"><mpath href="#ecoComputeRoute"/></animateMotion></circle>
            <g class="eco-kina-token"><circle r="10"/><text y=".5">K</text><animateMotion dur="4.25s" repeatCount="indefinite"><mpath href="#ecoCashRoute"/></animateMotion></g>'''
if packet_anchor not in text:
    raise SystemExit('Packet animation block not found')
text = text.replace(packet_anchor, packet_new, 1)

insight_anchor = '''      <div class="eco-insight" id="ecoInsight" aria-live="polite">'''
overlay = '''      <aside class="eco-story-overlay" id="ecoStoryOverlay" aria-live="polite" aria-hidden="true">
        <div class="eco-story-top"><span id="ecoStoryLabel">STORY MOCK</span><button type="button" id="ecoStoryClose" aria-label="Close story">×</button></div>
        <small id="ecoStoryPath">CITY → TELIKOM</small>
        <h3 id="ecoStoryTitle">The city comes online.</h3>
        <p id="ecoStoryBody">A short story view will live here, showing how this part of the ecosystem connects into the wider Telikom network.</p>
        <div class="eco-story-steps" id="ecoStorySteps"><span>01 · ORIGIN</span><span>02 · TELIKOM</span><span>03 · DESTINATION</span></div>
        <a id="ecoStoryLink" href="#services">Read full story ↗</a>
      </aside>

'''
if insight_anchor not in text:
    raise SystemExit('Insight tray anchor not found')
text = text.replace(insight_anchor, overlay + insight_anchor, 1)

css = r'''

/* Design 42 ecosystem iteration 2: live routes + story overlays. */
.eco-route{stroke-dasharray:2 9;animation:ecoRouteFlow 3.6s linear infinite;will-change:stroke-dashoffset}
.route-starlink{stroke-dasharray:8 11;animation-duration:4.2s}
.route-compute{stroke-dasharray:5 9;animation-duration:2.85s}
.route-tcash{stroke-dasharray:3 10;animation-duration:3.15s}
.eco-board-focused .eco-route.is-active{animation-duration:1.25s}
.eco-starlink-dot{fill:#f7fdff;stroke:#58aec8;stroke-width:1.2;filter:drop-shadow(0 0 4px rgba(78,174,204,.42))}
.eco-hub-light{fill:#20a957;filter:drop-shadow(0 0 4px rgba(32,169,87,.45));animation:ecoHubLight 2.2s ease-in-out infinite}
.eco-hub-ring{fill:none;stroke:#20a957;stroke-width:1.2;opacity:.16;transform-box:fill-box;transform-origin:center;animation:ecoHubRing 2.6s ease-out infinite}
.zone-network .eco-person-head{animation:ecoPeopleLive 3.4s ease-in-out infinite}
.zone-network .eco-window{animation:ecoWindowLive 4.4s ease-in-out infinite}
.zone-network .eco-window:nth-of-type(2n){animation-delay:.8s}
.eco-phone-check{transform-box:fill-box;transform-origin:center;animation:ecoReceivePulse 4.25s ease-out infinite}
.eco-zone{cursor:pointer}
.eco-zone.is-active .eco-label{fill:#0875c9}
.eco-zone.is-active .eco-small{fill:#4f8294}

.eco-story-overlay{position:absolute;z-index:14;left:22px;bottom:104px;width:min(390px,calc(100% - 44px));padding:17px 18px 16px;border:1px solid rgba(26,111,142,.14);border-radius:18px;background:rgba(255,255,255,.95);backdrop-filter:blur(16px);box-shadow:0 22px 54px rgba(18,72,93,.16);opacity:0;visibility:hidden;pointer-events:none;transform:translateY(12px) scale(.985);transform-origin:left bottom;transition:opacity .24s var(--ease),transform .32s var(--spring),visibility .24s}
.eco-story-overlay:before{content:"";position:absolute;left:0;right:0;top:0;height:3px;border-radius:18px 18px 0 0;background:linear-gradient(90deg,#1ca0e8,#0875c9 48%,#20a957)}
.eco-story-overlay.show{opacity:1;visibility:visible;pointer-events:auto;transform:none}
.eco-story-top{display:flex;align-items:center;justify-content:space-between;gap:12px;margin-bottom:8px}.eco-story-top span{font-size:5.7px;font-weight:800;letter-spacing:.16em;color:#7b949f}.eco-story-top button{width:25px;height:25px;border:0;border-radius:50%;background:#edf7fa;color:#5e8190;display:grid;place-items:center;cursor:pointer;font-size:15px;line-height:1}.eco-story-top button:hover,.eco-story-top button:focus-visible{outline:none;background:#e1f2f7;color:#0875c9}
.eco-story-overlay>small{display:block;font-size:6.2px;font-weight:800;letter-spacing:.14em;color:#0875c9;margin-bottom:7px}.eco-story-overlay h3{font-family:"Space Grotesk",Manrope,sans-serif;font-size:22px;line-height:1.02;letter-spacing:-.035em;color:#153a4b;margin:0 0 8px}.eco-story-overlay p{font-size:9px;line-height:1.55;color:#607c89;margin:0;max-width:350px}.eco-story-steps{display:flex;flex-wrap:wrap;gap:5px;margin:13px 0 12px}.eco-story-steps span{padding:5px 7px;border-radius:999px;background:#edf7fa;color:#4d7788;font-size:5.5px;font-weight:800;letter-spacing:.08em}.eco-story-overlay>a{display:inline-flex;align-items:center;min-height:29px;padding:0 10px;border-radius:999px;background:#102f3f;color:#fff;font-size:6.5px;font-weight:800}

@keyframes ecoRouteFlow{to{stroke-dashoffset:-44}}
@keyframes ecoHubLight{0%,100%{opacity:.64}50%{opacity:1}}
@keyframes ecoHubRing{0%{opacity:.28;transform:scale(.58)}75%,100%{opacity:0;transform:scale(1.55)}}
@keyframes ecoPeopleLive{0%,100%{opacity:.72}50%{opacity:1}}
@keyframes ecoWindowLive{0%,100%{opacity:.34}45%,60%{opacity:.76}}
@keyframes ecoReceivePulse{0%,70%,100%{transform:scale(1);filter:none}82%{transform:scale(1.18);filter:drop-shadow(0 0 5px rgba(32,169,87,.35))}}
@media(max-width:820px){.eco-story-overlay{position:absolute;left:14px;right:14px;bottom:118px;width:auto;padding:15px}.eco-story-overlay h3{font-size:19px}.eco-story-overlay p{font-size:8.3px}.eco-story-steps{margin:10px 0}.eco-story-overlay>a{min-height:31px}}
@media(prefers-reduced-motion:reduce){.eco-route,.eco-starlink-dot,.eco-hub-light,.eco-hub-ring,.zone-network .eco-person-head,.zone-network .eco-window,.eco-phone-check{animation:none!important}.eco-story-overlay{transition:none!important}}
'''
style_end = text.index('\n</style>\n</head>')
text = text[:style_end] + css + text[style_end:]

script_start = text.index("<script>\n;(()=>{\n  const section=document.getElementById('digital-png-rail')")
script_end = text.index('</script>', script_start) + len('</script>')
new_script = r'''<script>
;(()=>{
  const section=document.getElementById('digital-png-rail'),board=document.getElementById('digitalEcosystemBoard'),scene=document.getElementById('ecoScene');
  if(!section||!board)return;
  const nodes=[...board.querySelectorAll('.eco-node')],routes=[...board.querySelectorAll('[data-route]')],zones=[...board.querySelectorAll('[data-zone]')];
  const eyebrow=document.getElementById('ecoInsightEyebrow'),code=document.getElementById('ecoInsightCode'),title=document.getElementById('ecoInsightTitle'),text=document.getElementById('ecoInsightText'),link=document.getElementById('ecoInsightLink');
  const overlay=document.getElementById('ecoStoryOverlay'),storyLabel=document.getElementById('ecoStoryLabel'),storyPath=document.getElementById('ecoStoryPath'),storyTitle=document.getElementById('ecoStoryTitle'),storyBody=document.getElementById('ecoStoryBody'),storySteps=document.getElementById('ecoStorySteps'),storyLink=document.getElementById('ecoStoryLink'),storyClose=document.getElementById('ecoStoryClose');
  const data={
    network:{eyebrow:'CONNECT',code:'CITY + PEOPLE',title:'Everyday traffic enters the Telikom network.',text:'People, homes and businesses send mobile and data traffic into Telikom, where it can continue toward digital services and compute.',href:'#services',routes:['network'],zones:['network','telikom'],storyPath:'PEOPLE + CITY → TELIKOM',storyTitle:'The city comes online.',storyBody:'A person sends a message, a home opens a service, or a business moves data. Those everyday journeys converge on Telikom before continuing across the wider digital ecosystem.',steps:['01 · PEOPLE CREATE TRAFFIC','02 · TELIKOM RECEIVES IT','03 · SERVICES CONTINUE']},
    starlink:{eyebrow:'CONNECT',code:'STARLINK',title:'Remote PNG connects back into the same ecosystem.',text:'A remote site can use satellite connectivity to reach Telikom services beyond the usual terrestrial network edge.',href:'#business',routes:['starlink'],zones:['starlink','telikom'],storyPath:'REMOTE PNG → STARLINK → TELIKOM',storyTitle:'A remote site joins the same network.',storyBody:'Where terrestrial coverage is difficult, a remote site can reach the network through satellite connectivity and feed into the same Telikom service layer as the city.',steps:['01 · REMOTE SITE','02 · SATELLITE LINK','03 · TELIKOM CORE']},
    telikom:{eyebrow:'CORE',code:'TELIKOM HUB',title:'Telikom is the shared digital layer.',text:'The central network hub links customer connectivity, remote access, digital transactions and sovereign compute into one ecosystem.',href:'#services',routes:['network','starlink','compute','tcash'],zones:['network','starlink','telikom','compute','tcash'],storyPath:'MANY JOURNEYS → ONE TELIKOM CORE',storyTitle:'Everything meets at Telikom.',storyBody:'City traffic, remote connectivity, transactions and compute do not need to feel like separate worlds. Telikom becomes the common digital layer where those journeys meet and continue.',steps:['01 · CONNECT','02 · ROUTE','03 · DELIVER']},
    compute:{eyebrow:'COMPUTE',code:'KUMUL CLOUD',title:'Traffic can continue into sovereign compute.',text:'Kumul Cloud represents PNG-hosted cloud and AI infrastructure for resilient workloads and modern enterprise services.',href:'#business',routes:['compute'],zones:['telikom','compute'],storyPath:'TELIKOM → KUMUL CLOUD',storyTitle:'Traffic reaches sovereign compute.',storyBody:'Once traffic reaches the Telikom core, selected workloads can continue into PNG-hosted cloud and AI infrastructure for modern enterprise and government services.',steps:['01 · TELIKOM CORE','02 · SOVEREIGN ROUTE','03 · CLOUD + AI']},
    tcash:{eyebrow:'TRANSACT',code:'T-CASH',title:'Kina moves from one user to another through Telikom.',text:'A simple value journey shows one user sending Kina through the Telikom digital layer to another user, without implying unsupported wallet features.',href:'#services',routes:['tcash'],zones:['telikom','tcash'],storyPath:'USER A → TELIKOM → USER B',storyTitle:'A Kina journey between people.',storyBody:'One user sends value into the Telikom digital layer. The transaction travels through the network and reaches another user, shown simply without inventing unsupported wallet features.',steps:['01 · USER SENDS KINA','02 · TELIKOM CARRIES IT','03 · USER RECEIVES']}
  };
  const resetCopy=()=>{eyebrow.textContent='DIGITAL PNG';code.textContent='ECOSYSTEM';title.textContent='One Telikom ecosystem.';text.textContent='Connectivity, remote access, sovereign compute and digital transactions shown as parts of one shared Telikom layer.';link.href='#services'};
  const hideStory=()=>{overlay?.classList.remove('show');overlay?.setAttribute('aria-hidden','true')};
  const clear=()=>{board.classList.remove('eco-board-focused');nodes.forEach(n=>n.classList.remove('active'));routes.forEach(r=>r.classList.remove('is-active'));zones.forEach(z=>z.classList.remove('is-active'));hideStory()};
  const showStory=d=>{if(!overlay)return;storyLabel.textContent='STORY MOCK';storyPath.textContent=d.storyPath;storyTitle.textContent=d.storyTitle;storyBody.textContent=d.storyBody;storySteps.innerHTML=d.steps.map(s=>'<span>'+s+'</span>').join('');storyLink.href=d.href;overlay.classList.add('show');overlay.setAttribute('aria-hidden','false')};
  const activate=key=>{const d=data[key];if(!d)return;board.classList.add('eco-board-focused');nodes.forEach(n=>n.classList.toggle('active',n.dataset.eco===key));routes.forEach(r=>r.classList.toggle('is-active',d.routes.includes(r.dataset.route)));zones.forEach(z=>z.classList.toggle('is-active',d.zones.includes(z.dataset.zone)));eyebrow.textContent=d.eyebrow;code.textContent=d.code;title.textContent=d.title;text.textContent=d.text;link.href=d.href;showStory(d)};
  const bindTarget=(el,key)=>{el.addEventListener('pointerenter',e=>{if(e.pointerType!=='touch')activate(key)});el.addEventListener('focus',()=>activate(key));el.addEventListener('click',()=>activate(key))};
  nodes.forEach(node=>bindTarget(node,node.dataset.eco));
  zones.forEach(zone=>{const key=zone.dataset.zone;if(!data[key])return;zone.setAttribute('tabindex','0');zone.setAttribute('role','button');zone.setAttribute('aria-label','Open '+data[key].code+' story');bindTarget(zone,key)});
  storyClose?.addEventListener('click',e=>{e.stopPropagation();clear();resetCopy()});
  board.addEventListener('pointerleave',e=>{if(e.pointerType==='touch')return;clear();resetCopy()});
  if(matchMedia('(prefers-reduced-motion: reduce)').matches&&scene&&scene.pauseAnimations)scene.pauseAnimations();
})();
</script>'''
text = text[:script_start] + new_script + text[script_end:]

hero_start_after = text.index('<section class="hero"')
hero_end_after = text.index('</section>', hero_start_after) + len('</section>')
services_start_after = text.index('<section class="services service-stories"')
services_end_after = text.index('</section>', services_start_after) + len('</section>')
if text[hero_start_after:hero_end_after] != hero_before:
    raise SystemExit('Hero changed unexpectedly')
if text[services_start_after:services_end_after] != services_before:
    raise SystemExit('Services changed unexpectedly')

for marker in [
    'Design 42 ecosystem iteration 2',
    'eco-story-overlay',
    'USER A → TELIKOM → USER B',
    'eco-starlink-dot',
    'ecoHubRing',
    'M216 160C292 157 356 169 439 193'
]:
    if marker not in text:
        raise SystemExit('Verification marker missing: ' + marker)

path.write_text(text, encoding='utf-8')
print('Refined ecosystem with live separated routes and story overlays')
