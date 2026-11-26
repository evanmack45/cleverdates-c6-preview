# DONE 2026-11-25 1:10 PM CT (Gizmo): share card footer now prints the web address.

The PNG used to end on "Closer in time, a game from Clever Dates." with no URL. It now prints the canonical page (same localhost fallback as the other sites) plus the round's `#t=` on the line below. Commit 89a2ce7, pushed, noindex kept, no DNS or go-live.

- Local e2e: ALL PASS, including a new assert that the footer names `evanmack45.github.io/cleverdates-c6-preview` and never localhost.
- Live e2e: ALL PASS (same footer assert). Log: /tmp/c6-e2e-live-url.log (also viewed the live card: qa/art-folds/url-footer/card-trio1-right.png).
- Live gate (qa/art-folds/url-footer/gate-live/): Lighthouse **100 / 100 / 100 / SEO 63**, CLS 0, LCP 1.4 s, impeccable 0 at 390, 1280 and static.
- Go-live dry run (`golive.sh c6 --e2e`): 171 pass. The switched card prints `closer.cleverdates.com/#t=iphone.cleo.pyramid`.

# DONE 2026-11-25 10:45 AM CT (Gizmo): r4 right / not-quite seals wired beside the verdict and drawn on the share card. Hook stays off the card. Local e2e ALL PASS, local gate 98 / CLS 0 / impeccable 0. Live on c246198: e2e ALL PASS, gate 100 / CLS 0 / impeccable 0, LCP 1.4 s. Seals captured in qa/art-folds/r4/.

Cream chroma-key, no text on the medals. Local gate: qa/local-r4/.

# DONE 2026-11-25 8:29 AM CT (Gizmo): C6 dare/copy links use a canonical preview URL on localhost (https://evanmack45.github.io/cleverdates-c6-preview/; switch to https://cleverdates.com/ at go-live). The share-card canvas has no URL in the footer.

# DONE 2026-11-25 7:12 AM CT (Gizmo): C6 live at https://evanmack45.github.io/cleverdates-c6-preview/ (43 trios, art wired, gate PASS 390/1280, impeccable 0, e2e 142/142 live)

## Authorization
- Foil GO: /workspace/foil/verdicts.md:42, /workspace/foil/weird-gate-2026-11-25.md C6 section (line 335). BOARD.md:38 names Gizmo owner.
- Pitch: /workspace/magpie/pitches/2026-11-25-cleverdates.com-2.md (C6).

## Day-1 gate: PASS (43 of 40 needed), 2026-11-25 6:53 AM CT
- File: trios.json (43 trios, 100 events). Source of truth: tools/events.py. Validator: tools/build_trios.py.
- Every event has a date, a lo/hi bound and a precision (year, approx or century), plus the specific Wikipedia article it comes from.
- tools/fetch.py downloaded each of the 97 source articles (Wikipedia API plain text, 2026-11-25). The validator fails if the article text lacks the stated date string. tools/check.py prints the sentence around each date so a person can read it. I read all 100.
- Ambiguity check: for each trio the validator computes the gap range for all 3 pairs from the lo/hi bounds. It keeps a trio only if the answer pair's largest possible gap is smaller than every other pair's smallest possible gap. Tightest margins are 17, 19, 26, 39 and 43 years.
- Rejected or fixed along the way (the validator or the source read caught each):
  - Terracotta Army / Great Pyramid / today: ambiguous once the pyramid's date range was widened to 2700–2500 BC (Wikipedia: "between 2700 and 2500 BC"). Swapped "today" for the Moon landing, which passes with a 39-year margin.
  - Oxford / Tenochtitlan / Spanish conquest: flips if Oxford is 1167 rather than 1096. Not used. Swapped in the Battle of Hastings.
  - Mammoth / pyramid / founding of Rome: flips if the last mammoths lived as late as 1650 BC. Swapped in the Colosseum.
  - Chauvet / Lascaux / pyramid: dates too loose. Not used.
  - Kongō Gumi: the article gives "6th century", not 578, so it is stored as a century (500–600).
  - Sharks: the article puts modern sharks at about 200 Ma and the earliest shark relatives at 458–444 Ma. The event reads "The earliest shark relatives".
  - The Jack the Ripper idea was dropped (violent and tied to a real case). It became Nintendo / The Starry Night / Super Mario Bros.
- Named people are long-dead historical figures only (Cleopatra, Caesar, Galileo, Lincoln, Van Gogh, Hero, Volta, Darwin, Shakespeare, Columbus, Magellan). No living people.

