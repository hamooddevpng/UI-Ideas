from pathlib import Path
from urllib.parse import urljoin, quote
import io
import re
import json
import requests
from bs4 import BeautifulSoup
from PIL import Image, ImageOps

ROOT = Path('.')
TELIKOM_DIR = ROOT / 'assets/common/web-sourced/telikom'
COMMONS_DIR = ROOT / 'assets/common/web-sourced/commons'
TELIKOM_DIR.mkdir(parents=True, exist_ok=True)
COMMONS_DIR.mkdir(parents=True, exist_ok=True)

UA = {'User-Agent': 'Mozilla/5.0 (compatible; TelikomDesignResearch/1.0)'}
session = requests.Session()
session.headers.update(UA)


def get(url):
    r = session.get(url, timeout=40, allow_redirects=True, verify=False)
    r.raise_for_status()
    return r


def save_image(url, path, max_width=1500):
    r = get(url)
    try:
        im = Image.open(io.BytesIO(r.content))
        im.load()
    except Exception as e:
        raise RuntimeError(f'Not a usable image: {url}: {e}')
    im = ImageOps.exif_transpose(im).convert('RGB')
    if im.width > max_width:
        h = round(im.height * max_width / im.width)
        im = im.resize((max_width, h), Image.Resampling.LANCZOS)
    path.parent.mkdir(parents=True, exist_ok=True)
    im.save(path, 'JPEG', quality=82, optimize=True, progressive=True)
    if path.stat().st_size < 8000:
        raise RuntimeError(f'Image too small after conversion: {path}')
    return {'source': url, 'final_url': r.url, 'width': im.width, 'height': im.height, 'bytes': path.stat().st_size}


sources = {}

# Directly useful imagery from Telikom's own current website.
direct_telikom = {
    'fixed-broadband.jpg': 'https://www.telikom.com.pg/assets/business/voice-and-data.jpg',
    'business-systems.jpg': 'https://www.telikom.com.pg/assets/misc/pabx-connect.jpg',
    'business-data.jpg': 'https://www.telikom.com.pg/images/mockup/3.jpg',
    'mt-kegum.jpg': 'https://www.telikom.com.pg/assets/news/Mt_Kegum.jpg',
    'lotto.jpg': 'https://www.telikom.com.pg/assets/news/IMG-20240910-WA0001_1.jpg',
}
for name, url in direct_telikom.items():
    sources[f'telikom/{name}'] = save_image(url, TELIKOM_DIR / name)

# Crawl Telikom's news listing and collect distinct article photography.
listing_urls = [
    'https://www.telikom.com.pg/media/news/',
    'https://www.telikom.com.pg/index.php/media/news/',
]
article_links = []
for listing in listing_urls:
    try:
        soup = BeautifulSoup(get(listing).text, 'html.parser')
        for a in soup.find_all('a', href=True):
            href = urljoin(listing, a['href'])
            if '/media/read-news/' in href and href not in article_links:
                article_links.append(href)
        if article_links:
            break
    except Exception:
        pass

news_manifest = []
seen_img_urls = set(direct_telikom.values())
for article in article_links[:24]:
    if len(news_manifest) >= 8:
        break
    try:
        soup = BeautifulSoup(get(article).text, 'html.parser')
        title_node = soup.find('h3') or soup.find('h1') or soup.find('title')
        title = title_node.get_text(' ', strip=True) if title_node else article.rsplit('/', 1)[-1]
        candidates = []
        for img in soup.find_all('img'):
            src = img.get('src') or img.get('data-src') or img.get('data-lazy-src')
            if not src:
                continue
            src = urljoin(article, src)
            low = src.lower()
            if any(x in low for x in ('logo', 'icon', 'favicon', 'tpnglogo')):
                continue
            if '/assets/news/' in low or '/news/' in low:
                candidates.append(src)
        if not candidates:
            for img in soup.find_all('img'):
                src = img.get('src') or img.get('data-src')
                if src:
                    src = urljoin(article, src)
                    low = src.lower()
                    if not any(x in low for x in ('logo', 'icon', 'favicon', 'tpnglogo')):
                        candidates.append(src)
        chosen = next((u for u in candidates if u not in seen_img_urls), None)
        if not chosen:
            continue
        idx = len(news_manifest) + 1
        name = f'news-{idx:02d}.jpg'
        meta = save_image(chosen, TELIKOM_DIR / name)
        seen_img_urls.add(chosen)
        news_manifest.append({'file': name, 'article': article, 'title': title, 'image': chosen, **meta})
        sources[f'telikom/{name}'] = news_manifest[-1]
    except Exception as e:
        print('Skipping article', article, e)

