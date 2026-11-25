import { chromium } from 'playwright';
import { writeFileSync } from 'node:fs';
const b = await chromium.launch({ channel: 'chrome' }); const p = await b.newPage();
await p.goto('http://localhost:8766/#t=' + process.argv[2]);
for (const id of process.argv[3].split(',')) await p.click(`.ev[data-id="${id}"]`);
await p.click('#lock'); await p.waitForTimeout(1200);
let h = await p.content(); h = h.replace('<head>', '<head><base href="http://localhost:8766/">').replace(/<script src="app.js" defer><\/script>/, '');
writeFileSync('/workspace/sites/cleverdates.com/c6/docs/reveal-snap.html', h); await b.close();
