from pathlib import Path
import re

p = Path('40.html')
s = p.read_text(encoding='utf-8')
base = 'https://raw.githubusercontent.com/hamooddevpng/UI-Ideas/main/assets/common/png-people/'

css = r'''
/* Design 40 editorial refinement: less boxy, more image-led, still intentionally simple. */
.section{padding:76px 0}.section.soft{background:#f6f9fb}.section-head{margin-bottom:34px}
.plan-card{border:0!important;box-shadow:0 10px 28px rgba(23,49,66,.07);border-radius:18px!important}.plan-photo{height:190px}.plan-body{padding:24px 24px 26px}

.service-stories{display:grid;grid-template-columns:repeat(3,1fr);gap:30px 24px}.service-story{min-width:0}.service-story img{display:block;width:100%;aspect-ratio:16/10;object-fit:cover;border-radius:16px;margin-bottom:16px}.service-story .eyebrow{display:flex;align-items:center;gap:8px;color:var(--blue);font-size:9px;font-weight:800;letter-spacing:.1em;text-transform:uppercase}.service-story .eyebrow:before{content:"";width:18px;height:2px;background:var(--cyan)}.service-story h3{font-size:20px;line-height:1.12;margin:8px 0 8px}.service-story p{font-size:10.5px;line-height:1.6;color:var(--muted);margin:0 0 12px}.service-story a{font-size:10px;font-weight:800;color:var(--blue)}

.business-section{padding:80px 0;background:#fff}.org-stack{display:grid;gap:28px}.org-row{display:grid;grid-template-columns:1.08fr .92fr;min-height:390px;background:#f4f8fa;border-radius:22px;overflow:hidden}.org-row.reverse{grid-template-columns:.92fr 1.08fr}.org-row.reverse .org-media{order:2}.org-row.reverse .org-copy{order:1}.org-media{min-height:390px;background-size:cover;background-position:center}.org-copy{padding:42px 44px;display:flex;flex-direction:column;justify-content:center}.org-copy small{font-size:9px;letter-spacing:.13em;text-transform:uppercase;font-weight:800;color:var(--blue)}.org-copy h3{font-size:clamp(30px,3.2vw,46px);line-height:1.02;margin:10px 0 14px}.org-copy p{font-size:11px;line-height:1.65;color:#59717f;margin:0;max-width:560px}.org-points{display:flex;gap:8px;flex-wrap:wrap;margin:22px 0}.org-points span{background:#fff;border-radius:999px;padding:8px 11px;font-size:9px;font-weight:800;color:#496474}.org-cta{display:inline-flex;align-self:flex-start;background:var(--blue);color:#fff;padding:11px 14px;border-radius:8px;font-size:10px;font-weight:800}.org-row.government{background:#eaf6fc}.org-row.government .org-cta{background:#173142}

.updates-layout{display:grid;grid-template-columns:.78fr 1.22fr;gap:48px;align-items:start}.notice-board{background:#eef7fc;border-radius:18px;padding:22px 24px}.notice-board-head{display:flex;align-items:center;justify-content:space-between;margin-bottom:8px}.notice-board-head h3{margin:0;font-size:18px}.notice-board-head span{font-size:9px;font-weight:800;color:var(--blue);background:#fff;padding:6px 8px;border-radius:999px}.notice-row{position:relative;padding:18px 8px 18px 18px;border-bottom:1px solid #d7e7f0}.notice-row:last-child{border-bottom:0}.notice-row:before{content:"";position:absolute;left:0;top:20px;width:5px;height:5px;border-radius:50%;background:var(--blue)}.notice-row .meta{display:flex;gap:8px;align-items:center;margin-bottom:5px}.notice-row .badge{font-size:8px;font-weight:900;letter-spacing:.08em;text-transform:uppercase;color:#fff;background:var(--blue);padding:4px 6px;border-radius:4px}.notice-row time{font-size:9px;color:#7a8f9a}.notice-row strong{display:block;font-size:12px;line-height:1.35}.notice-row p{font-size:10px;line-height:1.5;color:#607784;margin:5px 0 8px}.notice-row a{font-size:9px;font-weight:800;color:var(--blue)}
.news-block h3{font-size:18px;margin:0 0 16px}.news-grid{display:grid;grid-template-columns:1.15fr .85fr;gap:20px}.news-feature,.news-small{position:relative;overflow:hidden;border-radius:18px;background:#173142;color:#fff}.news-feature{min-height:390px}.news-small{min-height:185px}.news-feature img,.news-small img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}.news-feature:after,.news-small:after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,transparent 28%,rgba(9,32,46,.88) 100%)}.news-copy{position:absolute;z-index:2;left:22px;right:22px;bottom:20px}.news-copy .meta{font-size:8px;font-weight:800;letter-spacing:.1em;text-transform:uppercase;color:#ccecff}.news-copy h4{font-size:20px;line-height:1.12;margin:7px 0 7px}.news-small .news-copy h4{font-size:15px}.news-copy p{font-size:10px;line-height:1.45;color:#e3eef3;margin:0 0 10px}.news-copy a{font-size:9px;font-weight:800;color:#fff}.news-side{display:grid;gap:20px}

@media(max-width:900px){.service-stories{grid-template-columns:1fr 1fr}.org-row,.org-row.reverse{grid-template-columns:1fr}.org-row.reverse .org-media,.org-row.reverse .org-copy{order:initial}.org-media{min-height:300px}.org-copy{padding:34px}.updates-layout{grid-template-columns:1fr}.news-grid{grid-template-columns:1fr}.news-feature{min-height:330px}.news-side{grid-template-columns:1fr 1fr}.news-small{min-height:220px}}
@media(max-width:600px){.service-stories{grid-template-columns:1fr;gap:28px}.service-story img{aspect-ratio:16/9}.org-row{border-radius:16px}.org-media{min-height:240px}.org-copy{padding:28px 24px}.org-points{margin:18px 0}.updates-layout{gap:30px}.notice-board{padding:18px}.news-side{grid-template-columns:1fr}.news-feature{min-height:300px}.news-small{min-height:230px}}
'''

