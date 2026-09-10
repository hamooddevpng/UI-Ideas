const { chromium } = require('playwright-core');
(async()=>{
  const browser=await chromium.launch({headless:true,executablePath:'/usr/bin/google-chrome',args:['--no-sandbox']});
  const page=await browser.newPage({viewport:{width:1600,height:900},deviceScaleFactor:1});
  const errors=[];page.on('pageerror',e=>errors.push(String(e)));
  await page.goto('http://127.0.0.1:8000/42.html',{waitUntil:'domcontentloaded',timeout:45000});
  await page.waitForTimeout(1100);

  const national=page.locator('#png-story');
  await national.scrollIntoViewIfNeeded();
  await page.waitForFunction(()=>document.querySelectorAll('#nationalProvinceNodes .national-mesh-node').length===22,{timeout:10000});
  await page.waitForTimeout(600);

  const geometry=await page.evaluate(()=>{
    const obj=document.getElementById('nationalProvinceMap');
    const doc=obj?.contentDocument;
    if(!doc) return {error:'no embedded province svg document'};
    const raw=[...doc.querySelectorAll('#features > path, #features > polygon')]
      .map(el=>{try{return {el,b:el.getBBox()}}catch(e){return null}})
      .filter(x=>x&&x.b.width>1&&x.b.height>1)
      .sort((a,b)=>(b.b.width*b.b.height)-(a.b.width*a.b.height)).slice(0,22);
    const nodes=[...document.querySelectorAll('#nationalProvinceNodes .national-mesh-node')];
    const root=doc.documentElement,failures=[],coords=[];
    nodes.forEach((node,i)=>{
      const m=(node.getAttribute('transform')||'').match(/translate\(([-\d.]+)\s+([-\d.]+)\)/);
      if(!m||!raw[i]){failures.push({i,reason:'missing transform or province'});return}
      const x=+m[1],y=+m[2],pt=root.createSVGPoint();pt.x=x;pt.y=y;
      let inside=false;try{inside=raw[i].el.isPointInFill(pt)}catch(e){}
      coords.push({i,x,y,inside});
      if(!inside)failures.push({i,x,y,reason:'point outside province fill'});
    });
    const section=document.getElementById('png-story'),map=document.getElementById('nationalMapBackdrop');
    const style=getComputedStyle(section),title=getComputedStyle(section.querySelector('.story-copy h2'));
    return {
      raw:raw.length,nodes:nodes.length,validated:coords.filter(x=>x.inside).length,failures,
      sectionHeight:section.getBoundingClientRect().height,
      sectionBackground:style.backgroundImage,
      titleColor:title.color,
      mapLoaded:map?.naturalWidth>0,
      mapOpacity:map?parseFloat(getComputedStyle(map).opacity):0,
      photo:!!section.querySelector('.png-story-photo'),
      links:document.querySelectorAll('#nationalMeshLinks .national-mesh-link').length,
      packets:document.querySelectorAll('#nationalMeshPackets .national-packet').length
    };
  });
  if(geometry.error)throw new Error(geometry.error);
  if(geometry.raw!==22||geometry.nodes!==22||geometry.validated!==22||geometry.failures.length)throw new Error('province marker geometry validation failed '+JSON.stringify(geometry));
  if(geometry.sectionHeight>810)throw new Error('National Story exceeds 90vh '+JSON.stringify(geometry));
  if(!geometry.mapLoaded||geometry.mapOpacity<.8||geometry.photo)throw new Error('National Story map/background state wrong '+JSON.stringify(geometry));
  if(geometry.links<30||geometry.packets<8)throw new Error('network mesh incomplete '+JSON.stringify(geometry));
  if(geometry.titleColor==='rgb(255, 255, 255)')throw new Error('National Story did not switch to light theme '+JSON.stringify(geometry));

  await page.waitForFunction(()=>document.querySelectorAll('#nationalMeshLinks .national-mesh-link.surge').length>0,{timeout:5000});
  const surge=await page.evaluate(()=>document.querySelectorAll('#nationalMeshLinks .national-mesh-link.surge').length);
  if(surge<1)throw new Error('random province lasers did not fire');

  const stage=page.locator('#nationalMapStage');
  const box=await stage.boundingBox();
  await page.mouse.move(box.x+box.width*.72,box.y+box.height*.44);
  await page.waitForTimeout(220);
  const pointer=await page.evaluate(()=>({
    lasers:document.querySelectorAll('#nationalPointerLasers .national-pointer-laser.live').length,
    core:document.getElementById('nationalPointerCore')?.classList.contains('live')
  }));
  if(pointer.lasers!==4||!pointer.core)throw new Error('pointer connectivity failed '+JSON.stringify(pointer));

  await page.screenshot({path:'/tmp/design42-national-province-points.png',fullPage:false});

  const hero=await page.evaluate(()=>({
    remote:document.querySelector('.scene-remote .hero-island')?.getAttribute('src'),
    tower:!!document.querySelector('.scene-art[data-art="2"] .tower'),
    heroMap:document.querySelector('.scene-enterprise .hero-map')?.getAttribute('src')
  }));
  if(!hero.remote?.includes('png-highlands-landscape.png')||!hero.tower||!hero.heroMap?.includes('png-admin1-simplemaps.svg'))throw new Error('hero regression '+JSON.stringify(hero));
  if(errors.length)throw new Error('page errors: '+errors.join(' | '));

  console.log(JSON.stringify({geometry,surge,pointer,hero,screenshot:'/tmp/design42-national-province-points.png'}));
  await browser.close();
})().catch(e=>{console.error(e);process.exit(1)});
