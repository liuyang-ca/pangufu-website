# Copy vetting, 2026-10-28 (Phase 6 of `docs/plan-us-practice-pages.md`)

Checked against the plan's Copy rules. Read dates are 2026-10-28. **French and Spanish rows: native review pending** (every `fr/` and `es/` row below carries it in the outcome column). No Google search was run (Phase 2's search step was skipped: no browser); the page copy rests on the app listings and the official pages below.

Outcome key: `keep` (passes), `changed` (new text this phase), `flagged` (kept, needs the developer).

## Facts table

| ID | Fact | Source | Read |
| --- | --- | --- | --- |
| F1 | Canadian test: 20 questions (multiple choice or true/false), English or French, 45 minutes, at least 15 right to pass, 3 chances; based on Discover Canada | canada.ca `/en/immigration-refugees-citizenship/services/canadian-citizenship/test/study.html` (and `/test/online.html` for the 45-minute timer) | 2026-10-28 |
| F2 | Official Canadian study guide is *Discover Canada*, free on canada.ca | same page; link on the CA pages | 2026-10-28 |
| F3 | US 2025 civics test: oral, officer asks up to 20 of 128 questions, 12 right to pass, stops at 12 right or 9 wrong; applies to Form N-400 filed on or after October 20, 2025 | uscis.gov `/citizenship-resource-center/naturalization-test-and-study-resources/2025-civics-test` (last reviewed 09/17/2025) | 2026-10-28 |
| F4 | 65/20 rule: age 65+ and 20+ years as a lawful permanent resident may study only the 20 questions marked with an asterisk; officer asks 10, 6 right pass. **Traced to uscis.gov this phase; Phase 2 had no source.** | uscis.gov 128 Civics Questions and Answers, form M-1778 (09/25), p. 1, `/sites/default/files/document/questions-and-answers/2025-Civics-Test-128-Questions-and-Answers.pdf` | 2026-10-28 |
| F5 | US English test: read aloud 1 of 3 sentences, write 1 of 3 correctly | uscis.gov `/citizenship/find-study-materials-and-resources/study-for-the-test` | 2026-10-28 |
| F6 | US Citizen Test Coach: 128 questions in English or Spanish, spoken mock interview, reading and writing practice; free: all study, 2 mock quizzes, 1 interview, 1 reading and 1 writing round; one purchase, no subscription; no account, ads or data collected | `../uscitizencoach/docs/app-store-listing.md` (2026-10-27); `docs/privacy.html` (effective October 28, 2026) | 2026-10-28 |
| F7 | Canada Citizenship Test Coach: 11 chapters plus province or territory, English and French, mock tests 20 questions / 45 minutes / 15 to pass, first 3 chapters and 2 mock tests free, one purchase, no subscription | `../citizencoach/docs/app-store-listing.md` (2026-10-27) | 2026-10-28 |
| F8 | Blackjack & Video Poker Coach: basic strategy free; Hi-Lo counting and video poker in one purchase; hints, right play and reason after a miss; accuracy by hard, soft and pair hands; practice only, no real money, no account, ads or data collected | `../cardtrainer/docs/app-store-listing.md`; `docs/privacy.html` (19 October 2026) | 2026-10-28 |
| F9 | Question counts on the pages: CA 27 / 28 / 112 (167 in the quiz), US 120 (128 minus 8 local or current) split 64 / 46 / 10 | generators from the app banks (vetted in the app repos) | 2026-10-28 |
| F10 | No data collected, no ads, no tracking, no account; data stays on the device | the four privacy policies (`../<repo>/docs/privacy.html`) | 2026-10-28 |
| F11 | All three apps "Coming soon"; iPhone and iPad | developer status (README / plan); listings | 2026-10-28 |

Unsourced before this phase and now sourced: the 65/20 line (F4) and the 12-right-or-9-wrong stop rule (F3). Added for accuracy: the "Form N-400 filed on or after October 20, 2025" scope line (F3), which tells earlier filers their interview may use the older test. The 65/20 line is **kept and reworded to match the source** (asterisk, 10 asked, 6 pass).

## Changed headline copy (old → new)

See the table in the Phase 6 report; the same data sits in `Changed lines` below.

### Changed lines

| Page | Item | Old | New |
| --- | --- | --- | --- |
| `blackjack-video-poker-coach/index.html` | title | Blackjack & Video Poker Coach: Strategy Practice App \| PANGUFU (62) | Blackjack & Video Poker Coach: Strategy Practice App (52) |
| `blackjack-video-poker-coach/index.html` | meta description | Blackjack & Video Poker Coach is an iPhone and iPad app for practising blackjack basic strategy, Hi-Lo card counting and video poker holds. Practice only, no real money. (169) | Practice blackjack basic strategy, Hi-Lo card counting and video poker holds on iPhone and iPad. Free to start. Practice only, no real money. (141) |
| `blackjack-video-poker-coach/index.html` | hero / first line | A thoughtful coach for card game practice. Learn blackjack basic strategy, then go further with card counting and video poker. (126) | Learn blackjack basic strategy one hand at a time, then practise Hi-Lo card counting and video poker holds. Basic strategy is free, and nothing is played for real money. (169) |
| `blackjack-video-poker-coach/privacy.html` | meta description |  (0) | Blackjack & Video Poker Coach privacy policy: no data collected, no ads or tracking, settings and stats stay on your device. Practice only. (139) |
| `canada-citizenship-test/history/index.html` | title | Canada's History: 112 Citizenship Test Practice Questions \| PANGUFU (67) | Canadian Citizenship Test: Canada’s History (43) |
| `canada-citizenship-test/index.html` | meta description | Free Canadian citizenship practice test for 2026: how the real test works (20 questions, 45 minutes, 15 to pass) and a study app in English and French. Independent practice. (173) | Free Canadian citizenship practice test: 20 questions, 45 minutes, 15 to pass, as on the real test. In English and French, no account needed. (141) |
| `canada-citizenship-test/index.html` | hero / first line | Practise for the Canadian citizenship test with questions written for study. Nothing to sign up for and nothing to pay. (119) | Take a free 20-question practice test in 45 minutes: you need 15 correct answers to pass, as on the real test. Nothing to sign up for and nothing to pay. (153) |
| `canada-citizenship-test/rights/index.html` | title | Rights and Responsibilities of Citizenship: 27 Citizenship Test Practice Questions \| PANGUFU (92) | Canadian Citizenship Test: Rights and Responsibilities (54) |
| `canada-citizenship-test/who-we-are/index.html` | title | Who We Are: 28 Citizenship Test Practice Questions \| PANGUFU (60) | Canadian Citizenship Test: Who We Are (37) |
| `citizen-coach-privacy/privacy.html` | title | Canada Citizenship Test Coach Privacy Policy / Politique de confidentialité de Coach Test Citoyenneté Canada (108) | Canada Citizenship Test Coach Privacy Policy (44) |
| `citizen-coach-privacy/privacy.html` | meta description |  (0) | Privacy policy for Canada Citizenship Test Coach, in English and French: no data collected, progress stays on your device, one-time Apple purchase. (147) |
| `fr/examen-citoyennete-canadienne/droits/index.html` | title | Les droits et responsabilités liés à la citoyenneté : 27 questions d’examen de citoyenneté \| PANGUFU (100) | Examen de citoyenneté canadienne : droits et responsabilités (60) |
| `fr/examen-citoyennete-canadienne/droits/index.html` | meta description | 27 questions de pratique gratuites sur « Les droits et responsabilités liés à la citoyenneté » pour l’examen de citoyenneté, avec réponses et explications. Sans compte. Pratique indépendante. (191) | 27 questions de pratique gratuites sur « droits et responsabilités » pour l’examen de citoyenneté, avec réponses et explications. Sans compte. (142) |
| `fr/examen-citoyennete-canadienne/histoire/index.html` | title | L’histoire du Canada : 112 questions d’examen de citoyenneté \| PANGUFU (70) | Examen de citoyenneté canadienne : histoire du Canada (53) |
| `fr/examen-citoyennete-canadienne/histoire/index.html` | meta description | 112 questions de pratique gratuites sur « L’histoire du Canada » pour l’examen de citoyenneté, avec réponses et explications. Sans compte. Pratique indépendante. (161) | 112 questions de pratique gratuites sur « histoire du Canada » pour l’examen de citoyenneté, avec réponses et explications. Sans compte. (136) |
| `fr/examen-citoyennete-canadienne/index.html` | title | Examen de citoyenneté canadienne gratuit : test pratique (2026) \| PANGUFU (73) | Examen de citoyenneté canadienne gratuit : test pratique (56) |
| `fr/examen-citoyennete-canadienne/index.html` | meta description | Test pratique gratuit pour l’examen de citoyenneté canadienne 2026 : 20 questions, 45 minutes, 15 bonnes réponses pour réussir. Pratique indépendante. (150) | Test pratique gratuit de l’examen de citoyenneté canadienne : 20 questions, 45 minutes, 15 bonnes réponses. Sans compte, en français et en anglais. (147) |
| `fr/examen-citoyennete-canadienne/index.html` | hero / first line | Pratiquez pour l’examen de citoyenneté canadienne avec des questions rédigées pour l’étude. Rien à créer, rien à payer. (119) | Faites un test pratique gratuit de 20 questions en 45 minutes : il faut 15 bonnes réponses pour réussir, comme à l’examen réel. Rien à créer, rien à payer. (155) |
| `fr/examen-citoyennete-canadienne/qui-nous-sommes/index.html` | title | Qui sommes-nous, les Canadiens ? : 28 questions d’examen de citoyenneté \| PANGUFU (81) | Examen de citoyenneté canadienne : qui sommes-nous ? (52) |
| `fr/examen-citoyennete-canadienne/qui-nous-sommes/index.html` | meta description | 28 questions de pratique gratuites sur « Qui sommes-nous, les Canadiens ? » pour l’examen de citoyenneté, avec réponses et explications. Sans compte. Pratique indépendante. (172) | 28 questions de pratique gratuites sur « qui sommes-nous ? » pour l’examen de citoyenneté, avec réponses et explications. Sans compte. (134) |
| `index.html` | title | PANGUFU — Small apps. Thoughtfully made. (40) | PANGUFU: iPhone & iPad Apps for Learning and Practice (53) |
| `index.html` | meta description | PANGUFU SOLUTION LTD. builds focused iPhone and iPad apps for learning and practice: Canada Citizenship Test Coach, US Citizen Test Coach and Blackjack & Video Poker Coach. (172) | PANGUFU builds focused iPhone and iPad apps for learning and practice: Canadian and US citizenship test coaches and a blackjack and video poker coach. (150) |
| `index.html` | hero / first line | PANGUFU builds focused apps for learning, practice and everyday life. We care about clear design, useful feedback and the small details that make an app feel natural to use. Our goal is simple: help you build skills, explore ideas and make steady progress at your own pace. (273) | PANGUFU builds focused iPhone and iPad apps for learning and practice. We care about clear design, useful feedback and the small details that make an app feel natural to use. Our apps today help people prepare for the Canadian and US citizenship tests and practise blackjack and video poker strategy, with more to come. (319) |
| `purrcade/privacy.html` | meta description |  (0) | Purrcade: Games for Cats privacy policy: no data collected, no ads or tracking, settings stay on your device, one-time unlock through Apple. (140) |
| `us-citizenship-test/index.html` | hero / first line | Practice the 2025 naturalization civics test with 120 questions, answers and explanations. Nothing to sign up for and nothing to pay. (133) | Practice the 2025 naturalization civics test with 120 questions, answers, and explanations. Nothing to sign up for and nothing to pay. (134) |
| `uscitizencoach-privacy/privacy.html` | title | US Citizen Test Coach Privacy Policy / Política de privacidad de Coach Examen Ciudadanía USA (92) | US Citizen Test Coach Privacy Policy (36) |
| `uscitizencoach-privacy/privacy.html` | meta description |  (0) | Privacy policy for US Citizen Test Coach, in English and Spanish: no data collected, speech recognition runs on your device, progress stays on it. (146) |

## Shared strings (site chrome, on 6 or more pages)

| Text | Rule checks | Outcome | Source |
| --- | --- | --- | --- |
| a: All apps | ok | keep | own copy, no fact |
| a: Blackjack & Video Poker Coach privacy policy | ok | keep | F10 |
| a: Canada Citizenship Test Coach privacy policy | ok | keep | F10 |
| a: English | ok | keep | own copy, no fact |
| a: PANGUFU | ok | keep | own copy, no fact |
| a: Privacy policy ↗ | ok | keep | own copy, no fact |
| a: Support | ok | keep | own copy, no fact |
| a: support@pangufu.ca ↗ | ok | keep | own copy, no fact |
| h2: We’re here to help. | ok | keep | own copy, no fact |
| p: For app support or general enquiries, send us a note. | ok | keep | own copy, no fact |
| p: Inside the app | ok | keep | own copy, no fact |
| p: Study · iPhone & iPad | ok | keep | own copy, no fact |
| p: Support & enquiries | ok | keep | own copy, no fact |
| p: The study app | ok | keep | own copy, no fact |
| span: © 2026 PANGUFU | ok | keep | own copy, no fact |
| strong: PANGUFU SOLUTION LTD. | ok | keep | own copy, no fact |

## Pages

### `blackjack-video-poker-coach/index.html` (en)

