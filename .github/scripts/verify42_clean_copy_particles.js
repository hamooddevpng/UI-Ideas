const { chromium } = require('playwright-core');
(async()=>{
  const browser=await chromium.launch({headless:true,executablePath:'/usr/bin/google-chrome',args:['--no-sandbox']});
  const page=await browser.newPage({viewport:{width:1440,height:900}});
  page.on('pageerror',e=>{throw e});
  await page.goto('http://127.0.0.1:8000/42.html',{waitUntil:'domcontentloaded',timeout:45000});

  const body=await page.locator('body').innerText();
  const banned=[
    'Move around the hub or search for what you need.',
    'Move across the feed to preview what needs attention',
    'Move across the cards to bring each service into focus.',
    'Move across a service to preview how that service reaches people'
  ];
  for(const phrase of banned)if(body.includes(phrase))throw new Error('Tutorial copy remains: '+phrase);

  const story=page.locator('#png-story .png-story-photo');
  const src=await story.getAttribute('src');
  if(!src||!src.includes('louisiade_tmo_2002254_lrg.jpg'))throw new Error('PNG aerial image not applied: '+src);
  await page.waitForFunction(()=>{const img=document.querySelector('#png-story .png-story-photo');return img&&img.complete&&img.naturalWidth>0},{timeout:20000});

  await page.evaluate(()=>{
    window.__offerParticleCount=0;
    const layer=document.getElementById('offerPopLayer');
    if(!layer)throw new Error('offerPopLayer missing');
    new MutationObserver(ms=>{for(const m of ms)for(const n of m.addedNodes)if(n.nodeType===1&&(n.classList.contains('offer-pop-particle')||n.classList.contains('offer-pop-ring')))window.__offerParticleCount++}).observe(layer,{childList:true});
  });
  await page.locator('#offers').scrollIntoViewIfNeeded();
  await page.mouse.wheel(0,120);
  await page.waitForTimeout(4200);
  const offerState=await page.evaluate(()=>({live:document.getElementById('offers').classList.contains('offer-pop-live'),particles:window.__offerParticleCount,cards:[...document.querySelectorAll('#personalOfferGrid .personal-offer')].map(c=>({opacity:getComputedStyle(c).opacity,rect:c.getBoundingClientRect().toJSON()}))}));
  if(!offerState.live)throw new Error('Offer pop sequence never armed');
  if(offerState.particles<25)throw new Error('Too few offer burst particles: '+offerState.particles);
  if(offerState.cards.length!==3)throw new Error('Offer cards missing');
  if(offerState.cards.some(c=>parseFloat(c.opacity)<.9))throw new Error('Offer cards did not settle visibly');

  await page.locator('[data-scene="1"]').click();
  await page.mouse.move(1110,180);await page.waitForTimeout(280);
  const a=await page.evaluate(()=>({sat:getComputedStyle(document.querySelector('.satellite')).transform,dish:getComputedStyle(document.querySelector('.dish-head-svg')).transform}));
  await page.mouse.move(760,430);await page.waitForTimeout(280);
  const b=await page.evaluate(()=>({sat:getComputedStyle(document.querySelector('.satellite')).transform,dish:getComputedStyle(document.querySelector('.dish-head-svg')).transform}));
  if(a.sat===b.sat||a.dish===b.dish)throw new Error('Hero satellite/dish regression');

  console.log(JSON.stringify({tutorialCopy:'clean',storyImage:src,offerParticles:offerState.particles,hero:'ok'}));
  await browser.close();
})().catch(e=>{console.error(e);process.exit(1)});
