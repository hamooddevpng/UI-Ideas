from pathlib import Path
import re
import subprocess

p = Path('41.html')
s = p.read_text(encoding='utf-8')

old_css = '[data-react]{--rx:0px;--ry:0px;translate:var(--rx) var(--ry);will-change:translate}'
new_css = '[data-react],.proximity-float{--rx:0px;--ry:0px;--px:0px;--py:0px;translate:calc(var(--rx) + var(--px)) calc(var(--ry) + var(--py));will-change:translate}'
if old_css not in s:
    raise SystemExit('Expected Design 41 data-react CSS marker was not found. Refusing to patch.')
s = s.replace(old_css, new_css, 1)

motion_css = "\n/* Design 10 inspired ambient proximity field. This composes with data-react instead of replacing it. */\n@media(hover:none),(pointer:coarse){.proximity-float{--px:0px!important;--py:0px!important}}\n@media(prefers-reduced-motion:reduce){.proximity-float{--px:0px!important;--py:0px!important}}\n"
if 'Design 10 inspired ambient proximity field' not in s:
    if '</style>' not in s:
        raise SystemExit('Closing style tag not found.')
    s = s.replace('</style>', motion_css + '</style>', 1)

marker = "const slides=qa('.hero-slide')"
if marker not in s:
    raise SystemExit('Current Design 41 carousel JS marker not found. Refusing to patch.')
if 'Design 10 style global depth field' in s:
    raise SystemExit('Proximity field already exists. Refusing duplicate patch.')

proximity_js = r'''
// Design 10 style global depth field: nearby UI gently drifts with the pointer.
// It writes only --px/--py, so the existing hover interpolation keeps ownership of --rx/--ry.
if(fine&&!reduce){
  const proximityGroups=[
    ['.brand',-5],
    ['.nav a',4],
    ['.header-actions button,.header-actions a',-4],
    ['.hero-arrow,.hero-dot',4],
    ['.quick-action',6],
    ['.offer-feature',-5],
    ['.offer-card',5],
    ['.service-row',4],
    ['.service-photo',-5],
    ['.segment-tab',4],
    ['.enterprise-links button',-4],
    ['.story-main,.story-small',-5],
    ['.story-step',5],
    ['.notice-head',3],
    ['.news-card',-4],
    ['.command',4],
    ['.support-panel',-4],
    ['.footer-col button,.logo-plate',3],
    ['.help-fab',5]
  ];
  const proximityItems=[];
  proximityGroups.forEach(([selector,baseDepth])=>{
    qa(selector).forEach((el,i)=>{
      if(el.closest('.drawer,.search-overlay'))return;
      el.classList.add('proximity-float');
      const depth=baseDepth*(i%2?-.82:1);
      proximityItems.push({el,depth,phase:(proximityItems.length%9)*.53,x:0,y:0,tx:0,ty:0});
    });
  });
  let proximityTick=0;
  const proximityFrame=()=>{
    proximityTick+=.016;
    const vw=Math.max(1,innerWidth),vh=Math.max(1,innerHeight);
    proximityItems.forEach(o=>{
      const r=o.el.getBoundingClientRect();
      if(r.bottom<-140||r.top>vh+140||r.right<-140||r.left>vw+140){
        o.tx=0;o.ty=0;
      }else{
        const ex=r.left+r.width/2,ey=r.top+r.height/2;
        const dx=mx-ex,dy=my-ey;
        const radius=Math.max(240,Math.min(430,Math.max(r.width,r.height)*1.25+180));
        const dist=Math.hypot(dx,dy);
        const near=Math.max(0,1-dist/radius);
        const nx=Math.max(-1,Math.min(1,dx/radius));
        const ny=Math.max(-1,Math.min(1,dy/radius));
        const d=o.depth;
        const globalX=((mx/vw)-.5)*2*d*.34;
        const globalY=((my/vh)-.5)*2*d*.24;
        const localX=nx*Math.abs(d)*.78*near;
        const localY=ny*Math.abs(d)*.56*near;
        const direction=d<0?-1:1;
        const idle=Math.sin(proximityTick*.55+o.phase)*Math.min(.9,Math.abs(d)*.12);
        o.tx=globalX+localX*direction+idle;
        o.ty=globalY+localY*direction-idle*.35;
      }
      o.x+=(o.tx-o.x)*.045;
      o.y+=(o.ty-o.y)*.045;
      o.el.style.setProperty('--px',o.x.toFixed(2)+'px');
      o.el.style.setProperty('--py',o.y.toFixed(2)+'px');
    });
    requestAnimationFrame(proximityFrame);
  };
  proximityFrame();
}
'''

s = s.replace(marker, proximity_js + marker, 1)
p.write_text(s, encoding='utf-8')

s2 = p.read_text(encoding='utf-8')
required = [
    'Design 10 style global depth field',
    'proximity-float',
    '--px',
    '--py',
    marker,
    'data-action="recharge"',
    'data-segment="government"',
    'data-search-open',
    'assets/brand/telikom-logo.png',
]
for token in required:
    if token not in s2:
        raise SystemExit(f'Missing required token after patch: {token}')
if s2.count('<script>') != s2.count('</script>'):
    raise SystemExit('Script tag count mismatch')
if s2.count('<style>') != s2.count('</style>'):
    raise SystemExit('Style tag count mismatch')

scripts = re.findall(r'<script>(.*?)</script>', s2, re.S)
if not scripts:
    raise SystemExit('No inline script found')
js_path = Path('/tmp/design41.js')
js_path.write_text('\n'.join(scripts), encoding='utf-8')
subprocess.run(['node', '--check', str(js_path)], check=True)
print('Design 41 proximity patch validated:', p.stat().st_size, 'bytes')
