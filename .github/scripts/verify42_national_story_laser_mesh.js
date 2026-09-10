const { chromium } = require('playwright-core');
(async()=>{
  const browser=await chromium.launch({headless:true,executablePath:'/usr/bin/google-chrome',args:['--no-sandbox']});
  const page=await browser.newPage({viewport:{width:1440,height:900}});
  const errors=[];page.on('pageerror',e=>errors.push(String(e)));
  await page.goto('http://127.0.0.1:8000/42.html',{waitUntil:'domcontentloaded',timeout:45000});
  await page.waitForTimeout(1200);

  // Hero must remain untouched by this pass.
  const hero=await page.evaluate(()=>({
    provinceOverlay:!!document.querySelector('.scene-enterprise .province-network'),
    provinceStatus:!!document.querySelector('.scene-enterprise .province-network-status'),
    tower:!!document.querySelector('.scene-art[data-art="2"] .tower'),
    networkDisplay:getComputedStyle(document.querySelector('.scene-art[data-art="2"] .network-svg')).display,
    gridDisplay:getComputedStyle(document.querySelector('.scene-art[data-art="2"] .grid-plane')).display
  }));
  if(hero.provinceOverlay||hero.provinceStatus||!hero.tower||hero.networkDisplay==='none'||hero.gridDisplay==='none')throw new Error('hero changed '+JSON.stringify(hero));

  const national=page.locator('#png-story');await national.scrollIntoViewIfNeeded();await page.waitForTimeout(1800);
  await page.waitForFunction(()=>document.querySelectorAll('#nationalProvinceNodes .national-mesh-node').length===22,{timeout:10000});
  const info=await page.evaluate(()=>({
    sectionHeight:document.getElementById('png-story').getBoundingClientRect().height,
    backdropSrc:document.getElementById('nationalMapBackdrop')?.getAttribute('src'),
    backdropLoaded:document.getElementById('nationalMapBackdrop')?.complete && document.getElementById('nationalMapBackdrop')?.naturalWidth>0,
    nodes:document.querySelectorAll('#nationalProvinceNodes .national-mesh-node').length,
    links:document.querySelectorAll('#nationalMeshLinks .national-mesh-link').length,
    packets:document.querySelectorAll('#nationalMeshPackets .national-packet').length,
    count:document.getElementById('nationalMapCount')?.textContent,
    cardBg:getComputedStyle(document.getElementById('nationalMapCard')).backgroundImage
  }));
  if(info.sectionHeight>810)throw new Error('National Story too tall '+JSON.stringify(info));
  if(!info.backdropLoaded||!String(info.backdropSrc).includes('png-admin1-national-light.svg'))throw new Error('light map backdrop missing '+JSON.stringify(info));
  if(info.nodes!==22||info.links<22||info.packets<8)throw new Error('laser mesh incomplete '+JSON.stringify(info));
  if(info.count.trim()!=='22 / 22')throw new Error('counter incorrect '+JSON.stringify(info));

  const box=await page.locator('#nationalMapStage').boundingBox();
  await page.mouse.move(box.x+box.width*.61,box.y+box.height*.46);await page.waitForTimeout(250);
  const pointer=await page.evaluate(()=>({
    lasers:document.querySelectorAll('#nationalPointerLasers .national-pointer-laser.live').length,
    core:document.getElementById('nationalPointerCore')?.classList.contains('live'),
    state:document.getElementById('nationalMapState')?.textContent,
    hot:document.querySelectorAll('#nationalProvinceNodes .national-mesh-node.hot').length
  }));
  if(pointer.lasers!==4||!pointer.core||pointer.state!=='POINTER LINK ACTIVE'||pointer.hot<3)throw new Error('pointer laser interaction failed '+JSON.stringify(pointer));

  // Existing quick-action readability still holds.
  const quick=await page.evaluate(()=>({p:parseFloat(getComputedStyle(document.querySelector('.quick-card p')).fontSize),h:parseFloat(getComputedStyle(document.querySelector('.quick-card h3')).fontSize)}));
  if(quick.p<8.5||quick.h<18)throw new Error('quick readability regressed '+JSON.stringify(quick));

  if(errors.length)throw new Error('page errors: '+errors.join(' | '));
  console.log(JSON.stringify({hero,info,pointer,quick}));
  await browser.close();
})().catch(e=>{console.error(e);process.exit(1)});