| Text | Rule checks | Outcome | Source |
| --- | --- | --- | --- |
| title: Blackjack & Video Poker Coach: Strategy Practice App | ≤60: 52 ok | changed | own copy; facts per facts table |
| desc: Practice blackjack basic strategy, Hi-Lo card counting and video poker holds on iPhone and iPad. Free to start. Practice only, no real money. | 120–155: 141 ok | changed | own copy; facts per facts table |
| p: Learn · iPhone & iPad | ok | keep | own copy, no fact |
| h1: Blackjack & Video Poker Coach | ok | keep | own copy; facts per facts table |
| p: Learn blackjack basic strategy one hand at a time, then practise Hi-Lo card counting and video poker holds. Basic strategy is free, and nothing is played for real money. | ok | changed | F8 |
| p: The app | ok | keep | own copy, no fact |
| h2: Practise the right play. | ok | keep | own copy, no fact |
| p: Practice only, with no real money or prizes. | ok | keep | own copy, no fact |
| alt: Blackjack and card coach icon | ok | keep | screenshot file, docs/assets.md |
| h3: Blackjack & Video Poker Coach | ok | keep | own copy, no fact |
| p: Practice blackjack strategy and card counting, then learn video poker holds. Practice only, with no real money or prizes. | ok | keep | own copy, no fact |
| li: Train with hints first, then without them | ok | changed | own copy, no fact |
| li: See the right play and why after a miss | ok | keep | own copy, no fact |
| li: Track accuracy across hard, soft and pair hands | ok | keep | own copy, no fact |
| p: Free to start. Blackjack basic strategy is free; one purchase unlocks card counting and video poker. | ok | keep | F8 |
| a: Blackjack & Video Poker Coach privacy policy ↗ | ok | keep | own copy, no fact |
| alt: Captioned App Store image: No Ads. No Subscription. Basic strategy is free, above the Blackjack practice screen with a hint for the hand | ok | keep | screenshot file, docs/assets.md |
| p: Two more ways to practise | ok | keep | own copy, no fact |
| h2: Go beyond the basics. | ok | keep | own copy, no fact |
| p: Hi-Lo counting and video poker, in one purchase. | ok | changed | F8 |
| p: Hi-Lo counting | ok | keep | own copy, no fact |
| h3: Keep the count | ok | keep | own copy, no fact |
| p: Work through card values, running count and true count, then practise deviations that change the usual play. | ok | keep | own copy, no fact |
| span: Unlocked with one purchase | ok | keep | F8 |
| alt: Captioned App Store image: Learn Hi-Lo Counting, step by step, with Unlock All, above the card values and the counting lessons | ok | keep | screenshot file, docs/assets.md |
| p: Video poker | ok | keep | own copy, no fact |
| h3: Find the best hold | empty praise | keep | own copy, no fact |
| p: Practise Jacks or Better and Deuces Wild. Compare your hold with the best one for the hand. | empty praise | keep | own copy, no fact |
| alt: Captioned App Store image: Perfect Video Poker Holds, one unlock for counting and video poker, above feedback comparing a hold with the best hold | empty praise | keep | screenshot file, docs/assets.md |
| p: A focused practice tool | ok | keep | own copy, no fact |
| h2: No account. No ads.No data collected. | ok | changed | own copy, no fact |
| p: Start with free blackjack basic strategy. One purchase adds the card-counting and video-poker trainers, with no subscription. | ok | keep | F8 |
| p: Your settings, practice stats and missed hands stay on your device. | ok | changed | own copy, no fact |

### `blackjack-video-poker-coach/privacy.html` (en)

| Text | Rule checks | Outcome | Source |
| --- | --- | --- | --- |
| title: Blackjack & Video Poker Coach Privacy Policy | ≤60: 44 ok | keep | own copy; facts per facts table |
| desc: Blackjack & Video Poker Coach privacy policy: no data collected, no ads or tracking, settings and stats stay on your device. Practice only. | 120–155: 139 ok | changed | own copy; facts per facts table |
| h1: Blackjack & Video Poker Coach — Privacy Policy | ok | keep | own copy; facts per facts table |
| p: Last updated: 19 October 2026 | ok | keep | own copy, no fact |
| p: Blackjack & Video Poker Coach does not collect, store or share any personal data. It has no ads, no analytics, no tracking and no account. | ok | keep | own copy, no fact |
| h2: What stays on your device | ok | keep | own copy, no fact |
| p: Your settings (rules, look, sound), your practice stats and your list of missed hands are saved on the device only. They are never sent anywhere and are removed when you delete the app. | ok | keep | own copy, no fact |
| h2: Purchases | ok | keep | F8 |
| p: The one-time unlock is sold and processed by Apple through the App Store. Blackjack & Video Poker Coach never sees your payment details or Apple Account. Apple's handling of purchases is covered by Apple's privacy policy. | ok | keep | F8 |
| h2: Practice only | ok | keep | own copy, no fact |
| p: Blackjack & Video Poker Coach is a practice tool. It uses no real money and has no real-money play. | ok | keep | own copy, no fact |
| h2: Children | ok | keep | own copy, no fact |
| p: Blackjack & Video Poker Coach collects no data from anyone, including children. | ok | keep | own copy, no fact |
| h2: Changes | ok | keep | own copy, no fact |
| p: If this policy changes, the new version is posted on this page with a new date. | ok | keep | own copy, no fact |
| h2: Contact | ok | keep | own copy, no fact |
| p: Questions: support@pangufu.ca. | ok | keep | own copy, no fact |

### `canada-citizenship-test/history/index.html` (en-CA)

| Text | Rule checks | Outcome | Source |
| --- | --- | --- | --- |
| title: Canadian Citizenship Test: Canada’s History | ≤60: 43 ok | changed | own copy; facts per facts table |
| desc: 112 free citizenship test practice questions on Canada's History, with answers and explanations. No account. Independent practice. | 120–155: 130 ok | keep; flagged: straight apostrophe comes from the app bank section title (fix in `../citizencoach`) | own copy; facts per facts table |
| a: Français | ok | keep | own copy, no fact |
| p: Free chapter 3 | ok | keep | F7 |
| h1: Canada's History: Citizenship Test Practice Questions | ok | keep; flagged: straight apostrophe comes from the app bank section title (fix in `../citizencoach`) | own copy; facts per facts table |
| p: 112 free practice questions on this chapter of the study guide. Pick an answer in your head, then open “Show answer” to check it and read the explanation. | ok | keep | F7 |
| p: Read this chapter in Discover Canada ↗ | ok | keep | own copy, no fact |
| p: Independent practice. Not affiliated with IRCC or the Government of Canada. The official study guide, Discover Canada, is free on canada.ca. Read it first; this page does not replace it. | ok | keep | F7 |
| h2: More practice by chapter | ok | keep | own copy, no fact |
| p: Take the timed 20-question practice test | ok | keep | F1 |
| li: Rights and Responsibilities of Citizenship (27 questions) | ok | keep | own copy, no fact |
| li: Who We Are (28 questions) | ok | keep | own copy, no fact |
| h2: Study every chapter, in English or French. | ok | keep | own copy, no fact |
| alt: Canada Citizenship Test Coach icon | ok | keep | screenshot file, docs/assets.md |
| h3: Canada Citizenship Test Coach | ok | keep | own copy, no fact |
| p: Study for the Canadian citizenship test one chapter at a time, then take timed mock tests with the real test’s pass mark. | ok | keep | own copy, no fact |
| li: All 11 chapters of the guide, plus your province or territory | ok | keep | own copy, no fact |
| li: Study and listen in English or French | ok | keep | own copy, no fact |
| li: Timed mock tests of 20 questions in 45 minutes, with every answer explained | ok | keep | F1 |
| p: Free to start. The first three chapters and two mock tests are free; one purchase unlocks everything, with no subscription. | ok | keep | F7 |
| alt: Captioned App Store image: Read or Listen, study in English or French, above the Rights chapter in English and French | ok | keep | screenshot file, docs/assets.md |
| h2: Practise, then see where you stand. | ok | keep | own copy, no fact |
| p: A quiz after each section and a readiness view for every chapter. | ok | keep | own copy, no fact |
| p: Section quizzes | ok | keep | own copy, no fact |
| h3: Learn from every answer | ok | keep | own copy, no fact |
| p: A quiz after each section, with a short explanation for every answer. | ok | keep | own copy, no fact |
| alt: Captioned App Store image: Learn From Every Answer, explanations for right and wrong answers, above a quiz question with the wrong choice in red and the right answer in green | ok | keep | screenshot file, docs/assets.md |
| p: Readiness by chapter | ok | keep | own copy, no fact |
| h3: Know what to review | ok | keep | own copy, no fact |
| p: See which parts of the guide you already know, chapter by chapter. | ok | keep | own copy, no fact |
| alt: Captioned App Store image: No Ads. No Subscription. Start free, no account needed, above the Home screen showing progress by chapter | ok | keep | screenshot file, docs/assets.md |

### `canada-citizenship-test/index.html` (en-CA)

| Text | Rule checks | Outcome | Source |
| --- | --- | --- | --- |
| title: Free Canadian Citizenship Practice Test (2026) \| PANGUFU | ≤60: 56 ok | keep | own copy; facts per facts table |
| desc: Free Canadian citizenship practice test: 20 questions, 45 minutes, 15 to pass, as on the real test. In English and French, no account needed. | 120–155: 141 ok | changed | own copy; facts per facts table |
| a: Français | ok | keep | own copy, no fact |
| p: Free · No account · No ads | ok | keep | F7 |
| h1: Free Canadian Citizenship Practice Test (2026) | ok | keep | own copy; facts per facts table |
| p: Take a free 20-question practice test in 45 minutes: you need 15 correct answers to pass, as on the real test. Nothing to sign up for and nothing to pay. | ok | changed | F1 |
| p: Independent practice. Not affiliated with IRCC or the Government of Canada. The official study guide, Discover Canada, is free on canada.ca. Read it first; this page does not replace it. | ok | keep | F7 |
| h2: How the real test works | ok | keep | own copy, no fact |
| li: 20 questions | ok | keep | F1 |
| li: 45 minutes | ok | keep | F1 |
| li: You need 15 correct answers to pass | ok | keep | F1 |
| li: The questions are based on the Discover Canada guide | ok | keep | own copy, no fact |
| h2: Practice test | ok | keep | own copy, no fact |
| p: Start with a quick 5-question quiz, or take the full test: 20 random questions from the three free chapters in 45 minutes. You need 15 correct to pass, like the real test. | ok | keep | F1 |
| p: The practice test requires JavaScript. The sample questions and chapter pages work without it. | ok | changed | own copy, no fact |
| button: Start quick quiz: 5 questions | verb first ok | changed | own copy, no fact |
| button: Start full test: 20 questions, 45 minutes | verb first ok | changed | F1 |
| p: · Time left: 45:00 | ok | keep | F1 |
| h2: Sample questions | ok | keep | own copy, no fact |
| p: Try these ten with no timer. Open “Show answer” to check each one. | ok | keep | own copy, no fact |
| h2: Practice by chapter | ok | keep | own copy, no fact |
| p: Every question in each free chapter, with answers and explanations. | ok | keep | F7 |
| li: Rights and Responsibilities of Citizenship (27 questions) | ok | keep | own copy, no fact |
| li: Who We Are (28 questions) | ok | keep | own copy, no fact |
| li: Canada's History (112 questions) | ok | keep; flagged: straight apostrophe comes from the app bank section title (fix in `../citizencoach`) | own copy, no fact |
| h2: Study every chapter, in English or French. | ok | keep | own copy, no fact |
| alt: Canada Citizenship Test Coach icon | ok | keep | screenshot file, docs/assets.md |
| h3: Canada Citizenship Test Coach | ok | keep | own copy, no fact |
| p: Study for the Canadian citizenship test one chapter at a time, then take timed mock tests with the real test’s pass mark. | ok | keep | own copy, no fact |
| li: All 11 chapters of the guide, plus your province or territory | ok | keep | own copy, no fact |
| li: Study and listen in English or French | ok | keep | own copy, no fact |
| li: Timed mock tests of 20 questions in 45 minutes, with every answer explained | ok | keep | F1 |
| p: Free to start. The first three chapters and two mock tests are free; one purchase unlocks everything, with no subscription. | ok | keep | F7 |
| alt: Captioned App Store image: Read or Listen, study in English or French, above the Rights chapter in English and French | ok | keep | screenshot file, docs/assets.md |
| h2: Practise, then see where you stand. | ok | keep | own copy, no fact |
| p: A quiz after each section and a readiness view for every chapter. | ok | keep | own copy, no fact |
| p: Section quizzes | ok | keep | own copy, no fact |
| h3: Learn from every answer | ok | keep | own copy, no fact |
| p: A quiz after each section, with a short explanation for every answer. | ok | keep | own copy, no fact |
| alt: Captioned App Store image: Learn From Every Answer, explanations for right and wrong answers, above a quiz question with the wrong choice in red and the right answer in green | ok | keep | screenshot file, docs/assets.md |
| p: Readiness by chapter | ok | keep | own copy, no fact |
| h3: Know what to review | ok | keep | own copy, no fact |
| p: See which parts of the guide you already know, chapter by chapter. | ok | keep | own copy, no fact |
| alt: Captioned App Store image: No Ads. No Subscription. Start free, no account needed, above the Home screen showing progress by chapter | ok | keep | screenshot file, docs/assets.md |

### `canada-citizenship-test/rights/index.html` (en-CA)

