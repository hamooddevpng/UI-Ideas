from pathlib import Path

p = Path('42.html')
s = p.read_text(encoding='utf-8')
marker = 'Design 42: simple province lasers v11'
if marker in s:
    raise SystemExit(0)

block = r'''
<style>
/* Design 42: simple province lasers v11 */
#provinceLaserShotsV7,#provinceLaserCssV9{display:none!important}
.province-route-v6,.province-route-glow-v6{display:none!important}
.province-laser-v11{fill:none;stroke-linecap:round;vector-effect:non-scaling-stroke;pointer-events:none;stroke-dasharray:1;stroke-dashoffset:1;animation:provinceLaserDrawV11 var(--laser-dur,1.2s) cubic-bezier(.18,.8,.2,1) forwards}
.province-laser-glow-v11{stroke:#22d7ff;stroke-width:10;opacity:.9;filter:blur(1.2px) drop-shadow(0 0 7px rgba(34,215,255,.95)) drop-shadow(0 0 14px rgba(8,117,201,.7))}
.province-laser-core-v11{stroke:#fff;stroke-width:2.7;opacity:1;filter:drop-shadow(0 0 2px #fff) drop-shadow(0 0 5px #63e8ff)}
@keyframes provinceLaserDrawV11{
  0%{stroke-dashoffset:1;opacity:0}
  8%{opacity:1}
  72%{stroke-dashoffset:0;opacity:1}
  84%{stroke-dashoffset:0;opacity:1}
  100%{stroke-dashoffset:0;opacity:0}
}
</style>
<script>
// Design 42: simple province lasers v11
(()=>{
  const NS='http://www.w3.org/2000/svg';
  const boot=()=>{
    const network=document.getElementById('provinceNetworkV6');
    if(!network){setTimeout(boot,100);return}
    if(document.getElementById('provinceLaserLayerV11'))return;

    const nodeEls=[...network.querySelectorAll('.province-node-v6')];
    if(nodeEls.length<2){setTimeout(boot,100);return}

    const parseNode=el=>{
      const raw=el.getAttribute('transform')||'';
      const m=raw.match(/translate\(\s*([-\d.]+)[ ,]+([-\d.]+)\s*\)/);
      if(!m)return null;
      return {x:parseFloat(m[1]),y:parseFloat(m[2]),el};
    };
    const nodes=nodeEls.map(parseNode).filter(Boolean);
    if(nodes.length<2){setTimeout(boot,100);return}

    const layer=document.createElementNS(NS,'g');
    layer.setAttribute('id','provinceLaserLayerV11');
    layer.setAttribute('class','province-laser-layer-v11');
    const nodeGroup=network.lastElementChild;
    if(nodeGroup&&nodeGroup.parentNode===network)network.insertBefore(layer,nodeGroup);else network.appendChild(layer);

    const pickPair=()=>{
      let a,b,d,tries=0;
      do{
        a=nodes[Math.floor(Math.random()*nodes.length)];
        b=nodes[Math.floor(Math.random()*nodes.length)];
        d=a&&b?Math.hypot(a.x-b.x,a.y-b.y):0;
        tries++;
      }while((!a||!b||a===b||d<70||d>470)&&tries<40);
      return a&&b&&a!==b?[a,b]:null;
    };

    const addLine=(a,b,cls,dur)=>{
      const line=document.createElementNS(NS,'line');
      line.setAttribute('x1',a.x);line.setAttribute('y1',a.y);
      line.setAttribute('x2',b.x);line.setAttribute('y2',b.y);
      line.setAttribute('pathLength','1');
      line.setAttribute('class','province-laser-v11 '+cls);
      line.style.setProperty('--laser-dur',dur+'ms');
      layer.appendChild(line);
      return line;
    };

    const shoot=()=>{
      const pair=pickPair();
      if(!pair)return;
      const [a,b]=pair;
      const dur=950+Math.floor(Math.random()*420);
      const glow=addLine(a,b,'province-laser-glow-v11',dur);
      const core=addLine(a,b,'province-laser-core-v11',dur);
      a.el.classList.add('v9-live');
      setTimeout(()=>b.el.classList.add('v9-live'),Math.floor(dur*.68));
      setTimeout(()=>{a.el.classList.remove('v9-live');b.el.classList.remove('v9-live');glow.remove();core.remove()},dur+120);
    };

    shoot();
    setTimeout(shoot,420);
    setTimeout(shoot,900);
    setInterval(()=>{
      shoot();
      if(Math.random()<.35)setTimeout(shoot,180+Math.random()*220);
    },920);
  };
  boot();
})();
</script>
'''

s = s.replace('</body>', block + '\n</body>', 1)
p.write_text(s, encoding='utf-8')