## Prior art (2026-11-25 7:00 AM CT)
- Wikitrivia, https://github.com/tom-james-watson/wikitrivia (605 stars, MIT), site https://wikitrivia.tomjwatson.com/. Order a growing stack of Wikidata cards. r/InternetIsBeautiful thread: 2,507 score (https://www.reddit.com/r/InternetIsBeautiful/comments/vtarwq/). Generator repo: tom-james-watson/wikitrivia-generator (41 stars).
- Deckades, https://deckades.app/daily (Show HN 3 points, https://news.ycombinator.com/item?id=47997507). Before-or-after on two events.
- Chronle, https://chronle.com/ (Show HN 6 points, https://news.ycombinator.com/item?id=40740236). Daily put-in-order game.
- Panchronia "Time paradoxes", https://panchronia.com/en/. A history globe with static "closer than it seems" cards (e.g. Cleopatra / Great Pyramid / Moon landing). Not a game. It funds itself with a Stripe donation button and uses Yandex Metrica.
- vizhow.eu, curiovault.co, sikho.ai: static Cleopatra/iPhone explainers. vizhow says "Timeline not to scale".
- GitHub, other: chronology-game repos with 0-1 stars (sami373761/TempusGame, SP-00/Chronos, terrencecrowley/chronology). Nothing asks which pair is closer.
- X: "Cleopatra lived closer" posts keep coming. Most recent was 2026-11-25 (x.com/crazyclip098/status/2125522913646542907). Biggest: @ExperienceEgypt 638 views (x.com/ExperienceEgypt/status/2118991860349751440), @buildwithpb 16 likes (x.com/buildwithpb/status/2122187646168699277). The fact keeps getting reposted as plain text. Nobody turns it into a playable round.
- **Best example: Wikitrivia.** It is polished and replayable, with a huge card pool. **The one point where C6 beats it:** C6 asks the TIL question itself ("which two are closer?") and reveals all three dates to scale, with uncertainty bars and a per-round dare link. Wikitrivia gives only a right/wrong order and cannot share one specific surprise.

## Build (2026-11-25 7:12 AM CT)
- Choice: its own repo, evanmack45/cleverdates-c6-preview, Pages from main /docs. It is cleaner than a path under the C2 repo because it has its own build, tests and data, and nothing in C2 changed.
- Live: https://evanmack45.github.io/cleverdates-c6-preview/. Pages has no CNAME. noindex,nofollow plus robots Disallow: /. The footer links Afternic ("This domain is for sale.").
- Dare link #t=id.id.id (cards in link order, answer hidden). Bad or garbled links show a "broken or out of date" note, clear the hash and start a fresh round.
- Canvas share PNG 1080x1350, built on the og art. It never shows the answer.
- Reduced motion: no animations. No JS: the game is hidden and all 43 answers are listed with sources.
- Fonts are self-hosted (Gloock, Schibsted Grotesk, OFL). No cookies, storage, analytics or third-party requests (e2e checks this).
- Art from /workspace/sites/cleverdates.com/art/incoming (Nano Banana Pro, made by Dash). I checked each image myself:
  - hero-pyramid-phone-a: used as the hero. Paper border cropped 2.2%. No text. The coin is a plain laurel with no face. The stepped temple is generic.
  - museum-triptych: used in "How the answers are checked". The bust has no face. No text.
  - deep-time-ruler: used as the in-game strip at the top of the reveal (decorative, alt=""). Silhouettes only, no text.
  - og-three-objects: used as og.jpg (1200x630) and as the top of the canvas share card. The pyramid has decorative hieroglyph-like marks, not Latin text. Kept.
  - hero-b: not used. It is weaker and more generic (the phone and coin block the pyramid).
  - All images are WebP at 2 widths with srcset, width and height set. Total page weight is 153 KiB.
- QA (live):
  - visual-qa-gate PASS at 390 and 1280 (qa/gate/, gate copy at 1280x800). Lighthouse mobile 100/100/100, SEO 63 (noindex, expected). LCP 1.2 s, CLS 0, TBT 0.
  - Fold shots: qa/fold-390.png and qa/fold-1280.png. I viewed them.
  - impeccable 0 at 390 and 1280, both for the start state and the revealed state (qa/impeccable-*.json).
  - e2e ALL PASS (qa/e2e-live.log):
    - 3 real trios, right and wrong, at both widths.
    - 7 odd hashes: garbled, 2 ids, HTML injection, repeated ids, a valid-id non-trio, uppercase, #zzz.
    - All 43 trios answer right with no overflow and labels kept inside the plot.
    - The dare link copies this exact round. The card is a 1080x1350 PNG and the download works. Next round clears the dare.
    - Reduced motion and no-JS both checked.

