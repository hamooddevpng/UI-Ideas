import fs from 'node:fs';
import assert from 'node:assert/strict';

const html = fs.readFileSync(new URL('../42.html', import.meta.url), 'utf8');

assert.match(
  html,
  /const injectedBase=new URL\('\.\/',document\.baseURI\)\.href;/,
  'Design 42 must derive its source root from HTMLPreview\'s injected <base> URL.'
);

assert.match(
  html,
  /if\(\/\^https:\\\/\\\/raw\\\.githubusercontent\\\.com\\\/\/i\.test\(injectedBase\)\)return injectedBase;/,
  'Design 42 must prefer a raw.githubusercontent.com document.baseURI before location-based fallbacks.'
);

console.log('Design 42 HTMLPreview source-root contract verified.');
