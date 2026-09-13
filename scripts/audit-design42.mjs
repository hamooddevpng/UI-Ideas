import fs from 'node:fs';
import path from 'node:path';

const root = process.cwd();
const read = file => fs.readFileSync(path.join(root, file), 'utf8');
const base = read('42-base.html');
const loader = read('42.html');

const lineAt = (text, index) => text.slice(0, index).split('\n').length;
const firstDesignComment = text => {
  const m = text.match(/\/\*\s*(Design 42:[^*\n]+)|\/\/\s*(Design 42:[^\n]+)/i);
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

const styleBlocks = [...base.matchAll(/<style(?:\s[^>]*)?>([\s\S]*?)<\/style>/gi)].map((m, index) => {
  const css = m[1];
  const marker = firstDesignComment(css);
  const selectors = selectorsFromCss(css);
  return {
    index,
    startLine: lineAt(base, m.index),
    marker,
    bytes: Buffer.byteLength(css),
    importantCount: (css.match(/!important/g) || []).length,
    selectorCount: selectors.length,
    selectors,
    tags: ['palette','laser','chat','support','business','quick','hero','news'].filter(k => `${marker || ''}\n${css}`.toLowerCase().includes(k))
  };
});

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
for (const block of styleBlocks) {
  for (const selector of new Set(block.selectors)) {
    const arr = selectorOwners.get(selector) || [];
    arr.push(block.index);
    selectorOwners.set(selector, arr);
  }
}
const duplicates = [...selectorOwners.entries()]
  .filter(([, owners]) => owners.length > 1)
  .map(([selector, owners]) => ({selector, owners, count: owners.length}))
  .sort((a,b) => b.count - a.count || a.selector.localeCompare(b.selector));

const paletteBlocks = styleBlocks.filter(b => b.tags.includes('palette') || /palette/i.test(b.marker || ''));
const laserStyleBlocks = styleBlocks.filter(b => b.tags.includes('laser'));
const laserScriptBlocks = scriptBlocks.filter(b => b.tags.includes('laser'));
const loaderInlineStyleTemplates = (loader.match(/\.textContent\s*=\s*`[\s\S]*?`/g) || []).length;

const report = {
  generatedAt: new Date().toISOString(),
  files: {
    '42-base.html': {bytes: Buffer.byteLength(base), lines: base.split('\n').length},
    '42.html': {bytes: Buffer.byteLength(loader), lines: loader.split('\n').length}
  },
  counts: {
    styleBlocks: styleBlocks.length,
    scriptBlocks: scriptBlocks.length,
    importantDeclarations: styleBlocks.reduce((n,b) => n + b.importantCount, 0),
    duplicateSelectors: duplicates.length,
    paletteBlocks: paletteBlocks.length,
    laserStyleBlocks: laserStyleBlocks.length,
    laserScriptBlocks: laserScriptBlocks.length,
    loaderInlineStyleTemplates
  },
  styleBlocks: styleBlocks.map(({selectors, ...rest}) => rest),
  scriptBlocks,
  paletteBlocks,
  laserStyleBlocks: laserStyleBlocks.map(({selectors, ...rest}) => rest),
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
md.push('', '## Palette-related style blocks', '');
if (!paletteBlocks.length) md.push('- None');
for (const b of paletteBlocks) md.push(`- Block ${b.index}, line ${b.startLine}: ${b.marker || '(no Design 42 marker)'} | ${b.importantCount} !important | ${b.bytes} bytes`);
md.push('', '## Laser-related style blocks', '');
for (const b of laserStyleBlocks) md.push(`- Style ${b.index}, line ${b.startLine}: ${b.marker || '(no Design 42 marker)'}`);
md.push('', '## Laser-related script blocks', '');
for (const b of laserScriptBlocks) md.push(`- Script ${b.index}, line ${b.startLine}: ${b.marker || '(no Design 42 marker)'}`);
md.push('', '## Highest-overlap selectors', '');
for (const d of duplicates.slice(0, 40)) md.push(`- \`${d.selector}\`: blocks ${d.owners.join(', ')}`);
md.push('');
fs.writeFileSync(path.join(root, 'qa/design42/refactor-audit.md'), md.join('\n'));

console.log(JSON.stringify(report.counts, null, 2));
