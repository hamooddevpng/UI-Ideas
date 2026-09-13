#!/usr/bin/env python3
from pathlib import Path
import json
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = ROOT / 'reference-screenshots' / 'page-design'
OUT_ROOT = ROOT / 'research' / 'page-design-reference' / 'contact-sheets'
OUT_ROOT.mkdir(parents=True, exist_ok=True)

CARD_W = 260
MAX_IMG_H = 1800
LABEL_H = 76
GAP = 18
MARGIN = 24
PER_SHEET = 5

try:
    FONT = ImageFont.truetype('DejaVuSans.ttf', 16)
    SMALL = ImageFont.truetype('DejaVuSans.ttf', 12)
except Exception:
    FONT = ImageFont.load_default()
    SMALL = FONT

# Clear old generated sheets so removed sources do not linger.
for p in OUT_ROOT.glob('*.jpg'):
    p.unlink()

for cohort_dir in sorted(p for p in SRC_ROOT.iterdir() if p.is_dir()):
    shot_dir = cohort_dir / 'desktop-1440'
    if not shot_dir.exists():
        continue

    result_map = {}
    result_file = shot_dir / 'capture-results.json'
    if result_file.exists():
        try:
            payload = json.loads(result_file.read_text())
            result_map = {r.get('researchFilename'): r for r in payload.get('results', [])}
        except Exception:
            pass

    files = sorted(shot_dir.glob('*.png'))
    if not files:
        continue

    cards = []
    for fp in files:
        try:
            with Image.open(fp) as src:
                img = src.convert('RGB')
                original_size = img.size
                scale = min(CARD_W / img.width, MAX_IMG_H / img.height)
                w = max(1, int(img.width * scale))
                h = max(1, int(img.height * scale))
                thumb = img.resize((w, h), Image.Resampling.LANCZOS)
        except Exception:
            continue

        meta = result_map.get(fp.name, {})
        status = meta.get('status', 'unknown')
        name = meta.get('name') or fp.stem.replace('-', ' ').title()
        cards.append((fp.name, name, status, original_size, thumb))

    for group_idx in range(0, len(cards), PER_SHEET):
        group = cards[group_idx:group_idx + PER_SHEET]
        max_h = max(card[4].height for card in group)
        canvas_w = MARGIN * 2 + PER_SHEET * CARD_W + (PER_SHEET - 1) * GAP
        canvas_h = MARGIN * 2 + LABEL_H + max_h
        canvas = Image.new('RGB', (canvas_w, canvas_h), 'white')
        draw = ImageDraw.Draw(canvas)
        title = f'{cohort_dir.name} · references {group_idx + 1}-{group_idx + len(group)} of {len(cards)}'
        draw.text((MARGIN, 5), title, fill='black', font=FONT)

        y0 = MARGIN + 28
        for j, (filename, name, status, original_size, thumb) in enumerate(group):
            x = MARGIN + j * (CARD_W + GAP)
            draw.rectangle((x, y0, x + CARD_W, y0 + LABEL_H - 6), outline='#cccccc', width=1)
            draw.text((x + 6, y0 + 5), name[:31], fill='black', font=SMALL)
            draw.text((x + 6, y0 + 24), f'{status} · {original_size[0]}×{original_size[1]}', fill='black', font=SMALL)
            draw.text((x + 6, y0 + 43), filename[:34], fill='black', font=SMALL)
            ix = x + (CARD_W - thumb.width) // 2
            canvas.paste(thumb, (ix, y0 + LABEL_H))

        out = OUT_ROOT / f'{cohort_dir.name}-{group_idx // PER_SHEET + 1:02d}.jpg'
        canvas.save(out, 'JPEG', quality=84, optimize=True)
        print(out.relative_to(ROOT))
