const { chromium } = require('playwright-core');
(async()=>{
  const browser=await chromium.launch({headless:true,executablePath:'/usr/bin/google-chrome',args:['--no-sandbox']});
  const page=await browser.newPage({viewport:{width:1440,height:900}});
  const errors=[];page.on('pageerror',e=>errors.push(String(e)));
  await page.goto('http://127.0.0.1:8000/42.html',{waitUntil:'domcontentloaded',timeout:45000});
  await page.waitForTimeout(500);

  const updates=page.locator('#updates');
  await updates.scrollIntoViewIfNeeded();
  await page.waitForTimeout(6500);
  const updateBox=await updates.boundingBox();
  if(!updateBox)throw new Error('updates missing');
  if(updateBox.height>810)throw new Error('updates exceeds 90vh: '+updateBox.height);

  const six=await page.locator('#liveNewsStream .live-feed-card').count();
  if(six!==6)throw new Error('expected 6 live cards after progressive fill, got '+six);
  const idsBefore=await page.locator('#liveNewsStream .live-feed-card').evaluateAll(els=>els.map(e=>e.dataset.liveNews));
  const imgs=await page.locator('#liveNewsStream img').evaluateAll(imgs=>imgs.map(i=>({src:i.getAttribute('src'),w:i.naturalWidth,h:i.naturalHeight})));
  if(imgs.some(i=>i.w<40||i.h<30))throw new Error('live feed image failed '+JSON.stringify(imgs));
  const status=await page.locator('#updatesFeedStatus').textContent();
  if(!/^06 LIVE ITEMS/.test(status||''))throw new Error('live status incorrect '+status);

  await page.waitForTimeout(3600);
  const sixAfter=await page.locator('#liveNewsStream .live-feed-card').count();
  const idsAfter=await page.locator('#liveNewsStream .live-feed-card').evaluateAll(els=>els.map(e=>e.dataset.liveNews));
  if(sixAfter!==6)throw new Error('feed did not stay capped at six');
  if(idsBefore.join('|')===idsAfter.join('|'))throw new Error('feed did not rotate');

  const source=await page.content();
  const expected=[
    'Mt. Kegum High-Capacity Network tower restored',
    'WIN K500,000 this Independence with 321 Lotto and Telikom',
    'Telikom and Lynk Global provide PNG with new connectivity',
    'Av-Comm and Telikom MOU to drive Pacific innovation',
    'Cable vandalism causes communication disruptions',
    'Telikom recruits new staff for retail expansion',
    'Telikom signs exclusive reseller agreement with SkyTel',
    'Industrial & Mining Exhibition & Conference',
    'Telikom co-sponsors Vocal Fusion',
    'Telikom chairman highlights successes at PITA event'
  ];
  for(const t of expected){if(!source.includes(t))throw new Error('missing news item: '+t)}

  const support=page.locator('#support');
  await support.scrollIntoViewIfNeeded();
  await page.waitForTimeout(500);
  const centering=await page.evaluate(()=>{
    const stage=document.getElementById('supportStage').getBoundingClientRect();
    const copy=document.querySelector('#support .support-copy').getBoundingClientRect();
    return {stageCenter:stage.top+stage.height/2,copyCenter:copy.top+copy.height/2,diff:Math.abs((stage.top+stage.height/2)-(copy.top+copy.height/2)),display:getComputedStyle(document.getElementById('supportStage')).display,align:getComputedStyle(document.getElementById('supportStage')).alignItems};
  });
  if(centering.diff>45)throw new Error('support copy not vertically centered '+JSON.stringify(centering));
  if(centering.align!=='center')throw new Error('support align-items not center '+JSON.stringify(centering));

  if(errors.length)throw new Error('page errors: '+errors.join(' | '));
  console.log(JSON.stringify({updatesHeight:updateBox.height,liveCount:six,before:idsBefore,after:idsAfter,status,centering}));
  await browser.close();
})().catch(e=>{console.error(e);process.exit(1)});
