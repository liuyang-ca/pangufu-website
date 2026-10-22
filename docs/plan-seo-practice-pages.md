# SEO pages: free practice tests that lead to the apps

Status: Phases 1–3 built and reviewed 2026-10-22, committed (`2db9f10`), not pushed. Phase 3b (developer feedback) built and reviewed 2026-10-22, committed, not pushed (French copy unreviewed by a French speaker). Phase 4 is the developer's; Phase 5 not started. Supersedes the single-app layout of
`docs/plan-company-homepage.md` (that plan stays as history).

## Goal

Get Google search traffic to the apps before and after launch. Google takes weeks to
months to rank a new page, so the pages go up now, before the apps are live, and gain
App Store links on launch day.

The main page is a **free Canadian citizenship practice test** in English and French that
ends with a pointer to Canada Citizenship Test Coach. A blackjack basic strategy chart for
Blackjack & Video Poker Coach is optional and last (see Phase 5).

## What the search results show (2026-10-21, Google Canada)

- **"canadian citizenship practice test free":** public libraries (Richmond, Toronto),
  small quiz sites (citizenshipcounts.ca, canoo.ca, mycanadianway.com, mycitizen.ca),
  canada.ca and a Google Play app. Every ranking page is an **interactive quiz with the
  questions on the page**. Small sites rank, so a new page can compete.
- **"examen de citoyenneté canadienne gratuit en ligne":** fewer and weaker sites
  (devienscitoyen.ca, canoo.ca/fr, examendecitoyennete.ca). The French page is the
  better chance per hour of work. The app's own research found the same gap in the
  App Store (`../citizencoach/docs/app-store-listing.md`, "Both languages").
- **"blackjack basic strategy chart":** Blackjack Apprenticeship, Wizard of Odds,
  BlackjackInfo: old, strong sites. A new page is unlikely to reach page 1.

## Decisions

1. **Questions shown on the site: the free chapters only.** The app gives away chapters
   1–3 (`rights`, `who-we-are`, `history`: 167 questions in each language, per
   `../citizencoach/docs/plan-citizen-coach.md` item 8). The site shows the same ones, so
   it gives away nothing the app sells. Chapters 4–11 and the province questions appear
   only as "in the app".
2. **No `current: true` questions** (officeholders). They go stale on the site, where
   no "checked on" date is shown.
3. **Generated, not hand-written.** A standard-library Python script reads
   `../citizencoach/CitizenCoachKit/Sources/CitizenCoachKit/Resources/questions-{en,fr}.json`
   and writes static HTML. The generated HTML is committed, so the published site stays
   dependency-free with no build step. Re-run the script when the app's questions change.
4. **The question text is the app's own wording**, already checked against the guide by
   `../citizencoach/tools/check_questions.py` (own words, 8-word overlap rule). Never
   copy text from *Discover Canada* onto the site: it is Crown copyright.
5. **Not official.** Every citizenship page says "Independent practice. Not affiliated
   with IRCC or the Government of Canada" and links the free official guide. No canada.ca
   colours (`#284162`, `#26374A`), no "official" or "IRCC" in titles (same rule as the
   App Store listing, guidelines 2.3 and 5.2).
6. **Purrcade gets no app card or page** (owner decision in the homepage plan). Revisit
   only if the owner asks. Its privacy page `/purrcade/privacy.html` stays published:
   App Store Connect links to it.

## Site structure (redesign)

The current site is one long page about Blackjack & Video Poker Coach. It becomes a small
multi-app site, keeping the Studio shell (nav, footer, `styles.css` tokens).

| URL | Page |
| --- | --- |
| `/` | Company intro plus one card per app (CitizenCoach first, then CardTrainer). Each card links to its app page. |
| `/canada-citizenship-test/` | **Main SEO page.** "Free Canadian Citizenship Practice Test (2026)": a 20-question timed quiz, how the real test works, and a block about the app. |
| `/canada-citizenship-test/<chapter>/` | One page per free chapter (3): every question in that chapter, answers behind "Show answer". Long-tail searches such as "citizenship test history questions". |
| `/fr/examen-citoyennete-canadienne/` and `/fr/examen-citoyennete-canadienne/<chapter>/` | The same in French. |
| `/blackjack-video-poker-coach/` | App page, moved from today's home page content. `privacy.html` stays where it is. |
| `/citizen-coach-privacy/privacy.html`, `/purrcade/privacy.html` | Unchanged: the URLs are in App Store Connect. |
| `/sitemap.xml`, `/robots.txt` | New. |

