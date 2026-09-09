from pathlib import Path
p=Path('42.html')
s=p.read_text()

# Remove the centre Telikom T spine between Business and Government cards.
spine='<div class="dual-spine" aria-hidden="true"><span></span><i></i><b>T</b></div>'
if spine not in s:
    raise SystemExit('dual spine target missing')
s=s.replace(spine,'',1)

css=r'''
/* Design 42: remove tower polygon and make Business/Government genuinely light */
.hero[data-scene-index="2"] .network-svg line{display:none}

.business-dual{
  --business-light-pass:2;
  color:#102b3c!important;
  background:
    radial-gradient(circle at 18% 18%,rgba(66,190,235,.16),transparent 30%),
    radial-gradient(circle at 84% 72%,rgba(65,188,148,.13),transparent 30%),
    linear-gradient(135deg,#eef9fc 0%,#f8fcfd 48%,#eef9f5 100%)!important;
}
.business-dual:before{
  background-image:
    linear-gradient(rgba(31,117,151,.055) 1px,transparent 1px),
    linear-gradient(90deg,rgba(31,117,151,.055) 1px,transparent 1px)!important;
  opacity:.72;
}
.business-dual-head .kicker{color:#0875c9!important}
.business-dual-head .title{color:#102b3c!important}
.business-dual-head .lead{color:#617d8b!important}
.business-dual-stage{gap:18px}
.business-dual .dual-world{
  background:linear-gradient(150deg,rgba(255,255,255,.96),rgba(221,244,251,.94))!important;
  border-color:rgba(21,116,157,.17)!important;
  box-shadow:0 22px 54px rgba(28,92,117,.11),inset 0 1px rgba(255,255,255,.92)!important;
}
.business-dual .government-world{
  background:linear-gradient(150deg,rgba(255,255,255,.97),rgba(225,247,239,.95))!important;
  border-color:rgba(37,139,109,.17)!important;
}
.business-dual[data-focus="business"] .business-world,
.business-dual[data-focus="government"] .government-world{
  box-shadow:0 27px 65px rgba(23,91,116,.14),0 0 44px rgba(39,169,225,.06),inset 0 1px #fff!important;
}
.business-dual[data-focus="government"] .government-world{
  box-shadow:0 27px 65px rgba(38,109,88,.13),0 0 44px rgba(80,196,157,.06),inset 0 1px #fff!important;
}
.business-dual[data-focus="business"] .government-world,
.business-dual[data-focus="government"] .business-world{opacity:.82}
.dual-world-top{color:#6a8795!important}
.business-world .dual-world-top b{color:#0875c9!important}
.government-world .dual-world-top b{color:#16875f!important}
.dual-ground{fill:rgba(30,143,188,.07)!important}
.government-world .dual-ground{fill:rgba(37,153,113,.065)!important}
.dual-world-copy>small{color:#2f7d9e!important}
.government-world .dual-world-copy>small{color:#2e8468!important}
.dual-world-copy h3{color:#102b3c!important}
.dual-world-copy>p{color:#607c89!important}
.government-world .dual-world-copy>p{color:#617f75!important}
.dual-stats span{
  border-color:rgba(31,120,157,.13)!important;
  background:rgba(255,255,255,.68)!important;
  box-shadow:0 8px 20px rgba(28,92,117,.055);
}
.dual-stats b{color:#17485d!important}
.dual-stats small{color:#708b97!important}
.government-stats span{border-color:rgba(43,143,111,.14)!important}
.government-stats b{color:#23634f!important}
.government-stats small{color:#728e84!important}
.business-portfolio{color:#102b3c}
.business-dual .portfolio-detail{
  background:rgba(255,255,255,.78)!important;
  border-color:rgba(23,109,145,.14)!important;
  box-shadow:0 12px 30px rgba(25,91,116,.06);
}
.portfolio-detail small{color:#648493!important}
.portfolio-detail b{color:#173d50!important}
.portfolio-detail span{color:#66828e!important}
.business-dual .portfolio-chip{
  background:rgba(255,255,255,.7)!important;
  border-color:rgba(22,101,135,.12)!important;
  color:#385c6d!important;
  box-shadow:0 7px 18px rgba(25,91,116,.035);
}
.business-dual .portfolio-chip small{color:#79939e!important}
.business-dual .portfolio-chip:hover,
.business-dual .portfolio-chip:focus-visible,
.business-dual .portfolio-chip.active{
  background:#fff!important;
  color:#0c6698!important;
  border-color:rgba(8,117,201,.3)!important;
  box-shadow:0 13px 28px rgba(8,117,201,.09);
}
.business-dual .portfolio-chip.active small{color:#5a879b!important}
@media(max-width:820px){
  .business-dual{background:linear-gradient(160deg,#eef9fc,#f7fcfd 52%,#eef9f5)!important}
}
'''
if 'Design 42: remove tower polygon and make Business/Government genuinely light' in s:
    raise SystemExit('cleanup patch already present')
pos=s.rfind('</style>')
if pos<0: raise SystemExit('style close missing')
s=s[:pos]+css+s[pos:]
p.write_text(s)
