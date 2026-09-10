from pathlib import Path

p=Path('42.html')
s=p.read_text()
marker='/* Design 42: validated province nodes + light national story */'
if marker in s:
    raise SystemExit('province point pass already present')

old="""    if(raw.length<22)return;\n    points=raw.map(({b},i)=>({i,x:b.x+b.width/2,y:b.y+b.height/2}));\n    linksG.replaceChildren();packetsG.replaceChildren();nodesG.replaceChildren();pointerG.replaceChildren();links=[];nodes=[];pointerLines=[];"""
new="""    if(raw.length<22)return;\n    const root=doc.documentElement;\n    const findInteriorPoint=(el,b)=>{\n      const pt=root.createSVGPoint();\n      const inside=(x,y)=>{\n        pt.x=x;pt.y=y;\n        try{return typeof el.isPointInFill==='function'&&el.isPointInFill(pt)}catch(e){return false}\n      };\n      const cx=b.x+b.width/2,cy=b.y+b.height/2;\n      if(inside(cx,cy))return {x:cx,y:cy};\n      let best=null,bestScore=-1;\n      // Dense, deterministic sampling over the actual province geometry.\n      // This avoids placing a node in water for concave or multi-island provinces.\n      for(let gy=1;gy<=19;gy++){\n        for(let gx=1;gx<=19;gx++){\n          const x=b.x+b.width*(gx/20),y=b.y+b.height*(gy/20);\n          if(!inside(x,y))continue;\n          const edge=Math.min(x-b.x,b.x+b.width-x,y-b.y,b.y+b.height-y);\n          const centerPenalty=Math.hypot(x-cx,y-cy)*.025;\n          const score=edge-centerPenalty;\n          if(score>bestScore){bestScore=score;best={x,y}}\n        }\n      }\n      if(best)return best;\n      // Tiny island fallback: progressively sample more densely until an interior pixel is found.\n      for(let div=30;div<=80;div+=10){\n        for(let gy=1;gy<div;gy++){\n          for(let gx=1;gx<div;gx++){\n            const x=b.x+b.width*(gx/div),y=b.y+b.height*(gy/div);\n            if(inside(x,y))return {x,y};\n          }\n        }\n      }\n      return {x:cx,y:cy};\n    };\n    points=raw.map(({el,b},i)=>({i,...findInteriorPoint(el,b)}));\n    linksG.replaceChildren();packetsG.replaceChildren();nodesG.replaceChildren();pointerG.replaceChildren();links=[];nodes=[];pointerLines=[];"""
if old not in s:
    raise SystemExit('province point block not found')
s=s.replace(old,new,1)

old_node="""      const g=make('g',{class:'national-mesh-node',transform:`translate(${p.x.toFixed(1)} ${p.y.toFixed(1)})`});"""
new_node="""      const g=make('g',{class:'national-mesh-node','data-province-index':i,transform:`translate(${p.x.toFixed(1)} ${p.y.toFixed(1)})`});"""
if old_node not in s:
    raise SystemExit('province node creation not found')
s=s.replace(old_node,new_node,1)

