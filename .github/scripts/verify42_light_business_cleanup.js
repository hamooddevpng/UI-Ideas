const { chromium } = require('playwright-core');
(async()=>{
  const browser=await chromium.launch({headless:true,executablePath:'/usr/bin/google-chrome',args:['--no-sandbox']});
  const page=await browser.newPage({viewport:{width:1440,height:900}});
  const errors=[]; page.on('pageerror',e=>errors.push(String(e)));
  await page.goto('http://127.0.0.1:8000/42.html',{waitUntil:'domcontentloaded',timeout:45000});
  await page.waitForTimeout(700);

  // Tower hero: map and tower stay, polygon links are gone.
  await page.locator('[data-scene="2"]').click();
  await page.waitForTimeout(450);
  if(await page.locator('.scene-enterprise .hero-map').count()!==1)throw new Error('tower hero map missing');
  if(await page.locator('.tower').count()!==1)throw new Error('tower missing');
  const lineStates=await page.locator('.network-svg line').evaluateAll(es=>es.map(e=>getComputedStyle(e).display));
  if(lineStates.some(v=>v!=='none'))throw new Error('tower polygon lines still visible '+JSON.stringify(lineStates));

  // Business/Government: no centre T/spine, and the outer section is genuinely light.
  const business=page.locator('#business');
  await business.scrollIntoViewIfNeeded();
  await page.waitForTimeout(500);
  if(await page.locator('#business .dual-spine').count())throw new Error('centre T spine still present');
  const state=await business.evaluate(el=>{
    const cs=getComputedStyle(el), sample=document.elementFromPoint(innerWidth/2,Math.max(1,Math.min(innerHeight-1,el.getBoundingClientRect().top+20)));
    return {flag:cs.getPropertyValue('--business-light-pass').trim(),bg:cs.backgroundImage,color:cs.color,sample:sample&&sample.className};
  });
  if(state.flag!=='2')throw new Error('light business pass missing '+JSON.stringify(state));
  if(!state.bg.includes('rgb(238, 249, 252)')&&!state.bg.includes('rgb(248, 252, 253)'))throw new Error('business background not light enough '+state.bg);

  const worlds=await page.locator('#business .dual-world').evaluateAll(es=>es.map(e=>({bg:getComputedStyle(e).backgroundImage,color:getComputedStyle(e).color,opacity:+getComputedStyle(e).opacity})));
  if(worlds.length!==2)throw new Error('expected two business worlds');
  if(worlds.some(w=>!w.bg.includes('rgba(255, 255, 255')))throw new Error('business worlds not light '+JSON.stringify(worlds));

  const bizBox=await business.boundingBox();
  if(!bizBox||bizBox.height>810)throw new Error('business section exceeds 90vh '+(bizBox&&bizBox.height));

  // Interactions still work.
  const gov=page.locator('[data-dual-world="government"]');
  await gov.hover(); await page.waitForTimeout(250);
  if((await business.getAttribute('data-focus'))!=='government')throw new Error('government hover focus broke');
  const chip=page.locator('.portfolio-chip').nth(2);
  await chip.hover(); await page.waitForTimeout(180);
  if(!(await chip.getAttribute('class')).includes('active'))throw new Error('portfolio hover broke');

  // Existing hero motion regression.
  await page.locator('#top').scrollIntoViewIfNeeded();
  await page.locator('[data-scene="1"]').click();
  await page.waitForTimeout(350);
  await page.mouse.move(1120,170); await page.waitForTimeout(250);
  const sx1=await page.locator('#top').evaluate(el=>getComputedStyle(el).getPropertyValue('--sat-x'));
  await page.mouse.move(760,430); await page.waitForTimeout(250);
  const sx2=await page.locator('#top').evaluate(el=>getComputedStyle(el).getPropertyValue('--sat-x'));
  if(sx1===sx2)throw new Error('satellite tracking regression');

  if(errors.length)throw new Error('page errors: '+errors.join(' | '));
  console.log(JSON.stringify({towerPolygonRemoved:true,spineRemoved:true,business:state,worlds,height:bizBox.height,governmentHover:true,portfolioHover:true,satellite:true}));
  await browser.close();
})().catch(e=>{console.error(e);process.exit(1)});