# Ensure we have enough distinct online imagery even if the site listing structure changes.
if len(news_manifest) < 5:
    raise RuntimeError(f'Only found {len(news_manifest)} usable Telikom news images; need at least 5')

# Two authentic PNG/Port Moresby photographs from Wikimedia Commons.
commons_files = {
    'port-moresby.jpg': 'Port moresby (5987247416).jpg',
    'hiri-moale.jpg': 'Papua New Guinea 1991-079 Lagotoi at the Hiri Moali Festival, Ela Beach, Port Moresby (33750628895).jpg',
}
for name, filename in commons_files.items():
    redirect = 'https://commons.wikimedia.org/wiki/Special:Redirect/file/' + quote(filename, safe='') + '?width=1600'
    sources[f'commons/{name}'] = save_image(redirect, COMMONS_DIR / name)
    sources[f'commons/{name}']['commons_file_page'] = 'https://commons.wikimedia.org/wiki/File:' + quote(filename.replace(' ', '_'), safe='()_,-')

# Write a small provenance file so future designs know where the web-sourced assets came from.
lines = [
    '# Web-sourced image assets',
    '',
    'Downloaded for UI mockup/reference use. Keep this file with the assets so original sources remain traceable.',
    '',
    '## Telikom',
    '',
]
for key, meta in sources.items():
    if key.startswith('telikom/'):
        lines.append(f'- `{key}` — {meta.get("article") or meta.get("source")}')
lines += ['', '## Wikimedia Commons', '']
for key, meta in sources.items():
    if key.startswith('commons/'):
        lines.append(f'- `{key}` — {meta.get("commons_file_page")}')
(ROOT / 'assets/common/web-sourced/SOURCES.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')
(ROOT / 'assets/common/web-sourced/telikom/news-manifest.json').write_text(json.dumps(news_manifest, indent=2), encoding='utf-8')

# ---------- Design 40 patch ----------
p = ROOT / '40.html'
s = p.read_text(encoding='utf-8')
raw = 'https://raw.githubusercontent.com/hamooddevpng/UI-Ideas/main/assets/common/web-sourced/'

def t(name): return raw + 'telikom/' + name

def c(name): return raw + 'commons/' + name

# Use every major editorial photo only once on the page.
service_assets = [
    t('fixed-broadband.jpg'),
    t('business-systems.jpg'),
    t('business-data.jpg'),
    c('port-moresby.jpg'),
    t(news_manifest[3]['file']),
    t(news_manifest[4]['file']),
]
business_assets = [t(news_manifest[5]['file']) if len(news_manifest) > 5 else t(news_manifest[3]['file']), t(news_manifest[6]['file']) if len(news_manifest) > 6 else t(news_manifest[4]['file'])]
news_assets = [t('mt-kegum.jpg'), t('lotto.jpg'), t(news_manifest[2]['file'])]
story_asset = c('hiri-moale.jpg')

