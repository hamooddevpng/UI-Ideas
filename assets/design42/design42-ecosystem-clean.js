(()=>{
  const board=document.getElementById('ecoBoard');
  if(!board)return;

  /*
   * The satellite shares data-zone="starlink" with Remote PNG, but it is
   * decorative artwork rather than an interaction target. Keeping it inside
   * .eco-zone lets the active-state transform override its SVG positioning,
   * which makes it jump toward the top-left when Remote PNG or the Telikom
   * core becomes active. Remove only that state class so its original SVG
   * transform and floating animation remain untouched.
   */
  const satellite=board.querySelector('.satellite-group.eco-zone');
  if(satellite){
    satellite.classList.remove('eco-zone','is-active');
    satellite.removeAttribute('tabindex');
    satellite.removeAttribute('role');
    satellite.removeAttribute('aria-label');
  }

  /* Remove only the white TELIKOM word printed on the core building. */
  const telikomCore=board.querySelector('.eco-zone[data-zone="telikom"]');
  if(telikomCore){
    telikomCore.querySelectorAll('text').forEach(text=>{
      if(text.textContent.trim()==='TELIKOM')text.style.display='none';
    });
  }

  const zones=[...board.querySelectorAll('.eco-zone[data-zone]')];
  const summary=document.getElementById('ecoSummary');
  const summarySub=document.getElementById('ecoSummarySub');
  const detailTitle=document.getElementById('detailTitle');
  const detailText=document.getElementById('detailText');

  if(summary)summary.setAttribute('aria-live','polite');

  const labels={
    starlink:'Remote PNG connectivity',
    network:'People and business connectivity',
    telikom:'Telikom digital core',
    compute:'Kumul Cloud',
    tcash:'T-Cash payments'
  };

  function buttonFor(key){
    return board.querySelector(`.eco-hotspot[data-service="${key}"]`);
  }

  function moveStoryToBottom(){
    if(!summary||!summarySub||!detailTitle||!detailText)return;
    const textNode=[...summary.childNodes].find(node=>node.nodeType===Node.TEXT_NODE);
    if(textNode)textNode.nodeValue=detailTitle.textContent;
    summarySub.textContent=detailText.textContent;
  }

  function preview(zone){
    const button=buttonFor(zone.dataset.zone);
    if(!button)return;
    button.dispatchEvent(new MouseEvent('mouseenter',{bubbles:false}));
    moveStoryToBottom();
  }

  function select(zone){
    const button=buttonFor(zone.dataset.zone);
    if(!button)return;
    button.click();
    moveStoryToBottom();
  }

  zones.forEach(zone=>{
    const key=zone.dataset.zone;
    zone.setAttribute('tabindex','0');
    zone.setAttribute('role','button');
    zone.setAttribute('aria-label',labels[key]||'Digital PNG service');

    zone.addEventListener('pointerenter',event=>{
      if(event.pointerType==='touch')return;
      preview(zone);
    });

    zone.addEventListener('click',event=>{
      event.preventDefault();
      select(zone);
    });

    zone.addEventListener('keydown',event=>{
      if(event.key!=='Enter'&&event.key!==' ')return;
      event.preventDefault();
      select(zone);
    });

    zone.addEventListener('focus',()=>preview(zone));
  });

  /* Mobile vertical-scroll -> horizontal-journey controller. */
  const section=board.closest('.eco-section');
  const world=document.getElementById('ecoWorld');
  if(!section||!world)return;

  const mobileQuery=matchMedia('(max-width:900px)');
  const reduceQuery=matchMedia('(prefers-reduced-motion: reduce)');
  const stickyTop=68;
  const marker=document.createElement('span');
  marker.className='eco-scroll-start';
  marker.setAttribute('aria-hidden','true');
  board.before(marker);

  let runway=0;
  let scrollFrame=0;

  function clamp(value,min,max){
    return Math.max(min,Math.min(max,value));
  }

  function scrollProgress(scrollY,start,distance){
    if(distance<=0)return 0;
    return clamp((scrollY-start)/distance,0,1);
  }

  function horizontalOffset(progress,scrollWidth,clientWidth){
    const maxScroll=Math.max(0,scrollWidth-clientWidth);
    return maxScroll*clamp(progress,0,1);
  }

  function updateHorizontalJourney(){
    scrollFrame=0;
    if(!mobileQuery.matches||reduceQuery.matches||runway<=0)return;

    const markerPageTop=scrollY+marker.getBoundingClientRect().top;
    const start=markerPageTop-stickyTop;
    const progress=scrollProgress(scrollY,start,runway);
    const target=horizontalOffset(progress,world.scrollWidth,world.clientWidth);

    if(Math.abs(world.scrollLeft-target)>.5)world.scrollLeft=target;
  }

  function scheduleJourneyUpdate(){
    if(scrollFrame)return;
    scrollFrame=requestAnimationFrame(updateHorizontalJourney);
  }

  function measureHorizontalJourney(){
    if(!mobileQuery.matches||reduceQuery.matches){
      runway=0;
      section.style.removeProperty('--eco-scroll-runway');
      world.scrollLeft=0;
      return;
    }

    const maxScroll=Math.max(0,world.scrollWidth-world.clientWidth);
    runway=maxScroll>0?Math.round(clamp(maxScroll*1.1,420,760)):0;
    section.style.setProperty('--eco-scroll-runway',`${runway}px`);
    scheduleJourneyUpdate();
  }

  addEventListener('scroll',scheduleJourneyUpdate,{passive:true});
  addEventListener('resize',measureHorizontalJourney,{passive:true});
  mobileQuery.addEventListener?.('change',measureHorizontalJourney);
  reduceQuery.addEventListener?.('change',measureHorizontalJourney);

  requestAnimationFrame(()=>{
    measureHorizontalJourney();
    requestAnimationFrame(measureHorizontalJourney);
  });
})();