| Text | Rule checks | Outcome | Source |
| --- | --- | --- | --- |
| title: Canadian Citizenship Test: Rights and Responsibilities | ≤60: 54 ok | changed | own copy; facts per facts table |
| desc: 27 free citizenship test practice questions on Rights and Responsibilities of Citizenship, with answers and explanations. No account. Independent practice. | 120–155: 155 ok | keep | own copy; facts per facts table |
| a: Français | ok | keep | own copy, no fact |
| p: Free chapter 1 | ok | keep | F7 |
| h1: Rights and Responsibilities of Citizenship: Citizenship Test Practice Questions | ok | keep | own copy; facts per facts table |
| p: 27 free practice questions on this chapter of the study guide. Pick an answer in your head, then open “Show answer” to check it and read the explanation. | ok | keep | F7 |
| p: Read this chapter in Discover Canada ↗ | ok | keep | own copy, no fact |
| p: Independent practice. Not affiliated with IRCC or the Government of Canada. The official study guide, Discover Canada, is free on canada.ca. Read it first; this page does not replace it. | ok | keep | F7 |
| h2: More practice by chapter | ok | keep | own copy, no fact |
| p: Take the timed 20-question practice test | ok | keep | F1 |
| li: Who We Are (28 questions) | ok | keep | own copy, no fact |
| li: Canada's History (112 questions) | ok | keep; flagged: straight apostrophe comes from the app bank section title (fix in `../citizencoach`) | own copy, no fact |
| h2: Study every chapter, in English or French. | ok | keep | own copy, no fact |
| alt: Canada Citizenship Test Coach icon | ok | keep | screenshot file, docs/assets.md |
| h3: Canada Citizenship Test Coach | ok | keep | own copy, no fact |
| p: Study for the Canadian citizenship test one chapter at a time, then take timed mock tests with the real test’s pass mark. | ok | keep | own copy, no fact |
| li: All 11 chapters of the guide, plus your province or territory | ok | keep | own copy, no fact |
| li: Study and listen in English or French | ok | keep | own copy, no fact |
| li: Timed mock tests of 20 questions in 45 minutes, with every answer explained | ok | keep | F1 |
| p: Free to start. The first three chapters and two mock tests are free; one purchase unlocks everything, with no subscription. | ok | keep | F7 |
| alt: Captioned App Store image: Read or Listen, study in English or French, above the Rights chapter in English and French | ok | keep | screenshot file, docs/assets.md |
| h2: Practise, then see where you stand. | ok | keep | own copy, no fact |
| p: A quiz after each section and a readiness view for every chapter. | ok | keep | own copy, no fact |
| p: Section quizzes | ok | keep | own copy, no fact |
| h3: Learn from every answer | ok | keep | own copy, no fact |
| p: A quiz after each section, with a short explanation for every answer. | ok | keep | own copy, no fact |
| alt: Captioned App Store image: Learn From Every Answer, explanations for right and wrong answers, above a quiz question with the wrong choice in red and the right answer in green | ok | keep | screenshot file, docs/assets.md |
| p: Readiness by chapter | ok | keep | own copy, no fact |
| h3: Know what to review | ok | keep | own copy, no fact |
| p: See which parts of the guide you already know, chapter by chapter. | ok | keep | own copy, no fact |
| alt: Captioned App Store image: No Ads. No Subscription. Start free, no account needed, above the Home screen showing progress by chapter | ok | keep | screenshot file, docs/assets.md |

### `canada-citizenship-test/who-we-are/index.html` (en-CA)

| Text | Rule checks | Outcome | Source |
| --- | --- | --- | --- |
| title: Canadian Citizenship Test: Who We Are | ≤60: 37 ok | changed | own copy; facts per facts table |
| desc: 28 free citizenship test practice questions on Who We Are, with answers and explanations. No account. Independent practice. | 120–155: 123 ok | keep | own copy; facts per facts table |
| a: Français | ok | keep | own copy, no fact |
| p: Free chapter 2 | ok | keep | F7 |
| h1: Who We Are: Citizenship Test Practice Questions | ok | keep | own copy; facts per facts table |
| p: 28 free practice questions on this chapter of the study guide. Pick an answer in your head, then open “Show answer” to check it and read the explanation. | ok | keep | F7 |
| p: Read this chapter in Discover Canada ↗ | ok | keep | own copy, no fact |
| p: Independent practice. Not affiliated with IRCC or the Government of Canada. The official study guide, Discover Canada, is free on canada.ca. Read it first; this page does not replace it. | ok | keep | F7 |
| h2: More practice by chapter | ok | keep | own copy, no fact |
| p: Take the timed 20-question practice test | ok | keep | F1 |
| li: Rights and Responsibilities of Citizenship (27 questions) | ok | keep | own copy, no fact |
| li: Canada's History (112 questions) | ok | keep; flagged: straight apostrophe comes from the app bank section title (fix in `../citizencoach`) | own copy, no fact |
| h2: Study every chapter, in English or French. | ok | keep | own copy, no fact |
| alt: Canada Citizenship Test Coach icon | ok | keep | screenshot file, docs/assets.md |
| h3: Canada Citizenship Test Coach | ok | keep | own copy, no fact |
| p: Study for the Canadian citizenship test one chapter at a time, then take timed mock tests with the real test’s pass mark. | ok | keep | own copy, no fact |
| li: All 11 chapters of the guide, plus your province or territory | ok | keep | own copy, no fact |
| li: Study and listen in English or French | ok | keep | own copy, no fact |
| li: Timed mock tests of 20 questions in 45 minutes, with every answer explained | ok | keep | F1 |
| p: Free to start. The first three chapters and two mock tests are free; one purchase unlocks everything, with no subscription. | ok | keep | F7 |
| alt: Captioned App Store image: Read or Listen, study in English or French, above the Rights chapter in English and French | ok | keep | screenshot file, docs/assets.md |
| h2: Practise, then see where you stand. | ok | keep | own copy, no fact |
| p: A quiz after each section and a readiness view for every chapter. | ok | keep | own copy, no fact |
| p: Section quizzes | ok | keep | own copy, no fact |
| h3: Learn from every answer | ok | keep | own copy, no fact |
| p: A quiz after each section, with a short explanation for every answer. | ok | keep | own copy, no fact |
| alt: Captioned App Store image: Learn From Every Answer, explanations for right and wrong answers, above a quiz question with the wrong choice in red and the right answer in green | ok | keep | screenshot file, docs/assets.md |
| p: Readiness by chapter | ok | keep | own copy, no fact |
| h3: Know what to review | ok | keep | own copy, no fact |
| p: See which parts of the guide you already know, chapter by chapter. | ok | keep | own copy, no fact |
| alt: Captioned App Store image: No Ads. No Subscription. Start free, no account needed, above the Home screen showing progress by chapter | ok | keep | screenshot file, docs/assets.md |

### `citizen-coach-privacy/privacy.html` (en)

| Text | Rule checks | Outcome | Source |
| --- | --- | --- | --- |
| title: Canada Citizenship Test Coach Privacy Policy | ≤60: 44 ok | changed | own copy; facts per facts table |
| desc: Privacy policy for Canada Citizenship Test Coach, in English and French: no data collected, progress stays on your device, one-time Apple purchase. | 120–155: 147 ok | changed | own copy; facts per facts table |

### `es/examen-ciudadania-estados-unidos/gobierno/index.html` (es-US)

| Text | Rule checks | Outcome | Source |
| --- | --- | --- | --- |
| title: Gobierno estadounidense: 64 preguntas de ciudadanía | ≤60: 51 ok | keep; native review pending | own copy; facts per facts table |
| desc: 64 preguntas de práctica del examen de ciudadanía de EE. UU. sobre el gobierno estadounidense, con respuestas y explicaciones. Gratis y sin cuenta. | 120–155: 147 ok | keep; native review pending | own copy; facts per facts table |
| a: Todas las apps | ok | keep; native review pending | own copy, no fact |
| a: Soporte | ok | keep; native review pending | own copy, no fact |
| p: Sección gratis | ok | keep; native review pending | F6 |
| h1: Gobierno estadounidense: preguntas de práctica del examen de ciudadanía de EE. UU. | ok | keep; native review pending | own copy; facts per facts table |
| p: 64 preguntas de práctica de esta parte del examen de educación cívica de 2025. Responda en voz alta y luego abra “Ver respuesta” para comprobarla y leer la explicación. | ok | keep; native review pending | own copy, no fact |
| p: Práctica independiente. No está afiliada a USCIS ni al gobierno de EE. UU. Las preguntas oficiales y la guía de estudio son gratuitas en uscis.gov (en inglés). Léalas primero; esta página no las sustituye. | ok | keep; native review pending | F6 |
| p: Ocho preguntas no aparecen porque la respuesta depende de dónde vive usted o de quién ocupa el cargo ahora: su senador, su representante, su gobernador y la capital de su estado, y el actual Presidente de la Cámara de Representantes, el Presidente, el Vicepresidente y el presidente de la Corte Suprema. La app le pregunta su estado y muestra a los funcionarios actuales. | ok | keep; native review pending | own copy, no fact |
| h2: Más práctica por sección | ok | keep; native review pending | own copy, no fact |
| p: Haga el examen de práctica de 20 preguntas | ok | keep; native review pending | F3/F4/F5 |
| li: Historia estadounidense (46 preguntas) | ok | keep; native review pending | own copy, no fact |
| li: Símbolos y días feriados (10 preguntas) | ok | keep; native review pending | own copy, no fact |
| p: La app de estudio | ok | keep; native review pending | own copy, no fact |
| h2: Estudie las 128 preguntas, en español o en inglés. | ok | keep; native review pending | F3/F4/F5 |
| alt: Ícono de Coach Examen Ciudadanía USA | ok | keep; native review pending | screenshot file, docs/assets.md |
| p: Estudio · iPhone y iPad | ok | keep; native review pending | own copy, no fact |
| h3: Coach Examen Ciudadanía USA | ok | keep; native review pending | own copy, no fact |
| p: Estudie para el examen de naturalización de EE. UU. de 2025 con las preguntas de educación cívica, una entrevista de práctica hablada y práctica de lectura y escritura en inglés. Sin cuenta ni anuncios. | ok | keep; native review pending | own copy, no fact |
| li: Las 128 preguntas de educación cívica con sus respuestas aceptadas, en español o en inglés | ok | keep; native review pending | F3/F4/F5 |
| li: Una entrevista de práctica hablada que escucha sus respuestas | ok | keep; native review pending | own copy, no fact |
| li: Práctica de lectura y escritura en inglés | ok | keep; native review pending | own copy, no fact |
| p: Gratis para empezar. Todo el estudio es gratis, con 2 cuestionarios de práctica, 1 entrevista hablada, 1 ronda de lectura y 1 ronda de escritura; una compra desbloquea simulacros ilimitados, sin suscripción. | ok | keep; native review pending | F6 |
| a: Política de privacidad ↗ | ok | keep; native review pending | own copy, no fact |
| alt: Imagen de la App Store con el texto: Sin anuncios. Sin suscripción. Todo el contenido de estudio es gratis. Debajo, la pantalla de inicio con el avance general, el cuestionario de práctica, la entrevista hablada y el avance por sección | ok | keep; native review pending | screenshot file, docs/assets.md |
| p: Dentro de la app | ok | keep; native review pending | own copy, no fact |
| h2: Practique la entrevista, la lectura y la escritura. | ok | keep; native review pending | own copy, no fact |
| p: Ninguna app puede prometer que aprobará. | ok | keep; native review pending | own copy, no fact |
| p: Entrevista de práctica hablada | ok | keep; native review pending | own copy, no fact |
| h3: Responda en voz alta | ok | keep; native review pending | own copy, no fact |
| p: Responda en voz alta a las preguntas de la entrevista y la app lo escucha en su dispositivo. | ok | keep; native review pending | own copy, no fact |
| alt: Imagen de la App Store con el texto: Practique la entrevista hablada, responda en voz alta y reciba comentarios. Debajo, una pregunta de la entrevista con la respuesta oída y marcada como correcta | ok | keep; native review pending | screenshot file, docs/assets.md |
| p: Lectura y escritura | ok | keep; native review pending | own copy, no fact |
| h3: Lea en voz alta, escuche y teclee | ok | keep; native review pending | own copy, no fact |
| p: Practique las partes de lectura y escritura en inglés del examen. | ok | keep; native review pending | own copy, no fact |
| alt: Imagen de la App Store con el texto: Lectura y escritura en inglés, lea en voz alta, escuche y teclee. Debajo, las pantallas de práctica de lectura y de escritura | ok | keep; native review pending | screenshot file, docs/assets.md |
| p: Soporte y consultas | ok | keep; native review pending | own copy, no fact |
| h2: Estamos para ayudarle. | ok | keep; native review pending | own copy, no fact |
| p: Para soporte de la app o consultas generales, escríbanos. | ok | keep; native review pending | own copy, no fact |
| a: Política de privacidad de Coach Examen Ciudadanía USA | ok | keep; native review pending | own copy, no fact |
| a: Política de privacidad de Blackjack & Video Poker Coach | ok | keep; native review pending | own copy, no fact |

### `es/examen-ciudadania-estados-unidos/historia/index.html` (es-US)

