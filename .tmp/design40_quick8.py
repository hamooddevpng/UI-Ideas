from pathlib import Path
import re

p = Path('40.html')
text = p.read_text(encoding='utf-8')

old = '''  <div class="wrap quick-main" aria-label="Quick actions">
    <a class="quick-item" href="#"><span class="quick-icon">↻</span><span><strong>Recharge</strong><small>Top up mobile credit</small></span><span class="go">›</span></a>
    <a class="quick-item" href="#"><span class="quick-icon">◎</span><span><strong>Self Care</strong><small>Manage your services</small></span><span class="go">›</span></a>
    <a class="quick-item" href="#"><span class="quick-icon">⌖</span><span><strong>Coverage</strong><small>Check availability</small></span><span class="go">›</span></a>
    <a class="quick-item" href="#support"><span class="quick-icon">?</span><span><strong>Support</strong><small>Find help quickly</small></span><span class="go">›</span></a>
  </div>'''

new = '''  <div class="wrap quick-main" aria-label="Quick actions">
    <a class="quick-item" href="#"><span class="quick-icon">↻</span><span><strong>Recharge</strong><small>Top up mobile credit</small></span><span class="go">›</span></a>
    <a class="quick-item" href="#"><span class="quick-icon">◎</span><span><strong>Self Care</strong><small>Manage your services</small></span><span class="go">›</span></a>
    <a class="quick-item" href="#"><span class="quick-icon">◉</span><span><strong>Coverage</strong><small>Check service availability</small></span><span class="go">›</span></a>
    <a class="quick-item" href="#support"><span class="quick-icon">?</span><span><strong>Support</strong><small>Find help quickly</small></span><span class="go">›</span></a>
    <a class="quick-item" href="#"><span class="quick-icon">⌖</span><span><strong>Find a Store</strong><small>Locate a Telikom branch</small></span><span class="go">›</span></a>
    <a class="quick-item" href="#"><span class="quick-icon">▣</span><span><strong>Buy SIM</strong><small>Get connected with Telikom</small></span><span class="go">›</span></a>
    <a class="quick-item" href="#"><span class="quick-icon">K</span><span><strong>Pay Bill</strong><small>Pay your Telikom account</small></span><span class="go">›</span></a>
    <a class="quick-item" href="#offers"><span class="quick-icon">≋</span><span><strong>Internet Plans</strong><small>Browse home internet options</small></span><span class="go">›</span></a>
  </div>'''

if old not in text:
    raise SystemExit('Quick action block did not match current Design 40')
text = text.replace(old, new, 1)

text, count = re.subn(r'\n\s*<nav class="quick-more"[^>]*>.*?</nav>', '', text, count=1, flags=re.S)
if count != 1:
    raise SystemExit('Secondary quick-action strip not found')

marker = '.quick-more a:hover{color:var(--blue)}'
css = '''
/* Eight-action trial: compact two-row desktop grid. */
.quick-main{height:auto}
.quick-item{min-height:62px}
@media(min-width:901px){.quick-item:nth-child(-n+4){border-bottom:1px solid var(--line)}}
@media(max-width:900px){.quick-item:not(:nth-last-child(-n+2)){border-bottom:1px solid var(--line)}}
'''
if marker not in text:
    raise SystemExit('Quick action CSS marker not found')
text = text.replace(marker, marker + css, 1)

block = re.search(r'<div class="wrap quick-main".*?</div>\s*</section>', text, re.S)
if not block or block.group(0).count('class="quick-item"') != 8:
    raise SystemExit('Eight-action validation failed')
if 'class="quick-more"' in text:
    raise SystemExit('Old quick-more strip still exists')

p.write_text(text, encoding='utf-8')
print('Design 40 now has eight quick actions')
