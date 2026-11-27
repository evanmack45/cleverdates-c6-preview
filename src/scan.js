// /scan-preview/ layer on top of app.js (unchanged ids): keeps each tile's pictogram in step with the round.
(() => {
  const KIND = JSON.parse(document.getElementById('kinds').textContent);
  const set = (b) => { const u = b.querySelector('.ev-ic use'); const k = KIND[b.dataset.id]; if (u && k) u.setAttribute('href', `#k-${k}`); };
  const evs = [...document.querySelectorAll('.ev')];
  evs.forEach(set);
  const mo = new MutationObserver((ms) => { for (const m of ms) if (m.attributeName === 'data-id') set(m.target); });
  evs.forEach((b) => mo.observe(b, { attributes: true, attributeFilter: ['data-id'] }));
})();
