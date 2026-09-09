from pathlib import Path
import re

path = Path('41.html')
text = path.read_text(encoding='utf-8')

header_logo = '<a class="brand" href="#top" aria-label="Telikom home"><img class="brand-logo" src="assets/brand/telikom-logo.png" alt="Telikom, Connecting you Anywhere Anytime"></a>'
text, header_count = re.subn(r'<a class="brand" href="#top" aria-label="Telikom home">.*?</a>', header_logo, text, count=1, flags=re.S)
if header_count != 1:
    raise SystemExit(f'Expected one header brand replacement, got {header_count}')

old_footer = '<div class="footer-brand"><div class="wordmark">teli<em>kom</em></div><p>'
new_footer = '<div class="footer-brand"><a class="footer-logo-plate" href="#top" aria-label="Telikom home"><img class="footer-logo" src="assets/brand/telikom-logo.png" alt="Telikom, Connecting you Anywhere Anytime"></a><p>'
if old_footer not in text:
    raise SystemExit('Footer wordmark target not found')
text = text.replace(old_footer, new_footer, 1)

css_marker = '/* DESIGN 41 OFFICIAL BRAND AND REACTIVE HOVER SYSTEM */'
if css_marker not in text:
    css = r'''

/* DESIGN 41 OFFICIAL BRAND AND REACTIVE HOVER SYSTEM */
.brand{min-width:154px;overflow:visible}
.brand-logo{display:block;width:auto;height:44px;max-width:174px;object-fit:contain;object-position:left center;filter:none!important}
.compact .brand-logo{height:40px}
.footer-logo-plate{display:inline-flex;align-items:center;justify-content:center;width:min(306px,100%);padding:11px 14px;border-radius:18px;background:#fff;border:1px solid rgba(255,255,255,.2);box-shadow:0 18px 55px rgba(0,0,0,.13);overflow:hidden}
.footer-logo{display:block;width:100%;height:auto;max-height:96px;object-fit:contain;filter:none!important}
.footer-brand p{margin-top:18px}
.reactive-target,.reactive-soft{--rx:0px;--ry:0px;--rs:1;translate:var(--rx) var(--ry);scale:var(--rs);transition:translate .34s var(--spring),scale .34s var(--spring),box-shadow .28s var(--ease),opacity .24s,border-color .24s,background-color .24s,color .24s}
.reactive-soft{transition-duration:.42s}
@media(hover:hover) and (pointer:fine){
  .reactive-target:hover{--rs:1.018}
  .reactive-soft:hover{--rs:1.007}
  .brand:hover{--rs:1.025}
  .brand:hover .brand-logo{filter:none!important}
  .nav a:hover,.secondary-actions a:hover,.view-link:hover,.offer-link:hover,.footer-col a:hover,.chat-panel a:hover{--rs:1.028}
  .hero-copy-slide .line:hover{--rs:1.008}
  .hero-index:hover,.kicker:hover,.tag:hover,.prototype-note:hover,.micro:hover{--rs:1.045}
  .hero-number:hover,.action-icon:hover,.cmd-num:hover{--rs:1.08}
  .hero-arrow:hover,.hero-dot:hover,.search-btn:hover,.menu-btn:hover,.chat-button:hover{--rs:1.065}
  .quick-action:hover{--rs:1.014;box-shadow:0 19px 42px rgba(31,84,113,.09)}
  .quick-action:hover .action-icon{transform:translateY(-4px) rotate(-4deg) scale(1.07)}
  .quick-action:hover .quick-arrow{transform:translateX(6px) scale(1.08)}
  .offer:hover{--rs:1.009;box-shadow:0 26px 64px rgba(31,84,113,.08)}
  .service-row:hover{--rs:1.008}
  .notice:hover{--rs:1.006}
  .news-card:hover{--rs:1.012}
  .service-preview:hover,.business-media:hover,.story-media:hover,.support-side:hover,.carousel-shell:hover{--rs:1.008}
  .section-head h2:hover,.story-copy h2:hover,.support-copy h2:hover,.business-copy h2:hover,.update-column h3:hover{--rs:1.008}
  .section-head p:hover,.story-copy p:hover,.support-copy p:hover,.business-copy p:hover,.footer-brand p:hover{--rs:1.006}
  .footer-logo-plate:hover{--rs:1.018;box-shadow:0 24px 70px rgba(0,0,0,.2)}
  .footer-logo-plate:hover .footer-logo{scale:1.012}
  .offer img,.service-preview img,.business-media img,.story-media img,.news-card img,.footer-logo,.brand-logo{transition:scale .55s var(--spring),translate .55s var(--spring)}
  .offer:hover img,.service-preview:hover img,.business-media:hover img,.story-media:hover img{scale:1.035}
  .support-side:before,.support-side:after{transition:transform .7s var(--spring)}
  .support-side:hover:before{transform:translate(-16px,12px) scale(1.07)}
  .support-side:hover:after{transform:translate(10px,-8px) scale(.94)}
  .news-card:hover:before{scale:1.08}
  .footer-watermark{transition:letter-spacing .7s var(--spring),color .5s,translate .7s var(--spring)}
  footer:hover .footer-watermark{letter-spacing:-.07em;color:rgba(255,255,255,.045);translate:9px 0}
  .scroll-signal{transition:translate .35s var(--spring),color .25s}
  .scroll-signal:hover{translate:8px 0;color:var(--blue)}
  .hero-progress{transition:scale .3s var(--spring)}
  .hero-progress:hover{scale:1.08 1.8}
}
@media(max-width:700px){
  .brand-logo{height:38px;max-width:138px}
  .compact .brand-logo{height:35px}
  .footer-logo-plate{width:min(270px,100%)}
}
@media(prefers-reduced-motion:reduce){
  .reactive-target,.reactive-soft{translate:0 0!important;scale:1!important}
  .footer-watermark{translate:0!important}
}
'''
    text = text.replace('</style>', css + '\n</style>', 1)