if '/* Design 40 editorial refinement:' not in s:
    s = s.replace('</style>', css + '\n</style>', 1)

services = f'''<section class="section soft" id="services"><div class="wrap"><div class="section-head"><div class="copy"><span class="kicker">Service categories</span><h2>Services for the way PNG connects.</h2><p>Each service has a clearer visual story, so customers can understand the use case before they click.</p></div></div><div class="service-stories">
  <article class="service-story"><img src="{base}community-harbour.jpg" alt="People in Papua New Guinea using mobile connectivity by the harbour" loading="lazy" decoding="async"><div class="eyebrow">Mobile</div><h3>Everyday mobile connection</h3><p>Prepaid, postpaid, data and SIM services for staying connected wherever the day takes you.</p><a href="#">Explore mobile →</a></article>
  <article class="service-story"><img src="{base}family-digital.jpg" alt="A Papua New Guinea family using a tablet at home" loading="lazy" decoding="async"><div class="eyebrow">Home Internet</div><h3>Internet for home life</h3><p>Plans, availability, setup and support for families, study, entertainment and everyday use.</p><a href="#">Explore home internet →</a></article>
  <article class="service-story"><img src="{base}young-professionals.jpg" alt="Young professionals in Papua New Guinea using connected devices" loading="lazy" decoding="async"><div class="eyebrow">Business</div><h3>Connectivity that keeps work moving</h3><p>Business internet, managed connectivity and reliable communication for growing organisations.</p><a href="#business">Explore business →</a></article>
  <article class="service-story"><img src="{base}market-connectivity.jpg" alt="People using a smartphone at a Papua New Guinea market" loading="lazy" decoding="async"><div class="eyebrow">Regional & Remote</div><h3>Connection beyond the city</h3><p>Regional enquiries and specialist connectivity pathways for communities and remote operations.</p><a href="#">Explore regional services →</a></article>
  <article class="service-story"><img src="{base}community-harbour.jpg" alt="People using mobile services in an urban Papua New Guinea setting" loading="lazy" decoding="async"><div class="eyebrow">Coverage & Stores</div><h3>Find service where you are</h3><p>Check availability, understand coverage and find a Telikom location close to you.</p><a href="#">Check coverage →</a></article>
  <article class="service-story"><img src="{base}family-digital.jpg" alt="Family using connected digital services at home" loading="lazy" decoding="async"><div class="eyebrow">Support</div><h3>Help when you need it</h3><p>Troubleshooting, account help, contact options and self service in one straightforward place.</p><a href="#support">Get support →</a></article>
</div></div></section>'''

