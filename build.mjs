// Builds docs/ from trios.json. No dependencies.
import { readFileSync, writeFileSync, mkdirSync, copyFileSync, readdirSync, rmSync, existsSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const here = dirname(fileURLToPath(import.meta.url));
const out = join(here, 'docs');
const data = JSON.parse(readFileSync(join(here, 'trios.json'), 'utf8'));
const SITE = 'https://closer.cleverdates.com/';
const AFTERNIC = 'https://www.afternic.com/domain/cleverdates.com';

// Boundary checks: the client trusts this shape.
if (data.trios.length < 40) throw new Error('need 40+ trios');
const keys = new Set();
for (const t of data.trios) {
  if (t.e.length !== 3 || t.answer.length !== 2) throw new Error(`bad trio ${t.n}`);
  for (const id of t.e) {
    const e = data.events[id];
    if (!e || !/^[a-z0-9_]+$/.test(id)) throw new Error(`bad event ${id}`);
    if (id !== 'today' && !/^https:\/\/en\.wikipedia\.org\/wiki\//.test(e.src)) throw new Error(`no source ${id}`);
  }
  if (!(t.margin > 0)) throw new Error(`ambiguous trio ${t.n}`);
  const k = t.e.join('.');
  if (keys.has(k)) throw new Error(`dupe ${k}`);
  keys.add(k);
}

const esc = (s) => String(s).replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
const first = data.trios[0];
const ev = (id) => data.events[id];
const spoilers = data.trios.map((t) => `<li><p class="sp-hook">${esc(t.hook)}</p><p class="sp-src">${t.e.map((id) => ev(id).src ? `<a href="${esc(ev(id).src)}" rel="noopener">${esc(ev(id).name)}: ${esc(ev(id).when)}</a>` : `${esc(ev(id).name)}: ${esc(ev(id).when)}`).join('<span aria-hidden="true"> · </span>')}</p></li>`).join('\n');

const html = `<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="canonical" href="${SITE}">
<meta property="og:url" content="${SITE}">
<title>Closer in time | Clever Dates</title>
<meta name="description" content="Three moments in history. Pick the two that happened closest together, then see all three to scale.">
<meta property="og:title" content="Bet you get this wrong: which two are closer in time?">
<meta property="og:description" content="Three moments. Pick the two closest together. Then see them to scale.">
<meta property="og:image" content="${SITE}og.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="A pyramid, an ancient amphora and a smartphone float in a row under a turquoise sky, joined by two gold measuring lines.">
<meta property="og:type" content="website">
<meta name="twitter:card" content="summary_large_image">
<link rel="preload" href="fonts/gloock.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="fonts/schibsted.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" as="image" href="art/hero-800.webp" imagesrcset="art/hero-800.webp 800w, art/hero-1400.webp 1400w" imagesizes="(min-width: 900px) 560px, 100vw" fetchpriority="high">
<link rel="stylesheet" href="style.css">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3E%3Crect width='16' height='16' rx='3' fill='%230f3b2c'/%3E%3Ccircle cx='4' cy='8' r='2' fill='%23f4eedf'/%3E%3Ccircle cx='10' cy='8' r='2' fill='%23ff7a59'/%3E%3Ccircle cx='13' cy='8' r='2' fill='%23ff7a59'/%3E%3C/svg%3E">
<script>document.documentElement.className='js'</script>
</head>
<body>
<header class="bar"><a class="mark" href="./">Clever Dates</a><span class="round" id="round" aria-live="polite"></span></header>
<main>
<section class="game" aria-labelledby="q">
 <p class="dare" id="dare" hidden>Someone sent you this one. They bet you get it wrong.</p>
 <div class="top">
  <div class="top-txt">
   <h1 id="q">Which two are closer in time?</h1>
   <p class="dek">Pick the two moments nearest each other.</p>
  </div>
  <figure class="hero-art"><img src="art/hero-800.webp" srcset="art/hero-800.webp 800w, art/hero-1400.webp 1400w" sizes="(min-width: 900px) 560px, 180vw" width="1400" height="782" fetchpriority="high" alt="Gouache poster: a smartphone and a gold coin half buried in desert sand beside the Great Pyramid, with a small stepped temple far off."></figure>
 </div>
 <p class="note" id="note" role="status" hidden></p>
 <div class="picks" id="picks" role="group" aria-label="Three moments. Pick two.">
  ${first.e.map((id, i) => `<button type="button" class="ev" data-id="${id}" aria-pressed="false"><span class="ev-n">${'ABC'[i]}</span><span class="ev-name">${esc(ev(id).name)}</span><span class="ev-when" hidden></span></button>`).join('\n  ')}
 </div>
 <div class="go"><button type="button" id="lock" class="primary" disabled>Pick two</button><p class="hint" id="hint">Tap two cards.</p></div>
 <section class="reveal" id="reveal" hidden aria-labelledby="verdict" tabindex="-1">
  <img class="ruler" src="art/ruler-800.webp" srcset="art/ruler-800.webp 800w, art/ruler-1584.webp 1584w" sizes="(min-width: 1180px) 1116px, 100vw" width="1584" height="672" loading="lazy" decoding="async" alt="">
  <div class="verdict-row">
  <h2 id="verdict"></h2>
  <img id="seal" src="art/seal-right-256.webp" srcset="art/seal-right-256.webp 256w, art/seal-right-512.webp 512w" sizes="96px" width="512" height="512" alt="" decoding="async" hidden>
  </div>
  <p class="hook" id="hook"></p>
  <figure class="tl" id="tl" aria-describedby="gaps"><figcaption class="tl-cap">To scale. Bars show how sure we are of each date.</figcaption><div class="tl-plot" id="plot"></div></figure>
  <ul class="gaps" id="gaps"></ul>
  <div class="acts"><button type="button" id="next" class="primary">Next round</button><button type="button" id="dare-btn" class="ghost">Dare a friend</button><button type="button" id="card-btn" class="ghost">Save card image</button></div>
  <p class="share-msg" id="share-msg" role="status"></p>
  <details class="srcs"><summary>Where these dates come from</summary><ul id="srcs"></ul></details>
 </section>
 <noscript><p class="nojs">The game needs JavaScript. Every answer and source is listed below.</p></noscript>
</section>
<section class="all" aria-labelledby="all-h">
 <details${''}><summary id="all-h">All ${data.trios.length} answers (spoilers)</summary>
 <ol class="sp">${spoilers}</ol></details>
</section>
<section class="how" aria-labelledby="how-h">
 <figure class="how-art"><img src="art/triptych-640.webp" srcset="art/triptych-640.webp 640w, art/triptych-1100.webp 1100w" sizes="(min-width: 900px) 460px, 100vw" width="1100" height="738" loading="lazy" decoding="async" alt="Three museum pedestals hold a papyrus scroll, a blank-faced helmeted bust and a smartphone, joined by glowing gold strings with measuring ticks."></figure>
 <div class="how-txt">
 <h2 id="how-h">How the answers are checked</h2>
 <p>Every date comes from the Wikipedia article linked next to it, read on ${esc(data.meta.checked)}. Old dates carry a range (the Great Pyramid is dated "between 2700 and 2500 BC"). A round is used only if its answer stays the same at both ends of every range. The closest call in the set is ${Math.min(...data.trios.map((t) => t.margin))} years.</p>
 <p>"You, reading this" is the current year. There is no year zero, so 1 BC to AD 1 counts as one year.</p>
 <p>Nothing you tap leaves your browser. No cookies, no tracking, no accounts.</p>
 <p class="credit">Illustrations made with an AI image model (Nano Banana Pro). No real people are shown.</p>
 </div>
</section>
</main>
<footer class="foot"><p><a href="${AFTERNIC}" rel="noopener">This domain is for sale.</a></p></footer>
<script type="application/json" id="data">${JSON.stringify({ events: data.events, trios: data.trios.map(({ e, answer, hook }) => ({ e, answer, hook })) }).replace(/</g, '\\u003c')}</script>
<script src="app.js" defer></script>
</body>
</html>
`;

// ---- /scan-preview/: scan-first home candidate (Dash 11/27). noindex, canonical to the home, not in the sitemap, nothing links to it. ----
// Same ids as the home, so app.js runs unchanged (a copy that shares the home URL and loads ../art/). scan.js keeps each tile's pictogram in step with the round.
const KIND = JSON.parse(readFileSync(join(here, 'kinds.json'), 'utf8'));
for (const id of Object.keys(data.events)) if (!KIND[id]) throw new Error(`no pictogram kind for ${id}`);
// Pictograms drawn here (24x24 line icons, not logos). One per kind of moment; none shows a real person.
const ICONS = {
  build: '<path d="M3 21h18M5 21V10l7-5 7 5v11M9 21v-6h6v6"/>',
  battle: '<path d="M5 3l9 9M3 5l2-2M14 12l-3 3 2 2 3-3M19 3l-9 9M21 5l-2-2M10 12l3 3-2 2-3-3M6 18l-3 3M18 18l3 3"/>',
  crown: '<path d="M3 8l4 4 5-7 5 7 4-4-2 11H5z"/><path d="M5 19h14"/>',
  flag: '<path d="M5 21V4M5 4h11l-2 4 2 4H5"/>',
  life: '<path d="M7 20c0-6 2-10 8-14M15 6c2 0 4 2 4 4-2 0-4-1-4-4zM11 11c-2-1-5 0-6 2 2 1 5 0 6-2zM9 15c3 0 5 1 6 3-3 1-5 0-6-3z"/>',
  make: '<path d="M9 18h6M10 21h4M12 3a6 6 0 0 0-4 10.5c.8.8 1 1.5 1 2.5h6c0-1 .2-1.7 1-2.5A6 6 0 0 0 12 3z"/>',
  write: '<path d="M4 20c4-1 7-4 9-8l6-8-4 1-7 8c-2 2-3 4-4 7zM9 15l3 3"/>',
  ship: '<path d="M3 17l2 4h14l2-4zM12 3v12M12 4l6 9H6z"/>',
  space: '<circle cx="12" cy="12" r="5"/><path d="M3 15c3 2 15-2 18-7"/>',
  fire: '<path d="M3 21l6-11 3 4 2-3 7 10zM12 7c0-2 1-3 2-4M15 8c1-1 2-1 3-1"/>',
  play: '<rect x="3" y="7" width="18" height="11" rx="4"/><path d="M7 12h4M9 10v4M15.5 11.5h.01M17.5 13.5h.01"/>',
  you: '<circle cx="12" cy="8" r="3.5"/><path d="M5 21c1-4 4-6 7-6s6 2 7 6"/>',
};
const sprite = `<svg class="sprite" aria-hidden="true" style="display:none"><defs>${Object.entries(ICONS).map(([k, d]) => `<symbol id="k-${k}" viewBox="0 0 24 24">${d}</symbol>`).join('')}</defs></svg>`;
const LOCKUP = (href) => `<a class="lockup" href="${href}" aria-label="Clever Dates home"><svg class="lk-mark" viewBox="0 0 40 40" aria-hidden="true"><rect x="2" y="5" width="36" height="33" rx="8" fill="#f4eedf"/><rect x="2" y="5" width="36" height="10" rx="8" fill="#ff7a59"/><rect x="2" y="11" width="36" height="4" fill="#ff7a59"/><rect x="11" y="2" width="4" height="8" rx="2" fill="#0f3b2c"/><rect x="25" y="2" width="4" height="8" rx="2" fill="#0f3b2c"/>${[0, 1, 2].map((r) => [0, 1, 2, 3].map((c) => `<rect x="${7 + c * 7.2}" y="${19 + r * 6}" width="4.6" height="4" rx="1" fill="${r === 2 && c === 2 ? '#ff7a59' : '#0f3b2c'}"${r === 2 && c === 2 ? '' : ' opacity=".8"'}/>`).join('')).join('')}</svg><span class="lk-word">Clever Dates</span></a>`;
const rel = (h) => h.replace(/(["\s,])art\//g, '$1../art/').replace(/(["(])fonts\//g, '$1../fonts/').replace('href="style.css"', 'href="../style.css"');
const swap = (h, a, b) => { if (h.split(a).length !== 2) throw new Error(`scan-preview: anchor not found once: ${a.slice(0, 60)}`); return h.replace(a, () => b); };
let scanHTML = rel(html);
scanHTML = swap(scanHTML, '<link rel="canonical"', '<meta name="robots" content="noindex">\n<link rel="canonical"');
scanHTML = swap(scanHTML, '<link rel="stylesheet" href="../style.css">', '<link rel="stylesheet" href="../style.css">\n<link rel="stylesheet" href="scan.css">');
scanHTML = swap(scanHTML, '<body>\n<header class="bar"><a class="mark" href="./">Clever Dates</a>', `<body>\n${sprite}\n<header class="bar">${LOCKUP('../')}`);
scanHTML = swap(scanHTML, '<main>', '<main class="scan">');
scanHTML = swap(scanHTML, '\n   <p class="dek">Pick the two moments nearest each other.</p>', '');
first.e.forEach((id, i) => { scanHTML = swap(scanHTML, `<span class="ev-n">${'ABC'[i]}</span>`, `<span class="ev-n"><svg class="ev-ic" aria-hidden="true"><use href="#k-${KIND[id]}"/></svg><span class="ev-l">${'ABC'[i]}</span></span>`); });
scanHTML = swap(scanHTML, '<details><summary id="all-h">', '<details><summary id="all-h"><svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><path d="M4 5h16M4 12h16M4 19h10"/></svg>');
{ const a = scanHTML.indexOf(' <div class="how-txt">'), b = scanHTML.indexOf(' </div>\n</section>', a);
  const inner = scanHTML.slice(a, b).replace('<h2 id="how-h">How the answers are checked</h2>', '<details><summary><svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><path d="M4 12l5 5L20 6"/></svg><h2 id="how-h">How the answers are checked</h2></summary>') + ' </details>\n';
  scanHTML = scanHTML.slice(0, a) + inner + scanHTML.slice(b); }
scanHTML = swap(scanHTML, '<footer class="foot"><p>', `<footer class="foot">${LOCKUP('../')}<p>`);
scanHTML = swap(scanHTML, '<script type="application/json" id="data">', `<script type="application/json" id="kinds">${JSON.stringify(KIND)}</script>\n<script type="application/json" id="data">`);
scanHTML = swap(scanHTML, '<script src="app.js" defer></script>', '<script src="app.js" defer></script>\n<script src="scan.js" defer></script>');
if (/scan-preview/.test(html)) throw new Error('home must not link the preview');
const scanApp = readFileSync(join(here, 'src/app.js'), 'utf8')
  .replace(/const publicPage = \(\) => .*\n/, () => 'const publicPage = () => CANONICAL; // preview copy: dares and cards always point at the home\n')
  .replace(/(['`])art\//g, '$1../art/');
if (!scanApp.includes('const publicPage = () => CANONICAL;') || /['`]art\//.test(scanApp)) throw new Error('scan-preview app.js patch failed');

rmSync(out, { recursive: true, force: true });
mkdirSync(join(out, 'fonts'), { recursive: true });
writeFileSync(join(out, 'index.html'), html);
for (const f of ['app.js', 'style.css', 'og.jpg']) copyFileSync(join(here, 'src', f), join(out, f));
mkdirSync(join(out, 'art'), { recursive: true });
for (const f of readdirSync(join(here, 'src/art'))) copyFileSync(join(here, 'src/art', f), join(out, 'art', f));
for (const f of readdirSync(join(here, 'src/fonts'))) copyFileSync(join(here, 'src/fonts', f), join(out, 'fonts', f));
mkdirSync(join(out, 'scan-preview'), { recursive: true });
writeFileSync(join(out, 'scan-preview/index.html'), scanHTML);
writeFileSync(join(out, 'scan-preview/app.js'), scanApp);
for (const f of ['scan.js', 'scan.css']) copyFileSync(join(here, 'src', f), join(out, 'scan-preview', f));
writeFileSync(join(out, 'robots.txt'), `User-agent: *\nAllow: /\nSitemap: ${SITE}sitemap.xml\n`);
writeFileSync(join(out, 'sitemap.xml'), `<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>${SITE}</loc></url></urlset>\n`);
writeFileSync(join(out, 'CNAME'), 'closer.cleverdates.com\n');
writeFileSync(join(out, '.nojekyll'), '');
console.log('built', data.trios.length, 'trios');
