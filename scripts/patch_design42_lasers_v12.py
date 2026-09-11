from pathlib import Path

p = Path('42.html')
s = p.read_text(encoding='utf-8')
marker = 'Design 42: endpoint lasers v12'
if marker in s:
    raise SystemExit(0)

block = r'''
<style>
/* Design 42: endpoint lasers v12 */
.province-laser-v11{display:none!important}
.province-laser-v12{pointer-events:none;fill:none;stroke-linecap:round;vector-effect:non-scaling-stroke;opacity:1}
.province-laser-v12.glow{stroke:#18d8ff;stroke-width:9;filter:blur(1.2px) drop-shadow(0 0 8px rgba(24,216,255,.95)) drop-shadow(0 0 14px rgba(8,117,201,.7))}
.province-laser-v12.core{stroke:#fff;stroke-width:2.8;filter:drop-shadow(0 0 2px #fff) drop-shadow(0 0 6px #68ecff)}
</style>
<script>
// Design 42: endpoint lasers v12
(()=>{
  const NS='http://www.w3.org/2000/svg';
  const boot=()=>{
    const network=document.getElementById('provinceNetworkV6');
    if(!network){setTimeout(boot,100);return}
    if(document.getElementById('provinceLaserLayerV12'))return;
    const nodeEls=[...network.querySelectorAll('.province-node-v6')];
    if(nodeEls.length<2){setTimeout(boot,100);return}

    const nodes=nodeEls.map(el=>{
      const m=el.transform.baseVal.consolidate();
      return {el,x:m?m.matrix.e:0,y:m?m.matrix.f:0};
    });

    const layer=document.createElementNS(NS,'g');
    layer.id='provinceLaserLayerV12';
    const nodesGroup=network.lastElementChild;
    if(nodesGroup&&nodesGroup.parentNode===network)network.insertBefore(layer,nodesGroup);else network.appendChild(layer);

    const dist=(a,b)=>Math.hypot(a.x-b.x,a.y-b.y);
    const pickPair=()=>{
      for(let i=0;i<30;i++){
        const a=nodes[Math.floor(Math.random()*nodes.length)];
        const b=nodes[Math.floor(Math.random()*nodes.length)];
        if(a===b)continue;
        const d=dist(a,b);
        if(d>55&&d<260)return [a,b];
      }
      return [nodes[0],nodes[1]];
    };

    const makeLine=(a,klass)=>{
      const el=document.createElementNS(NS,'line');
      el.setAttribute('class','province-laser-v12 '+klass);
      el.setAttribute('x1',a.x);el.setAttribute('y1',a.y);
      el.setAttribute('x2',a.x);el.setAttribute('y2',a.y);
      layer.appendChild(el);
      return el;
    };

    const fire=()=>{
      const [a,b]=pickPair();
      const glow=makeLine(a,'glow');
      const core=makeLine(a,'core');
      const duration=520+Math.random()*260;
      const started=performance.now();

      const frame=now=>{
        const t=Math.min(1,(now-started)/duration);
        const e=1-Math.pow(1-t,3);
        const x=a.x+(b.x-a.x)*e;
        const y=a.y+(b.y-a.y)*e;
        glow.setAttribute('x2',x);glow.setAttribute('y2',y);
        core.setAttribute('x2',x);core.setAttribute('y2',y);
        if(t<1){requestAnimationFrame(frame);return}
        setTimeout(()=>{
          glow.style.transition='opacity 180ms ease';
          core.style.transition='opacity 180ms ease';
          glow.style.opacity='0';core.style.opacity='0';
          setTimeout(()=>{glow.remove();core.remove()},210);
        },120);
      };
      requestAnimationFrame(frame);
    };

    let timer=null;
    const start=()=>{
      if(timer)return;
      fire();
      timer=setInterval(()=>{
        fire();
        if(Math.random()>.62)setTimeout(fire,140);
      },620);
    };
    const stop=()=>{if(timer){clearInterval(timer);timer=null}};

    const section=document.querySelector('.national-story-map');
    if(section&&'IntersectionObserver' in window){
      new IntersectionObserver(([entry])=>entry.isIntersecting?start():stop(),{threshold:.03}).observe(section);
    }else start();
    document.addEventListener('visibilitychange',()=>document.hidden?stop():start());
  };
  boot();
})();
</script>
'''

s = s.replace('</body>', block + '\n</body>', 1)
p.write_text(s, encoding='utf-8')
