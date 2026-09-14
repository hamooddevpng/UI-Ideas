#!/usr/bin/env python3
from pathlib import Path
import json
import re
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / 'reference-screenshots' / 'page-design'
OUT = ROOT / 'research' / 'page-design-reference' / 'QA_REPORT.md'

BAD_TITLE = re.compile(r'(just a moment|access denied|captcha|security verification|page not found|404 not found|^error$|service unavailable)', re.I)
BAD_URL = re.compile(r'(validate\.perfdrive\.com|challenge-platform|/cdn-cgi/challenge)', re.I)
# Explicit visual QA findings from the earlier review. These must never influence structure.
KNOWN_BAD = {
    ('news-media', 'verizon-press'): 'pathological over-expanded/infinite listing capture',
    ('news-media', 'orange-newsroom'): 'cookie consent overlay obstructs the page',
    ('careers', 'verizon-careers'): 'security verification page rather than careers content',
    ('contact', 'verizon-contact'): 'error page rather than contact experience',
    ('devices', 'vodafone-png-broadband-devices'): 'incomplete/failed local devices capture',
}

rows = []
for cohort in sorted(p for p in SRC.iterdir() if p.is_dir()):
    shot_dir = cohort / 'desktop-1440'
    meta_file = shot_dir / 'capture-results.json'
    if not meta_file.exists():
        continue
    payload = json.loads(meta_file.read_text())
    assessed = []
    for r in payload.get('results', []):
        slug = r.get('slug', '')
        reasons = []
        review = []
        if r.get('status') != 'ok':
            reasons.append(f"capture status={r.get('status')}")
        title = (r.get('title') or '').strip()
        final_url = r.get('finalUrl') or ''
        if BAD_TITLE.search(title):
            reasons.append(f"blocked/error title: {title[:80]}")
        if BAD_URL.search(final_url):
            reasons.append('bot/security redirect')
        if (cohort.name, slug) in KNOWN_BAD:
            reasons.append(KNOWN_BAD[(cohort.name, slug)])
        fp = shot_dir / (r.get('researchFilename') or f'{slug}.png')
        if not fp.exists():
            reasons.append('screenshot missing')
        else:
            try:
                with Image.open(fp) as im:
                    w, h = im.size
                if h > 40000:
                    reasons.append(f'abnormal full-page height {h}px')
                if w < 1000:
                    review.append(f'unexpected width {w}px')
                if fp.stat().st_size < 50_000:
                    review.append('very small screenshot file; inspect for blank/partial render')
            except Exception as e:
                reasons.append(f'image unreadable: {e}')
        if not title and not reasons:
            review.append('blank document title; visual confirmation required')
        verdict = 'exclude' if reasons else ('review' if review else 'candidate-valid')
        assessed.append({**r, 'qaVerdict': verdict, 'qaReasons': reasons, 'qaReview': review})

    valid = [r for r in assessed if r['qaVerdict'] == 'candidate-valid']
    review = [r for r in assessed if r['qaVerdict'] == 'review']
    excluded = [r for r in assessed if r['qaVerdict'] == 'exclude']
    rows.append((cohort.name, payload.get('pageStudy', {}).get('name', cohort.name), valid, review, excluded, len(assessed)))

lines = [
    '# Page Design Reference QA Report', '',
    'Automated QA screen for the expanded Telikom Page Design visual research. This is intentionally conservative: obvious failures are excluded, blank-title/small-image cases are held for contact-sheet review, and structural recommendations still require manual visual review.', '',
    '| Cohort | Captured | Candidate-valid | Needs visual review | Excluded | Gate |',
    '|---|---:|---:|---:|---:|---|'
]
for slug, name, valid, review, excluded, total in rows:
    gate = 'PASS' if len(valid) >= 15 else ('PASS after visual review' if len(valid) + len(review) >= 15 else 'BACKFILL REQUIRED')
    lines.append(f'| {name} (`{slug}`) | {total} | {len(valid)} | {len(review)} | {len(excluded)} | {gate} |')

lines += ['', '## Exclusions and review flags', '']
for slug, name, valid, review, excluded, total in rows:
    lines.append(f'### {name}')
    if excluded:
        lines.append('**Excluded:**')
        for r in excluded:
            why = '; '.join(r['qaReasons'])
            lines.append(f"- `{r.get('slug')}` — {why}")
    else:
        lines.append('**Excluded:** none detected by automated screen.')
    if review:
        lines.append('**Manual visual review required:**')
        for r in review:
            why = '; '.join(r['qaReview'])
            lines.append(f"- `{r.get('slug')}` — {why}")
    lines.append('')

OUT.write_text('\n'.join(lines) + '\n')
print(OUT.relative_to(ROOT))
