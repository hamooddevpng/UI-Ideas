from pathlib import Path
p=Path('42.html')
s=p.read_text()
old="rows.forEach((row,i)=>{row.addEventListener('pointerenter',()=>{if(!locked)setRoute(i)});row.addEventListener('focus',()=>{if(!locked)setRoute(i)});row.addEventListener('click',()=>setRoute(i,true))});"
new="rows.forEach((row,i)=>{const preview=()=>{if(!locked)setRoute(i)};row.addEventListener('pointerenter',preview);row.addEventListener('mouseenter',preview);row.addEventListener('mouseover',preview);row.addEventListener('focus',preview);row.addEventListener('click',()=>setRoute(i,true))});"
if old not in s:
    raise SystemExit('business route listener block not found')
s=s.replace(old,new,1)
p.write_text(s)
