#!/usr/bin/env python3
from pathlib import Path
import json
import re
import textwrap
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / 'reference-screenshots' / 'page-design'
OUT = ROOT / 'research' / 'page-design-reference' / 'final-boards'
OUT.mkdir(parents=True, exist_ok=True)

PAGE_STRUCTURES = {
    'services-hub': 'Hero + service promise → Audience/service-family switch → Core service categories → Featured plans & offers → PNG-wide infrastructure proof → Business / VSAT / remote connectivity → Quick actions & support → Related links / footer',
    'personal-mobile': 'Hero + plan-family intro → Plan / validity filters → Plan cards + comparison → Allowances & benefits → Passes / roaming / IDD → Activation + USSD → Eligibility / terms → FAQs + support',
    'affordable-home-data': 'Value-led hero → Connection / eligibility → Plan category switch → Plan comparison → Benefits & usage guidance → Activation / how it works → Featured unlimited offer → FAQs + terms',
    'special-home-passes': 'Hero + pass concept → Pass-type tabs → Visual pass cards → Supported apps / use cases → Price, data & validity → Activation / USSD → Featured pass → Terms + FAQs',
    'u-tokmoa': 'Hero + U-TOKMoa proposition → Duration selector → Plan cards / comparison → Voice + data breakdown → Benefits / ideal use → Activation + USSD → Popular plan → FAQs + terms',
    'home-entertainment': 'Entertainment hero → Triple-play benefits → Package tiers → TV / content ecosystem → Broadband + voice inclusions → Device / setup → Installation & eligibility → Order enquiry + FAQs',
    'devices': 'Catalogue hero / category chips → Search + filters + sort → Product grid → Price / badges / stock → Quick specs / compare → Compatibility + bonus data → Where to buy / store CTA → FAQs',
    'business-fixed': 'Outcome-led hero + sales CTA → Solution categories → SLA / NOC / network proof → Service details + use cases → Packages / rates / add-ons → Feasibility + site survey → Calculator / proposal → Enterprise support + FAQs',
    'business-mobile': 'Workforce mobility hero → Plan tiers → CUG / PUG / roaming → Benefits + management controls → Savings / fleet calculator → Commercial terms + SLA → Onboarding / SIM management → Quote CTA + FAQs',
    'news-media': 'Featured newsroom hero → Search + content-type filters → Latest news → Public / network notices → Promotions + community stories → Press releases → Media kit + media contact → Archive',
    'about-us': 'Purpose / PNG role hero → Company story + milestones → Mission / vision / values → National infrastructure + impact → CEO message → Board + executive leadership → Subsidiaries → Foundation / CSR → Key stats + careers / contact',
    'store-locator': 'Search + region / type filters → Interactive map → Synchronized outlet list → Store details → Services + opening hours → Directions / call / email → Featured / nearby outlets → Support fallback',
    'careers': 'Employer-brand hero + job search → Open roles + filters → Career areas → Why Telikom / PNG impact → Benefits + culture → Employee stories → Recruitment process → Application / talent network → FAQs + HR contact',
    'faqs': 'Search-first help hero → FAQ category tiles → Popular questions → Expandable answers → Related guides / product links → Still need help? → Contact / store / Self Care → FAQ structured data',
    'contact': 'Contact-channel cards → Choose enquiry type → Contextual support contacts → Enquiry / feedback / complaint form → Department contacts → HQ address + map + hours → Ticket / reference expectation → Contact FAQs',
}

BAD_TITLE = re.compile(r'(just a moment|access denied|captcha|security verification|page not found|404 not found|^error$|service unavailable)', re.I)
BAD_URL = re.compile(r'(validate\.perfdrive\.com|challenge-platform|/cdn-cgi/challenge)', re.I)
KNOWN_BAD = {
    ('news-media', 'verizon-press'), ('news-media', 'orange-newsroom'),
    ('careers', 'verizon-careers'), ('contact', 'verizon-contact'),
    ('devices', 'vodafone-png-broadband-devices'),
}

try:
    TITLE = ImageFont.truetype('DejaVuSans-Bold.ttf', 28)
    SUB = ImageFont.truetype('DejaVuSans.ttf', 15)
    LABEL = ImageFont.truetype('DejaVuSans-Bold.ttf', 13)
    SMALL = ImageFont.truetype('DejaVuSans.ttf', 11)
except Exception:
    TITLE = SUB = LABEL = SMALL = ImageFont.load_default()

CARD_W, CARD_H = 236, 430
COLS, ROWS = 5, 3
GAP, MARGIN = 18, 30
HEADER_H, FOOTER_H = 145, 175

