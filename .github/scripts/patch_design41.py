from pathlib import Path
import re

path = Path('41.html')
text = path.read_text(encoding='utf-8')

hero = '''<section class="hero" id="home">
  <div class="hero-copy carousel-copy" aria-live="polite">
    <div class="hero-index"><span id="heroCurrent">01</span> / <span id="heroTotal">02</span> · Telikom Alive</div>

    <div class="hero-copy-rail">
      <article class="hero-copy-slide active" data-copy-slide="0">
        <h1 aria-label="Stay connected from PNG to the world.">
          <span class="line"><span>Stay connected</span></span>
          <span class="line"><span>from <b class="outline">PNG</b></span></span>
          <span class="line"><span class="blue">to the world.</span></span>
        </h1>
        <div class="hero-sub">
          <div class="hero-number">01</div>
          <div>
            <p>Mobile, broadband and everyday connectivity designed to keep Papua New Guinea moving, wherever life takes you.</p>
            <div class="hero-actions">
              <a class="btn fill magnetic" href="#offers"><span>Explore offers</span><span class="arrow">→</span></a>
              <a class="btn magnetic" href="#services"><span>View services</span><span class="arrow">→</span></a>
            </div>
          </div>
        </div>
      </article>

      <article class="hero-copy-slide" data-copy-slide="1" aria-hidden="true">
        <h1 aria-label="More data. More moments. More PNG.">
          <span class="line"><span>More data.</span></span>
          <span class="line"><span>More <b class="outline">moments.</b></span></span>
          <span class="line"><span class="blue">More PNG.</span></span>
        </h1>
        <div class="hero-sub">
          <div class="hero-number">02</div>
          <div>
            <p>Discover Telikom deals built for streaming, sharing, work and the moments that matter every day.</p>
            <div class="hero-actions">
              <a class="btn fill magnetic" href="#offers"><span>See latest deals</span><span class="arrow">→</span></a>
              <a class="btn magnetic" href="#quick-actions"><span>Quick actions</span><span class="arrow">→</span></a>
            </div>
          </div>
        </div>
      </article>
    </div>

    <div class="hero-carousel-controls" aria-label="Hero carousel controls">
      <button class="hero-arrow magnetic" type="button" data-hero-prev aria-label="Previous banner">←</button>
      <div class="hero-dots" role="tablist" aria-label="Choose banner">
        <button class="hero-dot active" type="button" data-hero-dot="0" role="tab" aria-selected="true" aria-label="Banner 1"></button>
        <button class="hero-dot" type="button" data-hero-dot="1" role="tab" aria-selected="false" aria-label="Banner 2"></button>
      </div>
      <button class="hero-arrow magnetic" type="button" data-hero-next aria-label="Next banner">→</button>
      <div class="hero-progress" aria-hidden="true"><span></span></div>
    </div>
  </div>

  <div class="hero-stage" id="heroStage">
    <div class="stage-shell carousel-shell">
      <article class="hero-slide active" data-hero-slide="0">
        <img src="assets/banners/research/telikom-stay-connected-from-png-to-the-world.webp" alt="Telikom Stay Connected from PNG to the World campaign banner">
      </article>
      <article class="hero-slide" data-hero-slide="1" aria-hidden="true">
        <img src="assets/banners/research/telikom-festive-png-telecom-deals.webp" alt="Telikom festive PNG telecom deals campaign banner">
      </article>
      <div class="banner-sheen" aria-hidden="true"></div>
    </div>
  </div>
  <div class="scroll-signal">Scroll to explore <span></span></div>
</section>'''

text, count = re.subn(r'<section class="hero" id="home">.*?</section>', hero, text, count=1, flags=re.S)
if count != 1:
    raise RuntimeError('Could not replace Design 41 hero section')

