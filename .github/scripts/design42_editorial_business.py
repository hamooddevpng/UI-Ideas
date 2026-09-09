from pathlib import Path
import re

root=Path('.')
p=Path('42.html')
s=p.read_text()

# Purge the disliked Unsplash image everywhere in text assets.
bad_id='photo-1728957467648-ad5e95eafa1e'
replacement='assets/design42/png-photographer.jpg'
pattern=re.compile(r'https://images\.unsplash\.com/'+re.escape(bad_id)+r'[^"\'\)\s<]*')
text_suffixes={'.html','.md','.json','.css','.js','.txt','.yml','.yaml'}
for q in root.rglob('*'):
    if not q.is_file() or '.git' in q.parts or q.suffix.lower() not in text_suffixes:
        continue
    try:
        t=q.read_text()
    except UnicodeDecodeError:
        continue
    nt=pattern.sub(replacement,t)
    if nt!=t:
        q.write_text(nt)

# Re-read 42 after repo-wide replacement.
s=p.read_text()
s=re.sub(r'(<img[^>]+src="assets/design42/png-photographer\.jpg"[^>]+alt=")[^"]*(")',
         r'\1Papua New Guinea photographer working outdoors\2',s,count=1)

start=s.find('<div class="business-portfolio reveal" id="businessPortfolio">')
if start<0:
    raise SystemExit('business portfolio start missing')
close_marker='\n    </div>\n  </div>\n</section>\n<section class="png-story'
close_pos=s.find(close_marker,start)
if close_pos<0:
    raise SystemExit('business portfolio close marker missing')
end=close_pos+len('\n    </div>')

new_markup='''<div class="business-portfolio reveal" id="businessPortfolio">
      <article class="portfolio-feature" id="portfolioFeature">
        <div class="portfolio-feature-media"><img id="portfolioImage" src="assets/common/web-sourced/telikom/business-data.jpg" alt="Telikom business connectivity service in Papua New Guinea" loading="lazy" decoding="async"><span>FEATURED SERVICE</span></div>
        <div class="portfolio-detail"><small>BUSINESS PORTFOLIO</small><b id="portfolioTitle">Business Data</b><span id="portfolioDetail">IP VPN · MPLS up to 900 Mbps · managed network · 99% IP VLAN availability</span><a id="portfolioFeatureLink" href="#business">Open service page ↗</a></div>
      </article>
      <div class="portfolio-strip" role="tablist" aria-label="Telikom business services">
        <button class="portfolio-chip active" type="button" data-portfolio="0" data-side="business"><span class="portfolio-thumb"><img src="assets/common/web-sourced/telikom/business-data.jpg" alt="Business Data service" loading="lazy"></span><span class="portfolio-card-copy"><small>DATA</small><b>Business Data</b><em>IP VPN · MPLS</em></span></button>
        <button class="portfolio-chip" type="button" data-portfolio="1" data-side="business"><span class="portfolio-thumb"><img src="assets/common/web-sourced/telikom/business-systems.jpg" alt="Business Systems service" loading="lazy"></span><span class="portfolio-card-copy"><small>COLLABORATION</small><b>Business Systems</b><em>MiVoice · MiCollab</em></span></button>
        <button class="portfolio-chip" type="button" data-portfolio="2" data-side="business"><span class="portfolio-thumb"><img src="assets/common/web-sourced/telikom/news-01.jpg" alt="SIP Trunk service" loading="lazy"></span><span class="portfolio-card-copy"><small>VOICE</small><b>SIP Trunk</b><em>Voice over IP</em></span></button>
        <button class="portfolio-chip" type="button" data-portfolio="3" data-side="government"><span class="portfolio-thumb"><img src="assets/common/web-sourced/telikom/news-02.jpg" alt="Co-Location service" loading="lazy"></span><span class="portfolio-card-copy"><small>INFRASTRUCTURE</small><b>Co-Location</b><em>Secure infrastructure</em></span></button>
        <button class="portfolio-chip" type="button" data-portfolio="4" data-side="government"><span class="portfolio-thumb"><img src="assets/common/web-sourced/telikom/mt-kegum.jpg" alt="VSAT remote connectivity service" loading="lazy"></span><span class="portfolio-card-copy"><small>REMOTE</small><b>VSAT</b><em>Remote sites</em></span></button>
        <button class="portfolio-chip" type="button" data-portfolio="5" data-side="business"><span class="portfolio-thumb"><img src="assets/common/web-sourced/telikom/news-06.jpg" alt="Web and Hosting service" loading="lazy"></span><span class="portfolio-card-copy"><small>DIGITAL</small><b>Web &amp; Hosting</b><em>Hosting · email · backup</em></span></button>
        <button class="portfolio-chip" type="button" data-portfolio="6" data-side="business"><span class="portfolio-thumb"><img src="assets/common/web-sourced/telikom/news-07.jpg" alt="CUG and PUG business mobile groups" loading="lazy"></span><span class="portfolio-card-copy"><small>MOBILE</small><b>CUG / PUG</b><em>Business mobile groups</em></span></button>
      </div>
    </div>'''
