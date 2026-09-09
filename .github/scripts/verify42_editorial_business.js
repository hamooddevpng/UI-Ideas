const { chromium } = require('playwright-core');
(async()=>{
  const browser=await chromium.launch({headless:true,executablePath:'/usr/bin/google-chrome',args:['--no-sandbox']});
  const page=await browser.newPage({viewport:{width:1440,height:900}});
  const errors=[]; page.on('pageerror',e=>errors.push(String(e)));
  await page.goto('http://127.0.0.1:8000/42.html',{waitUntil:'domcontentloaded',timeout:45000});
  await page.waitForTimeout(900);

  const business=page.locator('#business');
  await business.scrollIntoViewIfNeeded();
  await page.waitForTimeout(800);
  const box=await business.boundingBox();
  if(!box)throw new Error('business section missing');
  if(box.height>810)throw new Error('business section exceeds 90vh: '+box.height);

  if(await page.locator('#business .dual-world').count()!==2)throw new Error('expected two Business/Government worlds');
  if(await page.locator('#business .portfolio-feature').count()!==1)throw new Error('featured portfolio card missing');
  if(await page.locator('#business .portfolio-chip').count()!==7)throw new Error('expected seven editorial service cards');

  const imageStates=await page.locator('#businessPortfolio img').evaluateAll(imgs=>imgs.map(i=>({src:i.getAttribute('src'),w:i.naturalWidth,h:i.naturalHeight})));
  if(imageStates.length!==8)throw new Error('expected 8 business portfolio images, got '+imageStates.length);
  if(imageStates.some(i=>i.w<80||i.h<60))throw new Error('portfolio image failed to load '+JSON.stringify(imageStates));

  const type=await page.evaluate(()=>({
    panelTitle:parseFloat(getComputedStyle(document.querySelector('.dual-world-copy h3')).fontSize),
    panelText:parseFloat(getComputedStyle(document.querySelector('.dual-world-copy>p')).fontSize),
    cardTitle:parseFloat(getComputedStyle(document.querySelector('.portfolio-card-copy b')).fontSize),
    featureTitle:parseFloat(getComputedStyle(document.querySelector('.portfolio-detail b')).fontSize)
  }));
  if(type.panelTitle<30||type.panelText<9.5||type.cardTitle<9||type.featureTitle<18)throw new Error('business typography still too small '+JSON.stringify(type));

  const vsat=page.locator('#businessPortfolio .portfolio-chip').nth(4);
  await vsat.hover();
  await page.waitForTimeout(260);
  const feature=await page.evaluate(()=>({
    title:document.getElementById('portfolioTitle')?.textContent,
    detail:document.getElementById('portfolioDetail')?.textContent,
    src:document.getElementById('portfolioImage')?.getAttribute('src'),
    active:[...document.querySelectorAll('#businessPortfolio .portfolio-chip')].findIndex(c=>c.classList.contains('active'))
  }));
  if(feature.title!=='VSAT'||!feature.src?.includes('mt-kegum.jpg')||feature.active!==4)throw new Error('editorial portfolio switching failed '+JSON.stringify(feature));

  const html=await page.content();
  if(html.includes('photo-1728957467648-ad5e95eafa1e'))throw new Error('removed Unsplash image still present in 42.html');

  const replacement=page.locator('img[src="assets/design42/png-photographer.jpg"]');
  if(await replacement.count()){
    const state=await replacement.first().evaluate(i=>({w:i.naturalWidth,h:i.naturalHeight,alt:i.alt}));
    if(state.w<100||state.h<100)throw new Error('replacement PNG photo failed to load '+JSON.stringify(state));
    if(!/Papua New Guinea/i.test(state.alt))throw new Error('replacement image alt is stale '+state.alt);
  }

  // Existing VSAT hero motion regression.
  await page.locator('#top').scrollIntoViewIfNeeded();
  await page.locator('[data-scene="1"]').click();
  await page.waitForTimeout(350);
  await page.mouse.move(1110,165); await page.waitForTimeout(220);
  const sx1=await page.locator('#top').evaluate(el=>getComputedStyle(el).getPropertyValue('--sat-x'));
  await page.mouse.move(760,420); await page.waitForTimeout(220);
  const sx2=await page.locator('#top').evaluate(el=>getComputedStyle(el).getPropertyValue('--sat-x'));
  if(sx1===sx2)throw new Error('satellite tracking regression');

  if(errors.length)throw new Error('page errors: '+errors.join(' | '));
  console.log(JSON.stringify({height:box.height,type,imageCount:imageStates.length,feature,replacementCount:await replacement.count(),satellite:true}));
  await browser.close();
})().catch(e=>{console.error(e);process.exit(1)});
