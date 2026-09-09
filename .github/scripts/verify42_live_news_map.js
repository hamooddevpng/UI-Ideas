const { chromium } = require('playwright-core');
(async()=>{
  const browser=await chromium.launch({headless:true,executablePath:'/usr/bin/google-chrome',args:['--no-sandbox']});
  const page=await browser.newPage({viewport:{width:1440,height:900}});
  const errors=[]; page.on('pageerror',e=>errors.push(String(e)));
  await page.goto('http://127.0.0.1:8000/42.html',{waitUntil:'domcontentloaded',timeout:45000});

  // Hero map is back only in the tower / PNG Network slide.
  const map=page.locator('.scene-enterprise .hero-map');
  if(await map.count()!==1)throw new Error('hero PNG map missing');
  if((await map.getAttribute('src'))!=='assets/design42/png-admin1-simplemaps.svg')throw new Error('wrong hero map source');
  await page.locator('[data-scene="2"]').click();
  await page.waitForTimeout(500);
  const mapState=await map.evaluate(el=>({opacity:parseFloat(getComputedStyle(el).opacity),w:el.naturalWidth,h:el.naturalHeight}));
  if(mapState.opacity<.1||mapState.w<500||mapState.h<300)throw new Error('hero map not visibly loaded '+JSON.stringify(mapState));
  if(await page.locator('#business .hero-map,#business .business-png-map').count())throw new Error('map leaked into Business/Government section');

  // Observe live feed timing after Updates is actually visible.
  await page.locator('#updates').scrollIntoViewIfNeeded();
  await page.waitForTimeout(1250);
  let ids=await page.locator('#liveNewsStream [data-live-news]').evaluateAll(es=>es.map(e=>e.dataset.liveNews));
  if(ids.length!==1)throw new Error('expected 1 live news card after ~1s, got '+ids.length);
  await page.waitForTimeout(2050);
  ids=await page.locator('#liveNewsStream [data-live-news]').evaluateAll(es=>es.map(e=>e.dataset.liveNews));
  if(ids.length!==2)throw new Error('expected 2 live news cards after ~3s, got '+ids.length);
  await page.waitForTimeout(2050);
  ids=await page.locator('#liveNewsStream [data-live-news]').evaluateAll(es=>es.map(e=>e.dataset.liveNews));
  if(ids.length!==3)throw new Error('expected 3 live news cards after ~5s, got '+ids.length);
  const first=ids[0], thirdSet=[...ids];
  await page.waitForTimeout(3650);
  const nextIds=await page.locator('#liveNewsStream [data-live-news]').evaluateAll(es=>es.map(e=>e.dataset.liveNews));
  if(nextIds.length!==3)throw new Error('live feed should stay capped at 3 cards');
  if(nextIds.includes(first))throw new Error('oldest live card did not rotate out');
  if(nextIds.join('|')===thirdSet.join('|'))throw new Error('live feed did not rotate');
  const status=(await page.locator('#updatesFeedStatus').innerText()).trim();
  if(!status.includes('03 LIVE ITEMS'))throw new Error('live feed status not updated: '+status);
  const featureTitle=(await page.locator('#newsLiveTitle').innerText()).trim();
  if(!featureTitle)throw new Error('featured news did not update');
  const updatesBox=await page.locator('#updates').boundingBox();
  if(!updatesBox||updatesBox.height>810)throw new Error('updates section exceeds 90vh: '+(updatesBox&&updatesBox.height));

  // Pause behavior: while section is out of view the feed should stop rotating.
  const beforePause=nextIds.join('|');
  await page.locator('#support').scrollIntoViewIfNeeded();
  await page.waitForTimeout(3600);
  const paused=await page.locator('#liveNewsStream [data-live-news]').evaluateAll(es=>es.map(e=>e.dataset.liveNews).join('|'));
  if(paused!==beforePause)throw new Error('live feed kept rotating while Updates was offscreen');

  // Hero regression: tower still has heartbeat pulse machinery.
  if(await page.locator('.tower-pulse-track').count()<2)throw new Error('tower pulse tracks missing');
  if(errors.length)throw new Error('page errors: '+errors.join(' | '));
  console.log(JSON.stringify({heroMap:mapState,initialTimeline:'1-3-5s',rotatedFrom:thirdSet,rotatedTo:nextIds,paused:true,updatesHeight:updatesBox.height,status,featureTitle}));
  await browser.close();
})().catch(e=>{console.error(e);process.exit(1)});
