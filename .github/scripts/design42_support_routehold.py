from pathlib import Path
p=Path('42.html')
s=p.read_text()

old_leave="n.addEventListener('pointerleave',()=>{stage.classList.remove('node-hot');if(!query?.value){coreMode.textContent='CALL';coreValue.textContent='1555';hint.textContent='Move around the hub or search for what you need.'}})"
if old_leave not in s:
    raise SystemExit('direct support pointerleave target missing')
s=s.replace(old_leave,"n.addEventListener('pointerleave',()=>{})",1)

old_hit="}setSupportRoute(hit)})},{passive:true});"
if old_hit not in s:
    raise SystemExit('support delegated hit target missing')
s=s.replace(old_hit,"}if(hit)setSupportRoute(hit)})},{passive:true});",1)

anchor="    if(query){const syncSearch=()=>{const on=query.value.trim().length>0;"
insert="""    let supportRouteHold=null;
    stage.addEventListener('pointermove',e=>{if(e.pointerType==='touch')return;const nearest=nodes.map(n=>{const r=n.getBoundingClientRect(),cx=r.left+r.width/2,cy=r.top+r.height/2;return {n,d:Math.hypot(e.clientX-cx,e.clientY-cy),r}}).sort((a,b)=>a.d-b.d)[0];const hit=nearest&&nearest.d<Math.max(105,Math.max(nearest.r.width,nearest.r.height)*.78)?nearest.n:null;clearTimeout(supportRouteHold);if(hit)supportRouteHold=setTimeout(()=>setSupportRoute(hit),34)},{passive:true});
    stage.addEventListener('pointerleave',()=>{clearTimeout(supportRouteHold);supportRouteHold=null;setSupportRoute(null)});
"""
if anchor not in s:
    raise SystemExit('support route hold anchor missing')
s=s.replace(anchor,insert+anchor,1)
p.write_text(s)
