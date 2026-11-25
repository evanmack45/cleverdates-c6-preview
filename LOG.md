# IN PROGRESS 2026-11-25 6:55 AM CT (Gizmo): C6 day-1 gate PASS, 43 sourced trios

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
