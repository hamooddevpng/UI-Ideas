const { chromium } = require('playwright-core');
(async()=>{
  const browser=await chromium.launch({headless:true,executablePath:'/usr/bin/google-chrome',args:['--no-sandbox']});
  const page=await browser.newPage({viewport:{width:1440,height:900}});
  const errors=[];page.on('pageerror',e=>errors.push(String(e)));
  await page.goto('http://127.0.0.1:8000/42.html',{waitUntil:'domcontentloaded',timeout:45000});
  await page.waitForTimeout(600);

  const hero=page.locator('#top');
  const heroBox=await hero.boundingBox();
  if(!heroBox||heroBox.height<490||heroBox.height>620)throw new Error('hero geometry changed unexpectedly '+JSON.stringify(heroBox));

  const quick=page.locator('#quick-actions');
  await quick.scrollIntoViewIfNeeded();
  await page.waitForTimeout(900);
  const count=await page.locator('#quickDeck .quick-card').count();
  if(count!==8)throw new Error('expected 8 quick actions, got '+count);
  const labels=await page.locator('#quickDeck .quick-card h3').allTextContents();
  const expected=['Top Up','Balance','Pay Bill','Bundles','Transfer','Internet','Business','Support'];
  if(expected.some(x=>!labels.includes(x)))throw new Error('missing quick action '+JSON.stringify({labels,expected}));
  const quickBox=await quick.boundingBox();
  if(!quickBox||quickBox.height>420)throw new Error('quick action section too tall '+JSON.stringify(quickBox));
  const ready=await quick.evaluate(el=>el.classList.contains('quick-ready'));
  if(!ready)throw new Error('quick action entrance did not arm');

  const topup=page.locator('[data-quick-selfcare="topup"]');
  const transformBefore=await topup.evaluate(el=>getComputedStyle(el).transform);
  const b=await topup.boundingBox();
  if(!b)throw new Error('topup card missing box');
  await page.mouse.move(b.x+b.width*.78,b.y+b.height*.32);
  await page.waitForTimeout(260);
  const hover=await topup.evaluate(el=>({hot:el.classList.contains('quick-hot'),transform:getComputedStyle(el).transform,sparks:el.querySelectorAll('.quick-spark').length}));
  if(!hover.hot)throw new Error('quick hover state missing');
  if(hover.transform===transformBefore)throw new Error('quick card did not tilt/lift');
  if(hover.sparks<1)throw new Error('quick spark burst missing');

  await topup.click();
  await page.waitForTimeout(450);
  const overlay=page.locator('#phoneOverlay');
  const opened=await overlay.evaluate(el=>el.classList.contains('open'));
  const headline=await page.locator('#overlayHeadline').textContent();
  if(!opened||!(headline||'').includes('Top Up'))throw new Error('Top Up quick action did not open matching Self Care panel '+headline);
  await page.locator('#phoneClose').click();
  await page.waitForTimeout(250);

  await hero.scrollIntoViewIfNeeded();
  await page.waitForTimeout(350);
  await page.locator('.scene-tab[data-scene="1"]').click();
  await page.waitForTimeout(800);
  const sat=page.locator('.satellite'),dish=page.locator('.dish-head-svg');
  const sat0=await sat.evaluate(el=>getComputedStyle(el).transform),dish0=await dish.evaluate(el=>getComputedStyle(el).transform);
  const hb=await hero.boundingBox();
  await page.mouse.move(hb.x+hb.width*.83,hb.y+hb.height*.28);
  await page.waitForTimeout(500);
  const sat1=await sat.evaluate(el=>getComputedStyle(el).transform),dish1=await dish.evaluate(el=>getComputedStyle(el).transform);
  if(sat0===sat1||dish0===dish1)throw new Error('hero satellite/dish regression');

  if(errors.length)throw new Error('page errors: '+errors.join(' | '));
  console.log(JSON.stringify({heroHeight:heroBox.height,quickHeight:quickBox.height,count,labels,hover,topupHeadline:headline,satellite:true}));
  await browser.close();
})().catch(e=>{console.error(e);process.exit(1)});
