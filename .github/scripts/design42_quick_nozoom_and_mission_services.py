from pathlib import Path
p=Path('42.html')
s=p.read_text()

biz_old='''<div class="dual-world-copy"><small>IP VPN · MPLS · SIP · BUSINESS SYSTEMS</small><h3>Your offices.<br>One network.</h3><p>Managed connectivity, secure private networks, collaboration and voice systems for organisations of every size.</p><div class="dual-stats"><span><b>99%</b><small>IP VLAN availability</small></span><span><b>900 Mbps</b><small>MPLS bandwidth up to</small></span><span><b>100K+</b><small>MX-ONE users supported</small></span></div></div>'''
biz_new='''<div class="dual-world-copy"><small>IP VPN · MPLS · SIP · BUSINESS SYSTEMS</small><h3>Your offices.<br>One network.</h3><p>Managed connectivity, secure private networks, collaboration and voice systems for organisations of every size.</p><div class="mission-service-block"><div class="mission-service-head"><b>Business service pages</b><span>Explore →</span></div><div class="mission-service-grid"><a class="mission-service-card" href="#business"><img src="assets/common/web-sourced/telikom/business-data.jpg" alt="Business Data service"><span><small>DATA</small><b>Business Data</b><em>IP VPN · MPLS</em></span></a><a class="mission-service-card" href="#business"><img src="assets/common/web-sourced/telikom/business-systems.jpg" alt="Business Systems service"><span><small>COLLABORATION</small><b>Business Systems</b><em>MiVoice · MiCollab</em></span></a><a class="mission-service-card" href="#business"><img src="assets/common/web-sourced/telikom/news-01.jpg" alt="SIP Trunk service"><span><small>VOICE</small><b>SIP Trunk</b><em>Voice over IP</em></span></a><a class="mission-service-card" href="#business"><img src="assets/common/web-sourced/telikom/news-07.jpg" alt="CUG and PUG service"><span><small>MOBILE</small><b>CUG / PUG</b><em>Business mobile groups</em></span></a></div></div></div>'''
if biz_old not in s: raise SystemExit('business copy block not found')
s=s.replace(biz_old,biz_new,1)

gov_old='''<div class="dual-world-copy"><small>DATA · VSAT · VOICE · HOSTING · CO-LOCATION</small><h3>Public services.<br>Closer to people.</h3><p>Enterprise-grade connectivity can link offices, remote sites and citizen-facing services through one Telikom portfolio.</p><div class="dual-stats government-stats"><span><b>VSAT</b><small>Remote connectivity</small></span><span><b>Secure</b><small>Co-location &amp; backup</small></span><span><b>Voice + Data</b><small>Integrated communications</small></span></div></div>'''
gov_new='''<div class="dual-world-copy"><small>DATA · VSAT · VOICE · HOSTING · CO-LOCATION</small><h3>Public services.<br>Closer to people.</h3><p>Enterprise-grade connectivity can link offices, remote sites and citizen-facing services through one Telikom portfolio.</p><div class="mission-service-block government-services"><div class="mission-service-head"><b>Government service pages</b><span>Explore →</span></div><div class="mission-service-grid"><a class="mission-service-card" href="#business"><img src="assets/common/web-sourced/telikom/mt-kegum.jpg" alt="VSAT remote connectivity service"><span><small>REMOTE</small><b>VSAT</b><em>Remote connectivity</em></span></a><a class="mission-service-card" href="#business"><img src="assets/common/web-sourced/telikom/news-02.jpg" alt="Co-Location service"><span><small>INFRASTRUCTURE</small><b>Co-Location</b><em>Secure infrastructure</em></span></a><a class="mission-service-card mission-wide" href="#business"><img src="assets/common/web-sourced/telikom/news-06.jpg" alt="Web and Hosting service"><span><small>DIGITAL</small><b>Web &amp; Hosting</b><em>Hosting · email · backup</em></span></a></div></div></div>'''
if gov_old not in s: raise SystemExit('government copy block not found')
s=s.replace(gov_old,gov_new,1)

