# C6 Closer In Time: STATUS (Gizmo)

## r3 art wired, live preview, 2026-11-25 10:05 AM CT

C6 (cleverdates-c6-preview). Commit 016ce90 (pushed, noindex kept, no DNS or go-live).

- Wired: the share card is drawn on `card-r3.webp` (pyramid, amphora and phone on turquoise, hieroglyph-free) with a source crop; the old `card-1080.webp` is removed from src and docs. The hook (the answer) is NOT drawn on the card, so the dare still hides the answer.
- CUT: the on-page reveal strip. A static picture of one trio would mislead on most of the 101 rounds. The on-page art set stays hero, ruler, triptych.
- Caveat and question: the card art is the same pyramid/amphora/phone for every trio, so a card for the Domesday Book trio shows a pyramid and a phone. Same trade-off as the old card. Decision for Evan or Dash: keep generic, or add a spoiler variant that shows the hook (needs trio-specific art or a typographic hook band).
- Test fix: the stale dare-link e2e line now expects the canonical URL on localhost.
- Live e2e (qa/art-folds/r3/e2e-live.log): ALL PASS (159), trios 1 (right), 13 (wrong), 19 (right) and 41 (wrong, longest names): 1080x1350, ground drawn, hook off the card, no localhost.
- Live gate (qa/art-folds/r3/gate-live/, PASS): Lighthouse 100 / 100 / 100 / SEO 63, CLS 0, LCP 1.2 s, impeccable 0 at 390, 1280, static. Local gate: qa/r3/gate-local (99).
- Live captures (viewed): qa/art-folds/r3/live-reveal-{right,wrong}-{390,1280}.png and the live card PNGs card-trio{1-right,13-wrong,19-right,41-wrong}.png.
Updated 2026-11-25 8:10 AM CT
- [x] Step 1: day-1 gate PASS, 43 sourced and validated trios (trios.json)
- [x] Step 2: prior art logged, noindex preview live at https://evanmack45.github.io/cleverdates-c6-preview/, gate PASS 390/1280, impeccable 0, e2e all pass
- [x] Art (Dash's fal set): hero, in-game deep-time strip, museum triptych, og.jpg, and a share card built on the art. Image slots are filled, so no separate plan is needed.
- [x] Step 3: 101 sourced and validated trios, live. Gate PASS 390/1280 (Lighthouse mobile 100/100/100, SEO 63 from noindex), impeccable 0 at both widths (start and revealed state), live e2e ALL PASS (143 checks, all 101 trios accept the right answer, no overflow).
- Validator rules now enforced: at least 100 trios, no anchor event in more than 4 trios (max is 4: cleo, pyramid, today, colosseum, gutenberg), a region on every event, and the coverage floors below.
- Coverage (a trio counts once per bucket it touches):
  - Era: Deep prehistory 11 · 10,000 BC to 500 BC 24 · 500 BC to AD 500 33 · AD 500 to 1500 45 · 1500 to 1799 21 · 1800 to 1899 19 · 1900 to now 34
  - Region: Africa 33 · Asia 46 · Middle East 27 · Latin America 14 · Oceania 12 · Europe 65 · North America 30 · Global 17
  - Event slots: Europe 93 · Asia 55 · Africa 38 · North America 33 · Middle East 29 · Global 27 · Latin America 16 · Oceania 12. Europe plus North America is 41.6% of slots (cap 50%).
- [x] Step 4: surprise pass. 22 plain same-year trios were swapped for long-gap "X is closer in time to M than to A" trios (21 plain ones plus the old Oxford trio, rebuilt so Oxford and the Aztecs are the close pair). Still 101 trios, same gate numbers (Lighthouse mobile 100/100/100, SEO 63 from noindex; impeccable 0 at both widths, start and revealed state; live e2e ALL PASS, 143 checks).
- Surprise score (tools/build_trios.py, per trio under `til` in trios.json; hand-tagged era "feel" in tools/feel.py, subjective by design):
  - Cultural lure: the truly closest pair feels at least 1 era-step farther apart than some decoy pair (Cleopatra and the iPhone vs Cleopatra and the Pyramid). 44 trios.
  - Long gap: the closest pair is 1,000+ years apart and the decoy is not absurdly farther (ratio 6 or less). 17 trios.
  - Low-surprise = neither. **50 of 101 remain.** Hard caps: low-surprise at most 50% (today's level, so it cannot get worse), plain same-decade at most 15.
  - Plain same-decade coincidences (answer pair 10 years or less apart, no lure, no long gap): **15 remain** (was 36). Trios 27, 32, 33, 43, 50, 54, 55, 56, 59, 68, 69, 70, 72, 73, 79 in the current numbering.
  - The other 35 low-surprise trios are "about the same time" pairs with a longer gap (for example Mohenjo-daro and Stonehenge, Kush and Rome). They are fine trivia but not illusions.
  - Why not fewer: new trios needed a decoy that feels like it belongs with the pair but is farther in time, and each event may appear in 4 trios at most. After 22 swaps I ran out of good decoys. The rest would have been filler, so I stopped and kept the 15.
- Open: Go-live on cleverdates.com waits on Dash. Some trios are "same year" pairs; the strongest surprises are the long-gap ones (for example Lucy, Lascaux, Ishango, Cleopatra).