js_marker = 'DESIGN 41 POINTER REACTIVITY'
if js_marker not in text:
    js = r'''
<script>
/* DESIGN 41 POINTER REACTIVITY */
(() => {
  const fine = matchMedia('(hover:hover) and (pointer:fine)');
  const reduced = matchMedia('(prefers-reduced-motion: reduce)');
  if (!fine.matches || reduced.matches) return;

  const configs = [
    {selector:'.brand,.nav a,.header-actions a,.header-actions button,.btn,.hero-arrow,.hero-dot,.secondary-actions a,.view-link,.offer-link,.service-row,.notice a,.news-card a,.support-command a,.chat-panel a,.footer-col a,.footer-logo-plate,.chat-button', max:6, dir:1, cls:'reactive-target'},
    {selector:'.hero-index,.hero-number,.kicker,.tag,.prototype-note,.micro,.action-icon,.quick-arrow,.cmd-num,.notice-dot', max:5, dir:-1, cls:'reactive-target'},
    {selector:'.quick-action,.offer,.service-preview,.business-media,.story-media,.notice,.news-card,.support-side,.carousel-shell', max:3.2, dir:1, cls:'reactive-soft'},
    {selector:'.hero-copy-slide .line,.section-head h2,.section-head p,.story-copy h2,.story-copy p,.business-copy h2,.business-copy p,.support-copy h2,.support-copy p,.update-column h3,.footer-brand p,.footer-col h5', max:2.5, dir:1, cls:'reactive-soft'}
  ];

  const seen = new Set();
  configs.forEach(({selector,max,dir,cls}) => {
    document.querySelectorAll(selector).forEach(el => {
      if (seen.has(el)) return;
      seen.add(el);
      el.classList.add(cls);
      el.addEventListener('pointermove', e => {
        const r = el.getBoundingClientRect();
        if (!r.width || !r.height) return;
        const x = Math.max(-1, Math.min(1, (e.clientX - (r.left + r.width / 2)) / (r.width / 2)));
        const y = Math.max(-1, Math.min(1, (e.clientY - (r.top + r.height / 2)) / (r.height / 2)));
        el.style.setProperty('--rx', `${(x * max * dir).toFixed(2)}px`);
        el.style.setProperty('--ry', `${(y * max * dir).toFixed(2)}px`);
      }, {passive:true});
      el.addEventListener('pointerleave', () => {
        el.style.setProperty('--rx','0px');
        el.style.setProperty('--ry','0px');
      }, {passive:true});
    });
  });
})();
</script>
'''
    text = text.replace('</body>', js + '\n</body>', 1)

path.write_text(text, encoding='utf-8')
