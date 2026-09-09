const { chromium } = require('playwright');
(async()=>{
  const browser = await chromium.launch({headless:true});
  const page = await browser.newPage({viewport:{width:1440,height:900}});
  const bad=[];
  page.on('response',r=>{ if(r.request().resourceType()==='image' && !r.ok()) bad.push([r.status(),r.url()]); });
  await page.goto('http://127.0.0.1:4173/41.html',{waitUntil:'networkidle'});
  const result = await page.evaluate(()=>{
    const imgs=[...document.images].map(i=>({src:i.getAttribute('src'),ok:i.complete&&i.naturalWidth>0,w:i.naturalWidth,h:i.naturalHeight}));
    const ids=['top','offers','services','business','story','updates','support'];
    const sections=ids.map(id=>({id,h:document.getElementById(id).getBoundingClientRect().height}));
    return {imgs,sections,html:document.documentElement.innerHTML};
  });
  if(bad.length) throw new Error('Image request failures: '+JSON.stringify(bad));
  const failed=result.imgs.filter(i=>!i.ok);
  if(failed.length) throw new Error('Broken images: '+JSON.stringify(failed));
  const over=result.sections.filter(s=>s.h>721);
  if(over.length) throw new Error('Sections over 80vh at 1440x900: '+JSON.stringify(over));
  const banned=['village-people.jpg','education-png.jpg','png-electricians.jpg','aptc-graduates.jpg','png-locals-meeting.jpg'];
  for(const b of banned) if(result.html.includes(b)) throw new Error('Banned image reference remains: '+b);
  const required=['moresby-kastom-dancers-2.jpg','mount-hagen-sing-sing-2019.jpg','kopar-village-child.jpg','telikom-retail-team.jpg','asaro-goroka-performers.jpg'];
  for(const r of required) if(!result.html.includes(r)) throw new Error('Required curated image missing: '+r);
  console.log('PASS PNG identity', {sections:result.sections, images:result.imgs.filter(i=>i.src&&i.src.includes('design41/')).map(i=>({src:i.src,w:i.w,h:i.h}))});
  await browser.close();
})().catch(e=>{console.error(e);process.exit(1)});
