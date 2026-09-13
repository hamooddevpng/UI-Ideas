import fs from 'node:fs';
import assert from 'node:assert/strict';

const read = path => fs.readFileSync(new URL(`../${path}`, import.meta.url), 'utf8');

const components = read('assets/design42/design42-components.css');
const chat = read('assets/design42/design42-chat.css');

assert.doesNotMatch(
  components,
  /(?:\.telikom-ai-|--telikom-ai-|body\.telikom-ai-open)/,
  'Ask Telikom presentation must have one CSS owner; component CSS still contains chatbot rules.'
);

for (const selector of [
  '.telikom-ai-launcher',
  '.telikom-ai-panel',
  '.telikom-ai-head',
  '.telikom-ai-scroll',
  '.telikom-ai-compose'
]) {
  assert.ok(chat.includes(selector), `Canonical chat stylesheet is missing ${selector}.`);
}

assert.equal(
  (chat.match(/!important/g) || []).length,
  0,
  'Canonical chat CSS must not rely on !important once it is the sole owner.'
);

assert.match(
  chat,
  /body\.telikom-ai-open\s+\.site-viewport\s*\{[^}]*width\s*:\s*100%/,
  'Opening Ask Telikom must keep the page viewport at full width.'
);
assert.match(
  chat,
  /\.telikom-ai-panel\s*\{[^}]*position\s*:\s*fixed[^}]*inset\s*:\s*auto\s+24px\s+94px\s+auto/s,
  'Ask Telikom must remain a fixed bottom-right popup rather than a full-height drawer.'
);
assert.doesNotMatch(
  chat,
  /width\s*:\s*calc\(100%\s*-\s*var\(--telikom-ai-w\)\)/,
  'Chat stylesheet must not reintroduce the old page-shrinking side drawer.'
);

console.log('Design 42 chat ownership guardrails passed.');
