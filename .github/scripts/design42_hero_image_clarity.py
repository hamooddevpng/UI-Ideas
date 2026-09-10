from pathlib import Path

p=Path('42.html')
s=p.read_text()
marker='/* Design 42: hero image clarity only */'
if marker in s:
    raise SystemExit('hero clarity pass already present')

old='''<div class="scene scene-remote"><img class="hero-atmos hero-island" src="assets/design42/png-remote-coast.jpg" alt="" aria-hidden="true"><div class="remote-sky"><div class="ridge far"></div><div class="ridge mid"></div><div class="ridge near"></div></div></div>'''
new='''<div class="scene scene-remote"><img class="hero-atmos hero-island" src="assets/design42/png-highlands-landscape.png" alt="" aria-hidden="true"><div class="remote-sky"><div class="ridge far"></div><div class="ridge mid"></div><div class="ridge near"></div></div></div>'''
if old not in s:
    raise SystemExit('remote hero markup not found')
s=s.replace(old,new,1)

css=r'''

/* Design 42: hero image clarity only */
/* Self Care: keep the existing PNG image, reveal it instead of burying it. */
.scene-phone{
  background:linear-gradient(115deg,#0b3445 0%,#0d4c62 52%,#167494 100%)!important;
}
.scene-phone .hero-people{
  opacity:.54!important;
  object-position:69% 46%!important;
  filter:saturate(1.03) contrast(1.02) brightness(.94)!important;
  transform:scale(1.01)!important;
  -webkit-mask-image:linear-gradient(90deg,transparent 0%,rgba(0,0,0,.30) 25%,rgba(0,0,0,.88) 53%,#000 72%)!important;
  mask-image:linear-gradient(90deg,transparent 0%,rgba(0,0,0,.30) 25%,rgba(0,0,0,.88) 53%,#000 72%)!important;
}
.scene-phone:after{
  background:linear-gradient(90deg,rgba(5,31,43,.68) 0%,rgba(5,31,43,.43) 34%,rgba(5,31,43,.13) 57%,rgba(5,31,43,.02) 78%)!important;
}

/* Remote Connectivity: use the PNG Highlands photograph and remove the drawn mountain silhouettes. */
.scene-remote{
  background:#a9d0d8!important;
}
.scene-remote .hero-island{
  opacity:.84!important;
  object-position:center 54%!important;
  filter:saturate(1.05) contrast(1.03) brightness(.96)!important;
  transform:scale(1.012)!important;
}
.scene-remote .ridge{display:none!important}
.scene-remote:after{
  background:linear-gradient(90deg,rgba(4,28,40,.62) 0%,rgba(4,28,40,.40) 28%,rgba(4,28,40,.15) 50%,rgba(4,28,40,.02) 72%,transparent 88%)!important;
}

@media(max-width:820px){
  .scene-phone .hero-people{opacity:.44!important;object-position:64% 47%!important}
  .scene-remote .hero-island{opacity:.72!important;object-position:58% 52%!important}
}
'''
if '</style>' not in s:
    raise SystemExit('style close missing')
s=s.replace('</style>',css+'\n</style>',1)
p.write_text(s)
print('Applied hero-only image clarity pass')
