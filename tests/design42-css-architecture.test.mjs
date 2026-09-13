import fs from 'node:fs';
import assert from 'node:assert/strict';

const read = path => fs.readFileSync(new URL(`../${path}`, import.meta.url), 'utf8');
const exists = path => fs.existsSync(new URL(`../${path}`, import.meta.url));

const loader = read('42.html');
const base = read('42-base.html');

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

// Phase 2: canonical theme ownership.
assert.ok(exists('assets/design42/design42-theme.css'), 'Design 42 must have one canonical external theme stylesheet.');
assert.match(loader, /design42-theme\.css/, '42.html must load the canonical external theme stylesheet.');

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

// Phase 3: one province-node foundation plus one active laser implementation.
assert.match(base, /Design 42: static province laser network v6/, 'The validated province node foundation must remain.');
assert.match(base, /Design 42: endpoint lasers v12/, 'The active endpoint laser implementation must remain.');
assert.match(base, /Design 42: laser tuning v13/, 'The active laser tuning layer must remain.');

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
assert.match(base, /province-node-v6\.laser-live/, 'Active laser endpoint feedback must be owned by the canonical laser presentation.');
assert.match(base, /classList\.add\('laser-live'\)/, 'The active endpoint runtime must drive canonical endpoint feedback.');

console.log('Design 42 CSS architecture guardrails passed.');
