import fs from 'node:fs';
import assert from 'node:assert/strict';

const html = fs.readFileSync(new URL('../42.html', import.meta.url), 'utf8');

assert.match(html, /data-design42-chat-popup-v1/, 'Design 42 should inject the chatbot popup override.');
assert.match(html, /body\.telikom-ai-open \.site-viewport\{width:100%!important\}/, 'Opening chat must not shrink the website.');
assert.match(html, /body\.telikom-ai-open \.site-header\{right:0!important\}/, 'Opening chat must not push the fixed header.');
assert.match(html, /\.telikom-ai-panel\{[^}]*width:min\(380px,calc\(100vw - 32px\)\)!important;[^}]*height:min\(540px,calc\(100dvh - 126px\)\)!important;/s, 'Chat should be a compact floating popup, not a full-height drawer.');
assert.match(html, /body\.telikom-ai-open \.telikom-ai-panel\{[^}]*opacity:1!important;[^}]*visibility:visible!important;/s, 'Popup should become visible when the existing open state is active.');

console.log('Design 42 chatbot popup structure verified.');
