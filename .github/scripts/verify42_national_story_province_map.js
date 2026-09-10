const { chromium } = require('playwright-core');
(async()=>{
  const browser=await chromium.launch({headless:true,executablePath:'/usr/bin/google-chrome',args:['--no-sandbox']});
  const page=await browser.newPage({viewport:{width:1440,height:900}});
  const errors=[];page.on('pageerror',e=>errors.push(String(e)));
  await page.goto('http://127.0.0.1:8000/42.html',{waitUntil:'domcontentloaded',timeout:45000});
  await page.waitForTimeout(1200);

  // Hero must be restored, with no 22-province overlay/status injected into the banner.
  const heroInfo=await page.evaluate(()=>({
    provinceOverlay:!!document.querySelector('.scene-enterprise .province-network'),
    provinceStatus:!!document.querySelector('.scene-enterprise .province-network-status'),
    peopleOpacity:getComputedStyle(document.querySelector('.scene-phone .hero-people')).opacity,
    remoteRidge:getComputedStyle(document.querySelector('.scene-remote .ridge')).display,
    networkDisplay:getComputedStyle(document.querySelector('.scene-art[data-art="2"] .network-svg')).display,
    gridDisplay:getComputedStyle(document.querySelector('.scene-art[data-art="2"] .grid-plane')).display
  }));
  if(heroInfo.provinceOverlay||heroInfo.provinceStatus)throw new Error('province overlay still exists in hero '+JSON.stringify(heroInfo));
  if(heroInfo.remoteRidge==='none')throw new Error('remote hero mountain drawing still force-hidden '+JSON.stringify(heroInfo));
  if(heroInfo.networkDisplay==='none'||heroInfo.gridDisplay==='none')throw new Error('tower hero network art still hidden '+JSON.stringify(heroInfo));

  // National Story owns the detailed map now.
  const national=page.locator('#png-story');
  await national.scrollIntoViewIfNeeded();
  await page.waitForTimeout(1800);
  const card=page.locator('#nationalMapCard');
  if(await card.count()!==1)throw new Error('national map card missing');
  await page.waitForFunction(()=>document.querySelectorAll('#nationalProvinceOverlay .national-province-node').length>=22,{timeout:10000});
  const mapInfo=await page.evaluate(()=>{
    const obj=document.getElementById('nationalProvinceMap');
    let raw=0;
    try{raw=obj.contentDocument?.querySelectorAll('#features > path, #features > polygon').length||0}catch(e){}
    return {
      objectLoaded:!!obj.contentDocument?.documentElement,
      rawFeatures:raw,
      nodes:document.querySelectorAll('#nationalProvinceOverlay .national-province-node').length,
      links:document.querySelectorAll('#nationalProvinceOverlay .national-province-link').length,
      activeLinks:document.querySelectorAll('#nationalProvinceOverlay .national-province-link.active').length,
      counter:document.getElementById('nationalMapCount')?.textContent,
      sectionHeight:document.getElementById('png-story')?.getBoundingClientRect().height,
      mapBox:document.getElementById('nationalMapCard')?.getBoundingClientRect().toJSON()
    };
  });
  if(!mapInfo.objectLoaded)throw new Error('province SVG object did not load '+JSON.stringify(mapInfo));
  if(mapInfo.rawFeatures<22)throw new Error('province SVG exposes fewer than 22 admin geometries '+JSON.stringify(mapInfo));
  if(mapInfo.links!==22||mapInfo.nodes<22)throw new Error('expected 22 province connections '+JSON.stringify(mapInfo));
  if(mapInfo.activeLinks!==1)throw new Error('province route animation not active '+JSON.stringify(mapInfo));
  if(mapInfo.sectionHeight>810)throw new Error('National Story exceeds 90vh '+JSON.stringify(mapInfo));
  const first=mapInfo.counter;await page.waitForTimeout(1300);const second=await page.locator('#nationalMapCount').textContent();
  if(first===second)throw new Error('province sequence did not advance '+first);

  // Quick action readability and news fix from business feedback remain.
  const quick=await page.evaluate(()=>({p:parseFloat(getComputedStyle(document.querySelector('.quick-card p')).fontSize),h:parseFloat(getComputedStyle(document.querySelector('.quick-card h3')).fontSize)}));
  if(quick.p<8.5||quick.h<18)throw new Error('quick action readability regressed '+JSON.stringify(quick));

  // Hero interaction regression.
  await page.evaluate(()=>scrollTo(0,0));
  await page.waitForTimeout(300);
  await page.locator('.scene-tab[data-scene="1"]').click();
  await page.waitForTimeout(250);
  const sat=page.locator('.satellite'),dish=page.locator('.dish-head-svg');
  const sat0=await sat.evaluate(e=>getComputedStyle(e).transform),dish0=await dish.evaluate(e=>getComputedStyle(e).transform);
  const hb=await page.locator('#top').boundingBox();
  await page.mouse.move(hb.x+hb.width*.77,hb.y+hb.height*.28);await page.waitForTimeout(350);
  const sat1=await sat.evaluate(e=>getComputedStyle(e).transform),dish1=await dish.evaluate(e=>getComputedStyle(e).transform);
  if(sat0===sat1||dish0===dish1)throw new Error('hero satellite/dish regression');
  if(errors.length)throw new Error('page errors: '+errors.join(' | '));
  console.log(JSON.stringify({heroInfo,mapInfo,counterAdvanced:[first,second],quick,satellite:true}));
  await browser.close();
})().catch(e=>{console.error(e);process.exit(1)});
