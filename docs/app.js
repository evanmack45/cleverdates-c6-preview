(() => {
  'use strict';
  const D = JSON.parse(document.getElementById('data').textContent);
  const EV = D.events;
  const $ = (id) => document.getElementById(id);
  const picksEl = $('picks'), lock = $('lock'), hint = $('hint'), reveal = $('reveal'), note = $('note');
  const reduce = matchMedia('(prefers-reduced-motion: reduce)');
  const mid = (e) => (e.lo + e.hi) / 2;
  const fmt = (n) => n.toLocaleString('en-US');

  // ---- state (memory only) ----
  const order = [0, ...shuffle(D.trios.slice(1).map((_, i) => i + 1))];
  let pos = 0, round = 0, right = 0;
  let cur = null;        // { t, ids } ids = display order
  let picked = [];
  let result = null;     // null | true | false

  function shuffle(a) { for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } return a; }

  // ---- gaps ----
  function gapYears(a, b) {
    const A = EV[a], B = EV[b];
    return Math.abs(mid(A) - mid(B));
  }
  function gapText(a, b) {
    const A = EV[a], B = EV[b], g = gapYears(a, b);
    const exact = A.prec === 'year' && B.prec === 'year';
    if (exact) {
      const ys = (e) => [Math.floor(e.lo), Math.floor(e.hi)];
      const [a0, a1] = ys(A), [b0, b1] = ys(B);
      const lo = Math.max(0, a0 - b1, b0 - a1), hi = Math.max(a1 - b0, b1 - a0);
      if (hi === 0) return 'the same year';
      if (lo === hi) return `${fmt(lo)} year${lo === 1 ? '' : 's'}`;
      return lo === 0 ? `0 to ${fmt(hi)} year${hi === 1 ? '' : 's'}` : `${fmt(lo)}–${fmt(hi)} years`;
    }
    if (g >= 1e6) { const m = g / 1e6; return `about ${m < 10 ? m.toFixed(1).replace(/\.0$/, '') : fmt(Math.round(m))} million years`; }
    if (g >= 10000) return `about ${fmt(Math.round(g / 1000) * 1000)} years`;
    if (g >= 1000) return `about ${fmt(Math.round(g / 10) * 10)} years`;
    if (g >= 100) return `about ${fmt(Math.round(g / 5) * 5)} years`;
    return `about ${fmt(Math.round(g))} years`;
  }

  // ---- hash: #t=id.id.id ----
  function fromHash() {
    const h = location.hash;
    if (!h || h === '#') return null;
    const m = /^#t=([a-z0-9_]{1,24})\.([a-z0-9_]{1,24})\.([a-z0-9_]{1,24})$/.exec(h);
    const ids = m && m.slice(1, 4);
    const i = ids ? D.trios.findIndex((t) => ids.every((id) => t.e.includes(id)) && new Set(ids).size === 3) : -1;
    if (i < 0) return { bad: true };
    return { i, ids };
  }

  function load(i, ids, dare) {
    const t = D.trios[i];
    cur = { t, ids: ids || t.e.slice() };
    picked = []; result = null; round++;
    $('dare').hidden = !dare;
    picksEl.querySelectorAll('.ev').forEach((b, k) => {
      const id = cur.ids[k], e = EV[id];
      b.dataset.id = id;
      b.querySelector('.ev-name').textContent = e.name;
      const w = b.querySelector('.ev-when'); w.textContent = e.when; w.hidden = true;
      b.setAttribute('aria-pressed', 'false'); b.disabled = false;
      b.classList.remove('is-ans', 'is-miss');
    });
    reveal.hidden = true; $('share-msg').textContent = '';
    picksEl.classList.remove('done');
    syncLock(); status();
  }

  function status() { $('round').textContent = `Round ${round}${round > 1 || result !== null ? ` · ${right} right` : ''}`; }
  function syncLock() {
    lock.disabled = picked.length !== 2;
    lock.textContent = picked.length === 2 ? 'Lock in these two' : 'Pick two';
    hint.textContent = picked.length === 0 ? 'Tap two cards.' : picked.length === 1 ? 'Now tap one more.' : 'Tap a card again to change it.';
    lock.hidden = result !== null; hint.hidden = result !== null;
  }

  picksEl.addEventListener('click', (ev) => {
    const b = ev.target.closest('.ev');
    if (!b || result !== null) return;
    const id = b.dataset.id;
    if (picked.includes(id)) picked = picked.filter((x) => x !== id);
    else { picked.push(id); if (picked.length > 2) picked.shift(); }
    picksEl.querySelectorAll('.ev').forEach((x) => x.setAttribute('aria-pressed', String(picked.includes(x.dataset.id))));
    syncLock();
  });

  lock.addEventListener('click', () => {
    if (picked.length !== 2 || result !== null) return;
    const ans = cur.t.answer;
    result = picked.every((id) => ans.includes(id));
    if (result) right++;
    showReveal();
    status(); syncLock();
  });

  function showReveal() {
    const ans = cur.t.answer;
    picksEl.classList.add('done');
    picksEl.querySelectorAll('.ev').forEach((b) => {
      b.querySelector('.ev-when').hidden = false;
      b.classList.toggle('is-ans', ans.includes(b.dataset.id));
      b.classList.toggle('is-miss', b.getAttribute('aria-pressed') === 'true' && !ans.includes(b.dataset.id));
    });
    $('verdict').textContent = result ? 'Right.' : 'Not quite.';
    $('verdict').className = result ? 'ok' : 'no';
    const seal = $('seal'), key = result ? 'right' : 'not-quite';
    seal.src = `art/seal-${key}-256.webp`;
    seal.srcset = `art/seal-${key}-256.webp 256w, art/seal-${key}-512.webp 512w`;
    seal.sizes = '96px';
    seal.alt = result ? 'A gold medal with a starburst and ribbons.' : 'A dusty rose medal with a crack, slightly tilted.';
    seal.hidden = false;
    $('hook').textContent = cur.t.hook;
    drawTimeline();
    const pairs = [[cur.ids[0], cur.ids[1]], [cur.ids[0], cur.ids[2]], [cur.ids[1], cur.ids[2]]]
      .sort((p, q) => gapYears(...p) - gapYears(...q));
    $('gaps').replaceChildren(...pairs.map((p, k) => {
      const li = document.createElement('li');
      if (cur.t.answer.includes(p[0]) && cur.t.answer.includes(p[1])) li.className = 'win';
      const a = document.createElement('span'); a.className = 'g-pair'; a.textContent = `${EV[p[0]].name} / ${EV[p[1]].name}`;
      const g = document.createElement('span'); g.className = 'g-yrs'; g.textContent = gapText(...p);
      li.append(a, g); return li;
    }));
    $('srcs').replaceChildren(...cur.ids.map((id) => {
      const e = EV[id], li = document.createElement('li');
      li.append(`${e.name}: ${e.when}. `);
      if (e.src) { const a = document.createElement('a'); a.href = e.src; a.rel = 'noopener'; a.textContent = decodeURIComponent(e.src.split('/wiki/')[1]).replace(/_/g, ' ') + ' (Wikipedia)'; li.append(a); }
      else li.append('The current year.');
      return li;
    }));
    reveal.hidden = false;
    reveal.classList.remove('in'); void reveal.offsetWidth; reveal.classList.add('in');
    reveal.focus({ preventScroll: true });
    reveal.scrollIntoView({ behavior: reduce.matches ? 'auto' : 'smooth', block: 'start' });
  }

  function drawTimeline() {
    const ids = cur.ids.slice().sort((a, b) => mid(EV[a]) - mid(EV[b]));
    const lo = Math.min(...ids.map((id) => EV[id].lo)), hi = Math.max(...ids.map((id) => EV[id].hi));
    const span = Math.max(hi - lo, 1), pad = 4;
    const x = (v) => pad + ((v - lo) / span) * (100 - 2 * pad);
    const plot = $('plot');
    const ans = cur.t.answer;
    const parts = [];
    parts.push('<div class="tl-track"></div>');
    // brackets between neighbours: the closest pair is always one of these
    for (let k = 0; k < 2; k++) {
      const a = ids[k], b = ids[k + 1];
      const l = x(mid(EV[a])), r = x(mid(EV[b]));
      const win = ans.includes(a) && ans.includes(b);
      const c = (l + r) / 2;
      parts.push(`<div class="br${win ? ' win' : ''}${c > 78 ? ' edge-r' : c < 22 ? ' edge-l' : ''}" style="--l:${l.toFixed(2)};--r:${r.toFixed(2)}"><span>${esc(gapText(a, b))}</span></div>`);
    }
    ids.forEach((id, k) => {
      const e = EV[id], l = x(e.lo), r = x(e.hi), m = x(mid(e));
      if (r - l > 0.8) parts.push(`<div class="band" style="--l:${l.toFixed(2)};--r:${r.toFixed(2)}"></div>`);
      parts.push(`<div class="dot${ans.includes(id) ? ' win' : ''}" style="--x:${m.toFixed(2)};--d:${k}"></div>`);
      parts.push(`<div class="lab" style="--x:${m.toFixed(2)};--row:${k}"><b>${esc(e.when)}</b><span>${esc(e.name)}</span></div>`);
    });
    plot.innerHTML = parts.join('');
  }
  function esc(s) { return String(s).replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c])); }

  $('next').addEventListener('click', () => {
    if (location.hash) history.replaceState(null, '', location.pathname + location.search);
    note.hidden = true;
    pos = (pos + 1) % order.length;
    load(order[pos], null, false);
    picksEl.querySelector('.ev').focus({ preventScroll: true });
    scrollTo({ top: 0, behavior: reduce.matches ? 'auto' : 'smooth' });
  });

  // Switch to https://cleverdates.com/ at go-live.
  const CANONICAL = 'https://closer.cleverdates.com/';
  const isLocalPage = () => location.protocol === 'file:' || location.hostname === 'localhost' || location.hostname === '127.0.0.1';
  const publicPage = () => (isLocalPage() ? CANONICAL : `${location.origin}${location.pathname}`).replace(/index\.html$/, '').replace(/\/?$/, '/');
  const publicLink = (hash) => `${publicPage()}${hash.startsWith('#') ? hash : '#' + hash}`;
  function dareURL() { return publicLink('#t=' + cur.ids.join('.')); }
  $('dare-btn').addEventListener('click', async () => {
    const url = dareURL(), text = 'Bet you get this wrong: which two are closer in time?';
    const msg = $('share-msg');
    try {
      if (navigator.share && matchMedia('(pointer: coarse)').matches) { await navigator.share({ title: 'Closer in time', text, url }); msg.textContent = 'Sent.'; return; }
      await navigator.clipboard.writeText(url);
      msg.textContent = 'Link copied. It opens this exact round, answer hidden.';
    } catch (e) {
      if (e && e.name === 'AbortError') return;
      msg.textContent = 'Copy this link: ' + url;
    }
  });

  // ---- share card (canvas PNG) ----
  async function card() {
    const W = 1080, H = 1350, c = document.createElement('canvas');
    c.width = W; c.height = H;
    const g = c.getContext('2d');
    try { await Promise.all([document.fonts.load('80px Gloock'), document.fonts.load('700 40px Schibsted'), document.fonts.load('400 40px Schibsted')]); } catch (e) { /* system fonts */ }
    const serif = 'Gloock, Georgia, serif', sans = 'Schibsted, Arial, sans-serif';
    g.fillStyle = '#0f3b2c'; g.fillRect(0, 0, W, H);
    const art = await loadArt();
    if (art) g.drawImage(art, 0, 12, art.width, Math.round((art.width * 470) / W), 0, 0, W, 470);
    const fade = g.createLinearGradient(0, 380, 0, 470); fade.addColorStop(0, 'rgba(15,59,44,0)'); fade.addColorStop(1, '#0f3b2c');
    g.fillStyle = fade; g.fillRect(0, 380, W, 90);
    g.fillStyle = '#ff7a59'; g.font = `700 34px ${sans}`;
    const line = result === true ? 'I got this one right.' : result === false ? 'This one got me.' : 'Bet you get this wrong.';
    g.fillText(line, 80, 540);
    if (result === true || result === false) {
      const seal = await loadSeal(result);
      if (seal) {
        const sw = 140, sx = Math.min(80 + g.measureText(line).width + 24, W - 80 - sw), sy = 540 - 88;
        g.drawImage(seal, sx, sy, sw, sw);
      }
    }
    const layout = { boxes: [], texts: [] };
    const rec = (s, x, y) => {
      const m = g.measureText(s);
      const t = { s, x, y, w: m.width, top: y - (m.actualBoundingBoxAscent || 0), bottom: y + (m.actualBoundingBoxDescent || 0) };
      layout.texts.push(t);
      g.fillText(s, x, y);
      return t;
    };
    g.fillStyle = '#f4eedf'; g.font = `400 76px ${serif}`;
    wrap(g, 'Which two are closer in time?', 80, 630, W - 160, 82);
    // The title is two lines (baselines 630 and 712). Fit the three option
    // boxes under it, leaving a reserved footer band so the last box cannot
    // cover the credit line (it used to end at 1254, 15px into that line).
    const boxH = 150, boxGap = 16, startY = 736;
    let y = startY;
    cur.ids.forEach((id, k) => {
      g.fillStyle = '#f6efe0'; rr(g, 80, y, W - 160, boxH, 28); g.fill();
      layout.boxes.push({ x: 80, y, w: W - 160, h: boxH });
      g.fillStyle = '#b83a18'; g.font = `400 60px ${serif}`; rec('ABC'[k], 120, y + 96);
      g.fillStyle = '#0f3b2c'; g.font = `700 40px ${sans}`;
      const lines = lines2(g, EV[id].name, W - 160 - 160);
      lines.forEach((ln, j) => rec(ln, 210, y + boxH / 2 + 14 - (lines.length - 1) * 23 + j * 46));
      y += boxH + boxGap;
    });
    const lastBottom = layout.boxes.at(-1).y + layout.boxes.at(-1).h;
    g.fillStyle = '#e3d9bf'; g.font = `400 30px ${sans}`;
    const credit = rec('Closer in time, a game from Clever Dates.', 80, lastBottom + 28 + 23);
    const foot = publicLink(cur && cur.ids ? '#t=' + cur.ids.join('.') : '').replace(/^https?:\/\//, '');
    if (g.measureText(foot).width > W - 160) g.font = `400 26px ${sans}`;
    rec(foot, 80, credit.y + 42);
    lastLayout = layout;
    return c;
  }
  let lastLayout = null;
  let artP = null, sealP = {};
  function loadArt() { return artP || (artP = new Promise((r) => { const i = new Image(); i.onload = () => r(i); i.onerror = () => r(null); i.src = 'art/card-r3.webp'; })); }
  function loadSeal(ok) {
    const src = ok ? 'art/seal-right-512.webp' : 'art/seal-not-quite-512.webp';
    return sealP[src] || (sealP[src] = new Promise((r) => { const i = new Image(); i.onload = () => r(i); i.onerror = () => r(null); i.src = src; }));
  }
  function rr(g, x, y, w, h, r) { g.beginPath(); g.moveTo(x + r, y); g.arcTo(x + w, y, x + w, y + h, r); g.arcTo(x + w, y + h, x, y + h, r); g.arcTo(x, y + h, x, y, r); g.arcTo(x, y, x + w, y, r); g.closePath(); }
  function lines2(g, text, max) {
    const words = text.split(' '), out = []; let line = '';
    for (const w of words) { const t = line ? line + ' ' + w : w; if (g.measureText(t).width > max && line) { out.push(line); line = w; } else line = t; }
    out.push(line); return out.slice(0, 3);
  }
  function wrap(g, text, x, y, max, lh) { lines2(g, text, max).forEach((ln, i) => g.fillText(ln, x, y + i * lh)); }
  window.__c6card = async () => (await card()).toDataURL('image/png');
  window.__c6cardLayout = async () => { const c = await card(); return lastLayout; };
  $('card-btn').addEventListener('click', async () => {
    const c = await card();
    c.toBlob((blob) => {
      const a = document.createElement('a');
      a.href = URL.createObjectURL(blob); a.download = 'closer-in-time.png';
      document.body.append(a); a.click(); a.remove();
      setTimeout(() => URL.revokeObjectURL(a.href), 4000);
      $('share-msg').textContent = 'Card saved. It hides the answer, so send it with your dare link.';
    }, 'image/png');
  });

  function start() {
    const h = fromHash();
    if (h && !h.bad) { pos = order.indexOf(h.i); load(h.i, h.ids, true); note.hidden = true; return; }
    if (h && h.bad) { note.textContent = 'That dare link is broken or out of date, so here is a fresh round.'; note.hidden = false; history.replaceState(null, '', location.pathname + location.search); }
    pos = 0; load(order[0], null, false);
  }
  addEventListener('hashchange', start);
  start();
})();
