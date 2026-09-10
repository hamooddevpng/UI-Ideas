from pathlib import Path

p = Path('42.html')
html = p.read_text(encoding='utf-8')
marker = 'Design 42: Ask Telikom side assistant v1'
if marker in html:
    raise SystemExit(0)

body_start = html.find('<body')
body_open_end = html.find('>', body_start)
body_end = html.rfind('</body>')
if body_start < 0 or body_open_end < 0 or body_end < 0:
    raise SystemExit('body bounds not found')

inner = html[body_open_end + 1:body_end]
addon = r'''
<style>
/* Design 42: Ask Telikom side assistant v1 */
:root{--telikom-ai-w:420px;--telikom-ai-ease:cubic-bezier(.16,1,.3,1)}
.site-viewport{position:relative;width:100%;min-width:0;transition:width .48s var(--telikom-ai-ease);overflow-x:clip}
body.telikom-ai-open .site-viewport{width:calc(100% - var(--telikom-ai-w))}
body.telikom-ai-open .site-header{right:var(--telikom-ai-w);transition:right .48s var(--telikom-ai-ease),height .3s,background .3s,backdrop-filter .3s}
.telikom-ai-launcher{position:fixed;right:24px;bottom:24px;z-index:490;height:52px;padding:0 18px;border:1px solid rgba(255,255,255,.22);border-radius:999px;background:#061925;color:#fff;display:flex;align-items:center;gap:10px;box-shadow:0 18px 44px rgba(6,25,37,.24);cursor:pointer;font:800 11px/1 Manrope,Arial,sans-serif;letter-spacing:.03em;transition:transform .25s var(--telikom-ai-ease),opacity .25s,visibility .25s,box-shadow .25s}
.telikom-ai-launcher:hover{transform:translateY(-3px);box-shadow:0 22px 54px rgba(6,25,37,.3)}
.telikom-ai-launcher .spark{width:27px;height:27px;border-radius:50%;display:grid;place-items:center;background:radial-gradient(circle at 35% 30%,#6ee7ff,#1ca0e8 42%,#0875c9 72%);box-shadow:0 0 0 5px rgba(28,160,232,.11),0 0 24px rgba(28,160,232,.45);font-size:13px}
body.telikom-ai-open .telikom-ai-launcher{opacity:0;visibility:hidden;transform:translateX(20px)}
.telikom-ai-panel{position:fixed;z-index:500;inset:0 0 0 auto;width:var(--telikom-ai-w);background:linear-gradient(180deg,#071d2a 0%,#061925 64%,#04131d 100%);color:#fff;transform:translateX(100%);transition:transform .48s var(--telikom-ai-ease);box-shadow:-24px 0 70px rgba(5,24,36,.18);display:grid;grid-template-rows:auto 1fr auto;overflow:hidden;isolation:isolate}
body.telikom-ai-open .telikom-ai-panel{transform:none}
.telikom-ai-panel:before{content:"";position:absolute;inset:-80px -90px auto auto;width:270px;height:270px;border-radius:50%;background:radial-gradient(circle,rgba(28,160,232,.18),transparent 68%);pointer-events:none;z-index:-1}
.telikom-ai-head{min-height:78px;padding:16px 16px 14px 18px;border-bottom:1px solid rgba(255,255,255,.09);display:flex;align-items:center;gap:12px;background:rgba(6,25,37,.72);backdrop-filter:blur(18px)}
.telikom-ai-orb{width:38px;height:38px;border-radius:50%;display:grid;place-items:center;background:radial-gradient(circle at 34% 30%,#83ecff 0 8%,#27b8ed 31%,#0875c9 68%,#075583 100%);box-shadow:0 0 0 6px rgba(28,160,232,.08),0 0 28px rgba(28,160,232,.24);font-size:14px;flex:0 0 auto}
.telikom-ai-title{min-width:0;flex:1}.telikom-ai-title b{display:block;font-family:"Space Grotesk",Manrope,sans-serif;font-size:16px;letter-spacing:-.02em}.telikom-ai-status{margin-top:3px;display:flex;align-items:center;gap:6px;font-size:8px;font-weight:800;letter-spacing:.12em;text-transform:uppercase;color:#8fcbe0}.telikom-ai-status i{width:6px;height:6px;border-radius:50%;background:#4be28c;box-shadow:0 0 8px rgba(75,226,140,.7)}
.telikom-ai-lang{height:29px;padding:0 9px;border:1px solid rgba(255,255,255,.12);border-radius:999px;background:rgba(255,255,255,.05);color:#b9d9e5;font-size:8px;font-weight:800}.telikom-ai-close{width:34px;height:34px;border:1px solid rgba(255,255,255,.12);border-radius:50%;background:rgba(255,255,255,.05);color:#fff;cursor:pointer;font-size:18px;line-height:1}
.telikom-ai-scroll{min-height:0;overflow-y:auto;overscroll-behavior:contain;padding:18px 17px 24px;scrollbar-width:thin;scrollbar-color:rgba(123,209,239,.22) transparent}
.telikom-ai-intro{padding:4px 2px 13px}.telikom-ai-intro .eyebrow{font-size:8px;font-weight:800;letter-spacing:.15em;text-transform:uppercase;color:#69c9eb}.telikom-ai-intro h3{font-family:"Space Grotesk",Manrope,sans-serif;font-size:26px;line-height:1.02;letter-spacing:-.045em;margin:8px 0 8px}.telikom-ai-intro p{margin:0;color:#a9c1cc;font-size:10px;line-height:1.55}
.telikom-ai-suggestions{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin:8px 0 18px}.telikom-ai-chip{min-height:42px;padding:9px 11px;border:1px solid rgba(132,207,234,.15);border-radius:13px;background:rgba(255,255,255,.045);color:#dff6ff;text-align:left;cursor:pointer;font-size:9px;font-weight:700;line-height:1.25;transition:.22s}.telikom-ai-chip:hover{background:rgba(28,160,232,.12);border-color:rgba(79,203,244,.35);transform:translateY(-1px)}
.telikom-ai-chat{display:flex;flex-direction:column;gap:11px}.telikom-ai-msg{max-width:88%;font-size:10px;line-height:1.55}.telikom-ai-msg.user{align-self:flex-end;padding:10px 12px;border-radius:14px 14px 4px 14px;background:#0875c9;color:#fff;box-shadow:0 8px 22px rgba(8,117,201,.18)}.telikom-ai-msg.bot{align-self:flex-start;padding:11px 12px;border:1px solid rgba(255,255,255,.08);border-radius:4px 14px 14px 14px;background:rgba(255,255,255,.055);color:#d4e5ec}.telikom-ai-msg.bot b{color:#fff}.telikom-ai-msg.bot a{display:inline-flex;margin-top:8px;color:#75dbff;font-weight:800;font-size:9px}.telikom-ai-typing{display:inline-flex;gap:4px;align-items:center;height:12px}.telikom-ai-typing i{width:4px;height:4px;border-radius:50%;background:#78cce9;animation:telikomAiDot 1s ease-in-out infinite}.telikom-ai-typing i:nth-child(2){animation-delay:.15s}.telikom-ai-typing i:nth-child(3){animation-delay:.3s}@keyframes telikomAiDot{0%,60%,100%{transform:translateY(0);opacity:.4}30%{transform:translateY(-3px);opacity:1}}
.telikom-ai-compose{padding:13px 14px 15px;border-top:1px solid rgba(255,255,255,.09);background:rgba(4,19,29,.86);backdrop-filter:blur(20px)}.telikom-ai-form{display:flex;align-items:flex-end;gap:8px;padding:7px 7px 7px 12px;border:1px solid rgba(142,210,234,.17);border-radius:16px;background:rgba(255,255,255,.055)}.telikom-ai-input{flex:1;min-width:0;min-height:34px;max-height:86px;border:0;resize:none;background:transparent;color:#fff;outline:none;padding:8px 0 6px;font:500 10px/1.45 Manrope,Arial,sans-serif}.telikom-ai-input::placeholder{color:#71909d}.telikom-ai-send{width:36px;height:36px;border:0;border-radius:11px;background:#1ca0e8;color:#fff;display:grid;place-items:center;cursor:pointer;font-size:15px;box-shadow:0 8px 20px rgba(28,160,232,.25)}.telikom-ai-note{margin:7px 2px 0;color:#587784;font-size:7px;line-height:1.4;text-align:center}
@media(max-width:1180px){:root{--telikom-ai-w:370px}}
@media(max-width:820px){:root{--telikom-ai-w:100vw}.site-viewport,body.telikom-ai-open .site-viewport{width:100%}.telikom-ai-panel{width:100vw}.telikom-ai-launcher{right:14px;bottom:14px}.telikom-ai-suggestions{grid-template-columns:1fr 1fr}body.telikom-ai-open .site-header{right:0}.telikom-ai-head{padding-top:max(16px,env(safe-area-inset-top))}.telikom-ai-compose{padding-bottom:max(15px,env(safe-area-inset-bottom))}}
@media(prefers-reduced-motion:reduce){.site-viewport,.telikom-ai-panel,.site-header,.telikom-ai-launcher{transition:none!important}.telikom-ai-typing i{animation:none!important}}
</style>
<button class="telikom-ai-launcher" id="telikomAiLauncher" type="button" aria-controls="telikomAiPanel" aria-expanded="false"><span class="spark">✦</span><span>Ask Telikom</span></button>
<aside class="telikom-ai-panel" id="telikomAiPanel" aria-label="Ask Telikom assistant" aria-hidden="true">
  <div class="telikom-ai-head">
    <div class="telikom-ai-orb">✦</div>
    <div class="telikom-ai-title"><b>Ask Telikom</b><span class="telikom-ai-status"><i></i> Online</span></div>
    <button class="telikom-ai-lang" type="button" title="Language prototype">EN · TP</button>
    <button class="telikom-ai-close" id="telikomAiClose" type="button" aria-label="Close Ask Telikom">×</button>
  </div>
  <div class="telikom-ai-scroll" id="telikomAiScroll">
    <div class="telikom-ai-intro"><span class="eyebrow">Telikom digital assistant</span><h3>Hi. How can I help?</h3><p>Explore plans, connectivity, payments and support while keeping the Telikom website right beside the conversation.</p></div>
    <div class="telikom-ai-suggestions" id="telikomAiSuggestions">
      <button class="telikom-ai-chip" data-prompt="Help me find the right plan">Find the right plan</button><button class="telikom-ai-chip" data-prompt="I want to check coverage">Check coverage</button><button class="telikom-ai-chip" data-prompt="I need help with my internet">Internet help</button><button class="telikom-ai-chip" data-prompt="Tell me about mobile services">Mobile services</button><button class="telikom-ai-chip" data-prompt="I need connectivity for a remote location">Remote connectivity</button><button class="telikom-ai-chip" data-prompt="What can Telikom offer my business?">Business solutions</button>
    </div>
    <div class="telikom-ai-chat" id="telikomAiChat"><div class="telikom-ai-msg bot">I can help you navigate Telikom services. Choose an option above or ask me something below.</div></div>
  </div>
  <div class="telikom-ai-compose"><form class="telikom-ai-form" id="telikomAiForm"><textarea class="telikom-ai-input" id="telikomAiInput" rows="1" placeholder="Ask me anything about Telikom…" aria-label="Message Ask Telikom"></textarea><button class="telikom-ai-send" type="submit" aria-label="Send message">↑</button></form><div class="telikom-ai-note">Prototype assistant. Account-specific actions will require secure sign-in and Telikom APIs.</div></div>
</aside>
<script>
// Design 42: Ask Telikom side assistant v1
(()=>{
  const body=document.body,launcher=document.getElementById('telikomAiLauncher'),panel=document.getElementById('telikomAiPanel'),close=document.getElementById('telikomAiClose'),form=document.getElementById('telikomAiForm'),input=document.getElementById('telikomAiInput'),chat=document.getElementById('telikomAiChat'),scroll=document.getElementById('telikomAiScroll'),suggestions=document.getElementById('telikomAiSuggestions');
  if(!launcher||!panel||!close||!form||!input||!chat)return;
  const setOpen=open=>{body.classList.toggle('telikom-ai-open',open);launcher.setAttribute('aria-expanded',String(open));panel.setAttribute('aria-hidden',String(!open));if(open)setTimeout(()=>input.focus({preventScroll:true}),420)};
  launcher.addEventListener('click',()=>setOpen(true));close.addEventListener('click',()=>setOpen(false));document.addEventListener('keydown',e=>{if(e.key==='Escape'&&body.classList.contains('telikom-ai-open'))setOpen(false)});
  const responses=[
    {keys:['remote','starlink','rural'],html:'For a remote location, <b>remote connectivity</b> is the best place to start. Telikom can support locations where conventional fixed access may not be practical.<br><a href="#services">Explore connectivity →</a>'},
    {keys:['business','company','enterprise'],html:'For a business, I would look at <b>Business Data, MPLS, connectivity and managed solutions</b> first. The right option depends on your sites, users and uptime needs.<br><a href="#business">Explore business solutions →</a>'},
    {keys:['mobile','sim','data','phone'],html:'Telikom mobile services cover everyday voice and data needs. I can help narrow the choice based on how much data you use and your budget.<br><a href="#services">View mobile services →</a>'},
    {keys:['internet','broadband','wifi','home'],html:'For home or office internet, <b>Fixed Broadband</b> is a strong starting point where service is available. For harder-to-reach locations, remote connectivity may fit better.<br><a href="#services">View broadband options →</a>'},
    {keys:['coverage','available','location'],html:'I can guide you to coverage information in this prototype. A production version should connect to Telikom coverage data so I can verify a specific location rather than guess.<br><a href="#support">Coverage & support →</a>'},
    {keys:['pay','bill','recharge','top up','topup'],html:'I can take you toward recharge and payment options. In production, this assistant could securely hand off to Self Care or payment APIs after authentication.<br><a href="#offers">Recharge & offers →</a>'},
    {keys:['plan','price','best'],html:'I can help find the right plan. Tell me whether this is for <b>mobile, home internet, business, or a remote location</b>, plus roughly how you use it.'}
  ];
  const fallback='I can help with mobile, broadband, remote connectivity, business services, coverage, payments and support. Tell me what you are trying to do and I’ll point you in the right direction.';
  const addUser=text=>{const el=document.createElement('div');el.className='telikom-ai-msg user';el.textContent=text;chat.appendChild(el)};
  const addBot=html=>{const el=document.createElement('div');el.className='telikom-ai-msg bot';el.innerHTML=html;chat.appendChild(el);el.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>setOpen(false)))};
  const toBottom=()=>scroll.scrollTo({top:scroll.scrollHeight,behavior:'smooth'});
  const answer=text=>{const lower=text.toLowerCase();const found=responses.find(r=>r.keys.some(k=>lower.includes(k)));const typing=document.createElement('div');typing.className='telikom-ai-msg bot';typing.innerHTML='<span class="telikom-ai-typing"><i></i><i></i><i></i></span>';chat.appendChild(typing);toBottom();setTimeout(()=>{typing.remove();addBot(found?found.html:fallback);toBottom()},520+Math.random()*380)};
  const send=text=>{text=text.trim();if(!text)return;addUser(text);if(suggestions)suggestions.style.display='none';input.value='';input.style.height='auto';toBottom();answer(text)};
  form.addEventListener('submit',e=>{e.preventDefault();send(input.value)});input.addEventListener('keydown',e=>{if(e.key==='Enter'&&!e.shiftKey){e.preventDefault();send(input.value)}});input.addEventListener('input',()=>{input.style.height='auto';input.style.height=Math.min(input.scrollHeight,86)+'px'});suggestions?.addEventListener('click',e=>{const b=e.target.closest('[data-prompt]');if(b)send(b.dataset.prompt)});
})();
</script>
'''
wrapped = '\n<div class="site-viewport" id="siteViewport">' + inner + '\n</div>\n' + addon + '\n'
html = html[:body_open_end + 1] + wrapped + html[body_end:]
p.write_text(html, encoding='utf-8')
