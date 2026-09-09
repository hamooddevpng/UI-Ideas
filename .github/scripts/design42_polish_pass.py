from pathlib import Path
import re

p=Path('42.html')
s=p.read_text()

# Self Care: replace current background with the locally mirrored FAO PNG image.
s,n=re.subn(r'(<div class="scene scene-phone active"><img class="hero-atmos hero-people" src=")[^"]+(" alt="" aria-hidden="true">)',r'\1assets/design42/png-selfcare-fao.jpg\2',s,count=1)
if n!=1: raise SystemExit('self care hero image target missing')

# Light Tok Pisin touches, using verified spellings only.
for old,new in [
    ('<div class="kicker">Picked for you</div>','<div class="kicker">Nambawan · Picked for you</div>'),
    ('<div class="kicker" style="color:#bcecff">100% PNG Owned Telecommunications Company</div>','<div class="kicker" style="color:#bcecff">Bilong yumi · 100% PNG Owned Telecommunications Company</div>'),
    ('<span class="live-feed-now">JUST NOW</span>','<span class="live-feed-now">NUPELA</span>')
]:
    if old not in s: raise SystemExit('copy target missing: '+old[:45])
    s=s.replace(old,new,1)

# Give every offer candidate a distinct image so random selection can never repeat artwork.
start=s.find('const personalizedOfferPool=[')
end=s.find('];const offersSection=',start)
if start<0 or end<0: raise SystemExit('personalized offer pool missing')
new_pool="""const personalizedOfferPool=[
{tag:'Mobile',icon:'⌁',title:'More data for today.',body:'Explore Telikom mobile data options and choose the bundle that fits what you are doing.',cta:'See mobile options ↗',href:'#services',image:'assets/common/web-sourced/telikom/news-01.jpg',alt:'Telikom mobile service in Papua New Guinea',media:'mobile'},
{tag:'Self Care',icon:'＋',title:'Top up in a few taps.',body:'Open Self Care to recharge, check your balance or manage voice and data bundles.',cta:'Open Self Care ↗',href:'#top',selfcare:true,image:'assets/design42/png-selfcare-fao.jpg',alt:'Papua New Guinea farmers and agripreneurs taking part in a hands-on training session',media:'selfcare'},
{tag:'Home Internet',icon:'⌂',title:'Bring more home online.',body:'Explore fixed broadband and home internet options for everyday browsing and streaming.',cta:'Explore home internet ↗',href:'#services',image:'assets/common/web-sourced/telikom/fixed-broadband.jpg',alt:'Telikom fixed broadband service',media:'home'},
{tag:'Remote',icon:'◌',title:'Connect beyond the network edge.',body:'Explore VSAT and remote connectivity options for business and communities across PNG.',cta:'Explore remote connectivity ↗',href:'#business',image:'assets/design42/png-remote-coast.jpg',alt:'Remote coastline in Papua New Guinea',media:'coast'},
{tag:'Business',icon:'↗',title:'Keep business connected.',body:'Explore Telikom connectivity, fixed voice, hosting and business data services.',cta:'Explore business services ↗',href:'#business',image:'assets/common/web-sourced/telikom/business-data.jpg',alt:'Telikom business connectivity service',media:'business'},
{tag:'Support',icon:'?',title:'Need a hand?',body:'Customer Care is available on 1555 when you need help with your Telikom service.',cta:'Get support ↗',href:'#support',image:'assets/common/web-sourced/telikom/news-06.jpg',alt:'Telikom customer and community activity in Papua New Guinea',media:'support'}]"""
s=s[:start]+new_pool+s[end+1:]

# Future-proof the shuffle too: pick by unique image even if the pool is edited later.
old='pool.slice(0,3).forEach((o,i)=>{'
new="const seenImages=new Set(),picked=pool.filter(o=>{if(seenImages.has(o.image))return false;seenImages.add(o.image);return true}).slice(0,3);picked.forEach((o,i)=>{"
if old not in s: raise SystemExit('offer shuffle target missing')
s=s.replace(old,new,1)

css=r'''
/* Design 42: PNG language, navbar fit, FAO Self Care and lighter enterprise */
.site-header .brand{height:44px;min-width:0;max-width:174px;padding:4px 8px;display:flex;align-items:center;justify-content:center;flex:0 0 auto}
.site-header .brand img{display:block;width:auto!important;max-width:158px!important;max-height:33px!important;height:auto!important;object-fit:contain;filter:none!important}
.scene-phone .hero-people{opacity:.21;object-position:69% 47%;filter:saturate(.88) contrast(1.05) brightness(.64);transform:scale(1.025)}
.business-dual{--business-light-pass:1;background:radial-gradient(circle at 50% 46%,rgba(88,211,244,.12),transparent 34%),linear-gradient(135deg,#0b3141 0%,#0f4051 48%,#10483f 100%)!important}
.business-dual:before{background-image:linear-gradient(rgba(168,232,255,.055) 1px,transparent 1px),linear-gradient(90deg,rgba(168,232,255,.055) 1px,transparent 1px)!important}
.business-dual .dual-world{background:linear-gradient(150deg,rgba(20,74,94,.94),rgba(9,46,61,.96));border-color:rgba(183,234,255,.19);box-shadow:0 24px 62px rgba(0,17,27,.22),inset 0 1px rgba(255,255,255,.055)}
.business-dual .government-world{background:linear-gradient(150deg,rgba(19,82,73,.95),rgba(8,50,52,.97));border-color:rgba(184,244,222,.18)}
.business-dual .portfolio-detail{background:rgba(255,255,255,.055);border-color:rgba(180,231,251,.16)}
.business-dual .portfolio-chip{background:rgba(255,255,255,.04);border-color:rgba(255,255,255,.12)}
@media(max-width:820px){.site-header .brand{height:41px;max-width:154px;padding:4px 7px}.site-header .brand img{max-width:140px!important;max-height:30px!important}.scene-phone .hero-people{opacity:.18;object-position:62% 46%}}
'''
if 'PNG language, navbar fit, FAO Self Care and lighter enterprise' in s:
    raise SystemExit('polish CSS already present')
pos=s.rfind('</style>')
if pos<0: raise SystemExit('style close missing')
s=s[:pos]+css+s[pos:]

p.write_text(s)

# Keep source attribution with the local asset.
a=Path('assets/design42/ATTRIBUTION.md')
text=a.read_text() if a.exists() else '# Design 42 banner image sources\n'
line='- `png-selfcare-fao.jpg`: FAO / EU-STREIT PNG, farmers and agripreneurs participating in a hands-on training session. Source: https://www.fao.org/images/faoraplibraries/default-album/farmers-and-agripreneurs-actively-participate-in-a-hands-on-training-session-provided-by-the-eu-streit-png-programme.jpg?sfvrsn=4cc42070_1\n'
if 'png-selfcare-fao.jpg' not in text:
    a.write_text(text.rstrip()+'\n'+line)
