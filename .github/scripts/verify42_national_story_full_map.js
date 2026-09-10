const { chromium } = require('playwright-core');
(async()=>{
  const browser=await chromium.launch({headless:true,executablePath:'/usr/bin/google-chrome',args:['--no-sandbox']});
  const page=await browser.newPage({viewport:{width:1440,height:900}});
  const errors=[];page.on('pageerror',e=>errors.push(String(e)));
  await page.goto('http://127.0.0.1:8000/42.html',{waitUntil:'domcontentloaded',timeout:45000});
  await page.waitForTimeout(1200);

  // Remote hero keeps Highlands image, hides drawn ridges, and has a two-sided vignette.
  const remote=await page.evaluate(()=>({
    src:document.querySelector('.scene-remote .hero-island')?.getAttribute('src'),
    ridge:getComputedStyle(document.querySelector('.scene-remote .ridge')).display,
    overlay:getComputedStyle(document.querySelector('.scene-remote'),'::after').backgroundImage,
    satellite:!!document.querySelector('.satellite'),
    dish:!!document.querySelector('.dish-head-svg'),
    tower:!!document.querySelector('.scene-art[data-art="2"] .tower')
  }));
  if(!remote.src?.endsWith('assets/design42/png-highlands-landscape.png'))throw new Error('remote Highlands image changed '+JSON.stringify(remote));
  if(remote.ridge!=='none')throw new Error('drawn remote ridges returned '+JSON.stringify(remote));
  if(!remote.overlay.includes('linear-gradient'))throw new Error('remote vignette missing '+JSON.stringify(remote));
  if(!remote.satellite||!remote.dish||!remote.tower)throw new Error('hero art regression '+JSON.stringify(remote));

  // National Story should no longer use a photographic wallpaper or visible card container.
  const national=page.locator('#png-story');
  await national.scrollIntoViewIfNeeded();
  await page.waitForTimeout(1500);
  await page.waitForFunction(()=>document.querySelectorAll('#nationalProvinceNodes .national-mesh-node').length>=22,{timeout:10000});
  const info=await page.evaluate(()=>{
    const section=document.getElementById('png-story'),card=document.getElementById('nationalMapCard'),stage=document.getElementById('nationalMapStage'),map=document.getElementById('nationalMapBackdrop');
    const cr=getComputedStyle(card),sr=stage.getBoundingClientRect(),rr=section.getBoundingClientRect(),mr=map.getBoundingClientRect();
    return {
      photo:!!section.querySelector('.png-story-photo'),
      className:section.className,
      sectionHeight:rr.height,
      cardBg:cr.backgroundColor,
      cardBorder:cr.borderTopWidth,
      cardRadius:cr.borderTopLeftRadius,
      stageWidth:sr.width,
      sectionWidth:rr.width,
      mapWidth:mr.width,
      mapHeight:mr.height,
      mapSrc:map.getAttribute('src'),
      mapLoaded:map.naturalWidth>0,
      nodes:document.querySelectorAll('#nationalProvinceNodes .national-mesh-node').length,
      links:document.querySelectorAll('#nationalMeshLinks .national-mesh-link').length,
      packets:document.querySelectorAll('#nationalMeshPackets .national-packet').length,
      counter:document.getElementById('nationalMapCount')?.textContent
    };
  });
  if(info.photo)throw new Error('old island wallpaper still present '+JSON.stringify(info));
  if(!info.className.includes('national-story-map'))throw new Error('full map section class missing '+JSON.stringify(info));
  if(info.cardBorder!=='0px'||info.cardRadius!=='0px')throw new Error('map still reads as a card '+JSON.stringify(info));
  if(!info.mapSrc?.includes('png-admin1-national-light.svg')||!info.mapLoaded)throw new Error('province map background missing '+JSON.stringify(info));
  if(info.nodes!==22||info.links<30||info.packets<8)throw new Error('national network incomplete '+JSON.stringify(info));
  if(info.stageWidth<info.sectionWidth*.55)throw new Error('map is not large enough to act as section artwork '+JSON.stringify(info));
  if(info.sectionHeight>810)throw new Error('National Story exceeds 90vh '+JSON.stringify(info));

  // A random province-to-province laser should fire automatically.
  await page.waitForFunction(()=>document.querySelectorAll('#nationalMeshLinks .national-mesh-link.surge').length>0,{timeout:4500});
  const surge=await page.evaluate(()=>document.querySelectorAll('#nationalMeshLinks .national-mesh-link.surge').length);
  if(surge<1||surge>3)throw new Error('random laser firing count unexpected '+surge);

  // Pointer lasers still connect provinces to the pointer.
  const box=await page.locator('#nationalMapStage').boundingBox();
  await page.mouse.move(box.x+box.width*.72,box.y+box.height*.42);
  await page.waitForTimeout(250);
  const pointer=await page.evaluate(()=>({
    lasers:document.querySelectorAll('#nationalPointerLasers .national-pointer-laser.live').length,
    core:document.getElementById('nationalPointerCore')?.classList.contains('live'),
    state:document.getElementById('nationalMapState')?.textContent
  }));
  if(pointer.lasers!==4||!pointer.core)throw new Error('pointer connectivity regression '+JSON.stringify(pointer));

  // Satellite/dish tracking regression.
  await page.evaluate(()=>scrollTo(0,0));
  await page.waitForTimeout(250);
  await page.locator('.scene-tab[data-scene="1"]').click();
  await page.waitForTimeout(250);
  const sat=page.locator('.satellite'),dish=page.locator('.dish-head-svg');
  const s0=await sat.evaluate(e=>getComputedStyle(e).transform),d0=await dish.evaluate(e=>getComputedStyle(e).transform);
  const hb=await page.locator('#top').boundingBox();
  await page.mouse.move(hb.x+hb.width*.78,hb.y+hb.height*.30);await page.waitForTimeout(380);
  const s1=await sat.evaluate(e=>getComputedStyle(e).transform),d1=await dish.evaluate(e=>getComputedStyle(e).transform);
  if(s0===s1||d0===d1)throw new Error('satellite/dish interaction regressed');

  if(errors.length)throw new Error('page errors: '+errors.join(' | '));
  console.log(JSON.stringify({remote,info,surge,pointer,satellite:true,dish:true}));
  await browser.close();
})().catch(e=>{console.error(e);process.exit(1)});