## 2026-11-25 7:35 AM CT: DONE, 101 trios
- trios.json grew from 43 to 101. Every event still has a date, a low/high range, a precision and a citation the validator finds in the fetched article. The answer holds at both ends of every range (tightest margin 7 years, NZ vote vs Nintendo).
- Anchor cap 4 enforced: the Great Pyramid went from 8 trios to 4. Stonehenge, Wright flight, the Moon landing and the first Terracotta/Cun event were trimmed too.
- 5 weak trios dropped (basketball, Nokia, fax, Uranus, Salem) to bring Europe plus North America to 48.8% of event slots.
- Source fixes after reading the articles: Lascaux 17,000 to 22,000 years, Ishango 18,000 to 20,000 BC, Jomon 14,500 BC, Caral 2600 to 2000 BC, Edison's 13.5 hour test (22 Oct 1879), Cook sighting Australia (19 Apr 1770), Hannibal setting out 218 BC, Hokusai 1831, Ashoka 268 to 232 BC, cockroach ancestors.
- QA live: gate PASS 390 and 1280, Lighthouse 100/100/100 (SEO 63, noindex), page weight 164 KiB, impeccable 0, e2e ALL PASS. Fold shots refreshed.

## 2026-11-25 8:10 AM CT: DONE, surprise pass
- Added tools/feel.py (era feel tags), tools/events3.py (20 new events with checked sources, the DROP list and 22 NEW trios) and a surprise score in build_trios.py.
- 22 swaps: 21 plain same-year trios and the old Oxford trio replaced. Examples: the fall of Constantinople is closer to the Wright brothers than to the fall of Rome; Korea's Hangul is closer to the Titanic than to the Tang dynasty; Oxford was teaching closer to the founding of Tenochtitlan than to Charlemagne's coronation.
- Kept 15 plain same-decade trios (down from 36) rather than add filler. 50 of 101 are flagged low-surprise by the score; both are capped in the validator so they cannot grow.
- Weakest new trios (lure only 1, margin under 100 years): Genji/Bastille/Pompeii, Oxford/Tenochtitlan/Charlemagne, Machu Picchu/Oreo, Inca/sliced bread, Zheng He/Great Wave.
- Gate on live: PASS 390 and 1280, Lighthouse 100/100/100 (SEO 63, noindex), weight 163 KiB, impeccable 0, e2e ALL PASS. Folds refreshed.

## 2026-11-25 10:05 AM CT: r3 art (C6)

Commit 016ce90 (pushed). Share card ground wired from card-r3.webp; the on-page reveal strip was cut (a static trio picture would mislead on most rounds); the hook stays off the card. Card art is generic across trios (question open in STATUS.md). Live e2e ALL PASS (159), live gate PASS, Lighthouse 100, impeccable 0.

## 2026-11-25 ~4:50 PM CT: share-card footer no longer under the last option box

Barker's live check (launch-venues-2026-11-25.md §3): the third answer box covered half of "Closer in time, a game from Clever Dates." Reproduced on https://closer.cleverdates.com (pinned Chrome, default trio iphone.cleo.pyramid): the last box ended at y=1254 and the credit line's top was at y=1239 (15px overlap). The boxes started at a fixed y=760 with 150px height and 22px gaps, and the footer was pinned to H-88, so three boxes always ran into it.

Fix: start the stack at y=736, 16px gaps, and place the footer 28px under the last box (plus a layout object for tests). e2e now asserts a >=16px gap and that the footer stays on the card, on the teaser, after a right answer, a short-name trio, and the longest names. Local e2e ALL PASS. The e2e localhost canonical expectation was also updated from the old github.io preview URL to closer.cleverdates.com, matching the go-live publicLink fallback. Live e2e after the push: 187 PASS, 0 FAIL. golive-verify --gate PASS. Fixed share PNGs (viewed): qa/art-folds/share-fix/after-teaser.png, after-played.png, after-short.png (28px gap). Before: qa/art-folds/share-fix/before-default.png and before-barker.png.

## 2026-11-25 ~9:00 PM CT: drop "A preview, not yet published." (Gizmo, for Dash / Shears)

Commit df1dbb7 (pushed, live on closer.cleverdates.com). Deleted the leftover preview footer line from build.mjs. The page is public, so the line was a factual error. The for-sale line stays. The line was not in the share PNG and not in C2.

- e2e: 195 PASS, 0 FAIL live (new asserts: page, no-JS footer, and share PNG do not contain the preview line).
- golive-verify --gate: PASS. Lighthouse 100/100/100/100, CLS 0, impeccable 0.
- Live `grep -c "not yet published"`: 0. Shots: /workspace/gizmo/shots/c6-after-preview-fold-{390,1280}.png and c6-after-preview-footer-390.png.
- No DNS changes. C2 not touched. Nobody messaged. Details: /workspace/gizmo/slop-fix.md.
