from pathlib import Path
import re

p=Path('42.html')
s=p.read_text()

# Replace the current four-card quick action strip with an eight-action launchpad.
new_markup='''<section class="quick-actions quick-launchpad" id="quick-actions">
  <div class="quick-deck quick-deck-eight reveal" id="quickDeck">
    <svg class="quick-circuit" viewBox="0 0 1000 260" preserveAspectRatio="none" aria-hidden="true">
      <path id="quickCircuitPath" d="M80 66 H920 Q962 66 962 108 V151 Q962 194 920 194 H80 Q38 194 38 151 V108 Q38 66 80 66 Z"/>
      <path class="quick-circuit-cross" d="M250 28 V232 M500 28 V232 M750 28 V232"/>
      <circle class="quick-packet qp1" r="4"><animateMotion dur="7s" repeatCount="indefinite"><mpath href="#quickCircuitPath"/></animateMotion></circle>
      <circle class="quick-packet qp2" r="3"><animateMotion dur="7s" begin="-3.5s" repeatCount="indefinite"><mpath href="#quickCircuitPath"/></animateMotion></circle>
    </svg>
    <div class="quick-deck-glow" id="quickDeckGlow" aria-hidden="true"></div>

    <button class="quick-card" type="button" data-quick-selfcare="topup" style="--qdelay:0ms;--qrot:-2deg"><div class="q-top"><span class="q-num">01 / RECHARGE</span><span class="q-icon">＋</span></div><h3>Top Up</h3><p>Recharge your Telikom service.</p></button>
    <button class="quick-card" type="button" data-quick-selfcare="balance" style="--qdelay:55ms;--qrot:1.4deg"><div class="q-top"><span class="q-num">02 / ACCOUNT</span><span class="q-icon">◉</span></div><h3>Balance</h3><p>Check your available balance.</p></button>
    <button class="quick-card" type="button" data-quick-selfcare="bill" style="--qdelay:110ms;--qrot:-1.2deg"><div class="q-top"><span class="q-num">03 / BILLING</span><span class="q-icon">✓</span></div><h3>Pay Bill</h3><p>Manage your post-paid bill.</p></button>
    <button class="quick-card" type="button" data-quick-selfcare="bundles" style="--qdelay:165ms;--qrot:1.8deg"><div class="q-top"><span class="q-num">04 / BUNDLES</span><span class="q-icon">⌁</span></div><h3>Bundles</h3><p>Browse voice and data bundles.</p></button>
    <button class="quick-card" type="button" data-quick-selfcare="transfer" style="--qdelay:220ms;--qrot:1.5deg"><div class="q-top"><span class="q-num">05 / CREDIT</span><span class="q-icon">↗</span></div><h3>Transfer</h3><p>Send credit to another number.</p></button>
    <a class="quick-card" href="#services" style="--qdelay:275ms;--qrot:-1.6deg"><div class="q-top"><span class="q-num">06 / INTERNET</span><span class="q-icon">⌂</span></div><h3>Internet</h3><p>Explore fixed and mobile connectivity.</p></a>
    <a class="quick-card" href="#business" style="--qdelay:330ms;--qrot:1.1deg"><div class="q-top"><span class="q-num">07 / BUSINESS</span><span class="q-icon">▦</span></div><h3>Business</h3><p>Data, voice, systems and hosting.</p></a>
    <a class="quick-card" href="#support" style="--qdelay:385ms;--qrot:-1.8deg"><div class="q-top"><span class="q-num">08 / HELP</span><span class="q-icon">?</span></div><h3>Support</h3><p>Customer Care is available on 1555.</p></a>
  </div>
</section>'''

s,n=re.subn(r'<section class="quick-actions">.*?</section>',new_markup,s,count=1,flags=re.S)
if n!=1:
    raise SystemExit(f'quick action section replacement count {n}')