services = f'''<section class="section soft" id="services"><div class="wrap"><div class="section-head"><div class="copy"><span class="kicker">Service categories</span><h2>Services for the way PNG connects.</h2><p>Clear service pathways with a different visual story for each use case.</p></div></div><div class="service-stories">
  <article class="service-story"><img src="{service_assets[0]}" alt="Telikom fixed broadband connectivity" loading="lazy" decoding="async"><div class="eyebrow">Home Internet</div><h3>Fast connection for home life</h3><p>Plans, availability, setup and support for study, work, streaming and everyday use.</p><a href="#">Explore home internet →</a></article>
  <article class="service-story"><img src="{service_assets[1]}" alt="Telikom business communication systems" loading="lazy" decoding="async"><div class="eyebrow">Business Systems</div><h3>Communication built for work</h3><p>Voice, office systems and practical tools for organisations that need dependable communication.</p><a href="#business">Explore business systems →</a></article>
  <article class="service-story"><img src="{service_assets[2]}" alt="Telikom data and connectivity services" loading="lazy" decoding="async"><div class="eyebrow">Business Data</div><h3>Data that keeps teams moving</h3><p>Reliable connectivity for branches, offices and organisations across Papua New Guinea.</p><a href="#business">Explore business data →</a></article>
  <article class="service-story"><img src="{service_assets[3]}" alt="Port Moresby, Papua New Guinea" loading="lazy" decoding="async"><div class="eyebrow">Coverage & Stores</div><h3>Find service where you are</h3><p>Check availability, understand coverage and find a Telikom service point close to you.</p><a href="#">Check coverage →</a></article>
  <article class="service-story"><img src="{service_assets[4]}" alt="Telikom activity in Papua New Guinea" loading="lazy" decoding="async"><div class="eyebrow">Regional & Remote</div><h3>Connection beyond the city</h3><p>Regional enquiries and specialist connectivity pathways for communities and remote operations.</p><a href="#">Explore regional services →</a></article>
  <article class="service-story"><img src="{service_assets[5]}" alt="Telikom customer and community services" loading="lazy" decoding="async"><div class="eyebrow">Support</div><h3>Help when you need it</h3><p>Troubleshooting, account help, contact options and self service in one straightforward place.</p><a href="#support">Get support →</a></article>
</div></div></section>'''

business = f'''<section class="business-section" id="business"><div class="wrap"><div class="section-head"><div class="copy"><span class="kicker">Business & Government</span><h2>Built for organisations that keep PNG moving.</h2><p>Dedicated solutions, practical expertise and national reach without adding unnecessary complexity.</p></div></div><div class="org-stack">
  <article class="org-row business"><div class="org-media" style="background-image:url('{business_assets[0]}')" role="img" aria-label="Telikom business connectivity in Papua New Guinea"></div><div class="org-copy"><small>For business</small><h3>Keep your organisation connected.</h3><p>Business internet, managed connectivity, voice and regional solutions through one clear entry point.</p><div class="org-points"><span>Business Internet</span><span>Managed Connectivity</span><span>Voice</span><span>Regional Solutions</span></div><a class="org-cta" href="#">Explore business solutions →</a></div></article>
  <article class="org-row government reverse"><div class="org-media" style="background-image:url('{business_assets[1]}')" role="img" aria-label="Telikom national infrastructure and government connectivity"></div><div class="org-copy"><small>For government</small><h3>Reliable connection for national services.</h3><p>Government connectivity, regional services and specialist support for organisations serving communities across PNG.</p><div class="org-points"><span>National Connectivity</span><span>Regional Services</span><span>Infrastructure</span><span>Specialist Support</span></div><a class="org-cta" href="#">Government solutions →</a></div></article>
</div></div></section>'''

story = f'''<section class="png-strip" id="story"><div class="wrap png-panel"><div class="png-copy"><span class="kicker">PNG / National story</span><h2>Connecting people and places across Papua New Guinea.</h2><p>Telikom is part of daily life across PNG, supporting families, communities, businesses and national services as they communicate and grow.</p><div class="png-links"><a href="#">About Telikom →</a><a href="#">Our Network →</a><a href="#">Community →</a></div></div><div class="png-art"><img class="png-story-photo" src="{story_asset}" alt="Papua New Guinea community life at Ela Beach, Port Moresby" loading="lazy" decoding="async"></div></div></section>'''

