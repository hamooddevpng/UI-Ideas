const { chromium } = require('playwright');

(async()=>{
  const browser = await chromium.launch({headless:true});
  const page = await browser.newPage({viewport:{width:1440,height:900}});
  const errors=[];
  page.on('pageerror',e=>errors.push('pageerror: '+e.message));
  await page.goto('http://127.0.0.1:4173/41.html',{waitUntil:'networkidle'});
  await page.waitForTimeout(800);

  const data = await page.evaluate(()=>{
    const sections=[...document.querySelectorAll('main>section')].map(el=>({id:el.id,height:el.getBoundingClientRect().height}));
    const imgs=[...document.querySelectorAll('img')].map(img=>({src:img.getAttribute('src'),w:img.naturalWidth,h:img.naturalHeight}));
    const thumbs=[...document.querySelectorAll('.offer-card .thumb')].map(el=>{const r=el.getBoundingClientRect();return {w:r.width,h:r.height}});
    return {sections,imgs,thumbs,external:[...document.querySelectorAll('img[src^="http"]')].length};
  });

  const limit=900*.8+.5;
  for(const s of data.sections){
    if(s.height>limit) throw new Error(`section ${s.id} exceeds 80vh: ${s.height}`);
  }
  if(data.external!==0) throw new Error(`external image hotlinks remain: ${data.external}`);
  const bad=data.imgs.filter(x=>!x.w||!x.h);
  if(bad.length) throw new Error('broken images: '+JSON.stringify(bad));
  if(data.thumbs.length!==2) throw new Error('expected two secondary offer thumbnails');
  for(const t of data.thumbs){
    if(t.w<150||t.h<150) throw new Error('offer photo still crushed: '+JSON.stringify(t));
  }

  await page.locator('.offer-card[data-plan="home"]').click();
  await page.waitForTimeout(250);
  if(!(await page.locator('.drawer').evaluate(el=>el.classList.contains('open')))) throw new Error('offer action drawer stopped working');
  await page.locator('.drawer-close').click();

  if(errors.length) throw new Error(errors.join('\n'));
  console.log('PASS desktop photo refresh',data);

  await page.setViewportSize({width:390,height:844});
  await page.reload({waitUntil:'networkidle'});
  await page.waitForTimeout(500);
  const mobileThumbs=await page.locator('.offer-card .thumb').evaluateAll(els=>els.map(el=>el.getBoundingClientRect().height));
  if(mobileThumbs.some(h=>h<190)) throw new Error('mobile offer photo too short: '+JSON.stringify(mobileThumbs));
  console.log('PASS mobile offer photos',mobileThumbs);

  await browser.close();
})().catch(err=>{console.error(err);process.exit(1)});
