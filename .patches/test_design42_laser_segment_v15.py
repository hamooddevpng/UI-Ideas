from pathlib import Path

html = Path('42-base.html').read_text(encoding='utf-8')
marker = '// Design 42: endpoint lasers v12'
start = html.rfind('<script>', 0, html.index(marker) + 1)
end = html.index('</script>', html.index(marker))
section = html[start:end]

assert 'const segmentPx=5' in section, 'laser segment is not capped at 5 rendered pixels'
assert 'getScreenCTM()' in section, 'laser cap is not converted from screen pixels to SVG geometry'
assert 'segmentProgress' in section, 'laser tail does not follow at a fixed short distance'
assert 'catchProgress' in section, 'laser tail does not explicitly catch the destination'
assert "setAttribute('x1',tailX)" in section, 'laser tail endpoint is not animated'
assert "setAttribute('x2',headX)" in section, 'laser head endpoint is not animated'
print('5px travelling laser segment contract satisfied')