css = r'''
/* DESIGN 41 MOVING HERO CAROUSEL + FIRST-VIEW COMPOSITION */
@media (min-width:981px){
  .hero{min-height:0;height:calc(100svh - 98px);max-height:690px;padding:94px 4.5vw 52px;grid-template-columns:minmax(0,.86fr) minmax(500px,1.14fr);gap:42px}
  .hero-copy{transform:translateY(calc(var(--scrollY) * .025))}
  .hero-copy-rail{position:relative;height:clamp(286px,39svh,356px)}
  .hero h1{font-size:clamp(48px,5.45vw,88px);line-height:.83;letter-spacing:-.07em;max-width:760px}
  .hero-sub{margin-top:22px;grid-template-columns:44px minmax(0,430px);gap:14px}
  .hero-number{width:44px;height:44px}
  .hero-sub p{font-size:13px;line-height:1.6}
  .hero-actions{margin-top:14px}
  .btn{min-height:42px;padding:0 16px}
  .hero-stage{min-height:0;height:min(50svh,455px);transform:translateY(calc(var(--scrollY) * -.018))}
  .stage-shell{width:min(720px,51vw);aspect-ratio:16/9;border-radius:26px!important}
  .stage-shell:hover{border-radius:26px!important}
  .quick-shell{margin-top:-46px;padding:0 4.5vw}
  .quick-dock{padding:7px;border-radius:20px;gap:5px}
  .quick-action{min-height:82px;padding:12px 14px;gap:11px;border-radius:15px}
  .quick-icon{width:40px;height:40px}
  .quick-action h3{font-size:13px;margin-bottom:3px}
  .quick-action p{font-size:9px}
  .quick-arrow{width:27px;height:27px}
  .secondary-actions{margin-top:10px}
  .scroll-signal{bottom:18px}
}
.carousel-copy{position:relative;z-index:10}
.hero-copy-rail{position:relative}
.hero-copy-slide{position:absolute;inset:0;opacity:0;pointer-events:none;transform:translateX(54px);filter:blur(5px);transition:opacity .38s var(--ease),transform .7s var(--spring),filter .5s var(--ease)}
.hero-copy-slide.active{opacity:1;pointer-events:auto;transform:none;filter:none}
.hero-copy-slide.leaving{opacity:0;transform:translateX(-42px);filter:blur(4px)}
.hero-copy-slide .line>span{animation:none!important;opacity:0;transform:translateY(115%) rotate(1.5deg)}
.hero-copy-slide.active .line:nth-child(1)>span{animation:carouselTextIn .72s .06s var(--spring) both!important}
.hero-copy-slide.active .line:nth-child(2)>span{animation:carouselTextIn .72s .14s var(--spring) both!important}
.hero-copy-slide.active .line:nth-child(3)>span{animation:carouselTextIn .72s .22s var(--spring) both!important}
.hero-copy-slide .hero-sub{opacity:0;transform:translateY(18px)}
.hero-copy-slide.active .hero-sub{animation:carouselSubIn .58s .31s var(--ease) both}
@keyframes carouselTextIn{from{opacity:0;transform:translateY(115%) rotate(1.5deg)}to{opacity:1;transform:none}}
@keyframes carouselSubIn{to{opacity:1;transform:none}}
.carousel-shell{overflow:hidden;background:#dceaf2;isolation:isolate}
.hero-slide{position:absolute;inset:0;opacity:0;transform:translateX(8%) scale(1.035);transition:opacity .56s var(--ease),transform .9s var(--ease);z-index:1;pointer-events:none}
.hero-slide.active{opacity:1;transform:none;z-index:2}
.hero-slide img{position:absolute!important;inset:0!important;width:100%!important;height:100%!important;object-fit:cover!important;object-position:center!important;transform:scale(1.015)!important;filter:none!important;transition:transform 6s linear!important}
.hero-slide.active img{transform:scale(1.06)!important}
.banner-sheen{position:absolute;inset:-40%;z-index:4;pointer-events:none;background:linear-gradient(112deg,transparent 35%,rgba(255,255,255,.28) 49%,transparent 63%);transform:translateX(-70%) rotate(4deg)}
.carousel-shell:hover .banner-sheen{animation:bannerSheen 1.15s var(--ease)}
@keyframes bannerSheen{to{transform:translateX(70%) rotate(4deg)}}
.hero-carousel-controls{display:flex;align-items:center;gap:9px;margin-top:16px;min-height:38px}
.hero-arrow{width:36px;height:36px;border-radius:50%;border:1px solid rgba(16,43,60,.17);background:rgba(255,255,255,.82);display:grid;place-items:center;cursor:pointer;transition:transform .28s var(--spring),background .25s,border-color .25s}
.hero-arrow:hover{transform:scale(1.08);background:#fff;border-color:rgba(8,117,201,.38)}
.hero-dots{display:flex;gap:7px;align-items:center}
.hero-dot{width:8px;height:8px;border:0;padding:0;border-radius:999px;background:#bdd2de;cursor:pointer;transition:width .38s var(--spring),background .25s}
.hero-dot.active{width:28px;background:var(--blue)}
.hero-progress{width:74px;height:2px;background:#d5e2e9;overflow:hidden;margin-left:4px;border-radius:99px}
.hero-progress span{display:block;width:100%;height:100%;background:var(--blue);transform-origin:left;transform:scaleX(0)}
.hero-progress.running span{animation:heroProgress 5.4s linear forwards}
@keyframes heroProgress{to{transform:scaleX(1)}}
@media (min-width:981px) and (max-height:720px){
  .hero{height:calc(100svh - 88px);padding-top:82px;padding-bottom:42px}
  .hero-copy-rail{height:275px}
  .hero h1{font-size:clamp(44px,5vw,72px)}
  .hero-stage{height:min(48svh,390px)}
  .hero-sub p{line-height:1.5}
  .quick-action{min-height:74px}
  .secondary-actions{display:none}
}
@media (max-width:980px){
  .hero{min-height:auto;padding-top:118px;grid-template-columns:1fr}
  .hero-copy-rail{height:390px}
  .hero-stage{min-height:0;height:min(58vw,480px)}
  .stage-shell{width:min(760px,91vw);aspect-ratio:16/9;border-radius:24px!important}
  .quick-shell{margin-top:-28px}
}
@media (max-width:620px){
  .hero-copy-rail{height:345px}
  .hero h1{font-size:clamp(43px,14vw,68px)}
  .hero-stage{height:54vw;min-height:210px}
  .stage-shell{width:92vw;border-radius:18px!important}
  .hero-carousel-controls{margin-top:8px}
}
@media (prefers-reduced-motion:reduce){
  .hero-copy-slide,.hero-slide,.hero-slide img{transition:none!important;animation:none!important}
  .hero-copy-slide.active .line>span,.hero-copy-slide.active .hero-sub{animation:none!important;opacity:1;transform:none}
  .hero-progress{display:none}
}
'''
if 'DESIGN 41 MOVING HERO CAROUSEL' not in text:
    text = text.replace('</style>', css + '\n</style>', 1)

