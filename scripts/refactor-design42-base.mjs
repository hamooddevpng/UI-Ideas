import fs from 'node:fs';
import path from 'node:path';

const root=process.cwd();
const basePath=path.join(root,'42-base.html');
const themePath=path.join(root,'assets/design42/design42-theme.css');
const apply=process.argv.includes('--apply');

const paletteMarkers=[
  'Design 42: brighter Telikom palette v2',
  'Design 42: daylight Telikom palette v3',
  'Design 42: daylight palette polish v4'
];

const html=fs.readFileSync(basePath,'utf8');
const styleRegex=/<style(?:\s[^>]*)?>([\s\S]*?)<\/style>/gi;
const blocks=[...html.matchAll(styleRegex)].map(match=>({
  full:match[0],
  css:match[1],
  index:match.index
}));

const selected=[];
for(const marker of paletteMarkers){
  const matches=blocks.filter(block=>block.css.includes(marker));
  if(matches.length!==1){
    throw new Error(`Expected exactly one style block for "${marker}", found ${matches.length}. Refusing to migrate.`);
  }
  selected.push({marker,...matches[0]});
}

selected.sort((a,b)=>a.index-b.index);
const selectedSet=new Set(selected.map(item=>item.full));
let cleaned=html;
for(const item of [...selected].sort((a,b)=>b.index-a.index)){
  const before=cleaned.length;
  cleaned=cleaned.slice(0,item.index)+cleaned.slice(item.index+item.full.length);
  if(cleaned.length===before)throw new Error(`Failed to remove ${item.marker}`);
}

for(const marker of paletteMarkers){
  if(cleaned.includes(marker))throw new Error(`Marker remained after migration: ${marker}`);
}

const normalizeSection=(css,marker,index)=>{
  const withoutMarker=css.replace(new RegExp(`/\\*\\s*${marker.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')}\\s*\\*/`,'i'),'').trim();
  return `/* Canonical theme migration layer ${index+1}. Preserved cascade from the approved pre-refactor render. */\n${withoutMarker}`;
};

const theme=`/*
 * Design 42 canonical theme owner.
 *
 * Stage 1 of the refactor moves the final three historical palette passes out of
 * 42-base.html without changing their cascade order. A later cleanup pass can
 * simplify declarations inside this one file with visual regression coverage.
 */\n\n${selected.map((item,index)=>normalizeSection(item.css,item.marker,index)).join('\n\n')}\n`;

const summary={
  sourceStyleBlocks:blocks.length,
  migratedPaletteBlocks:selected.length,
  sourceBytes:Buffer.byteLength(html),
  cleanedBytes:Buffer.byteLength(cleaned),
  themeBytes:Buffer.byteLength(theme),
  markers:paletteMarkers
};

if(!apply){
  console.log(JSON.stringify(summary,null,2));
  process.exit(0);
}

fs.mkdirSync(path.dirname(themePath),{recursive:true});
fs.writeFileSync(basePath,cleaned);
fs.writeFileSync(themePath,theme);
console.log(JSON.stringify(summary,null,2));