Each section is a directory with `index.html`, so GitHub Pages serves the clean URL.
CitizenCoach pages use the app's lake-blue accent (`#1F4E8C`, `#3E8EF0` on dark, from
`../citizencoach/docs/theme.md`) through a page-level CSS variable. CardTrainer keeps lime.

## Page rules (every page)

- Unique `<title>` and `<meta name="description">`, `<link rel="canonical">`, one `<h1>`.
- English and French pages link each other with `<link rel="alternate" hreflang>` (en-CA,
  fr-CA, and x-default pointing to the English page) and a visible language switch.
- Chapter pages show every question in the HTML, readable without JavaScript, with the
  answer and explanation in a `<details>` "Show answer". The main page shows 10 fixed
  sample questions the same way, plus links to the chapter pages; JavaScript only adds
  the timed 20-question mode and scoring.
- Mobile first: most searchers are on a phone. 16px side gutter, no horizontal scroll.
- `MobileApplication` JSON-LD on the app block, only once the app is live (no price or
  rating data before then).
- No analytics, cookies or forms (homepage plan rule). Measure traffic with Google Search
  Console and App Store Connect instead (Phase 4).

## Quiz behaviour (`/canada-citizenship-test/`)

- Mirrors the real test as the app describes it: 20 questions, 45 minutes, pass at 15 of 20.
- "Start practice test" draws 20 random questions from the free chapters, shows one at a
  time, then a score with every wrong answer, the right one and its explanation.
- The result screen points to the app: "This test used 3 of 11 chapters. The app covers
  all 11 chapters and your province, in English and French, with audio." Until the app is
  live, the button reads "Coming soon to the App Store" with no link (README rule: verify
  public availability first).

## Phases

### Phase 1: Restructure the site

- Move the CardTrainer content to `/blackjack-video-poker-coach/index.html`; turn `/` into
  the company intro plus app cards; add a CitizenCoach app page shell at
  `/canada-citizenship-test/` (app block only, quiz comes in Phase 2).
- Add `robots.txt` and a hand-written `sitemap.xml`.
- Update `.github/workflows/pages.yml` "Stage production files", the AGENTS.md
  "Published files" list and README.md (Hosting, Privacy policies) for the new directories
  and files.
- **Done when:** every old URL still works (`/` and the three privacy pages), and the
  homepage plan's local checks pass on every new page: Chromium at 1440×1000, 390×844 and
  320 px with no horizontal scroll, 200% text zoom, no broken links.

### Phase 2: English practice test

- `tools/make_citizenship_pages.py` (standard library only): reads the app's JSON, keeps
  free-chapter, non-`current` questions, and writes the three chapter pages whole. In the
  hand-written main page it replaces only the text between
  `<!-- generated:questions:start -->` and `<!-- generated:questions:end -->`: the 10
  sample questions (fixed ids listed in the script) and a
  `<script type="application/json" id="question-data">` block with all 167 for the quiz. It
  also rewrites `sitemap.xml` from the list of published pages.
- `tools/test_make_citizenship_pages.py` (`unittest`): only free chapters, no `current`
  question, each question's right answer survives, only the marked block of the main page
  changes, output is stable across runs.
- Quiz script inline in the page, no library.
- **Done when:** the generator test passes, the quiz scores a run correctly in a browser,
  the page works with JavaScript off (questions and answers readable).

### Phase 3: French pages

- Same generator with `questions-fr.json` and French copy; hreflang pairs both ways.
- French copy written for Canadian French ("examen de citoyenneté", "test pratique").
  The app block uses the fr-CA store name `Coach Test Citoyenneté Canada`
  (`../citizencoach/docs/app-store-listing.md`).
- **Done when:** every English page has its French pair and back-links; the developer
  reads the French copy (no French speaker available, so note it as unreviewed).

### Phase 3b: Make the two apps consistent and fill the home page

Developer feedback on the local preview, 2026-10-22: the text reads too big on the new
pages; the two apps are shown differently (status, tag line, button, app page); the
citizenship pages have no screenshots; the home page is thin now that the CardTrainer
screenshots moved off it. Builds on Phases 1–3 (commit `2db9f10`).

