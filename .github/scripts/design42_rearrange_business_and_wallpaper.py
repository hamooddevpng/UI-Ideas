from pathlib import Path

p=Path('42.html')
s=p.read_text()

old_img='<img class="png-story-photo" src="assets/design42/milne-bay-aerial.jpg" alt="Aerial view of Tawali Resort coastline and coral reefs in Milne Bay, Papua New Guinea" loading="lazy" decoding="async">'
new_img='<img class="png-story-photo" src="https://images.pexels.com/photos/14558429/pexels-photo-14558429.jpeg?auto=compress&cs=tinysrgb&w=2400" alt="Aerial view of the tropical coastline at Salamaua, Morobe Province, Papua New Guinea" loading="lazy" decoding="async" referrerpolicy="no-referrer">'
if old_img not in s:
    raise SystemExit('old PNG story image markup not found')
s=s.replace(old_img,new_img,1)

needle='<div class="business-portfolio reveal" id="businessPortfolio">\n      <article class="portfolio-feature" id="portfolioFeature">'
replacement='<div class="business-portfolio reveal" id="businessPortfolio">\n      <div class="portfolio-rail-heading"><div><small>BUSINESS PORTFOLIO</small><b>Explore business services</b></div><span>Seven service areas · image-led pages</span></div>\n      <article class="portfolio-feature" id="portfolioFeature">'
if needle not in s:
    raise SystemExit('portfolio insertion point not found')
s=s.replace(needle,replacement,1)

marker='/* Design 42: mission-band business layout + Salamaua wallpaper */'
if marker in s:
    raise SystemExit('marker already present')

