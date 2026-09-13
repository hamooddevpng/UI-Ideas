from pathlib import Path
import re

path = Path('42-base.html')
html = path.read_text(encoding='utf-8')
pattern = re.compile(
    r"      const duration=220\+Math\.random\(\)\*120;\n"
    r"      const started=performance\.now\(\);\n\n"
    r"      const frame=now=>\{\n"
    r".*?"
    r"      \};\n"
    r"      requestAnimationFrame\(frame\);\n",
    re.S,
)
new = """      const duration=220+Math.random()*120;
      const catchDuration=65;
      const segmentPx=5;
      const dx=b.x-a.x,dy=b.y-a.y;
      const ctm=network.getScreenCTM();
      const screenDx=ctm?ctm.a*dx+ctm.c*dy:dx;
      const screenDy=ctm?ctm.b*dx+ctm.d*dy:dy;
      const screenDistance=Math.max(1,Math.hypot(screenDx,screenDy));
      const segmentProgress=Math.min(1,segmentPx/screenDistance);
      const started=performance.now();

      const frame=now=>{
        const elapsed=now-started;
        const travelT=Math.min(1,elapsed/duration);
        const headE=1-Math.pow(1-travelT,3);
        let tailE=Math.max(0,headE-segmentProgress);
        let done=false;
        if(travelT>=1){
          const catchProgress=Math.min(1,(elapsed-duration)/catchDuration);
          const catchE=1-Math.pow(1-catchProgress,3);
          tailE=(1-segmentProgress)+segmentProgress*catchE;
          done=catchProgress>=1;
        }
        const headX=a.x+(b.x-a.x)*headE;
        const headY=a.y+(b.y-a.y)*headE;
        const tailX=a.x+(b.x-a.x)*tailE;
        const tailY=a.y+(b.y-a.y)*tailE;
        glow.setAttribute('x1',tailX);glow.setAttribute('y1',tailY);
        glow.setAttribute('x2',headX);glow.setAttribute('y2',headY);
        core.setAttribute('x1',tailX);core.setAttribute('y1',tailY);
        core.setAttribute('x2',headX);core.setAttribute('y2',headY);
        if(!done){requestAnimationFrame(frame);return}
        glow.remove();core.remove();
      };
      requestAnimationFrame(frame);
"""
updated, count = pattern.subn(new, html, count=1)
if count != 1:
    raise SystemExit(f'expected exactly one laser frame block, found {count}; refusing unrelated edits')
path.write_text(updated, encoding='utf-8')
