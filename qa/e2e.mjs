// e2e for Closer in time. node e2e.mjs <base-url>
import { chromium } from 'playwright';
import { readFileSync } from 'node:fs';
const base = process.argv[2];
const data = JSON.parse(readFileSync(new URL('../trios.json', import.meta.url)));
const b = await chromium.launch({ channel: 'chrome' });
let fails = 0;
const ok = (c, m) => { console.log((c ? 'PASS  ' : 'FAIL  ') + m); if (!c) fails++; };
async function page(w, opts = {}) {
  const mobile = w < 600;
  const ctx = await b.newContext({ viewport: { width: w, height: mobile ? 844 : 800 }, isMobile: mobile, hasTouch: mobile, deviceScaleFactor: mobile ? 2 : 1, ...opts });
  const p = await ctx.newPage();
  p.errs = []; p.on('pageerror', (e) => p.errs.push(e.message)); p.on('console', (m) => m.type() === 'error' && p.errs.push(m.text()));
  p.reqs = []; p.on('request', (r) => { if (!r.url().startsWith(base) && !r.url().startsWith('data:') && !r.url().startsWith('blob:')) p.reqs.push(r.url()); });
  return p;
}
const shown = (p) => p.$$eval('.ev', (bs) => bs.map((x) => x.dataset.id));
async function play(p, ids) {
  for (const id of ids) await p.click(`.ev[data-id="${id}"]`);
  await p.click('#lock');
  await p.waitForSelector('#reveal:not([hidden])');
  return p.textContent('#verdict');
}
const overflow = (p) => p.evaluate(() => document.documentElement.scrollWidth > innerWidth + 1);

