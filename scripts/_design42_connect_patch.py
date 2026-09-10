from pathlib import Path

path = Path('42.html')
text = path.read_text(encoding='utf-8')

if 'id="digitalPngLab"' in text:
    raise SystemExit('Digital PNG lab already exists')

html = r'''
<div class="digital-png-lab reveal" id="digitalPngLab" aria-labelledby="digitalPngTitle">
  <div class="digital-png-head">
    <div><div class="kicker">Digital PNG · New services</div><h3 id="digitalPngTitle">Connect. Compute. Transact.</h3></div>
    <p>Three new digital capabilities, each designed around a different part of how Papua New Guinea connects, builds and participates online.</p>
  </div>
  <div class="digital-sequence" aria-label="Digital PNG service sequence">
    <button class="digital-sequence-step active" type="button" data-digital-step="connect" aria-current="step"><small>01 / CONNECT</small><b>Starlink</b><span>Beyond the network edge</span></button>
    <button class="digital-sequence-step pending" type="button" data-digital-step="compute" disabled><small>02 / COMPUTE</small><b>Kumul Cloud</b><span>Sovereign cloud + AI</span></button>
    <button class="digital-sequence-step pending" type="button" data-digital-step="transact" disabled><small>03 / TRANSACT</small><b>Tcash</b><span>Digital financial access</span></button>
  </div>
  <article class="digital-story digital-connect active" data-digital-panel="connect">
    <div class="digital-story-copy">
      <div class="digital-story-label"><i></i><span>STARLINK · TELIKOM AUTHORISED RESELLER</span></div>
      <h4>Beyond the<br>network edge.</h4>
      <p>Connect remote sites, businesses, government locations and resource projects with Starlink through Telikom's local connectivity portfolio.</p>
      <div class="connect-usecases" role="group" aria-label="Explore Starlink use cases">
        <button class="active" type="button" data-starlink-use="remote"><span>01</span>Remote site</button>
        <button type="button" data-starlink-use="business"><span>02</span>Business</button>
        <button type="button" data-starlink-use="government"><span>03</span>Government</button>
        <button type="button" data-starlink-use="resource"><span>04</span>Resource project</button>
      </div>
      <div class="connect-use-detail"><small id="connectUseEyebrow">REMOTE SITE</small><b id="connectUseTitle">Reach locations beyond the usual network edge.</b><span id="connectUseBody">A visual link from orbit to a remote PNG site, showing how satellite connectivity can extend Telikom's reach.</span></div>
      <a class="digital-story-link" href="#business">Explore remote connectivity ↗</a>
    </div>
    <div class="connect-visual" id="connectVisual" data-use="remote" aria-label="Interactive Starlink connectivity visual">
      <div class="connect-grid" aria-hidden="true"></div>
      <div class="connect-orbit orbit-one" aria-hidden="true"></div>
      <div class="connect-orbit orbit-two" aria-hidden="true"></div>
      <div class="connect-satellite" aria-hidden="true"><i class="sat-array"></i><i class="sat-bus"></i><i class="sat-fin"></i><span>STARLINK</span></div>
      <div class="connect-beam beam-remote" aria-hidden="true"></div>
      <div class="connect-beam beam-business" aria-hidden="true"></div>
      <div class="connect-beam beam-government" aria-hidden="true"></div>
      <div class="connect-beam beam-resource" aria-hidden="true"></div>
      <img class="connect-png-map" src="assets/design42/png-admin1-simplemaps.svg" alt="" aria-hidden="true">
      <button class="connect-node node-remote active" type="button" data-starlink-node="remote"><i></i><b>REMOTE SITE</b><small>BEYOND EDGE</small></button>
      <button class="connect-node node-business" type="button" data-starlink-node="business"><i></i><b>BUSINESS</b><small>BRANCH LINK</small></button>
      <button class="connect-node node-government" type="button" data-starlink-node="government"><i></i><b>GOVERNMENT</b><small>PUBLIC SITE</small></button>
      <button class="connect-node node-resource" type="button" data-starlink-node="resource"><i></i><b>RESOURCE</b><small>PROJECT SITE</small></button>
      <div class="connect-telemetry"><span><i></i> ORBIT LINK</span><small>ACTIVE TARGET</small><b id="connectTelemetry">REMOTE SITE</b></div>
      <div class="connect-caption"><span>CONNECT</span><b>Satellite reach, Telikom context.</b></div>
    </div>
  </article>
</div>
'''

