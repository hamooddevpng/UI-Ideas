import fs from 'node:fs';
import path from 'node:path';

const root=process.cwd();
const basePath=path.join(root,'42-base.html');
const corePath=path.join(root,'assets/design42/design42-core.css');
const componentsPath=path.join(root,'assets/design42/design42-components.css');
const apply=process.argv.includes('--apply');

const html=fs.readFileSync(basePath,'utf8');
const styleRegex=/<style(?:\s[^>]*)?>([\s\S]*?)<\/style>/gi;
const blocks=[...html.matchAll(styleRegex)].map(match=>({
  full:match[0],
  css:match[1],
  index:match.index
}));

if(blocks.length!==5){
  throw new Error(`Expected exactly 5 remaining Design 42 style blocks, found ${blocks.length}. Refusing to extract.`);
}

const definitions=[
  {key:'core',marker:'Design 42: magnetic service deck'},
  {key:'assistant',marker:'Design 42: Ask Telikom side assistant v1'},
  {key:'obsoletePatch',marker:'Design 42: targeted lighter dark sections v1'},
  {key:'footer',marker:'Design 42 footer social icons'},
  {key:'laser',marker:'Design 42: laser tuning v13'}
];

const found={};
for(const definition of definitions){
  const matches=blocks.filter(block=>block.css.includes(definition.marker));
  if(matches.length!==1){
    throw new Error(`Expected exactly one style block containing "${definition.marker}", found ${matches.length}. Refusing to extract.`);
  }
  found[definition.key]=matches[0];
}

const recognized=new Set(Object.values(found).map(block=>block.index));
if(recognized.size!==blocks.length){
  throw new Error('At least one remaining style block is not covered by the explicit extraction map. Refusing to guess ownership.');
}

let cleaned=html;
for(const block of [...blocks].sort((a,b)=>b.index-a.index)){
  cleaned=cleaned.slice(0,block.index)+cleaned.slice(block.index+block.full.length);
}

if(/<style(?:\s|>)/i.test(cleaned)){
  throw new Error('Inline style blocks remain after extraction.');
}

const banner=(title,description)=>`/*\n * ${title}\n * ${description}\n * Extracted from 42-base.html without selector rewrites so visual behavior stays stable.\n */\n\n`;

const coreCss=
  banner(
    'Design 42 core stylesheet',
    'Owns the original page structure, layout, responsive rules, component foundations and motion.'
  )+found.core.css.trim()+"\n";

const componentBlocks=[found.assistant,found.footer,found.laser].sort((a,b)=>a.index-b.index);
const componentsCss=
  banner(
    'Design 42 component stylesheet',
    'Owns later component additions that intentionally load after the isolated Digital PNG prototype CSS.'
  )+componentBlocks.map(block=>block.css.trim()).join('\n\n')+"\n";

for(const [label,css] of [['core',coreCss],['components',componentsCss]]){
  if(css.includes('Design 42: targeted lighter dark sections v1')){
    throw new Error(`Obsolete lighter-dark patch leaked into ${label} stylesheet.`);
  }
}

const summary={
  sourceStyleBlocks:blocks.length,
  coreBytes:Buffer.byteLength(coreCss),
  componentsBytes:Buffer.byteLength(componentsCss),
  cleanedBaseBytes:Buffer.byteLength(cleaned),
  removedObsoletePatch:true,
  componentOrder:componentBlocks.map(block=>{
    const definition=definitions.find(item=>block.css.includes(item.marker));
    return definition?.key||'unknown';
  })
};

if(!apply){
  console.log(JSON.stringify(summary,null,2));
  process.exit(0);
}

fs.mkdirSync(path.dirname(corePath),{recursive:true});
fs.writeFileSync(basePath,cleaned);
fs.writeFileSync(corePath,coreCss);
fs.writeFileSync(componentsPath,componentsCss);
console.log(JSON.stringify(summary,null,2));
