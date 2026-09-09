from pathlib import Path

p = Path('41.html')
s = p.read_text()

repls = [
    (
        '<div class="utility">',
        '<div class="utility"><span class="tok-chip" lang="tpi" title="Tok Pisin: hello">Gude</span>',
    ),
    (
        '<div class="micro">01 / OFFERS + PLANS</div>',
        '<div class="micro">01 / OFFERS + PLANS <span class="tok-accent" lang="tpi">/ GUTPELA</span></div>',
    ),
    (
        '<div class="micro">03 / BUSINESS + GOVERNMENT</div>',
        '<div class="micro">03 / BUSINESS + GOVERNMENT <span class="tok-accent" lang="tpi">/ WOK</span></div>',
    ),
    (
        '<div class="story-points"><span>People</span><span>Homes</span><span>Work</span><span>Communities</span></div>',
        '<div class="story-points"><span lang="tpi" title="Tok Pisin: close friend / community relation">Wantok</span><span>Homes</span><span lang="tpi" title="Tok Pisin: work">Wok</span><span>Communities</span></div>',
    ),
    (
        '<div class="micro" style="color:#7ccfee">05 / NOTICES + NEWS</div>',
        '<div class="micro" style="color:#7ccfee">05 / NOTICES + NEWS <span class="tok-accent tok-light" lang="tpi">/ TOKAUT</span></div>',
    ),
    (
        '<div class="micro">06 / HELP + SUPPORT + STORES</div>',
        '<div class="micro">06 / HELP + SUPPORT + STORES <span class="tok-accent" lang="tpi">/ HELPIM</span></div>',
    ),
    (
        '<div class="foot-bottom"><span>TELIKOM PNG</span><span>CONNECTING YOU ANYWHERE ANYTIME</span></div>',
        '<div class="foot-bottom"><span>TELIKOM PNG <b class="tok-footer" lang="tpi">· TENKYU</b></span><span>CONNECTING YOU ANYWHERE ANYTIME</span></div>',
    ),
]

for old, new in repls:
    if old not in s:
        raise SystemExit(f'missing marker: {old}')
    if s.count(old) != 1:
        raise SystemExit(f'expected one marker, found {s.count(old)}: {old}')
    s = s.replace(old, new, 1)

css = '''
/* Subtle Tok Pisin accents. English remains the primary functional UI language. */
.tok-chip{display:inline-flex;align-items:center;justify-content:center;padding:7px 9px;border:1px solid rgba(8,117,201,.18);border-radius:999px;background:rgba(234,246,252,.72);font:500 8px DM Mono,monospace;letter-spacing:.12em;text-transform:uppercase;color:var(--blue);white-space:nowrap}
.tok-accent{color:var(--blue);font-weight:500}.tok-light{color:#8fd9f5}.tok-footer{font-weight:500;color:var(--blue);letter-spacing:.11em}
@media(max-width:700px){.tok-chip{display:none}}
'''
marker = '</style>'
if marker not in s:
    raise SystemExit('style close marker missing')
s = s.replace(marker, css + '\n' + marker, 1)

p.write_text(s)
print('Tok Pisin accents added:', s.count('lang="tpi"'))