css = r'''
/* Design 42: Digital PNG innovation sequence, step 01 Starlink CONNECT */
.digital-png-lab{margin-top:52px;padding:30px;border:1px solid rgba(9,70,101,.12);border-radius:34px;background:linear-gradient(145deg,#f8fdff 0%,#eef9fd 52%,#edf8f5 100%);box-shadow:0 24px 70px rgba(20,79,102,.09);overflow:hidden;position:relative;isolation:isolate}
.digital-png-lab:before{content:"";position:absolute;inset:-30% 45% auto -8%;height:320px;background:radial-gradient(circle,rgba(28,160,232,.13),transparent 68%);pointer-events:none}
.digital-png-head{position:relative;z-index:2;display:grid;grid-template-columns:1fr .82fr;gap:38px;align-items:end;margin-bottom:22px}.digital-png-head .kicker{color:#0875c9}.digital-png-head h3{font-family:"Space Grotesk",Manrope,sans-serif;font-size:clamp(36px,4vw,58px);line-height:.92;letter-spacing:-.055em;margin:9px 0 0;color:#102b3c}.digital-png-head p{justify-self:end;max-width:540px;margin:0;color:#657f8b;font-size:12px;line-height:1.62}
.digital-sequence{position:relative;z-index:3;display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin-bottom:10px}.digital-sequence:before{content:"";position:absolute;left:8%;right:8%;top:20px;height:1px;background:linear-gradient(90deg,#1ca0e8,rgba(28,160,232,.18) 34%,rgba(32,169,87,.15));z-index:-1}.digital-sequence-step{min-height:74px;padding:12px 14px;border:1px solid rgba(16,86,116,.12);border-radius:18px;background:rgba(255,255,255,.78);text-align:left;color:#173d50;cursor:pointer;transition:.3s var(--spring);box-shadow:0 8px 22px rgba(22,84,107,.045)}.digital-sequence-step small{display:block;font-size:6.5px;font-weight:800;letter-spacing:.14em;color:#63818e}.digital-sequence-step b{display:block;font-family:"Space Grotesk";font-size:17px;line-height:1;margin:5px 0 4px}.digital-sequence-step span{display:block;font-size:7px;color:#718994}.digital-sequence-step.active{background:#fff;border-color:rgba(8,117,201,.35);box-shadow:0 13px 30px rgba(8,117,201,.10);transform:translateY(-2px)}.digital-sequence-step.active small{color:#0875c9}.digital-sequence-step.pending{opacity:.58;cursor:default}.digital-sequence-step:disabled{color:#4f6874}
.digital-story{position:relative;z-index:2;display:grid;grid-template-columns:.82fr 1.18fr;min-height:510px;border:1px solid rgba(8,73,103,.13);border-radius:28px;background:#071d29;overflow:hidden;color:#fff}.digital-story-copy{position:relative;z-index:5;padding:42px 34px 34px;display:flex;flex-direction:column;justify-content:center;background:linear-gradient(110deg,rgba(5,28,40,.99) 0%,rgba(6,35,49,.96) 74%,rgba(6,35,49,.70) 100%)}.digital-story-label{display:flex;align-items:center;gap:8px;font-size:6.5px;letter-spacing:.13em;font-weight:800;color:#98e5ff}.digital-story-label i{width:7px;height:7px;border-radius:50%;background:#8ae6ff;box-shadow:0 0 0 5px rgba(85,205,247,.09),0 0 18px rgba(85,205,247,.5)}.digital-story-copy h4{font-family:"Space Grotesk";font-size:clamp(42px,4.6vw,68px);line-height:.86;letter-spacing:-.06em;margin:15px 0 17px}.digital-story-copy>p{margin:0;max-width:480px;font-size:11.5px;line-height:1.62;color:#a9c1cc}.digital-story-link{margin-top:16px;width:max-content;font-size:8px;font-weight:800;color:#a8eaff;border-bottom:1px solid rgba(168,234,255,.35);padding-bottom:3px}
.connect-usecases{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:6px;margin:20px 0 12px}.connect-usecases button{min-width:0;padding:9px 10px;border:1px solid rgba(150,221,250,.12);border-radius:12px;background:rgba(255,255,255,.035);color:#a9c2cd;text-align:left;font-size:7px;font-weight:800;cursor:pointer;transition:.24s}.connect-usecases button span{font-size:5.5px;color:#62899b;margin-right:6px}.connect-usecases button:hover,.connect-usecases button:focus-visible,.connect-usecases button.active{outline:none;background:rgba(96,207,249,.10);border-color:rgba(135,224,255,.34);color:#fff;transform:translateY(-2px)}
.connect-use-detail{min-height:68px;padding:11px 12px;border-left:2px solid rgba(116,218,255,.42);background:linear-gradient(90deg,rgba(82,190,232,.08),transparent);border-radius:0 12px 12px 0}.connect-use-detail small{display:block;font-size:5.8px;letter-spacing:.12em;color:#77c9e8;font-weight:800}.connect-use-detail b{display:block;font-family:"Space Grotesk";font-size:12px;line-height:1.15;margin:4px 0;color:#f0fbff}.connect-use-detail span{display:block;font-size:7.2px;line-height:1.4;color:#8daab7}
.connect-visual{--sx:23%;--sy:18%;position:relative;overflow:hidden;min-height:510px;background:radial-gradient(circle at 74% 68%,rgba(42,170,222,.18),transparent 28%),radial-gradient(circle at 32% 23%,rgba(105,211,252,.09),transparent 22%),linear-gradient(145deg,#061925,#0b3345 70%,#0b3b41);isolation:isolate}.connect-visual:before{content:"";position:absolute;inset:0;background:radial-gradient(circle at 50% 55%,transparent 0 22%,rgba(110,225,255,.025) 23% 23.4%,transparent 24% 100%);background-size:42px 42px;opacity:.4}.connect-visual:after{content:"";position:absolute;inset:0;box-shadow:inset 50px 0 80px rgba(5,28,40,.46);pointer-events:none;z-index:9}.connect-grid{position:absolute;inset:0;background-image:linear-gradient(rgba(142,223,255,.035) 1px,transparent 1px),linear-gradient(90deg,rgba(142,223,255,.035) 1px,transparent 1px);background-size:38px 38px;mask-image:radial-gradient(circle at 62% 58%,#000,transparent 78%)}.connect-orbit{position:absolute;border:1px solid rgba(142,226,255,.17);border-radius:50%;transform:rotate(-17deg);pointer-events:none}.orbit-one{width:700px;height:245px;left:-7%;top:1%}.orbit-two{width:850px;height:340px;left:-15%;top:-9%;border-style:dashed;opacity:.48;animation:connectOrbitDrift 18s linear infinite}@keyframes connectOrbitDrift{to{transform:rotate(343deg)}}
.connect-satellite{position:absolute;z-index:6;left:var(--sx);top:var(--sy);width:106px;height:52px;transform:translate(-50%,-50%) rotate(-8deg);transition:left .75s var(--spring),top .75s var(--spring),transform .75s var(--spring);filter:drop-shadow(0 12px 18px rgba(0,0,0,.3))}.connect-satellite .sat-array{position:absolute;left:0;top:13px;width:67px;height:24px;border:1px solid rgba(149,217,241,.5);background:repeating-linear-gradient(90deg,transparent 0 12px,rgba(112,198,229,.22) 13px),linear-gradient(145deg,#153d50,#081f2b)}.connect-satellite .sat-bus{position:absolute;left:61px;top:15px;width:32px;height:20px;border-radius:5px;background:linear-gradient(90deg,#eff7f8,#748b93);clip-path:polygon(0 12%,79% 0,100% 40%,82% 100%,8% 86%)}.connect-satellite .sat-fin{position:absolute;left:88px;top:10px;width:17px;height:29px;background:#163b4c;clip-path:polygon(0 17%,100% 0,85% 83%,10% 100%)}.connect-satellite span{position:absolute;left:66px;top:39px;font-size:4.5px;letter-spacing:.12em;font-weight:800;color:#a9dff1}.connect-visual[data-use="remote"]{--sx:23%;--sy:18%}.connect-visual[data-use="business"]{--sx:39%;--sy:13%}.connect-visual[data-use="government"]{--sx:57%;--sy:14%}.connect-visual[data-use="resource"]{--sx:73%;--sy:20%}
.connect-png-map{position:absolute;z-index:2;right:7%;bottom:5%;width:72%;height:70%;object-fit:contain;opacity:.18;filter:brightness(2.1) saturate(.2) drop-shadow(0 0 18px rgba(97,214,255,.18));transform:rotate(-2deg)}
.connect-beam{position:absolute;z-index:4;width:2px;opacity:0;transform-origin:top;background:linear-gradient(#d9f9ff,rgba(116,224,255,.34) 55%,transparent);filter:drop-shadow(0 0 6px #8ee8ff);transition:opacity .25s}.connect-beam:after{content:"";position:absolute;left:50%;bottom:-6px;width:12px;height:12px;border:1px solid rgba(171,239,255,.8);border-radius:50%;transform:translateX(-50%);animation:connectTargetPulse 1.5s ease-out infinite}@keyframes connectTargetPulse{to{width:44px;height:44px;bottom:-22px;opacity:0}}.beam-remote{left:24%;top:21%;height:285px;transform:rotate(13deg)}.beam-business{left:40%;top:16%;height:296px;transform:rotate(21deg)}.beam-government{left:58%;top:17%;height:248px;transform:rotate(27deg)}.beam-resource{left:74%;top:23%;height:265px;transform:rotate(-23deg)}.connect-visual[data-use="remote"] .beam-remote,.connect-visual[data-use="business"] .beam-business,.connect-visual[data-use="government"] .beam-government,.connect-visual[data-use="resource"] .beam-resource{opacity:1;animation:connectBeamIn .65s var(--spring)}@keyframes connectBeamIn{from{opacity:0;transform-origin:top;filter:blur(4px)}to{opacity:1;filter:drop-shadow(0 0 6px #8ee8ff)}}
.connect-node{position:absolute;z-index:8;min-width:106px;padding:8px 9px 7px 24px;border:1px solid rgba(131,220,255,.17);border-radius:12px;background:rgba(5,31,43,.66);backdrop-filter:blur(12px);color:#d9eff6;text-align:left;cursor:pointer;transition:.28s var(--spring);box-shadow:0 10px 24px rgba(0,0,0,.13)}.connect-node>i{position:absolute;left:9px;top:50%;width:7px;height:7px;border-radius:50%;background:#5d8393;transform:translateY(-50%);transition:.25s}.connect-node b{display:block;font-size:6.5px;letter-spacing:.08em}.connect-node small{display:block;margin-top:2px;font-size:4.8px;color:#688b99}.connect-node:hover,.connect-node:focus-visible,.connect-node.active{outline:none;border-color:rgba(142,232,255,.48);background:rgba(11,59,77,.84);transform:translateY(-3px)}.connect-node.active>i{background:#c6f6ff;box-shadow:0 0 0 5px rgba(134,230,255,.10),0 0 16px #80e1ff}.node-remote{left:29%;bottom:16%}.node-business{left:49%;bottom:11%}.node-government{right:7%;top:43%}.node-resource{right:14%;bottom:9%}
.connect-telemetry{position:absolute;z-index:8;left:18px;top:18px;padding:10px 12px;border:1px solid rgba(138,225,255,.14);border-radius:13px;background:rgba(5,28,40,.53);backdrop-filter:blur(10px)}.connect-telemetry>span{display:flex;align-items:center;gap:6px;font-size:5.3px;font-weight:800;letter-spacing:.11em;color:#96dff8}.connect-telemetry>span i{width:5px;height:5px;border-radius:50%;background:#7ce5ff;box-shadow:0 0 10px #7ce5ff;animation:connectBlink 1.3s ease-in-out infinite alternate}@keyframes connectBlink{to{opacity:.35}}.connect-telemetry small{display:block;font-size:4.6px;color:#5e8291;margin:6px 0 2px}.connect-telemetry b{display:block;font-family:"Space Grotesk";font-size:10px;color:#effcff}.connect-caption{position:absolute;z-index:8;left:20px;bottom:19px}.connect-caption span{display:block;font-size:6px;letter-spacing:.15em;color:#79d6f6;font-weight:800}.connect-caption b{display:block;font-family:"Space Grotesk";font-size:13px;margin-top:4px;color:#eefbff}
@media(max-width:1000px){.digital-story{grid-template-columns:1fr 1.15fr}.digital-story-copy{padding:34px 25px}.connect-node{min-width:95px}.node-remote{left:22%}.node-business{left:44%}.node-resource{right:7%}}
@media(max-width:820px){.digital-png-lab{margin-top:34px;padding:18px;border-radius:25px}.digital-png-head{grid-template-columns:1fr;gap:12px}.digital-png-head p{justify-self:start}.digital-sequence{display:flex;overflow-x:auto;padding-bottom:4px;scroll-snap-type:x mandatory}.digital-sequence-step{flex:0 0 180px;scroll-snap-align:start}.digital-story{grid-template-columns:1fr;min-height:0}.digital-story-copy{padding:30px 22px}.digital-story-copy h4{font-size:50px}.connect-visual{min-height:430px}.connect-png-map{width:87%;right:-5%}.connect-node{min-width:92px}.node-remote{left:15%;bottom:17%}.node-business{left:42%;bottom:9%}.node-government{right:4%;top:43%}.node-resource{right:7%;bottom:25%}}
@media(prefers-reduced-motion:reduce){.orbit-two,.connect-beam:after,.connect-telemetry>span i{animation:none!important}.connect-satellite,.connect-node{transition:none!important}}
'''

