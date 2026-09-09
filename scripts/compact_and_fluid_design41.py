from pathlib import Path
import re
import subprocess

p = Path('41.html')
s = p.read_text(encoding='utf-8')

# 1) Make proximity motion compose with existing reveal/centering translate rules.
old_rule = '[data-react],.proximity-float{--rx:0px;--ry:0px;--px:0px;--py:0px;translate:calc(var(--rx) + var(--px)) calc(var(--ry) + var(--py));will-change:translate}'
new_rule = '[data-react]{--rx:0px;--ry:0px;translate:var(--rx) var(--ry);will-change:translate}.proximity-float{--px:0px;--py:0px;transform:translate3d(var(--px),var(--py),0);will-change:transform}'
if old_rule not in s:
    raise SystemExit('Current combined proximity rule not found. Refusing unsafe patch.')
s = s.replace(old_rule, new_rule, 1)

# 2) Compact desktop section system. Every major homepage section is <= 80svh.
compact_css = r'''
/* DESIGN 41 / 80VH SECTION RHYTHM */
@media (min-width:901px){
  main>section{height:80svh;max-height:80svh;min-height:0!important;overflow:hidden}
  .landing{height:80svh;min-height:0!important;padding:84px 28px 10px}
  .hero-frame{height:calc(100% - 92px);min-height:0!important;border-radius:26px}
  .quick-rail{height:84px;margin-top:8px;gap:7px}
  .quick-action{padding:10px 14px;grid-template-columns:36px 1fr auto;gap:10px}
  .quick-icon{width:36px;height:36px;font-size:16px}
  .hero-copy{width:min(610px,45vw)}
  .hero-title{font-size:clamp(46px,5.8vw,88px)}
  .hero-copy p{font-size:12px;line-height:1.55;margin-top:14px;max-width:430px}
  .hero-actions{margin-top:14px}
  .hero-side-label{top:18px;right:18px}
  .hero-controls{bottom:16px}

  #offers.section{padding:clamp(28px,4.3vh,46px) 0}
  #offers>.wrap{height:100%;display:grid;grid-template-rows:auto minmax(0,1fr);gap:clamp(18px,2.7vh,30px)}
  .offers-head{margin-bottom:0;gap:48px}
  .section-title{font-size:clamp(42px,5.4vw,78px)}
  .section-copy{font-size:12px;line-height:1.55}
  .offer-deck{height:100%;min-height:0;grid-template-columns:1.25fr .75fr}
  .offer-feature{height:100%;min-height:0}
  .offer-stack{min-height:0;grid-template-rows:1fr 1fr}
  .offer-card{min-height:0;padding:18px}
  .offer-card .thumb{height:42%;margin:-2px -2px 13px}
  .offer-card h3{font-size:clamp(22px,2.4vw,34px);margin:6px 0}
  .offer-card p{line-height:1.45;margin:6px 0}
  .link-arrow{margin-top:9px;padding-top:9px}
  .offer-copy{left:26px;right:26px;bottom:22px}
  .offer-copy h3{font-size:clamp(34px,4.3vw,58px);margin:8px 0 9px}
  .offer-copy p{font-size:11px;line-height:1.5;margin:8px 0}

  #services.section{padding:clamp(28px,4.5vh,48px) 0}
  .service-layout{height:100%;align-items:center;gap:5vw}
  .service-row{padding:clamp(9px,1.4vh,14px) 0}
  .service-row h3{font-size:clamp(27px,3.2vw,46px)}
  .service-stage{position:relative;top:auto;align-self:center}
  .service-photo{height:min(47vh,390px)}
  .service-meta{padding:12px 4px;gap:12px}
  .service-meta h4{font-size:27px}

  .enterprise-grid{height:100%;min-height:0}
  .enterprise-copy{padding:clamp(30px,4.6vh,52px) 6vw}
  .enterprise h2{font-size:clamp(44px,5.9vw,82px)}
  .enterprise-copy p{line-height:1.5;font-size:12px}
  .segment-tabs{margin:16px 0 18px}
  .enterprise-links button{padding:11px 0}
  .enterprise-media{height:100%;min-height:0}

  .story{padding:clamp(28px,4.5vh,48px) 0}
  .story-grid{height:100%;gap:5vw}
  .story-collage{height:min(58vh,480px)}
  .story-copy h2{font-size:clamp(44px,5.8vw,80px)}
  .story-copy>p{font-size:12px;line-height:1.55}
  .story-steps{margin-top:18px}
  .story-step{padding:11px 0}
  .story-badge{width:100px;height:100px}

  .updates{padding:0 0 clamp(22px,3.5vh,38px)}
  .updates .ticker{margin-bottom:clamp(18px,3vh,30px)}
  .updates .ticker-track{padding:10px 0}
  .update-grid{height:calc(100% - 64px);align-items:start;gap:5vw}
  .update-grid h3{font-size:26px;margin:8px 0 14px}
  .notice-head{padding:11px 0}
  .notice-body p{padding-bottom:10px}
  .news-card{height:min(43vh,350px);min-height:0;grid-template-rows:44% 1fr}
  .news-copy{padding:14px}
  .news-copy h4{font-size:20px;margin:7px 0}
  .news-copy p{line-height:1.45;margin:5px 0}

  .support{padding:clamp(28px,4.5vh,48px) 0}
  .support-grid{height:100%;align-items:center;gap:5vw}
  .support h2{font-size:clamp(44px,5.8vw,80px);margin-bottom:14px}
  .support .section-copy{margin:8px 0}
  .command-list{margin-top:18px}
  .command{padding:11px 0}
  .support-panel{position:relative;top:auto;height:min(58vh,460px);min-height:0;padding:28px}
  .support-panel h3{font-size:clamp(34px,4.2vw,56px)}

  footer{padding:44px 0 22px;max-height:80svh}
  .footer-watermark{margin:36px 0 -16px}
}

/* Compact fallback for short laptop screens. */
@media (min-width:901px) and (max-height:720px){
  .landing{padding-top:74px}
  .hero-title{font-size:clamp(42px,5.2vw,72px)}
  .hero-copy p{margin-top:10px}
  .hero-actions{margin-top:10px}
  .quick-rail{height:76px}
  .hero-frame{height:calc(100% - 84px)}
  .service-photo{height:43vh}
  .story-collage{height:52vh}
  .news-card{height:39vh}
  .support-panel{height:52vh}
}

/* On smaller screens keep the 80vh visual rhythm without hiding content: dense sections scroll internally. */
@media (max-width:900px){
  main>section{max-height:80svh;overflow:auto;overscroll-behavior:contain}
  .landing{height:80svh;min-height:0!important}
}
'''
if 'DESIGN 41 / 80VH SECTION RHYTHM' not in s:
    s = s.replace('</style>', compact_css + '\n</style>', 1)

