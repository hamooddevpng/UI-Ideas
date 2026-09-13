from pathlib import Path
p=Path('42-base.html')
s=p.read_text()
old="const travel=Math.min(1,elapsed/laser.duration);"
new="const travel=Math.max(0,Math.min(1,elapsed/laser.duration));"
if old not in s:
    raise SystemExit('expected canvas laser travel expression not found')
p.write_text(s.replace(old,new,1))