1. **Smaller headings on content pages only.** Add `content-page` to the `<body>` class
   of every page that loads `styles.css`, except `/` (the citizenship pages already have
   `class="theme-citizen"`; the three privacy pages carry their own styles and are left
   alone). Under it, `.page-intro h1` is `clamp(30px, 4.5vw, 44px)` (today
   `clamp(32px, 6vw, 56px)`) and every `h2` (`.section-heading`, `.support`,
   `.principles`, `.prose`) is `clamp(24px, 3vw, 32px)` (today `clamp(36px, 4vw, 48px)`,
   `.prose` `clamp(28px, 4vw, 36px)`, and 38–39px under 800px). Put the rule after the
   `max-width: 800px` block, with a selector that outranks those, e.g.
   `.content-page :is(.section-heading, .support, .principles, .prose) h2`, so it holds
   at every width. Body text and the home page are unchanged. Chapter pages get the
   class from the main page's shell (`chapter_page()` in `tools/make_citizenship_pages.py`
   copies everything up to `<main>`).
2. **One status for both apps:** "Coming soon" on home cards, "Coming soon to the App
   Store" on app pages, "Bientôt sur l’App Store" in French (curly apostrophe, as the
   pages have it today). CardTrainer's page and card drop "In development". Neither app
   is on the App Store yet.
3. **One card pattern on the home page** (`index.html`, both cards the same):
   - Tag line: `Study · iPhone & iPad` (CitizenCoach), `Learn · iPhone & iPad`
     (CardTrainer). "English and French" moves into CitizenCoach's description.
   - Primary button `About the app →`: CitizenCoach to `/canada-citizenship-test/#app`,
     CardTrainer to `/blackjack-video-poker-coach/`.
   - CitizenCoach adds a text link `Free practice test →` to `/canada-citizenship-test/`.
     CardTrainer gets none until Phase 5's chart exists.
   - One captioned screenshot in each card, as on the old home page:
     `assets/citizencoach-study.jpg` and the existing `assets/cardtrainer-practice.jpg`.
   - Layout: one card per row, full width, with the CardTrainer page's featured-card
     markup (`.app-card` holding `.feature-copy` and `figure.app-shot`), so desktop shows
     copy left and image right and mobile stacks them. Drop `app-card-simple` and the
     two-column `.app-grid` on the home page; two image cards side by side are too
     narrow.
4. **One shared-values strip on the home page**, between the apps and support, true of
   both apps (checked against both privacy policies and listings, 2026-10-22): free to
   start, one purchase with no subscription, no ads, no account, no data collected.
   Reuse the `.principles` section style already in `styles.css`. No invented numbers
   or reviews.
5. **Same app section on both apps' pages.** The citizenship main page's app block (the
   `apps-section`, which the generator copies into every chapter page) takes the
   CardTrainer page's structure, with `id="app"`: a featured card (icon, tag line, name,
   description, three feature points, purchase note, status, privacy link, one
   screenshot), then a `training-section` with two panels, each with one screenshot.
   Facts come from `../citizencoach/docs/app-store-listing.md` only; French wording
   follows its French listing. Theme stays lake blue.
   - Tag line `Study · iPhone & iPad` / `Étude · iPhone et iPad`, as on the home card.
   - Feature points: all 11 chapters of the guide plus your province or territory;
     study and listen in English or French; timed mock tests of 20 questions in 45
     minutes, with every answer explained.
   - Purchase note: free to start with the first three chapters and two mock tests; one
     purchase unlocks everything, no subscription.
   - Panels, in `.training-card` markup with `mode-number`, `app-kind`, `h3`, one
     sentence and the screenshot; no SVG icon and no `mode-detail` line (nothing to claim
     there). 01: section quizzes, a quiz after each section with a short explanation for
     every answer (`03-quiz`). 02: readiness by chapter, which parts of the guide you
     already know (`05-readiness`).
6. **Screenshots** from `../citizencoach/scratch/appstore-screenshots/captioned/<lang>/iphone/`:
   `01-study.png` (featured), `03-quiz.png` and `05-readiness.png` (panels). English pages
   use `en`, French pages `fr`. Save as `assets/citizencoach-<name>.jpg` and
   `assets/citizencoach-<name>-fr.jpg`, 680 px wide, JPEG quality 84, like CardTrainer's,
   and add each to `docs/assets.md` with its source. Look at each image for personal
   information before copying. Descriptive `alt` text in the page's language.