s=s[:start]+new_markup+s[end:]

css=r'''
/* Design 42: editorial Business/Government service rail */
.business-dual .dual-world-top{font-size:8px!important;letter-spacing:.12em!important}
.business-dual .dual-world-copy>small{font-size:8px!important;line-height:1.25!important}
.business-dual .dual-world-copy h3{font-size:clamp(31px,2.75vw,42px)!important;line-height:.94!important;margin:7px 0 8px!important}
.business-dual .dual-world-copy>p{font-size:10.5px!important;line-height:1.48!important;max-width:420px!important}
.business-dual .dual-stats span{width:98px!important;padding:9px 10px!important}
.business-dual .dual-stats b{font-size:12.5px!important}
.business-dual .dual-stats small{font-size:6.4px!important;line-height:1.3!important}

.business-portfolio{display:grid!important;grid-template-columns:330px minmax(0,1fr)!important;gap:12px!important;align-items:stretch!important;min-height:154px!important}
.portfolio-feature{position:relative;display:grid;grid-template-columns:42% 1fr;min-width:0;overflow:hidden;border:1px solid rgba(22,101,135,.13);border-radius:22px;background:rgba(255,255,255,.86);box-shadow:0 14px 34px rgba(24,89,113,.07)}
.portfolio-feature-media{position:relative;min-width:0;overflow:hidden;background:#dceef4}
.portfolio-feature-media:after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,transparent 38%,rgba(4,31,43,.48))}
.portfolio-feature-media img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;transition:opacity .18s ease,transform .6s var(--spring)}
.portfolio-feature:hover .portfolio-feature-media img{transform:scale(1.045)}
.portfolio-feature-media img.swapping{opacity:.18;transform:scale(1.07)}
.portfolio-feature-media>span{position:absolute;z-index:2;left:11px;bottom:10px;color:#fff;font-size:6px;font-weight:800;letter-spacing:.13em}
.business-dual .portfolio-detail{padding:14px 15px!important;border:0!important;border-radius:0!important;background:transparent!important;box-shadow:none!important;display:flex!important;flex-direction:column!important;justify-content:center!important;min-width:0}
.business-dual .portfolio-detail small{font-size:7px!important;letter-spacing:.13em!important;color:#5d8191!important}
.business-dual .portfolio-detail b{font-family:"Space Grotesk";font-size:22px!important;line-height:1!important;letter-spacing:-.035em;color:#15394a!important;margin:6px 0 7px!important}
.business-dual .portfolio-detail span{font-size:8px!important;line-height:1.45!important;color:#637f8b!important;display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical;overflow:hidden}
.business-dual .portfolio-detail a{margin-top:8px;font-size:7.5px;font-weight:800;color:#0875c9}

.business-dual .portfolio-strip{display:grid!important;grid-template-columns:repeat(7,minmax(0,1fr))!important;gap:8px!important;min-width:0!important;overflow:visible!important}
.business-dual .portfolio-chip{position:relative!important;height:154px!important;min-width:0!important;padding:0!important;border-radius:20px!important;overflow:hidden!important;border:1px solid rgba(21,102,137,.13)!important;background:#dceef4!important;color:#fff!important;box-shadow:0 10px 24px rgba(25,91,116,.055)!important;text-align:left!important;isolation:isolate;transform:none!important}
.business-dual .portfolio-chip:before{display:none!important}
.portfolio-thumb{position:absolute;inset:0;z-index:0}
.portfolio-thumb:after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(5,35,47,.02) 18%,rgba(5,35,47,.18) 50%,rgba(5,28,39,.88) 100%)}
.portfolio-thumb img{width:100%;height:100%;object-fit:cover;display:block;filter:saturate(.9) contrast(1.02);transition:transform .5s var(--spring),filter .28s}
.portfolio-card-copy{position:absolute;z-index:2;left:11px;right:10px;bottom:10px;display:block;transform:translateY(0);transition:transform .3s var(--spring)}
.portfolio-card-copy small{display:block!important;color:#a9e8ff!important;font-size:5.8px!important;letter-spacing:.12em!important;font-style:normal!important;font-weight:800!important;margin:0 0 4px!important}
.portfolio-card-copy b{display:block!important;font-family:"Space Grotesk";font-size:10.5px!important;line-height:1.02!important;letter-spacing:-.025em;color:#fff!important}
.portfolio-card-copy em{display:block;font-style:normal;font-size:6.5px;line-height:1.25;color:#d7e8ee;margin-top:4px}
.business-dual .portfolio-chip:hover,.business-dual .portfolio-chip:focus-visible,.business-dual .portfolio-chip.active{transform:translateY(-5px)!important;border-color:rgba(8,117,201,.34)!important;box-shadow:0 17px 34px rgba(8,93,135,.14)!important;outline:none!important}
.business-dual .portfolio-chip:hover .portfolio-thumb img,.business-dual .portfolio-chip:focus-visible .portfolio-thumb img,.business-dual .portfolio-chip.active .portfolio-thumb img{transform:scale(1.075);filter:saturate(1.03) contrast(1.04)}
.business-dual .portfolio-chip.active:after{content:"";position:absolute;z-index:3;left:11px;top:10px;width:6px;height:6px;border-radius:50%;background:#8ee6ff;box-shadow:0 0 0 5px rgba(142,230,255,.14)}

@media(min-width:821px){
  .business-dual{padding-top:24px!important;padding-bottom:24px!important}
  .business-dual-shell{height:min(88vh,790px)!important;min-height:710px!important;display:grid!important;grid-template-rows:auto minmax(0,1fr) 154px!important;gap:14px!important}
  .business-dual-head{margin:0!important}
  .business-dual-stage{min-height:0!important;margin-top:0!important}
  .business-dual .dual-world{height:auto!important;min-height:0!important}
  .business-dual .dual-art-wrap{inset:28px 4px 128px!important}
}
@media(max-height:780px) and (min-width:821px){
  .business-dual-shell{height:min(88vh,680px)!important;min-height:620px!important;grid-template-rows:auto minmax(0,1fr) 136px!important;gap:10px!important}
  .business-portfolio{min-height:136px!important}
  .business-dual .portfolio-chip{height:136px!important}
  .business-dual .dual-art-wrap{inset:23px 4px 116px!important}
  .business-dual .dual-world-copy h3{font-size:30px!important}
  .business-dual .dual-world-copy>p{font-size:9.5px!important}
}
@media(max-width:1100px) and (min-width:821px){
  .business-portfolio{grid-template-columns:280px minmax(0,1fr)!important}
  .portfolio-feature{grid-template-columns:38% 1fr}
  .business-dual .portfolio-detail b{font-size:19px!important}
  .portfolio-card-copy b{font-size:9px!important}
}
@media(max-width:820px){
  .business-portfolio{display:block!important;min-height:0!important}
  .portfolio-feature{height:260px;grid-template-columns:44% 1fr;margin-bottom:12px}
  .business-dual .portfolio-strip{display:flex!important;overflow-x:auto!important;gap:10px!important;padding:2px 1px 12px;scroll-snap-type:x mandatory}
  .business-dual .portfolio-chip{flex:0 0 180px!important;height:190px!important;scroll-snap-align:start}
  .business-dual .dual-world-copy>small{font-size:7px!important}
  .business-dual .dual-world-copy h3{font-size:34px!important}
  .business-dual .dual-world-copy>p{font-size:10px!important}
}
'''
if 'Design 42: editorial Business/Government service rail' in s:
    raise SystemExit('editorial business patch already applied')
