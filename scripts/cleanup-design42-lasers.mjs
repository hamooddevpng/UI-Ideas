import fs from 'node:fs';
import path from 'node:path';

const root=process.cwd();
const file=path.join(root,'42-base.html');
const apply=process.argv.includes('--apply');
let html=fs.readFileSync(file,'utf8');

const obsolete=[
  {marker:'Design 42: animated laser shots v7',tags:['style','script'],expected:2},
  {marker:'Design 42: robust province lasers v9',tags:['style','script'],expected:2},
  {marker:'Design 42: lasers only v10',tags:['style'],expected:1},
  {marker:'Design 42: simple province lasers v11',tags:['style','script'],expected:2}
];

const blocks=()=>[...html.matchAll(/<(style|script)(?:\s[^>]*)?>([\s\S]*?)<\/\1>/gi)].map(match=>({
  tag:match[1].toLowerCase(),
  body:match[2],
  full:match[0],
  index:match.index
}));

const removals=[];
for(const rule of obsolete){
  const matches=blocks().filter(block=>rule.tags.includes(block.tag)&&block.body.includes(rule.marker));
  if(matches.length!==rule.expected){
    throw new Error(`Expected ${rule.expected} ${rule.marker} block(s), found ${matches.length}. Refusing cleanup.`);
  }
  removals.push(...matches.map(block=>({...block,marker:rule.marker})));
}

for(const item of removals.sort((a,b)=>b.index-a.index)){
  html=html.slice(0,item.index)+html.slice(item.index+item.full.length);
}

for(const rule of obsolete){
  if(html.includes(rule.marker))throw new Error(`Obsolete marker survived cleanup: ${rule.marker}`);
}

const currentBlocks=[...html.matchAll(/<(style|script)(?:\s[^>]*)?>([\s\S]*?)<\/\1>/gi)].map(match=>({
  tag:match[1].toLowerCase(),body:match[2],full:match[0],index:match.index
}));

const oneBlock=(tag,marker)=>{
  const matches=currentBlocks.filter(block=>block.tag===tag&&block.body.includes(marker));
  if(matches.length!==1)throw new Error(`Expected exactly one ${tag} block containing ${marker}, found ${matches.length}`);
  return matches[0];
};

// v6 becomes geometry ownership only. Its older route/shot animation was already
// hidden by later passes, so removing that runtime preserves the rendered result
// while eliminating duplicate timers and invisible SVG work.
const v6=oneBlock('script','Design 42: static province laser network v6');
const pointsMatch=v6.body.match(/const points=(\[[\s\S]*?\]);\s*\n\s*const reduce=/);
if(!pointsMatch)throw new Error('Could not extract validated province coordinates from v6.');
const pointsLiteral=pointsMatch[1];
const v6Replacement=`<script>
// Design 42: static province laser network v6
// Canonical responsibility: validated province coordinates and node geometry only.
(()=>{
  const overlay=document.getElementById('nationalProvinceOverlay');
  if(!overlay||document.getElementById('provinceNetworkV6'))return;
  const NS='http://www.w3.org/2000/svg';
  const points=${pointsLiteral};
  const make=(tag,attrs={})=>{const el=document.createElementNS(NS,tag);Object.entries(attrs).forEach(([key,value])=>el.setAttribute(key,String(value)));return el};
  const layer=make('g',{id:'provinceNetworkV6',class:'province-network-v6'});
  const nodes=make('g',{class:'province-node-layer'});
  layer.appendChild(nodes);
  overlay.appendChild(layer);
  points.forEach(point=>{
    const node=make('g',{class:'province-node-v6','data-province':point.name,transform:\`translate(\${point.x} \${point.y})\`});
    node.append(make('circle',{class:'halo',r:'9'}),make('circle',{class:'dot',r:'4.5'}));
    nodes.appendChild(node);
  });
})();
</script>`;
html=html.slice(0,v6.index)+v6Replacement+html.slice(v6.index+v6.full.length);

