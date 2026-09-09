const { chromium } = require('playwright-core');
(async()=>{
  const browser=await chromium.launch({headless:true,executablePath:'/usr/bin/google-chrome',args:['--no-sandbox']});
  const page=await browser.newPage({viewport:{width:1440,height:900}});
  const errors=[]; page.on('pageerror',e=>errors.push(String(e)));
  await page.goto('http://127.0.0.1:8000/42.html',{waitUntil:'domcontentloaded',timeout:45000});
  await page.waitForTimeout(700);

  const heroImg=page.locator('.scene-phone .hero-people');
  if((await heroImg.getAttribute('src'))!=='assets/design42/png-selfcare-fao.jpg')throw new Error('Self Care FAO image not wired');
  const heroImageState=await heroImg.evaluate(el=>({w:el.naturalWidth,h:el.naturalHeight,complete:el.complete,opacity:+getComputedStyle(el).opacity}));
  if(!heroImageState.complete||heroImageState.w<600||heroImageState.h<300)throw new Error('FAO image did not load '+JSON.stringify(heroImageState));
  if(heroImageState.opacity<.16)throw new Error('Self Care image too faint '+heroImageState.opacity);

  const offerImages=await page.locator('#personalOfferGrid .personal-offer-media img').evaluateAll(es=>es.map(e=>e.getAttribute('src')));
  if(offerImages.length!==3||new Set(offerImages).size!==3)throw new Error('Offers repeated imagery '+JSON.stringify(offerImages));
  for(const src of offerImages){
    const img=page.locator(`#personalOfferGrid .personal-offer-media img[src="${src}"]`).first();
    const ok=await img.evaluate(el=>el.complete&&el.naturalWidth>0);
    if(!ok)throw new Error('Offer image failed '+src);
  }

  const bodyText=await page.locator('body').innerText();
  if(!bodyText.includes('Nambawan'))throw new Error('Nambawan microcopy missing');
  if(!bodyText.includes('Bilong yumi'))throw new Error('Bilong yumi microcopy missing');

  const header=page.locator('#header'),brand=page.locator('#header .brand'),logo=page.locator('#header .brand img'),nav=page.locator('#header .main-nav');
  const [hr,br,lr,nr]=await Promise.all([header.boundingBox(),brand.boundingBox(),logo.boundingBox(),nav.boundingBox()]);
  if(!hr||!br||!lr||!nr)throw new Error('Navbar geometry unavailable');
  if(lr.top<br.top-1||lr.bottom>br.bottom+1||br.height>=hr.height)throw new Error('Logo does not fit navbar '+JSON.stringify({hr,br,lr}));
  if(br.right>nr.left+2)throw new Error('Logo overlaps navigation '+JSON.stringify({br,nr}));

  const business=page.locator('#business');
  const businessState=await business.evaluate(el=>({flag:getComputedStyle(el).getPropertyValue('--business-light-pass').trim(),bg:getComputedStyle(el).backgroundImage}));
  if(businessState.flag!=='1')throw new Error('Lighter business palette missing');
  if(!businessState.bg.includes('rgb(11, 49, 65)'))throw new Error('Unexpected business palette '+businessState.bg);
  const bizBox=await business.boundingBox();
  if(!bizBox||bizBox.height>810)throw new Error('Business section exceeds 90vh '+(bizBox&&bizBox.height));

  // Regression: restored map stays in tower hero, not Business/Government.
  if(await page.locator('.scene-enterprise .hero-map').count()!==1)throw new Error('Tower hero map missing');
  if(await page.locator('#business .hero-map,#business .business-png-map').count())throw new Error('Map leaked into Business/Government');

  // Live feed regression plus Tok Pisin Nupela label.
  await page.locator('#updates').scrollIntoViewIfNeeded();
  await page.waitForTimeout(1350);
  const live=page.locator('#liveNewsStream .live-feed-card');
  if(await live.count()<1)throw new Error('Live news feed did not start');
  if((await live.first().locator('.live-feed-now').innerText()).trim()!=='NUPELA')throw new Error('Nupela live label missing');

  if(errors.length)throw new Error('page errors: '+errors.join(' | '));
  console.log(JSON.stringify({heroImage:heroImageState,offerImages,logo:{brand:br,logo:lr,nav:nr},business:businessState.bg,tokPisin:['Nambawan','Bilong yumi','Nupela'],liveNews:true}));
  await browser.close();
})().catch(e=>{console.error(e);process.exit(1)});
