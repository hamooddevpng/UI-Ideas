from pathlib import Path

p = Path('42-base.html')
s = p.read_text(encoding='utf-8')

repls = [
    (".province-laser-v12.glow{stroke:#18d8ff;stroke-width:9;filter:blur(1.2px) drop-shadow(0 0 8px rgba(24,216,255,.95)) drop-shadow(0 0 14px rgba(8,117,201,.7))}",
     ".province-laser-v12.glow{display:none!important}"),
    (".province-laser-v12.core{stroke:#fff;stroke-width:2.8;filter:drop-shadow(0 0 2px #fff) drop-shadow(0 0 6px #68ecff)}",
     ".province-laser-v12.core{stroke:#079fd2;stroke-width:1.35;filter:none}"),
    ("const duration=520+Math.random()*260;",
     "const duration=220+Math.random()*120;"),
    ("glow.style.transition='opacity 180ms ease';\n          core.style.transition='opacity 180ms ease';",
     "glow.style.transition='opacity 60ms linear';\n          core.style.transition='opacity 60ms linear';"),
    ("        },120);",
     "        },25);"),
    ("          setTimeout(()=>{glow.remove();core.remove()},210);",
     "          setTimeout(()=>{glow.remove();core.remove()},75);")
]

for old, new in repls:
    if old not in s:
        raise SystemExit(f'Missing expected v12 snippet: {old[:100]}')
    s = s.replace(old, new, 1)

marker = '/* Design 42: laser tuning v13 */'
if marker not in s:
    s = s.replace('/* Design 42: endpoint lasers v12 */', marker + '\n/* Faster, thinner, glow-free source-to-destination beams. */\n/* Design 42: endpoint lasers v12 */', 1)

p.write_text(s, encoding='utf-8')
