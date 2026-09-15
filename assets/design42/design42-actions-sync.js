/* Design 42 action/link sync. */
(()=>{
  // Redirect every visible Self Care anchor to the external portal.
  const SELF_CARE_URL='https://selfcare.bmobile.com.pg/Care/Login';

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

  syncSelfCareLinks();

  const observer=new MutationObserver((records)=>{
    records.forEach((record)=>record.addedNodes.forEach((node)=>{
      if(node.nodeType===1)syncSelfCareLinks(node);
    }));
  });
  observer.observe(document.body,{childList:true,subtree:true});
})();
