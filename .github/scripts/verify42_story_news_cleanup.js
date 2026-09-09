const { chromium } = require('playwright-core');
(async()=>{
  const browser=await chromium.launch({headless:true,executablePath:'/usr/bin/google-chrome',args:['--no-sandbox']});
  const page=await browser.newPage({viewport:{width:1440,height:900}});
  const errors=[]; page.on('pageerror',e=>errors.push(String(e)));
  await page.goto('http://127.0.0.1:8000/42.html',{waitUntil:'domcontentloaded',timeout:45000});
  await page.waitForTimeout(800);

  const story=page.locator('#png-story');
  await story.scrollIntoViewIfNeeded();
  await page.waitForTimeout(500);
  const img=page.locator('#png-story .png-story-photo');
  const state=await img.evaluate(el=>({src:el.getAttribute('src'),w:el.naturalWidth,h:el.naturalHeight,complete:el.complete,filter:getComputedStyle(el).filter}));
  if(state.src!=='assets/design42/milne-bay-aerial.jpg')throw new Error('Milne Bay image not wired '+JSON.stringify(state));
  if(!state.complete||state.w<700||state.h<400)throw new Error('Milne Bay image failed '+JSON.stringify(state));
  if(!state.filter.includes('brightness(0.82)'))throw new Error('story brightness override missing '+state.filter);
  const storyBox=await story.boundingBox();
  if(!storyBox||storyBox.height>810)throw new Error('PNG story exceeds 90vh '+(storyBox&&storyBox.height));

  const updates=page.locator('#updates');
  await updates.scrollIntoViewIfNeeded();
  await page.waitForTimeout(350);
  if(await page.locator('#updates .notice-row').count())throw new Error('old confusing notice controls still present');
  if(await page.locator('#updates .live-feed-heading').count()!==1)throw new Error('live feed heading missing');
  const heading=(await page.locator('#updates .live-feed-heading').innerText()).replace(/\s+/g,' ').trim();
  if(!heading.includes('Notices & news')||!heading.includes('LIVE'))throw new Error('live feed heading unclear '+heading);

  await page.waitForTimeout(1100);
  const live=page.locator('#liveNewsStream .live-feed-card');
  if(await live.count()<1)throw new Error('live news did not start after one second');
  await page.waitForTimeout(2200);
  if(await live.count()<2)throw new Error('second live news item missing');
  await page.waitForTimeout(2200);
  if(await live.count()<3)throw new Error('third live news item missing');
  const updateBox=await updates.boundingBox();
  if(!updateBox||updateBox.height>810)throw new Error('updates exceeds 90vh '+(updateBox&&updateBox.height));

  // Important regressions.
  if(await page.locator('.scene-enterprise .hero-map').count()!==1)throw new Error('hero map regression');
  if(await page.locator('#business .dual-world').count()!==2)throw new Error('business worlds regression');
  if(errors.length)throw new Error('page errors: '+errors.join(' | '));

  console.log(JSON.stringify({story:state,storyHeight:storyBox.height,newsControlsRemoved:true,liveCount:await live.count(),updatesHeight:updateBox.height,heading}));
  await browser.close();
})().catch(e=>{console.error(e);process.exit(1)});
