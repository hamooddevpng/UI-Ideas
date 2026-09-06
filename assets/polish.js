(()=>{
  'use strict';

  const current=document.currentScript;
  const base=current&&current.src?new URL('.',current.src).href:'assets/';
  const chatbotCdn='https://cdn.jsdelivr.net/gh/Kesehet/hosting_static@main/telikom-homepage-mocks/assets/';

  const reloadOnce=()=>{
    const href=window.location.href;
    if(href.includes('_RELOADED')) return false;

    const marker=Math.random().toString(36).slice(2,10)+'_'+Date.now().toString(36)+'_RELOADED';

    if(window.location.hostname==='htmlpreview.github.io'){
      const prefix='https://htmlpreview.github.io/?';
      if(!href.startsWith(prefix)) return false;

      let inner=href.slice(prefix.length);
      if(!/^https?:\/\//i.test(inner)) return false;

      let hash='';
      const hashAt=inner.indexOf('#');
      if(hashAt!==-1){
        hash=inner.slice(hashAt);
        inner=inner.slice(0,hashAt);
      }

      const sep=inner.includes('?')?'&':'?';
      window.location.replace(prefix+inner+sep+'cb='+encodeURIComponent(marker)+hash);
      return true;
    }

    const u=new URL(href);
    u.searchParams.set('cb',marker);
    window.location.replace(u.toString());
    return true;
  };

  if(reloadOnce()) return;

  const loadLocal=(file,key)=>{
    if(document.querySelector(`script[data-${key}]`)) return;
    const s=document.createElement('script');
    s.src=base+file+'?v='+Date.now()+'_'+Math.random().toString(36).slice(2,8);
    s.async=true;
    s.setAttribute(`data-${key}`,'1');
    document.body.appendChild(s);
  };

  const loadChatbot=(n)=>{
    if(!n||document.querySelector('script[data-telikom-chatbot]')) return;
    const s=document.createElement('script');
    s.src=chatbotCdn+'chatbot-'+n+'.js?v='+Date.now()+'_'+Math.random().toString(36).slice(2,8);
    s.async=true;
    s.setAttribute('data-telikom-chatbot',n);
    document.body.appendChild(s);
  };

  const removeServiceCommand=()=>{
    if(!document.title.includes('Digital Self Service')) return;
    document.querySelectorAll('.ux-executive').forEach(el=>el.remove());
  };

  const run=()=>{
    const cls=[...document.body.classList].find(c=>/^d[1-5]$/.test(c));
    const n=cls?cls.slice(1):document.title.includes('Consumer Services Hub')?'1':document.title.includes('Connected Nation')?'2':document.title.includes('Balanced Corporate')?'3':document.title.includes('National Connectivity')?'4':document.title.includes('Digital Self Service')?'5':null;
    const isDesign5=n==='5';

    if(isDesign5){
      document.body.dataset.uniqueSections='1';
      removeServiceCommand();
    }

    // Each homepage now has its own standalone chatbot file.
    // Use absolute CDN URL so HTMLPreview never has to resolve the chatbot asset.
    loadChatbot(n);
    loadLocal('polish-core.js','polish-core');
  };

  if(document.readyState==='loading') document.addEventListener('DOMContentLoaded',run,{once:true}); else run();
})();