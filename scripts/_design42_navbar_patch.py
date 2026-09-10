from pathlib import Path

path = Path('42.html')
text = path.read_text(encoding='utf-8')
old = '.main-nav a{font-size:10px;font-weight:800}'
new = '.main-nav a{font-size:13px;font-weight:700}'

if text.count(old) != 1:
    raise SystemExit(f'Expected exactly one navbar rule, found {text.count(old)}')

text = text.replace(old, new, 1)
path.write_text(text, encoding='utf-8')
print('Updated Design 42 navbar to 13px / 700 weight')