| Text | Rule checks | Outcome | Source |
| --- | --- | --- | --- |
| title: Historia estadounidense: 46 preguntas de ciudadanía | ≤60: 51 ok | keep; native review pending | own copy; facts per facts table |
| desc: 46 preguntas de práctica del examen de ciudadanía de EE. UU. sobre la historia estadounidense, con respuestas y explicaciones. Gratis y sin cuenta. | 120–155: 147 ok | keep; native review pending | own copy; facts per facts table |
| a: Todas las apps | ok | keep; native review pending | own copy, no fact |
| a: Soporte | ok | keep; native review pending | own copy, no fact |
| p: Sección gratis | ok | keep; native review pending | F6 |
| h1: Historia estadounidense: preguntas de práctica del examen de ciudadanía de EE. UU. | ok | keep; native review pending | own copy; facts per facts table |
| p: 46 preguntas de práctica de esta parte del examen de educación cívica de 2025. Responda en voz alta y luego abra “Ver respuesta” para comprobarla y leer la explicación. | ok | keep; native review pending | own copy, no fact |
| p: Práctica independiente. No está afiliada a USCIS ni al gobierno de EE. UU. Las preguntas oficiales y la guía de estudio son gratuitas en uscis.gov (en inglés). Léalas primero; esta página no las sustituye. | ok | keep; native review pending | F6 |
| h2: Más práctica por sección | ok | keep; native review pending | own copy, no fact |
| p: Haga el examen de práctica de 20 preguntas | ok | keep; native review pending | F3/F4/F5 |
| li: Gobierno estadounidense (64 preguntas) | ok | keep; native review pending | own copy, no fact |
| li: Símbolos y días feriados (10 preguntas) | ok | keep; native review pending | own copy, no fact |
| p: La app de estudio | ok | keep; native review pending | own copy, no fact |
| h2: Estudie las 128 preguntas, en español o en inglés. | ok | keep; native review pending | F3/F4/F5 |
| alt: Ícono de Coach Examen Ciudadanía USA | ok | keep; native review pending | screenshot file, docs/assets.md |
| p: Estudio · iPhone y iPad | ok | keep; native review pending | own copy, no fact |
| h3: Coach Examen Ciudadanía USA | ok | keep; native review pending | own copy, no fact |
| p: Estudie para el examen de naturalización de EE. UU. de 2025 con las preguntas de educación cívica, una entrevista de práctica hablada y práctica de lectura y escritura en inglés. Sin cuenta ni anuncios. | ok | keep; native review pending | own copy, no fact |
| li: Las 128 preguntas de educación cívica con sus respuestas aceptadas, en español o en inglés | ok | keep; native review pending | F3/F4/F5 |
| li: Una entrevista de práctica hablada que escucha sus respuestas | ok | keep; native review pending | own copy, no fact |
| li: Práctica de lectura y escritura en inglés | ok | keep; native review pending | own copy, no fact |
| p: Gratis para empezar. Todo el estudio es gratis, con 2 cuestionarios de práctica, 1 entrevista hablada, 1 ronda de lectura y 1 ronda de escritura; una compra desbloquea simulacros ilimitados, sin suscripción. | ok | keep; native review pending | F6 |
| a: Política de privacidad ↗ | ok | keep; native review pending | own copy, no fact |
| alt: Imagen de la App Store con el texto: Sin anuncios. Sin suscripción. Todo el contenido de estudio es gratis. Debajo, la pantalla de inicio con el avance general, el cuestionario de práctica, la entrevista hablada y el avance por sección | ok | keep; native review pending | screenshot file, docs/assets.md |
| p: Dentro de la app | ok | keep; native review pending | own copy, no fact |
| h2: Practique la entrevista, la lectura y la escritura. | ok | keep; native review pending | own copy, no fact |
| p: Ninguna app puede prometer que aprobará. | ok | keep; native review pending | own copy, no fact |
| p: Entrevista de práctica hablada | ok | keep; native review pending | own copy, no fact |
| h3: Responda en voz alta | ok | keep; native review pending | own copy, no fact |
| p: Responda en voz alta a las preguntas de la entrevista y la app lo escucha en su dispositivo. | ok | keep; native review pending | own copy, no fact |
| alt: Imagen de la App Store con el texto: Practique la entrevista hablada, responda en voz alta y reciba comentarios. Debajo, una pregunta de la entrevista con la respuesta oída y marcada como correcta | ok | keep; native review pending | screenshot file, docs/assets.md |
| p: Lectura y escritura | ok | keep; native review pending | own copy, no fact |
| h3: Lea en voz alta, escuche y teclee | ok | keep; native review pending | own copy, no fact |
| p: Practique las partes de lectura y escritura en inglés del examen. | ok | keep; native review pending | own copy, no fact |
| alt: Imagen de la App Store con el texto: Lectura y escritura en inglés, lea en voz alta, escuche y teclee. Debajo, las pantallas de práctica de lectura y de escritura | ok | keep; native review pending | screenshot file, docs/assets.md |
| p: Soporte y consultas | ok | keep; native review pending | own copy, no fact |
| h2: Estamos para ayudarle. | ok | keep; native review pending | own copy, no fact |
| p: Para soporte de la app o consultas generales, escríbanos. | ok | keep; native review pending | own copy, no fact |
| a: Política de privacidad de Coach Examen Ciudadanía USA | ok | keep; native review pending | own copy, no fact |
| a: Política de privacidad de Blackjack & Video Poker Coach | ok | keep; native review pending | own copy, no fact |

### `es/examen-ciudadania-estados-unidos/index.html` (es-US)

| Text | Rule checks | Outcome | Source |
| --- | --- | --- | --- |
| title: Examen de ciudadanía americana: práctica gratis | ≤60: 47 ok | keep; native review pending | own copy; facts per facts table |
| desc: Practique gratis el examen de ciudadanía de EE. UU.: 120 preguntas de educación cívica con respuestas, un examen de 20 preguntas y cómo es el real. | 120–155: 147 ok | keep; native review pending | own copy; facts per facts table |
| a: Todas las apps | ok | keep; native review pending | own copy, no fact |
| a: Soporte | ok | keep; native review pending | own copy, no fact |
| p: Gratis · Sin cuenta · Sin anuncios | ok | keep; native review pending | F6 |
| h1: Examen de ciudadanía americana: práctica gratis | ok | keep; native review pending | own copy; facts per facts table |
| p: Practique el examen de educación cívica de naturalización de 2025 con 120 preguntas, respuestas y explicaciones. No tiene que registrarse ni pagar nada. | ok | keep; native review pending | own copy, no fact |
| p: Práctica independiente. No está afiliada a USCIS ni al gobierno de EE. UU. Las preguntas oficiales y la guía de estudio son gratuitas en uscis.gov (en inglés). Léalas primero; esta página no las sustituye. | ok | keep; native review pending | F6 |
| h2: Cómo es el examen real | ok | keep; native review pending | own copy, no fact |
| li: Este es el examen de 2025, para el Formulario N-400 presentado el 20 de octubre de 2025 o después. Si presentó el suyo antes, su entrevista podría usar otro examen | ok | changed; native review pending | F3/F4/F5 |
| li: El oficial le hace en voz alta hasta 20 de las 128 preguntas de educación cívica, y usted responde en voz alta | ok | keep; native review pending | F3/F4/F5 |
| li: Necesita 12 respuestas correctas para aprobar; el oficial deja de preguntar al llegar a 12 correctas o a 9 incorrectas | ok | changed; native review pending | F3/F4/F5 |
| li: La entrevista también evalúa la lectura y la escritura en inglés | ok | keep; native review pending | own copy, no fact |
| li: Si tiene 65 años o más y es residente permanente desde hace 20 años o más, puede estudiar solo las 20 preguntas marcadas con un asterisco en la lista oficial. El oficial le hace 10 de ellas, y 6 respuestas correctas bastan para aprobar | ok | changed; native review pending | F3/F4/F5 |
| h2: Examen de práctica | ok | keep; native review pending | own copy, no fact |
| p: Empiece con un cuestionario rápido de 5 preguntas o haga el examen completo: 20 preguntas al azar del banco. Necesita 12 respuestas correctas para aprobar, como en el examen real. No hay cronómetro, como en la entrevista real. | ok | keep; native review pending | F3/F4/F5 |
| p: El examen de práctica necesita JavaScript. Las preguntas de muestra y las páginas por sección funcionan sin él. | ok | keep; native review pending | own copy, no fact |
| button: Empiece el cuestionario rápido: 5 preguntas | verb first ok | changed; native review pending | own copy, no fact |
| button: Empiece el examen completo: 20 preguntas | verb first ok | changed; native review pending | F3/F4/F5 |
| h2: Preguntas de muestra | ok | keep; native review pending | own copy, no fact |
| p: Responda primero estas diez en voz alta. Abra “Ver respuesta” para comprobar cada una. | ok | keep; native review pending | own copy, no fact |
| h2: Practique por sección | ok | keep; native review pending | own copy, no fact |
| p: Todas las preguntas de cada sección, con todas las respuestas aceptadas y explicaciones. | ok | keep; native review pending | own copy, no fact |
| li: Gobierno estadounidense (64 preguntas) | ok | keep; native review pending | own copy, no fact |
| li: Historia estadounidense (46 preguntas) | ok | keep; native review pending | own copy, no fact |
| li: Símbolos y días feriados (10 preguntas) | ok | keep; native review pending | own copy, no fact |
| p: Ocho preguntas no aparecen porque la respuesta depende de dónde vive usted o de quién ocupa el cargo ahora: su senador, su representante, su gobernador y la capital de su estado, y el actual Presidente de la Cámara de Representantes, el Presidente, el Vicepresidente y el presidente de la Corte Suprema. La app le pregunta su estado y muestra a los funcionarios actuales. | ok | keep; native review pending | own copy, no fact |
| p: La app de estudio | ok | keep; native review pending | own copy, no fact |
| h2: Estudie las 128 preguntas, en español o en inglés. | ok | keep; native review pending | F3/F4/F5 |
| alt: Ícono de Coach Examen Ciudadanía USA | ok | keep; native review pending | screenshot file, docs/assets.md |
| p: Estudio · iPhone y iPad | ok | keep; native review pending | own copy, no fact |
| h3: Coach Examen Ciudadanía USA | ok | keep; native review pending | own copy, no fact |
| p: Estudie para el examen de naturalización de EE. UU. de 2025 con las preguntas de educación cívica, una entrevista de práctica hablada y práctica de lectura y escritura en inglés. Sin cuenta ni anuncios. | ok | keep; native review pending | own copy, no fact |
| li: Las 128 preguntas de educación cívica con sus respuestas aceptadas, en español o en inglés | ok | keep; native review pending | F3/F4/F5 |
| li: Una entrevista de práctica hablada que escucha sus respuestas | ok | keep; native review pending | own copy, no fact |
| li: Práctica de lectura y escritura en inglés | ok | keep; native review pending | own copy, no fact |
| p: Gratis para empezar. Todo el estudio es gratis, con 2 cuestionarios de práctica, 1 entrevista hablada, 1 ronda de lectura y 1 ronda de escritura; una compra desbloquea simulacros ilimitados, sin suscripción. | ok | keep; native review pending | F6 |
| a: Política de privacidad ↗ | ok | keep; native review pending | own copy, no fact |
| alt: Imagen de la App Store con el texto: Sin anuncios. Sin suscripción. Todo el contenido de estudio es gratis. Debajo, la pantalla de inicio con el avance general, el cuestionario de práctica, la entrevista hablada y el avance por sección | ok | keep; native review pending | screenshot file, docs/assets.md |
| p: Dentro de la app | ok | keep; native review pending | own copy, no fact |
| h2: Practique la entrevista, la lectura y la escritura. | ok | keep; native review pending | own copy, no fact |
| p: Ninguna app puede prometer que aprobará. | ok | keep; native review pending | own copy, no fact |
| p: Entrevista de práctica hablada | ok | keep; native review pending | own copy, no fact |
| h3: Responda en voz alta | ok | keep; native review pending | own copy, no fact |
| p: Responda en voz alta a las preguntas de la entrevista y la app lo escucha en su dispositivo. | ok | keep; native review pending | own copy, no fact |
| alt: Imagen de la App Store con el texto: Practique la entrevista hablada, responda en voz alta y reciba comentarios. Debajo, una pregunta de la entrevista con la respuesta oída y marcada como correcta | ok | keep; native review pending | screenshot file, docs/assets.md |
| p: Lectura y escritura | ok | keep; native review pending | own copy, no fact |
| h3: Lea en voz alta, escuche y teclee | ok | keep; native review pending | own copy, no fact |
| p: Practique las partes de lectura y escritura en inglés del examen. | ok | keep; native review pending | own copy, no fact |
| alt: Imagen de la App Store con el texto: Lectura y escritura en inglés, lea en voz alta, escuche y teclee. Debajo, las pantallas de práctica de lectura y de escritura | ok | keep; native review pending | screenshot file, docs/assets.md |
| p: Soporte y consultas | ok | keep; native review pending | own copy, no fact |
| h2: Estamos para ayudarle. | ok | keep; native review pending | own copy, no fact |
| p: Para soporte de la app o consultas generales, escríbanos. | ok | keep; native review pending | own copy, no fact |
| a: Política de privacidad de Coach Examen Ciudadanía USA | ok | keep; native review pending | own copy, no fact |
| a: Política de privacidad de Blackjack & Video Poker Coach | ok | keep; native review pending | own copy, no fact |

### `es/examen-ciudadania-estados-unidos/simbolos-feriados/index.html` (es-US)

