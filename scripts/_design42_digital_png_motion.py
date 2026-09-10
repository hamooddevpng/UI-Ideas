from pathlib import Path

path = Path('42.html')
text = path.read_text(encoding='utf-8')

marker = '/* Design 42: compact Digital PNG service rail. Kept outside Service Categories so the original grid is untouched. */'
if text.count(marker) != 1:
    raise SystemExit(f'Digital PNG CSS marker mismatch: {text.count(marker)}')

start = text.index(marker)
end = text.index('</style>', start)
outside_before = text[:start] + text[end:]

css = r'''/* Design 42: compact Digital PNG service rail. Kept outside Service Categories so the original grid is untouched. */
.digital-png-rail{position:relative;padding:42px 0 48px;background:linear-gradient(180deg,#eef8fb 0%,#f7fbfc 100%);border-top:1px solid rgba(16,43,60,.06);border-bottom:1px solid rgba(16,43,60,.07);overflow:hidden}
.digital-png-rail:before{content:"";position:absolute;inset:-45% -10% auto;height:430px;background:radial-gradient(circle at 22% 46%,rgba(28,160,232,.10),transparent 30%),radial-gradient(circle at 76% 42%,rgba(32,169,87,.07),transparent 30%);pointer-events:none}
.digital-png-intro{position:relative;z-index:2;display:flex;align-items:end;justify-content:space-between;gap:30px;margin-bottom:18px}
.digital-png-intro h2{font-family:"Space Grotesk",Manrope,sans-serif;font-size:clamp(27px,3vw,40px);line-height:1;letter-spacing:-.045em;margin:7px 0 0;color:#102f3f}
.digital-png-intro p{max-width:500px;margin:0;font-size:11px;line-height:1.55;color:#607c89}
.digital-png-cards{position:relative;z-index:2;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px}
.digital-png-card{--dx:0px;--dy:0px;position:relative;min-width:0;height:250px;border:1px solid rgba(20,78,102,.10);border-radius:22px;background:#fff;box-shadow:0 14px 35px rgba(19,70,91,.06);overflow:hidden;outline:none;transition:transform .34s var(--spring),box-shadow .34s var(--spring),border-color .25s,opacity .34s var(--ease),filter .34s var(--ease)}
.digital-png-card:hover,.digital-png-card:focus-visible{transform:translateY(-3px);box-shadow:0 20px 46px rgba(18,74,98,.11);border-color:rgba(8,117,201,.24)}
.digital-png-card:nth-child(1).reveal{transition-delay:.06s}.digital-png-card:nth-child(2).reveal{transition-delay:.14s}.digital-png-card:nth-child(3).reveal{transition-delay:.22s}
.digital-card-top{height:34px;padding:0 14px;display:flex;align-items:center;justify-content:space-between;border-bottom:1px solid rgba(20,78,102,.08);background:rgba(255,255,255,.76);position:relative;z-index:4}
.digital-card-top span,.digital-card-top small{font-size:6px;line-height:1;letter-spacing:.12em;font-weight:800}.digital-card-top span{color:#0875c9}.digital-card-top small{color:#738b96}
.digital-card-art{position:relative;height:112px;overflow:hidden;transition:filter .34s var(--ease)}.digital-art-tag{position:absolute;left:13px;bottom:9px;font-size:5.5px;font-weight:800;letter-spacing:.11em;color:rgba(255,255,255,.82)}
.digital-png-card:hover .digital-card-art,.digital-png-card:focus-visible .digital-card-art{filter:saturate(1.06) brightness(1.025)}
.digital-card-copy{height:104px;padding:12px 14px 11px;display:flex;flex-direction:column}.digital-card-copy h3{font-family:"Space Grotesk";font-size:21px;line-height:1;margin:0 0 6px;letter-spacing:-.035em;color:#14394a}.digital-card-copy p{margin:0;font-size:7.9px;line-height:1.42;color:#647f8b;max-width:96%}.digital-card-meta{display:flex;gap:5px;margin-top:auto}.digital-card-meta span{padding:4px 6px;border-radius:999px;background:#edf6f9;color:#4e7687;font-size:5.2px;font-weight:800;letter-spacing:.07em}
@media(hover:hover) and (pointer:fine){.digital-png-cards:has(.digital-png-card:hover) .digital-png-card:not(:hover){opacity:.78;filter:saturate(.88)}.digital-png-cards:has(.digital-png-card:focus-visible) .digital-png-card:not(:focus-visible){opacity:.82;filter:saturate(.9)}}

/* Starlink mini visual: quiet orbital drift, directional beam pulse and hover lock-on. */
.starlink-card-art{background:linear-gradient(145deg,#061b27 0%,#0c4152 58%,#397789 100%)}.starlink-card-art svg{position:absolute;inset:0;width:100%;height:100%}.sl-orbit{fill:none;stroke:rgba(191,239,255,.20);stroke-width:1.2;stroke-dasharray:5 8;transition:stroke .28s,filter .28s}.sl-panel{fill:#123a4d;stroke:#72a9ba;stroke-width:1}.sl-grid{fill:none;stroke:rgba(157,211,232,.26);stroke-width:.8}.sl-body{fill:#dce7e9;stroke:#f4fbfc;stroke-width:1}.sl-mini-sat{transform-box:fill-box;transform-origin:center;animation:dpSatOrbit 9.6s ease-in-out infinite alternate;will-change:transform}.sl-beacon{fill:#dff9ff;filter:drop-shadow(0 0 5px #b9efff);transform-box:fill-box;transform-origin:center;animation:dpBeacon 2.1s ease-in-out infinite}.sl-beam{fill:rgba(162,230,249,.08);stroke:rgba(182,239,255,.22);stroke-width:.7;stroke-dasharray:2 5;filter:drop-shadow(0 0 4px rgba(185,239,255,.08));animation:dpBeam 2.8s linear infinite;transition:fill .28s,stroke .28s,filter .28s}.sl-ground,.sl-mast{fill:none;stroke:#d9e3e5;stroke-width:3;stroke-linecap:round}.sl-dish{fill:#eef3f3;stroke:#fff;stroke-width:1;transition:filter .28s}.digital-starlink:hover .sl-orbit,.digital-starlink:focus-visible .sl-orbit{stroke:rgba(199,243,255,.38);filter:drop-shadow(0 0 4px rgba(185,239,255,.18))}.digital-starlink:hover .sl-beacon,.digital-starlink:focus-visible .sl-beacon{animation-duration:1.05s;filter:drop-shadow(0 0 9px #c9f5ff)}.digital-starlink:hover .sl-beam,.digital-starlink:focus-visible .sl-beam{fill:rgba(168,234,252,.14);stroke:rgba(210,248,255,.48);filter:drop-shadow(0 0 7px rgba(185,239,255,.2));animation-duration:1.45s}.digital-starlink:hover .sl-dish,.digital-starlink:focus-visible .sl-dish{filter:brightness(1.12) drop-shadow(0 0 4px rgba(218,248,255,.22))}
@keyframes dpSatOrbit{0%{transform:translate(214px,23px) rotate(-10deg)}50%{transform:translate(226px,20px) rotate(-8deg)}100%{transform:translate(239px,17px) rotate(-5deg)}}
@keyframes dpBeacon{0%,100%{opacity:.7;transform:scale(.82)}50%{opacity:1;transform:scale(1.28)}}
@keyframes dpBeam{0%{opacity:.18;stroke-dashoffset:0}45%{opacity:.5}100%{opacity:.2;stroke-dashoffset:-18}}

/* Kumul Cloud mini visual: one-way packets into the sovereign core, responsive rack lights and a restrained core breath. */
.kumul-card-art{background:radial-gradient(circle at 55% 52%,rgba(78,209,176,.18),transparent 28%),linear-gradient(145deg,#061e28,#0b4546 68%,#0d5c4d)}.kumul-card-art>img{position:absolute;left:50%;top:50%;width:74%;height:98%;object-fit:contain;transform:translate(-50%,-50%);opacity:.18;filter:brightness(2) saturate(.25)}.kumul-mini-core{position:absolute;left:50%;top:48%;width:82px;height:58px;border:1px solid rgba(158,241,218,.25);border-radius:14px;background:rgba(6,42,47,.86);box-shadow:0 10px 24px rgba(0,0,0,.15),0 0 24px rgba(103,228,196,.11);transform:translate(-50%,-50%);display:flex;flex-direction:column;align-items:center;justify-content:center;color:#eafff8;transition:filter .3s}.kumul-mini-core:after{content:"";position:absolute;inset:-8px;border:1px solid rgba(126,235,206,.16);border-radius:18px;opacity:.2;transform:scale(.94);pointer-events:none;animation:dpCoreBreath 4.8s ease-in-out infinite}.kumul-mini-core small{font-size:4.7px;letter-spacing:.16em;color:#82dcc3}.kumul-mini-core b{font-family:"Space Grotesk";font-size:13px;line-height:1;margin-top:2px}.kumul-mini-core>i{position:absolute;width:5px;height:5px;border-radius:50%;right:9px;top:9px;background:#7ce3c5;box-shadow:0 0 9px #7ce3c5;animation:dpCoreLight 2.4s ease-in-out infinite}.kumul-rack{position:absolute;width:36px;height:52px;padding:5px;border:1px solid rgba(153,233,213,.15);border-radius:8px;background:#123b42}.kumul-rack i{display:block;height:8px;margin-bottom:4px;border-radius:2px;background:linear-gradient(90deg,#235966 0 75%,#8ce8cf 76% 83%,#17434b 84%);animation:dpRackLight 3.1s ease-in-out infinite}.kumul-rack i:nth-child(2){animation-delay:.45s}.kumul-rack i:nth-child(3){animation-delay:.9s}.kr1{left:16%;top:24%;transform:rotate(-5deg)}.kr2{right:14%;top:26%;transform:rotate(5deg)}.kr2 i{animation-delay:.75s}.kr2 i:nth-child(2){animation-delay:1.2s}.kr2 i:nth-child(3){animation-delay:1.65s}.kumul-route{position:absolute;height:1px;background:linear-gradient(90deg,transparent,#8ee8cf,transparent);transform-origin:left}.ka{left:24%;top:47%;width:100px;transform:rotate(6deg)}.kb{left:52%;top:50%;width:95px;transform:rotate(-9deg)}.kumul-packet{position:absolute;width:6px;height:6px;border-radius:2px;background:#dffcf4;box-shadow:0 0 9px #7ce3c5;opacity:0}.kp1{left:23%;top:43%;animation:dpPacketA 3.2s cubic-bezier(.4,0,.2,1) infinite}.kp2{right:23%;top:42%;animation:dpPacketB 3.4s cubic-bezier(.4,0,.2,1) infinite .55s}.digital-kumul:hover .kumul-mini-core,.digital-kumul:focus-visible .kumul-mini-core{filter:brightness(1.08)}.digital-kumul:hover .kumul-mini-core:after,.digital-kumul:focus-visible .kumul-mini-core:after{animation-duration:2.8s}.digital-kumul:hover .kumul-rack i,.digital-kumul:focus-visible .kumul-rack i{animation-duration:1.9s}
@keyframes dpPacketA{0%{left:23%;top:43%;opacity:0;transform:scale(.72)}12%{opacity:.92}72%{left:47%;top:49%;opacity:1;transform:scale(1)}88%,100%{left:49%;top:49%;opacity:0;transform:scale(.42)}}
@keyframes dpPacketB{0%{right:23%;top:42%;opacity:0;transform:scale(.72)}12%{opacity:.92}72%{right:44%;top:49%;opacity:1;transform:scale(1)}88%,100%{right:47%;top:49%;opacity:0;transform:scale(.42)}}
@keyframes dpRackLight{0%,100%{filter:brightness(.9);opacity:.8}50%{filter:brightness(1.22);opacity:1}}
@keyframes dpCoreLight{0%,100%{opacity:.62;box-shadow:0 0 5px #7ce3c5}50%{opacity:1;box-shadow:0 0 11px #7ce3c5}}
@keyframes dpCoreBreath{0%,100%{opacity:.14;transform:scale(.94)}50%{opacity:.42;transform:scale(1.04)}}

/* T-Cash mini visual: a single Kina token travels phone-to-phone, then the receiver confirms. */
.tcash-card-art{background:radial-gradient(circle at 50% 50%,rgba(101,215,255,.16),transparent 30%),linear-gradient(145deg,#07304a,#0875c9 66%,#1496df)}.tcash-phone{position:absolute;top:18px;width:49px;height:74px;border:2px solid rgba(255,255,255,.83);border-radius:12px;background:rgba(7,45,73,.38);box-shadow:0 12px 24px rgba(0,0,0,.15);display:flex;flex-direction:column;align-items:center;justify-content:center;color:#fff}.tcash-phone:before{content:"";position:absolute;top:5px;width:15px;height:2px;border-radius:999px;background:rgba(255,255,255,.34)}.tcash-phone.left{left:18%}.tcash-phone.right{right:18%}.tcash-phone.right:after{content:"";position:absolute;inset:-5px;border:1px solid rgba(205,244,255,.65);border-radius:15px;opacity:0;transform:scale(.9);pointer-events:none;animation:dpCashConfirm 4.2s ease-out infinite}.tcash-phone b{font-family:"Space Grotesk";font-size:18px;line-height:1}.tcash-phone small{font-size:4.8px;letter-spacing:.1em;margin-top:4px;color:#bdeaff}.tcash-link{position:absolute;left:34%;right:34%;top:50%;height:1px;background:rgba(210,246,255,.32)}.tcash-link span{position:absolute;inset:-5px 0;border-top:1px dashed rgba(210,246,255,.22)}.tcash-link i{position:absolute;right:-4px;top:-10px;color:#d8f7ff;font-size:14px;font-style:normal}.tcash-token{position:absolute;z-index:3;left:35%;top:44%;width:28px;height:28px;border-radius:50%;background:#fff;color:#0875c9;display:grid;place-items:center;font-family:"Space Grotesk";font-size:13px;font-weight:800;box-shadow:0 0 0 6px rgba(255,255,255,.09),0 8px 22px rgba(0,0,0,.15);animation:dpCash 4.2s cubic-bezier(.4,0,.2,1) infinite}.digital-tcash:hover .tcash-token,.digital-tcash:focus-visible .tcash-token{animation-duration:2.9s}.digital-tcash:hover .tcash-phone.right:after,.digital-tcash:focus-visible .tcash-phone.right:after{animation-duration:2.9s}.digital-tcash:hover .tcash-phone.right,.digital-tcash:focus-visible .tcash-phone.right{box-shadow:0 12px 24px rgba(0,0,0,.15),0 0 23px rgba(188,239,255,.24)}
@keyframes dpCash{0%{left:35%;transform:scale(.8);opacity:0}12%{opacity:.72}48%{left:58%;transform:scale(1);opacity:1}58%,100%{left:58%;transform:scale(.86);opacity:0}}
@keyframes dpCashConfirm{0%,43%{opacity:0;transform:scale(.9)}50%{opacity:.62;transform:scale(1)}64%{opacity:0;transform:scale(1.12)}100%{opacity:0;transform:scale(1.12)}}

@media(max-width:1050px) and (min-width:821px){.digital-png-card{height:258px}.digital-card-copy p{font-size:7.4px}.digital-card-meta span{font-size:4.8px}}
@media(max-width:820px){.digital-png-rail{padding:34px 0 40px}.digital-png-intro{display:block;margin-bottom:15px}.digital-png-intro p{margin-top:9px;font-size:10px}.digital-png-cards{display:flex;gap:10px;overflow-x:auto;padding:2px 1px 12px;scroll-snap-type:x mandatory}.digital-png-card{flex:0 0 min(84vw,390px);height:250px;scroll-snap-align:start}.digital-png-cards::-webkit-scrollbar{height:4px}.digital-png-cards::-webkit-scrollbar-thumb{background:rgba(8,117,201,.2);border-radius:999px}}
@media(prefers-reduced-motion:reduce){.digital-png-rail .reveal{opacity:1!important;transform:none!important;transition:none!important;transition-delay:0s!important}.digital-png-card,.digital-card-art,.sl-orbit,.sl-beacon,.sl-beam,.sl-mini-sat,.sl-dish,.kumul-mini-core,.kumul-mini-core:after,.kumul-mini-core>i,.kumul-rack i,.kumul-packet,.tcash-token,.tcash-phone.right:after{animation:none!important;transition:none!important}.digital-png-card:hover,.digital-png-card:focus-visible{transform:none!important}.digital-png-cards:has(.digital-png-card:hover) .digital-png-card:not(:hover){opacity:1!important;filter:none!important}}

'''

new_text = text[:start] + css + text[end:]
outside_after = new_text[:start] + new_text[new_text.index('</style>', start):]
if outside_after != outside_before:
    raise SystemExit('Patch escaped Digital PNG CSS block')

# Guard the compact geometry and responsive rail behavior explicitly.
required = [
    '.digital-png-card{--dx:0px;--dy:0px;position:relative;min-width:0;height:250px',
    'grid-template-columns:repeat(3,minmax(0,1fr))',
    '.digital-png-card{flex:0 0 min(84vw,390px);height:250px;scroll-snap-align:start}',
    'scroll-snap-type:x mandatory',
]
for needle in required:
    if needle not in new_text:
        raise SystemExit(f'Compact layout guard missing: {needle}')

path.write_text(new_text, encoding='utf-8')
print('Refined Digital PNG motion only; all content outside its CSS block is byte-for-byte unchanged')
