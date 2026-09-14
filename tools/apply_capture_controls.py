from pathlib import Path
import re

p = Path('all.html')
s = p.read_text()

if 'id="captureDesktop"' in s:
    print('Screenshot controls already present; no changes needed.')
    raise SystemExit(0)

needle = '.mobile-nav a.primary{border-color:rgba(24,167,235,.35);background:rgba(24,167,235,.18);color:#bcecff;}'
insert = needle + '.mobile-captures{grid-column:1/-1;display:flex;align-items:center;gap:6px;margin-top:-2px;}.mobile-capture{display:inline-flex;align-items:center;justify-content:center;min-height:30px;padding:0 9px;border:1px solid rgba(255,255,255,.12);border-radius:9px;background:rgba(255,255,255,.06);color:#d9e7f3;text-decoration:none;font-size:9px;font-weight:900;white-space:nowrap;}.mobile-capture.phone{border-color:rgba(53,197,139,.28);color:#9ce5c7;}'
assert needle in s
s = s.replace(needle, insert, 1)

needle = '.open-current{display:inline-flex;min-height:31px;align-items:center;justify-content:center;padding:0 10px;border:1px solid #354255;border-radius:8px;background:#151d28;color:#d9e3ec;text-decoration:none;font-size:9px;font-weight:900;}'
insert = needle + '.browser-actions{display:flex;align-items:center;justify-content:flex-end;gap:6px;flex-wrap:wrap;}.capture-btn{display:inline-flex;min-height:31px;align-items:center;justify-content:center;padding:0 10px;border:1px solid rgba(24,167,235,.35);border-radius:8px;background:rgba(24,167,235,.10);color:#bdeaff;text-decoration:none;font-size:9px;font-weight:900;white-space:nowrap;}.capture-btn.phone{border-color:rgba(53,197,139,.35);background:rgba(53,197,139,.09);color:#9de4c8;}'
assert needle in s
s = s.replace(needle, insert, 1)

mobile_capture = '<div class="mobile-captures"><a class="mobile-capture" data-mobile-capture="desktop" href="#" target="_blank" rel="noopener noreferrer" aria-label="Capture full-page desktop PNG">↓ Desktop PNG</a><a class="mobile-capture phone" data-mobile-capture="phone" href="#" target="_blank" rel="noopener noreferrer" aria-label="Capture full-page phone PNG">↓ Phone PNG</a></div>'
pattern = re.compile(r'(<div class="mobile-nav">.*?</div>)(</div></section>)')
s, count = pattern.subn(r'\1' + mobile_capture + r'\2', s)
assert count == 5, count

old = '<a class="open-current" id="openCurrent" href="42.html" target="_blank" rel="noopener noreferrer">Open full design ↗</a>'
new = '<div class="browser-actions"><a class="open-current" id="openCurrent" href="42.html" target="_blank" rel="noopener noreferrer">Open full design ↗</a><a class="capture-btn" id="captureDesktop" href="#" target="_blank" rel="noopener noreferrer">↓ Full Page · Desktop</a><a class="capture-btn phone" id="capturePhone" href="#" target="_blank" rel="noopener noreferrer">↓ Full Page · Phone</a></div>'
assert old in s
s = s.replace(old, new, 1)

start = s.index('<script>')
end = s.index('</script>', start) + len('</script>')
script = '''<script>(() => {const desktopFrame = document.getElementById('desktopFrame');if (!desktopFrame) return;const browserAddress = document.getElementById('browserAddress');const browserLabel = document.getElementById('browserLabel');const browserKicker = document.getElementById('browserKicker');const browserTitle = document.getElementById('browserTitle');const openCurrent = document.getElementById('openCurrent');const captureDesktop = document.getElementById('captureDesktop');const capturePhone = document.getElementById('capturePhone');const mainOptions = [...document.querySelectorAll('.main-option')];const otherStrip = document.getElementById('otherStrip');for (let n = 1; n <= 41; n += 1) {const btn = document.createElement('button');btn.className = 'other-design';btn.type = 'button';btn.dataset.design = String(n);btn.setAttribute('aria-label', `Load Design ${n}`);btn.textContent = String(n);otherStrip.appendChild(btn);}const otherDesigns = [...document.querySelectorAll('.other-design')];const owner = 'hamooddevpng';const repo = 'UI-Ideas';const branch = 'main';const screenshotApi = 'https://telikom-website.onrender.com/api/screenshot';function fullPreviewForLocal(n) {return `https://htmlpreview.github.io/?https://raw.githubusercontent.com/${owner}/${repo}/${branch}/${n}.html`;}function captureTarget(target) {const match = /^(\\d+)\\.html$/.exec(target);return match ? fullPreviewForLocal(Number(match[1])) : target;}function screenshotUrl(target, viewport) {return `${screenshotApi}?url=${encodeURIComponent(captureTarget(target))}&viewport=${encodeURIComponent(viewport)}`;}function updateCaptureLinks(target) {captureDesktop.href = screenshotUrl(target, 'desktop');capturePhone.href = screenshotUrl(target, 'phone');}function clearActive() {mainOptions.forEach(btn => btn.classList.remove('active'));otherDesigns.forEach(btn => btn.classList.remove('active'));}function loadMain(btn) {clearActive();btn.classList.add('active');const src = btn.dataset.src;const target = captureTarget(src);desktopFrame.src = target;browserAddress.textContent = btn.dataset.address;browserLabel.textContent = btn.dataset.label;browserTitle.textContent = btn.dataset.label;const selected = btn.classList.contains('selected-choice');browserKicker.textContent = selected ? 'Selected direction' : 'Homepage option';openCurrent.href = target;updateCaptureLinks(target);}function loadOther(n, btn) {clearActive();btn.classList.add('active');const target = fullPreviewForLocal(n);desktopFrame.src = target;browserAddress.textContent = `UI-Ideas · Design ${n}`;browserLabel.textContent = `Design ${n}`;browserKicker.textContent = 'Other design';browserTitle.textContent = `Design ${n}`;openCurrent.href = target;updateCaptureLinks(target);}mainOptions.forEach(btn => btn.addEventListener('click', () => loadMain(btn)));otherDesigns.forEach(btn => btn.addEventListener('click', () => loadOther(Number(btn.dataset.design), btn)));document.getElementById('otherPrev').addEventListener('click', () => otherStrip.scrollBy({left: -520, behavior: 'smooth'}));document.getElementById('otherNext').addEventListener('click', () => otherStrip.scrollBy({left: 520, behavior: 'smooth'}));document.querySelectorAll('[data-mobile-capture]').forEach(link => {const slide = link.closest('.mobile-slide');const target = slide.querySelector('iframe').getAttribute('src');link.href = screenshotUrl(target, link.dataset.mobileCapture);});updateCaptureLinks('42.html');})();</script>'''
s = s[:start] + script + s[end:]

p.write_text(s)
print('Applied screenshot controls to all.html')