# Wire the five Self Care actions directly into the existing phone prototype.
old="document.getElementById('heroPrimary').onclick=()=>openPhone('home');document.getElementById('quickSelfCare').onclick=()=>openPhone('home');document.getElementById('phoneClose').onclick=closePhone;"
new="document.getElementById('heroPrimary').onclick=()=>openPhone('home');document.querySelectorAll('[data-quick-selfcare]').forEach(b=>b.onclick=()=>openPhone(b.dataset.quickSelfcare||'home'));document.getElementById('phoneClose').onclick=closePhone;"
if old not in s:
    raise SystemExit('quickSelfCare handler anchor not found')
s=s.replace(old,new,1)

css='''

/* Design 42: eight-action kinetic launchpad */
.quick-launchpad{position:relative;z-index:40;margin-top:-50px;padding:0 0 58px;isolation:isolate}
.quick-launchpad .quick-deck{--deck-x:50%;--deck-y:50%;position:relative;width:min(1320px,calc(100% - 80px));margin:auto;padding:10px;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));grid-template-rows:repeat(2,104px);gap:8px;border-radius:28px;background:radial-gradient(430px circle at var(--deck-x) var(--deck-y),rgba(117,218,255,.17),transparent 60%),rgba(255,255,255,.96);box-shadow:0 28px 76px rgba(4,28,41,.18);overflow:hidden;perspective:1100px;transform-style:preserve-3d}
.quick-launchpad .quick-deck:before{content:"";position:absolute;z-index:0;inset:-55%;background:conic-gradient(from 0deg,transparent 0 37%,rgba(28,160,232,.11) 43%,rgba(104,221,255,.24) 48%,transparent 54% 100%);animation:quickAura 9s linear infinite;pointer-events:none}
@keyframes quickAura{to{transform:rotate(360deg)}}
.quick-circuit{position:absolute;z-index:1;inset:7px;width:calc(100% - 14px);height:calc(100% - 14px);overflow:visible;pointer-events:none;opacity:.4}
.quick-circuit path{fill:none;stroke:rgba(28,160,232,.24);stroke-width:1.1;stroke-dasharray:7 11;vector-effect:non-scaling-stroke;animation:quickCircuitFlow 2.2s linear infinite}
.quick-circuit .quick-circuit-cross{stroke:rgba(16,43,60,.07);stroke-dasharray:2 8;animation-duration:4.5s}
@keyframes quickCircuitFlow{to{stroke-dashoffset:-54}}
.quick-packet{fill:#eaffff;stroke:#1ca0e8;stroke-width:1;filter:drop-shadow(0 0 7px #1ca0e8);opacity:.9}
.quick-deck-glow{position:absolute;z-index:2;width:165px;height:165px;left:var(--deck-x);top:var(--deck-y);border-radius:50%;transform:translate(-50%,-50%);background:radial-gradient(circle,rgba(119,224,255,.22),rgba(28,160,232,.08) 38%,transparent 70%);filter:blur(3px);pointer-events:none;opacity:.66;transition:opacity .2s}
.quick-launchpad .quick-card{--qrx:0deg;--qry:0deg;--qx:50%;--qy:50%;position:relative;z-index:4;min-width:0;min-height:0;height:104px;padding:13px 15px;border-radius:18px;border:1px solid rgba(16,43,60,.085);background:rgba(255,255,255,.88);backdrop-filter:blur(13px);box-shadow:0 7px 20px rgba(19,63,84,.035);color:var(--ink);text-align:left;cursor:pointer;overflow:hidden;opacity:0;transform:translate3d(0,20px,0) rotate(var(--qrot)) scale(.86);filter:blur(4px);transition:opacity .52s var(--qdelay) ease,transform .78s var(--qdelay) var(--spring),filter .5s var(--qdelay) ease,box-shadow .26s ease,border-color .26s ease,background .26s ease}
.quick-launchpad .quick-card:before{content:"";position:absolute;z-index:-1;inset:0;background:radial-gradient(145px circle at var(--qx) var(--qy),rgba(117,220,255,.26),transparent 68%);opacity:0;transition:opacity .2s}
.quick-launchpad.quick-ready .quick-card{opacity:1;filter:none;transform:none}
.quick-launchpad .quick-card:hover,.quick-launchpad .quick-card:focus-visible{background:rgba(250,254,255,.98);border-color:rgba(28,160,232,.34);box-shadow:0 22px 45px rgba(16,70,97,.13);transform:perspective(700px) translateY(-8px) rotateX(var(--qrx)) rotateY(var(--qry)) scale(1.025)!important;outline:none}
.quick-launchpad .quick-card:hover:before,.quick-launchpad .quick-card:focus-visible:before{opacity:1}
.quick-launchpad.quick-focused .quick-card:not(.quick-hot){opacity:.62;filter:saturate(.7);transform:scale(.985)}
.quick-launchpad .q-top{position:relative;z-index:2}
.quick-launchpad .q-num{font-size:6px;letter-spacing:.13em}
.quick-launchpad .q-icon{position:relative;width:30px;height:30px;background:linear-gradient(145deg,#e7f7fd,#d8f0fb);box-shadow:0 8px 19px rgba(8,117,201,.08);transition:.32s var(--spring)}
.quick-launchpad .quick-card:hover .q-icon,.quick-launchpad .quick-card:focus-visible .q-icon{background:var(--navy);color:#9ee7ff;transform:translateY(-2px) rotate(7deg) scale(1.12);box-shadow:0 10px 24px rgba(6,25,37,.18),0 0 0 5px rgba(28,160,232,.08)}
.quick-launchpad .quick-card h3{position:relative;z-index:2;font-size:18px;margin:10px 0 2px;line-height:1}
.quick-launchpad .quick-card p{position:relative;z-index:2;font-size:7.3px;line-height:1.35;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.quick-spark{position:absolute;z-index:9;left:var(--sx0);top:var(--sy0);width:4px;height:4px;border-radius:50%;background:#4dc9f4;box-shadow:0 0 9px rgba(28,160,232,.75);pointer-events:none;animation:quickSpark .62s var(--spring) forwards}
.quick-spark:nth-of-type(2n){background:#20a957}
@keyframes quickSpark{0%{opacity:0;transform:translate(-50%,-50%) scale(.2)}20%{opacity:1}100%{opacity:0;transform:translate(calc(-50% + var(--sdx)),calc(-50% + var(--sdy))) scale(.1)}}
@media(max-width:1050px) and (min-width:821px){.quick-launchpad .quick-deck{width:calc(100% - 48px);grid-template-rows:repeat(2,100px)}.quick-launchpad .quick-card{height:100px;padding:12px}.quick-launchpad .quick-card h3{font-size:16px}.quick-launchpad .quick-card p{font-size:6.7px}}
@media(max-width:820px){.quick-launchpad{margin-top:-40px;padding-bottom:52px}.quick-launchpad .quick-deck{width:calc(100% - 28px);display:grid;grid-auto-flow:column;grid-template-columns:none;grid-template-rows:repeat(2,104px);grid-auto-columns:minmax(155px,44vw);gap:8px;overflow-x:auto;overflow-y:hidden;scroll-snap-type:x mandatory;scrollbar-width:none;padding:9px}.quick-launchpad .quick-card{height:104px;scroll-snap-align:start;opacity:1!important;filter:none!important;transform:none!important}.quick-circuit,.quick-deck-glow{display:none}.quick-launchpad .quick-card p{display:block;font-size:6.8px}.quick-launchpad.quick-focused .quick-card:not(.quick-hot){opacity:1;filter:none;transform:none}}
@media(prefers-reduced-motion:reduce){.quick-launchpad .quick-deck:before,.quick-circuit path{animation:none!important}.quick-packet{display:none}.quick-launchpad .quick-card{opacity:1;filter:none;transform:none}.quick-spark{display:none}}
'''