css=r'''

/* Design 42: validated province nodes + light national story */
.national-story-map{
  background:
    radial-gradient(circle at 78% 42%,rgba(50,181,226,.16),transparent 27%),
    linear-gradient(118deg,#f7fcfd 0%,#e9f7fa 44%,#d8eff4 100%)!important;
  color:#102f3f!important;
}
.national-story-map:after{
  background:linear-gradient(90deg,rgba(248,253,254,.97) 0%,rgba(244,251,253,.94) 25%,rgba(235,248,251,.66) 37%,rgba(225,244,249,.13) 52%,rgba(225,244,249,0) 72%)!important;
}
.national-story-map .story-copy{color:#102f3f!important}
.national-story-map .story-copy h2{color:#102f3f!important;text-shadow:none!important}
.national-story-map .story-copy p{color:#496e7d!important;font-weight:500}
.national-story-map .story-copy .kicker,.national-story-map .story-copy>.kicker{color:#0875c9!important}
.national-story-map .story-marker{
  color:#17485c!important;
  border-color:rgba(24,112,143,.24)!important;
  background:rgba(255,255,255,.62)!important;
  box-shadow:0 8px 20px rgba(25,94,119,.055)!important;
}
.national-story-map .national-map-stage{left:30%!important;right:-2%!important;top:1%!important;bottom:1%!important}
.national-story-map .national-map-backdrop{
  opacity:.94!important;
  mix-blend-mode:normal!important;
  filter:saturate(.94) contrast(1.04) drop-shadow(0 18px 42px rgba(48,128,151,.08))!important;
}
.national-story-map .national-map-counter{
  border-color:rgba(19,119,151,.18)!important;
  background:rgba(255,255,255,.72)!important;
  box-shadow:0 12px 30px rgba(27,98,120,.08)!important;
}
.national-story-map .national-map-counter b{color:#143b4d!important}
.national-story-map .national-map-counter span{color:#0875c9!important}
.national-story-map .national-map-foot{color:#4c7d8e!important}
.national-story-map .national-map-foot span:last-child{color:#0875c9!important}
.national-story-map .national-mesh-link{
  stroke:#168fc0!important;
  opacity:.055!important;
  stroke-width:1!important;
}
.national-story-map .national-mesh-link.long{stroke:#0875c9!important;opacity:.04!important}
.national-story-map .national-mesh-link.surge{
  stroke:#0875c9!important;
  stroke-width:3!important;
  opacity:1!important;
  filter:url(#nationalLaserGlow) drop-shadow(0 0 4px rgba(8,117,201,.46))!important;
}
.national-story-map .national-mesh-node{opacity:1!important}
.national-story-map .national-mesh-node .node-halo{
  r:8!important;
  fill:rgba(28,160,232,.11)!important;
  stroke:#38aeda!important;
  stroke-width:1.15!important;
  opacity:.78!important;
}
.national-story-map .national-mesh-node .node-dot{
  r:4.2!important;
  fill:#0875c9!important;
  stroke:#fff!important;
  stroke-width:2.2!important;
  filter:drop-shadow(0 0 5px rgba(8,117,201,.68))!important;
}
.national-story-map .national-mesh-node.hot .node-halo{opacity:1!important}
.national-story-map .national-mesh-node.hot .node-dot{fill:#04a9ea!important;filter:drop-shadow(0 0 8px rgba(8,117,201,.9))!important}
.national-story-map .national-packet{fill:#fff!important;stroke:#0875c9!important;stroke-width:1.4!important;filter:drop-shadow(0 0 5px rgba(8,117,201,.72))!important}
.national-story-map .national-pointer-laser{stroke:#0875c9!important;stroke-width:2.25!important;filter:drop-shadow(0 0 4px rgba(8,117,201,.5))!important}
.national-story-map .national-pointer-core{fill:#fff!important;stroke:#0875c9!important;filter:drop-shadow(0 0 7px rgba(8,117,201,.55))!important}
@media(max-width:1050px) and (min-width:821px){
  .national-story-map .national-map-stage{left:34%!important;right:-5%!important}
}
@media(max-width:820px){
  .national-story-map:after{background:linear-gradient(180deg,rgba(248,253,254,.96) 0%,rgba(242,251,253,.82) 30%,rgba(229,246,250,.16) 52%,rgba(220,242,247,.02) 100%)!important}
  .national-story-map .national-map-stage{left:-8%!important;right:-8%!important;top:305px!important;bottom:26px!important}
  .national-story-map .story-copy h2{color:#102f3f!important}
  .national-story-map .story-copy p{color:#496e7d!important}
}
'''
if '</style>' not in s:
    raise SystemExit('style close missing')
s=s.replace('</style>',css+'\n</style>',1)
p.write_text(s)
print('Installed lighter National Story and geometry-validated province points')