7. Re-run the generator for both languages so chapter pages pick up items 1, 2, 5 and 6.

- **Done when:** the generator tests pass; both home cards have the same parts in the same
  order; every page states the same status; the homepage plan's local checks pass on `/`,
  both citizenship main pages, one chapter page and the CardTrainer page (Chromium
  1440×1000, 390×844, 320 px with no horizontal scroll, 200% text zoom, no broken links or
  images); each new image is under 200 KB.

### Phase 4: Launch tasks (developer, outside this repo)

1. Verify `pangufu.ca` in **Google Search Console** (DNS TXT record) and submit
   `sitemap.xml`. Do this as soon as Phase 2 is live: it starts the indexing clock.
2. When an app is live: replace "Coming soon" with the App Store link carrying a campaign
   token (`?pt=<provider id>&ct=web-practice-test`), so App Store Connect → Analytics →
   Sources shows installs from the site. Add the `apple-itunes-app` Smart App Banner meta.
3. Ask for links: library citizenship pages (Richmond, Toronto) and settlement agencies
   list free practice tests. A free, ad-free, bilingual test is a reasonable ask.
4. Check Search Console after 4 and 8 weeks: queries, impressions, position.

### Phase 5 (optional): Blackjack basic strategy chart

- `/blackjack-video-poker-coach/basic-strategy-chart/` generated from
  `../cardtrainer/CardTrainerKit/Sources/CardTrainerKit/Resources/Charts/`, as an HTML
  table, with the app block.
- Low expected search traffic (see the search results above). Do it only if Phases 1–3
  are live and there is time; it is still useful as a link target for forum posts.

## Quality and risks

- **Accessibility:** each question is a `<fieldset>` with a `<legend>` and native radio
  buttons, usable by keyboard. The score is announced through an `aria-live` region; the
  45-minute timer is shown but not announced every second. Colour is never the only sign
  of right or wrong.
- **Performance:** no fonts, libraries or tracking; the quiz data is about 170 questions
  inline, so each page stays one small HTML file plus `styles.css`.
- **Security:** static files only, no forms, no third-party scripts.
- **Rollback:** `git revert` and push; GitHub Pages redeploys the previous files.
- **Risks:** Google may take months to rank a new domain, and may never for the blackjack
  chart. The site goes stale when the app's free-chapter questions change: re-run the
  generator with each app content release. The French copy is unreviewed by a French
  speaker.

## Out of scope

Blog, paid ads, analytics scripts, accounts, comments, chapters 4–11 on the site, Purrcade.

## Run decisions (`/impl-plan auto`, 2026-10-21)

- **Free chapters only** (Decision 1) stands: it gives away nothing the app sells, and
  167 questions per language is more than most ranking quiz sites show for free.
- **Stay on `pangufu.ca`.** A keyword domain costs money and a later move needs 301
  redirects, which GitHub Pages cannot do; the developer can still choose one later.
- **This run builds Phases 1–3.** Phase 4 is the developer's (Search Console, App Store
  links once live). Phase 5 is skipped: the plan sets it after Phases 1–3 are live.
- **Commit, do not push.** The developer changed the run on 2026-10-21 ("stop before the
  push"): they preview the pages locally (`python3 -m http.server 8000` in the repo root)
  before a push to `main` publishes them through GitHub Pages. The new pages say "Coming
  soon", with no App Store link.

## Run decisions (`/impl-plan auto`, Phase 3b, 2026-10-22)

- **Build Phase 3b only** (`phases=3b`); Phases 1–3 are committed in `2db9f10`.
- **Commit, do not push** still holds: the developer previews before a push publishes the
  site. Report the push command instead.
- **Study screenshots at JPEG quality 68**, not 84: at 84 they were 247 KB and 262 KB,
  over the 200 KB limit. The other four are quality 84. `docs/assets.md` records it.
- **Home cards in `.app-list`** (one column) with a `.card-actions` row for the button and
  text link; `.app-grid` and `.app-card-simple` had no other user and are removed.
- **Panel labels keep clear of the number:** `.training-card .app-kind` gets right padding,
  since the citizenship panels have no icon and a wrapped label could run under "01".
- **Home values strip leaves out "progress stays on your device"**: not checked for
  CardTrainer, so only the facts true of both apps are stated.
