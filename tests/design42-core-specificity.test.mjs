import fs from 'node:fs';
import assert from 'node:assert/strict';

const core = fs.readFileSync(new URL('../assets/design42/design42-core.css', import.meta.url), 'utf8');

const section = (startMarker, endMarker) => {
  const start = core.indexOf(startMarker);
  const end = core.indexOf(endMarker, start + startMarker.length);
  assert.ok(start >= 0, `Missing Design 42 core section marker: ${startMarker}`);
  assert.ok(end > start, `Missing Design 42 core end marker: ${endMarker}`);
  return core.slice(start, end);
};

const starlink = section(
  '/* Design 42: Starlink hardware refresh only. Banner composition and copy intentionally untouched. */',
  '/* Design 42: static province laser network v6 */'
);

assert.equal(
  (starlink.match(/!important/g) || []).length,
  0,
  'Starlink hardware refresh must rely on source order and scoped selectors, not !important.'
);

for (const selector of ['.satellite{', '.dish-rig{', '.starlink-satellite-svg{']) {
  assert.ok(starlink.includes(selector), `Starlink refresh lost required selector ${selector}`);
}

const newsroom = section(
  '/* Design 42: six-item live newsroom + vertically centred support copy */',
  '/* Design 42: eight-action kinetic launchpad */'
);

assert.equal(
  (newsroom.match(/!important/g) || []).length,
  0,
  'Live newsroom/support alignment must use the Core cascade, not !important.'
);

for (const selector of ['.live-news-stream{', '.live-feed-card{', '.updates-live .news-feature{']) {
  assert.ok(newsroom.includes(selector), `Newsroom cleanup lost required selector ${selector}`);
}

console.log('Design 42 core specificity guardrails passed.');
