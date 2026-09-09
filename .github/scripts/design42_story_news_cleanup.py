from pathlib import Path
p=Path('42.html')
s=p.read_text()

old_img='''<img class="png-story-photo" src="assets/design42/louisiade-archipelago-nasa.jpg" alt="Aerial view of the Louisiade Archipelago and coral reefs in Papua New Guinea" loading="lazy" decoding="async">'''
new_img='''<img class="png-story-photo" src="assets/design42/milne-bay-aerial.jpg" alt="Aerial view of Tawali Resort coastline and coral reefs in Milne Bay, Papua New Guinea" loading="lazy" decoding="async">'''
if old_img not in s:
    raise SystemExit('PNG story image target missing')
s=s.replace(old_img,new_img,1)

old_notices='''<div class="notices">
      <div class="notice-row active" data-update-preview="0"><div class="notice-head"><span class="status-chip">Service</span><b>Planned service information</b><span>＋</span></div><div class="notice-body">Service notices and maintenance information can be published here.</div></div>
      <div class="notice-row" data-update-preview="1"><div class="notice-head"><span class="status-chip">Customer</span><b>Customer updates</b><span>＋</span></div><div class="notice-body">Important information for Telikom customers can be placed here.</div></div>
      <div class="notice-row" data-update-preview="2"><div class="notice-head"><span class="status-chip">Public</span><b>Public notices</b><span>＋</span></div><div class="notice-body">Public notices, careers and corporate information can be linked from here.</div></div>
    </div><div class="live-news-stream" id="liveNewsStream" aria-live="polite"></div>'''
new_notices='''<div class="live-feed-heading" aria-hidden="true"><span>LATEST</span><b>Notices &amp; news</b><small>LIVE</small></div><div class="live-news-stream" id="liveNewsStream" aria-live="polite" aria-label="Latest Telikom notices and news"></div>'''
if old_notices not in s:
    raise SystemExit('static notice rows target missing')
s=s.replace(old_notices,new_notices,1)

css=r'''
/* Design 42: brighter PNG story + simplified live news */
.png-live .png-story-photo{
  object-position:center 52%!important;
  filter:saturate(1.08) contrast(1.04) brightness(.82)!important;
  transform:scale(1.018);
}
.png-live .png-story-wash{
  background:linear-gradient(90deg,rgba(2,24,34,.80) 0%,rgba(2,24,34,.58) 30%,rgba(2,24,34,.25) 52%,rgba(2,24,34,.08) 72%,rgba(2,24,34,.12) 100%)!important;
}
.png-live .png-story-glow{
  background:radial-gradient(circle at 69% 44%,rgba(86,218,238,.12),transparent 36%)!important;
}
.live-feed-heading{
  display:grid;
  grid-template-columns:auto 1fr auto;
  align-items:center;
  gap:10px;
  padding:13px 0 12px;
  border-bottom:1px solid var(--line);
}
.live-feed-heading span,.live-feed-heading small{
  font-size:6px;
  font-weight:800;
  letter-spacing:.14em;
  color:#7d96a2;
}
.live-feed-heading b{
  font-size:10px;
  color:var(--ink);
}
.live-feed-heading small{
  color:#16875f;
  display:flex;
  align-items:center;
  gap:5px;
}
.live-feed-heading small:before{
  content:"";
  width:5px;
  height:5px;
  border-radius:50%;
  background:#20a957;
  box-shadow:0 0 0 4px rgba(32,169,87,.10);
}
#liveNewsStream{padding-top:10px}
@media(max-width:820px){.png-live .png-story-photo{object-position:58% 50%!important}}
'''
marker='Design 42: brighter PNG story + simplified live news'
if marker in s:
    raise SystemExit('cleanup already applied')
pos=s.rfind('</style>')
if pos<0:
    raise SystemExit('style close missing')
s=s[:pos]+css+s[pos:]

p.write_text(s)

attr=Path('assets/design42/ATTRIBUTION.md')
existing=attr.read_text() if attr.exists() else '# Design 42 image sources\n'
entry='''\n## Milne Bay aerial background\n- Used in: PNG / National Story section\n- Source page: https://www.tripspoint.com/papua-new-guinea/gurney/tour/multi-day-tours-cruises/tawali-resort-stay-7-pay-5-diving-package/6967\n- Image source: https://cdn.tripspoint.com/uploads/photos/6967/tawali-resort-stay-7-pay-5-diving-package_QnCtx.jpeg\n- Subject: Tawali Resort, Milne Bay Province, Papua New Guinea\n- Note: mirrored locally for the design prototype.\n'''
if '## Milne Bay aerial background' not in existing:
    attr.write_text(existing.rstrip()+entry+'\n')