| Text | Rule checks | Outcome | Source |
| --- | --- | --- | --- |
| title: Símbolos y días feriados: 10 preguntas de ciudadanía | ≤60: 52 ok | keep; native review pending | own copy; facts per facts table |
| desc: 10 preguntas de práctica del examen de ciudadanía de EE. UU. sobre los símbolos y días feriados, con respuestas y explicaciones. Gratis y sin cuenta. | 120–155: 149 ok | keep; native review pending | own copy; facts per facts table |
| a: Todas las apps | ok | keep; native review pending | own copy, no fact |
| a: Soporte | ok | keep; native review pending | own copy, no fact |
| p: Sección gratis | ok | keep; native review pending | F6 |
| h1: Símbolos y días feriados: preguntas de práctica del examen de ciudadanía de EE. UU. | ok | keep; native review pending | own copy; facts per facts table |
| p: 10 preguntas de práctica de esta parte del examen de educación cívica de 2025. Responda en voz alta y luego abra “Ver respuesta” para comprobarla y leer la explicación. | ok | keep; native review pending | own copy, no fact |
| p: Práctica independiente. No está afiliada a USCIS ni al gobierno de EE. UU. Las preguntas oficiales y la guía de estudio son gratuitas en uscis.gov (en inglés). Léalas primero; esta página no las sustituye. | ok | keep; native review pending | F6 |
| h2: Más práctica por sección | ok | keep; native review pending | own copy, no fact |
| p: Haga el examen de práctica de 20 preguntas | ok | keep; native review pending | F3/F4/F5 |
| li: Gobierno estadounidense (64 preguntas) | ok | keep; native review pending | own copy, no fact |
| li: Historia estadounidense (46 preguntas) | ok | keep; native review pending | own copy, no fact |
| p: La app de estudio | ok | keep; native review pending | own copy, no fact |
| h2: Estudie las 128 preguntas, en español o en inglés. | ok | keep; native review pending | F3/F4/F5 |
| alt: Ícono de Coach Examen Ciudadanía USA | ok | keep; native review pending | screenshot file, docs/assets.md |
| p: Estudio · iPhone y iPad | ok | keep; native review pending | own copy, no fact |
| h3: Coach Examen Ciudadanía USA | ok | keep; native review pending | own copy, no fact |
| p: Estudie para el examen de naturalización de EE. UU. de 2025 con las preguntas de educación cívica, una entrevista de práctica hablada y práctica de lectura y escritura en inglés. Sin cuenta ni anuncios. | ok | keep; native review pending | own copy, no fact |
| li: Las 128 preguntas de educación cívica con sus respuestas aceptadas, en español o en inglés | ok | keep; native review pending | F3/F4/F5 |
| li: Una entrevista de práctica hablada que escucha sus respuestas | ok | keep; native review pending | own copy, no fact |
| li: Práctica de lectura y escritura en inglés | ok | keep; native review pending | own copy, no fact |
| p: Gratis para empezar. Todo el estudio es gratis, con 2 cuestionarios de práctica, 1 entrevista hablada, 1 ronda de lectura y 1 ronda de escritura; una compra desbloquea simulacros ilimitados, sin suscripción. | ok | keep; native review pending | F6 |
| a: Política de privacidad ↗ | ok | keep; native review pending | own copy, no fact |
| alt: Imagen de la App Store con el texto: Sin anuncios. Sin suscripción. Todo el contenido de estudio es gratis. Debajo, la pantalla de inicio con el avance general, el cuestionario de práctica, la entrevista hablada y el avance por sección | ok | keep; native review pending | screenshot file, docs/assets.md |
| p: Dentro de la app | ok | keep; native review pending | own copy, no fact |
| h2: Practique la entrevista, la lectura y la escritura. | ok | keep; native review pending | own copy, no fact |
| p: Ninguna app puede prometer que aprobará. | ok | keep; native review pending | own copy, no fact |
| p: Entrevista de práctica hablada | ok | keep; native review pending | own copy, no fact |
| h3: Responda en voz alta | ok | keep; native review pending | own copy, no fact |
| p: Responda en voz alta a las preguntas de la entrevista y la app lo escucha en su dispositivo. | ok | keep; native review pending | own copy, no fact |
| alt: Imagen de la App Store con el texto: Practique la entrevista hablada, responda en voz alta y reciba comentarios. Debajo, una pregunta de la entrevista con la respuesta oída y marcada como correcta | ok | keep; native review pending | screenshot file, docs/assets.md |
| p: Lectura y escritura | ok | keep; native review pending | own copy, no fact |
| h3: Lea en voz alta, escuche y teclee | ok | keep; native review pending | own copy, no fact |
| p: Practique las partes de lectura y escritura en inglés del examen. | ok | keep; native review pending | own copy, no fact |
| alt: Imagen de la App Store con el texto: Lectura y escritura en inglés, lea en voz alta, escuche y teclee. Debajo, las pantallas de práctica de lectura y de escritura | ok | keep; native review pending | screenshot file, docs/assets.md |
| p: Soporte y consultas | ok | keep; native review pending | own copy, no fact |
| h2: Estamos para ayudarle. | ok | keep; native review pending | own copy, no fact |
| p: Para soporte de la app o consultas generales, escríbanos. | ok | keep; native review pending | own copy, no fact |
| a: Política de privacidad de Coach Examen Ciudadanía USA | ok | keep; native review pending | own copy, no fact |
| a: Política de privacidad de Blackjack & Video Poker Coach | ok | keep; native review pending | own copy, no fact |

### `fr/examen-citoyennete-canadienne/droits/index.html` (fr-CA)

| Text | Rule checks | Outcome | Source |
| --- | --- | --- | --- |
| title: Examen de citoyenneté canadienne : droits et responsabilités | ≤60: 60 ok | changed; native review pending | own copy; facts per facts table |
| desc: 27 questions de pratique gratuites sur « droits et responsabilités » pour l’examen de citoyenneté, avec réponses et explications. Sans compte. | 120–155: 142 ok | changed; native review pending | own copy; facts per facts table |
| a: Toutes les applis | ok | keep; native review pending | own copy, no fact |
| a: Soutien | ok | keep; native review pending | own copy, no fact |
| p: Chapitre gratuit 1 | ok | keep; native review pending | F7 |
| h1: Les droits et responsabilités liés à la citoyenneté : questions de pratique | ok | keep; native review pending | own copy; facts per facts table |
| p: 27 questions de pratique gratuites sur ce chapitre du guide d’étude. Choisissez une réponse dans votre tête, puis ouvrez « Afficher la réponse » pour la vérifier et lire l’explication. | ok | keep; native review pending | F7 |
| p: Lire ce chapitre dans Découvrir le Canada ↗ | ok | keep; native review pending | own copy, no fact |
| p: Pratique indépendante. Non affilié à IRCC ni au gouvernement du Canada. Le guide d’étude officiel, Découvrir le Canada, est gratuit sur canada.ca. Lisez-le d’abord ; cette page ne le remplace pas. | ok | keep; native review pending | F7 |
| h2: Plus de pratique par chapitre | ok | keep; native review pending | own copy, no fact |
| p: Faire le test chronométré de 20 questions | ok | keep; native review pending | F1 |
| li: Qui sommes-nous, les Canadiens ? (28 questions) | ok | keep; native review pending | own copy, no fact |
| li: L’histoire du Canada (112 questions) | ok | keep; native review pending | own copy, no fact |
| p: L’application d’étude | ok | keep; native review pending | own copy, no fact |
| h2: Étudiez chaque chapitre, en français ou en anglais. | ok | keep; native review pending | own copy, no fact |
| alt: Icône de Coach Test Citoyenneté Canada | ok | keep; native review pending | screenshot file, docs/assets.md |
| p: Étude · iPhone et iPad | ok | keep; native review pending | own copy, no fact |
| h3: Coach Test Citoyenneté Canada | ok | keep; native review pending | own copy, no fact |
| p: Étudiez pour l’examen de citoyenneté canadienne un chapitre à la fois, puis faites des examens simulés chronométrés avec la note de passage du vrai examen. | ok | keep; native review pending | own copy, no fact |
| li: Les 11 chapitres du guide, plus votre province ou territoire | ok | keep; native review pending | own copy, no fact |
| li: Étudiez et écoutez en français ou en anglais | ok | keep; native review pending | own copy, no fact |
| li: Examens simulés chronométrés de 20 questions en 45 minutes, chaque réponse expliquée | ok | keep; native review pending | F1 |
| p: Gratuit pour commencer. Les trois premiers chapitres et deux examens simulés sont gratuits ; un achat débloque tout, sans abonnement. | ok | changed; native review pending | F7 |
| a: Politique de confidentialité ↗ | ok | keep; native review pending | own copy, no fact |
| alt: Image de l’App Store avec légende : Lisez ou écoutez, étudiez en français ou en anglais, au-dessus du chapitre Les droits en français et en anglais | ok | keep; native review pending | screenshot file, docs/assets.md |
| p: Dans l’application | ok | keep; native review pending | own copy, no fact |
| h2: Pratiquez, puis voyez où vous en êtes. | ok | keep; native review pending | own copy, no fact |
| p: Un quiz après chaque section et la préparation de chaque chapitre. | ok | keep; native review pending | own copy, no fact |
| p: Quiz par section | ok | keep; native review pending | own copy, no fact |
| h3: Apprenez de chaque réponse | ok | keep; native review pending | own copy, no fact |
| p: Un quiz après chaque section, avec une courte explication pour chaque réponse. | ok | keep; native review pending | own copy, no fact |
| alt: Image de l’App Store avec légende : Apprenez de chaque réponse, des explications pour les bonnes et les mauvaises réponses, au-dessus d’une question de quiz avec le mauvais choix en rouge et la bonne réponse en vert | ok | keep; native review pending | screenshot file, docs/assets.md |
| p: Préparation par chapitre | ok | keep; native review pending | own copy, no fact |
| h3: Sachez ce qu’il faut réviser | ok | changed; native review pending | own copy, no fact |
| p: Voyez quelles parties du guide vous connaissez déjà, chapitre par chapitre. | ok | keep; native review pending | own copy, no fact |
| alt: Image de l’App Store avec légende : Sans publicité. Sans abonnement. Commencez gratuitement, aucun compte requis, au-dessus de l’écran Accueil avec les progrès par chapitre | ok | keep; native review pending | screenshot file, docs/assets.md |
| p: Soutien et demandes | ok | keep; native review pending | own copy, no fact |
| h2: Nous sommes là pour vous aider. | ok | keep; native review pending | own copy, no fact |
| p: Pour du soutien sur l’application ou toute autre demande, écrivez-nous. | ok | keep; native review pending | own copy, no fact |
| a: Politique de confidentialité de Coach Test Citoyenneté Canada | ok | keep; native review pending | own copy, no fact |
| a: Politique de confidentialité de Blackjack & Video Poker Coach | ok | keep; native review pending | own copy, no fact |

### `fr/examen-citoyennete-canadienne/histoire/index.html` (fr-CA)

| Text | Rule checks | Outcome | Source |
| --- | --- | --- | --- |
| title: Examen de citoyenneté canadienne : histoire du Canada | ≤60: 53 ok | changed; native review pending | own copy; facts per facts table |
| desc: 112 questions de pratique gratuites sur « histoire du Canada » pour l’examen de citoyenneté, avec réponses et explications. Sans compte. | 120–155: 136 ok | changed; native review pending | own copy; facts per facts table |
| a: Toutes les applis | ok | keep; native review pending | own copy, no fact |
| a: Soutien | ok | keep; native review pending | own copy, no fact |
| p: Chapitre gratuit 3 | ok | keep; native review pending | F7 |
| h1: L’histoire du Canada : questions de pratique | ok | keep; native review pending | own copy; facts per facts table |
| p: 112 questions de pratique gratuites sur ce chapitre du guide d’étude. Choisissez une réponse dans votre tête, puis ouvrez « Afficher la réponse » pour la vérifier et lire l’explication. | ok | keep; native review pending | F7 |
| p: Lire ce chapitre dans Découvrir le Canada ↗ | ok | keep; native review pending | own copy, no fact |
| p: Pratique indépendante. Non affilié à IRCC ni au gouvernement du Canada. Le guide d’étude officiel, Découvrir le Canada, est gratuit sur canada.ca. Lisez-le d’abord ; cette page ne le remplace pas. | ok | keep; native review pending | F7 |
| h2: Plus de pratique par chapitre | ok | keep; native review pending | own copy, no fact |
| p: Faire le test chronométré de 20 questions | ok | keep; native review pending | F1 |
| li: Les droits et responsabilités liés à la citoyenneté (27 questions) | ok | keep; native review pending | own copy, no fact |
| li: Qui sommes-nous, les Canadiens ? (28 questions) | ok | keep; native review pending | own copy, no fact |
| p: L’application d’étude | ok | keep; native review pending | own copy, no fact |
| h2: Étudiez chaque chapitre, en français ou en anglais. | ok | keep; native review pending | own copy, no fact |
| alt: Icône de Coach Test Citoyenneté Canada | ok | keep; native review pending | screenshot file, docs/assets.md |
| p: Étude · iPhone et iPad | ok | keep; native review pending | own copy, no fact |
| h3: Coach Test Citoyenneté Canada | ok | keep; native review pending | own copy, no fact |
| p: Étudiez pour l’examen de citoyenneté canadienne un chapitre à la fois, puis faites des examens simulés chronométrés avec la note de passage du vrai examen. | ok | keep; native review pending | own copy, no fact |
| li: Les 11 chapitres du guide, plus votre province ou territoire | ok | keep; native review pending | own copy, no fact |
| li: Étudiez et écoutez en français ou en anglais | ok | keep; native review pending | own copy, no fact |
| li: Examens simulés chronométrés de 20 questions en 45 minutes, chaque réponse expliquée | ok | keep; native review pending | F1 |
| p: Gratuit pour commencer. Les trois premiers chapitres et deux examens simulés sont gratuits ; un achat débloque tout, sans abonnement. | ok | changed; native review pending | F7 |
| a: Politique de confidentialité ↗ | ok | keep; native review pending | own copy, no fact |
| alt: Image de l’App Store avec légende : Lisez ou écoutez, étudiez en français ou en anglais, au-dessus du chapitre Les droits en français et en anglais | ok | keep; native review pending | screenshot file, docs/assets.md |
| p: Dans l’application | ok | keep; native review pending | own copy, no fact |
| h2: Pratiquez, puis voyez où vous en êtes. | ok | keep; native review pending | own copy, no fact |
| p: Un quiz après chaque section et la préparation de chaque chapitre. | ok | keep; native review pending | own copy, no fact |
| p: Quiz par section | ok | keep; native review pending | own copy, no fact |
| h3: Apprenez de chaque réponse | ok | keep; native review pending | own copy, no fact |
| p: Un quiz après chaque section, avec une courte explication pour chaque réponse. | ok | keep; native review pending | own copy, no fact |
| alt: Image de l’App Store avec légende : Apprenez de chaque réponse, des explications pour les bonnes et les mauvaises réponses, au-dessus d’une question de quiz avec le mauvais choix en rouge et la bonne réponse en vert | ok | keep; native review pending | screenshot file, docs/assets.md |
| p: Préparation par chapitre | ok | keep; native review pending | own copy, no fact |
| h3: Sachez ce qu’il faut réviser | ok | changed; native review pending | own copy, no fact |
| p: Voyez quelles parties du guide vous connaissez déjà, chapitre par chapitre. | ok | keep; native review pending | own copy, no fact |
| alt: Image de l’App Store avec légende : Sans publicité. Sans abonnement. Commencez gratuitement, aucun compte requis, au-dessus de l’écran Accueil avec les progrès par chapitre | ok | keep; native review pending | screenshot file, docs/assets.md |
| p: Soutien et demandes | ok | keep; native review pending | own copy, no fact |
| h2: Nous sommes là pour vous aider. | ok | keep; native review pending | own copy, no fact |
| p: Pour du soutien sur l’application ou toute autre demande, écrivez-nous. | ok | keep; native review pending | own copy, no fact |
| a: Politique de confidentialité de Coach Test Citoyenneté Canada | ok | keep; native review pending | own copy, no fact |
| a: Politique de confidentialité de Blackjack & Video Poker Coach | ok | keep; native review pending | own copy, no fact |

### `fr/examen-citoyennete-canadienne/index.html` (fr-CA)

