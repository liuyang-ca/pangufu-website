# US practice test and app page, plus shorter pages

Status: planned 2026-10-28, plan reviewed (`/review-loop doc`, 2026-10-28: 4 MEDIUM, 6 LOW fixed), copy vetting (Copy rules, Phase 6) added and reviewed 2026-10-28 (1 MEDIUM, 2 LOW fixed), search basics (SEO audit, Phases 7–8) added and reviewed 2026-10-28 (4 MEDIUM, 2 LOW fixed); Phases 1–7 built 2026-10-28 (`/impl-plan`, `/review-loop`), committed, not pushed; Phase 6 copy approval and native French/Spanish review are open before the push. **Spanish unreviewed** (Decision 8). Builds on the 2026-10-28 work on
disk (US home card, US privacy page, refreshed screenshots), which this plan keeps.
Follows the pattern of `docs/plan-seo-practice-pages.md` (the Canadian pages); where this
plan is silent, that plan's rules hold.

## Goal

1. Give US Citizen Test Coach the same web presence as Canada Citizenship Test Coach: a
   free **US citizenship practice test** page in English and Spanish that ends with an
   "About the app" section, so the home card gets `About the app →` and
   `Free practice test →`.
2. Cut scrolling on the home page and the two bilingual privacy pages (developer
   feedback, 2026-10-28: "need lots of scrolling").
3. Vet and tighten every line of site copy so it is accurate, precise and draws
   attention (developer request, 2026-10-28). Until now only the question banks were
   vetted, in the app repos. The site's own copy (titles, descriptions, intros, cards,
   "how the test works", app sections, alt text) was checked against the listings while
   it was built, never in one pass against fixed rules, and the French copy was never
   read by a French speaker.
4. Close the gaps in how search engines and link previews read the site (developer
   request, 2026-10-28). See "SEO audit" and Phase 7.

## What the search results show

Not checked yet. Phase 2 starts with one Google US search each for "us citizenship
practice test free" and "examen de ciudadanía americana práctica gratis", noting which
kinds of pages rank (expected, as in Canada: interactive quizzes with the questions on
the page). This informs the page copy only; it does not change the decisions below.

## Measured page lengths (2026-10-28, local preview)

| Page | Body | h1 / first h2 | 1440×900 | 390×844 |
| --- | --- | --- | --- | --- |
| `/` | 16px | 76px / 48px | 3.2 screens | 4.6 screens |
| `/uscitizencoach-privacy/privacy.html` | 17px | 27px / 25.5px | 3.5 screens | 5.5 screens |
| `/canada-citizenship-test/` | 16px | 44px / 32px | 6.0 screens | 9.2 screens |

Body text is a normal size. The length comes from home-page heading sizes and section
padding, and from each privacy page holding the whole policy twice (two languages).

## SEO audit (2026-10-28, local files and live site)

In place on every non-privacy page: one `h1`, a unique `<title>`, a meta description,
`rel="canonical"`, the favicon, `lang` on `<html>`, `alt` on every image. The CA pages
carry hreflang (`en-CA`, `fr-CA`, `x-default`) both ways. `robots.txt` allows all and
names the sitemap; `sitemap.xml` lists all 14 published URLs. `http://` and `www.`
answer 301 (GitHub Pages). No fonts, libraries or tracking, so the pages are light.

Gaps:

- **No Open Graph or Twitter tags** on any page: a shared link shows no image and a
  guessed title. This is about link previews, not ranking.
- **No structured data** (JSON-LD) on any page, so search results cannot show the site
  name "PANGUFU" in place of the domain.
- **Privacy pages** (4) have no meta description, canonical or favicon, and two have 2
  `h1`s (one per language). Phase 6 adds the description and title; Phase 7 the rest.
- **No `404.html`**: a mistyped URL gets GitHub's generic 404 page with no way back.
- **Titles and descriptions** are over the Copy rules' lengths on 9 of 10 pages
  (Phase 6).
- **Indexing unknown.** The CA pages went live 2026-10-22; Search Console is not
  verified yet (the CA plan's Phase 4, the developer's task), so there is no data on
  which pages are indexed or what they rank for. A `site:pangufu.ca` query through
  Firecrawl returned nothing, which proves nothing about Google.

