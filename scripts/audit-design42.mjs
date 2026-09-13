import fs from 'node:fs';
import path from 'node:path';

const root = process.cwd();
const read = file => fs.readFileSync(path.join(root, file), 'utf8');
const base = read('42-base.html');
const loader = read('42.html');

const cssFiles = [
  'assets/design42/design42-core.css',
  'assets/design42/design42-components.css',
  'assets/design42/design42-theme.css',
  'assets/design42/design42-chat.css'
];

const lineAt = (text, index) => text.slice(0, index).split('\n').length;
const firstDesignComment = text => {
  const m = text.match(/\/\*\s*(Design 42[^*\n]*)|\/\/\s*(Design 42[^\n]*)/i);
  return (m?.[1] || m?.[2] || '').trim() || null;
};
const selectorsFromCss = css => {
  const withoutComments = css.replace(/\/\*[\s\S]*?\*\//g, '');
  const selectors = [];
  for (const m of withoutComments.matchAll(/(^|})\s*([^@{}][^{}]*)\{/g)) {
    const raw = m[2].trim();
    if (!raw || raw.includes('from') || raw.includes('to')) continue;
    raw.split(',').map(s => s.trim()).filter(Boolean).forEach(s => selectors.push(s));
  }
  return selectors;
};
const describeCss = (owner, css, kind='external') => {
  const marker = firstDesignComment(css);
  const selectors = selectorsFromCss(css);
  const haystack = `${owner}\n${marker || ''}\n${css}`.toLowerCase();
  return {
    owner,
    kind,
    marker,
    bytes: Buffer.byteLength(css),
    lines: css.split('\n').length,
    importantCount: (css.match(/!important/g) || []).length,
    selectorCount: selectors.length,
    selectors,
    tags: ['palette','theme','laser','chat','support','business','quick','hero','news','ecosystem']
      .filter(tag => haystack.includes(tag))
  };
};

const cssSources = cssFiles.map(file => describeCss(file, read(file)));

const ecosystemHtml = read('design42-ecosystem-v2.html');
const ecosystemStyles = [...ecosystemHtml.matchAll(/<style(?:\s[^>]*)?>([\s\S]*?)<\/style>/gi)];
for (const [index, match] of ecosystemStyles.entries()) {
  cssSources.splice(1 + index, 0, describeCss(`design42-ecosystem-v2.html#style-${index}`, match[1], 'prototype-inline'));
}

const baseInlineStyles = [...base.matchAll(/<style(?:\s[^>]*)?>([\s\S]*?)<\/style>/gi)].map((match, index) => ({
  ...describeCss(`42-base.html#style-${index}`, match[1], 'base-inline'),
  startLine: lineAt(base, match.index)
}));
cssSources.push(...baseInlineStyles);

const scriptBlocks = [...base.matchAll(/<script(?:\s[^>]*)?>([\s\S]*?)<\/script>/gi)].map((m, index) => {
  const js = m[1];
  return {
    index,
    startLine: lineAt(base, m.index),
    marker: firstDesignComment(js),
    bytes: Buffer.byteLength(js),
    tags: ['laser','chat','support','business','quick','hero','news'].filter(k => js.toLowerCase().includes(k))
  };
});

const selectorOwners = new Map();
for (const source of cssSources) {
  for (const selector of new Set(source.selectors)) {
    const owners = selectorOwners.get(selector) || [];
    owners.push(source.owner);
    selectorOwners.set(selector, owners);
  }
}
const duplicates = [...selectorOwners.entries()]
  .filter(([, owners]) => owners.length > 1)
  .map(([selector, owners]) => ({selector, owners, count: owners.length}))
  .sort((a,b) => b.count - a.count || a.selector.localeCompare(b.selector));

const paletteSources = cssSources.filter(source => source.tags.includes('palette'));
const themeSources = cssSources.filter(source => source.tags.includes('theme'));
const laserStyleSources = cssSources.filter(source => source.tags.includes('laser'));
const laserScriptBlocks = scriptBlocks.filter(block => block.tags.includes('laser'));
const loaderInlineStyleTemplates = (loader.match(/\.textContent\s*=\s*`[\s\S]*?`/g) || []).length;
const loaderShellStyleBlocks = [...loader.matchAll(/<style(?:\s[^>]*)?>[\s\S]*?<\/style>/gi)].length;

const report = {
  generatedAt: new Date().toISOString(),
  files: {
    '42-base.html': {bytes: Buffer.byteLength(base), lines: base.split('\n').length},
    '42.html': {bytes: Buffer.byteLength(loader), lines: loader.split('\n').length},
    ...Object.fromEntries(cssFiles.map(file => {
      const text = read(file);
      return [file, {bytes: Buffer.byteLength(text), lines: text.split('\n').length}];
    })),
    'design42-ecosystem-v2.html': {bytes: Buffer.byteLength(ecosystemHtml), lines: ecosystemHtml.split('\n').length}
  },
  counts: {
    cssFiles: cssSources.length,
    externalCssFiles: cssFiles.length,
    ecosystemStyleBlocks: ecosystemStyles.length,
    inlineStyleBlocks: baseInlineStyles.length,
    scriptBlocks: scriptBlocks.length,
    importantDeclarations: cssSources.reduce((sum, source) => sum + source.importantCount, 0),
    duplicateSelectorsAcrossOwners: duplicates.length,
    paletteSources: paletteSources.length,
    themeSources: themeSources.length,
    laserStyleSources: laserStyleSources.length,
    laserScriptBlocks: laserScriptBlocks.length,
    loaderInlineStyleTemplates,
    loaderShellStyleBlocks
  },
  cssFiles: cssSources.map(({selectors, ...source}) => source),
  scriptBlocks,
  paletteSources: paletteSources.map(({selectors, ...source}) => source),
  themeSources: themeSources.map(({selectors, ...source}) => source),
  laserStyleSources: laserStyleSources.map(({selectors, ...source}) => source),
  laserScriptBlocks,
  topDuplicateSelectors: duplicates.slice(0, 100)
};

fs.mkdirSync(path.join(root, 'qa/design42'), {recursive:true});
fs.writeFileSync(path.join(root, 'qa/design42/refactor-audit.json'), JSON.stringify(report, null, 2));

const md = [];
md.push('# Design 42 CSS / JS Ownership Audit', '');
md.push(`Generated: ${report.generatedAt}`, '');
md.push('## Summary', '');
for (const [key, value] of Object.entries(report.counts)) md.push(`- **${key}:** ${value}`);

md.push('', '## CSS ownership', '');
for (const source of report.cssFiles) {
  md.push(`- \`${source.owner}\` (${source.kind}): ${source.selectorCount} selectors, ${source.importantCount} !important, ${source.bytes} bytes${source.marker ? ` | ${source.marker}` : ''}`);
}

md.push('', '## Palette / theme ownership', '');
if (!paletteSources.length) md.push('- No historical palette source remains.');
for (const source of themeSources) md.push(`- Theme: \`${source.owner}\``);

md.push('', '## Laser ownership', '');
for (const source of laserStyleSources) md.push(`- CSS: \`${source.owner}\`${source.marker ? ` | ${source.marker}` : ''}`);
for (const block of laserScriptBlocks) md.push(`- Script ${block.index}, line ${block.startLine}: ${block.marker || '(no Design 42 marker)'}`);

md.push('', '## Highest cross-owner selector overlap', '');
if (!duplicates.length) md.push('- None');
for (const item of duplicates.slice(0, 40)) md.push(`- \`${item.selector}\`: ${item.owners.join(' ↔ ')}`);
md.push('');
fs.writeFileSync(path.join(root, 'qa/design42/refactor-audit.md'), md.join('\n'));

console.log(JSON.stringify(report.counts, null, 2));
