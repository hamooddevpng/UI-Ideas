from pathlib import Path
import re

html = Path('42-base.html').read_text(encoding='utf-8')
start = html.index('/* Design 42: laser tuning v')
end = html.index('</script>', html.index('// Design 42: endpoint lasers v12', start))
section = html[start:end]

# The moving laser must move both endpoints. The head (x2/y2) reaches B first,
# then the tail (x1/y1) follows so the beam actually travels instead of stretching.
assert "setAttribute('x2'," in section, 'laser head is not animated'
assert "setAttribute('x1'," in section, 'laser tail is still pinned to the source'
assert re.search(r'tailProgress|tailT|tailE', section), 'no independent tail progress exists'
print('laser tail animation contract satisfied')
