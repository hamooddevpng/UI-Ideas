const { chromium } = require('playwright-core');
(async()=>{
  const browser=await chromium.launch({headless:true,executablePath:'/usr/bin/google-chrome',args:['--no-sandbox']});
  const page=await browser.newPage({viewport:{width:1440,height:900}});
  const errors=[];page.on('pageerror',e=>errors.push(String(e)));
  await page.goto('http://127.0.0.1:8000/42.html',{waitUntil:'domcontentloaded',timeout:45000});
  await page.waitForTimeout(1100);

  // Self Care background visibility
  const selfCare=await page.evaluate(()=>{
    const img=document.querySelector('.scene-phone .hero-people');
    const r=img.getBoundingClientRect(),cs=getComputedStyle(img);
    return {opacity:parseFloat(cs.opacity),w:img.naturalWidth,h:img.naturalHeight,box:[r.width,r.height]};
  });
  if(selfCare.opacity<.4||selfCare.w<500)throw new Error('Self Care image still too hidden '+JSON.stringify(selfCare));

  // Remote scene should use photo, no synthetic ridges
  await page.locator('.scene-tab[data-scene="1"]').click();
  await page.waitForTimeout(650);
  const remote=await page.evaluate(()=>{
    const img=document.querySelector('.scene-remote .hero-island');
    return {opacity:parseFloat(getComputedStyle(img).opacity),w:img.naturalWidth,h:img.naturalHeight,ridges:[...document.querySelectorAll('.scene-remote .ridge')].map(x=>getComputedStyle(x).display)};
  });
  if(remote.opacity<.55||remote.w<500||remote.ridges.some(x=>x!=='none'))throw new Error('Remote hero not corrected '+JSON.stringify(remote));

  // Satellite interaction regression
  const sat=page.locator('.satellite');
  const satBefore=await sat.evaluate(el=>getComputedStyle(el).transform);
  const hero=page.locator('#top');
  const hb=await hero.boundingBox();
  await page.mouse.move(hb.x+hb.width*.83,hb.y+hb.height*.3);
  await page.waitForTimeout(380);
  const satAfter=await sat.evaluate(el=>getComputedStyle(el).transform);
  if(satBefore===satAfter)throw new Error('satellite tracking regressed');

  // 22-province map network
  await page.locator('.scene-tab[data-scene="2"]').click();
  await page.waitForTimeout(900);
  const province=await page.evaluate(()=>{
    const map=document.querySelector('.hero-map'),net=document.querySelector('.province-network');
    const mr=map.getBoundingClientRect(),nr=net.getBoundingClientRect();
    return {
      mapOpacity:parseFloat(getComputedStyle(map).opacity),
      nodes:document.querySelectorAll('.province-node[data-province]').length,
      links:document.querySelectorAll('.province-link').length,
      activeNodes:document.querySelectorAll('.province-node.active').length,
      status:document.querySelector('.province-network-status strong')?.textContent,
      alignment:{dx:Math.abs(mr.left-nr.left),dy:Math.abs(mr.top-nr.top),dw:Math.abs(mr.width-nr.width),dh:Math.abs(mr.height-nr.height)},
      genericDisplay:getComputedStyle(document.querySelector('.scene-art[data-art="2"] .network-svg')).display
    };
  });
  if(province.nodes!==22||province.links!==22||province.activeNodes!==1)throw new Error('province network incomplete '+JSON.stringify(province));
  if(province.status!=='22 PROVINCES'||province.mapOpacity<.45)throw new Error('province status/map visibility failed '+JSON.stringify(province));
  if(Math.max(...Object.values(province.alignment))>2)throw new Error('province overlay not aligned to map '+JSON.stringify(province.alignment));
  if(province.genericDisplay!=='none')throw new Error('old generic network still visible');

  // Quick Actions readability and crisp hover
  const quick=page.locator('#quick-actions');
  await quick.scrollIntoViewIfNeeded();await page.waitForTimeout(500);
  const q=page.locator('#quick-actions .quick-card').first();
  await q.hover();await page.waitForTimeout(220);
  const quickStyle=await q.evaluate(el=>({
    transform:getComputedStyle(el).transform,
    filter:getComputedStyle(el).filter,
    pSize:parseFloat(getComputedStyle(el.querySelector('p')).fontSize),
    qSize:parseFloat(getComputedStyle(el.querySelector('.q-num')).fontSize),
    pColor:getComputedStyle(el.querySelector('p')).color
  }));
  if(quickStyle.transform!=='none'||quickStyle.filter!=='none'||quickStyle.pSize<8.5||quickStyle.qSize<7)throw new Error('Quick Actions clarity failed '+JSON.stringify(quickStyle));

  // News copy should be safely lifted from bottom
  const updates=page.locator('#updates');
  await updates.scrollIntoViewIfNeeded();await page.waitForTimeout(1700);
  const news=await page.evaluate(()=>{
    const f=document.querySelector('#updates .news-feature'),c=document.querySelector('#updates .news-copy'),h=document.querySelector('#updates .news-copy h3');
    const fr=f.getBoundingClientRect(),cr=c.getBoundingClientRect(),hr=h.getBoundingClientRect();
    return {bottomGap:fr.bottom-hr.bottom,copyBottomGap:fr.bottom-cr.bottom,headline:h.textContent.trim(),overflow:getComputedStyle(f).overflow};
  });
  if(news.bottomGap<70)throw new Error('News headline still too low '+JSON.stringify(news));

  if(errors.length)throw new Error('page errors: '+errors.join(' | '));
  console.log(JSON.stringify({selfCare,remote,province,quickStyle,news,satellite:true}));
  await browser.close();
})().catch(e=>{console.error(e);process.exit(1)});
