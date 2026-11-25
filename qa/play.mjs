// Screens: fold, picked, reveal, for a given hash. node play.mjs <base> <outdir> <w> [hash]
import { chromium } from 'playwright';
const [base, out, w, hash = ''] = process.argv.slice(2);
const mobile = +w < 600;
const b = await chromium.launch({ channel: 'chrome' });
const p = await b.newPage({ viewport: { width: +w, height: mobile ? 844 : 900 }, isMobile: mobile, hasTouch: mobile, deviceScaleFactor: mobile ? 2 : 1 });
const errs = []; p.on('pageerror', (e) => errs.push(e.message)); p.on('console', (m) => m.type() === 'error' && errs.push(m.text()));
await p.goto(base + hash); await p.waitForTimeout(500);
await p.screenshot({ path: `${out}/fold-${w}.png` });
const evs = p.locator('.ev');
await evs.nth(0).click(); await evs.nth(2).click();
await p.screenshot({ path: `${out}/picked-${w}.png` });
await p.click('#lock'); await p.waitForTimeout(1500);
await p.screenshot({ path: `${out}/reveal-${w}.png` });
await p.screenshot({ path: `${out}/reveal-full-${w}.png`, fullPage: true });
const png = await p.evaluate(() => window.__c6card());
await (await import('node:fs')).promises.writeFile(`${out}/card-${w}.png`, Buffer.from(png.split(',')[1], 'base64'));
console.log('errors', errs);
await b.close();