Not worth doing: `<lastmod>` in `sitemap.xml` (14 URLs, all reachable by links from the
home page, so it adds nothing a crawler needs, and a wrong date teaches Google to ignore it), a
meta keywords tag (ignored by Google), FAQ markup (Google shows FAQ
rich results only for well-known government and health sites since 2023), more pages
written for keywords alone, any paid link scheme.

## Copy rules (every page, existing and new)

Phases 2–4 write to these rules; Phase 6 checks every page against them.

- **Accurate.** Every fact (numbers, test rules, free allowances, prices, privacy and
  language claims) traces to one source, recorded in the vetting log: the app's
  `docs/app-store-listing.md`, its privacy policy, its code, or an official page
  (canada.ca for the Canadian test, uscis.gov for the US test) with the date it was
  read. No invented numbers, ratings, reviews or user counts.
- **Precise.** One claim per sentence. Store names exactly as in the listings
  (`Canada Citizenship Test Coach`, `Coach Test Citoyenneté Canada`,
  `US Citizen Test Coach`, `Coach Examen Ciudadanía USA`,
  `Blackjack & Video Poker Coach`). No empty praise ("thoughtfully made", "best",
  "ultimate"); say what the user gets instead. One name per thing on every page.
- **Draws attention.** `<title>` at most 60 characters with the search phrase first
  (Google cuts longer ones); on `/`, the brand first, then what the apps do. `<meta name="description">` 120–155 characters: what the
  page gives, that it is free, and one thing others lack. `h1` matches the search
  phrase; the first paragraph answers the searcher's question in two sentences. Buttons
  start with a verb. Measured 2026-10-28: 9 of the 10 non-privacy pages break the title
  or description limit (titles up to 100 characters, descriptions up to 191); only
  `/canada-citizenship-test/who-we-are/` passes.