start=s.find('<div class="business-portfolio reveal" id="businessPortfolio">')
end_marker='\n  </div>\n</section>\n<section class="png-story png-live"'
if start==-1: raise SystemExit('business portfolio start not found')
end=s.find(end_marker,start)
if end==-1: raise SystemExit('business portfolio end not found')
s=s[:start]+s[end:]

marker='/* Design 42: crisp quick actions + mission-contained service pages */'
if marker in s: raise SystemExit('marker already present')
css=r'''

/* Design 42: crisp quick actions + mission-contained service pages */
.quick-launchpad .quick-card{
  filter:none!important;
  transform:translateY(10px)!important;
  clip-path:inset(0 100% 0 0 round 18px);
  transition:opacity .42s var(--qdelay) ease,clip-path .72s var(--qdelay) var(--spring),transform .55s var(--qdelay) var(--spring),box-shadow .22s ease,border-color .22s ease,background .22s ease!important;
}
.quick-launchpad.quick-ready .quick-card{
  opacity:1!important;
  filter:none!important;
  transform:none!important;
  clip-path:inset(0 0 0 0 round 18px);
}
.quick-launchpad .quick-card:before{
  z-index:1!important;
  inset:0!important;
  background:linear-gradient(105deg,transparent 0 34%,rgba(117,220,255,.08) 43%,rgba(117,220,255,.32) 50%,rgba(117,220,255,.08) 57%,transparent 66% 100%)!important;
  background-size:220% 100%!important;
  background-position:130% 0!important;
  opacity:0!important;
  pointer-events:none!important;
}
.quick-launchpad .quick-card:after{
  content:"";
  position:absolute;
  z-index:5;
  inset:0;
  border-radius:inherit;
  padding:1px;
  pointer-events:none;
  opacity:0;
  background:conic-gradient(from 0deg,transparent 0 25%,#60d4fb 35%,#0875c9 43%,transparent 55% 100%);
  -webkit-mask:linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);
  -webkit-mask-composite:xor;
  mask-composite:exclude;
}
.quick-launchpad .quick-card:hover,.quick-launchpad .quick-card:focus-visible{
  transform:none!important;
  filter:none!important;
  background:#fbfeff!important;
  border-color:rgba(28,160,232,.38)!important;
  box-shadow:0 16px 34px rgba(16,70,97,.12),inset 0 -3px 0 rgba(28,160,232,.65)!important;
  outline:none!important;
}
.quick-launchpad .quick-card:hover:before,.quick-launchpad .quick-card:focus-visible:before{
  opacity:1!important;
  animation:quickCardSweep .82s ease both;
}
.quick-launchpad .quick-card:hover:after,.quick-launchpad .quick-card:focus-visible:after,.quick-launchpad .quick-card.quick-hot:after{
  opacity:.95;
  animation:quickEdgeRun 1.35s linear infinite;
}
.quick-launchpad.quick-focused .quick-card:not(.quick-hot){opacity:.64!important;filter:none!important;transform:none!important}
.quick-launchpad .quick-card:hover .q-icon,.quick-launchpad .quick-card:focus-visible .q-icon{
  transform:none!important;
  background:var(--navy)!important;
  color:#9ee7ff!important;
  box-shadow:0 0 0 5px rgba(28,160,232,.08),0 10px 24px rgba(6,25,37,.16)!important;
}
@keyframes quickCardSweep{from{background-position:130% 0}to{background-position:-130% 0}}
@keyframes quickEdgeRun{to{transform:rotate(360deg)}}

.business-dual-shell{
  height:min(84vh,756px)!important;
  min-height:700px!important;
  grid-template-rows:auto minmax(0,1fr)!important;
  gap:11px!important;
}
.business-dual-stage{grid-template-rows:repeat(2,minmax(0,1fr))!important}
.business-dual .business-world{grid-template-columns:48% 52%!important}
.business-dual .government-world{grid-template-columns:52% 48%!important}
.business-dual .dual-world-copy{padding:33px 20px 14px!important;justify-content:center!important}
.business-dual .dual-world-copy h3{font-size:clamp(26px,2.1vw,32px)!important;margin:7px 0 5px!important}
.business-dual .dual-world-copy>p{font-size:10.2px!important;line-height:1.42!important;max-width:520px!important}
.business-dual .dual-art-wrap{margin:26px 10px 6px!important}
.business-dual .dual-art{max-height:190px!important}
.business-dual .dual-stats{display:none!important}

.mission-service-block{margin-top:10px;min-width:0}
.mission-service-head{display:flex;align-items:center;justify-content:space-between;gap:14px;margin-bottom:6px}
.mission-service-head b{font-size:7px;letter-spacing:.12em;text-transform:uppercase;color:#2f7d9e}
.mission-service-head span{font-size:7px;font-weight:800;color:#0875c9}
.government-services .mission-service-head b{color:#2e8468}
.government-services .mission-service-head span{color:#16875f}
.mission-service-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:6px}
.mission-service-card{min-width:0;min-height:54px;display:grid;grid-template-columns:58px minmax(0,1fr);align-items:center;gap:8px;padding:5px;border:1px solid rgba(20,99,132,.12);border-radius:12px;background:rgba(255,255,255,.76);box-shadow:0 7px 16px rgba(20,87,112,.045);overflow:hidden;transition:border-color .2s,box-shadow .2s,background .2s}
.mission-service-card img{width:58px;height:44px;object-fit:cover;border-radius:8px;display:block}
.mission-service-card span{min-width:0;display:block}
.mission-service-card small{display:block;font-size:5.6px;line-height:1;color:#4f8398;letter-spacing:.11em;font-weight:800;margin-bottom:3px}
.mission-service-card b{display:block;font-family:"Space Grotesk";font-size:10.8px;line-height:1;color:#15394a;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.mission-service-card em{display:block;font-style:normal;font-size:6.6px;line-height:1.2;color:#6d8792;margin-top:3px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.mission-service-card:hover,.mission-service-card:focus-visible{outline:none;border-color:rgba(8,117,201,.3);background:#fff;box-shadow:0 10px 22px rgba(16,91,121,.10)}
.government-services .mission-service-card{border-color:rgba(37,139,109,.12)}
.government-services .mission-service-card:hover,.government-services .mission-service-card:focus-visible{border-color:rgba(37,139,109,.30)}
.government-services .mission-wide{grid-column:1 / -1}

@media(max-height:780px) and (min-width:821px){
  .business-dual-shell{height:min(84vh,720px)!important;min-height:680px!important}
  .business-dual .dual-world-copy{padding-top:31px!important;padding-bottom:10px!important}
  .business-dual .dual-world-copy h3{font-size:27px!important}
  .business-dual .dual-world-copy>p{font-size:9.4px!important}
  .mission-service-block{margin-top:7px}
  .mission-service-card{min-height:48px;grid-template-columns:50px minmax(0,1fr);padding:4px}
  .mission-service-card img{width:50px;height:38px}
}
@media(max-width:820px){
  .business-dual-shell{height:auto!important;min-height:0!important}
  .business-dual .dual-world{min-height:560px!important}
  .business-dual .dual-world-copy{padding:43px 20px 14px!important}
  .mission-service-card{min-height:58px}
  .government-services .mission-wide{grid-column:auto}
  .government-services .mission-service-grid{grid-template-columns:1fr}
  .quick-launchpad .quick-card{clip-path:none!important;transform:none!important;filter:none!important}
}
@media(prefers-reduced-motion:reduce){
  .quick-launchpad .quick-card:before,.quick-launchpad .quick-card:after{animation:none!important}
}
'''
if '</style>' not in s: raise SystemExit('style close missing')
s=s.replace('</style>',css+'\n</style>',1)
p.write_text(s)
print('patched 42.html')
