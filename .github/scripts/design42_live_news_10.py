from pathlib import Path
import re

p=Path('42.html')
s=p.read_text()

# Start the status at zero. The live feed fills progressively once visible.
s=s.replace('<small id="updatesFeedStatus">03 ITEMS · TELIKOM</small>','<small id="updatesFeedStatus">00 LIVE ITEMS · TELIKOM</small>',1)

# Give the featured story CTA a real official media destination that JS can keep in sync.
s=s.replace('<a class="btn dark" href="#">View update ↗</a></div></article></div>',
'''<a class="btn dark" id="newsLiveLink" href="https://www.telikom.com.pg/media/news/" target="_blank" rel="noreferrer">View update ↗</a></div></article></div>''',1)

feed_pattern=re.compile(r'''  const feed=\[.*?\n  \];\n  let visible=false,visibleMs=0,last=performance\.now\(\),initial=0,cycleMs=0,next=0,previewTimer=null;\n  const thresholds=\[1000,3000,5000\];''',re.S)
new_feed='''  const feed=[
    {id:'kegum',k:'Network',date:'16 APR 2025',t:'Mt. Kegum High-Capacity Network tower restored',p:'Telikom reported the restoration of the Mt. Kegum HCN telecommunications tower and renewed connectivity for affected areas.',img:'assets/common/web-sourced/telikom/mt-kegum.jpg',url:'https://www.telikom.com.pg/media/news/'},
    {id:'lotto',k:'Promotion',date:'11 SEP 2024',t:'WIN K500,000 this Independence with 321 Lotto and Telikom',p:'An Independence promotion from Telikom and 321 Lotto with a K500,000 headline prize.',img:'assets/common/web-sourced/telikom/lotto.jpg',url:'https://www.telikom.com.pg/media/news/'},
    {id:'lynk',k:'Connectivity',date:'21 DEC 2023',t:'Telikom and Lynk Global provide PNG with new connectivity',p:'Telikom announced an agreement with Lynk Global focused on satellite direct-to-phone connectivity for Papua New Guinea.',img:'assets/common/web-sourced/telikom/news-01.jpg',url:'https://www.telikom.com.pg/media/news/'},
    {id:'avcomm',k:'Partnership',date:'09 NOV 2023',t:'Av-Comm and Telikom MOU to drive Pacific innovation',p:'Telikom and Av-Comm announced an MOU focused on telecommunications innovation and evolving Pacific connectivity needs.',img:'assets/common/web-sourced/telikom/news-02.jpg',url:'https://www.telikom.com.pg/media/news/'},
    {id:'cable',k:'Service Notice',date:'16 OCT 2023',t:'Cable vandalism causes communication disruptions',p:'Telikom published an update addressing communication disruptions associated with a rise in cable vandalism.',img:'assets/common/web-sourced/telikom/news-03.jpg',url:'https://www.telikom.com.pg/media/news/'},
    {id:'retail',k:'Company',date:'01 JUL 2023',t:'Telikom recruits new staff for retail expansion',p:'Telikom shared an update on new staff recruitment supporting its retail expansion drive.',img:'assets/common/web-sourced/telikom/news-04.jpg',url:'https://www.telikom.com.pg/media/news/'},
    {id:'skytel',k:'Business',date:'30 JUN 2023',t:'Telikom signs exclusive reseller agreement with SkyTel',p:'Telikom announced an exclusive reseller agreement with SkyTel as part of its business connectivity portfolio.',img:'assets/common/web-sourced/telikom/news-05.jpg',url:'https://www.telikom.com.pg/media/news/'},
    {id:'mining',k:'Industry',date:'21 JUN 2023',t:'Industrial & Mining Exhibition & Conference',p:'Telikom highlighted its participation in an industrial and mining exhibition and conference in Papua New Guinea.',img:'assets/common/web-sourced/telikom/news-06.jpg',url:'https://www.telikom.com.pg/media/news/'},
    {id:'vocal',k:'Community',date:'11 JUN 2023',t:'Telikom co-sponsors Vocal Fusion',p:'Telikom shared its support for EMTV’s Vocal Fusion and the local talent platform behind the programme.',img:'assets/common/web-sourced/telikom/news-07.jpg',url:'https://www.telikom.com.pg/media/news/'},
    {id:'pita',k:'Corporate',date:'01 JUN 2023',t:'Telikom chairman highlights successes at PITA event',p:'Telikom published a corporate update following the Pacific Islands Telecommunications Association event.',img:'assets/common/web-sourced/telikom/news-08.jpg',url:'https://www.telikom.com.pg/media/news/'}
  ];
  let visible=false,visibleMs=0,last=performance.now(),initial=0,cycleMs=0,next=0,previewTimer=null;
  const thresholds=[900,1700,2600,3600,4700,5900];'''
