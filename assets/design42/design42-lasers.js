/*
 * Design 42 province lasers v14.
 * Replaces the legacy ultra-fast 5px endpoint bolt with calmer, readable motion.
 */
(()=>{
  if(matchMedia('(prefers-reduced-motion: reduce)').matches)return;

  const boot=()=>{
    const section=document.querySelector('.national-story-map');
    const stage=document.getElementById('nationalMapStage');
    const network=document.getElementById('provinceNetworkV6');
    if(!section||!stage||!network){setTimeout(boot,80);return}
    if(document.getElementById('provinceLaserLayerV14'))return;

    // The loader plants this marker before the legacy v12 runtime executes,
    // causing v12 to exit before it starts its timer. Remove it now.
    const legacyMarker=document.getElementById('provinceLaserLayerV12');
    if(legacyMarker)legacyMarker.remove();

    const nodeEls=[...network.querySelectorAll('.province-node-v6')];
    if(nodeEls.length<2){setTimeout(boot,80);return}

    const layer=document.createElement('div');
    layer.id='provinceLaserLayerV14';
    layer.className='province-laser-layer-v14';
    layer.setAttribute('aria-hidden','true');
    stage.appendChild(layer);

    let nodes=[];
    let active=0;
    let visible=true;
    const stats=window.__provinceLaserV14Stats={shots:0,finishes:0,last:null};

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
      const a=nodes[0],b=nodes[1];
      return {a,b,d:Math.hypot(b.x-a.x,b.y-a.y)};
    };

    const pulse=(el,ms)=>{
      el.classList.add('laser-live-v14');
      setTimeout(()=>el.classList.remove('laser-live-v14'),ms);
    };

    const fire=()=>{
      if(!visible||document.hidden||active>=2)return;
      const pair=pickPair();
      if(!pair)return;
      const {a,b,d}=pair;
      const dx=b.x-a.x,dy=b.y-a.y;
      const angle=Math.atan2(dy,dx)*180/Math.PI;
      const bolt=document.createElement('i');
      bolt.className='province-bolt-v14';
      layer.appendChild(bolt);
      active++;stats.shots++;

      const start=`translate3d(${a.x}px,${a.y}px,0) translate(-50%,-50%) rotate(${angle}deg)`;
      const end=`translate3d(${b.x}px,${b.y}px,0) translate(-50%,-50%) rotate(${angle}deg)`;
      const duration=Math.max(700,Math.min(1100,d*1.8));

      pulse(a.el,220);
      setTimeout(()=>pulse(b.el,280),Math.max(240,duration-150));

      const anim=bolt.animate([
        {transform:start,opacity:0,offset:0},
        {transform:start,opacity:1,offset:.08},
        {transform:end,opacity:1,offset:.88},
        {transform:end,opacity:0,offset:1}
      ],{duration,easing:'cubic-bezier(.22,.61,.36,1)',fill:'forwards'});

      stats.last={from:{x:a.x,y:a.y},to:{x:b.x,y:b.y},distance:d,duration};
      anim.onfinish=()=>{bolt.remove();active=Math.max(0,active-1);stats.finishes++};
      anim.oncancel=()=>{bolt.remove();active=Math.max(0,active-1)};
    };

    const tick=()=>{
      if(visible&&!document.hidden)fire();
      setTimeout(tick,900+Math.random()*500);
    };

    if('ResizeObserver' in window)new ResizeObserver(rebuild).observe(stage);
    else addEventListener('resize',rebuild,{passive:true});
    if('IntersectionObserver' in window)new IntersectionObserver(([entry])=>{visible=entry.isIntersecting;if(visible)rebuild()},{threshold:.03}).observe(section);
    document.addEventListener('visibilitychange',()=>{if(!document.hidden)rebuild()});

    setTimeout(()=>{fire();tick()},280);
  };

  boot();
})();
