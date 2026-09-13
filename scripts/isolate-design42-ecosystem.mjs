import fs from 'node:fs';
import path from 'node:path';

const root=process.cwd();
const apply=process.argv.includes('--apply');
const paths={
  core:path.join(root,'assets/design42/design42-core.css'),
  ecosystem:path.join(root,'assets/design42/design42-ecosystem.css'),
  prototype:path.join(root,'design42-ecosystem-v2.html'),
  loader:path.join(root,'42.html'),
  audit:path.join(root,'scripts/audit-design42.mjs')
};

const read=file=>fs.readFileSync(file,'utf8');
const replaceOnce=(text,from,to,label)=>{
  const first=text.indexOf(from);
  if(first<0)throw new Error(`Could not find ${label}. Refusing migration.`);
  if(text.indexOf(from,first+from.length)>=0)throw new Error(`Found ${label} more than once. Refusing migration.`);
  return text.slice(0,first)+to+text.slice(first+from.length);
};

let prototype=read(paths.prototype);
const styleMatches=[...prototype.matchAll(/<style(?:\s[^>]*)?>([\s\S]*?)<\/style>/gi)];
if(styleMatches.length!==1)throw new Error(`Expected exactly one Digital PNG prototype style block, found ${styleMatches.length}.`);
const styleMatch=styleMatches[0];
let ecosystemCss=styleMatch[1].trim();

// Scope prototype-era globals to the Digital PNG section. These declarations
// previously leaked into the full page because the prototype was injected into
// the same document as Design 42.
ecosystemCss=replaceOnce(ecosystemCss,':root{','.eco-section{','ecosystem :root token block');
ecosystemCss=replaceOnce(ecosystemCss,'*{box-sizing:border-box}','.eco-section,.eco-section *{box-sizing:border-box}','global box-sizing rule');
ecosystemCss=replaceOnce(ecosystemCss,'html{background:#f6fbfb}\n','','global html background');
ecosystemCss=replaceOnce(
  ecosystemCss,
  'body{margin:0;color:var(--ink);font-family:Inter,ui-sans-serif,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;background:#f6fbfb;overflow-x:hidden}',
  '.eco-section{color:var(--ink);font-family:Inter,ui-sans-serif,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}',
  'global body rule'
);
ecosystemCss=replaceOnce(ecosystemCss,'button,a{font:inherit}','.eco-section button,.eco-section a{font:inherit}','global button/link font rule');
ecosystemCss=ecosystemCss.replace(/(^|})\.eyebrow(?=[:{])/gm,'$1.eco-section .eyebrow');
ecosystemCss=ecosystemCss.replace(/(^|})h1(?=\{)/gm,'$1.eco-section h1');
ecosystemCss=replaceOnce(
  ecosystemCss,
  '@media (prefers-reduced-motion:reduce){*,*:before,*:after{animation:none!important;scroll-behavior:auto!important;transition-duration:.01ms!important}.eco-svg{transform:none!important}}',
  '@media (prefers-reduced-motion:reduce){.eco-section,.eco-section *,.eco-section *:before,.eco-section *:after{animation:none!important;scroll-behavior:auto!important;transition-duration:.01ms!important}.eco-svg{transform:none!important}}',
  'global reduced-motion reset'
);

for(const forbidden of [/(^|})\s*:root\s*\{/m,/(^|})\s*html\s*\{/m,/(^|})\s*body\s*\{/m,/(^|})\s*h1\s*\{/m,/(^|})\s*\.eyebrow(?:\s|:|\{)/m]){
  if(forbidden.test(ecosystemCss))throw new Error(`Digital PNG stylesheet still contains an unscoped global selector: ${forbidden}`);
}

ecosystemCss=`/*\n * Design 42 Digital PNG V2 stylesheet.\n * Isolated from the old ecosystem prototype so it cannot leak global styles\n * or inherit superseded .eco-* rules from the core stylesheet.\n */\n\n${ecosystemCss}\n`;
prototype=prototype.slice(0,styleMatch.index)+prototype.slice(styleMatch.index+styleMatch[0].length);
if(/<style(?:\s|>)/i.test(prototype))throw new Error('Digital PNG prototype still contains inline CSS after extraction.');

let core=read(paths.core);
const oldStart='/* Design 42: light interactive Digital PNG ecosystem. */';
const nextOwner='/* Design 42: static province laser network v6 */';
const start=core.indexOf(oldStart);
const end=core.indexOf(nextOwner);
if(start<0||end<0||end<=start)throw new Error('Could not locate obsolete Digital PNG CSS boundaries in core.');
const removedCore=core.slice(start,end);
for(const marker of [
  oldStart,
  'Design 42 ecosystem iteration 2: live routes + story overlays.',
  'Design 42 ecosystem iteration 3: calm topology.'
]) if(!removedCore.includes(marker))throw new Error(`Expected obsolete ecosystem marker missing from removal range: ${marker}`);
core=core.slice(0,start)+core.slice(end);

let loader=read(paths.loader);
loader=replaceOnce(
  loader,
  'const [baseHtml,coreCss,ecosystemHtml,componentCss,themeCss,chatCss]=await Promise.all([',
  'const [baseHtml,coreCss,ecosystemHtml,ecosystemCss,componentCss,themeCss,chatCss]=await Promise.all([',
  'loader dependency tuple'
);
loader=replaceOnce(
  loader,
  "      fetchText(source('design42-ecosystem-v2.html')).catch(error=>{console.warn('Digital PNG enhancement could not be loaded.',error);return ''}),\n      fetchText(source('assets/design42/design42-components.css'))",
  "      fetchText(source('design42-ecosystem-v2.html')).catch(error=>{console.warn('Digital PNG enhancement markup could not be loaded.',error);return ''}),\n      fetchText(source('assets/design42/design42-ecosystem.css')).catch(error=>{console.warn('Digital PNG enhancement styles could not be loaded.',error);return ''}),\n      fetchText(source('assets/design42/design42-components.css'))",
  'loader ecosystem fetch sequence'
);
loader=replaceOnce(loader,'    if(ecosystemHtml){','    if(ecosystemHtml&&ecosystemCss){','ecosystem availability guard');
loader=replaceOnce(
  loader,
  "        const prototypeStyle=prototype.querySelector('style');\n        if(prototypeStyle)addStyle(page,prototypeStyle.textContent,'data-design42-ecosystem-v2');",
  "        addStyle(page,ecosystemCss,'data-design42-ecosystem-v2');",
  'prototype inline-style injection'
);

let audit=read(paths.audit);
audit=replaceOnce(
  audit,
  "  'assets/design42/design42-core.css',\n  'assets/design42/design42-components.css',",
  "  'assets/design42/design42-core.css',\n  'assets/design42/design42-ecosystem.css',\n  'assets/design42/design42-components.css',",
  'audit CSS owner list'
);

const summary={
  extractedEcosystemBytes:Buffer.byteLength(ecosystemCss),
  removedCoreBytes:Buffer.byteLength(removedCore),
  coreBytesAfter:Buffer.byteLength(core),
  prototypeBytesAfter:Buffer.byteLength(prototype),
  scopedGlobalPrototypeRules:true
};

if(!apply){console.log(JSON.stringify(summary,null,2));process.exit(0)}
fs.writeFileSync(paths.core,core);
fs.writeFileSync(paths.ecosystem,ecosystemCss);
fs.writeFileSync(paths.prototype,prototype);
fs.writeFileSync(paths.loader,loader);
fs.writeFileSync(paths.audit,audit);
console.log(JSON.stringify(summary,null,2));
