from pathlib import Path

path = Path('42-base.html')
text = path.read_text(encoding='utf-8')
old = """      const frame=now=>{\n        const t=Math.min(1,(now-started)/duration);\n        const e=1-Math.pow(1-t,3);\n        const x=a.x+(b.x-a.x)*e;\n        const y=a.y+(b.y-a.y)*e;\n        glow.setAttribute('x2',x);glow.setAttribute('y2',y);\n        core.setAttribute('x2',x);core.setAttribute('y2',y);\n        if(t<1){requestAnimationFrame(frame);return}\n        setTimeout(()=>{\n          glow.style.transition='opacity 60ms linear';\n          core.style.transition='opacity 60ms linear';\n          glow.style.opacity='0';core.style.opacity='0';\n          setTimeout(()=>{glow.remove();core.remove()},75);\n        },25);\n      };"""
new = """      const frame=now=>{\n        const t=Math.min(1,(now-started)/duration);\n        const headE=1-Math.pow(1-t,3);\n        const tailDelay=.24;\n        const tailProgress=Math.max(0,Math.min(1,(t-tailDelay)/(1-tailDelay)));\n        const tailE=1-Math.pow(1-tailProgress,3);\n        const headX=a.x+(b.x-a.x)*headE;\n        const headY=a.y+(b.y-a.y)*headE;\n        const tailX=a.x+(b.x-a.x)*tailE;\n        const tailY=a.y+(b.y-a.y)*tailE;\n        glow.setAttribute('x1',tailX);glow.setAttribute('y1',tailY);\n        glow.setAttribute('x2',headX);glow.setAttribute('y2',headY);\n        core.setAttribute('x1',tailX);core.setAttribute('y1',tailY);\n        core.setAttribute('x2',headX);core.setAttribute('y2',headY);\n        if(t<1){requestAnimationFrame(frame);return}\n        glow.remove();core.remove();\n      };"""
if text.count(old) != 1:
    raise SystemExit(f'Expected exactly one laser frame block, found {text.count(old)}')
text = text.replace(old, new, 1)
text = text.replace('/* Design 42: laser tuning v13 */\n/* Faster, thinner, glow-free source-to-destination beams. */', '/* Design 42: laser tuning v14 */\n/* Fast, thin beams whose head and tail both travel from source to destination. */', 1)
path.write_text(text, encoding='utf-8')
