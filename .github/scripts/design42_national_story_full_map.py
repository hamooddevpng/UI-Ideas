from pathlib import Path
import re

p=Path('42.html')
s=p.read_text()
marker='/* Design 42: full-section province network + remote vignette */'
if marker in s:
    raise SystemExit('pass already present')

# National Story: remove the external island/coast wallpaper and let the verified 22-province SVG become the section artwork.
s=s.replace('<section class="png-story png-live" id="png-story">','<section class="png-story png-live national-story-map" id="png-story">',1)
s,n=re.subn(r'\n\s*<img class="png-story-photo"[^>]+>','',s,count=1)
if n!=1:
    raise SystemExit(f'national story wallpaper removal count {n}')

# Make the live connectivity read as random province-to-province laser firing instead of a uniform always-on mesh.
old="""      surgeTimer=setInterval(()=>{\n        if(!section.matches(':hover')&&document.hidden)return;\n        links.forEach(l=>l.classList.remove('surge'));nodes.forEach(n=>n.classList.remove('hot'));\n        const start=Math.floor(Math.random()*links.length);for(let j=0;j<4;j++)links[(start+j*3)%links.length]?.classList.add('surge');\n        for(let j=0;j<5;j++)nodes[(start+j*4)%nodes.length]?.classList.add('hot');\n      },1700);"""
new="""      const fireRandom=()=>{\n        if(document.hidden){surgeTimer=setTimeout(fireRandom,900);return}\n        links.forEach(l=>l.classList.remove('surge'));nodes.forEach(n=>n.classList.remove('hot'));\n        const shots=1+Math.floor(Math.random()*3),picked=new Set();\n        while(picked.size<Math.min(shots,links.length))picked.add(Math.floor(Math.random()*links.length));\n        picked.forEach((idx,j)=>{\n          links[idx]?.classList.add('surge');\n          nodes[(idx*3+j)%nodes.length]?.classList.add('hot');\n          nodes[(idx*7+j+5)%nodes.length]?.classList.add('hot');\n        });\n        setTimeout(()=>{picked.forEach(idx=>links[idx]?.classList.remove('surge'))},760);\n        surgeTimer=setTimeout(fireRandom,520+Math.random()*1180);\n      };\n      surgeTimer=setTimeout(fireRandom,420+Math.random()*700);"""
if old not in s:
    raise SystemExit('old surge timer block not found')
s=s.replace(old,new,1)

