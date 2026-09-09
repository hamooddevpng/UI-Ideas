const { chromium } = require('playwright-core');
(async()=>{
  const browser=await chromium.launch({headless:true,executablePath:'/usr/bin/google-chrome',args:['--no-sandbox']});
  const page=await browser.newPage({viewport:{width:1440,height:900}});
  const errors=[];page.on('pageerror',e=>errors.push(String(e)));
  await page.goto('http://127.0.0.1:8000/42.html',{waitUntil:'domcontentloaded',timeout:45000});

  const body=await page.locator('body').innerText();
  for(const phrase of ['Move around the hub or search for what you need.','Move across the feed to preview what needs attention','Move across the cards to bring each service into focus.','Move across a service to preview how that service reaches people']){
    if(body.includes(phrase))throw new Error('Tutorial copy remains: '+phrase);
  }

  const story=page.locator('#png-story .png-story-photo');
  const storySrc=await story.getAttribute('src');
  if(storySrc!=='assets/design42/louisiade-archipelago-nasa.jpg')throw new Error('PNG island aerial not applied: '+storySrc);
  await page.waitForFunction(()=>{const i=document.querySelector('#png-story .png-story-photo');return i&&i.complete&&i.naturalWidth>1000},{timeout:10000});

  // Observe the Offers reveal before scrolling so the particle burst cannot be missed.
  await page.evaluate(()=>{
    window.__offerParticles=0;
    const layer=document.getElementById('offerPopLayer');
    if(!layer)throw new Error('offer particle layer missing');
    new MutationObserver(ms=>{for(const m of ms)for(const n of m.addedNodes)if(n.nodeType===1&&(n.classList.contains('offer-pop-particle')||n.classList.contains('offer-pop-ring')))window.__offerParticles++}).observe(layer,{childList:true});
  });
  await page.locator('#offers').scrollIntoViewIfNeeded();
  await page.mouse.wheel(0,120);
  await page.waitForTimeout(4500);
  const offer=await page.evaluate(()=>({live:document.getElementById('offers').classList.contains('offer-pop-live'),particles:window.__offerParticles,cards:[...document.querySelectorAll('#personalOfferGrid .personal-offer')].map(c=>parseFloat(getComputedStyle(c).opacity))}));
  if(!offer.live)throw new Error('offer pop animation did not run');
  if(offer.particles<40)throw new Error('offer burst too weak: '+offer.particles);
  if(offer.cards.some(v=>v<.9))throw new Error('offer cards did not settle');

  await page.locator('#business').scrollIntoViewIfNeeded();await page.waitForTimeout(700);
  if(await page.locator('#businessConsole').count())throw new Error('old network command console still exists');
  if(await page.locator('#business .business-png-map').count())throw new Error('map remains in business section');
  if(await page.locator('#business [data-dual-world]').count()!==2)throw new Error('two-world layout missing');
  const sectionBox=await page.locator('#business').boundingBox();
  if(!sectionBox||sectionBox.height>810)throw new Error('business section exceeds 90vh: '+(sectionBox&&sectionBox.height));
  const motions=await page.locator('#business animateMotion').count();
  if(motions<7)throw new Error('not enough live network packets: '+motions);

  await page.locator('[data-dual-world="government"]').hover();await page.waitForTimeout(250);
  if(await page.locator('#business').getAttribute('data-focus')!=='government')throw new Error('government world did not focus');
  const govOpacity=parseFloat(await page.locator('[data-dual-world="government"]').evaluate(el=>getComputedStyle(el).opacity));
  const bizOpacity=parseFloat(await page.locator('[data-dual-world="business"]').evaluate(el=>getComputedStyle(el).opacity));
  if(govOpacity<=bizOpacity)throw new Error('government focus lacks visual priority');

  const biz=page.locator('[data-dual-world="business"]');const bb=await biz.boundingBox();
  await page.mouse.move(bb.x+bb.width*.82,bb.y+bb.height*.28);await page.waitForTimeout(220);
  const tilted=await biz.evaluate(el=>getComputedStyle(el).transform);
  await page.mouse.move(bb.x+bb.width*.5,bb.y+bb.height*.5);await page.waitForTimeout(220);
  const centered=await biz.evaluate(el=>getComputedStyle(el).transform);
  if(tilted===centered)throw new Error('business SVG world has no mouse depth');

  await page.locator('[data-portfolio="1"]').hover();await page.waitForTimeout(160);
  if((await page.locator('#portfolioTitle').innerText()).trim()!=='Business Systems')throw new Error('portfolio detail did not switch to Business Systems');
  if(!(await page.locator('#portfolioDetail').innerText()).includes('MiVoice'))throw new Error('real business systems detail missing');
  await page.locator('[data-portfolio="3"]').hover();await page.waitForTimeout(160);
  if(await page.locator('#business').getAttribute('data-focus')!=='government')throw new Error('Co-Location did not shift emphasis to government/public side');

  // Hero regression after the large section replacement.
  await page.locator('[data-scene="1"]').click();
  await page.mouse.move(1110,180);await page.waitForTimeout(300);
  const a=await page.evaluate(()=>({sat:getComputedStyle(document.querySelector('.satellite')).transform,dish:getComputedStyle(document.querySelector('.dish-head-svg')).transform}));
  await page.mouse.move(760,430);await page.waitForTimeout(300);
  const b=await page.evaluate(()=>({sat:getComputedStyle(document.querySelector('.satellite')).transform,dish:getComputedStyle(document.querySelector('.dish-head-svg')).transform}));
  if(a.sat===b.sat||a.dish===b.dish)throw new Error('hero satellite/dish regression');

  if(errors.length)throw new Error('page errors: '+errors.join(' | '));
  console.log(JSON.stringify({tutorialCopy:'clean',islandAerial:'loaded',offerParticles:offer.particles,businessHeight:sectionBox.height,networkMotions:motions,businessGovernment:'ok',hero:'ok'}));
  await browser.close();
})().catch(e=>{console.error(e);process.exit(1)});