- **Allowed claims only.** No "official", "IRCC" or "USCIS" in titles; every citizenship
  page carries the not-affiliated line; no pass promises (US listing: "No app can
  promise a pass"); no copied *Discover Canada* or uscis.gov prose; "Coming soon" until
  each app is live.
- **Clean language.** LanguageTool (`languagetool --level PICKY -l <lang>`, installed at
  `/opt/homebrew/bin/languagetool`) with `en-CA`, `en-US`, `fr-CA` or `es` by page; every flag fixed or recorded as a false
  positive. Canadian spelling on Canadian pages ("practise" as a verb), US spelling on
  US pages. French and Spanish stay marked unreviewed until a native speaker reads them.
- **Question text is not site copy.** Questions, answers and explanations come from the
  app banks, vetted in their repos (`../citizencoach/tools/check_questions.py`;
  `../uscitizencoach/docs/text-vetting-2026-10-24.md`). A problem found in one is fixed
  in the app repo and regenerated, never edited on the site.

## Decisions

Defaults chosen by the agent; the developer can change any of them before Phase 2.

1. **Questions shown: every civics question except the 8 that vary.** The app gives all
   study away free (`../uscitizencoach/docs/app-store-listing.md`, "FREE AND PAID"), so
   showing the bank gives away nothing the app sells. Left out: the 4 `local` questions
   (q023, q029, q061, q062: your senator, representative, governor, capital) and the 4
   `current` officeholder questions (q030, q038, q039, q057), which go stale on a page
   with no "checked on" date. The pages say these 8 depend on where you live or who holds
   office now, and that the app asks for your state. 120 questions per language. All 8 are
   in `gov-system`, so the section pages hold 64 (government), 46 (history) and 10
   (symbols and holidays).
2. **Three section pages, grouped as the official list is:** American Government
   (`gov-principles`, `gov-system`, `gov-rights`), American History (`history-colonial`,
   `history-1800s`, `history-recent`), Symbols and Holidays (`symbols`, `holidays`).
   Same as the Canadian site's three chapter pages. The unit-to-section map lives in the
   generator.
3. **Quiz rules follow the 2025 test as the app states it:** up to 20 questions, 12 right
   to pass (`TestRules.standard`, listing line "Mock quizzes of 20 questions: 12 right
   answers pass"). No timer: the real interview has none. Two starts, as on the Canadian
   page: "Quick quiz: 5 questions" and "Full test: 20 questions".
4. **Multiple choice from the app's own `choices`.** The right option is built as the
   app builds it (`../uscitizencoach/USCitizenCoach/QuizViewModel.swift`, `make` and
   `joined`), so the site and the app agree: pick `required` distinct accepted answers at
   random, keep them in bank order, and join them: `A and B`, `A, B, and C` in English;
   `A y B`, `A, B y C` in Spanish (no serial comma). Shuffle it in with the three
   `choices`. The generator ships every accepted answer's `text` per question and the
   quiz script picks at quiz start, like the app. Section pages show **every accepted answer** behind
   "Show answer", with "Give N of these" when `required` > 1, plus the explanation.
5. **Generated, not hand-written.** New `tools/make_us_citizenship_pages.py` (standard
   library) reads `../uscitizencoach/USCitizenCoachKit/Sources/USCitizenCoachKit/Resources/questions-{en,es}.json`.
   It imports `esc`, `script_json`, `update_sitemap`, `START`/`END` and `QUIZ_JS` from
   `tools/make_citizenship_pages.py` rather than copying them. The marked-block
   replacement sits inline in that file's `generate()`: move it into a small shared
   function both scripts call. `QUIZ_JS` hard-codes `var PASS = 15, MINUTES = 45;`: read
   both from the generated `T` object instead (US: `MINUTES` 0 = no timer), and add the
   US option-building step behind a flag in the data. After a re-run the Canadian pages
   differ only inside the emitted quiz script, its 11 tests stay green, and its 5- and
   20-question quizzes still time and score as before in a browser. `update_sitemap` only replaces URLs under the language's main page, so the
   Canadian entries are safe.
6. **URLs:** `/us-citizenship-test/` with `/us-citizenship-test/<section>/`
   (`government`, `history`, `symbols-holidays`); Spanish
   `/es/examen-ciudadania-estados-unidos/` with `gobierno`, `historia`,
   `simbolos-feriados`. hreflang `en-US`, `es-US`, x-default the English page.
7. **Not official.** Every US page says "Independent practice. Not affiliated with USCIS
   or the U.S. government." and links the free official questions on uscis.gov. No USCIS
   seal, flag-and-eagle imagery or government blues; no "official" or "USCIS" in titles
   (App Store guidelines 2.3 and 5.2, same as the listing). The question wording is the
   app's, which follows the public USCIS list; explanations are the app's own.
8. **Spanish pages ship with the English ones but are flagged.** The app's Spanish is an
   AI translation awaiting a native-speaker check (`../uscitizencoach/docs/plan-spanish-text-vetting.md`).
   The plan status and the push report say "Spanish unreviewed"; the developer decides
   at push time whether to publish `/es/` or hold it back (drop it from the workflow
   staging and sitemap).
9. **Theme:** the US pages and card keep `theme-citizen` (lake blue) for now, as the home
   card already does. A separate US accent waits for the app's own theme doc.

## Site structure

| URL | Page |
| --- | --- |
| `/us-citizenship-test/` | Main US page: intro, notice, "How the real test works", quiz, 10 sample questions, "Practice by section", `#app` (About the app), support. |
| `/us-citizenship-test/<section>/` | Every question in that section, answers behind "Show answer". |
| `/es/examen-ciudadania-estados-unidos/` and `/es/.../<section>/` | The same in Spanish. |
| `/` | US card gains `card-actions`; `app-jump` gains a US link. |

## Phases

### Phase 1: Shorter pages (no new content)

1. **Home headings.** `.intro h1` (home only) from `clamp(54px, 6vw, 76px)` to
   `clamp(40px, 5vw, 56px)`; under 800px from `clamp(48px, 8vw, 68px)` to
   `clamp(36px, 9vw, 48px)`. `h2` in `.section-heading`, `.support`, `.principles` from
   `clamp(36px, 4vw, 48px)` to `clamp(28px, 3vw, 36px)`, and the fixed 800px overrides
   (`styles.css` `.section-heading h2` 39px, `.principles h2` 38px, `.support h2` 39px)
   to 30px. Every page except `/` has `content-page`, whose rule outranks these, so only
   `/` changes.
2. **Home spacing.** Cut vertical padding by about a third on `/` only, scoped with
   `body:not(.content-page)` because `.apps-section` and `.training-section` are also on
   the app pages: `.apps-section` `53px 0 64px` to `36px 0 44px`; `.intro` `min-height`
   420px to 300px and `padding-block` `58px 64px` to `40px 44px`; `.principles` and
   `.support` padding (today 53/58 and 57/62px) by the same third.
3. **Privacy pages (CA and US, both bilingual).** At the top, under the title of the
   first section, a line of language links: `English · Français` /
   `English · Español`, jumping to `id="en"` and `id="fr"` / `id="es"` on the two
   `<section>`s. `h2` set to `1.15em` (today the browser default 1.5em). Body stays 17px.
   Both stay one URL, since App Store Connect links to it. Edit the **source** copy in
   the app repo (`../citizencoach/docs/privacy.html`, `../uscitizencoach/docs/privacy.html`)
   and copy it to the site, so the pair stays identical (`cmp` passes). Each app repo
   commits its own copy; the US one was committed 2026-10-28 (`f76570e`). No text change,
   so no new effective date. The single-language privacy pages (CardTrainer, Purrcade)
   are left alone.
- **Done when:** `/` at 1440×900 and 390×844 is at least 20% shorter than the table
  above; no horizontal scroll at 320px; 200% text zoom
  still reads; the CardTrainer and CA citizenship pages look as before at 1440 and 390px;
  each privacy page shows its two language links in the first screen at 390px, each
  link lands on its section, and `h2` computes smaller than `h1`; `cmp` passes for both
  source/site pairs.

### Phase 2: US generator and English pages

- Hand-write `us-citizenship-test/index.html` from the Canadian main page's structure
  (`content-page theme-citizen`, page-intro, notice, how-it-works, generated block,
  sections, `#app`, support), with US copy. "How the real test works": the officer asks
  up to 20 of the 128 questions aloud and you answer aloud; 12 right answers pass; the
  interview also tests English reading and writing; people 65+ with 20 years of
  residence study only the 20 marked questions. Facts only from
  `../uscitizencoach/docs/app-store-listing.md` and uscis.gov.
- `tools/make_us_citizenship_pages.py`: keeps non-`local`, non-`current` questions,
  writes the three section pages whole, replaces only the
  `<!-- generated:questions:start/end -->` block of the main page (10 fixed sample ids
  spread over the three sections, plus `<script type="application/json" id="question-data">`
  with all 120), and updates `sitemap.xml`.
- Quiz script: the generator emits the shared `QUIZ_JS` inside the marked block, as for
  Canada, with `PASS` 12 and no timer (Decision 5); result note: "The app covers all 128 questions, your state and current
  officeholders, a spoken mock interview and reading and writing practice." Status
  "Coming soon to the App Store", no link.
- `tools/test_make_us_citizenship_pages.py` (`unittest`): no `local` or `current`
  question appears; each section page holds exactly its units; every accepted answer of
  a question survives; the quiz's right option matches the app's rule for a
  `required` > 1 question; only the marked block of the main page changes; output is
  stable across runs; the Canadian sitemap entries survive a US run.
- **Done when:** both generators' tests pass; a 5- and a 20-question run score right in a
  browser; the page reads with JavaScript off.

### Phase 3: About the app (`#app`) and home card

- `#app` section in the CardTrainer/CA structure: featured card (icon, `Study · iPhone &
  iPad`, name, description, three feature points, purchase note, status, privacy link,
  one screenshot), then a `training-section` with two panels.
  - Feature points: all 128 civics questions with accepted answers, in English or
    Spanish; a spoken mock interview that listens to your answers; English reading and
    writing practice.
  - Purchase note: all study is free, with 2 mock quizzes, 1 spoken interview, 1 reading
    round and 1 writing round; one purchase unlocks unlimited simulations, no
    subscription.
  - Panels: 01 spoken mock interview (`02-interview`), 02 reading and writing
    (`03-writing`). Featured shot `01-home`.
- Screenshots from `../uscitizencoach/scratch/appstore-screenshots/captioned/{en,es}/iphone/`,
  680px wide JPEG, under 200 KB. English pages reuse the three already on disk
  (`assets/uscitizencoach-home.jpg`, `-interview.jpg`, `-reading-writing.jpg`, from
  `01-home`, `02-interview`, `03-writing`); Spanish pages get the same three with `-es`
  (`assets/uscitizencoach-home-es.jpg` and so on); log each in
  `docs/assets.md`; look at each for personal data.
- Home: the US card gets `.card-actions` with `About the app →`
  (`/us-citizenship-test/#app`) and `Free practice test →` (`/us-citizenship-test/`);
  `app-jump` gets a US link to `#us-citizenship`.
- **Done when:** the three home cards have the same parts in the same order; links land.

### Phase 4: Spanish pages

- Same generator with `--lang es` and `questions-es.json`; Spanish copy in formal
  `usted`, US/Mexican usage, store name `Coach Examen Ciudadanía USA`; hreflang pairs
  both ways and a visible language switch.
- **Done when:** every English page has its Spanish pair and back-links; status notes
  the Spanish as unreviewed (Decision 8).

### Phase 5: Publishing files

- `.github/workflows/pages.yml` "Stage production files": add `us-citizenship-test` and
  `es` to the `cp -R` line (drop `es` if Decision 8 holds it back); AGENTS.md "Published files", README.md,
  `sitemap.xml` (via the generator), `robots.txt` unchanged.
- **Done when:** the homepage plan's local checks pass on `/`, both US main pages, one
  section page each, and both privacy pages (Chromium 1440×1000, 390×844, 320px, no
  horizontal scroll, 200% zoom, no broken links or images).

### Phase 6: Copy vetting across the site

Runs after Phases 1–5, so it covers the new US pages too. Scope: every published page
(`/`, the CA main and 3 chapter pages in English and French, the US main and section
pages in both languages, the CardTrainer page, the four privacy pages), plus the
site-only strings in both generators (the `COPY_*` dictionaries).

1. **Inventory.** A throwaway script in the scratchpad (not committed) lists per page:
   `<title>` and meta description with lengths, `h1`/`h2`/`h3`, every paragraph, list
   item, button, link text and `alt`, skipping generated question rows. Output:
   `docs/copy-vetting-2026-10.md`, one table per page with columns text, rule checks,
   outcome (keep / changed / flagged) and source.
2. **Facts table** in the same doc: each distinct fact once, with its source and the
   date read. Re-read the official rules on canada.ca (20 questions, 45 minutes, 15 to
   pass) and uscis.gov (2025 test: up to 20 asked, 12 right to pass).
3. **Rewrite** what fails a rule: titles, descriptions, `h1`s, first paragraphs, card
   pitches, buttons and alt text. Edit the hand-written pages and the generators'
   `COPY_*`, then re-run both generators for both languages. Privacy pages get a meta
   description and a title of at most 60 characters (today 110 and 94 on the two
   bilingual ones): edit the source in each app repo (`../<repo>/docs/privacy.html`, per the
   `README.md` "Privacy policies" table: catgame, cardtrainer, citizencoach,
   uscitizencoach), copy it to the site and confirm with `cmp`. catgame and cardtrainer
   need `/review-loop` before their commit (personal repo rules). A `<head>`-only change needs no new effective date. Policy text changes
   only for a factual error, with a new effective date. Headings and layout are
   Phase 1's.
4. **LanguageTool** on all changed and new copy, by language; record flags.
- **Done when:** every inventory row has an outcome; every page's title is ≤60 and its
  description 120–155 characters; every fact has a dated source; LanguageTool has no
  unrecorded flags; both generators' tests pass; the developer has approved the changed
  titles, descriptions, `h1`s and hero lines (the brand voice is theirs) before any
  push; French and Spanish rows still say "native review pending".

### Phase 7: Search basics (technical SEO)

Runs after Phase 6, so the tags reuse the final titles and descriptions. Fills the gaps
in "SEO audit"; no copy changes.

1. **Open Graph and Twitter tags** on every non-privacy page: `og:type` (`website`),
   `og:site_name` (`PANGUFU`), `og:title` and `og:description` (same text as `<title>` and
   the meta description), `og:url` (the canonical URL), `og:locale` (`en_CA`, `fr_CA`,
   `en_US`, `es_US`), `og:image` (absolute URL, see below) with `og:image:alt`, and
   `twitter:card` `summary_large_image`. Both generators emit them from `COPY_*`; the
   hand-written pages get them by hand.
2. **Share images**: one 1200×630 JPEG per app under 300 KB
   (`assets/og-citizencoach.jpg`, `og-uscitizencoach.jpg`, `og-cardtrainer.jpg`) plus
   `og-pangufu.jpg` for `/`, made with a scratchpad script (not committed) from the app icon and one captioned screenshot already
   in `assets/`; logged in `docs/assets.md`. The French and Spanish pages use their
   app's image unless it carries English text, in which case they get a `-fr`/`-es` one.
3. **JSON-LD**: `WebSite` (`name` `PANGUFU`, `url`) and `Organization` (`name`
   `PANGUFU SOLUTION LTD.`, `url`, `email` `support@pangufu.ca`; no `logo`, since the
   site has only an SVG favicon) on `/` only;
   `BreadcrumbList` (home › practice test › section) on each CA and US section page,
   emitted by the generators. `MobileApplication` stays as the CA plan says: only once
   an app is live, with no price. Validate each page with Google's Rich Results Test
   (paste the HTML, not the URL, before the push).
4. **Privacy pages**: add `rel="canonical"` and the favicon link in each app repo's
   source (`../<repo>/docs/privacy.html`), in the same edit and with the same `cmp` and
   `/review-loop` steps as Phase 6; keep both `h1`s (one per language section, a valid
   pattern).
5. **`404.html`** at the site root: the site header, "Page not found", and links to `/`
   and the two practice tests; add it to
   the workflow's `cp` line and AGENTS.md "Published files". GitHub Pages serves it for
   any missing path.
6. **Internal links**: the CA and US main practice-test pages link to each other once,
   in the support section, with the target named ("US citizenship practice test",
   "Canadian citizenship practice test"). Section pages already link to the other
   sections by name; the US generator does the same.
- **Done when:** every non-privacy page has the 9 tags of step 1, and each `og:image`
  path exists under `assets/`; the Rich Results Test (code tab) shows no errors for `/`
  and one section page per language; the 4 privacy pages have a canonical and favicon
  and match their app repo by `cmp`; `/404.html` renders locally with working links,
  and after the push `https://pangufu.ca/nope` shows it; both generators' tests pass,
  with a test that `og:title` and `og:description` equal the page's title and meta
  description.

### Phase 8: Launch and measure (developer)

Same as the CA plan's Phase 4, extended to the whole site; nothing here needs code.

1. Verify `pangufu.ca` in Google Search Console (DNS TXT record, once covers every
   page) and Bing Webmaster Tools (import from Search Console); submit `sitemap.xml` in
   both.
2. In Search Console, request indexing for `/`, both practice-test main pages and the
   Spanish and French main pages.
3. Ask for links: library citizenship pages (Richmond, Toronto, and US public libraries
   with citizenship corners) and settlement and immigrant-service agencies. One page
   that links to the free test is worth more than any tag here.
4. At app launch: App Store links with `?pt=&ct=web-practice-test`, the Smart App
   Banner (`apple-itunes-app` meta), and `MobileApplication` JSON-LD.
5. Check Search Console after 4 and 8 weeks: indexed pages, queries, impressions,
   position, and Core Web Vitals. Rewrite a title or description only where a page
   has impressions but a low click rate.
- **Done when:** both consoles show the sitemap read with no errors, and the 4- and
  8-week numbers are noted in this plan.

## Quality and risks

- Accessibility, performance and security as in the Canadian plan (fieldset/legend
  radios, `aria-live` score, no libraries, no forms, no tracking).
- **Copyright:** the USCIS question list is a US government work; the app's
  explanations and distractors are its own. Do not copy uscis.gov study-guide prose.
- **Staleness:** re-run the generator with each app content release. Officeholder and
  state questions stay out by design.
- **Spanish unreviewed** (Decision 8); the Canadian French copy is unreviewed too.
- **Title rewrites** keep every URL, so no redirect is needed; check Search Console 4
  weeks after the Phase 6 copy goes live.
- **Two citizenship pages** (CA and US) target different searches and countries. They
  are not translations of each other, so they get no hreflang pair; distinct titles,
  questions and `lang` (`en-CA`/`en-US`) keep them apart.
- **Rollback:** `git revert` and push.

## Out of scope

The 8 local/current questions on the site, reading and writing sentence lists, a 65/20
filter, analytics, App Store links before launch, a US-only accent colour, pushing (needs
the developer's approval for each push), native French and Spanish review (the developer
arranges it), rewording the question banks on the site.