// Re-scan after replacing v6 because indexes changed.
const rescan=()=>[...html.matchAll(/<(style|script)(?:\s[^>]*)?>([\s\S]*?)<\/\1>/gi)].map(match=>({tag:match[1].toLowerCase(),body:match[2],full:match[0],index:match.index}));
const unique=(tag,marker)=>{
  const matches=rescan().filter(block=>block.tag===tag&&block.body.includes(marker));
  if(matches.length!==1)throw new Error(`Expected one ${tag} block containing ${marker}, found ${matches.length}`);
  return matches[0];
};

// v13 owns all laser styling. It also owns endpoint feedback that used to leak
// in from v9/v11 through the historical v9-live class.
const v13=unique('style','Design 42: laser tuning v13');
const v13Replacement=`<style>
/* Design 42: laser tuning v13 */
/* Canonical province laser presentation for the active endpoint v12 runtime. */
.province-laser-v12{pointer-events:none;fill:none;stroke-linecap:round;vector-effect:non-scaling-stroke;opacity:1}
.province-laser-v12.glow{display:none}
.province-laser-v12.core{stroke:#079fd2;stroke-width:1.35;filter:none}
.province-node-v6.laser-live .halo{fill:rgba(37,211,255,.28);stroke:#36d8ff;stroke-width:2.2;filter:drop-shadow(0 0 8px rgba(0,196,255,.9))}
.province-node-v6.laser-live .dot{fill:#fff;stroke:#00b7ed;filter:drop-shadow(0 0 5px #fff) drop-shadow(0 0 11px #00b8ef)}
</style>`;
html=html.slice(0,v13.index)+v13Replacement+html.slice(v13.index+v13.full.length);

const v12=unique('script','Design 42: endpoint lasers v12');
let v12Body=v12.body;
const durationNeedle=`      const duration=220+Math.random()*120;\n      const started=performance.now();`;
const durationReplacement=`      const duration=220+Math.random()*120;\n      a.el.classList.add('laser-live');\n      setTimeout(()=>b.el.classList.add('laser-live'),Math.max(80,Math.floor(duration*.68)));\n      const started=performance.now();`;
if(!v12Body.includes(durationNeedle))throw new Error('Could not find v12 duration insertion point.');
v12Body=v12Body.replace(durationNeedle,durationReplacement);
const cleanupNeedle=`          setTimeout(()=>{glow.remove();core.remove()},75);`;
const cleanupReplacement=`          setTimeout(()=>{a.el.classList.remove('laser-live');b.el.classList.remove('laser-live');glow.remove();core.remove()},75);`;
if(!v12Body.includes(cleanupNeedle))throw new Error('Could not find v12 cleanup insertion point.');
v12Body=v12Body.replace(cleanupNeedle,cleanupReplacement);
const v12Replacement=`<script>${v12Body}</script>`;
html=html.slice(0,v12.index)+v12Replacement+html.slice(v12.index+v12.full.length);

const required=[
  'Design 42: static province laser network v6',
  'Design 42: endpoint lasers v12',
  'Design 42: laser tuning v13',
  'province-node-v6.laser-live',
  'provinceLaserLayerV12'
];
for(const marker of required){if(!html.includes(marker))throw new Error(`Required canonical laser marker missing: ${marker}`)}
for(const rule of obsolete){if(html.includes(rule.marker))throw new Error(`Obsolete marker returned: ${rule.marker}`)}

const summary={
  removedBlocks:removals.length,
  removedMarkers:[...new Set(removals.map(item=>item.marker))],
  canonicalFoundation:'v6 province nodes',
  canonicalRuntime:'v12 endpoint lasers',
  canonicalPresentation:'v13 laser tuning',
  bytesBefore:fs.statSync(file).size,
  bytesAfter:Buffer.byteLength(html)
};

if(apply)fs.writeFileSync(file,html);
console.log(JSON.stringify(summary,null,2));