updates = f'''<section class="section" id="updates"><div class="wrap"><div class="section-head"><div class="copy"><span class="kicker">Notices & news</span><h2>Important information and stories from Telikom.</h2></div></div><div class="updates-layout">
  <aside class="notice-board"><div class="notice-board-head"><h3>Service notices</h3><span>Customer updates</span></div>
    <article class="notice-row"><div class="meta"><span class="badge">Notice</span><time>Service</time></div><strong>Network and service information</strong><p>Verified advisories, maintenance notices and service information in a format that is easy to scan.</p><a href="#">View notice →</a></article>
    <article class="notice-row"><div class="meta"><span class="badge">Notice</span><time>Customer</time></div><strong>Customer service updates</strong><p>Practical information affecting support, stores and customer access.</p><a href="#">View notice →</a></article>
    <article class="notice-row"><div class="meta"><span class="badge">Tender</span><time>08 Apr 2026</time></div><strong>Properties tender notice</strong><p>Procurement and formal notices stay distinct from editorial news.</p><a href="#">View notice →</a></article>
  </aside>
  <div class="news-block"><h3>Latest news</h3><div class="news-grid">
    <article class="news-feature"><img src="{news_assets[0]}" alt="Officials inspecting the restored Mt. Kegum telecommunications tower" loading="lazy" decoding="async"><div class="news-copy"><div class="meta">Infrastructure · 16 Apr 2025</div><h4>Mt. Kegum High-Capacity Network tower restored</h4><p>Critical telecommunications infrastructure reconnects communities across northern and highland PNG.</p><a href="#">Read story →</a></div></article>
    <div class="news-side">
      <article class="news-small"><img src="{news_assets[1]}" alt="Telikom Independence campaign" loading="lazy" decoding="async"><div class="news-copy"><div class="meta">Community · Sep 2024</div><h4>Telikom connects customers through new services</h4><a href="#">Read story →</a></div></article>
      <article class="news-small"><img src="{news_assets[2]}" alt="Telikom partnership announcement" loading="lazy" decoding="async"><div class="news-copy"><div class="meta">Partnerships</div><h4>New partnerships extend connectivity across PNG</h4><a href="#">Read story →</a></div></article>
    </div>
  </div>
</div></div></section>'''

for pattern, replacement, label in [
    (r'<section class="section soft" id="services">.*?</section>\n<section class="business-section" id="business">', services + '\n<section class="business-section" id="business">', 'services'),
    (r'<section class="business-section" id="business">.*?</section>\n<section class="png-strip" id="story">', business + '\n<section class="png-strip" id="story">', 'business'),
    (r'<section class="png-strip" id="story">.*?</section>\n<section class="section" id="updates">', story + '\n<section class="section" id="updates">', 'story'),
    (r'<section class="section" id="updates">.*?</section>\n<section class="section soft" id="support">', updates + '\n<section class="section soft" id="support">', 'updates'),
]:
    s, n = re.subn(pattern, replacement, s, count=1, flags=re.S)
    if n != 1:
        raise RuntimeError(f'Could not replace {label} section; count={n}')

# Make sure these editorial areas have no repeated image URL.
editorial = re.search(r'<section class="section soft" id="services">.*?<section class="section soft" id="support">', s, re.S).group(0)
urls = re.findall(r'https://raw\.githubusercontent\.com/[^\"\')]+', editorial)
from collections import Counter
repeated = [u for u, count in Counter(urls).items() if count > 1]
if repeated:
    raise RuntimeError('Repeated editorial image URLs remain: ' + ', '.join(repeated))

p.write_text(s, encoding='utf-8')
print(f'Downloaded {len(sources)} source images, including {len(news_manifest)} Telikom news photos.')