| Text | Rule checks | Outcome | Source |
| --- | --- | --- | --- |
| title: Examen de citoyenneté canadienne gratuit : test pratique | ≤60: 56 ok | changed; native review pending | own copy; facts per facts table |
| desc: Test pratique gratuit de l’examen de citoyenneté canadienne : 20 questions, 45 minutes, 15 bonnes réponses. Sans compte, en français et en anglais. | 120–155: 147 ok | changed; native review pending | own copy; facts per facts table |
| a: Toutes les applis | ok | keep; native review pending | own copy, no fact |
| a: Soutien | ok | keep; native review pending | own copy, no fact |
| p: Gratuit · Sans compte · Sans publicité | ok | keep; native review pending | F7 |
| h1: Examen de citoyenneté canadienne gratuit : test pratique (2026) | ok | keep; native review pending | own copy; facts per facts table |
| p: Faites un test pratique gratuit de 20 questions en 45 minutes : il faut 15 bonnes réponses pour réussir, comme à l’examen réel. Rien à créer, rien à payer. | ok | changed; native review pending | F1 |
| p: Pratique indépendante. Non affilié à IRCC ni au gouvernement du Canada. Le guide d’étude officiel, Découvrir le Canada, est gratuit sur canada.ca. Lisez-le d’abord ; cette page ne le remplace pas. | ok | keep; native review pending | F7 |
| h2: Le déroulement de l’examen réel | ok | keep; native review pending | own copy, no fact |
| li: 20 questions | ok | keep; native review pending | F1 |
| li: 45 minutes | ok | keep; native review pending | F1 |
| li: Il faut 15 bonnes réponses pour réussir | ok | keep; native review pending | F1 |
| li: Les questions s’appuient sur le guide Découvrir le Canada | ok | keep; native review pending | own copy, no fact |
| h2: Test pratique | ok | keep; native review pending | own copy, no fact |
| p: Commencez par un quiz rapide de 5 questions, ou faites le test complet : 20 questions tirées au hasard dans les trois chapitres gratuits, en 45 minutes. Il faut 15 bonnes réponses pour réussir, comme à l’examen réel. | ok | keep; native review pending | F1 |
| p: Le test pratique demande JavaScript. Les exemples de questions et les pages par chapitre fonctionnent sans. | ok | keep; native review pending | own copy, no fact |
| button: Commencer le quiz rapide : 5 questions | verb first ok | changed; native review pending | own copy, no fact |
| button: Commencer le test complet : 20 questions, 45 minutes | verb first ok | changed; native review pending | F1 |
| p: · Temps restant : 45:00 | ok | keep; native review pending | F1 |
| h2: Exemples de questions | ok | keep; native review pending | own copy, no fact |
| p: Essayez ces dix questions sans chronomètre. Ouvrez « Afficher la réponse » pour vérifier chacune. | ok | keep; native review pending | own copy, no fact |
| h2: Pratique par chapitre | ok | keep; native review pending | own copy, no fact |
| p: Toutes les questions de chaque chapitre gratuit, avec réponses et explications. | ok | keep; native review pending | F7 |
| li: Les droits et responsabilités liés à la citoyenneté (27 questions) | ok | keep; native review pending | own copy, no fact |
| li: Qui sommes-nous, les Canadiens ? (28 questions) | ok | keep; native review pending | own copy, no fact |
| li: L’histoire du Canada (112 questions) | ok | keep; native review pending | own copy, no fact |
| p: L’application d’étude | ok | keep; native review pending | own copy, no fact |
| h2: Étudiez chaque chapitre, en français ou en anglais. | ok | keep; native review pending | own copy, no fact |
| alt: Icône de Coach Test Citoyenneté Canada | ok | keep; native review pending | screenshot file, docs/assets.md |
| p: Étude · iPhone et iPad | ok | keep; native review pending | own copy, no fact |
| h3: Coach Test Citoyenneté Canada | ok | keep; native review pending | own copy, no fact |
| p: Étudiez pour l’examen de citoyenneté canadienne un chapitre à la fois, puis faites des examens simulés chronométrés avec la note de passage du vrai examen. | ok | keep; native review pending | own copy, no fact |
| li: Les 11 chapitres du guide, plus votre province ou territoire | ok | keep; native review pending | own copy, no fact |
| li: Étudiez et écoutez en français ou en anglais | ok | keep; native review pending | own copy, no fact |
| li: Examens simulés chronométrés de 20 questions en 45 minutes, chaque réponse expliquée | ok | keep; native review pending | F1 |
| p: Gratuit pour commencer. Les trois premiers chapitres et deux examens simulés sont gratuits ; un achat débloque tout, sans abonnement. | ok | changed; native review pending | F7 |
| a: Politique de confidentialité ↗ | ok | keep; native review pending | own copy, no fact |
| alt: Image de l’App Store avec légende : Lisez ou écoutez, étudiez en français ou en anglais, au-dessus du chapitre Les droits en français et en anglais | ok | keep; native review pending | screenshot file, docs/assets.md |
| p: Dans l’application | ok | keep; native review pending | own copy, no fact |
| h2: Pratiquez, puis voyez où vous en êtes. | ok | keep; native review pending | own copy, no fact |
| p: Un quiz après chaque section et la préparation de chaque chapitre. | ok | keep; native review pending | own copy, no fact |
| p: Quiz par section | ok | keep; native review pending | own copy, no fact |
| h3: Apprenez de chaque réponse | ok | keep; native review pending | own copy, no fact |
| p: Un quiz après chaque section, avec une courte explication pour chaque réponse. | ok | keep; native review pending | own copy, no fact |
| alt: Image de l’App Store avec légende : Apprenez de chaque réponse, des explications pour les bonnes et les mauvaises réponses, au-dessus d’une question de quiz avec le mauvais choix en rouge et la bonne réponse en vert | ok | keep; native review pending | screenshot file, docs/assets.md |
| p: Préparation par chapitre | ok | keep; native review pending | own copy, no fact |
| h3: Sachez ce qu’il faut réviser | ok | changed; native review pending | own copy, no fact |
| p: Voyez quelles parties du guide vous connaissez déjà, chapitre par chapitre. | ok | keep; native review pending | own copy, no fact |
| alt: Image de l’App Store avec légende : Sans publicité. Sans abonnement. Commencez gratuitement, aucun compte requis, au-dessus de l’écran Accueil avec les progrès par chapitre | ok | keep; native review pending | screenshot file, docs/assets.md |
| p: Soutien et demandes | ok | keep; native review pending | own copy, no fact |
| h2: Nous sommes là pour vous aider. | ok | keep; native review pending | own copy, no fact |
| p: Pour du soutien sur l’application ou toute autre demande, écrivez-nous. | ok | keep; native review pending | own copy, no fact |
| a: Politique de confidentialité de Coach Test Citoyenneté Canada | ok | keep; native review pending | own copy, no fact |
| a: Politique de confidentialité de Blackjack & Video Poker Coach | ok | keep; native review pending | own copy, no fact |

### `fr/examen-citoyennete-canadienne/qui-nous-sommes/index.html` (fr-CA)

| Text | Rule checks | Outcome | Source |
| --- | --- | --- | --- |
| title: Examen de citoyenneté canadienne : qui sommes-nous ? | ≤60: 52 ok | changed; native review pending | own copy; facts per facts table |
| desc: 28 questions de pratique gratuites sur « qui sommes-nous ? » pour l’examen de citoyenneté, avec réponses et explications. Sans compte. | 120–155: 134 ok | changed; native review pending | own copy; facts per facts table |
| a: Toutes les applis | ok | keep; native review pending | own copy, no fact |
| a: Soutien | ok | keep; native review pending | own copy, no fact |
| p: Chapitre gratuit 2 | ok | keep; native review pending | F7 |
| h1: Qui sommes-nous, les Canadiens ? : questions de pratique | ok | keep; native review pending | own copy; facts per facts table |
| p: 28 questions de pratique gratuites sur ce chapitre du guide d’étude. Choisissez une réponse dans votre tête, puis ouvrez « Afficher la réponse » pour la vérifier et lire l’explication. | ok | keep; native review pending | F7 |
| p: Lire ce chapitre dans Découvrir le Canada ↗ | ok | keep; native review pending | own copy, no fact |
| p: Pratique indépendante. Non affilié à IRCC ni au gouvernement du Canada. Le guide d’étude officiel, Découvrir le Canada, est gratuit sur canada.ca. Lisez-le d’abord ; cette page ne le remplace pas. | ok | keep; native review pending | F7 |
| h2: Plus de pratique par chapitre | ok | keep; native review pending | own copy, no fact |
| p: Faire le test chronométré de 20 questions | ok | keep; native review pending | F1 |
| li: Les droits et responsabilités liés à la citoyenneté (27 questions) | ok | keep; native review pending | own copy, no fact |
| li: L’histoire du Canada (112 questions) | ok | keep; native review pending | own copy, no fact |
| p: L’application d’étude | ok | keep; native review pending | own copy, no fact |
| h2: Étudiez chaque chapitre, en français ou en anglais. | ok | keep; native review pending | own copy, no fact |
| alt: Icône de Coach Test Citoyenneté Canada | ok | keep; native review pending | screenshot file, docs/assets.md |
| p: Étude · iPhone et iPad | ok | keep; native review pending | own copy, no fact |
| h3: Coach Test Citoyenneté Canada | ok | keep; native review pending | own copy, no fact |
| p: Étudiez pour l’examen de citoyenneté canadienne un chapitre à la fois, puis faites des examens simulés chronométrés avec la note de passage du vrai examen. | ok | keep; native review pending | own copy, no fact |
| li: Les 11 chapitres du guide, plus votre province ou territoire | ok | keep; native review pending | own copy, no fact |
| li: Étudiez et écoutez en français ou en anglais | ok | keep; native review pending | own copy, no fact |
| li: Examens simulés chronométrés de 20 questions en 45 minutes, chaque réponse expliquée | ok | keep; native review pending | F1 |
| p: Gratuit pour commencer. Les trois premiers chapitres et deux examens simulés sont gratuits ; un achat débloque tout, sans abonnement. | ok | changed; native review pending | F7 |
| a: Politique de confidentialité ↗ | ok | keep; native review pending | own copy, no fact |
| alt: Image de l’App Store avec légende : Lisez ou écoutez, étudiez en français ou en anglais, au-dessus du chapitre Les droits en français et en anglais | ok | keep; native review pending | screenshot file, docs/assets.md |
| p: Dans l’application | ok | keep; native review pending | own copy, no fact |
| h2: Pratiquez, puis voyez où vous en êtes. | ok | keep; native review pending | own copy, no fact |
| p: Un quiz après chaque section et la préparation de chaque chapitre. | ok | keep; native review pending | own copy, no fact |
| p: Quiz par section | ok | keep; native review pending | own copy, no fact |
| h3: Apprenez de chaque réponse | ok | keep; native review pending | own copy, no fact |
| p: Un quiz après chaque section, avec une courte explication pour chaque réponse. | ok | keep; native review pending | own copy, no fact |
| alt: Image de l’App Store avec légende : Apprenez de chaque réponse, des explications pour les bonnes et les mauvaises réponses, au-dessus d’une question de quiz avec le mauvais choix en rouge et la bonne réponse en vert | ok | keep; native review pending | screenshot file, docs/assets.md |
| p: Préparation par chapitre | ok | keep; native review pending | own copy, no fact |
| h3: Sachez ce qu’il faut réviser | ok | changed; native review pending | own copy, no fact |
| p: Voyez quelles parties du guide vous connaissez déjà, chapitre par chapitre. | ok | keep; native review pending | own copy, no fact |
| alt: Image de l’App Store avec légende : Sans publicité. Sans abonnement. Commencez gratuitement, aucun compte requis, au-dessus de l’écran Accueil avec les progrès par chapitre | ok | keep; native review pending | screenshot file, docs/assets.md |
| p: Soutien et demandes | ok | keep; native review pending | own copy, no fact |
| h2: Nous sommes là pour vous aider. | ok | keep; native review pending | own copy, no fact |
| p: Pour du soutien sur l’application ou toute autre demande, écrivez-nous. | ok | keep; native review pending | own copy, no fact |
| a: Politique de confidentialité de Coach Test Citoyenneté Canada | ok | keep; native review pending | own copy, no fact |
| a: Politique de confidentialité de Blackjack & Video Poker Coach | ok | keep; native review pending | own copy, no fact |

### `index.html` (en)