business = f'''<section class="business-section" id="business"><div class="wrap"><div class="section-head"><div class="copy"><span class="kicker">Business & Government</span><h2>Built for organisations that keep PNG moving.</h2><p>Two clear pathways with more context, stronger imagery and simple calls to action.</p></div></div><div class="org-stack">
  <article class="org-row business"><div class="org-media" style="background-image:url('{base}young-professionals.jpg')" role="img" aria-label="Young professionals in Papua New Guinea using connected devices"></div><div class="org-copy"><small>For business</small><h3>Connect your organisation with confidence.</h3><p>From day-to-day internet to managed connectivity and regional requirements, Telikom gives businesses a direct route to the right solution.</p><div class="org-points"><span>Business Internet</span><span>Managed Connectivity</span><span>Voice</span><span>Regional Solutions</span></div><a class="org-cta" href="#">Explore business solutions →</a></div></article>
  <article class="org-row government reverse"><div class="org-media" style="background-image:url('{base}market-connectivity.jpg')" role="img" aria-label="Community connectivity in Papua New Guinea"></div><div class="org-copy"><small>For government</small><h3>Reliable connection for public services.</h3><p>Dedicated pathways for government connectivity, regional services and specialist enquiries that support people and communities across PNG.</p><div class="org-points"><span>Government Solutions</span><span>Regional Services</span><span>Specialist Support</span></div><a class="org-cta" href="#">View government services →</a></div></article>
</div></div></section>'''

updates = f'''<section class="section" id="updates"><div class="wrap"><div class="section-head"><div class="copy"><span class="kicker">Notices & news</span><h2>Important updates and stories from Telikom.</h2><p>Notices stay practical and easy to scan. News is presented visually, like real editorial content.</p></div></div><div class="updates-layout">
  <aside class="notice-board" aria-label="Service notices"><div class="notice-board-head"><h3>Service notices</h3><span>Latest updates</span></div>
    <article class="notice-row"><div class="meta"><span class="badge">Network</span><time>Today</time></div><strong>Network and service information</strong><p>Verified service advisories, planned maintenance and restoration updates appear here.</p><a href="#">View notice →</a></article>
    <article class="notice-row"><div class="meta"><span class="badge">Customer</span><time>Recent</time></div><strong>Customer service updates</strong><p>Practical information affecting service access, support channels and customer care.</p><a href="#">View notice →</a></article>
    <article class="notice-row"><div class="meta"><span class="badge">Important</span><time>Recent</time></div><strong>Important announcements</strong><p>High-priority information can stand out without competing with the news section.</p><a href="#">View notice →</a></article>
  </aside>
  <div class="news-block"><h3>Latest news</h3><div class="news-grid">
    <article class="news-feature"><img src="{base}community-harbour.jpg" alt="People in Papua New Guinea staying connected near the harbour" loading="lazy" decoding="async"><div class="news-copy"><div class="meta">Community · PNG</div><h4>Connecting people and places across Papua New Guinea</h4><p>Stories about connectivity, communities and the role the network plays in everyday life.</p><a href="#">Read story →</a></div></article>
    <div class="news-side">
      <article class="news-small"><img src="{base}young-professionals.jpg" alt="Young professionals using digital connectivity in Papua New Guinea" loading="lazy" decoding="async"><div class="news-copy"><div class="meta">Business</div><h4>Digital connection supporting the next generation of work</h4><a href="#">Read story →</a></div></article>
      <article class="news-small"><img src="{base}market-connectivity.jpg" alt="People using mobile connectivity at a market in Papua New Guinea" loading="lazy" decoding="async"><div class="news-copy"><div class="meta">Community</div><h4>Keeping local businesses and communities connected</h4><a href="#">Read story →</a></div></article>
    </div>
  </div>
</div></div></section>'''

s, n1 = re.subn(r'<section class="section soft" id="services">.*?</section>\n<section class="business-section" id="business">', services + '\n<section class="business-section" id="business">', s, count=1, flags=re.S)
s, n2 = re.subn(r'<section class="business-section" id="business">.*?</section>\n<section class="png-strip" id="story">', business + '\n<section class="png-strip" id="story">', s, count=1, flags=re.S)
s, n3 = re.subn(r'<section class="section" id="updates">.*?</section>\n<section class="section soft" id="support">', updates + '\n<section class="section soft" id="support">', s, count=1, flags=re.S)

if (n1, n2, n3) != (1, 1, 1):
    raise SystemExit(f'Replacement counts were {(n1, n2, n3)}')

checks = ['service-stories','org-stack','notice-board','news-grid','community-harbour.jpg','family-digital.jpg','market-connectivity.jpg','young-professionals.jpg']
for token in checks:
    if token not in s:
        raise SystemExit(f'Missing expected token: {token}')

p.write_text(s, encoding='utf-8')
