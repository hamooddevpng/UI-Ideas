const { chromium } = require('playwright-core');
(async()=>{
  const browser=await chromium.launch({headless:true,executablePath:'/usr/bin/google-chrome',args:['--no-sandbox']});
  const page=await browser.newPage({viewport:{width:1440,height:900}});
  const errors=[];page.on('pageerror',e=>errors.push(String(e)));
  await page.goto('http://127.0.0.1:8000/42.html',{waitUntil:'domcontentloaded',timeout:45000});
  await page.waitForTimeout(900);

  const quick=page.locator('#quick-actions');
  await quick.scrollIntoViewIfNeeded();
  await page.waitForTimeout(800);
  const cards=page.locator('#quick-actions .quick-card');
  if(await cards.count()!==8)throw new Error('expected 8 quick cards');
  const second=cards.nth(1);
  await second.hover();
  await page.waitForTimeout(220);
  const hover=await second.evaluate(el=>({transform:getComputedStyle(el).transform,filter:getComputedStyle(el).filter,after:getComputedStyle(el,'::after').opacity,border:getComputedStyle(el).borderColor}));
  if(hover.transform!=='none')throw new Error('quick card still transforms/zooms on hover: '+JSON.stringify(hover));
  if(hover.filter!=='none')throw new Error('quick card still filtered on hover: '+JSON.stringify(hover));
  if(parseFloat(hover.after)<.5)throw new Error('edge animation not active: '+JSON.stringify(hover));

  const business=page.locator('#business');
  await business.scrollIntoViewIfNeeded();
  await page.waitForTimeout(900);
  const sectionBox=await business.boundingBox();
  if(!sectionBox)throw new Error('business section missing');
  if(sectionBox.height>810)throw new Error('business exceeds 90vh: '+sectionBox.height);
  if(await page.locator('#businessPortfolio').count()!==0)throw new Error('old separate business portfolio still present');
  const bizServices=page.locator('.business-world .mission-service-card');
  const govServices=page.locator('.government-world .mission-service-card');
  if(await bizServices.count()!==4)throw new Error('expected 4 business service cards');
  if(await govServices.count()!==3)throw new Error('expected 3 government service cards');
  const labels=await page.evaluate(()=>({
    business:[...document.querySelectorAll('.business-world .mission-service-card b')].map(x=>x.textContent.trim()),
    government:[...document.querySelectorAll('.government-world .mission-service-card b')].map(x=>x.textContent.trim()),
    businessInside:document.querySelector('.business-world').contains(document.querySelector('.business-world .mission-service-block')),
    governmentInside:document.querySelector('.government-world').contains(document.querySelector('.government-world .mission-service-block')),
    bizTitleSize:parseFloat(getComputedStyle(document.querySelector('.business-world .mission-service-card b')).fontSize),
    panelHeights:[...document.querySelectorAll('.dual-world')].map(x=>x.getBoundingClientRect().height)
  }));
  if(!labels.businessInside||!labels.governmentInside)throw new Error('service blocks not contained in mission panels '+JSON.stringify(labels));
  if(labels.bizTitleSize<10)throw new Error('mission service titles too small '+JSON.stringify(labels));
  const expectedBiz=['Business Data','Business Systems','SIP Trunk','CUG / PUG'];
  const expectedGov=['VSAT','Co-Location','Web & Hosting'];
  if(JSON.stringify(labels.business)!==JSON.stringify(expectedBiz))throw new Error('business grouping wrong '+JSON.stringify(labels));
  if(JSON.stringify(labels.government)!==JSON.stringify(expectedGov))throw new Error('government grouping wrong '+JSON.stringify(labels));

  await page.locator('#top').scrollIntoViewIfNeeded();
  await page.waitForTimeout(300);
  await page.locator('[data-scene="1"]').click();
  await page.waitForTimeout(250);
  const sat=page.locator('.satellite');
  const before=await sat.evaluate(el=>getComputedStyle(el).transform);
  const heroBox=await page.locator('#top').boundingBox();
  await page.mouse.move(heroBox.x+heroBox.width*.78,heroBox.y+heroBox.height*.36);
  await page.waitForTimeout(260);
  const after=await sat.evaluate(el=>getComputedStyle(el).transform);
  if(before===after)throw new Error('satellite regression');
  if(errors.length)throw new Error('page errors: '+errors.join(' | '));

  console.log(JSON.stringify({quickHover:hover,businessHeight:sectionBox.height,labels,satellite:true}));
  await browser.close();
})().catch(e=>{console.error(e);process.exit(1)});