| Text | Rule checks | Outcome | Source |
| --- | --- | --- | --- |
| title: PANGUFU: iPhone & iPad Apps for Learning and Practice | ≤60: 53 ok | changed | own copy; facts per facts table |
| desc: PANGUFU builds focused iPhone and iPad apps for learning and practice: Canadian and US citizenship test coaches and a blackjack and video poker coach. | 120–155: 150 ok | changed | own copy; facts per facts table |
| a: Apps | ok | keep | own copy, no fact |
| h1: Small apps.Thoughtfully made. | ok | keep | developer’s brand line |
| p: PANGUFU builds focused iPhone and iPad apps for learning and practice. We care about clear design, useful feedback and the small details that make an app feel natural to use. Our apps today help people prepare for the Canadian and US citizenship tests and practise blackjack and video poker strategy, with more to come. | ok | changed | F6/F7/F8 |
| a: Explore our apps ↓ | ok | keep | own copy, no fact |
| span: Care in every detail | ok | keep | developer’s brand line |
| p: iPhone & iPad apps | ok | changed | own copy, no fact |
| h2: Our apps | ok | keep | own copy, no fact |
| p: Each app shows you the right answer. | ok | changed | own copy, no fact |
| a: Canada Citizenship Test Coach ↓ | ok | keep | own copy, no fact |
| a: US Citizen Test Coach ↓ | ok | keep | own copy, no fact |
| a: Blackjack & Video Poker Coach ↓ | ok | keep | own copy, no fact |
| alt: Canada Citizenship Test Coach icon | ok | keep | screenshot file, docs/assets.md |
| h3: Canada Citizenship Test Coach | ok | keep | own copy, no fact |
| p: Get ready for the Canadian citizenship test with the whole study guide on your iPhone or iPad. Learn a section, check it with a short quiz, and see which chapters still need work. | ok | keep | own copy, no fact |
| li: The full guide in 11 chapters, with your province or territory | ok | keep | own copy, no fact |
| li: Read or listen, in English or French | ok | keep | own copy, no fact |
| li: Practice tests timed like the real one: 20 questions, 45 minutes | ok | keep | own copy, no fact |
| a: About the app → | ok | flagged: flagged: not verb-first; wording set by plan Phase 3, developer decides | own copy, no fact |
| a: Free practice test → | ok | keep | F6/F7/F8 |
| alt: Captioned App Store image: No Ads. No Subscription. Start free, no account needed, above the home screen with a 30-day test countdown, overall progress and progress by chapter | ok | keep | screenshot file, docs/assets.md |
| alt: Captioned App Store image: Learn From Every Answer, explanations for right and wrong answers, above a quiz question with the wrong choice in red and the right answer in green | ok | keep | screenshot file, docs/assets.md |
| alt: Captioned App Store image: Read or Listen, study in English or French, above the Rights chapter in English and French | ok | keep | screenshot file, docs/assets.md |
| alt: US Citizen Test Coach icon | ok | keep | screenshot file, docs/assets.md |
| h3: US Citizen Test Coach | ok | keep | own copy, no fact |
| p: Get ready for the US naturalization test on your iPhone or iPad: the 2025 civics questions, English reading and writing, and a spoken mock interview. All study content is free. | ok | keep | F6/F7/F8 |
| li: Every civics question, in English or Spanish, with flash cards and audio | ok | keep | own copy, no fact |
| li: Answer the interview questions aloud and get feedback | ok | keep | own copy, no fact |
| li: Reading and writing practice, plus answers for your state | ok | keep | own copy, no fact |
| alt: Captioned App Store image: No Ads. No Subscription. All study content is free, above the home screen with overall progress, the mock quiz and spoken interview, and progress by chapter | ok | keep | screenshot file, docs/assets.md |
| alt: Captioned App Store image: Practice the Spoken Interview, answer aloud and get feedback, above an interview question with the spoken answer heard and marked right | ok | keep | screenshot file, docs/assets.md |
| alt: Captioned App Store image: English Reading and Writing, read aloud, listen and type, above the reading and writing practice screens | ok | keep | screenshot file, docs/assets.md |
| alt: Blackjack and card coach icon | ok | keep | screenshot file, docs/assets.md |
| p: Learn · iPhone & iPad | ok | keep | own copy, no fact |
| h3: Blackjack & Video Poker Coach | ok | keep | own copy, no fact |
| p: Learn blackjack basic strategy one hand at a time, then move on to card counting and video poker. It is a practice tool only: no real money and no prizes. | ok | keep | own copy, no fact |
| li: Basic strategy practice, with hints at first and then without | ok | keep | own copy, no fact |
| li: Hi-Lo card counting drills | ok | keep | own copy, no fact |
| li: Video poker holds checked against the best hold | empty praise | keep | own copy, no fact |
| alt: Captioned App Store image: No Ads. No Subscription. Basic strategy is free, above the Blackjack practice screen with a hint for the hand | ok | keep | screenshot file, docs/assets.md |
| alt: Captioned App Store image: Learn Hi-Lo Counting, step by step, with Unlock All, above the card values and the counting lessons | ok | keep | screenshot file, docs/assets.md |
| alt: Captioned App Store image: Perfect Video Poker Holds, one unlock for counting and video poker, above feedback comparing a hold with the best hold | empty praise | keep | screenshot file, docs/assets.md |
| p: All our apps | ok | keep | own copy, no fact |
| h2: Free to start.No subscription. | ok | keep | F6/F7/F8 |
| p: Each app is free to start. One purchase unlocks the rest, and there is no subscription. | ok | keep | F6/F7/F8 |
| p: No ads, no account and no data collected. | ok | keep | own copy, no fact |
| a: US Citizen Test Coach privacy policy | ok | keep | own copy, no fact |

### `purrcade/privacy.html` (en)

| Text | Rule checks | Outcome | Source |
| --- | --- | --- | --- |
| title: Purrcade Privacy Policy | ≤60: 23 ok | keep | own copy; facts per facts table |
| desc: Purrcade: Games for Cats privacy policy: no data collected, no ads or tracking, settings stay on your device, one-time unlock through Apple. | 120–155: 140 ok | changed | own copy; facts per facts table |

### `us-citizenship-test/government/index.html` (en-US)

| Text | Rule checks | Outcome | Source |
| --- | --- | --- | --- |
| title: American Government: 64 US Citizenship Test Questions | ≤60: 53 ok | keep | own copy; facts per facts table |
| desc: 64 free US citizenship test practice questions on American Government, with every accepted answer and an explanation. No account. Independent practice. | 120–155: 151 ok | keep | own copy; facts per facts table |
| a: Español | ok | keep | own copy, no fact |
| p: Free section | ok | keep | F6 |
| h1: American Government: US Citizenship Test Practice Questions | ok | keep | own copy; facts per facts table |
| p: 64 practice questions from this part of the 2025 civics test. Answer out loud, then open “Show answer” to check it and read the explanation. | ok | keep | own copy, no fact |
| p: Independent practice. Not affiliated with USCIS or the U.S. government. The official questions and study guide are free on uscis.gov. Read them first; this page does not replace them. | ok | keep | F6 |
| p: Eight questions are not listed because the answer depends on where you live or who holds office now: your senator, representative, governor and state capital, and the current Speaker of the House, President, Vice President and Chief Justice. The app asks for your state and shows the current officeholders. | ok | keep | own copy, no fact |
| h2: More practice by section | ok | keep | own copy, no fact |
| p: Take the 20-question practice test | ok | keep | F3/F4/F5 |
| li: American History (46 questions) | ok | keep | own copy, no fact |
| li: Symbols and Holidays (10 questions) | ok | keep | own copy, no fact |
| h2: Study all 128 questions, in English or Spanish. | ok | keep | F3/F4/F5 |
| alt: US Citizen Test Coach icon | ok | keep | screenshot file, docs/assets.md |
| h3: US Citizen Test Coach | ok | keep | own copy, no fact |
| p: Study for the 2025 US naturalization test with the civics questions, a spoken mock interview and English reading and writing practice. No account and no ads. | ok | keep | own copy, no fact |
| li: All 128 civics questions with accepted answers, in English or Spanish | ok | keep | F3/F4/F5 |
| li: A spoken mock interview that listens to your answers | ok | keep | own copy, no fact |
| li: English reading and writing practice | ok | keep | own copy, no fact |
| p: Free to start. All study is free, with 2 mock quizzes, 1 spoken interview, 1 reading round and 1 writing round; one purchase unlocks unlimited simulations, with no subscription. | ok | keep | F6 |
| alt: Captioned App Store image: No Ads. No Subscription. All study content is free, above the home screen with overall progress, the mock quiz and spoken interview, and progress by chapter | ok | keep | screenshot file, docs/assets.md |
| h2: Practice the interview, reading and writing. | ok | keep | own copy, no fact |
| p: No app can promise a pass. | ok | keep | own copy, no fact |
| p: Spoken mock interview | ok | keep | own copy, no fact |
| h3: Answer aloud | ok | keep | own copy, no fact |
| p: Answer the interview questions aloud, and the app listens on your device. | ok | changed | own copy, no fact |
| alt: Captioned App Store image: Practice the Spoken Interview, answer aloud and get feedback, above an interview question with the spoken answer heard and marked right | ok | keep | screenshot file, docs/assets.md |
| p: Reading and writing | ok | keep | own copy, no fact |
| h3: Read aloud, listen and type | ok | keep | own copy, no fact |
| p: Practice the English reading and writing parts of the test. | ok | keep | own copy, no fact |
| alt: Captioned App Store image: English Reading and Writing, read aloud, listen and type, above the reading and writing practice screens | ok | keep | screenshot file, docs/assets.md |
| p: Support & inquiries | ok | changed | own copy, no fact |
| p: For app support or general inquiries, send us a note. | ok | changed | own copy, no fact |
| a: US Citizen Test Coach privacy policy | ok | keep | own copy, no fact |

### `us-citizenship-test/history/index.html` (en-US)

| Text | Rule checks | Outcome | Source |
| --- | --- | --- | --- |
| title: American History: 46 US Citizenship Test Questions | ≤60: 50 ok | keep | own copy; facts per facts table |
| desc: 46 free US citizenship test practice questions on American History, with every accepted answer and an explanation. No account. Independent practice. | 120–155: 148 ok | keep | own copy; facts per facts table |
| a: Español | ok | keep | own copy, no fact |
| p: Free section | ok | keep | F6 |
| h1: American History: US Citizenship Test Practice Questions | ok | keep | own copy; facts per facts table |
| p: 46 practice questions from this part of the 2025 civics test. Answer out loud, then open “Show answer” to check it and read the explanation. | ok | keep | own copy, no fact |
| p: Independent practice. Not affiliated with USCIS or the U.S. government. The official questions and study guide are free on uscis.gov. Read them first; this page does not replace them. | ok | keep | F6 |
| h2: More practice by section | ok | keep | own copy, no fact |
| p: Take the 20-question practice test | ok | keep | F3/F4/F5 |
| li: American Government (64 questions) | ok | keep | own copy, no fact |
| li: Symbols and Holidays (10 questions) | ok | keep | own copy, no fact |
| h2: Study all 128 questions, in English or Spanish. | ok | keep | F3/F4/F5 |
| alt: US Citizen Test Coach icon | ok | keep | screenshot file, docs/assets.md |
| h3: US Citizen Test Coach | ok | keep | own copy, no fact |
| p: Study for the 2025 US naturalization test with the civics questions, a spoken mock interview and English reading and writing practice. No account and no ads. | ok | keep | own copy, no fact |
| li: All 128 civics questions with accepted answers, in English or Spanish | ok | keep | F3/F4/F5 |
| li: A spoken mock interview that listens to your answers | ok | keep | own copy, no fact |
| li: English reading and writing practice | ok | keep | own copy, no fact |
| p: Free to start. All study is free, with 2 mock quizzes, 1 spoken interview, 1 reading round and 1 writing round; one purchase unlocks unlimited simulations, with no subscription. | ok | keep | F6 |
| alt: Captioned App Store image: No Ads. No Subscription. All study content is free, above the home screen with overall progress, the mock quiz and spoken interview, and progress by chapter | ok | keep | screenshot file, docs/assets.md |
| h2: Practice the interview, reading and writing. | ok | keep | own copy, no fact |
| p: No app can promise a pass. | ok | keep | own copy, no fact |
| p: Spoken mock interview | ok | keep | own copy, no fact |
| h3: Answer aloud | ok | keep | own copy, no fact |
| p: Answer the interview questions aloud, and the app listens on your device. | ok | changed | own copy, no fact |
| alt: Captioned App Store image: Practice the Spoken Interview, answer aloud and get feedback, above an interview question with the spoken answer heard and marked right | ok | keep | screenshot file, docs/assets.md |
| p: Reading and writing | ok | keep | own copy, no fact |
| h3: Read aloud, listen and type | ok | keep | own copy, no fact |
| p: Practice the English reading and writing parts of the test. | ok | keep | own copy, no fact |
| alt: Captioned App Store image: English Reading and Writing, read aloud, listen and type, above the reading and writing practice screens | ok | keep | screenshot file, docs/assets.md |
| p: Support & inquiries | ok | changed | own copy, no fact |
| p: For app support or general inquiries, send us a note. | ok | changed | own copy, no fact |
| a: US Citizen Test Coach privacy policy | ok | keep | own copy, no fact |

### `us-citizenship-test/index.html` (en-US)

