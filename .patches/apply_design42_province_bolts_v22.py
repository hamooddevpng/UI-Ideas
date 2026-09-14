from pathlib import Path
import re

base_path = Path('42-base.html')
css_path = Path('assets/design42/design42-components.css')
base = base_path.read_text(encoding='utf-8')
css = css_path.read_text(encoding='utf-8')

new_script = r'''<script>
// Design 42: endpoint lasers v12
// Rebuilt after the CSS architecture refactor: a literal 5px HTML bolt travels A -> B.
(()=>{
  if(matchMedia('(prefers-reduced-motion: reduce)').matches)return;
  const boot=()=>{
    const section=document.querySelector('.national-story-map');
    const stage=document.getElementById('nationalMapStage');
    const network=document.getElementById('provinceNetworkV6');
    if(!section||!stage||!network){setTimeout(boot,80);return}
    if(document.getElementById('provinceLaserLayerV12'))return;

    const nodeEls=[...network.querySelectorAll('.province-node-v6')];
    if(nodeEls.length<2){setTimeout(boot,80);return}

    const layer=document.createElement('div');
    layer.id='provinceLaserLayerV12';
    layer.className='province-laser-layer-v12';
    layer.setAttribute('aria-hidden','true');
    stage.appendChild(layer);

    let nodes=[];
    const rebuild=()=>{
      const sr=stage.getBoundingClientRect();
      nodes=nodeEls.map(el=>{
        const dot=el.querySelector('.dot')||el;
        const r=dot.getBoundingClientRect();
        return {el,x:r.left+r.width/2-sr.left,y:r.top+r.height/2-sr.top};
      }).filter(p=>Number.isFinite(p.x)&&Number.isFinite(p.y));
    };
    rebuild();

    const pickPair=()=>{
      if(nodes.length<2)return null;
      for(let tries=0;tries<32;tries++){
        const a=nodes[Math.floor(Math.random()*nodes.length)];
        const b=nodes[Math.floor(Math.random()*nodes.length)];
        if(!a||!b||a===b)continue;
        const d=Math.hypot(b.x-a.x,b.y-a.y);
        if(d>=80&&d<=620)return {a,b,d};
      }
      return {a:nodes[0],b:nodes[1],d:Math.hypot(nodes[1].x-nodes[0].x,nodes[1].y-nodes[0].y)};
    };

    let active=0,visible=true;
    const stats=window.__provinceLaserV12Stats={shots:0,finishes:0,last:null};

    const fire=()=>{
      if(!visible||document.hidden||active>=4)return;
      const pair=pickPair();
      if(!pair)return;
      const {a,b,d}=pair;
      const dx=b.x-a.x,dy=b.y-a.y;
      const angle=Math.atan2(dy,dx)*180/Math.PI;
      const bolt=document.createElement('i');
      bolt.className='province-bolt-v12';
      layer.appendChild(bolt);
      active++;stats.shots++;

      const start=`translate3d(${a.x}px,${a.y}px,0) translate(-50%,-50%) rotate(${angle}deg)`;
      const end=`translate3d(${b.x}px,${b.y}px,0) translate(-50%,-50%) rotate(${angle}deg)`;
      const duration=Math.max(260,Math.min(520,d*.9));

      a.el.classList.add('laser-live');
      setTimeout(()=>a.el.classList.remove('laser-live'),110);
      setTimeout(()=>{
        b.el.classList.add('laser-live');
        setTimeout(()=>b.el.classList.remove('laser-live'),150);
      },Math.max(90,duration-70));

      const anim=bolt.animate([
        {transform:start,opacity:0,offset:0},
        {transform:start,opacity:1,offset:.04},
        {transform:end,opacity:1,offset:.94},
        {transform:end,opacity:0,offset:1}
      ],{duration,easing:'linear',fill:'forwards'});

      stats.last={from:{x:a.x,y:a.y},to:{x:b.x,y:b.y},distance:d,duration};
      anim.onfinish=()=>{bolt.remove();active=Math.max(0,active-1);stats.finishes++};
      anim.oncancel=()=>{bolt.remove();active=Math.max(0,active-1)};
    };

    const tick=()=>{
      if(visible&&!document.hidden){
        fire();
        if(Math.random()>.48)setTimeout(fire,95);
      }
      setTimeout(tick,230+Math.random()*150);
    };

    if('ResizeObserver' in window)new ResizeObserver(rebuild).observe(stage);
    else addEventListener('resize',rebuild,{passive:true});
    if('IntersectionObserver' in window)new IntersectionObserver(([entry])=>{visible=entry.isIntersecting;if(visible)rebuild()},{threshold:.03}).observe(section);
    document.addEventListener('visibilitychange',()=>{if(!document.hidden)rebuild()});

    setTimeout(()=>{fire();setTimeout(fire,120);tick()},180);
  };
  boot();
})();
</script>'''

pattern = r'<script>\s*// Design 42: endpoint lasers v12[\s\S]*?</script>'
base, n = re.subn(pattern, new_script, base, count=1)
if n != 1:
    raise SystemExit(f'expected one endpoint laser runtime, replaced {n}')

new_css = r'''/* Design 42: laser tuning v13 */
/* Canonical province laser presentation for the active endpoint v12 runtime. */
.province-laser-layer-v12{position:absolute;inset:0;z-index:30;pointer-events:none;overflow:hidden}
.province-bolt-v12{position:absolute;left:0;top:0;width:5px;height:1.5px;border-radius:999px;background:#006fd6;opacity:0;transform-origin:50% 50%;will-change:transform,opacity;box-shadow:none}
.province-node-v6.laser-live .halo{fill:rgba(37,211,255,.20);stroke:#1bbce9;stroke-width:1.6;filter:none}
.province-node-v6.laser-live .dot{fill:#fff;stroke:#007fc4;filter:none}
@media(prefers-reduced-motion:reduce){.province-laser-layer-v12{display:none!important}}
'''

css_pattern = r'/\* Design 42: laser tuning v13 \*/[\s\S]*\Z'
css, n = re.subn(css_pattern, new_css, css, count=1)
if n != 1:
    raise SystemExit(f'expected one laser tuning block, replaced {n}')

base_path.write_text(base, encoding='utf-8')
css_path.write_text(css, encoding='utf-8')
print('updated active v12 runtime and component laser CSS')