js = r'''
<script>
(() => {
  const hero = document.querySelector('.hero');
  if (!hero) return;
  const visuals = [...hero.querySelectorAll('[data-hero-slide]')];
  const copies = [...hero.querySelectorAll('[data-copy-slide]')];
  const dots = [...hero.querySelectorAll('[data-hero-dot]')];
  const prev = hero.querySelector('[data-hero-prev]');
  const next = hero.querySelector('[data-hero-next]');
  const current = hero.querySelector('#heroCurrent');
  const total = hero.querySelector('#heroTotal');
  const progress = hero.querySelector('.hero-progress');
  const reduced = matchMedia('(prefers-reduced-motion: reduce)');
  const interval = 5400;
  let index = 0, timer = null, paused = false;
  if (!visuals.length || visuals.length !== copies.length) return;
  if (total) total.textContent = String(visuals.length).padStart(2, '0');
  function restartProgress(){
    if (!progress || reduced.matches || paused) return;
    progress.classList.remove('running'); void progress.offsetWidth; progress.classList.add('running');
  }
  function render(nextIndex, userInitiated=false){
    const target = (nextIndex + visuals.length) % visuals.length;
    copies[index]?.classList.add('leaving');
    visuals.forEach((slide,i)=>{const active=i===target;slide.classList.toggle('active',active);slide.setAttribute('aria-hidden',String(!active));});
    copies.forEach((copy,i)=>{const active=i===target;copy.classList.remove('active');copy.setAttribute('aria-hidden',String(!active));});
    dots.forEach((dot,i)=>{const active=i===target;dot.classList.toggle('active',active);dot.setAttribute('aria-selected',String(active));});
    index=target;
    if(current) current.textContent=String(index+1).padStart(2,'0');
    requestAnimationFrame(()=>requestAnimationFrame(()=>{copies.forEach(c=>c.classList.remove('leaving'));copies[index]?.classList.add('active');}));
    restartProgress();
  }
  function stop(){if(timer)clearInterval(timer);timer=null}
  function start(){stop();if(reduced.matches||paused||document.hidden)return;timer=setInterval(()=>render(index+1),interval);restartProgress()}
  function move(delta){render(index+delta,true);start()}
  prev?.addEventListener('click',()=>move(-1));
  next?.addEventListener('click',()=>move(1));
  dots.forEach(dot=>dot.addEventListener('click',()=>{render(Number(dot.dataset.heroDot),true);start()}));
  hero.addEventListener('mouseenter',()=>{paused=true;stop();progress?.classList.remove('running')});
  hero.addEventListener('mouseleave',()=>{paused=false;start()});
  hero.addEventListener('focusin',()=>{paused=true;stop();progress?.classList.remove('running')});
  hero.addEventListener('focusout',e=>{if(!hero.contains(e.relatedTarget)){paused=false;start()}});
  hero.addEventListener('keydown',e=>{if(e.key==='ArrowLeft'){e.preventDefault();move(-1)}if(e.key==='ArrowRight'){e.preventDefault();move(1)}});
  document.addEventListener('visibilitychange',start);
  reduced.addEventListener?.('change',start);
  let touchX=null;
  hero.addEventListener('touchstart',e=>{touchX=e.touches[0]?.clientX??null},{passive:true});
  hero.addEventListener('touchend',e=>{if(touchX==null)return;const end=e.changedTouches[0]?.clientX??touchX;const distance=end-touchX;touchX=null;if(Math.abs(distance)>45)move(distance>0?-1:1)},{passive:true});
  render(0);start();
})();
</script>
'''
if 'const visuals = [...hero.querySelectorAll' not in text:
    text = text.replace('</body>', js + '\n</body>', 1)

path.write_text(text, encoding='utf-8')