| Text | Rule checks | Outcome | Source |
| --- | --- | --- | --- |
| title: Free US Citizenship Practice Test (2025 Civics Test) | ≤60: 52 ok | keep | own copy; facts per facts table |
| desc: Free US citizenship practice test: 120 civics questions with answers, a 20-question mock quiz and how the 2025 naturalization test works. No account. | 120–155: 149 ok | keep | own copy; facts per facts table |
| a: Español | ok | keep | own copy, no fact |
| p: Free · No account · No ads | ok | keep | F6 |
| h1: Free US Citizenship Practice Test | ok | keep | own copy; facts per facts table |
| p: Practice the 2025 naturalization civics test with 120 questions, answers, and explanations. Nothing to sign up for and nothing to pay. | ok | changed | own copy, no fact |
| p: Independent practice. Not affiliated with USCIS or the U.S. government. The official questions and study guide are free on uscis.gov. Read them first; this page does not replace them. | ok | keep | F6 |
| h2: How the real test works | ok | keep | own copy, no fact |
| li: This is the 2025 test, for Form N-400 filed on or after October 20, 2025. If you filed earlier, your interview may use a different test | ok | changed | F3/F4/F5 |
| li: The officer asks up to 20 of the 128 civics questions aloud, and you answer aloud | ok | keep | F3/F4/F5 |
| li: You need 12 correct answers to pass; the officer stops after 12 right or 9 wrong answers | ok | changed | F3/F4/F5 |
| li: The interview also tests English reading and writing | ok | keep | own copy, no fact |
| li: If you are 65 or older and have been a permanent resident for 20 years or more, you may study just the 20 questions marked with an asterisk in the official list. The officer asks 10 of them, and 6 right answers pass | ok | changed | F3/F4/F5 |
| h2: Practice test | ok | keep | own copy, no fact |
| p: Start with a quick 5-question quiz, or take the full test: 20 random questions from the bank. You need 12 correct to pass, like the real test. There is no timer, as in the real interview. | ok | keep | F3/F4/F5 |
| p: The practice test requires JavaScript. The sample questions and section pages work without it. | ok | changed | own copy, no fact |
| button: Start quick quiz: 5 questions | verb first ok | changed | own copy, no fact |
| button: Start full test: 20 questions | verb first ok | changed | F3/F4/F5 |
| h2: Sample questions | ok | keep | own copy, no fact |
| p: Try these ten out loud first. Open “Show answer” to check each one. | ok | keep | own copy, no fact |
| h2: Practice by section | ok | keep | own copy, no fact |
| p: Every question in each section, with all accepted answers and explanations. | ok | keep | own copy, no fact |
| li: American Government (64 questions) | ok | keep | own copy, no fact |
| li: American History (46 questions) | ok | keep | own copy, no fact |
| li: Symbols and Holidays (10 questions) | ok | keep | own copy, no fact |
| p: Eight questions are not listed because the answer depends on where you live or who holds office now: your senator, representative, governor and state capital, and the current Speaker of the House, President, Vice President and Chief Justice. The app asks for your state and shows the current officeholders. | ok | keep | own copy, no fact |
| h2: Study all 128 questions, in English or Spanish. | ok | keep | F3/F4/F5 |
| alt: US Citizen Test Coach icon | ok | keep | screenshot file, docs/assets.md |
| h3: US Citizen Test Coach | ok | keep | own copy, no fact |
| p: Study for the 2025 US naturalization test with the civics questions, a spoken mock interview and English reading and writing practice. No account and no ads. | ok | keep | own copy, no fact |
| li: All 128 civics questions with accepted answers, in English or Spanish | ok | keep | F3/F4/F5 |
| li: A spoken mock interview that listens to your answers | ok | keep | own copy, no fact |
| li: English reading and writing practice | ok | keep | own copy, no fact |
| p: Free to start. All study is free, with 2 mock quizzes, 1 spoken interview, 1 reading round and 1 writing round; one purchase unlocks unlimited simulations, with no subscription. | ok | keep | F6 |
| alt: Captioned App Store image: No Ads. No Subscription. All study content is free, above the home screen with overall progress, the mock quiz and spoken interview, and progress by chapter | ok | keep | screenshot file, docs/assets.md |
| h2: Practice the interview, reading and writing. | ok | keep | own copy, no fact |
| p: No app can promise a pass. | ok | keep | own copy, no fact |
| p: Spoken mock interview | ok | keep | own copy, no fact |
| h3: Answer aloud | ok | keep | own copy, no fact |
| p: Answer the interview questions aloud, and the app listens on your device. | ok | changed | own copy, no fact |
| alt: Captioned App Store image: Practice the Spoken Interview, answer aloud and get feedback, above an interview question with the spoken answer heard and marked right | ok | keep | screenshot file, docs/assets.md |
| p: Reading and writing | ok | keep | own copy, no fact |
| h3: Read aloud, listen and type | ok | keep | own copy, no fact |
| p: Practice the English reading and writing parts of the test. | ok | keep | own copy, no fact |
| alt: Captioned App Store image: English Reading and Writing, read aloud, listen and type, above the reading and writing practice screens | ok | keep | screenshot file, docs/assets.md |
| p: Support & inquiries | ok | changed | own copy, no fact |
| p: For app support or general inquiries, send us a note. | ok | changed | own copy, no fact |
| a: US Citizen Test Coach privacy policy | ok | keep | own copy, no fact |

### `us-citizenship-test/symbols-holidays/index.html` (en-US)

| Text | Rule checks | Outcome | Source |
| --- | --- | --- | --- |
| title: Symbols and Holidays: 10 US Citizenship Test Questions | ≤60: 54 ok | keep | own copy; facts per facts table |
| desc: 10 free US citizenship test practice questions on Symbols and Holidays, with every accepted answer and an explanation. No account. Independent practice. | 120–155: 152 ok | keep | own copy; facts per facts table |
| a: Español | ok | keep | own copy, no fact |
| p: Free section | ok | keep | F6 |
| h1: Symbols and Holidays: US Citizenship Test Practice Questions | ok | keep | own copy; facts per facts table |
| p: 10 practice questions from this part of the 2025 civics test. Answer out loud, then open “Show answer” to check it and read the explanation. | ok | keep | own copy, no fact |
| p: Independent practice. Not affiliated with USCIS or the U.S. government. The official questions and study guide are free on uscis.gov. Read them first; this page does not replace them. | ok | keep | F6 |
| h2: More practice by section | ok | keep | own copy, no fact |
| p: Take the 20-question practice test | ok | keep | F3/F4/F5 |
| li: American Government (64 questions) | ok | keep | own copy, no fact |
| li: American History (46 questions) | ok | keep | own copy, no fact |
| h2: Study all 128 questions, in English or Spanish. | ok | keep | F3/F4/F5 |
| alt: US Citizen Test Coach icon | ok | keep | screenshot file, docs/assets.md |
| h3: US Citizen Test Coach | ok | keep | own copy, no fact |
| p: Study for the 2025 US naturalization test with the civics questions, a spoken mock interview and English reading and writing practice. No account and no ads. | ok | keep | own copy, no fact |
| li: All 128 civics questions with accepted answers, in English or Spanish | ok | keep | F3/F4/F5 |
| li: A spoken mock interview that listens to your answers | ok | keep | own copy, no fact |
| li: English reading and writing practice | ok | keep | own copy, no fact |
| p: Free to start. All study is free, with 2 mock quizzes, 1 spoken interview, 1 reading round and 1 writing round; one purchase unlocks unlimited simulations, with no subscription. | ok | keep | F6 |
| alt: Captioned App Store image: No Ads. No Subscription. All study content is free, above the home screen with overall progress, the mock quiz and spoken interview, and progress by chapter | ok | keep | screenshot file, docs/assets.md |
| h2: Practice the interview, reading and writing. | ok | keep | own copy, no fact |
| p: No app can promise a pass. | ok | keep | own copy, no fact |
| p: Spoken mock interview | ok | keep | own copy, no fact |
| h3: Answer aloud | ok | keep | own copy, no fact |
| p: Answer the interview questions aloud, and the app listens on your device. | ok | changed | own copy, no fact |
| alt: Captioned App Store image: Practice the Spoken Interview, answer aloud and get feedback, above an interview question with the spoken answer heard and marked right | ok | keep | screenshot file, docs/assets.md |
| p: Reading and writing | ok | keep | own copy, no fact |
| h3: Read aloud, listen and type | ok | keep | own copy, no fact |
| p: Practice the English reading and writing parts of the test. | ok | keep | own copy, no fact |
| alt: Captioned App Store image: English Reading and Writing, read aloud, listen and type, above the reading and writing practice screens | ok | keep | screenshot file, docs/assets.md |
| p: Support & inquiries | ok | changed | own copy, no fact |
| p: For app support or general inquiries, send us a note. | ok | changed | own copy, no fact |
| a: US Citizen Test Coach privacy policy | ok | keep | own copy, no fact |

### `uscitizencoach-privacy/privacy.html` (en)

| Text | Rule checks | Outcome | Source |
| --- | --- | --- | --- |
| title: US Citizen Test Coach Privacy Policy | ≤60: 36 ok | changed | own copy; facts per facts table |
| desc: Privacy policy for US Citizen Test Coach, in English and Spanish: no data collected, speech recognition runs on your device, progress stays on it. | 120–155: 146 ok | changed | own copy; facts per facts table |

## Quiz-script strings (generators, `COPY_*["quiz"]`)

Rendered by the quiz script, so not in the page inventory. All keep; `Next question` / `Next` is flagged as not verb-first (a stock control label, developer decides). French and Spanish: native review pending.

| Set | Strings |
| --- | --- |
| CA en | Question {n} of {total} / Next question / See my score / You scored {score} of {total} / Pass. The real test needs 15 correct answers out of 20. / Not a pass yet. The real test needs 15 correct answers out of 20. / Time is up. Unanswered questions count as wrong. / That was a quick quiz. The full test has 20 questions in 45 minutes, like the real one. / Take the full 20-question test / Questions to review / Not correct / Your answer: / No answer / Right answer: / 15 / 45 / This test used 3 of 11 chapters. The app covers all 11 chapters and your province, in English and French, with audio. / Coming soon to the App Store / Try another |
| CA fr | Question {n} sur {total} / Question suivante / Voir mon résultat / Vous avez obtenu {score} sur {total} / Réussi. L’examen réel exige 15 bonnes réponses sur 20. / Pas encore réussi. L’examen réel exige 15 bonnes réponses sur 20. / Le temps est écoulé. Les questions sans réponse comptent comme fausses. / C’était un quiz rapide. Le test complet compte 20 questions en 45 minutes, comme l’examen réel. / Faire le test complet de 20 questions / Questions à revoir / Incorrect / Votre réponse : / Aucune réponse / Bonne réponse : / 15 / 45 / Ce test couvrait 3 chapitres sur 11. L’application couvre les 11 chapitres et votre province, en français et en anglais, avec audio. / Bientôt sur l’App Store / Recommencer |
| US en | Question {n} of {total} / Next question / See my score / You scored {score} of {total} / Pass. The real test needs 12 correct answers out of 20. / Not a pass yet. The real test needs 12 correct answers out of 20. /  / That was a quick quiz. The full test has 20 questions and needs 12 correct answers, like the real one. / Take the full 20-question test / Questions to review / Not correct / Your answer: / No answer / Right answer: / 12 / 0 / and / True / The app covers all 128 questions, your state and current officeholders, a spoken mock interview and reading and writing practice. / Coming soon to the App Store / Try another |
| US es | Pregunta {n} de {total} / Siguiente pregunta / Ver mi puntaje / Obtuvo {score} de {total} / Aprobado. El examen real requiere 12 respuestas correctas de 20. / Todavía no aprueba. El examen real requiere 12 respuestas correctas de 20. /  / Fue un cuestionario rápido. El examen completo tiene 20 preguntas y requiere 12 respuestas correctas, como el real. / Haga el examen completo de 20 preguntas / Preguntas para repasar / Incorrecta / Su respuesta: / Sin respuesta / Respuesta correcta: / 12 / 0 / y / False / La app cubre las 128 preguntas, su estado y los funcionarios actuales, una entrevista de práctica hablada y práctica de lectura y escritura. / Próximamente en la App Store / Probar con otras |

## LanguageTool (`/opt/homebrew/bin/languagetool --level PICKY`)

Run after the edits on every title, description and page row (privacy policy body text excluded: unchanged), by language: `en-CA` (home, CA, Blackjack, privacy titles and descriptions), `en-US`, `fr-CA`, `es`. Fixed: US pages "enquiries" to "inquiries" (US spelling); US serial comma in the hero; US "Answer ... aloud, and the app listens"; "needs JavaScript" to "requires JavaScript" (CA and US generators); French "gratuits ;" spacing; French "Sachez quoi réviser" to "Sachez ce qu’il faut réviser"; Blackjack list "Practice with hints" (three sentences starting with "Practice") to "Train with hints first, then without them".

Recorded as false positives or accepted, no change:

| Flag | Where | Disposition |
| --- | --- | --- |
| Spelling: PANGUFU, LTD, Purrcade, IRCC, USCIS, English, Video, Poker | all languages | brand, acronym or English store name |
| `enquiries` (en-CA) | Support blocks on `/`, CA and Blackjack pages | valid Canadian usage, kept; US pages use "inquiries" |
| PUNCTUATION_PARAGRAPH_END | image `alt` texts, list items | no final full stop by design |
| SENTENCE_WHITESPACE, `forcitizenship`, `ENGLISH_WORD_REPEAT_BEGINNING` | headings split by `<br>` (home h1, "Free to start.<br>No subscription.", Blackjack "No account. No ads.<br>No data collected.") | text extraction joins the lines; the page renders a line break. The three "No" lines are an intended parallel |
| EN_REPEATEDWORDS_NEED | CA hero and quiz intro ("you need 15", "You need 15") | the same fact stated twice on purpose |
| fr NOMBRES_EN_LETTRES (27, 28, 112) | chapter descriptions and intros start with the count | count-first is deliberate for search snippets |
| fr PREP_PAYS `sur canada.ca` | notice line | "sur canada.ca" is correct for a website |
| fr PAS_DE_VIRGULE_STYLE, VOIR_REGARDER (`Voyez`), VIRG_NON_TROUVEE | "Gratuit pour commencer…", "Voyez quelles parties…" | style suggestions; native review pending |
| es | only brand and acronym spelling flags | none left |

## Rules and exceptions

- Titles at most 60 characters and descriptions 120–155 characters on all 22 published pages (checked by script after the final edit; the checks column above shows each).
- No "official", "IRCC" or "USCIS" in any title. "Thoughtful(ly)" and "Made for a little more" removed from the Blackjack page and "Made for a little more" from `/`. On `/` the developer kept the brand line "Small apps. Thoughtfully made." and the caption "Care in every detail" (2026-10-28), with the keywords in the title and description instead.
- Buttons start with a verb: quiz buttons changed ("Start quick quiz", "Start full test"; French "Commencer…", Spanish "Empiece…"). **Flagged, kept:** `About the app →` on the home cards (wording fixed by plan Phase 3) and the quiz control `Next question` / `Siguiente pregunta` / `Question suivante`.
- Question text is not site copy: the CA/FR question rows changed only because the app banks moved since the pages were last generated (see the Phase 6 report for counts); nothing was edited on the site.
- Straight apostrophe in the English chapter title `Canada's History` comes from the app bank; fix in `../citizencoach`, not here.
- Privacy pages: description added and titles shortened in the source repos (`../catgame`, `../cardtrainer`, `../citizencoach`, `../uscitizencoach`, each `docs/privacy.html`), copied here, `cmp` identical. Head-only change, no new effective date. The four app repos are not committed.

## Verification

- `python3 -m unittest discover -s tools -p 'test_*.py'` (cwd: repo root): 26 tests OK, exit 0.
- Generators re-run after the last edit: `python3 tools/make_citizenship_pages.py` (+ `--lang fr`), `python3 tools/make_us_citizenship_pages.py` (+ `--lang es`).
- `cmp ../<repo>/docs/privacy.html <site copy>` identical for all four.
- Working-tree snapshot after the last edit: tree `495b2ff696a97dc85da2dbb0996885458710f633`.
