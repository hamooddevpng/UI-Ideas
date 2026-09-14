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
})();
