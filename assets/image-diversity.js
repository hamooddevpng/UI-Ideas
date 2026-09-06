(()=>{
  const enc=f=>'https://commons.wikimedia.org/wiki/Special:FilePath/'+encodeURIComponent(f);
  const title=document.title||'';
  const variant=title.includes('Consumer Services Hub')?'consumer':title.includes('Connected Nation')?'nation':title.includes('Balanced Corporate')?'corporate':title.includes('National Connectivity')?'human':title.includes('Digital Self Service')?'executive':title.includes('Living Network')?'living':null;
  if(!variant)return;

  const pools={
    consumer:[
      'Mt. Hagen Sing sing (49074334702).jpg',
      "Traditional Morobe 'sing sing' (10730256135).jpg",
      'Mt. Hagen Sing Sing. Lady with her bilum (bag) (48951197053).jpg'
    ],
    nation:[
      '(Mount Hagen cultural show in Papua New Guinea) - DPLA - 7857cec288cce6e6407b34026296b200.jpg',
      '(Mount Hagen cultural show in Papua New Guinea) - DPLA - 4d5984e556a57ca49a252e03ef49c319.jpg',
      '(Native warriors performing at sing-sing in Goroka, Papua New Guinea) - DPLA - d78c94bf77525a378cbeac5b42a7e872.jpg'
    ],
    corporate:[
      'Goroka Show - Lastra.jpg',
      "Traditional Morobe 'sing sing' (10730545163).jpg",
      '(Mount Hagen cultural show in Papua New Guinea) - DPLA - 6b637b431fc6fb711b7ce6bfd4c0e92c.jpg'
    ],
    human:[
      'Huli Wigman cultures of Papua New Guinea.jpg',
      'Melpa woman western Highlands of PNG in traditional attire before performing a dance.jpg',
      '(Mount Hagen cultural show in Papua New Guinea) - DPLA - 1d81bea7b7e15e3e36681c88e3dfbc3f.jpg'
    ],
    executive:[
      'Mt Hagen Cultural Show PNG 2008.jpg',
      'Male dancers from Western Highlands in traditional costumes performing a traditional dance.jpg',
      'Папуасские женщины.jpg'
    ],
    living:[
      'Mt Hagen Cultural Show PNG 2008 (cropped).jpg',
      '(Mount Hagen cultural show in Papua New Guinea) - DPLA - 71fc5e53d6c7260785622a2eaf10b642.jpg',
      'Headdress (48858644898).jpg'
    ]
  };

  const apply=()=>{
    const files=pools[variant];
    const heroBgs=[...document.querySelectorAll('.institutional-hero .inst-bg')];
    heroBgs.forEach((el,i)=>{
      if(files[i]){
        el.style.backgroundImage=`url("${enc(files[i])}")`;
        el.style.backgroundPosition=variant==='human'?'center 28%':'center';
      }
    });

    if(variant==='living'){
      const hb=[...document.querySelectorAll('.hero-bg')];
      hb.forEach((el,i)=>{if(files[i]) el.style.backgroundImage=`linear-gradient(90deg,rgba(2,14,24,.67),rgba(2,14,24,.22)),url("${enc(files[i])}")`;});
    }

    if(variant==='human'){
      const mosaic=[...document.querySelectorAll('.ux-story-tile')];
      const extra=[
        '(Mount Hagen cultural show in Papua New Guinea) - DPLA - b9cdb88827e088577c37a24397fde560.jpg',
        'Mount Hagen Sing Sing 2019 (49060446801).jpg',
        'Papua New Guinea Sing Sing. (48986244873).jpg'
      ];
      mosaic.forEach((el,i)=>{if(extra[i]) el.style.backgroundImage=`url("${enc(extra[i])}")`;});
    }
  };

  apply();
  let ticks=0;
  const mo=new MutationObserver(()=>{apply();if(++ticks>18)mo.disconnect();});
  mo.observe(document.documentElement,{childList:true,subtree:true});
  setTimeout(()=>mo.disconnect(),12000);
})();