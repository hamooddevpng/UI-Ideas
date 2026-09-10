from pathlib import Path

path = Path('42.html')
text = path.read_text(encoding='utf-8')

if 'id="digital-png-rail"' in text:
    raise SystemExit('Compact Digital PNG rail already exists')

business_anchor = '<section class="business business-dual" id="business" data-focus="business">'
if text.count(business_anchor) != 1:
    raise SystemExit(f'Business section anchor mismatch: {text.count(business_anchor)}')

rail = r'''
<section class="digital-png-rail" id="digital-png-rail" aria-labelledby="digitalPngTitle">
  <div class="shell">
    <div class="digital-png-intro reveal">
      <div><div class="kicker">Digital PNG</div><h2 id="digitalPngTitle">Connect. Compute. Transact.</h2></div>
      <p>Three capabilities extending Telikom from connectivity into sovereign cloud, AI and digital financial access.</p>
    </div>
    <div class="digital-png-cards">
      <article class="digital-png-card digital-starlink reveal" tabindex="0" aria-label="Starlink remote connectivity">
        <div class="digital-card-top"><span>01 / CONNECT</span><small>REMOTE CONNECTIVITY</small></div>
        <div class="digital-card-art starlink-card-art" aria-hidden="true">
          <svg viewBox="0 0 360 132" role="presentation">
            <path class="sl-orbit" d="M-10 72 C72 2 224 -12 374 36"/>
            <g class="sl-mini-sat" transform="translate(226 20) rotate(-8)">
              <path d="M-48 10h59v27h-59z" class="sl-panel"/>
              <path d="M-38 12v23M-25 12v23M-12 12v23M1 12v23M-47 20h57M-47 28h57" class="sl-grid"/>
              <path d="M12 14h42l13 9-8 20H17L7 31z" class="sl-body"/>
              <circle cx="57" cy="29" r="3" class="sl-beacon"/>
            </g>
            <path class="sl-beam" d="M283 50 L223 112 L322 112 Z"/>
            <g class="sl-mini-dish" transform="translate(252 82)">
              <path d="M0 32h52" class="sl-ground"/><path d="M25 9v23M25 24L9 34M25 24l17 10" class="sl-mast"/>
              <rect x="4" y="-2" width="43" height="22" rx="5" transform="rotate(-13 25 9)" class="sl-dish"/>
            </g>
          </svg>
          <div class="digital-art-tag">STARLINK · TELIKOM</div>
        </div>
        <div class="digital-card-copy"><h3>Starlink</h3><p>Extend connectivity to remote sites, communities and operations beyond the usual network edge.</p><div class="digital-card-meta"><span>REMOTE SITES</span><span>BUSINESS</span><span>GOVERNMENT</span></div></div>
      </article>

      <article class="digital-png-card digital-kumul reveal" tabindex="0" aria-label="Kumul Cloud sovereign AI data centre">
        <div class="digital-card-top"><span>02 / COMPUTE</span><small>SOVEREIGN AI DATA CENTRE</small></div>
        <div class="digital-card-art kumul-card-art" aria-hidden="true">
          <img src="assets/design42/png-admin1-simplemaps.svg" alt="">
          <div class="kumul-mini-core"><small>KUMUL</small><b>CLOUD</b><i></i></div>
          <div class="kumul-rack kr1"><i></i><i></i><i></i></div>
          <div class="kumul-rack kr2"><i></i><i></i><i></i></div>
          <span class="kumul-route ka"></span><span class="kumul-route kb"></span>
          <span class="kumul-packet kp1"></span><span class="kumul-packet kp2"></span>
          <div class="digital-art-tag">PNG-HOSTED · AI-READY</div>
        </div>
        <div class="digital-card-copy"><h3>Kumul Cloud</h3><p>PNG-hosted cloud and AI infrastructure for sovereign data, resilient workloads and modern enterprise services.</p><div class="digital-card-meta"><span>CLOUD</span><span>AI</span><span>BACKUP</span></div></div>
      </article>

      <article class="digital-png-card digital-tcash reveal" tabindex="0" aria-label="T-Cash digital wallet">
        <div class="digital-card-top"><span>03 / TRANSACT</span><small>DIGITAL WALLET</small></div>
        <div class="digital-card-art tcash-card-art" aria-hidden="true">
          <div class="tcash-phone left"><i></i><b>K</b><small>SEND</small></div>
          <div class="tcash-link"><span></span><i>→</i></div>
          <div class="tcash-token">K</div>
          <div class="tcash-phone right"><i></i><b>✓</b><small>RECEIVED</small></div>
          <div class="digital-art-tag">PAYMENTS · TRANSFERS · ACCESS</div>
        </div>
        <div class="digital-card-copy"><h3>T-Cash</h3><p>Digital wallet services designed to make payments, transfers and financial access simpler from a mobile device.</p><div class="digital-card-meta"><span>PAYMENTS</span><span>TRANSFERS</span><span>MOBILE</span></div></div>
      </article>
    </div>
  </div>
</section>
'''

