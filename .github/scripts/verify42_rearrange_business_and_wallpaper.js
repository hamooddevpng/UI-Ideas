const { chromium } = require('playwright-core');
(async()=>{
  const browser=await chromium.launch({headless:true,executablePath:'/usr/bin/google-chrome',args:['--no-sandbox']});
  const page=await browser.newPage({viewport:{width:1440,height:900}});
  const errors=[];page.on('pageerror',e=>errors.push(String(e)));
  await page.goto('http://127.0.0.1:8000/42.html',{waitUntil:'domcontentloaded',timeout:45000});
  await page.waitForTimeout(900);

  const business=page.locator('#business');
  await business.scrollIntoViewIfNeeded();
  await page.waitForTimeout(900);
  const sectionBox=await business.boundingBox();
  if(!sectionBox)throw new Error('business section missing');
  if(sectionBox.height>810)throw new Error('business exceeds 90vh at 1440x900: '+sectionBox.height);

  const stage=page.locator('#businessDualStage');
  const biz=page.locator('.business-world');
  const gov=page.locator('.government-world');
  const bizBox=await biz.boundingBox(),govBox=await gov.boundingBox();
  if(!bizBox||!govBox)throw new Error('mission panels missing');
  if(bizBox.width<1100||govBox.width<1100)throw new Error('mission panels are not full-width bands '+JSON.stringify({bizBox,govBox}));
  if(govBox.y < bizBox.y + bizBox.height - 4)throw new Error('mission panels are not stacked '+JSON.stringify({bizBox,govBox}));

  const separation=await page.evaluate(()=>{
    const rect=s=>document.querySelector(s).getBoundingClientRect();
    const bc=rect('.business-world .dual-world-copy'),ba=rect('.business-world .dual-art-wrap');
    const ga=rect('.government-world .dual-art-wrap'),gc=rect('.government-world .dual-world-copy');
    return {businessGap:ba.left-bc.right,governmentGap:gc.left-ga.right,businessFont:parseFloat(getComputedStyle(document.querySelector('.business-world .dual-world-copy p')).fontSize),governmentFont:parseFloat(getComputedStyle(document.querySelector('.government-world .dual-world-copy p')).fontSize)};
  });
  if(separation.businessGap < -30||separation.governmentGap < -30)throw new Error('copy/art overlap '+JSON.stringify(separation));
  if(separation.businessFont<10||separation.governmentFont<10)throw new Error('mission copy still too small '+JSON.stringify(separation));

  const featureDisplay=await page.locator('#portfolioFeature').evaluate(el=>getComputedStyle(el).display);
  if(featureDisplay!=='none')throw new Error('duplicated featured service card still visible');
  const chips=page.locator('#businessPortfolio .portfolio-chip');
  if(await chips.count()!==7)throw new Error('expected 7 service cards');
  const rail=await page.evaluate(()=>({
    heading:document.querySelector('.portfolio-rail-heading b')?.textContent,
    cardHeight:document.querySelector('.portfolio-chip')?.getBoundingClientRect().height,
    titleFont:parseFloat(getComputedStyle(document.querySelector('.portfolio-card-copy b')).fontSize)
  }));
  if(rail.heading!=='Explore business services')throw new Error('portfolio heading missing '+JSON.stringify(rail));
  if(rail.cardHeight<125||rail.titleFont<10.5)throw new Error('service cards still too small '+JSON.stringify(rail));

  const png=page.locator('#png-story');
  await png.scrollIntoViewIfNeeded();
  await page.waitForTimeout(1800);
  const photo=await page.locator('#png-story .png-story-photo').evaluate(img=>({src:img.currentSrc||img.src,w:img.naturalWidth,h:img.naturalHeight,fit:getComputedStyle(img).objectFit}));
  if(!photo.src.includes('14558429'))throw new Error('new Salamaua wallpaper not active '+JSON.stringify(photo));
  if(photo.w<1800||photo.h<900)throw new Error('wallpaper resolution too small '+JSON.stringify(photo));
  if(photo.fit!=='cover')throw new Error('wallpaper is not cover '+JSON.stringify(photo));

  await page.locator('#top').scrollIntoViewIfNeeded();
  await page.waitForTimeout(250);
  await page.locator('.scene-tab[data-scene="1"]').click();
  await page.waitForTimeout(800);
  const satBefore=await page.locator('.satellite').evaluate(el=>getComputedStyle(el).transform);
  await page.mouse.move(1260,220);await page.waitForTimeout(450);
  const satAfter=await page.locator('.satellite').evaluate(el=>getComputedStyle(el).transform);
  if(satBefore===satAfter)throw new Error('hero satellite regression');

  if(errors.length)throw new Error('page errors: '+errors.join(' | '));
  console.log(JSON.stringify({businessHeight:sectionBox.height,bizBox,govBox,separation,rail,photo}));
  await browser.close();
})().catch(e=>{console.error(e);process.exit(1)});