for (const w of [390, 1280]) {
  // three real trios, right and wrong
  for (const n of [1, 13, 19]) {
    const t = data.trios[n - 1], key = t.e.join('.');
    const p = await page(w);
    await p.goto(`${base}#t=${key}`);
    ok(!(await p.isHidden('#dare')), `#t=${key}: dare banner shows (${w})`);
    ok((await shown(p)).join('.') === key, `#t=${key}: cards in link order (${w})`);
    ok((await p.textContent('.ev-name')).length > 3 && await p.isHidden('.ev-when'), `dates hidden before answering (${w})`);
    ok((await play(p, t.answer)) === 'Right.', `trio ${n} right pair ${t.answer.join('+')} gives "Right." (${w})`);
    ok((await p.textContent('#hook')) === t.hook, `trio ${n} hook shows (${w})`);
    ok((await p.$$('.dot')).length === 3 && (await p.$$('.br.win')).length === 1, `trio ${n} timeline: 3 dots, 1 answer bracket (${w})`);
    const win = await p.textContent('.gaps li.win .g-pair');
    ok(t.answer.every((id) => win.includes(data.events[id].name)), `trio ${n} gap list marks the answer pair (${w})`);
    ok((await p.$$('#srcs a')).length === t.e.filter((id) => data.events[id].src).length, `trio ${n} lists a source link per dated event (${w})`);
    ok(!(await overflow(p)), `trio ${n} reveal has no horizontal overflow (${w})`);
    const odd = t.e.find((id) => !t.answer.includes(id));
    await p.goto(`${base}#t=${key}x`); await p.waitForTimeout(100);
    await p.goto(`${base}#t=${key}`); await p.waitForSelector(`.ev[data-id="${odd}"]`, { timeout: 5000 }).catch(() => {});
    ok((await shown(p)).join('.') === key, `bad link then good link loads the good round (${w}): ${(await shown(p)).join('.')}`);
    await p.reload(); await p.waitForSelector(`.ev[data-id="${odd}"]`, { timeout: 5000 }).catch(() => {});
    ok((await play(p, [odd, t.answer[0]])) === 'Not quite.', `trio ${n} wrong pair gives "Not quite." (${w})`);
    ok(await p.$eval(`.ev[data-id="${odd}"]`, (x) => x.classList.contains('is-miss')), `trio ${n} wrong pick is marked (${w})`);
    ok(p.errs.length === 0 && p.reqs.length === 0, `trio ${n}: no errors, no third-party requests (${w}) ${p.errs.join(';')} ${p.reqs.join(';')}`);
    await p.context().close();
  }
  // odd input
  for (const h of ['#t=garbled%%%', '#t=cleo.pyramid', '#t=%3Cimg%20src=x%20onerror=alert(1)%3E', '#t=cleo.cleo.cleo', '#t=cleo.pyramid.moon', '#t=CLEO.PYRAMID.IPHONE', '#zzz']) {
    const p = await page(w);
    await p.goto(base + h);
    ok(!(await p.isHidden('#note')) && (await p.textContent('#note')).includes('broken'), `odd hash ${h}: clear message (${w})`);
    ok((await shown(p)).length === 3 && await p.isHidden('#dare'), `odd hash ${h}: plays a fresh round, no dare banner (${w})`);
    ok(!(await p.evaluate(() => location.hash)), `odd hash ${h}: hash cleared (${w})`);
    ok((await p.$$eval('img', (is) => is.every((i) => i.getAttribute('src').startsWith('art/')) && is.length === 3)) && p.errs.length === 0, `odd hash ${h}: nothing injected, no errors (${w})`);
    await p.context().close();
  }
}
// every trio answers right at 390, no overflow
{
  const p = await page(390); let bad = [];
  for (const t of data.trios) {
    await p.goto(`${base}#t=${t.e.join('.')}`); await p.reload();
    const v = await play(p, t.answer);
    if (v !== 'Right.' || await overflow(p)) bad.push(t.n);
    const labs = await p.$$eval('.lab', (ls) => ls.map((l) => { const r = l.getBoundingClientRect(), q = l.closest('.tl').getBoundingClientRect(); return r.left >= q.left - 1 && r.right <= q.right + 1; }));
    if (labs.includes(false)) bad.push(`${t.n}:label`);
  }
  ok(bad.length === 0, `all ${data.trios.length} trios: right answer accepted, no overflow, labels inside the plot (390) ${bad.join(',')}`);
  await p.context().close();
}
// next round, dare link, card, reduced motion
{
  const p = await page(1280, { permissions: ['clipboard-read', 'clipboard-write'] });
  await p.goto(`${base}#t=${data.trios[4].e.join('.')}`);
  await play(p, data.trios[4].answer);
  await p.click('#dare-btn'); await p.waitForTimeout(200);
  const clip = await p.evaluate(() => navigator.clipboard.readText());
  ok(clip === `${base}#t=${data.trios[4].e.join('.')}`, `dare link copies this exact round: ${clip}`);
  const png = await p.evaluate(() => window.__c6card());
  const dims = await p.evaluate((u) => new Promise((r) => { const i = new Image(); i.onload = () => r([i.width, i.height]); i.src = u; }), png);
  ok(png.length > 30000 && dims[0] === 1080 && dims[1] === 1350, `share card PNG 1080x1350 (${Math.round(png.length / 1024)} KB)`);
  const [dl] = await Promise.all([p.waitForEvent('download'), p.click('#card-btn')]);
  ok(dl.suggestedFilename() === 'closer-in-time.png', 'Save card image downloads closer-in-time.png');
  await p.click('#next');
  ok(!(await p.evaluate(() => location.hash)) && await p.isHidden('#dare') && await p.isHidden('#reveal'), 'Next round clears the dare and the reveal');
  ok((await p.textContent('#round')).startsWith('Round 2 · 1 right'), `round counter: ${await p.textContent('#round')}`);
  await p.context().close();
  const r = await page(390, { reducedMotion: 'reduce' });
  await r.goto(`${base}#t=${data.trios[0].e.join('.')}`);
  await play(r, data.trios[0].answer);
  const anim = await r.evaluate(() => [getComputedStyle(document.getElementById('reveal')).animationName, getComputedStyle(document.querySelector('.dot')).animationName]);
  ok(anim.every((a) => a === 'none'), `reduced motion: no reveal or dot animation (${anim})`);
  await r.context().close();
  const nj = await page(390, { javaScriptEnabled: false });
  await nj.goto(base);
  ok(await nj.isHidden('.picks') && (await nj.$$('.sp li')).length === data.trios.length, 'no JS: game hidden, all answers with sources listed');
  await nj.context().close();
}
console.log(fails ? `${fails} FAILED` : 'ALL PASS');
await b.close();
process.exit(fails ? 1 : 0);
