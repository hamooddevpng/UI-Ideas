(()=>{
  'use strict';
  const reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
  const fine=matchMedia('(pointer:fine)').matches;

  const fx=document.createElement('style');
  fx.textContent=`
    .hero:before{content:'';position:absolute;inset:0;z-index:3;pointer-events:none;background:radial-gradient(520px circle at var(--mx,72%) var(--my,42%),rgba(74,207,255,.15),transparent 64%);mix-blend-mode:screen}
    .hero-canvas{opacity:.95;filter:drop-shadow(0 0 18px rgba(78,211,255,.28))}
    .hero-panel{position:relative;background:linear-gradient(150deg,rgba(5,50,78,.48),rgba(2,24,39,.58))!important;border-color:rgba(124,224,255,.24)!important;box-shadow:0 30px 90px rgba(0,0,0,.34),0 0 55px rgba(45,185,238,.09)!important}
    .hero-panel:after{content:'LIVE NETWORK';position:absolute;right:18px;top:16px;font-size:9px;letter-spacing:.12em;color:#7fe0ff;font-weight:800;opacity:.85}
    .signal{animation:signalBreath 4.2s ease-in-out infinite;animation-delay:var(--signal-delay,0s)}
    @keyframes signalBreath{0%,100%{background:transparent}50%{background:rgba(95,215,255,.045)}}
    .gateway{transform-style:preserve-3d;will-change:transform}.gateway .round-arrow,.gateway .label,.gateway-bottom{transform:translateZ(18px)}
    .plan.featured{position:relative;overflow:hidden}.plan.featured:after{content:'';position:absolute;width:180px;height:180px;border-radius:50%;background:radial-gradient(circle,rgba(112,221,255,.22),transparent 68%);right:-65px;top:-65px;animation:floatGlow 5s ease-in-out infinite}@keyframes floatGlow{50%{transform:translate(-20px,18px) scale(1.15)}}
    .rail-card.is-near{border-color:#9fd7ef;box-shadow:0 25px 62px rgba(5,65,98,.15)}
    @media(max-width:900px){.hero-canvas{opacity:.52}.hero:before{display:none}}
  `;
  document.head.appendChild(fx);

  const topProgress=document.createElement('div');
  topProgress.className='motion-progress';
  document.body.appendChild(topProgress);

  const nav=document.querySelector('.nav');
  const hero=document.querySelector('.hero');
  const heroBgs=[...document.querySelectorAll('.hero-bg')];
  const dots=[...document.querySelectorAll('.hero-dot')];
  let slideIndex=0;
  function showSlide(i){
    if(!heroBgs.length)return;
    slideIndex=(i+heroBgs.length)%heroBgs.length;
    heroBgs.forEach((s,n)=>s.classList.toggle('active',n===slideIndex));
    dots.forEach((d,n)=>d.classList.toggle('active',n===slideIndex));
  }
  dots.forEach((d,i)=>d.addEventListener('click',()=>showSlide(i)));
  if(!reduce&&heroBgs.length)setInterval(()=>showSlide(slideIndex+1),5200);

  const reveals=[...document.querySelectorAll('.reveal')];
  if('IntersectionObserver' in window&&!reduce){
    const io=new IntersectionObserver(entries=>entries.forEach(e=>{
      if(!e.isIntersecting)return;
      const siblings=e.target.parentElement?[...e.target.parentElement.children].filter(x=>x.classList&&x.classList.contains('reveal')):[];
      const idx=Math.max(0,siblings.indexOf(e.target));
      e.target.style.transitionDelay=Math.min(idx,5)*70+'ms';
      e.target.classList.add('in');
      io.unobserve(e.target);
    }),{threshold:.12,rootMargin:'0px 0px -5% 0px'});
    reveals.forEach(el=>io.observe(el));
  }else reveals.forEach(el=>el.classList.add('in'));

  const story=document.getElementById('storyScene');
  const storyImg=story&&story.querySelector('img');
  const campaign=document.querySelector('.campaign');
  function onScroll(){
    const y=scrollY;
    if(nav)nav.classList.toggle('scrolled',y>40);
    const doc=Math.max(1,document.documentElement.scrollHeight-innerHeight);
    topProgress.style.width=Math.min(100,y/doc*100)+'%';

    if(!reduce&&hero&&y<innerHeight*1.2){
      const p=Math.min(1,y/Math.max(1,innerHeight));
      heroBgs.forEach((bg,i)=>{
        if(bg.classList.contains('active'))bg.style.transform=`translate3d(0,${p*34}px,0) scale(${1+p*.035})`;
        else bg.style.transform='scale(1.09)';
      });
    }

    if(!reduce&&story&&storyImg&&innerWidth>720){
      const r=story.getBoundingClientRect();
      const p=Math.max(0,Math.min(1,(innerHeight-r.top)/(innerHeight+r.height)));
      storyImg.style.transform=`translate3d(0,${(p-.5)*42}px,0) scale(1.06)`;
    }

    if(!reduce&&campaign&&innerWidth>720){
      const r=campaign.getBoundingClientRect();
      const p=Math.max(0,Math.min(1,(innerHeight-r.top)/(innerHeight+r.height)));
      campaign.style.backgroundPosition=`center ${48+(p-.5)*12}%`;
    }
  }
  addEventListener('scroll',onScroll,{passive:true});
  onScroll();

  if(hero&&!reduce&&fine){
    hero.addEventListener('pointermove',e=>{
      const r=hero.getBoundingClientRect();
      hero.style.setProperty('--mx',`${e.clientX-r.left}px`);
      hero.style.setProperty('--my',`${e.clientY-r.top}px`);
    });
  }

  if(!reduce&&fine){
    document.querySelectorAll('.gateway').forEach(card=>{
      card.addEventListener('pointermove',e=>{
        const r=card.getBoundingClientRect();
        const x=(e.clientX-r.left)/r.width-.5;
        const y=(e.clientY-r.top)/r.height-.5;
        card.style.transform=`perspective(900px) rotateX(${(-y*4).toFixed(2)}deg) rotateY(${(x*5).toFixed(2)}deg) translateY(-5px)`;
      });
      card.addEventListener('pointerleave',()=>card.style.transform='');
    });
  }

  document.querySelectorAll('.signal').forEach((el,i)=>el.style.setProperty('--signal-delay',`${i*.22}s`));

  const shell=document.getElementById('railShell');
  const rail=document.getElementById('rail');
  const railProgress=document.getElementById('railProgress');
  const cards=rail?[...rail.querySelectorAll('.rail-card')]:[];
  let dragging=false,startX=0,startScroll=0;

  function updateRail(){
    if(!shell)return;
    const max=Math.max(0,shell.scrollWidth-shell.clientWidth);
    if(railProgress)railProgress.style.width=(max?shell.scrollLeft/max*100:0)+'%';
    const center=shell.getBoundingClientRect().left+shell.clientWidth/2;
    cards.forEach(card=>{
      const r=card.getBoundingClientRect();
      const d=Math.abs((r.left+r.width/2)-center);
      card.classList.toggle('is-near',d<r.width*.68);
    });
  }

  if(shell){
    shell.addEventListener('scroll',updateRail,{passive:true});
    shell.addEventListener('wheel',e=>{
      if(innerWidth<=720)return;
      const max=Math.max(0,shell.scrollWidth-shell.clientWidth);
      if(max<=0)return;
      const delta=Math.abs(e.deltaX)>Math.abs(e.deltaY)?e.deltaX:e.deltaY;
      const next=shell.scrollLeft+delta;
      const can=(delta>0&&shell.scrollLeft<max-1)||(delta<0&&shell.scrollLeft>1);
      if(can){e.preventDefault();shell.scrollLeft=Math.max(0,Math.min(max,next));}
    },{passive:false});

    shell.addEventListener('pointerdown',e=>{
      if(e.button!==0)return;
      dragging=true;startX=e.clientX;startScroll=shell.scrollLeft;
      shell.classList.add('dragging');
      shell.setPointerCapture?.(e.pointerId);
    });
    shell.addEventListener('pointermove',e=>{
      if(!dragging)return;
      shell.scrollLeft=startScroll-(e.clientX-startX)*1.15;
    });
    const endDrag=e=>{
      dragging=false;shell.classList.remove('dragging');
      try{shell.releasePointerCapture?.(e.pointerId)}catch(_){ }
    };
    shell.addEventListener('pointerup',endDrag);
    shell.addEventListener('pointercancel',endDrag);
    shell.addEventListener('pointerleave',e=>{if(dragging&&e.buttons===0)endDrag(e)});
    addEventListener('resize',updateRail,{passive:true});
    updateRail();
  }

  addEventListener('load',()=>{
    try{
      if(!window.THREE||reduce)return;
      const canvas=document.getElementById('heroCanvas');
      if(!canvas)return;
      const scene=new THREE.Scene();
      const camera=new THREE.PerspectiveCamera(42,innerWidth/innerHeight,.1,100);
      const renderer=new THREE.WebGLRenderer({canvas,alpha:true,antialias:innerWidth>800});
      camera.position.z=8.2;
      renderer.setPixelRatio(Math.min(devicePixelRatio,innerWidth<720?1:1.65));
      renderer.setSize(innerWidth,innerHeight);

      const globe=new THREE.Group();scene.add(globe);
      globe.add(new THREE.Mesh(new THREE.SphereGeometry(2.05,48,48),new THREE.MeshBasicMaterial({color:0x0d72a8,transparent:true,opacity:.12})));
      const wire=new THREE.Mesh(new THREE.SphereGeometry(2.12,32,32),new THREE.MeshBasicMaterial({color:0x63d9ff,transparent:true,opacity:.18,wireframe:true}));globe.add(wire);
      const pts=new THREE.Points(new THREE.SphereGeometry(2.18,72,72),new THREE.PointsMaterial({color:0xa9efff,size:.03,transparent:true,opacity:.8}));globe.add(pts);
      [2.22,2.30].forEach((r,i)=>globe.add(new THREE.Mesh(new THREE.SphereGeometry(r,42,42),new THREE.MeshBasicMaterial({color:i?0x137fc1:0x59d7ff,transparent:true,opacity:i?.04:.055,side:THREE.BackSide}))));
      [[2.75,0,0],[2.65,.72,.15],[2.55,-.55,.7]].forEach(([r,rx,rz])=>{const ring=new THREE.Mesh(new THREE.TorusGeometry(r,.009,8,180),new THREE.MeshBasicMaterial({color:0x75ddff,transparent:true,opacity:.32}));ring.rotation.x=Math.PI/2+rx;ring.rotation.z=rz;globe.add(ring)});

      const positions=[];
      for(let i=0;i<16;i++){
        const a=Math.random()*Math.PI*2,b=(Math.random()-.5)*Math.PI*.9;
        const p=new THREE.Vector3(2.19*Math.cos(b)*Math.cos(a),2.19*Math.sin(b),2.19*Math.cos(b)*Math.sin(a));positions.push(p);
        const node=new THREE.Mesh(new THREE.SphereGeometry(.038,12,12),new THREE.MeshBasicMaterial({color:0xc9f6ff}));node.position.copy(p);globe.add(node);
        const halo=new THREE.Mesh(new THREE.SphereGeometry(.10,12,12),new THREE.MeshBasicMaterial({color:0x2ebeff,transparent:true,opacity:.20}));halo.position.copy(p);globe.add(halo);
      }
      for(let i=0;i<14;i++){
        const p1=positions[i%positions.length],p2=positions[(i*5+3)%positions.length];
        const mid=p1.clone().add(p2).multiplyScalar(.5).normalize().multiplyScalar(3.25+Math.random()*.35);
        const curve=new THREE.QuadraticBezierCurve3(p1,mid,p2);
        globe.add(new THREE.Line(new THREE.BufferGeometry().setFromPoints(curve.getPoints(48)),new THREE.LineBasicMaterial({color:0x73e2ff,transparent:true,opacity:.48})));
      }
      const satellites=[];
      for(let i=0;i<3;i++){
        const s=new THREE.Mesh(new THREE.OctahedronGeometry(.09),new THREE.MeshBasicMaterial({color:0xffffff,transparent:true,opacity:.9}));
        s.userData={angle:i*2.1,speed:.0035+i*.0008,radius:2.72+i*.12,tilt:(i-1)*.38};globe.add(s);satellites.push(s);
      }
      globe.position.x=innerWidth<900?1.65:2.65;
      let tx=0,ty=0;
      addEventListener('pointermove',e=>{tx=(e.clientX/innerWidth-.5)*.42;ty=(e.clientY/innerHeight-.5)*.24},{passive:true});
      function render(){
        globe.rotation.y+=.0017;globe.rotation.x+=(ty-globe.rotation.x)*.025;globe.rotation.z+=(tx*.2-globe.rotation.z)*.025;
        wire.rotation.y-=.0011;pts.rotation.y+=.0006;
        satellites.forEach(s=>{s.userData.angle+=s.userData.speed*10;const a=s.userData.angle,r=s.userData.radius,t=s.userData.tilt;s.position.set(Math.cos(a)*r,Math.sin(a)*r*Math.cos(t),Math.sin(a)*r*Math.sin(t));s.rotation.x+=.03;s.rotation.y+=.025});
        renderer.render(scene,camera);requestAnimationFrame(render);
      }
      render();
      addEventListener('resize',()=>{camera.aspect=innerWidth/innerHeight;camera.updateProjectionMatrix();renderer.setSize(innerWidth,innerHeight);globe.position.x=innerWidth<900?1.65:2.65});
    }catch(err){console.warn('Design 6 3D layer skipped:',err)}
  });
})();