s,n=feed_pattern.subn(new_feed,s,count=1)
if n!=1:
    raise SystemExit('live news feed block not found')

# Add date and official media link to the featured preview.
s=s.replace("const card=document.getElementById('newsLiveCard'),img=document.getElementById('newsLiveImage'),kicker=document.getElementById('newsLiveKicker'),title=document.getElementById('newsLiveTitle'),text=document.getElementById('newsLiveText');",
"const card=document.getElementById('newsLiveCard'),img=document.getElementById('newsLiveImage'),kicker=document.getElementById('newsLiveKicker'),title=document.getElementById('newsLiveTitle'),text=document.getElementById('newsLiveText'),newsLink=document.getElementById('newsLiveLink');",1)

s=s.replace("previewTimer=setTimeout(()=>{img.src=d.img;img.alt=d.t;kicker.textContent=d.k;title.textContent=d.t+'.';text.textContent=d.p;card.classList.remove('switching')},170);",
"previewTimer=setTimeout(()=>{img.src=d.img;img.alt=d.t;kicker.textContent=d.k+' · '+d.date;title.textContent=d.t; text.textContent=d.p;if(newsLink)newsLink.href=d.url||'https://www.telikom.com.pg/media/news/';card.classList.remove('switching')},170);",1)

s=s.replace("el.innerHTML='<div class=\"live-feed-thumb\"><img src=\"'+d.img+'\" alt=\"\"></div><div class=\"live-feed-copy\"><small>'+d.k+'</small><b>'+d.t+'</b></div><span class=\"live-feed-now\">NUPELA</span>';",
"el.innerHTML='<div class=\"live-feed-thumb\"><img src=\"'+d.img+'\" alt=\"\"></div><div class=\"live-feed-copy\"><small>'+d.k+' · '+d.date+'</small><b>'+d.t+'</b></div><span class=\"live-feed-now\">NUPELA</span>';",1)

s=s.replace("if(stream.children.length>=3){const old=stream.firstElementChild;old.classList.add('leaving');setTimeout(()=>{old.remove();insert()},380)}else insert();",
"if(stream.children.length>=6){const old=stream.firstElementChild;old.classList.add('leaving');setTimeout(()=>{old.remove();insert()},380)}else insert();",1)

# More room for six compact cards while keeping the whole section under the desktop height ceiling.
css=r'''
/* Design 42: six-item live newsroom + vertically centred support copy */
.live-news-stream{height:288px!important;margin-top:8px!important;padding-top:7px!important}
.live-feed-card{height:44px!important;margin-bottom:4px!important;padding:4px 7px 4px 4px!important;grid-template-columns:48px minmax(0,1fr) auto!important;gap:8px!important;border-radius:11px!important}
.live-feed-thumb{width:48px!important;height:34px!important;border-radius:8px!important}
.live-feed-copy small{font-size:5.2px!important;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.live-feed-copy b{font-size:7.8px!important;margin-top:2px!important}
.live-feed-now{font-size:4.8px!important;padding:3px 5px!important}
.updates-live .updates-grid{min-height:420px!important}
.updates-live .news-feature{min-height:420px!important}
.updates-console{padding-bottom:12px!important}
.feed-meter{margin-top:8px!important}
@media(min-width:821px){
  .support-orbit .support-stage{display:flex;align-items:center}
  .support-orbit .support-copy{margin-top:0;margin-bottom:0}
}
@media(max-width:820px){
  .live-news-stream{height:288px!important}
  .support-orbit .support-stage{display:block}
}
'''
if 'Design 42: six-item live newsroom + vertically centred support copy' in s:
    raise SystemExit('live newsroom patch already present')
pos=s.rfind('</style>')
if pos<0:
    raise SystemExit('style close missing')
s=s[:pos]+css+s[pos:]

p.write_text(s)
