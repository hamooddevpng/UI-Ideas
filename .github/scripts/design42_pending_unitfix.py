from pathlib import Path
p=Path('42.html')
s=p.read_text()
repls={
'.png-live{--png-x:0;--png-y:0;':'.png-live{--png-x:0;--png-y:0;--png-tx:0px;--png-ty:0px;--png-gx:50%;--png-gy:50%;',
' transform:translate3d(calc(var(--png-x)*-14px),calc(var(--png-y)*-8px),0) scale(1.035);':' transform:translate3d(var(--png-tx),var(--png-ty),0) scale(1.035);',
'background:radial-gradient(320px circle at calc(50% + var(--png-x)*18%) calc(50% + var(--png-y)*16%),rgba(137,232,255,.16),transparent 74%);':'background:radial-gradient(320px circle at var(--png-gx) var(--png-gy),rgba(137,232,255,.16),transparent 74%);',
'.news-feature{--news-x:0;--news-y:0;position:relative;transform:perspective(1100px) rotateX(calc(var(--news-y)*-1.7deg)) rotateY(calc(var(--news-x)*2.2deg));':'.news-feature{--news-x:0;--news-y:0;--news-rx:0deg;--news-ry:0deg;--news-tx:0px;--news-ty:0px;position:relative;transform:perspective(1100px) rotateX(var(--news-rx)) rotateY(var(--news-ry));',
' transform:translate3d(calc(var(--news-x)*-10px),calc(var(--news-y)*-7px),0) scale(1.03);':' transform:translate3d(var(--news-tx),var(--news-ty),0) scale(1.03);',
'.support-orbit .support-stage{--support-x:0;--support-y:0;min-height:520px;':'.support-orbit .support-stage{--support-x:0;--support-y:0;--support-rx:0px;--support-ry:0px;--core-x:0px;--core-y:0px;min-height:520px;',
'transform:translateY(-50%) translate3d(calc(var(--support-x)*8px),calc(var(--support-y)*6px),0);':'transform:translateY(-50%) translate3d(var(--support-rx),var(--support-ry),0);',
'transform:translate(50%,-50%) translate3d(calc(var(--support-x)*12px),calc(var(--support-y)*9px),0);':'transform:translate(50%,-50%) translate3d(var(--core-x),var(--core-y),0);',
"png.style.setProperty('--png-y',Math.max(-1,Math.min(1,y)).toFixed(3))":"png.style.setProperty('--png-y',Math.max(-1,Math.min(1,y)).toFixed(3));png.style.setProperty('--png-tx',(-x*14).toFixed(2)+'px');png.style.setProperty('--png-ty',(-y*8).toFixed(2)+'px');png.style.setProperty('--png-gx',(50+x*18).toFixed(2)+'%');png.style.setProperty('--png-gy',(50+y*16).toFixed(2)+'%')",
"png.style.setProperty('--png-y','0')":"png.style.setProperty('--png-y','0');png.style.setProperty('--png-tx','0px');png.style.setProperty('--png-ty','0px');png.style.setProperty('--png-gx','50%');png.style.setProperty('--png-gy','50%')",
"newsCard.style.setProperty('--news-y',Math.max(-1,Math.min(1,y)).toFixed(3))":"newsCard.style.setProperty('--news-y',Math.max(-1,Math.min(1,y)).toFixed(3));newsCard.style.setProperty('--news-rx',(y*-1.7).toFixed(2)+'deg');newsCard.style.setProperty('--news-ry',(x*2.2).toFixed(2)+'deg');newsCard.style.setProperty('--news-tx',(-x*10).toFixed(2)+'px');newsCard.style.setProperty('--news-ty',(-y*7).toFixed(2)+'px')",
"newsCard.style.setProperty('--news-y','0')":"newsCard.style.setProperty('--news-y','0');newsCard.style.setProperty('--news-rx','0deg');newsCard.style.setProperty('--news-ry','0deg');newsCard.style.setProperty('--news-tx','0px');newsCard.style.setProperty('--news-ty','0px')",
"stage.style.setProperty('--support-y',Math.max(-1,Math.min(1,y)).toFixed(3));nodes.forEach":"stage.style.setProperty('--support-y',Math.max(-1,Math.min(1,y)).toFixed(3));stage.style.setProperty('--support-rx',(x*8).toFixed(2)+'px');stage.style.setProperty('--support-ry',(y*6).toFixed(2)+'px');stage.style.setProperty('--core-x',(x*12).toFixed(2)+'px');stage.style.setProperty('--core-y',(y*9).toFixed(2)+'px');nodes.forEach",
"stage.style.setProperty('--support-y','0');nodes.forEach":"stage.style.setProperty('--support-y','0');stage.style.setProperty('--support-rx','0px');stage.style.setProperty('--support-ry','0px');stage.style.setProperty('--core-x','0px');stage.style.setProperty('--core-y','0px');nodes.forEach"
}
for old,new in repls.items():
    if old not in s:
        raise SystemExit('unit fix target missing: '+old[:80])
    s=s.replace(old,new,1)
p.write_text(s)
