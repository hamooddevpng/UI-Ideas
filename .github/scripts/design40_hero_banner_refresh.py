from pathlib import Path
import re

p = Path('40.html')
s = p.read_text(encoding='utf-8')

# Remove any lingering references to the two compressed Design 40 banner copies.
s = s.replace('https://raw.githubusercontent.com/hamooddevpng/UI-Ideas/main/assets/design40/banner-travel.jpg', 'https://www.telikom.com.pg/assets/homebanner/NewYear_NewDeals_Together_2026.jpg')
s = s.replace('https://raw.githubusercontent.com/hamooddevpng/UI-Ideas/main/assets/design40/banner-festive.jpg', 'https://www.telikom.com.pg/assets/homebanner/Wantok_e-SIM.jpg')
s = s.replace('assets/design40/banner-travel.jpg', 'https://www.telikom.com.pg/assets/homebanner/NewYear_NewDeals_Together_2026.jpg')
s = s.replace('assets/design40/banner-festive.jpg', 'https://www.telikom.com.pg/assets/homebanner/Wantok_e-SIM.jpg')

hero = '''<section class="campaign" id="top" data-carousel aria-label="Telikom campaign banners">
  <div class="campaign-track">
    <article class="campaign-slide" style="background-image:url('https://www.telikom.com.pg/assets/homebanner/NewYear_NewDeals_Together_2026.jpg')" aria-hidden="false" aria-label="Telikom New Year New Deals campaign"></article>
    <article class="campaign-slide" style="background-image:url('https://www.telikom.com.pg/assets/homebanner/Wantok_e-SIM.jpg')" aria-hidden="true" aria-label="Telikom Wantok eSIM campaign"></article>
    <article class="campaign-slide" style="background-image:url('https://www.telikom.com.pg/assets/homebanner/Device_Bundled_Deals_v2.jpg')" aria-hidden="true" aria-label="Telikom device bundled deals campaign"></article>
    <article class="campaign-slide" style="background-image:url('https://telikom-frontend.vercel.app/images/png/banner.png')" aria-hidden="true" aria-label="Telikom PNG coastal connectivity campaign"></article>
    <article class="campaign-slide" style="background-image:url('https://telikom-frontend.vercel.app/images/png/top-banner-highlands.png')" aria-hidden="true" aria-label="Telikom Highlands connectivity campaign"></article>
    <article class="campaign-slide" style="background-image:url('https://telikom-frontend.vercel.app/images/png/starlink_horizon_concept.png')" aria-hidden="true" aria-label="Telikom remote connectivity campaign"></article>
  </div>
  <button class="campaign-arrow prev" type="button" data-prev aria-label="Previous banner">‹</button>
  <button class="campaign-arrow next" type="button" data-next aria-label="Next banner">›</button>
  <div class="campaign-dots" aria-label="Choose banner">
    <button class="campaign-dot" type="button" data-dot="0" aria-current="true" aria-label="Banner 1"></button>
    <button class="campaign-dot" type="button" data-dot="1" aria-current="false" aria-label="Banner 2"></button>
    <button class="campaign-dot" type="button" data-dot="2" aria-current="false" aria-label="Banner 3"></button>
    <button class="campaign-dot" type="button" data-dot="3" aria-current="false" aria-label="Banner 4"></button>
    <button class="campaign-dot" type="button" data-dot="4" aria-current="false" aria-label="Banner 5"></button>
    <button class="campaign-dot" type="button" data-dot="5" aria-current="false" aria-label="Banner 6"></button>
  </div>
</section>'''

pattern = r'<section class="campaign" id="top" data-carousel aria-label="Telikom campaign banners">.*?</section>'
s, count = re.subn(pattern, hero, s, count=1, flags=re.S)
if count != 1:
    raise SystemExit(f'Expected one hero carousel block, replaced {count}')

# Add a final hero-only override without disturbing the rest of Design 40.
override = '''
/* Design 40 sharp banner carousel: direct original Telikom and Vercel assets. */
.campaign-slide{background-size:cover;background-position:center center;background-color:#d9e9f2}
.campaign-slide:after,.campaign-copy{display:none!important}
'''
s = s.replace('</style>', override + '\n</style>', 1)

# Guardrails.
old = ['banner-travel.jpg', 'banner-festive.jpg']
for x in old:
    if x in s:
        raise SystemExit(f'Old blurry banner reference still present: {x}')
required = [
    'NewYear_NewDeals_Together_2026.jpg',
    'Wantok_e-SIM.jpg',
    'Device_Bundled_Deals_v2.jpg',
    'telikom-frontend.vercel.app/images/png/banner.png',
    'top-banner-highlands.png',
    'starlink_horizon_concept.png',
]
for x in required:
    if x not in s:
        raise SystemExit(f'Missing new banner: {x}')
if s.count('class="campaign-slide"') != 6:
    raise SystemExit('Expected exactly 6 hero slides')
if s.count('class="campaign-dot"') != 6:
    raise SystemExit('Expected exactly 6 hero dots')
if 'setInterval(()=>show(index+1),4500)' not in s:
    raise SystemExit('Carousel autoplay was unexpectedly changed')

p.write_text(s, encoding='utf-8')
print('Design 40 hero updated to six sharp, direct-source banners.')