# 3) Replace the previous proximity block with a stronger field that composes via transform.
start = '// Design 10 style global depth field: strong layered proximity motion.'
end = "const slides=qa('.hero-slide')"
pattern = re.compile(re.escape(start) + r'.*?(?=' + re.escape(end) + r')', re.S)
if not pattern.search(s):
    raise SystemExit('Current Design 41 depth block not found. Refusing unsafe patch.')

fluid_js = r'''// Design 10 style global depth field: fluid layered proximity motion.
// Uses transform so it composes with reveal/centering translate instead of being overridden.
if(fine&&!reduce){
  const depthGroups=[
    ['.brand',5],
    ['.nav a',7],
    ['.header-actions button,.header-actions a',-8],
    ['.hero-photo',16],
    ['.hero-copy',-18],
    ['.hero-index',-10],
    ['.hero-title span:nth-child(1)',-14],
    ['.hero-title span:nth-child(2)',-25],
    ['.hero-title span:nth-child(3)',19],
    ['.hero-copy p',-9],
    ['.hero-actions',12],
    ['.hero-side-label',-28],
    ['.hero-orbit',22],
    ['.hero-controls',10],
    ['.quick-action',14],
    ['.quick-icon',-10],
    ['.offers-head>div',-13],
    ['.offers-head>.section-copy',12],
    ['.offer-feature',-15],
    ['.offer-feature .photo',18],
    ['.offer-copy',-11],
    ['.offer-card',14],
    ['.offer-card .thumb',-12],
    ['.service-list',-12],
    ['.service-row',11],
    ['.service-stage',15],
    ['.service-photo',-20],
    ['.service-meta',10],
    ['.enterprise-copy',-16],
    ['.enterprise-copy h2',-11],
    ['.segment-tabs',12],
    ['.enterprise-links',-9],
    ['.enterprise-media',18],
    ['.signal',-22],
    ['.story-collage',16],
    ['.story-main',-22],
    ['.story-small',18],
    ['.story-badge',-28],
    ['.story-copy',-14],
    ['.story-copy h2',-10],
    ['.story-steps',11],
    ['.update-grid>div:first-child',-13],
    ['.update-grid>div:last-child',14],
    ['.notice',9],
    ['.news-card',-14],
    ['.support-grid>div',-15],
    ['.support-panel',17],
    ['.command',9],
    ['.footer-brand',-12],
    ['.footer-col',9],
    ['.logo-plate',-15],
    ['.footer-watermark',18],
    ['.help-fab',24]
  ];
  const depthItems=[];
  depthGroups.forEach(([selector,baseDepth])=>{
    qa(selector).forEach((el,i)=>{
      if(el.closest('.drawer,.search-overlay'))return;
      el.classList.add('proximity-float');
      const depth=baseDepth*(i%2?-.88:1);
      depthItems.push({el,depth,phase:(depthItems.length%11)*.41,x:0,y:0,tx:0,ty:0});
    });
  });
  let fieldX=0,fieldY=0,tick=0;
  const clampField=n=>Math.max(-1,Math.min(1,n));
  const fluidFrame=()=>{
    requestAnimationFrame(fluidFrame);
    tick+=.016;
    const vw=Math.max(1,innerWidth),vh=Math.max(1,innerHeight);
    const targetX=(mx/vw-.5)*2,targetY=(my/vh-.5)*2;
    fieldX+=(targetX-fieldX)*.045;
    fieldY+=(targetY-fieldY)*.045;
    depthItems.forEach(o=>{
      const r=o.el.getBoundingClientRect();
      if(r.bottom<-180||r.top>vh+180||r.right<-180||r.left>vw+180){
        o.tx=0;o.ty=0;
      }else{
        const ex=r.left+r.width/2,ey=r.top+r.height/2;
        const localX=clampField((mx-ex)/Math.max(240,r.width));
        const localY=clampField((my-ey)/Math.max(200,r.height));
        const distance=Math.hypot((mx-ex)/vw,(my-ey)/vh);
        const proximity=Math.max(0,1-Math.min(1,distance*1.48));
        const d=o.depth;
        const idle=Math.sin(tick*.64+o.phase)*Math.min(2.2,Math.abs(d)*.08);
        o.tx=fieldX*d*.78+localX*Math.abs(d)*.42*proximity+idle;
        o.ty=fieldY*d*.54+localY*Math.abs(d)*.31*proximity-idle*.42;
      }
      o.x+=(o.tx-o.x)*.065;
      o.y+=(o.ty-o.y)*.065;
      o.el.style.setProperty('--px',o.x.toFixed(2)+'px');
      o.el.style.setProperty('--py',o.y.toFixed(2)+'px');
    });
  };
  fluidFrame();
}
'''
s = pattern.sub(fluid_js, s, count=1)

p.write_text(s, encoding='utf-8')

# Static checks and JS syntax validation.
out = p.read_text(encoding='utf-8')
for token in [
    'DESIGN 41 / 80VH SECTION RHYTHM',
    'fluid layered proximity motion',
    'transform:translate3d(var(--px),var(--py),0)',
    'height:80svh',
    'const slides=qa(\'.hero-slide\')',
    'data-action="recharge"',
    'data-segment="government"',
    'data-search-open',
    'assets/brand/telikom-logo.png'
]:
    if token not in out:
        raise SystemExit(f'Missing required token after patch: {token}')
if out.count('<script>') != out.count('</script>'):
    raise SystemExit('Script tag mismatch')
if out.count('<style>') != out.count('</style>'):
    raise SystemExit('Style tag mismatch')
scripts = re.findall(r'<script>(.*?)</script>', out, re.S)
Path('/tmp/design41.js').write_text('\n'.join(scripts), encoding='utf-8')
subprocess.run(['node', '--check', '/tmp/design41.js'], check=True)
print('Design 41 compact + fluid patch validated:', p.stat().st_size, 'bytes')