for out in OUT.glob('*.jpg'):
    out.unlink()

for slug, structure in PAGE_STRUCTURES.items():
    shot_dir = SRC / slug / 'desktop-1440'
    meta_file = shot_dir / 'capture-results.json'
    if not meta_file.exists():
        raise SystemExit(f'Missing capture metadata for {slug}')
    payload = json.loads(meta_file.read_text())
    valid = []
    excluded = []
    for r in payload.get('results', []):
        title = (r.get('title') or '').strip()
        url = r.get('finalUrl') or ''
        reasons = []
        if r.get('status') != 'ok': reasons.append(f"status={r.get('status')}")
        if BAD_TITLE.search(title): reasons.append('blocked/error title')
        if BAD_URL.search(url): reasons.append('bot/security redirect')
        if (slug, r.get('slug')) in KNOWN_BAD: reasons.append('known bad visual capture')
        fp = shot_dir / (r.get('researchFilename') or f"{r.get('slug')}.png")
        if not fp.exists(): reasons.append('missing image')
        else:
            try:
                with Image.open(fp) as im:
                    w, h = im.size
                if h > 40000: reasons.append('abnormal page height')
                if fp.stat().st_size < 50_000: reasons.append('too small / likely incomplete')
            except Exception: reasons.append('unreadable image')
        if reasons:
            excluded.append((r, reasons))
        else:
            valid.append((r, fp))

    if len(valid) < 15:
        raise SystemExit(f'{slug}: only {len(valid)} QA-passing references; need 15')
    chosen = valid[:15]

    page_name = payload.get('pageStudy', {}).get('name', slug.replace('-', ' ').title())
    canvas_w = MARGIN * 2 + COLS * CARD_W + (COLS - 1) * GAP
    canvas_h = HEADER_H + ROWS * CARD_H + (ROWS - 1) * GAP + FOOTER_H + MARGIN
    canvas = Image.new('RGB', (canvas_w, canvas_h), '#f6f7f9')
    draw = ImageDraw.Draw(canvas)

    draw.text((MARGIN, 22), f'{page_name} · Final expanded research board', font=TITLE, fill='#111111')
    draw.text((MARGIN, 64), f'15 QA-passing visual references shown · {len(valid)} usable candidates · {len(excluded)} excluded by capture QA', font=SUB, fill='#333333')
    draw.text((MARGIN, 91), 'Evidence mix: direct telecom/page-type references + PNG business/public-sector context. Structural recommendation is synthesis, not a copied layout.', font=SMALL, fill='#555555')

    y0 = HEADER_H
    for idx, (r, fp) in enumerate(chosen):
        col, row = idx % COLS, idx // COLS
        x = MARGIN + col * (CARD_W + GAP)
        y = y0 + row * (CARD_H + GAP)
        draw.rounded_rectangle((x, y, x + CARD_W, y + CARD_H), 10, fill='white', outline='#d9dde3', width=1)
        draw.text((x + 9, y + 8), (r.get('name') or r.get('slug',''))[:31], font=LABEL, fill='#111111')
        category = r.get('category') or 'page-specific reference'
        draw.text((x + 9, y + 29), category[:34], font=SMALL, fill='#5a6470')
        with Image.open(fp) as src:
            img = src.convert('RGB')
            target_w = CARD_W - 18
            target_h = CARD_H - 62
            scale = min(target_w / img.width, target_h / img.height)
            nw, nh = max(1, int(img.width*scale)), max(1, int(img.height*scale))
            thumb = img.resize((nw, nh), Image.Resampling.LANCZOS)
        ix = x + (CARD_W - nw)//2
        iy = y + 55
        canvas.paste(thumb, (ix, iy))

    fy = HEADER_H + ROWS * CARD_H + (ROWS - 1) * GAP + 18
    draw.text((MARGIN, fy), 'Recommended Telikom information architecture', font=LABEL, fill='#111111')
    wrapped = textwrap.wrap(structure, width=145)
    for i, line in enumerate(wrapped[:5]):
        draw.text((MARGIN, fy + 27 + i*22), line, font=SUB, fill='#222222')
    draw.text((MARGIN, fy + 137), 'Research/design preparation only. Preserve Telikom content parity and customer actions; do not copy competitor visual identity.', font=SMALL, fill='#555555')

    out = OUT / f'{slug}-final-research.jpg'
    canvas.save(out, 'JPEG', quality=88, optimize=True)
    print(out.relative_to(ROOT))
