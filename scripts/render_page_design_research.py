#!/usr/bin/env python3
import json
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'research/page-design/page-research.json'
SRC = ROOT / 'reference-screenshots/page-design'
OUT = ROOT / 'research/page-design/generated'
OUT.mkdir(parents=True, exist_ok=True)

REG = Path('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf')
BOLD = Path('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf')

def font(size, bold=False):
    p = BOLD if bold else REG
    return ImageFont.truetype(str(p), size) if p.exists() else ImageFont.load_default()

def wrap(draw, text, width, f):
    words = str(text).split()
    lines, cur = [], ''
    for w in words:
        test = (cur + ' ' + w).strip()
        if draw.textbbox((0,0), test, font=f)[2] <= width:
            cur = test
        else:
            if cur: lines.append(cur)
            cur = w
    if cur: lines.append(cur)
    return lines

def thumb(path, w, h):
    im = Image.open(path).convert('RGB')
    # Extremely long pages remain useful as evidence, but cap the raster used for the board.
    if im.height > im.width * 18:
        im = im.crop((0, 0, im.width, min(im.height, im.width * 18)))
    im.thumbnail((w, h), Image.Resampling.LANCZOS)
    return im

def page_images(slug):
    d = SRC / slug / 'desktop-1440'
    meta = json.loads((d / 'capture-results.json').read_text(encoding='utf-8'))
    items = []
    for r in meta.get('results', []):
        if r.get('status') != 'ok':
            continue
        p = d / r.get('researchFilename', f"{r['slug']}.png")
        if p.exists():
            items.append((r.get('name') or r['slug'], p))
    return items

def render(slug, data):
    items = page_images(slug)
    W, H = 2400, 1500
    c = Image.new('RGB', (W,H), 'white')
    d = ImageDraw.Draw(c)
    d.text((60,45), f"{data['title']} - Competitor Pattern Research", font=font(42,True), fill='black')
    d.text((60,102), f"Telikom Page Design study · {len(items)} usable captures · desktop 1440px", font=font(22), fill='#555555')

    x0, y0, pw, ph = 60, 155, 1450, 1280
    d.rectangle((x0,y0,x0+pw,y0+ph), outline='#cccccc', width=2)
    if items:
        cols = 2
        rows = (len(items) + cols - 1) // cols
        cell_w = (pw - 50) // cols
        cell_h = (ph - 60) // rows
        for i,(name,p) in enumerate(items):
            col, row = i % cols, i // cols
            cx = x0 + 20 + col * cell_w
            cy = y0 + 20 + row * cell_h
            t = thumb(p, cell_w - 30, cell_h - 60)
            c.paste(t, (cx + (cell_w - 30 - t.width)//2, cy + 28))
            label = name[:42]
            d.text((cx,cy), label, font=font(15,True), fill='#111111')

    x, y, rw = 1560, 160, 770
    d.text((x,y), 'REFERENCE SET', font=font(22,True), fill='black'); y += 42
    for cpt in data['competitors']:
        for line in wrap(d, '• ' + cpt, rw, font(18)):
            d.text((x,y), line, font=font(18), fill='#222222'); y += 28
    y += 16
    d.text((x,y), 'WHAT THE REFERENCES SHOW', font=font(22,True), fill='black'); y += 42
    for obs in data['observations']:
        for line in wrap(d, '• ' + obs, rw, font(18)):
            d.text((x,y), line, font=font(18), fill='#222222'); y += 27
        y += 7
    y += 10
    d.text((x,y), 'RECOMMENDED TELIKOM STRUCTURE', font=font(22,True), fill='black'); y += 44
    for i, step in enumerate(data['structure'], 1):
        ff = font(18, i <= 3)
        for line in wrap(d, f'{i}. {step}', rw, ff):
            d.text((x,y), line, font=ff, fill='#111111'); y += 28
        y += 4

    note = 'Research note: screenshots are comparison evidence, not layouts to copy. Telikom content and API requirements remain authoritative. Failed or distorted captures are excluded from structural conclusions.'
    yy = 1435
    d.rectangle((60,yy-8,2340,1490), fill='#f5f5f5')
    for line in wrap(d, note, 2240, font(16)):
        d.text((80,yy), line, font=font(16), fill='#555555'); yy += 23
    c.save(OUT / f'{slug}-research.jpg', 'JPEG', quality=88, optimize=True)
    c.close()


def main():
    research = json.loads(DATA.read_text(encoding='utf-8'))
    lines = ['# Telikom Page Design Competitor Research', '', 'Generated from committed competitor screenshots. Tasks remain open; these are research inputs for design.', '']
    for slug, data in research.items():
        render(slug, data)
        lines += [f"## {data['title']}", '', f"![{data['title']}](./{slug}-research.jpg)", '', '**Recommended structure:** ' + ' → '.join(data['structure']), '']
    (OUT / 'README.md').write_text('\n'.join(lines), encoding='utf-8')
    print(f'Rendered {len(research)} page-design research boards.')

if __name__ == '__main__':
    main()