pos=s.rfind('</style>')
if pos<0:
    raise SystemExit('style close missing')
s=s[:pos]+css+s[pos:]

js=r'''
const editorialPortfolio=[
  {title:'Business Data',detail:'IP VPN · MPLS up to 900 Mbps · managed network · 99% IP VLAN availability',image:'assets/common/web-sourced/telikom/business-data.jpg'},
  {title:'Business Systems',detail:'MiVoice, MX-ONE and MiCollab tools for business calling, messaging and collaboration.',image:'assets/common/web-sourced/telikom/business-systems.jpg'},
  {title:'SIP Trunk',detail:'Voice over IP connectivity for modern business phone systems and scalable enterprise calling.',image:'assets/common/web-sourced/telikom/news-01.jpg'},
  {title:'Co-Location',detail:'Secure infrastructure space for critical systems, hosting, backup and resilient business services.',image:'assets/common/web-sourced/telikom/news-02.jpg'},
  {title:'VSAT',detail:'Remote telecommunications connectivity for organisations and sites beyond the usual network edge.',image:'assets/common/web-sourced/telikom/mt-kegum.jpg'},
  {title:'Web & Hosting',detail:'Hosting, email and backup services that support an organisation’s digital presence and operations.',image:'assets/common/web-sourced/telikom/news-06.jpg'},
  {title:'CUG / PUG',detail:'Business mobile groups that keep teams connected with practical closed-user communication options.',image:'assets/common/web-sourced/telikom/news-07.jpg'}
],editorialImage=document.getElementById('portfolioImage'),editorialTitle=document.getElementById('portfolioTitle'),editorialDetail=document.getElementById('portfolioDetail'),editorialChips=[...document.querySelectorAll('#businessPortfolio .portfolio-chip')];
if(editorialImage&&editorialTitle&&editorialDetail&&editorialChips.length){
  let editorialSwap=0;
  const syncEditorial=i=>{
    const d=editorialPortfolio[i];if(!d)return;
    editorialChips.forEach((c,n)=>c.classList.toggle('active',n===i));
    editorialTitle.textContent=d.title;editorialDetail.textContent=d.detail;
    if(editorialImage.getAttribute('src')!==d.image){
      clearTimeout(editorialSwap);editorialImage.classList.add('swapping');
      editorialSwap=setTimeout(()=>{editorialImage.src=d.image;editorialImage.alt=d.title+' service in Papua New Guinea';editorialImage.classList.remove('swapping')},95)
    }
  };
  editorialChips.forEach((chip,i)=>{
    chip.addEventListener('pointerenter',()=>syncEditorial(i));
    chip.addEventListener('focus',()=>syncEditorial(i));
    chip.addEventListener('click',()=>syncEditorial(i));
  });
}
'''
pos=s.rfind('})();')
if pos<0:
    raise SystemExit('main IIFE end missing')
s=s[:pos]+js+s[pos:]

p.write_text(s)

attr=Path('assets/design42/ATTRIBUTION.md')
existing=attr.read_text() if attr.exists() else '# Design 42 image sources\n'
entry='''\n## PNG photographer replacement\n- Used in: service imagery where the removed Ela Beach image previously appeared\n- Photographer: Asso Myron\n- Source: https://unsplash.com/photos/man-with-camera-on-tripod-looking-up-6h253CDCK2k\n- Location: Papua New Guinea\n- License: Unsplash License\n- Note: mirrored locally for the design prototype.\n'''
if '## PNG photographer replacement' not in existing:
    attr.write_text(existing.rstrip()+entry+'\n')
