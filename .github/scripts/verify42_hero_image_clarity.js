const { chromium } = require('playwright-core');
(async()=>{
  const browser=await chromium.launch({headless:true,executablePath:'/usr/bin/google-chrome',args:['--no-sandbox']});
  const page=await browser.newPage({viewport:{width:1440,height:900}});
  const errors=[];page.on('pageerror',e=>errors.push(String(e)));
  await page.goto('http://127.0.0.1:8000/42.html',{waitUntil:'domcontentloaded',timeout:45000});
  await page.waitForTimeout(1200);

  const hero=page.locator('#top');
  const selfImg=page.locator('.scene-phone .hero-people');
  const remoteImg=page.locator('.scene-remote .hero-island');
  const base=await page.evaluate(()=>({
    selfOpacity:parseFloat(getComputedStyle(document.querySelector('.scene-phone .hero-people')).opacity),
    selfBrightness:getComputedStyle(document.querySelector('.scene-phone .hero-people')).filter,
    selfWidth:document.querySelector('.scene-phone .hero-people').naturalWidth,
    remoteSrc:document.querySelector('.scene-remote .hero-island').getAttribute('src'),
    remoteOpacity:parseFloat(getComputedStyle(document.querySelector('.scene-remote .hero-island')).opacity),
    remoteWidth:document.querySelector('.scene-remote .hero-island').naturalWidth,
    ridgeDisplay:getComputedStyle(document.querySelector('.scene-remote .ridge')).display,
    tower:!!document.querySelector('.scene-art[data-art="2"] .tower'),
    heroMap:document.querySelector('.scene-enterprise .hero-map')?.getAttribute('src'),
    networkDisplay:getComputedStyle(document.querySelector('.scene-art[data-art="2"] .network-svg')).display,
    gridDisplay:getComputedStyle(document.querySelector('.scene-art[data-art="2"] .grid-plane')).display
  }));
  if(base.selfOpacity<.45||base.selfWidth<500)throw new Error('Self Care image not visible enough '+JSON.stringify(base));
  if(!base.remoteSrc.endsWith('assets/design42/png-highlands-landscape.png'))throw new Error('Remote hero is not using Highlands asset '+JSON.stringify(base));
  if(base.remoteOpacity<.7||base.remoteWidth<800)throw new Error('Highlands image not visible/loaded '+JSON.stringify(base));
  if(base.ridgeDisplay!=='none')throw new Error('drawn ridges still visible '+JSON.stringify(base));
  if(!base.tower||base.networkDisplay==='none'||base.gridDisplay==='none')throw new Error('tower slide was altered '+JSON.stringify(base));
  if(!base.heroMap?.includes('png-admin1-simplemaps.svg'))throw new Error('tower hero map changed '+JSON.stringify(base));

  await page.locator('.scene-tab[data-scene="1"]').click();
  await page.waitForTimeout(250);
  const sat=page.locator('.satellite'),dish=page.locator('.dish-head-svg');
  const sat0=await sat.evaluate(e=>getComputedStyle(e).transform),dish0=await dish.evaluate(e=>getComputedStyle(e).transform);
  const hb=await hero.boundingBox();
  await page.mouse.move(hb.x+hb.width*.79,hb.y+hb.height*.28);await page.waitForTimeout(380);
  const sat1=await sat.evaluate(e=>getComputedStyle(e).transform),dish1=await dish.evaluate(e=>getComputedStyle(e).transform);
  if(sat0===sat1||dish0===dish1)throw new Error('remote satellite/dish interaction regressed');
  if(errors.length)throw new Error('page errors: '+errors.join(' | '));
  console.log(JSON.stringify({base,satellite:true,dish:true}));
  await browser.close();
})().catch(e=>{console.error(e);process.exit(1)});
