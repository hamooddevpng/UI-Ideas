import fs from 'node:fs';
import assert from 'node:assert/strict';

const read = path => fs.readFileSync(new URL(`../${path}`, import.meta.url), 'utf8');
const exists = path => fs.existsSync(new URL(`../${path}`, import.meta.url));

const loader = read('42.html');
const base = read('42-base.html');
const core = read('assets/design42/design42-core.css');
const theme = read('assets/design42/design42-theme.css');

// Phase 1: loader and popup ownership.
assert.ok(exists('assets/design42/design42-chat.css'), 'Design 42 popup presentation must live in an external chat stylesheet.');
assert.doesNotMatch(
  loader,
  /raw\.githubusercontent\.com\/hamooddevpng\/UI-Ideas\/main\/42-base\.html/,
  '42.html must not hard-code main for 42-base.html; branch previews must load sibling files from the same ref.'
);
assert.doesNotMatch(
  loader,
  /chatbotPopupStyle\.textContent\s*=|conventional floating support-chat popup[\s\S]*`/,
  '42.html must not carry the chatbot CSS as a large inline template literal.'
);
assert.match(loader, /resolveSourceRoot/, '42.html must have one source-root resolver for local and htmlpreview branch/commit previews.');
assert.match(loader, /design42-chat\.css/, '42.html must load the external chatbot stylesheet.');

// Phase 2: all page CSS has explicit external ownership.
for (const file of [
  'assets/design42/design42-core.css',
  'assets/design42/design42-ecosystem.css',
  'assets/design42/design42-components.css',
  'assets/design42/design42-theme.css'
]) assert.ok(exists(file), `Missing Design 42 stylesheet: ${file}`);

assert.match(loader, /design42-core\.css/, '42.html must load the core stylesheet.');
assert.match(loader, /design42-ecosystem\.css/, '42.html must load the Digital PNG V2 stylesheet.');
assert.match(loader, /design42-components\.css/, '42.html must load the component stylesheet.');
assert.match(loader, /design42-theme\.css/, '42.html must load the canonical external theme stylesheet.');

const cascadeMarkers=[
  'data-design42-core',
  'data-design42-ecosystem-v2',
  'data-design42-components',
  'data-design42-theme',
  'data-design42-chat-popup'
];
let previousIndex=-1;
for(const marker of cascadeMarkers){
  const index=loader.indexOf(marker);
  assert.ok(index>previousIndex, `Design 42 stylesheet ownership order is wrong around ${marker}.`);
  previousIndex=index;
}

assert.doesNotMatch(base, /<style(?:\s|>)/i, '42-base.html must not contain inline style blocks after the CSS ownership refactor.');
assert.ok(!base.includes('Design 42: targeted lighter dark sections v1'), 'Legacy lighter-dark section patch must not remain in 42-base.html.');

// The active Digital PNG V2 experience owns its CSS. Core must not carry the
// three older ecosystem generations that shared selectors with it.
for(const marker of [
  'Design 42: light interactive Digital PNG ecosystem.',
  'Design 42 ecosystem iteration 2: live routes + story overlays.',
  'Design 42 ecosystem iteration 3: calm topology.'
]) assert.ok(!core.includes(marker),`Core still contains obsolete Digital PNG CSS: ${marker}`);

const ecosystemPrototype=read('design42-ecosystem-v2.html');
assert.doesNotMatch(ecosystemPrototype,/<style(?:\s|>)/i,'Digital PNG V2 prototype must not carry inline CSS.');
const ecosystemCss=read('assets/design42/design42-ecosystem.css');
assert.doesNotMatch(ecosystemCss,/(^|\})\s*:root\s*\{/m,'Digital PNG V2 must not redefine global :root tokens.');
assert.doesNotMatch(ecosystemCss,/(^|\})\s*html\s*\{/m,'Digital PNG V2 must not style the global html element.');
assert.doesNotMatch(ecosystemCss,/(^|\})\s*body\s*\{/m,'Digital PNG V2 must not style the global body element.');
assert.doesNotMatch(ecosystemCss,/(^|\})\s*h1\s*\{/m,'Digital PNG V2 heading styles must be scoped to its section.');
assert.doesNotMatch(ecosystemCss,/(^|\})\s*\.eyebrow(?:\s|:|\{)/m,'Digital PNG V2 eyebrow styles must be scoped to its section.');

const obsoletePaletteMarkers = [
  'brighter Telikom palette',
  'daylight Telikom palette',
  'daylight palette polish',
  'balanced daylight palette'
];
for (const marker of obsoletePaletteMarkers) {
  assert.ok(!base.toLowerCase().includes(marker.toLowerCase()), `42-base.html still contains obsolete palette pass: ${marker}`);
}

const paletteMentions = [...base.matchAll(/Design 42:[^\n]*palette[^\n]*/gi)].map(m => m[0]);
assert.equal(paletteMentions.length, 0, `42-base.html should not own historical palette passes; found: ${paletteMentions.join(' | ')}`);

// Phase 2b: one canonical theme sourced from the approved untouched backup.
assert.match(theme, /backup\/42-2026-09-10-1552-ist/, 'Canonical Design 42 theme must document the approved backup color source.');
assert.doesNotMatch(theme, /Canonical theme migration layer/i, 'Historical theme migration layers must be collapsed into one theme.');
for(const marker of obsoletePaletteMarkers){
  assert.ok(!theme.toLowerCase().includes(marker.toLowerCase()), `Canonical theme still contains obsolete palette pass: ${marker}`);
}
assert.doesNotMatch(theme, /!mportant/i, 'Canonical theme contains a malformed !important declaration.');
assert.equal((theme.match(/:root\s*\{/g)||[]).length,1,'Canonical Design 42 theme must have exactly one :root token block.');
for(const token of ['--blue:#0875c9','--cyan:#1ca0e8','--green:#20a957','--navy:#061925','--navy2:#0a2838','--ink:#102b3c','--ice:#f5fafc','--sky:#e9f6fc']){
  assert.ok(theme.replace(/\s/g,'').includes(token),`Canonical theme is missing approved backup token ${token}.`);
}
for(const legacyToken of ['--warm:','--warm-2:','--mist:','--mist-2:','--mint:']){
  assert.ok(!theme.includes(legacyToken),`Canonical theme still contains temporary daylight token ${legacyToken}`);
}

// Phase 3: one province-node foundation plus one active laser implementation.
assert.match(base, /Design 42: static province laser network v6/, 'The validated province node foundation must remain.');
assert.match(base, /Design 42: endpoint lasers v12/, 'The active endpoint laser implementation must remain.');
assert.match(read('assets/design42/design42-components.css'), /Design 42: laser tuning v13/, 'The active laser tuning layer must move to component CSS.');

const obsoleteLaserMarkers = [
  'Design 42: animated laser shots v7',
  'Design 42: robust province lasers v9',
  'Design 42: lasers only v10',
  'Design 42: simple province lasers v11'
];
for (const marker of obsoleteLaserMarkers) {
  assert.ok(!base.includes(marker), `42-base.html still contains superseded laser pass: ${marker}`);
}
assert.doesNotMatch(base, /provinceLaserShotsV7|provinceLaserCssV9|provinceLaserLayerV11/, 'Superseded laser runtime layers must be removed.');
assert.doesNotMatch(base, /v9-live|laser-source-v7|laser-hit-v7/, 'Superseded laser state classes must be removed.');
assert.doesNotMatch(base, /const buildEdges=|const routeD=/, 'The v6 foundation must no longer run hidden route/shot animation infrastructure.');
assert.match(base, /provinceLaserLayerV12/, 'The active v12 laser runtime layer must still be created.');
assert.match(read('assets/design42/design42-components.css'), /province-node-v6\.laser-live/, 'Active laser endpoint feedback must be owned by component CSS.');
assert.match(base, /classList\.add\('laser-live'\)/, 'The active endpoint runtime must drive canonical endpoint feedback.');

// Phase 4: the audit must measure the actual external CSS ownership, not only inline HTML.
const auditScript=read('scripts/audit-design42.mjs');
for(const file of ['design42-core.css','design42-ecosystem.css','design42-components.css','design42-theme.css','design42-chat.css']){
  assert.ok(auditScript.includes(file),`Design 42 audit does not include external stylesheet ${file}.`);
}
assert.match(auditScript,/cssFiles/, 'Design 42 audit must report per-file external CSS ownership.');

console.log('Design 42 CSS architecture guardrails passed.');
