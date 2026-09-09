const { chromium } = require('playwright-core');
(async()=>{
  const browser=await chromium.launch({headless:true,executablePath:'/usr/bin/google-chrome',args:['--no-sandbox']});
  const page=await browser.newPage({viewport:{width:1440,height:900}});
  const errors=[]; page.on('pageerror',e=>errors.push(String(e)));
  await page.goto('http://127.0.0.1:8000/42.html',{waitUntil:'domcontentloaded',timeout:45000});
  await page.waitForTimeout(600);

  const title=await page.title();
  if(!title.includes('Telikom PNG')||title.includes('Design 42'))throw new Error('SEO title not production-ready: '+title);
  const content=(sel,attr='content')=>page.locator(sel).first().getAttribute(attr);
  const description=await content('meta[name="description"]');
  if(!description||description.length<120||description.length>190)throw new Error('meta description length invalid '+(description&&description.length));
  const robots=await content('meta[name="robots"]');
  if(!robots||!robots.includes('index')||robots.includes('noindex'))throw new Error('robots directive wrong: '+robots);
  for(const bot of ['googlebot','bingbot']){
    const value=await content(`meta[name="${bot}"]`);
    if(!value||!value.includes('index'))throw new Error(bot+' metadata missing');
  }

  const canonical=await page.locator('link[rel="canonical"]').getAttribute('href');
  if(canonical!=='https://www.telikom.com.pg/')throw new Error('canonical wrong '+canonical);
  if(await page.locator('link[rel="alternate"][hreflang="en-PG"]').count()!==1)throw new Error('en-PG hreflang missing');
  if(await page.locator('link[rel="alternate"][hreflang="x-default"]').count()!==1)throw new Error('x-default hreflang missing');

  const ogRequired=['og:type','og:url','og:site_name','og:title','og:description','og:locale','og:image','og:image:alt'];
  for(const prop of ogRequired){if(await page.locator(`meta[property="${prop}"]`).count()!==1)throw new Error('missing '+prop)}
  const twitterRequired=['twitter:card','twitter:title','twitter:description','twitter:image','twitter:image:alt'];
  for(const name of twitterRequired){if(await page.locator(`meta[name="${name}"]`).count()!==1)throw new Error('missing '+name)}
  for(const name of ['application-name','author','publisher','theme-color','color-scheme','geo.region','geo.placename']){
    if(await page.locator(`meta[name="${name}"]`).count()!==1)throw new Error('missing meta '+name);
  }
  if(await page.locator('link[rel="icon"]').count()!==1)throw new Error('favicon link missing');
  if(await page.locator('link[rel="apple-touch-icon"]').count()!==1)throw new Error('apple touch icon missing');
  if(await page.locator('link[rel="preload"][as="image"]').count()!==1)throw new Error('hero image preload missing');

  const raw=await page.locator('#telikomSeoSchema').textContent();
  let schema; try{schema=JSON.parse(raw)}catch(e){throw new Error('JSON-LD invalid '+e.message)}
  if(schema['@context']!=='https://schema.org'||!Array.isArray(schema['@graph']))throw new Error('schema graph invalid');
  const types=schema['@graph'].map(x=>x['@type']);
  for(const type of ['Organization','WebSite','WebPage','ItemList'])if(!types.includes(type))throw new Error('schema type missing '+type);
  const items=schema['@graph'].find(x=>x['@type']==='ItemList');
  if(!items||items.itemListElement.length<7)throw new Error('service schema incomplete');
  if(await page.locator('meta[name="robots"][content*="noindex"]').count())throw new Error('legacy noindex remains');

  if(await page.locator('#top').count()!==1||await page.locator('#offers').count()!==1||await page.locator('#business').count()!==1)throw new Error('page structure regression');
  await page.locator('[data-scene="1"]').click();
  await page.waitForTimeout(300);
  await page.mouse.move(1100,180); await page.waitForTimeout(180);
  const sx=await page.locator('#top').evaluate(el=>getComputedStyle(el).getPropertyValue('--sat-x'));
  if(!sx||Math.abs(parseFloat(sx))<.05)throw new Error('hero interaction regression');

  if(errors.length)throw new Error('page errors: '+errors.join(' | '));
  console.log(JSON.stringify({title,descriptionLength:description.length,canonical,robots,og:ogRequired.length,twitter:twitterRequired.length,schemaTypes:types,services:items.itemListElement.length,hero:true}));
  await browser.close();
})().catch(e=>{console.error(e);process.exit(1)});
