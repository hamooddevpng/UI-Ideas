from pathlib import Path

path = Path('42-base.html')
text = path.read_text(encoding='utf-8')
marker = 'Design 42: province laser bolt v16'
if marker in text:
    raise SystemExit('v16 laser bolt already present')

block = r'''
<style>
/* Design 42: province laser bolt v16 */
/* Match the hero bolt approach: a literal 5 CSS-pixel element translates from A to B. */
.province-laser-v12{display:none!important}
.province-laser-bolt-layer-v16{position:absolute;inset:0;pointer-events:none;z-index:7;overflow:hidden}
.province-laser-bolt-v16{position:absolute;left:0;top:0;width:5px;height:1.25px;border-radius:999px;background:#079fd2;transform-origin:0 50%;will-change:transform,opacity;opacity:.96;pointer-events:none}
@media(prefers-reduced-motion:reduce){.province-laser-bolt-layer-v16{display:none!important}}
</style>
<script>
// Design 42: province laser bolt v16
(()=>{
  if(matchMedia('(prefers-reduced-motion: reduce)').matches)return;
  const boot=()=>{
    const section=document.querySelector('.national-story-map');
    const network=document.getElementById('provinceNetworkV6');
    if(!section||!network){setTimeout(boot,100);return}
    if(document.getElementById('provinceLaserBoltLayerV16'))return;
    const nodeEls=[...network.querySelectorAll('.province-node-v6')];
    if(nodeEls.length<2){setTimeout(boot,100);return}

    const nodes=nodeEls.map(el=>{
      const m=el.transform.baseVal.consolidate();
      return {el,x:m?m.matrix.e:0,y:m?m.matrix.f:0};
    });

    const pairs=[];
    nodes.forEach((a,i)=>{
      nodes
        .map((b,j)=>({j,d:j===i?Infinity:Math.hypot(b.x-a.x,b.y-a.y)}))
        .sort((p,q)=>p.d-q.d)
        .slice(0,3)
        .forEach(({j})=>{const key=i<j?`${i}:${j}`:`${j}:${i}`;if(!pairs.some(p=>p.key===key))pairs.push({key,a:i,b:j})});
    });

    const layer=document.createElement('div');
    layer.id='provinceLaserBoltLayerV16';
    layer.className='province-laser-bolt-layer-v16';
    section.appendChild(layer);

    const toSectionPoint=node=>{
      const ctm=network.getScreenCTM();
      const rect=section.getBoundingClientRect();
      if(!ctm)return {x:0,y:0};
      return {
        x:ctm.a*node.x+ctm.c*node.y+ctm.e-rect.left,
        y:ctm.b*node.x+ctm.d*node.y+ctm.f-rect.top
      };
    };

    let visible=true;
    if('IntersectionObserver' in window){
      visible=false;
      new IntersectionObserver(([entry])=>{visible=entry.isIntersecting},{threshold:.04}).observe(section);
    }

    const shoot=()=>{
      if(!visible||document.hidden||!pairs.length)return;
      const pair=pairs[Math.floor(Math.random()*pairs.length)];
      const forward=Math.random()>.5;
      const source=nodes[forward?pair.a:pair.b];
      const target=nodes[forward?pair.b:pair.a];
      const a=toSectionPoint(source),b=toSectionPoint(target);
      const dx=b.x-a.x,dy=b.y-a.y;
      if(Math.hypot(dx,dy)<8)return;
      const angle=Math.atan2(dy,dx);
      const bolt=document.createElement('i');
      bolt.className='province-laser-bolt-v16';
      layer.appendChild(bolt);
      const start=`translate3d(${a.x}px,${a.y}px,0) rotate(${angle}rad) translateY(-50%)`;
      const end=`translate3d(${b.x}px,${b.y}px,0) rotate(${angle}rad) translateY(-50%)`;
      const anim=bolt.animate([
        {transform:start,opacity:0,offset:0},
        {transform:start,opacity:.96,offset:.06},
        {transform:end,opacity:.96,offset:.94},
        {transform:end,opacity:0,offset:1}
      ],{duration:190+Math.random()*90,easing:'cubic-bezier(.18,.72,.2,1)',fill:'forwards'});
      anim.onfinish=()=>bolt.remove();
      anim.oncancel=()=>bolt.remove();
    };

    const tick=()=>{
      if(visible&&!document.hidden){shoot();if(Math.random()>.58)setTimeout(shoot,95)}
      setTimeout(tick,360+Math.random()*420);
    };
    setTimeout(()=>{shoot();setTimeout(shoot,120);tick()},260);
  };
  boot();
})();
</script>
'''

text = text.replace('</body>', block + '\n</body>', 1)
path.write_text(text, encoding='utf-8')
