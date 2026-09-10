from pathlib import Path

helper = Path('scripts/_design42_ecosystem_calm.py')
src = helper.read_text(encoding='utf-8')
old = """hero_after = text[hero_start:hero_end]\nservices_after = text[services_start:services_end]\nif hero_before != hero_after:\n    raise SystemExit('Hero changed unexpectedly')\nif services_before != services_after:\n    raise SystemExit('Services changed unexpectedly')"""
new = """hero_after_start = text.index('<section class=\\\"hero\\\"')\nhero_after_end = text.index('</section>', hero_after_start) + len('</section>')\nhero_after = text[hero_after_start:hero_after_end]\nservices_after_start = text.index('<section class=\\\"services service-stories\\\"')\nservices_after_end = text.index('</section>', services_after_start) + len('</section>')\nservices_after = text[services_after_start:services_after_end]\nif hero_before != hero_after:\n    raise SystemExit('Hero changed unexpectedly')\nif services_before != services_after:\n    raise SystemExit('Services changed unexpectedly')"""
if old not in src:
    raise SystemExit('Guard block not found in helper')
src = src.replace(old, new, 1)
exec(compile(src, str(helper), 'exec'))