js = r'''
<script id="digitalPngConnectScript">
(()=>{
  const visual=document.getElementById('connectVisual');
  if(!visual)return;
  const buttons=[...document.querySelectorAll('[data-starlink-use]')];
  const nodes=[...document.querySelectorAll('[data-starlink-node]')];
  const eyebrow=document.getElementById('connectUseEyebrow');
  const title=document.getElementById('connectUseTitle');
  const body=document.getElementById('connectUseBody');
  const telemetry=document.getElementById('connectTelemetry');
  const details={
    remote:{eyebrow:'REMOTE SITE',title:'Reach locations beyond the usual network edge.',body:'A visual link from orbit to a remote PNG site, showing how satellite connectivity can extend Telikom\'s reach.'},
    business:{eyebrow:'BUSINESS',title:'Keep branches and field teams connected.',body:'Use satellite connectivity as another option for business locations where terrestrial connectivity is difficult or unavailable.'},
    government:{eyebrow:'GOVERNMENT',title:'Connect public-service locations across distance.',body:'Show how remote offices and service locations can stay connected through Telikom\'s broader connectivity portfolio.'},
    resource:{eyebrow:'RESOURCE PROJECT',title:'Bring connectivity to project locations.',body:'A strong fit for remote project environments that need a reliable link back to teams, systems and services.'}
  };
  function setUse(key){
    if(!details[key])return;
    visual.dataset.use=key;
    buttons.forEach(b=>b.classList.toggle('active',b.dataset.starlinkUse===key));
    nodes.forEach(n=>n.classList.toggle('active',n.dataset.starlinkNode===key));
    const d=details[key];
    eyebrow.textContent=d.eyebrow;title.textContent=d.title;body.textContent=d.body;telemetry.textContent=d.eyebrow;
  }
  buttons.forEach(b=>{b.addEventListener('click',()=>setUse(b.dataset.starlinkUse));b.addEventListener('pointerenter',e=>{if(e.pointerType!=='touch')setUse(b.dataset.starlinkUse)})});
  nodes.forEach(n=>{n.addEventListener('click',()=>setUse(n.dataset.starlinkNode));n.addEventListener('pointerenter',e=>{if(e.pointerType!=='touch')setUse(n.dataset.starlinkNode)})});
  visual.addEventListener('pointermove',e=>{if(e.pointerType==='touch')return;const r=visual.getBoundingClientRect();visual.style.setProperty('--connect-x',(((e.clientX-r.left)/r.width-.5)*2).toFixed(3));visual.style.setProperty('--connect-y',(((e.clientY-r.top)/r.height-.5)*2).toFixed(3))},{passive:true});
})();
</script>
'''

marker = '\n<section class="business business-dual" id="business"'
if text.count(marker) != 1:
    raise SystemExit(f'Expected one Business section marker, found {text.count(marker)}')

service_tail = '</article></div></div></section>' + marker
if text.count(service_tail) != 1:
    raise SystemExit(f'Expected one Services section tail, found {text.count(service_tail)}')

text = text.replace(service_tail, '</article></div>' + html + '</div></section>' + marker, 1)

style_marker = '</style>'
if text.count(style_marker) != 1:
    raise SystemExit(f'Expected one style close, found {text.count(style_marker)}')
text = text.replace(style_marker, css + '\n</style>', 1)

body_marker = '</body>'
if text.count(body_marker) != 1:
    raise SystemExit(f'Expected one body close, found {text.count(body_marker)}')
text = text.replace(body_marker, js + '\n</body>', 1)

path.write_text(text, encoding='utf-8')
print('Added Digital PNG Starlink CONNECT experience inside Services')
