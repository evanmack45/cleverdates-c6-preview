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
  p.reqs = []; p.on('request', (r) => { if (!r.url().startsWith(new URL(base).origin) && !r.url().startsWith('data:') && !r.url().startsWith('blob:')) p.reqs.push(r.url()); });
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
    ok((await p.$$eval('img', (is) => is.every((i) => i.getAttribute('src').startsWith('art/')) && is.length === 4)) && p.errs.length === 0, `odd hash ${h}: nothing injected, no errors (${w})`);
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
  const CANON = 'https://closer.cleverdates.com/', pub = /^https?:\/\/(localhost|127\.0\.0\.1)[:/]/.test(base) ? CANON : base;
  ok(clip === `${pub}#t=${data.trios[4].e.join('.')}` && !/localhost|127\.0\.0\.1/.test(clip), `dare link copies this exact round, canonical URL on localhost: ${clip}`);
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
  ok(!(await nj.textContent('body')).includes('A preview, not yet published.') && !(await nj.textContent('body')).includes('not yet published'), 'no JS: footer does not say the page is a preview');
  ok((await nj.textContent('.foot')).includes('This domain is for sale.'), 'no JS: for-sale footer remains');
  await nj.context().close();
}
{
  const p = await page(390);
  await p.goto(base);
  const body = await p.textContent('body');
  const html = await p.content();
  ok(!body.includes('A preview, not yet published.') && !body.includes('not yet published') && !html.includes('A preview, not yet published.'), 'page footer does not say the page is a preview');
  ok((await p.textContent('.foot')).includes('This domain is for sale.'), 'for-sale footer remains');
  await p.context().close();
}
// r3 art: share-card ground drawn into the canvas; three real trios, right and wrong, plus an odd one (longest event names)
{
  const longest = data.trios.map((t) => [t, Math.max(...t.e.map((id) => data.events[id].name.length))]).sort((a, c) => c[1] - a[1])[0][0];
  const cases = [[data.trios[0], true, false], [data.trios[12], false, false], [data.trios[18], true, false], [longest, false, true]];
  for (const [t, win, odd] of cases) {
    const p = await page(1280, { acceptDownloads: true });
    await p.addInitScript(() => { window.__t = []; window.__img = []; const f = CanvasRenderingContext2D.prototype.fillText, di = CanvasRenderingContext2D.prototype.drawImage; CanvasRenderingContext2D.prototype.fillText = function (x, ...r) { window.__t.push(String(x)); return f.call(this, x, ...r); }; CanvasRenderingContext2D.prototype.drawImage = function (im, ...r) { window.__img.push(im && im.src ? im.src : 'canvas'); return di.call(this, im, ...r); }; });
    await p.goto(`${base}#t=${t.e.join('.')}`);
    const odds = t.e.find((id) => !t.answer.includes(id));
    await play(p, win ? t.answer : [odds, t.answer[0]]);
    const [dl] = await Promise.all([p.waitForEvent('download'), p.click('#card-btn')]);
    const buf = readFileSync(await dl.path());
    const txt = await p.evaluate(() => window.__t.join('\n')), im = await p.evaluate(() => window.__img.join('\n'));
    const tag = `r3 card trio ${t.n}${win ? ' right' : ' wrong'}${odd ? ' (odd: longest names)' : ''}`;
    ok(buf.slice(1, 4).toString() === 'PNG' && buf.readUInt32BE(16) === 1080 && buf.readUInt32BE(20) === 1350, `${tag}: PNG is 1080x1350`);
    ok(/card-r3\.webp/.test(im) && !/card-1080/.test(im), `${tag}: the hieroglyph-free ground is drawn into the canvas`);
    const seal = await p.$eval('#seal', (e) => ({ src: e.getAttribute('src'), hidden: e.hidden, ok: e.complete && e.naturalWidth > 0 }));
    ok(!seal.hidden && seal.ok && (win ? /seal-right-/.test(seal.src) : /seal-not-quite-/.test(seal.src)), `${tag}: the ${win ? 'right' : 'not-quite'} seal sits beside the verdict`);
    ok((win ? /seal-right-512\.webp/ : /seal-not-quite-512\.webp/).test(im), `${tag}: the matching seal is drawn into the canvas next to the result line`);
    ok(!txt.includes(t.hook) && t.e.every((id) => txt.includes(data.events[id].name.split(' ')[0])) && txt.includes(win ? 'I got this one right.' : 'This one got me.'), `${tag}: type is the three events and the result line; the hook (the answer) stays off the card`);
    const host = (/^https?:\/\/(localhost|127\.0\.0\.1)[:/]/.test(base) ? 'https://closer.cleverdates.com/' : base).replace(/^https?:\/\//, '').replace(/\/?$/, '');
    ok(txt.includes('Closer in time, a game from Clever Dates.') && txt.includes(host) && !/localhost|127\.0\.0\.1/.test(txt), `${tag}: footer names the canonical host (${host})`);
    ok(!/A preview, not yet published|not yet published/.test(txt), `${tag}: share PNG footer does not say the page is a preview`);
    const lay = await p.evaluate(async () => window.__c6cardLayout());
    const footer = (lay.texts || []).filter((t) => /Closer in time, a game from|cleverdates\.com/.test(t.s));
    const gap = Math.min(...footer.map((t) => t.top)) - Math.max(...lay.boxes.map((b) => b.y + b.h));
    ok(lay.boxes.length === 3 && footer.length >= 2 && gap >= 16, `${tag}: footer sits ${gap}px below the last option box`);
    ok(footer.every((t) => t.bottom <= 1350 - 8), `${tag}: footer stays inside the card (bottom ${Math.max(...footer.map((t) => t.bottom))})`);
    ok(p.errs.length === 0 && p.reqs.length === 0, `${tag}: no errors, no third-party requests ${p.errs.join(';')}`);
    await dl.saveAs(`r3/card-trio${t.n}-${win ? 'right' : 'wrong'}.png`);
    await p.context().close();
  }
  const p = await page(390); await p.goto(base);
  ok(await p.$$eval('img', (is) => is.length === 4 && is.every((i) => /^(\.\.\/)?art\/(hero|ruler|triptych|seal-right|seal-not-quite)-/.test(i.getAttribute('src')))), 'r4: on-page art is hero, ruler, triptych and the result seal');
  await p.context().close();
}

// footer must clear the last option box: teaser (the live bug), a short-name trio, and the longest names
{
  const shortest = data.trios.map((t) => [t, Math.max(...t.e.map((id) => data.events[id].name.length))]).sort((a, c) => a[1] - c[1])[0][0];
  const longest = data.trios.map((t) => [t, Math.max(...t.e.map((id) => data.events[id].name.length))]).sort((a, c) => c[1] - a[1])[0][0];
  const cases = [[data.trios[0], 'teaser (no play)', null], [data.trios[0], 'after a right answer', true], [shortest, 'short names', true], [longest, 'odd: longest names', false]];
  for (const [t, label, win] of cases) {
    const p = await page(390);
    await p.goto(`${base}#t=${t.e.join('.')}`);
    if (win === true) await play(p, t.answer);
    else if (win === false) await play(p, [t.e.find((id) => !t.answer.includes(id)), t.answer[0]]);
    const lay = await p.evaluate(async () => window.__c6cardLayout());
    const footer = (lay.texts || []).filter((t) => /Closer in time, a game from|cleverdates\.com/.test(t.s));
    const gap = Math.min(...footer.map((t) => t.top)) - Math.max(...lay.boxes.map((b) => b.y + b.h));
    ok(lay.boxes.length === 3 && footer.length >= 2 && gap >= 16, `footer gap, ${label} (trio ${t.n}): ${gap}px`);
    ok(footer.every((t) => t.bottom <= 1350 - 8), `footer in bounds, ${label} (trio ${t.n})`);
    await p.context().close();
  }
}

// Hero rule (bar v1.2, Shears 11/25): at 390x844 the hero art's visible box is at least 0.40 of the fold, the first control is in the first screen, and the art is not blown up past 1.25x
{
  const p = await page(390);
  await p.goto(base, { waitUntil: 'networkidle' });
  const h = await p.evaluate(() => { const VW = innerWidth, VH = innerHeight; const el = document.querySelector('figure.hero-art'), im = el.querySelector('img'); const r = el.getBoundingClientRect(); const w = Math.max(0, Math.min(VW, r.right) - Math.max(0, r.left)), hh = Math.max(0, Math.min(VH, r.bottom) - Math.max(0, r.top)); const ir = im.getBoundingClientRect(); const sc = Math.max(ir.width / im.naturalWidth, ir.height / im.naturalHeight); const first = document.querySelector('.ev').getBoundingClientRect(), lock = document.querySelector('#lock').getBoundingClientRect(); return { ratio: w * hh / (VW * VH), up: (im.naturalWidth * sc * devicePixelRatio) / +(/-(\d+)\.webp/.exec(im.currentSrc) || [0, 1])[1], natW: +(/-(\d+)\.webp/.exec(im.currentSrc) || [0, 0])[1], firstBottom: first.bottom, lockBottom: lock.bottom, VH, words: document.body.innerText.slice(0, 0) }; });
  ok(h.ratio >= 0.4, `hero: figure.hero-art fills ${h.ratio.toFixed(3)} of the 390x844 first screen (need 0.40)`);
  ok(h.up <= 1.25, `hero: art is sharp, ${h.up.toFixed(2)}x upscale from a ${h.natW}px file at DPR 2`);
  ok(h.lockBottom <= h.VH && h.firstBottom <= h.VH, `hero: the cards and the Pick-two button stay in the first screen (button bottom ${Math.round(h.lockBottom)} of ${h.VH})`);
  await p.context().close();
}
console.log(fails ? `${fails} FAILED` : 'ALL PASS');
await b.close();
process.exit(fails ? 1 : 0);
