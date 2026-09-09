const { chromium } = require('playwright-core');
(async()=>{
  const browser=await chromium.launch({headless:true,executablePath:'/usr/bin/google-chrome',args:['--no-sandbox']});
  const page=await browser.newPage({viewport:{width:1440,height:900}});
  const errors=[];page.on('pageerror',e=>errors.push(String(e)));
  await page.goto('http://127.0.0.1:8000/42.html',{waitUntil:'networkidle'});
  const vh=900;
  const sectionHeights=await page.evaluate(()=>Object.fromEntries(['png-story','updates','support'].map(id=>{const el=document.getElementById(id);return [id,el?el.getBoundingClientRect().height:0]})));
  for(const [id,h] of Object.entries(sectionHeights)){if(!h||h>vh*.91)throw new Error(id+' height outside target: '+h)}

  await page.locator('#png-story').scrollIntoViewIfNeeded();await page.waitForTimeout(1100);
  const pngState=await page.evaluate(()=>{const s=document.getElementById('png-story'),img=s.querySelector('.png-story-photo'),b=[...s.querySelectorAll('.png-beacon')];return {live:s.classList.contains('png-live-active'),natural:img.naturalWidth,beacons:b.length,opacity:getComputedStyle(b[3]).opacity,tx:getComputedStyle(s).getPropertyValue('--png-tx').trim()}});
  if(!pngState.live||pngState.natural<100||pngState.beacons!==4||Number(pngState.opacity)<.6)throw new Error('PNG story wake failed '+JSON.stringify(pngState));
  const pr=await page.locator('#png-story').boundingBox();await page.mouse.move(pr.x+pr.width*.82,pr.y+pr.height*.35);await page.waitForTimeout(120);
  const pngTx=await page.evaluate(()=>getComputedStyle(document.getElementById('png-story')).getPropertyValue('--png-tx').trim());
  if(!pngTx||pngTx==='0px')throw new Error('PNG story pointer parallax failed '+pngTx);

  await page.locator('#updates').scrollIntoViewIfNeeded();await page.waitForTimeout(500);
  await page.locator('[data-update-preview="1"]').hover();await page.waitForTimeout(420);
  const updateState=await page.evaluate(()=>({title:document.getElementById('newsLiveTitle').textContent,img:document.getElementById('newsLiveImage').getAttribute('src'),natural:document.getElementById('newsLiveImage').naturalWidth,active:document.querySelector('[data-update-preview="1"]').classList.contains('active')}));
  if(!/customers/i.test(updateState.title)||!updateState.img.includes('news-06.jpg')||updateState.natural<50||!updateState.active)throw new Error('Updates preview failed '+JSON.stringify(updateState));
  await page.locator('[data-update-preview="1"] .notice-head').click();await page.waitForTimeout(100);
  if(!(await page.locator('[data-update-preview="1"]').evaluate(el=>el.classList.contains('open'))))throw new Error('Updates accordion failed');
  const nr=await page.locator('#newsLiveCard').boundingBox();await page.mouse.move(nr.x+nr.width*.82,nr.y+nr.height*.28);await page.waitForTimeout(120);
  const newsRy=await page.evaluate(()=>getComputedStyle(document.getElementById('newsLiveCard')).getPropertyValue('--news-ry').trim());
  if(!newsRy||newsRy==='0deg')throw new Error('News monitor perspective failed '+newsRy);

  await page.locator('#support').scrollIntoViewIfNeeded();await page.waitForTimeout(450);
  const sr=await page.locator('#supportStage').boundingBox();await page.mouse.move(sr.x+sr.width*.78,sr.y+sr.height*.28);await page.waitForTimeout(140);
  const supportMove=await page.evaluate(()=>getComputedStyle(document.getElementById('supportStage')).getPropertyValue('--support-rx').trim());
  if(!supportMove||supportMove==='0px')throw new Error('Support radar pointer movement failed '+supportMove);
  await page.locator('.support-orbit .sn2').hover();await page.waitForTimeout(100);
  const routeValue=await page.locator('#supportCoreValue').textContent();if(routeValue.trim()!=='CONTACT')throw new Error('Support node routing failed '+routeValue);
  await page.locator('#supportQuery').fill('billing');await page.waitForTimeout(100);
  const searchState=await page.evaluate(()=>({searching:document.getElementById('supportStage').classList.contains('searching'),v:document.getElementById('supportCoreValue').textContent,h:document.getElementById('supportHint').textContent}));
  if(!searchState.searching||searchState.v.trim()!=='HELP'||!/billing/i.test(searchState.h))throw new Error('Support search state failed '+JSON.stringify(searchState));

  if((await page.locator('.service-story-card').count())!==5)throw new Error('Service story regression');
  await page.locator('#business').scrollIntoViewIfNeeded();await page.waitForTimeout(300);await page.locator('[data-business-route="1"]').hover();await page.waitForTimeout(180);
  const bizRoute=await page.locator('#businessConsole').getAttribute('data-route');if(bizRoute!=='1')throw new Error('Business command regression '+bizRoute);

  await page.evaluate(()=>scrollTo(0,0));await page.waitForTimeout(250);await page.mouse.move(700,300);await page.locator('[data-scene="1"]').click();await page.waitForTimeout(100);await page.mouse.move(1110,170);await page.waitForTimeout(280);
  const sat1=await page.locator('.satellite').evaluate(el=>getComputedStyle(el).transform);await page.mouse.move(790,410);await page.waitForTimeout(280);const sat2=await page.locator('.satellite').evaluate(el=>getComputedStyle(el).transform);
  if(sat1===sat2)throw new Error('Hero satellite regression');
  if(errors.length)throw new Error('Page errors: '+errors.join(' | '));
  console.log('Design 42 pending sections verified',JSON.stringify({sectionHeights,pngTx,updateState,newsRy,supportMove,searchState,bizRoute,sat1,sat2}));
  await browser.close();
})().catch(e=>{console.error(e);process.exit(1)});
