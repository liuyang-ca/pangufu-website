# SEO pages: free practice tests that lead to the apps

Status: Phases 1–3 built and reviewed 2026-10-22, committed, not pushed (French copy unreviewed by a French speaker). Phase 4 is the developer's; Phase 5 not started. Supersedes the single-app layout of
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