# Append CSS to the final style block only once.
if '/* Design 42: eight-action kinetic launchpad */' in s:
    raise SystemExit('launchpad CSS already present')
pos=s.rfind('</style>')
if pos<0:
    raise SystemExit('style close not found')
s=s[:pos]+css+s[pos:]

js='''
<script>
;(()=>{
  const section=document.getElementById('quick-actions'),deck=document.getElementById('quickDeck');
  if(!section||!deck)return;
  const cards=[...deck.querySelectorAll('.quick-card')],reduce=matchMedia('(prefers-reduced-motion: reduce)').matches,coarse=matchMedia('(pointer: coarse)').matches;
  const ready=new IntersectionObserver(([entry])=>{if(entry.isIntersecting){section.classList.add('quick-ready');ready.disconnect()}},{threshold:.18});
  ready.observe(section);
  if(reduce||coarse)return;
  const resetCard=card=>{card.style.setProperty('--qrx','0deg');card.style.setProperty('--qry','0deg');card.style.setProperty('--qx','50%');card.style.setProperty('--qy','50%')};
  const burst=card=>{
    const icon=card.querySelector('.q-icon'),cr=card.getBoundingClientRect(),ir=icon?.getBoundingClientRect();
    if(!ir)return;
    const x=ir.left-cr.left+ir.width/2,y=ir.top-cr.top+ir.height/2;
    for(let i=0;i<8;i++){
      const spark=document.createElement('i'),a=(Math.PI*2/8)*i+(Math.random()-.5)*.28,d=20+Math.random()*22;
      spark.className='quick-spark';spark.style.setProperty('--sx0',x+'px');spark.style.setProperty('--sy0',y+'px');spark.style.setProperty('--sdx',(Math.cos(a)*d).toFixed(1)+'px');spark.style.setProperty('--sdy',(Math.sin(a)*d).toFixed(1)+'px');card.appendChild(spark);setTimeout(()=>spark.remove(),700)
    }
  };
  deck.addEventListener('pointermove',e=>{
    const r=deck.getBoundingClientRect();
    deck.style.setProperty('--deck-x',((e.clientX-r.left)/r.width*100).toFixed(2)+'%');
    deck.style.setProperty('--deck-y',((e.clientY-r.top)/r.height*100).toFixed(2)+'%');
  },{passive:true});
  deck.addEventListener('pointerleave',()=>{section.classList.remove('quick-focused');cards.forEach(c=>{c.classList.remove('quick-hot');resetCard(c)});deck.style.setProperty('--deck-x','50%');deck.style.setProperty('--deck-y','50%')});
  cards.forEach(card=>{
    card.addEventListener('pointerenter',()=>{section.classList.add('quick-focused');cards.forEach(c=>c.classList.toggle('quick-hot',c===card));burst(card)});
    card.addEventListener('pointermove',e=>{const r=card.getBoundingClientRect(),x=(e.clientX-r.left)/r.width,y=(e.clientY-r.top)/r.height;card.style.setProperty('--qx',(x*100).toFixed(1)+'%');card.style.setProperty('--qy',(y*100).toFixed(1)+'%');card.style.setProperty('--qry',((x-.5)*7).toFixed(2)+'deg');card.style.setProperty('--qrx',((y-.5)*-6).toFixed(2)+'deg')},{passive:true});
    card.addEventListener('pointerleave',()=>resetCard(card));
    card.addEventListener('focusin',()=>{section.classList.add('quick-focused');cards.forEach(c=>c.classList.toggle('quick-hot',c===card));burst(card)});
    card.addEventListener('focusout',()=>{card.classList.remove('quick-hot');resetCard(card);if(!deck.querySelector(':focus'))section.classList.remove('quick-focused')});
  });
})();
</script>
'''

pos=s.rfind('</body>')
if pos<0:
    raise SystemExit('body close not found')
s=s[:pos]+js+s[pos:]

p.write_text(s)
print('patched 42.html')
