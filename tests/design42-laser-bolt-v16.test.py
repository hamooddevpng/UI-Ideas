from pathlib import Path

text = Path('42-base.html').read_text(encoding='utf-8')
compact = ''.join(text.split())

assert 'Design 42: province laser bolt v16' in text
assert '.province-laser-bolt-v16' in text
assert 'width:5px' in compact
assert 'height:1.25px' in compact
assert '.province-laser-v12{display:none!important}' in compact
assert "document.createElement('i')" in text
assert 'bolt.animate([' in text
assert 'network.getScreenCTM()' in text
assert 'section.getBoundingClientRect()' in text
