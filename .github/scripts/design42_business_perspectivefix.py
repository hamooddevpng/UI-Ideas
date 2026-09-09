from pathlib import Path
p=Path('42.html')
s=p.read_text()
repls={
"--business-x:0;--business-y:0;min-height:520px":"--business-x:0;--business-y:0;--business-rx:0deg;--business-ry:0deg;--business-tx:0px;--business-ty:0px;min-height:520px",
"transform:perspective(1050px) rotateX(calc(var(--business-y)*-2.2deg)) rotateY(calc(var(--business-x)*3deg))":"transform:perspective(1050px) rotateX(var(--business-rx)) rotateY(var(--business-ry))",
"transform:translate3d(calc(var(--business-x)*5px),calc(var(--business-y)*4px),0)":"transform:translate3d(var(--business-tx),var(--business-ty),0)",
"consoleEl.style.setProperty('--business-x',x.toFixed(3));consoleEl.style.setProperty('--business-y',y.toFixed(3))":"consoleEl.style.setProperty('--business-x',x.toFixed(3));consoleEl.style.setProperty('--business-y',y.toFixed(3));consoleEl.style.setProperty('--business-rx',(-y*2.2).toFixed(2)+'deg');consoleEl.style.setProperty('--business-ry',(x*3).toFixed(2)+'deg');consoleEl.style.setProperty('--business-tx',(x*5).toFixed(2)+'px');consoleEl.style.setProperty('--business-ty',(y*4).toFixed(2)+'px')",
"consoleEl.style.setProperty('--business-x','0');consoleEl.style.setProperty('--business-y','0')":"consoleEl.style.setProperty('--business-x','0');consoleEl.style.setProperty('--business-y','0');consoleEl.style.setProperty('--business-rx','0deg');consoleEl.style.setProperty('--business-ry','0deg');consoleEl.style.setProperty('--business-tx','0px');consoleEl.style.setProperty('--business-ty','0px')"
}
for old,new in repls.items():
    if old not in s:
        raise SystemExit('perspective target not found: '+old[:80])
    s=s.replace(old,new,1)
p.write_text(s)
