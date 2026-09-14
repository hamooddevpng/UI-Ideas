(function(root,factory){
  const api=factory();
  if(typeof module==='object'&&module.exports){
    module.exports=api;
  }else{
    root.Design42ServiceScroll=api;
    const boot=()=>api.init();
    if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',boot,{once:true});
    else boot();
  }
})(typeof window!=='undefined'?window:globalThis,function(){
  const clamp=(value,min,max)=>Math.max(min,Math.min(max,value));

  function scrollProgress(scrollY,start,distance){
    if(distance<=0)return 0;
    return clamp((scrollY-start)/distance,0,1);
  }

  function horizontalOffset(progress,scrollWidth,clientWidth){
    const maxScroll=Math.max(0,scrollWidth-clientWidth);
    return maxScroll*clamp(progress,0,1);
  }

  function journeyStart(gridPageTop,viewportHeight,startViewportRatio=.82){
    return gridPageTop-(viewportHeight*startViewportRatio);
  }

  function computeJourneyMetrics(scrollWidth,clientWidth,viewportHeight){
    const maxScroll=Math.max(0,scrollWidth-clientWidth);
    if(maxScroll<=0)return{maxScroll:0,journeyDistance:0,holdDistance:0,runway:0};
    const journeyDistance=Math.round(clamp(maxScroll*1.35,720,1280));
    const holdDistance=Math.round(clamp(viewportHeight*.30,180,300));
    return{maxScroll,journeyDistance,holdDistance,runway:journeyDistance+holdDistance};
  }

  function init(){
    const section=document.getElementById('services');
    const grid=document.getElementById('serviceStoryGrid');
    if(!section||!grid)return;

    const mobileQuery=matchMedia('(max-width:820px)');
    const reduceQuery=matchMedia('(prefers-reduced-motion: reduce)');
    const startViewportRatio=.82;
    let marker=section.querySelector('.service-scroll-start');
    if(!marker){
      marker=document.createElement('span');
      marker.className='service-scroll-start';
      marker.setAttribute('aria-hidden','true');
      grid.before(marker);
    }
    let journeyDistance=0;
    let frame=0;

    const viewportHeight=()=>innerHeight||document.documentElement.clientHeight||800;
    const markerPageTop=()=>scrollY+marker.getBoundingClientRect().top;

    function update(){
      frame=0;
      if(!mobileQuery.matches||reduceQuery.matches||journeyDistance<=0)return;
      const start=journeyStart(markerPageTop(),viewportHeight(),startViewportRatio);
      const progress=scrollProgress(scrollY,start,journeyDistance);
      const target=horizontalOffset(progress,grid.scrollWidth,grid.clientWidth);
      if(Math.abs(grid.scrollLeft-target)>.5)grid.scrollLeft=target;
    }

    function schedule(){
      if(frame)return;
      frame=requestAnimationFrame(update);
    }

    function measure(){
      if(!mobileQuery.matches||reduceQuery.matches){
        journeyDistance=0;
        section.style.removeProperty('--service-scroll-runway');
        grid.scrollLeft=0;
        return;
      }

      const metrics=computeJourneyMetrics(grid.scrollWidth,grid.clientWidth,viewportHeight());
      journeyDistance=metrics.journeyDistance;
      if(metrics.runway>0)section.style.setProperty('--service-scroll-runway',`${metrics.runway}px`);
      else section.style.removeProperty('--service-scroll-runway');
      schedule();
    }

    addEventListener('scroll',schedule,{passive:true});
    addEventListener('resize',measure,{passive:true});
    mobileQuery.addEventListener?.('change',measure);
    reduceQuery.addEventListener?.('change',measure);

    requestAnimationFrame(()=>{
      measure();
      requestAnimationFrame(measure);
    });
  }

  return{clamp,scrollProgress,horizontalOffset,journeyStart,computeJourneyMetrics,init};
});
