# Visual QA gate

Result: PASS (no P0)

## http://localhost:8954/ — phone
Load 559ms · frames p50 16.7ms p95 16.8ms · fonts Schibsted / Gloock · canvases 0
- no issues
Shots: localhost-8954__phone__fold.png, localhost-8954__phone__scroll025.png, localhost-8954__phone__scroll050.png, localhost-8954__phone__scroll075.png, localhost-8954__phone__scroll100.png, localhost-8954__phone__full.png, localhost-8954__phone__reduced-motion.png

## http://localhost:8954/ — desktop
Load 547ms · frames p50 16.7ms p95 16.8ms · fonts Schibsted / Gloock · canvases 0
- no issues
Shots: localhost-8954__desktop__fold.png, localhost-8954__desktop__scroll025.png, localhost-8954__desktop__scroll050.png, localhost-8954__desktop__scroll075.png, localhost-8954__desktop__scroll100.png, localhost-8954__desktop__full.png, localhost-8954__desktop__reduced-motion.png

## http://localhost:8954/ — lighthouse-mobile
Lighthouse: {"performance":99,"accessibility":100,"best-practices":100,"seo":66} LCP 2.2 s CLS 0 TBT 0 ms weight Total size was 265 KiB
- no issues

Human/AI review still required: look at every *__fold.png and *__scroll*.png. This gate catches breakage, not blandness.