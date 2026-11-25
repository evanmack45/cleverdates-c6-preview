# Visual QA gate

Result: PASS (no P0)

## http://127.0.0.1:8947/ — phone
Load 827ms · frames p50 16.7ms p95 16.7ms · fonts Schibsted / Gloock · canvases 0
- no issues
Shots: 127-0-0-1-8947__phone__fold.png, 127-0-0-1-8947__phone__scroll025.png, 127-0-0-1-8947__phone__scroll050.png, 127-0-0-1-8947__phone__scroll075.png, 127-0-0-1-8947__phone__scroll100.png, 127-0-0-1-8947__phone__full.png, 127-0-0-1-8947__phone__reduced-motion.png

## http://127.0.0.1:8947/ — desktop
Load 545ms · frames p50 16.7ms p95 16.8ms · fonts Schibsted / Gloock · canvases 0
- no issues
Shots: 127-0-0-1-8947__desktop__fold.png, 127-0-0-1-8947__desktop__scroll025.png, 127-0-0-1-8947__desktop__scroll050.png, 127-0-0-1-8947__desktop__scroll075.png, 127-0-0-1-8947__desktop__scroll100.png, 127-0-0-1-8947__desktop__full.png, 127-0-0-1-8947__desktop__reduced-motion.png

## http://127.0.0.1:8947/ — lighthouse-mobile
Lighthouse: {"performance":98,"accessibility":100,"best-practices":100,"seo":66} LCP 2.3 s CLS 0 TBT 0 ms weight Total size was 278 KiB
- no issues

Human/AI review still required: look at every *__fold.png and *__scroll*.png. This gate catches breakage, not blandness.