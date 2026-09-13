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

console.log('Design 42 CSS architecture guardrails passed.');