text = text.replace(business_anchor, rail + '\n' + business_anchor, 1)

css = r'''

/* Design 42: compact Digital PNG service rail. Kept outside Service Categories so the original grid is untouched. */
.digital-png-rail{position:relative;padding:42px 0 48px;background:linear-gradient(180deg,#eef8fb 0%,#f7fbfc 100%);border-top:1px solid rgba(16,43,60,.06);border-bottom:1px solid rgba(16,43,60,.07);overflow:hidden}
.digital-png-rail:before{content:"";position:absolute;inset:-45% -10% auto;height:430px;background:radial-gradient(circle at 22% 46%,rgba(28,160,232,.10),transparent 30%),radial-gradient(circle at 76% 42%,rgba(32,169,87,.07),transparent 30%);pointer-events:none}
.digital-png-intro{position:relative;z-index:2;display:flex;align-items:end;justify-content:space-between;gap:30px;margin-bottom:18px}
.digital-png-intro h2{font-family:"Space Grotesk",Manrope,sans-serif;font-size:clamp(27px,3vw,40px);line-height:1;letter-spacing:-.045em;margin:7px 0 0;color:#102f3f}
.digital-png-intro p{max-width:500px;margin:0;font-size:11px;line-height:1.55;color:#607c89}
.digital-png-cards{position:relative;z-index:2;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px}
.digital-png-card{--dx:0px;--dy:0px;position:relative;min-width:0;height:250px;border:1px solid rgba(20,78,102,.10);border-radius:22px;background:#fff;box-shadow:0 14px 35px rgba(19,70,91,.06);overflow:hidden;outline:none;transition:transform .34s var(--spring),box-shadow .34s var(--spring),border-color .25s}
.digital-png-card:hover,.digital-png-card:focus-visible{transform:translateY(-6px);box-shadow:0 24px 55px rgba(18,74,98,.13);border-color:rgba(8,117,201,.24)}
.digital-card-top{height:34px;padding:0 14px;display:flex;align-items:center;justify-content:space-between;border-bottom:1px solid rgba(20,78,102,.08);background:rgba(255,255,255,.76);position:relative;z-index:4}
.digital-card-top span,.digital-card-top small{font-size:6px;line-height:1;letter-spacing:.12em;font-weight:800}.digital-card-top span{color:#0875c9}.digital-card-top small{color:#738b96}
.digital-card-art{position:relative;height:112px;overflow:hidden}.digital-art-tag{position:absolute;left:13px;bottom:9px;font-size:5.5px;font-weight:800;letter-spacing:.11em;color:rgba(255,255,255,.82)}
.digital-card-copy{height:104px;padding:12px 14px 11px;display:flex;flex-direction:column}.digital-card-copy h3{font-family:"Space Grotesk";font-size:21px;line-height:1;margin:0 0 6px;letter-spacing:-.035em;color:#14394a}.digital-card-copy p{margin:0;font-size:7.9px;line-height:1.42;color:#647f8b;max-width:96%}.digital-card-meta{display:flex;gap:5px;margin-top:auto}.digital-card-meta span{padding:4px 6px;border-radius:999px;background:#edf6f9;color:#4e7687;font-size:5.2px;font-weight:800;letter-spacing:.07em}

/* Starlink mini visual */
.starlink-card-art{background:linear-gradient(145deg,#061b27 0%,#0c4152 58%,#397789 100%)}.starlink-card-art svg{position:absolute;inset:0;width:100%;height:100%}.sl-orbit{fill:none;stroke:rgba(191,239,255,.20);stroke-width:1.2;stroke-dasharray:5 8}.sl-panel{fill:#123a4d;stroke:#72a9ba;stroke-width:1}.sl-grid{fill:none;stroke:rgba(157,211,232,.26);stroke-width:.8}.sl-body{fill:#dce7e9;stroke:#f4fbfc;stroke-width:1}.sl-beacon{fill:#dff9ff;filter:drop-shadow(0 0 5px #b9efff);animation:dpBeacon 1.5s ease-in-out infinite}.sl-beam{fill:url(#none);fill:rgba(162,230,249,.08);stroke:rgba(182,239,255,.22);stroke-width:.7;animation:dpBeam 2.1s ease-in-out infinite}.sl-ground,.sl-mast{fill:none;stroke:#d9e3e5;stroke-width:3;stroke-linecap:round}.sl-dish{fill:#eef3f3;stroke:#fff;stroke-width:1}.digital-starlink:hover .sl-mini-sat,.digital-starlink:focus-visible .sl-mini-sat{animation:dpSatDrift 2.8s ease-in-out infinite}.digital-starlink:hover .sl-beam,.digital-starlink:focus-visible .sl-beam{fill:rgba(168,234,252,.15);stroke:rgba(210,248,255,.52)}
@keyframes dpBeacon{50%{opacity:.22;transform:scale(1.7);transform-origin:center}}@keyframes dpBeam{50%{opacity:.42}}@keyframes dpSatDrift{50%{transform:translate(218px,24px) rotate(-5deg)}}

/* Kumul Cloud mini visual */
.kumul-card-art{background:radial-gradient(circle at 55% 52%,rgba(78,209,176,.18),transparent 28%),linear-gradient(145deg,#061e28,#0b4546 68%,#0d5c4d)}.kumul-card-art>img{position:absolute;left:50%;top:50%;width:74%;height:98%;object-fit:contain;transform:translate(-50%,-50%);opacity:.18;filter:brightness(2) saturate(.25)}.kumul-mini-core{position:absolute;left:50%;top:48%;width:82px;height:58px;border:1px solid rgba(158,241,218,.25);border-radius:14px;background:rgba(6,42,47,.86);box-shadow:0 10px 24px rgba(0,0,0,.15),0 0 24px rgba(103,228,196,.11);transform:translate(-50%,-50%);display:flex;flex-direction:column;align-items:center;justify-content:center;color:#eafff8}.kumul-mini-core small{font-size:4.7px;letter-spacing:.16em;color:#82dcc3}.kumul-mini-core b{font-family:"Space Grotesk";font-size:13px;line-height:1;margin-top:2px}.kumul-mini-core>i{position:absolute;width:5px;height:5px;border-radius:50%;right:9px;top:9px;background:#7ce3c5;box-shadow:0 0 9px #7ce3c5;animation:dpBeacon 1.7s ease-in-out infinite}.kumul-rack{position:absolute;width:36px;height:52px;padding:5px;border:1px solid rgba(153,233,213,.15);border-radius:8px;background:#123b42}.kumul-rack i{display:block;height:8px;margin-bottom:4px;border-radius:2px;background:linear-gradient(90deg,#235966 0 75%,#8ce8cf 76% 83%,#17434b 84%)}.kr1{left:16%;top:24%;transform:rotate(-5deg)}.kr2{right:14%;top:26%;transform:rotate(5deg)}.kumul-route{position:absolute;height:1px;background:linear-gradient(90deg,transparent,#8ee8cf,transparent);transform-origin:left}.ka{left:24%;top:47%;width:100px;transform:rotate(6deg)}.kb{left:52%;top:50%;width:95px;transform:rotate(-9deg)}.kumul-packet{position:absolute;width:6px;height:6px;border-radius:2px;background:#dffcf4;box-shadow:0 0 9px #7ce3c5}.kp1{left:23%;top:43%;animation:dpPacketA 2.6s ease-in-out infinite}.kp2{right:23%;top:42%;animation:dpPacketB 2.8s ease-in-out infinite .45s}.digital-kumul:hover .kumul-mini-core,.digital-kumul:focus-visible .kumul-mini-core{box-shadow:0 10px 24px rgba(0,0,0,.15),0 0 42px rgba(103,228,196,.25)}
@keyframes dpPacketA{50%{left:47%;top:49%}100%{left:23%;top:43%;opacity:.35}}@keyframes dpPacketB{50%{right:44%;top:49%}100%{right:23%;top:42%;opacity:.35}}

/* T-Cash mini visual */
.tcash-card-art{background:radial-gradient(circle at 50% 50%,rgba(101,215,255,.16),transparent 30%),linear-gradient(145deg,#07304a,#0875c9 66%,#1496df)}.tcash-phone{position:absolute;top:18px;width:49px;height:74px;border:2px solid rgba(255,255,255,.83);border-radius:12px;background:rgba(7,45,73,.38);box-shadow:0 12px 24px rgba(0,0,0,.15);display:flex;flex-direction:column;align-items:center;justify-content:center;color:#fff}.tcash-phone:before{content:"";position:absolute;top:5px;width:15px;height:2px;border-radius:999px;background:rgba(255,255,255,.34)}.tcash-phone.left{left:18%}.tcash-phone.right{right:18%}.tcash-phone b{font-family:"Space Grotesk";font-size:18px;line-height:1}.tcash-phone small{font-size:4.8px;letter-spacing:.1em;margin-top:4px;color:#bdeaff}.tcash-link{position:absolute;left:34%;right:34%;top:50%;height:1px;background:rgba(210,246,255,.32)}.tcash-link span{position:absolute;inset:-5px 0;border-top:1px dashed rgba(210,246,255,.22)}.tcash-link i{position:absolute;right:-4px;top:-10px;color:#d8f7ff;font-size:14px;font-style:normal}.tcash-token{position:absolute;z-index:3;left:35%;top:44%;width:28px;height:28px;border-radius:50%;background:#fff;color:#0875c9;display:grid;place-items:center;font-family:"Space Grotesk";font-size:13px;font-weight:800;box-shadow:0 0 0 6px rgba(255,255,255,.09),0 8px 22px rgba(0,0,0,.15);animation:dpCash 3s ease-in-out infinite}.digital-tcash:hover .tcash-token,.digital-tcash:focus-visible .tcash-token{animation-duration:1.45s}.digital-tcash:hover .tcash-phone.right,.digital-tcash:focus-visible .tcash-phone.right{box-shadow:0 12px 24px rgba(0,0,0,.15),0 0 25px rgba(188,239,255,.28)}
@keyframes dpCash{0%,100%{left:35%;transform:scale(.82);opacity:.6}50%{left:58%;transform:scale(1);opacity:1}}

@media(max-width:1050px) and (min-width:821px){.digital-png-card{height:258px}.digital-card-copy p{font-size:7.4px}.digital-card-meta span{font-size:4.8px}}
@media(max-width:820px){.digital-png-rail{padding:34px 0 40px}.digital-png-intro{display:block;margin-bottom:15px}.digital-png-intro p{margin-top:9px;font-size:10px}.digital-png-cards{display:flex;gap:10px;overflow-x:auto;padding:2px 1px 12px;scroll-snap-type:x mandatory}.digital-png-card{flex:0 0 min(84vw,390px);height:250px;scroll-snap-align:start}.digital-png-cards::-webkit-scrollbar{height:4px}.digital-png-cards::-webkit-scrollbar-thumb{background:rgba(8,117,201,.2);border-radius:999px}}
@media(prefers-reduced-motion:reduce){.digital-png-card,.sl-beacon,.sl-beam,.sl-mini-sat,.kumul-mini-core>i,.kumul-packet,.tcash-token{animation:none!important;transition:none!important}}
'''

style_close = '</style>'
if text.count(style_close) != 1:
    raise SystemExit('style close mismatch')
text = text.replace(style_close, css + '\n</style>', 1)

path.write_text(text, encoding='utf-8')
print('Added compact Digital PNG rail after Services')
