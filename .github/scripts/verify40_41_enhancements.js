const {chromium}=require('playwright-core');
(async()=>{
  const browser=await chromium.launch({headless:true,executablePath:'/usr/bin/google-chrome',args:['--no-sandbox']});
  const page=await browser.newPage({viewport:{width:1440,height:900}});

  await page.goto('http://127.0.0.1:8000/40.html',{waitUntil:'networkidle'});
  await page.locator('#services').scrollIntoViewIfNeeded();
  await page.waitForTimeout(300);
  const stories=page.locator('#services .service-story');
  if(await stories.count()!==6) throw new Error('Design 40 service stories missing');
  if(!await stories.nth(0).evaluate(el=>el.classList.contains('active-story'))) throw new Error('Design 40 default active story missing');
  await stories.nth(2).hover();
  await page.waitForTimeout(160);
  const d40focus=await stories.nth(2).evaluate(el=>({active:el.classList.contains('active-story'),grow:getComputedStyle(el).flexGrow,height:el.closest('#services').getBoundingClientRect().height}));
  const d40neighbor=await stories.nth(1).evaluate(el=>getComputedStyle(el).flexGrow);
  if(!d40focus.active || Number(d40focus.grow)<=Number(d40neighbor)) throw new Error('Design 40 cinematic service ribbon failed '+JSON.stringify({d40focus,d40neighbor}));
  if(d40focus.height>810) throw new Error('Design 40 service section exceeds 90vh '+d40focus.height);
  const sbox=await stories.nth(2).boundingBox();
  await page.mouse.move(sbox.x+sbox.width*.82,sbox.y+sbox.height*.25);await page.waitForTimeout(90);
  const imgTransform=await stories.nth(2).locator('img').evaluate(el=>getComputedStyle(el).transform);
  if(!imgTransform || imgTransform==='none') throw new Error('Design 40 story image parallax failed');

  const plan=page.locator('#offers .plan-card').first();await plan.scrollIntoViewIfNeeded();const pbox=await plan.boundingBox();await page.mouse.move(pbox.x+pbox.width*.84,pbox.y+pbox.height*.22);await page.waitForTimeout(100);const planTransform=await plan.evaluate(el=>getComputedStyle(el).transform);if(!planTransform||planTransform==='none')throw new Error('Design 40 plan tilt failed');
  const pngArt=page.locator('.png-art');await pngArt.scrollIntoViewIfNeeded();await pngArt.hover();await page.waitForTimeout(100);const scan=await pngArt.evaluate(el=>({live:el.classList.contains('scan-live'),scan:!!el.querySelector('.png-signal-scan'),spots:el.querySelectorAll('.png-hotspot').length}));if(!scan.live||!scan.scan||scan.spots!==3)throw new Error('Design 40 PNG scan failed '+JSON.stringify(scan));

  await page.goto('http://127.0.0.1:8000/41.html',{waitUntil:'networkidle'});
  const offer=page.locator('#offers .offer-card').first();await offer.scrollIntoViewIfNeeded();const obox=await offer.boundingBox();await page.mouse.move(obox.x+obox.width*.8,obox.y+obox.height*.2);await page.waitForTimeout(120);const offerState=await offer.evaluate(el=>({active:el.classList.contains('offer-active'),transform:getComputedStyle(el).transform,focus:el.closest('.offer-deck').classList.contains('offer-focus')}));if(!offerState.active||!offerState.focus||!offerState.transform||offerState.transform==='none')throw new Error('Design 41 offer gravity failed '+JSON.stringify(offerState));

  const photo=page.locator('.service-photo');await photo.scrollIntoViewIfNeeded();const ph=await photo.boundingBox();await page.mouse.move(ph.x+ph.width*.78,ph.y+ph.height*.25);await page.waitForTimeout(120);const serviceTransform=await photo.evaluate(el=>getComputedStyle(el).transform);if(!serviceTransform||serviceTransform==='none')throw new Error('Design 41 service depth failed');

  const enterprise=page.locator('.enterprise-media');await enterprise.scrollIntoViewIfNeeded();await page.waitForTimeout(300);const packets=page.locator('.enterprise-media .data-packet');if(await packets.count()!==4)throw new Error('Design 41 data packets missing: '+await packets.count());const pos1=await packets.first().evaluate(el=>[el.getAttribute('cx'),el.getAttribute('cy')]);await page.waitForTimeout(260);const pos2=await packets.first().evaluate(el=>[el.getAttribute('cx'),el.getAttribute('cy')]);if(pos1[0]===pos2[0]&&pos1[1]===pos2[1])throw new Error('Design 41 data packet did not move');

  const collage=page.locator('.story-collage');await collage.scrollIntoViewIfNeeded();const cb=await collage.boundingBox();await page.mouse.move(cb.x+cb.width*.82,cb.y+cb.height*.3);await page.waitForTimeout(100);const collTransform=await collage.locator('.story-main').evaluate(el=>getComputedStyle(el).transform);if(!collTransform||collTransform==='none')throw new Error('Design 41 collage depth failed');await page.locator('.story-step').nth(1).click();await page.waitForTimeout(80);if(!await collage.evaluate(el=>el.classList.contains('story-shuffle')))throw new Error('Design 41 collage shuffle failed');

  console.log('Design 40/41 interaction verification passed',JSON.stringify({d40ServiceHeight:d40focus.height,d40Plan:planTransform,d41Offer:offerState.transform,packetStart:pos1,packetLater:pos2}));
  await browser.close();
})().catch(e=>{console.error(e);process.exit(1)});
