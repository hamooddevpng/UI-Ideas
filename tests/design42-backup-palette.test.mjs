import fs from 'node:fs';
import assert from 'node:assert/strict';

const html = fs.readFileSync(new URL('../42.html', import.meta.url), 'utf8');

assert.match(html, /data-design42-backup-palette-v2/, 'The backup palette must be injected into the rendered Design 42 document.');
assert.match(html, /page\.head\.appendChild\(backupPaletteStyle\)/, 'The backup palette must be appended to the loaded page head before document.write().');
assert.match(html, /--deep-bg:#061925/, 'The restored palette should use the original deep navy from the backup.');
assert.match(html, /\.site-header\.scrolled\{background:rgba\(6,25,37,\.9\)!important/, 'Scrolled navigation should use the backup navy treatment.');
assert.match(html, /linear-gradient\(115deg,#061925 0 52%,#0a2e42 100%\)!important/, 'The main hero should restore the backup navy gradient.');
assert.match(html, /\.service-stage\{background:#061925!important/, 'The service feature stage should use the backup navy.');
assert.match(html, /\.support-orbit \.support-stage\{background:#061925!important/, 'The support stage should use the backup navy.');
assert.match(html, /footer\{background:#061925!important/, 'The footer should use the backup navy.');
assert.doesNotMatch(html, /<\/script>\s*<style>\s*\/\* Design 42: restored backup palette \*\//, 'Do not place the palette outside the dynamically rendered page.');
assert.match(html, /data-design42-chat-popup-v1/, 'The popup chatbot implementation must remain intact.');

console.log('Design 42 rendered backup palette structure verified.');