css=r'''

/* Design 42: mission-band business layout + Salamaua wallpaper */
.png-live .png-story-photo{
  inset:0!important;
  width:100%!important;
  height:100%!important;
  object-fit:cover!important;
  object-position:center 48%!important;
  transform:translate3d(var(--png-tx),var(--png-ty),0) scale(1.018)!important;
  filter:saturate(.98) contrast(1.04) brightness(.72)!important;
}
.png-live .png-story-wash{
  background:linear-gradient(90deg,rgba(3,23,28,.86) 0%,rgba(3,23,28,.62) 34%,rgba(3,23,28,.12) 66%,rgba(3,23,28,.24) 100%)!important;
}

.business-dual{padding:18px 0!important}
.business-dual-shell{
  height:min(84vh,756px)!important;
  min-height:700px!important;
  grid-template-rows:auto minmax(0,1fr) 162px!important;
  gap:11px!important;
}
.business-dual-head{grid-template-columns:.86fr 1.14fr!important;align-items:center!important;gap:52px!important}
.business-dual-head .title{font-size:clamp(38px,4.1vw,58px)!important;line-height:.9!important}
.business-dual-head .lead{font-size:13px!important;line-height:1.55!important;max-width:560px!important}

.business-dual-stage{
  display:grid!important;
  grid-template-columns:1fr!important;
  grid-template-rows:repeat(2,minmax(0,1fr))!important;
  gap:10px!important;
  min-height:0!important;
  perspective:none!important;
}
.business-dual .dual-world{
  display:grid!important;
  flex:none!important;
  opacity:1!important;
  min-height:0!important;
  border-radius:24px!important;
  transform:none!important;
  overflow:hidden!important;
}
.business-dual .business-world{grid-template-columns:40% 60%!important}
.business-dual .government-world{grid-template-columns:60% 40%!important}
.business-dual[data-focus="business"] .government-world,
.business-dual[data-focus="government"] .business-world{opacity:1!important;flex:none!important}

.business-dual .dual-world-top{
  top:12px!important;
  left:18px!important;
  right:18px!important;
  font-size:7px!important;
  letter-spacing:.13em!important;
}
.business-dual .dual-world-copy{
  position:relative!important;
  left:auto!important;
  right:auto!important;
  bottom:auto!important;
  transform:none!important;
  z-index:6!important;
  padding:35px 24px 18px!important;
  display:flex!important;
  flex-direction:column!important;
  justify-content:center!important;
  min-width:0!important;
}
.business-dual .business-world .dual-world-copy{grid-column:1!important;grid-row:1!important}
.business-dual .government-world .dual-world-copy{grid-column:2!important;grid-row:1!important}
.business-dual .dual-world-copy>small{
  display:inline-flex!important;
  width:max-content!important;
  max-width:100%!important;
  padding:5px 8px!important;
  border-radius:999px!important;
  background:rgba(8,117,201,.075)!important;
  font-size:7.5px!important;
  line-height:1.2!important;
  letter-spacing:.09em!important;
  white-space:nowrap!important;
  overflow:hidden!important;
  text-overflow:ellipsis!important;
}
.business-dual .government-world .dual-world-copy>small{background:rgba(32,169,87,.08)!important}
.business-dual .dual-world-copy h3{
  font-size:clamp(27px,2.4vw,35px)!important;
  line-height:.94!important;
  margin:8px 0 7px!important;
}
.business-dual .dual-world-copy>p{
  display:block!important;
  font-size:10.8px!important;
  line-height:1.48!important;
  max-width:430px!important;
  margin:0!important;
}
.business-dual .dual-stats{display:none!important}

.business-dual .dual-art-wrap{
  position:relative!important;
  inset:auto!important;
  left:auto!important;
  right:auto!important;
  top:auto!important;
  bottom:auto!important;
  width:auto!important;
  height:auto!important;
  min-width:0!important;
  min-height:0!important;
  margin:28px 12px 5px!important;
  transform:none!important;
  display:grid!important;
  place-items:center!important;
}
.business-dual .business-world .dual-art-wrap{grid-column:2!important;grid-row:1!important}
.business-dual .government-world .dual-art-wrap{grid-column:1!important;grid-row:1!important}
.business-dual .dual-art{width:100%!important;height:100%!important;max-height:178px!important}

.business-portfolio{
  display:block!important;
  position:relative!important;
  min-height:0!important;
  height:162px!important;
  padding-top:31px!important;
}
.portfolio-rail-heading{
  position:absolute;
  left:2px;
  right:2px;
  top:0;
  height:25px;
  display:flex;
  align-items:center;
  justify-content:space-between;
  gap:18px;
}
.portfolio-rail-heading div{display:flex;align-items:baseline;gap:10px;min-width:0}
.portfolio-rail-heading small{font-size:6px;font-weight:800;letter-spacing:.14em;color:#40809b}
.portfolio-rail-heading b{font-family:"Space Grotesk";font-size:15px;letter-spacing:-.025em;color:#15394a}
.portfolio-rail-heading>span{font-size:7px;color:#728f9b}
.portfolio-feature{display:none!important}
.business-dual .portfolio-strip{
  display:grid!important;
  grid-template-columns:repeat(7,minmax(0,1fr))!important;
  gap:9px!important;
  width:100%!important;
  height:131px!important;
  overflow:visible!important;
}
.business-dual .portfolio-chip{
  height:131px!important;
  border-radius:18px!important;
  box-shadow:0 9px 22px rgba(25,91,116,.06)!important;
}
.portfolio-card-copy{left:12px!important;right:10px!important;bottom:10px!important}
.portfolio-card-copy small{font-size:6px!important;margin-bottom:4px!important}
.portfolio-card-copy b{font-size:11.2px!important;line-height:1!important}
.portfolio-card-copy em{font-size:7px!important;line-height:1.25!important;margin-top:4px!important}
.business-dual .portfolio-chip:hover,
.business-dual .portfolio-chip:focus-visible,
.business-dual .portfolio-chip.active{transform:translateY(-3px)!important}

@media(max-width:1100px) and (min-width:821px){
  .business-dual-shell{height:min(88vh,775px)!important;min-height:720px!important}
  .business-dual .business-world{grid-template-columns:44% 56%!important}
  .business-dual .government-world{grid-template-columns:56% 44%!important}
  .business-dual .dual-world-copy h3{font-size:28px!important}
  .business-dual .dual-world-copy>p{font-size:9.8px!important}
  .business-dual .portfolio-strip{overflow-x:auto!important;grid-template-columns:repeat(7,165px)!important;padding-bottom:4px!important}
}
@media(max-width:820px){
  .business-dual-shell{height:auto!important;min-height:0!important;display:block!important}
  .business-dual-stage{display:block!important;margin-top:24px!important}
  .business-dual .dual-world{display:flex!important;flex-direction:column!important;height:auto!important;min-height:430px!important;margin-bottom:12px!important}
  .business-dual .dual-world-copy{order:1!important;padding:45px 22px 18px!important}
  .business-dual .dual-art-wrap{order:2!important;height:250px!important;margin:0 8px 8px!important}
  .business-dual .dual-art{max-height:250px!important}
  .business-portfolio{height:auto!important;margin-top:18px!important;padding-top:38px!important}
  .portfolio-rail-heading{align-items:flex-start;height:32px}
  .portfolio-rail-heading>span{display:none}
  .business-dual .portfolio-strip{display:flex!important;height:auto!important;overflow-x:auto!important;gap:10px!important;scroll-snap-type:x mandatory}
  .business-dual .portfolio-chip{flex:0 0 190px!important;height:178px!important;scroll-snap-align:start}
  .portfolio-card-copy b{font-size:13px!important}
  .portfolio-card-copy em{font-size:7.5px!important}
}
'''

if '</style>' not in s:
    raise SystemExit('style close not found')
s=s.replace('</style>',css+'\n</style>',1)
p.write_text(s)
print('patched 42.html')
