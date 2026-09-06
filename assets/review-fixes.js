(()=>{'use strict';
const title=document.title||'';
const variant=title.includes('Consumer Services Hub')?'1':title.includes('Connected Nation')?'2':title.includes('Balanced Corporate')?'3':title.includes('National Connectivity')?'4':title.includes('Digital Self Service')?'5':title.includes('Living Network')?'6':null;
if(!variant)return;

/* Guarantee the themed chatbot is present even if another enhancement script is cached or fails. */
if(!document.querySelector('script[data-chatbot-vibes]')&&!document.querySelector('.tk-vibe-chat')){
  const s=document.createElement('script');s.src='assets/chatbot-vibes.js?v=20260903-1258';s.dataset.chatbotVibes='1';document.body.appendChild(s);
}

const css=document.createElement('style');css.textContent=`
/* Explicit client-review brand lockup */
.tk-footer-brand{display:flex;flex-direction:column;align-items:flex-start;gap:7px}.tk-footer-slogan{font:700 11px/1.3 Inter,Arial,sans-serif;letter-spacing:.02em;color:inherit;opacity:.92;white-space:nowrap}.tk-footer-brand img{filter:none!important;opacity:1!important;background:#fff!important;padding:7px 10px!important;border-radius:8px!important;object-fit:contain!important;max-width:215px!important;max-height:66px!important;width:auto!important;height:auto!important}
/* Make the chatbot impossible to miss during mock review while still staying stationary. */
.tk-vibe-chat{position:fixed!important;right:22px!important;bottom:22px!important;z-index:2147480000!important}.tk-vibe-chat .tk-launch{display:grid!important;visibility:visible!important;opacity:1!important}.tk-vibe-chat .tk-peek{display:block!important}.tk-vibe-chat.open .tk-peek{display:none!important}
@media(max-width:640px){.tk-vibe-chat{right:12px!important;bottom:12px!important}.tk-vibe-chat .tk-peek{display:none!important}.tk-footer-slogan{font-size:10px}}
`;
document.head.appendChild(css);

const footerBrand=()=>{
  document.querySelectorAll('footer img[src*="TPNGLOGO"],.footer img[src*="TPNGLOGO"],.foot img[src*="TPNGLOGO"]').forEach(img=>{
    if(img.dataset.footerLockup)return;img.dataset.footerLockup='1';
    let wrap=img.parentElement;if(!wrap)return;wrap.classList.add('tk-footer-brand');
    if(!wrap.querySelector('.tk-footer-slogan')){const s=document.createElement('span');s.className='tk-footer-slogan';s.textContent='Connecting you anywhere anytime';img.insertAdjacentElement('afterend',s)}
  });
};
footerBrand();
const mo=new MutationObserver(footerBrand);mo.observe(document.body,{childList:true,subtree:true});setTimeout(()=>mo.disconnect(),12000);
})();