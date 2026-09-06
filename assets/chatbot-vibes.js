(()=>{
  'use strict';
  if(window.__telikomChatStyled)return;
  window.__telikomChatStyled=true;

  const cls=[...document.body.classList].find(c=>/^d[1-6]$/.test(c));
  const n=cls?cls.slice(1):'5';
  const themes={
    1:{name:'Telikom Help',sub:'Customer Care • Online',hello:'Hi there 👋',copy:'How can we help you today?',icon:'💬',actions:['Top up or buy data','Home internet','Find a store'],accent:'#0875c9',head:'#0875c9',bg:'#f6fbff',radius:'22px'},
    2:{name:'Telikom Service Desk',sub:'National Service Desk • Online',hello:'Welcome to Telikom',copy:'Choose a service area and we’ll point you in the right direction.',icon:'T',actions:['Business services','Enterprise support','Government enquiries'],accent:'#0875c9',head:'#123d58',bg:'#f5f8fa',radius:'8px'},
    3:{name:'Telikom Assistant',sub:'Support • Online',hello:'Welcome',copy:'How may we direct you today?',icon:'↗',actions:['Personal services','Business services','Company information'],accent:'#0875c9',head:'#103b58',bg:'#f7f9fb',radius:'14px'},
    4:{name:'Ask Telikom',sub:'PNG Customer Support • Online',hello:'Hello from Telikom PNG 👋',copy:'We can help with home, business and everyday support.',icon:'✦',actions:['For my home','For my business','Get support'],accent:'#0875c9',head:'#0875c9',bg:'#f5fbfe',radius:'24px'},
    5:{name:'Telikom Quick Help',sub:'Self Care Assistant • Online',hello:'What would you like to do?',copy:'Choose a quick action or type a question below.',icon:'⌁',actions:['Buy data','Pay bill / Self Care','Get support'],accent:'#0875c9',head:'#063451',bg:'#f4f7f9',radius:'14px'},
    6:{name:'TELIKOM // ASSIST',sub:'Network Support Node • ONLINE',hello:'Connection ready.',copy:'Select a route or enter a request.',icon:'◉',actions:['Explore network','Services','Support'],accent:'#6ed6ff',head:'#061620',bg:'#020f18',radius:'8px'}
  };
  const t=themes[n];
  document.querySelectorAll('.tk-vibe-chat,#tk-chat-1,#tk-chat-2,#tk-chat-3,#tk-chat-4,#tk-chat-5,#tk-chat-6,#tk-production-chat').forEach(el=>el.remove());

  const css=document.createElement('style');
  css.textContent=`
  #tk-production-chat{position:fixed!important;right:0!important;bottom:0!important;width:0!important;height:0!important;z-index:2147483647!important;font-family:Inter,Arial,sans-serif!important;color:#173247!important;line-height:1.4!important;overflow:visible!important}
  #tk-production-chat *{box-sizing:border-box!important}
  #tk-production-chat .tk-window{display:none!important;position:fixed!important;right:20px!important;bottom:90px!important;width:360px!important;max-width:calc(100vw - 40px)!important;max-height:min(610px,calc(100vh - 120px))!important;margin:0!important;background:#fff!important;border:1px solid rgba(17,59,83,.13)!important;border-radius:${t.radius}!important;box-shadow:0 24px 70px rgba(4,31,48,.26)!important;overflow:hidden!important}
  #tk-production-chat.open .tk-window{display:flex!important;flex-direction:column!important;animation:tkPop .18s ease-out!important}
  #tk-production-chat .tk-header{background:${t.head}!important;color:#fff!important;padding:15px 15px 14px!important;display:flex!important;align-items:center!important;gap:11px!important;min-height:68px!important}
  #tk-production-chat .tk-brand{width:38px!important;height:38px!important;border-radius:10px!important;background:#fff!important;display:grid!important;place-items:center!important;overflow:hidden!important;flex:0 0 auto!important;border:1px solid rgba(255,255,255,.5)!important}
  #tk-production-chat .tk-brand img{width:32px!important;height:auto!important;display:block!important}
  #tk-production-chat .tk-title{min-width:0!important;flex:1!important}
  #tk-production-chat .tk-title b{display:block!important;font-size:14px!important;line-height:1.2!important;color:#fff!important}
  #tk-production-chat .tk-title small{display:flex!important;align-items:center!important;gap:6px!important;color:rgba(255,255,255,.78)!important;font-size:10.5px!important;margin-top:4px!important}
  #tk-production-chat .tk-status{width:7px!important;height:7px!important;border-radius:50%!important;background:#55d98a!important;box-shadow:0 0 0 3px rgba(85,217,138,.14)!important;display:inline-block!important}
  #tk-production-chat .tk-close{width:32px!important;height:32px!important;border:0!important;border-radius:8px!important;background:rgba(255,255,255,.1)!important;color:#fff!important;font-size:20px!important;line-height:1!important;cursor:pointer!important}
  #tk-production-chat .tk-body{padding:15px!important;background:${t.bg}!important;overflow:auto!important;min-height:245px!important}
  #tk-production-chat .tk-time{text-align:center!important;color:#8a9aa6!important;font-size:10px!important;margin:0 0 12px!important}
  #tk-production-chat .tk-row{display:flex!important;align-items:flex-end!important;gap:8px!important;margin-bottom:10px!important}
  #tk-production-chat .tk-avatar{width:28px!important;height:28px!important;border-radius:50%!important;background:${t.accent}!important;color:${n==='6'?'#061620':'#fff'}!important;display:grid!important;place-items:center!important;font-size:12px!important;font-weight:900!important;flex:0 0 auto!important}
  #tk-production-chat .tk-msg{max-width:270px!important;background:#fff!important;border:1px solid rgba(17,59,83,.1)!important;border-radius:14px 14px 14px 4px!important;padding:10px 11px!important;box-shadow:0 3px 12px rgba(7,42,65,.05)!important;color:#183247!important;font-size:12.5px!important}
  #tk-production-chat .tk-msg b{display:block!important;font-size:13px!important;margin-bottom:3px!important;color:#102f45!important}
  #tk-production-chat .tk-actions{display:grid!important;gap:7px!important;margin:12px 0 4px 36px!important}
  #tk-production-chat .tk-actions button{appearance:none!important;border:1px solid rgba(8,117,201,.24)!important;background:#fff!important;border-radius:10px!important;padding:10px 11px!important;text-align:left!important;color:#173247!important;font:700 12px Inter,Arial,sans-serif!important;cursor:pointer!important;transition:.15s ease!important}
  #tk-production-chat .tk-actions button:hover{border-color:${t.accent}!important;transform:translateY(-1px)!important}
  #tk-production-chat .tk-compose{padding:10px!important;background:#fff!important;border-top:1px solid #e5ebef!important;display:flex!important;align-items:center!important;gap:7px!important}
  #tk-production-chat .tk-compose input{flex:1!important;min-width:0!important;height:40px!important;border:1px solid #dbe4e9!important;border-radius:10px!important;padding:0 11px!important;outline:0!important;color:#173247!important;background:#fff!important;font:12px Inter,Arial,sans-serif!important}
  #tk-production-chat .tk-compose input:focus{border-color:${t.accent}!important;box-shadow:0 0 0 3px rgba(8,117,201,.08)!important}
  #tk-production-chat .tk-send{width:40px!important;height:40px!important;border:0!important;border-radius:10px!important;background:${t.accent}!important;color:${n==='6'?'#04131c':'#fff'}!important;font-size:18px!important;font-weight:900!important;cursor:pointer!important}
  #tk-production-chat .tk-powered{text-align:center!important;background:#fff!important;color:#9aa8b1!important;font-size:9.5px!important;padding:0 10px 8px!important}
  #tk-production-chat .tk-peek{position:fixed!important;right:90px!important;bottom:27px!important;background:#fff!important;border:1px solid rgba(17,59,83,.12)!important;border-radius:12px!important;padding:9px 11px!important;box-shadow:0 12px 32px rgba(4,31,48,.18)!important;color:#173247!important;font-size:11.5px!important;white-space:nowrap!important;max-width:230px!important}
  #tk-production-chat.open .tk-peek{display:none!important}
  #tk-production-chat .tk-launch{position:fixed!important;right:20px!important;bottom:20px!important;width:58px!important;height:58px!important;margin:0!important;border:0!important;border-radius:${n==='5'?'16px':'50%'}!important;background:${t.head}!important;color:#fff!important;display:grid!important;place-items:center!important;cursor:pointer!important;box-shadow:0 15px 36px rgba(4,31,48,.28)!important;padding:0!important}
  #tk-production-chat .tk-launch img{width:38px!important;height:auto!important;background:#fff!important;border-radius:8px!important;padding:4px!important}
  #tk-production-chat .tk-dot{position:absolute!important;right:1px!important;top:1px!important;width:12px!important;height:12px!important;border-radius:50%!important;background:#ef4b4b!important;border:2px solid #fff!important}
  #tk-production-chat[data-v='2'] .tk-window{border-radius:6px!important}
  #tk-production-chat[data-v='2'] .tk-header,#tk-production-chat[data-v='2'] .tk-launch{border-bottom:3px solid #0875c9!important}
  #tk-production-chat[data-v='3'] .tk-header{background:#fff!important;color:#103b58!important;border-top:4px solid #0875c9!important;border-bottom:1px solid #e4ebef!important}
  #tk-production-chat[data-v='3'] .tk-title b{color:#103b58!important}#tk-production-chat[data-v='3'] .tk-title small{color:#708390!important}#tk-production-chat[data-v='3'] .tk-close{color:#103b58!important;background:#f2f5f7!important}
  #tk-production-chat[data-v='4'] .tk-msg{border-radius:18px 18px 18px 5px!important}
  #tk-production-chat[data-v='5'] .tk-window{width:342px!important}#tk-production-chat[data-v='5'] .tk-actions{grid-template-columns:1fr 1fr!important}#tk-production-chat[data-v='5'] .tk-actions button:first-child{grid-column:1/3!important;background:#0875c9!important;color:#fff!important;border-color:#0875c9!important}
  #tk-production-chat[data-v='6']{color:#dff5ff!important}#tk-production-chat[data-v='6'] .tk-window{background:#020f18!important;border-color:rgba(110,214,255,.24)!important;box-shadow:0 0 0 1px rgba(110,214,255,.05),0 30px 90px #000!important}#tk-production-chat[data-v='6'] .tk-body{background:#03131e!important}#tk-production-chat[data-v='6'] .tk-msg{background:#061a27!important;border-color:rgba(110,214,255,.18)!important;color:#dff5ff!important}#tk-production-chat[data-v='6'] .tk-msg b{color:#fff!important}#tk-production-chat[data-v='6'] .tk-actions button{background:#061a27!important;color:#dff5ff!important;border-color:rgba(110,214,255,.2)!important;font-family:ui-monospace,SFMono-Regular,monospace!important}#tk-production-chat[data-v='6'] .tk-compose,#tk-production-chat[data-v='6'] .tk-powered{background:#020f18!important;border-color:rgba(110,214,255,.12)!important}#tk-production-chat[data-v='6'] .tk-compose input{background:#061a27!important;color:#fff!important;border-color:rgba(110,214,255,.18)!important}
  @keyframes tkPop{from{opacity:0;transform:translateY(8px) scale(.985)}to{opacity:1;transform:none}}
  @media(max-width:640px){
    #tk-production-chat .tk-launch{right:10px!important;bottom:10px!important;width:54px!important;height:54px!important}
    #tk-production-chat .tk-window{right:10px!important;bottom:74px!important;width:calc(100vw - 20px)!important;max-width:none!important;max-height:72vh!important}
    #tk-production-chat .tk-peek{display:none!important}
  }
  `;
  document.head.appendChild(css);

  const box=document.createElement('div');
  box.id='tk-production-chat';
  box.dataset.v=n;
  box.innerHTML=`
    <div class="tk-window" role="dialog" aria-label="${t.name}">
      <div class="tk-header">
        <div class="tk-brand"><img src="https://www.telikom.com.pg/assets/misc/TPNGLOGO.png" alt="Telikom"></div>
        <div class="tk-title"><b>${t.name}</b><small><span class="tk-status"></span>${t.sub}</small></div>
        <button class="tk-close" type="button" aria-label="Close chat">×</button>
      </div>
      <div class="tk-body">
        <div class="tk-time">Today</div>
        <div class="tk-row"><div class="tk-avatar">${t.icon}</div><div class="tk-msg"><b>${t.hello}</b>${t.copy}</div></div>
        <div class="tk-actions">${t.actions.map(a=>`<button type="button">${a}</button>`).join('')}</div>
      </div>
      <form class="tk-compose"><input aria-label="Message Telikom" autocomplete="off" placeholder="Type your message…"><button class="tk-send" aria-label="Send message">→</button></form>
      <div class="tk-powered">Telikom PNG • Mock customer support experience</div>
    </div>
    <div class="tk-peek">Hi 👋 Need help?</div>
    <button class="tk-launch" type="button" aria-label="Open ${t.name}"><img src="https://www.telikom.com.pg/assets/misc/TPNGLOGO.png" alt=""><span class="tk-dot"></span></button>`;

  const launch=box.querySelector('.tk-launch');
  const close=box.querySelector('.tk-close');
  const input=box.querySelector('input');
  const msg=box.querySelector('.tk-msg');
  const open=()=>{box.classList.add('open');box.querySelector('.tk-dot').style.display='none';setTimeout(()=>input.focus(),80)};
  const shut=()=>box.classList.remove('open');
  launch.onclick=()=>box.classList.contains('open')?shut():open();
  close.onclick=shut;
  box.querySelectorAll('.tk-actions button').forEach(btn=>btn.onclick=()=>{msg.innerHTML=`<b>${btn.textContent}</b>Great — this mock would now open the relevant Telikom flow or guide you through the next step.`;});
  box.querySelector('.tk-compose').onsubmit=e=>{e.preventDefault();const q=input.value.trim();if(!q)return;msg.innerHTML=`<b>Thanks — we received your message.</b>“${q.replace(/[<>]/g,'')}”<br><br><span style="color:#728592">In production, the assistant would answer from Telikom service information or hand off to support.</span>`;input.value='';};
  document.body.appendChild(box);
})();