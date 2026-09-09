from pathlib import Path
import re, subprocess

p=Path('41.html')
s=p.read_text(encoding='utf-8')

start='// Design 10 style global depth field: nearby UI gently drifts with the pointer.'
end="const slides=qa('.hero-slide')"
if start not in s or end not in s:
    raise SystemExit('Expected current Design 41 proximity markers not found')

new_block=r'''// Design 10 style global depth field: strong layered proximity motion.
// Uses Design 10's normalized pointer interpolation and depth ranges.
if(fine&&!reduce){
  const proximityGroups=[
    ['.brand',3],
    ['.nav a',4],
    ['.header-actions button,.header-actions a',-5],
    ['.hero-copy',-10],
    ['.hero-index',-5],
    ['.hero-title span:nth-child(1)',-6],
    ['.hero-title span:nth-child(2)',-12],
    ['.hero-title span:nth-child(3)',9],
    ['.hero-actions',-5],
    ['.hero-side-label',-24],
    ['.hero-arrow',12],
    ['.hero-dot',-8],
    ['.quick-action',10],
    ['.offers-head',-8],
    ['.section-title',-12],
    ['.offer-feature',-9],
    ['.offer-card',10],
    ['.service-row',-9],
    ['.service-photo',12],
    ['.service-meta',-7],
    ['.enterprise-copy',-10],
    ['.enterprise-copy h2',-14],
    ['.segment-tab',11],
    ['.enterprise-links button',-9],
    ['.enterprise-media',14],
    ['.story-main',-14],
    ['.story-small',18],
    ['.story-badge',-20],
    ['.story-copy',10],
    ['.story-copy h2',-12],
    ['.story-step',9],
    ['.notice-head',-7],
    ['.news-card',10],
    ['.support-grid>div',-10],
    ['.support h2',-13],
    ['.command',8],
    ['.support-panel',13],
    ['.footer-brand',-7],
    ['.footer-col',6],
    ['.logo-plate',-10],
    ['.help-fab',16]
  ];
  const proximityItems=[];
  proximityGroups.forEach(([selector,baseDepth])=>{
    qa(selector).forEach((el,i)=>{
      if(el.closest('.drawer,.search-overlay'))return;
      el.classList.add('proximity-float');
      const depth=baseDepth*(i%2?-.86:1);
      proximityItems.push({el,depth,phase:(proximityItems.length%7)*.37,x:0,y:0});
    });
  });
  let fieldX=0,fieldY=0,proximityTick=0;
  const clampDepth=n=>Math.max(-1,Math.min(1,n));
  const proximityFrame=()=>{
    requestAnimationFrame(proximityFrame);
    proximityTick+=.016;
    const vw=Math.max(1,innerWidth),vh=Math.max(1,innerHeight);
    const targetX=(mx/vw-.5)*2,targetY=(my/vh-.5)*2;
    fieldX+=(targetX-fieldX)*.055;
    fieldY+=(targetY-fieldY)*.055;
    proximityItems.forEach(o=>{
      const r=o.el.getBoundingClientRect();
      if(r.bottom<-160||r.top>vh+160){return}
      const ex=r.left+r.width/2,ey=r.top+r.height/2;
      const localX=clampDepth((mx-ex)/Math.max(260,r.width));
      const localY=clampDepth((my-ey)/Math.max(220,r.height));
      const proximity=Math.max(0,1-Math.min(1,Math.hypot((mx-ex)/vw,(my-ey)/vh)*1.65));
      const d=o.depth;
      const x=fieldX*d*.72+localX*Math.abs(d)*.32*proximity;
      const y=fieldY*d*.48+localY*Math.abs(d)*.24*proximity;
      const idle=Math.sin(proximityTick*.7+o.phase)*Math.min(1.8,Math.abs(d)*.045);
      o.x+=(x+idle-o.x)*.09;
      o.y+=(y-idle*.45-o.y)*.09;
      o.el.style.setProperty('--px',o.x.toFixed(2)+'px');
      o.el.style.setProperty('--py',o.y.toFixed(2)+'px');
    });
  };
  proximityFrame();
}
'''

pattern=re.compile(re.escape(start)+r'.*?(?='+re.escape(end)+r')',re.S)
s2,n=pattern.subn(new_block,s,count=1)
if n!=1:
    raise SystemExit(f'Could not replace proximity block, matches={n}')

# Slightly strengthen the pointer light so movement reads as one coherent field.
s2=s2.replace('radial-gradient(520px circle at var(--mx) var(--my),rgba(26,160,219,.09),transparent 72%)','radial-gradient(440px circle at var(--mx) var(--my),rgba(26,160,219,.12),transparent 72%)',1)

p.write_text(s2,encoding='utf-8')

# Safety checks
out=p.read_text(encoding='utf-8')
for token in ["['.hero-side-label',-24]","['.story-badge',-20]","fieldX+=(targetX-fieldX)*.055","localX*Math.abs(d)*.32*proximity","const slides=qa('.hero-slide')",'data-action="recharge"','data-search-open']:
    if token not in out: raise SystemExit('Missing token: '+token)
if out.count('<script>')!=out.count('</script>'): raise SystemExit('script tag mismatch')
js='\n'.join(re.findall(r'<script>(.*?)</script>',out,re.S))
Path('/tmp/d41.js').write_text(js,encoding='utf-8')
subprocess.run(['node','--check','/tmp/d41.js'],check=True)
print('Design 41 strong depth field validated')
