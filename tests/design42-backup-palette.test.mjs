import fs from 'node:fs';
import assert from 'node:assert/strict';

const html = fs.readFileSync(new URL('../42.html', import.meta.url), 'utf8');

assert.match(html, /Design 42: restored backup palette/, 'Design 42 should declare the restored backup palette.');
assert.match(html, /--deep-bg:#061925/, 'The restored palette should use the original deep navy from the backup.');
assert.match(html, /background:#f5fafc!important;color:#102b3c!important/, 'The page canvas should use the backup light surface and ink colors.');
assert.doesNotMatch(html, /balanced daylight palette v3/, 'The later daylight palette override should be removed on this branch.');
assert.match(html, /data-design42-chat-popup-v1/, 'The popup chatbot implementation must remain intact.');

console.log('Design 42 backup palette structure verified.');
