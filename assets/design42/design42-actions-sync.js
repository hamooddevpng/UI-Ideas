/* Design 42 action/link sync. */
(()=>{
  const SELF_CARE_URL='https://selfcare.bmobile.com.pg/Care/Login';

  const syncNavbarCleanup=()=>{
    document.querySelectorAll('.shell-nav-item,.shell-mobile-item').forEach((item)=>{
      const link=item.querySelector(':scope > .shell-nav-main > a,:scope > .shell-mobile-main > a');
      if(link?.textContent.trim()==='Home')item.remove();
    });

    document.getElementById('searchOpen')?.remove();
    document.getElementById('searchOverlay')?.remove();
    document.querySelectorAll('#header [aria-label="Search"]').forEach(node=>node.remove());
  };

  const syncSelfCareLinks=(root=document)=>{
    const anchors=[];
    if(root instanceof HTMLAnchorElement)anchors.push(root);
    if(root.querySelectorAll)anchors.push(...root.querySelectorAll('a'));
    anchors.forEach((anchor)=>{
      if(!/self\s*care/i.test(anchor.textContent||''))return;
      anchor.href=SELF_CARE_URL;
      anchor.onclick=null;
      anchor.removeAttribute('onclick');
    });
  };

  const QUICK_ITEMS=[
    {title:'Recharge',label:'RECHARGE',body:'Top up now',icon:'card',selfcare:'topup'},
    {title:'Buy SIM',label:'SIM',body:'Get your SIM',icon:'sim',href:'/personal/mobile'},
    {title:'Pay Bill',label:'BILLING',body:'Pay quickly',icon:'bill',selfcare:'bill'},
    {title:'Coverage',label:'COVERAGE',body:'Check coverage',icon:'signal',target:'png-story'},
    {title:'Support',label:'HELP',body:'Get help',icon:'support',target:'support'},
    {title:'Store Locator',label:'STORES',body:'Find a store',icon:'pin',href:'/locations/retail'}
  ];

  const QUICK_ICONS={
    card:'<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3.5" y="6" width="17" height="12" rx="2"/><path d="M3.5 10h17"/></svg>',
    sim:'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M8 3.5h6l4 4V20.5H6V5.5A2 2 0 0 1 8 3.5Z"/><rect x="9" y="11" width="6" height="6" rx="1"/></svg>',
    bill:'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7 3.5h10v17l-2-1.4-2 1.4-2-1.4-2 1.4-2-1.4V3.5Z"/><path d="M9.5 8h5M9.5 11.5h5M9.5 15h3"/></svg>',
    signal:'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 19v-3M9.5 19v-6M14 19v-9M18.5 19V7"/></svg>',
    support:'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 13v-1a7 7 0 0 1 14 0v1"/><path d="M5 12.5H4.5A1.5 1.5 0 0 0 3 14v3a1.5 1.5 0 0 0 1.5 1.5H7v-6H5Zm14 0h.5A1.5 1.5 0 0 1 21 14v3a1.5 1.5 0 0 1-1.5 1.5H17v-6h2Z"/></svg>',
    pin:'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 21s6-5.2 6-11a6 6 0 1 0-12 0c0 5.8 6 11 6 11Z"/><circle cx="12" cy="10" r="2"/></svg>'
  };

  const syncQuickActions=()=>{
    const deck=document.getElementById('quickDeck');
    if(!deck)return;

    deck.classList.remove('quick-deck-eight','quick-deck-nine');
    deck.classList.add('quick-deck-six');

    const cards=[...deck.querySelectorAll('.quick-card')];
    cards.slice(6).forEach(card=>card.remove());

    const liveCards=[...deck.querySelectorAll('.quick-card')];
    QUICK_ITEMS.forEach((item,index)=>{
      const card=liveCards[index];
      if(!card)return;

      card.dataset.quickIndex=String(index+1);
      card.style.setProperty('--qdelay',`${index*55}ms`);
      card.style.setProperty('--qrot','0deg');
      card.removeAttribute('data-quick-selfcare');

      const qnum=card.querySelector('.q-num');
      const icon=card.querySelector('.q-icon');
      const title=card.querySelector('h3');
      const body=card.querySelector('p');
      if(qnum)qnum.textContent=`${String(index+1).padStart(2,'0')} / ${item.label}`;
      if(icon)icon.innerHTML=QUICK_ICONS[item.icon]||'';
      if(title)title.textContent=item.title;
      if(body)body.textContent=item.body;

      if(item.selfcare){
        card.setAttribute('data-quick-selfcare',item.selfcare);
      }else if(item.href){
        card.onclick=null;
        if(card instanceof HTMLAnchorElement)card.href=item.href;
        else card.onclick=()=>{location.href=item.href};
      }else if(item.target){
        card.onclick=()=>document.getElementById(item.target)?.scrollIntoView({behavior:'smooth',block:'start'});
      }
    });
  };

  syncNavbarCleanup();
  syncSelfCareLinks();
  syncQuickActions();

  const observer=new MutationObserver((records)=>{
    records.forEach((record)=>record.addedNodes.forEach((node)=>{
      if(node.nodeType===1)syncSelfCareLinks(node);
    }));
  });
  observer.observe(document.body,{childList:true,subtree:true});
})();
