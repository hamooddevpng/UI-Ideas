from pathlib import Path
p=Path('42.html')
s=p.read_text()
old='<div class="business-console reveal" id="businessConsole" data-route="0">'
new='<div class="business-console" id="businessConsole" data-route="0">'
if old not in s:
    raise SystemExit('business console reveal target not found')
s=s.replace(old,new,1)
p.write_text(s)