css=r'''

/* Design 42: full-section province network + remote vignette */
/* Remote Connectivity: subtle edge vignette so the satellite/dish stay readable without burying the Highlands photo. */
.scene-remote:after{
  background:
    linear-gradient(90deg,rgba(4,28,40,.42) 0%,rgba(4,28,40,.14) 22%,rgba(4,28,40,.025) 51%,rgba(4,28,40,.10) 76%,rgba(4,28,40,.28) 100%),
    linear-gradient(180deg,rgba(4,28,40,.13) 0%,transparent 24%,transparent 76%,rgba(4,28,40,.10) 100%)!important;
}

/* National Story: the map itself is the background artwork, not a card inside the section. */
.national-story-map{
  background:
    radial-gradient(circle at 78% 42%,rgba(28,160,232,.16),transparent 27%),
    linear-gradient(118deg,#082735 0%,#0a3b49 48%,#0d5660 100%)!important;
  isolation:isolate;
}
.national-story-map:after{
  z-index:5!important;
  background:linear-gradient(90deg,rgba(4,25,34,.76) 0%,rgba(4,25,34,.52) 28%,rgba(4,25,34,.13) 47%,rgba(4,25,34,.02) 72%,rgba(4,25,34,.12) 100%)!important;
  pointer-events:none;
}
.national-story-map .png-story-wash,
.national-story-map .png-story-glow{display:none!important}
.national-story-map .story-copy{
  z-index:12!important;
  padding-right:59%!important;
}
.national-story-map .story-copy p{color:#dff3f8!important;max-width:480px}
.national-story-map .story-marker{background:rgba(6,37,49,.46)!important;backdrop-filter:blur(8px)}

.national-story-map .national-map-card{
  position:absolute!important;
  inset:0!important;
  width:100%!important;
  height:100%!important;
  min-height:0!important;
  transform:none!important;
  border:0!important;
  border-radius:0!important;
  background:transparent!important;
  box-shadow:none!important;
  backdrop-filter:none!important;
  overflow:hidden!important;
  pointer-events:none;
  z-index:4!important;
}
.national-story-map .national-map-card:before,
.national-story-map .national-map-card:after{display:none!important}
.national-story-map .national-map-head{
  left:auto!important;
  right:max(34px,calc((100vw - 1380px)/2))!important;
  top:32px!important;
  width:auto!important;
  z-index:9!important;
  pointer-events:none;
}
.national-story-map .national-map-head>div:first-child{display:none!important}
.national-story-map .national-map-counter{
  min-width:88px!important;
  padding:10px 12px!important;
  border:1px solid rgba(178,235,250,.26)!important;
  background:rgba(5,43,55,.55)!important;
  backdrop-filter:blur(12px)!important;
  box-shadow:0 12px 30px rgba(2,21,29,.12)!important;
}
.national-story-map .national-map-counter b{color:#fff!important}
.national-story-map .national-map-counter span{color:#aeeaff!important}
.national-story-map .national-map-stage{
  position:absolute!important;
  left:35%!important;
  right:-1%!important;
  top:2%!important;
  bottom:2%!important;
  border-radius:0!important;
  overflow:visible!important;
  pointer-events:auto!important;
  z-index:3!important;
}
.national-story-map .national-map-backdrop{
  inset:0!important;
  width:100%!important;
  height:100%!important;
  object-fit:contain!important;
  opacity:.66!important;
  filter:brightness(1.04) saturate(.88) drop-shadow(0 18px 42px rgba(0,12,18,.17))!important;
  mix-blend-mode:screen;
}
.national-story-map .national-map-overlay{
  inset:0!important;
  width:100%!important;
  height:100%!important;
  z-index:4!important;
}
.national-story-map .national-mesh-link{
  stroke:#75dcff!important;
  opacity:.09!important;
  stroke-width:1.05!important;
  stroke-dasharray:2 10!important;
  animation-duration:4.4s!important;
}
.national-story-map .national-mesh-link.long{stroke:#b7f0ff!important;opacity:.07!important}
.national-story-map .national-mesh-link.surge{
  opacity:.98!important;
  stroke:#d9f8ff!important;
  stroke-width:2.55!important;
  stroke-dasharray:18 7!important;
  animation:nationalLaserShot .76s cubic-bezier(.17,.74,.18,1) both!important;
}
@keyframes nationalLaserShot{
  0%{opacity:0;stroke-dashoffset:50}
  15%{opacity:1}
  72%{opacity:.95}
  100%{opacity:0;stroke-dashoffset:-80}
}
.national-story-map .national-mesh-node .node-halo{stroke:#8be5ff!important;fill:rgba(117,220,255,.07)!important;opacity:.34!important}
.national-story-map .national-mesh-node .node-dot{fill:#e9fbff!important;stroke:#24b8ed!important;filter:url(#nationalLaserGlow)}
.national-story-map .national-mesh-node.hot .node-dot{fill:#fff!important}
.national-story-map .national-packet{fill:#fff!important;stroke:#5ed8ff!important}
.national-story-map .national-pointer-laser{stroke:#d8f8ff!important;stroke-width:2.05!important}
.national-story-map .national-pointer-core{fill:#fff!important;stroke:#42cff8!important}
.national-story-map .national-map-foot{
  left:auto!important;
  right:max(36px,calc((100vw - 1380px)/2))!important;
  bottom:24px!important;
  width:auto!important;
  gap:12px!important;
  z-index:9!important;
  color:#b6e8f5!important;
}
.national-story-map .national-map-foot span:first-child{display:none!important}
.national-story-map .national-map-foot span:last-child{color:#c8f3ff!important}

@media(max-width:1050px) and (min-width:821px){
  .national-story-map .story-copy{padding-right:55%!important}
  .national-story-map .national-map-stage{left:38%!important;right:-5%!important}
}
@media(max-width:820px){
  .scene-remote:after{background:linear-gradient(90deg,rgba(4,28,40,.44),rgba(4,28,40,.08) 52%,rgba(4,28,40,.24))!important}
  .national-story-map{min-height:850px!important}
  .national-story-map .story-copy{padding-right:0!important;padding-top:64px!important}
  .national-story-map .national-map-stage{left:-8%!important;right:-8%!important;top:305px!important;bottom:26px!important}
  .national-story-map .national-map-head{top:286px!important;right:18px!important}
  .national-story-map .national-map-foot{right:18px!important;bottom:18px!important}
  .national-story-map:after{background:linear-gradient(180deg,rgba(4,25,34,.77) 0%,rgba(4,25,34,.38) 34%,rgba(4,25,34,.03) 60%,rgba(4,25,34,.13) 100%)!important}
}
@media(prefers-reduced-motion:reduce){.national-story-map .national-mesh-link.surge{animation:none!important;opacity:.62!important}}
'''

if '</style>' not in s:
    raise SystemExit('style close missing')
s=s.replace('</style>',css+'\n</style>',1)
p.write_text(s)
print('Removed National Story card treatment, promoted map to section artwork, and added Remote vignette')
