# PANGUFU company homepage

Status: Studio implemented; phases 2–3 verified locally; launch pending. Created 2026-10-19.

## Goal

Build a sleek dark company homepage at `pangufu.ca` using the selected Studio
visual direction: compact company introduction, a Featured app section for CardTrainer, and support plus legal footer.

The owner selected Studio and approved a CardTrainer showcase on 2026-10-19. This
supersedes the earlier company-only direction. Implement and verify locally;
prepare GitHub Pages deployment files. No commit, push, DNS change or deployment
is authorized by this build request.

## Verified starting point

- Checkout: `/Users/liu.yang/git-personal/pangufu-website`; remote:
  `git@github.com:liuyang-ca/pangufu-website.git`. At initial planning the checkout was empty apart from
  Git metadata, on unborn `main` with no initial commit. No repo-local AGENTS.md,
  build configuration, ADRs or test commands existed at initial planning time.
- Personal rules: `/Users/liu.yang/git-personal/agent-config/rules/personal.md`.
  Work on main; push only when requested; selective TDD and proportionate checks.
- Interpret the user's “cardgame” reference as CardTrainer, the local card project
  with documented dark mockups. Reference its `docs/mockups/dark-home.html` and
  `docs/plan-card-trainer.md` under `/Users/liu.yang/git-personal/cardtrainer`.
  Reuse design principles, not fixed phone-screen dimensions or game-specific UI.
- Company name and support address come from the owner. Email setup and its
  verification limits are in `/Users/liu.yang/git-personal/catgame/docs/support-email.md`.
- Purrcade's listing copy is in that repo's `docs/app-store-listing.md`. Treat
  recorded release status as historical; verify public availability before using
  an App Store download call to action.
- Privacy policy hosting was extended after the initial homepage build: the
  canonical Purrcade URL is `https://pangufu.ca/purrcade/privacy.html`, with policies
  for all three apps staged by the Pages workflow. See `README.md` for paths and
  source files. Keep the original public policy repositories for older app versions.

## Content and boundaries

1. Compact navigation: PANGUFU, Training and Support.
2. Short company hero: “Small apps. Thoughtfully made.”, a concise independent
   software company introduction and an action that scrolls to the featured app.
3. Featured app: CardTrainer's public name is **Blackjack & Video Poker Coach**.
   Show its actual icon and three captioned App Store screenshots: blackjack in
   the featured section, then counting and video poker in two training panels.
   Include a concise description of blackjack
   strategy, card counting and video poker practice, with no real money or prizes.
   Use a wide feature row on desktop, stacked on mobile. Source product facts from
   `/Users/liu.yang/git-personal/cardtrainer/docs/app-store-listing.md`.
4. Apple ID 6824308279 returned zero results in Apple's Canadian lookup on
   2026-10-19. Public availability is unverified; show “In development” and no
   download button. Recheck availability before launch.
5. Support: selectable `support@pangufu.ca` and working mailto; footer shows
   PANGUFU SOLUTION LTD., current copyright year and the clearly labelled Coach
   privacy policy link from its listing doc.

Latest owner decision: exclude Purrcade, which the owner considers a test app.
No Purrcade copy, imagery or privacy links on the production site. Existing mockup
history can remain unchanged. Inspect real screen exports for private information
before copying. Resize/compress screenshots and icons for the web; record source
paths in an asset note. No invented reviews, metrics or release claims, internal
Gmail address, forms, accounts, analytics, cookies, backend or payment integration.

## Phase 1 — Two comparable mockups (completed; historical company-only brief)

Create `mockups/studio.html` and `mockups/quiet.html` as independent responsive
HTML/CSS concepts, with a local
comparison index at `mockups/index.html`. Each concept must be a complete page,
not just a hero. Keep content identical; vary composition, typography and accent.

| Concept | Direction | Distinctive treatment |
| --- | --- | --- |
| A — Studio | Sleek dark, CardTrainer-inspired | Near-black canvas, charcoal panels, restrained lime accent, rounded contact treatment, compact bold typography. |
| B — Quiet | Apple-inspired | White/off-white canvas, generous whitespace, large calm typography, restrained neutral actions and a centred company introduction. |

Use original layout and copy, with no Apple logos or copied site assets. Build
interest through typography, spacing, borders and restrained CSS/SVG decoration.
No product imagery or placeholder device renders. Do not add filler sections just
to make a short company introduction longer. No raster assets are required.

Start with system fonts. If choosing Manrope for Studio, vendor the font with its
licence after checking the source licence; avoid remote font dependencies.

Deliver browser-openable concepts, a short comparison note, and matching desktop
and mobile screenshots (1440×1000 and 390×844 viewport sizes). Capture full-page
images too if viewport crops hide key sections. Provide clickable previews so
the owner can inspect scrolling, anchors, focus and mail links.

Done: both complete concepts render at both sizes, show the same content,
and the owner has previews and a recommendation. Stop for the owner's selection
before choosing the production design; a request to combine concepts is valid.

## Phase 2 — Implement the chosen direction

Build static, dependency-light HTML/CSS: `index.html`, `styles.css`, `assets/` and
`README.md` at the repository root. Add JavaScript only for an interaction that
cannot reasonably use HTML/CSS. Keep navigation simple enough to avoid a mobile
menu if possible. Explain local preview with `python3 -m http.server 8000` in README.

Apply the selected design consistently from desktop to mobile. Use semantic
header/nav/main/section/footer, one h1, logical headings, descriptive links,
useful image alt text, visible keyboard focus and at least 44px primary targets.
Meet WCAG AA text contrast, respect reduced motion and support 200% text zoom.
No autoplay video, scroll hijacking, heavy animation or essential hover-only UI.

Set the page title, description, favicon and final canonical URL. Add social
preview metadata only with an actual local preview image and the intended domain.
Use relative asset paths so both a local server and the GitHub project URL work.
Keep mockups and review records out of the production deployment artifact.

Done: selected page is complete, with functional links and no
placeholder claims or broken controls; README explains preview and hosting.

## Phase 3 — Verify and prepare launch

No existing automated gates exist. Use proportionate visual/manual checks under
the personal testing policy; no new framework or test suite solely for static copy.
Serve locally and use available browser tooling to check Chromium and WebKit;
report unavailable engines rather than claiming unrun checks.

Check 390px and 1440px layouts plus 320px reflow, 200% text zoom, no horizontal
overflow, keyboard navigation and focus, contrast, reduced motion, anchors,
mailto links. Verify every production local asset returns
success with no console errors. If decorative images are added later, compress them, specify dimensions and
lazy-load below-fold images. Target at most 1 MB initial transfer for the homepage.
Check company name, support address, the featured app description and release label before release.

Prepare `.github/workflows/pages.yml` to stage `index.html`, `styles.css`,
`assets/`, `purrcade/`, `blackjack-video-poker-coach/` and `citizen-coach-privacy/`
into a clean `_site/` directory, adding any production JavaScript explicitly if
introduced. Upload only `_site/` with GitHub Pages Actions; never
upload the repository root. Ignore `_site/` in Git. This excludes mockups, docs
and review evidence from the public artifact. Set workflow permissions to contents
read, pages write and id-token write; use the GitHub Pages deployment environment.
Resolve supported action versions from official documentation during implementation.
No server runtime or Sites hosting is needed; the user chose GitHub Pages.

Launch checklist, to execute only when the owner requests publication:

- Commit and push only within the owner's authorization; enable Pages and first
  validate the generated `github.io` URL before changing DNS.
- Verify domain ownership in GitHub, set the Pages custom domain, then configure
  Cloudflare website records using current official GitHub Pages instructions.
  Preserve mail MX/TXT records. Document existing website records before changes.
- Enable HTTPS, confirm the canonical host and any www redirect, load the final
  page, and recheck incoming email after DNS changes. Website deployment does not
  itself complete SPF/DKIM/DMARC or change Gmail sending configuration.
- Coordinate App Store Support URL and privacy contact updates separately;
  do not silently edit the catgame or public purrcade repositories.

Rollback: retain the pre-launch website DNS values and previous Pages configuration;
restore them if the domain or HTTPS fails. Keep the existing privacy URL working.
No persisted app data or migrations exist; email authentication is outside scope.

Done: local acceptance checks and release instructions are recorded. Public launch
is tracked separately and is complete only after authorization and live checks.

## Review record

Reviewed 2026-10-19 using `$review-loop` in document mode, default three-round cap.
Scope: this plan only. One MEDIUM finding: deployment packaging was underspecified.
Fixed inline in round 1 with an explicit production allowlist and Pages workflow;
delta re-reviewed, no remaining findings or disputes. User correction applied:
two concepts, sleek dark and Apple-inspired; no Tesla concept.

Verification: reference paths, repository state, design sources and personal rules
checked. No code gates, extra gates or review stamp exist for this empty repository;
no tests apply to this plan. No branch sync required. No fresh pass requested or
required for this document-only review. No commit, push or deployment performed.


## Historical decisions during the mockup run

- 2026-10-19: Owner explicitly chose company-only, no apps yet. Both visual
  concepts retain the same company introduction and support content; app assets
  and app-specific links are removed. This supersedes the original product brief.
- Phase 1 was that run's scope because the visual selection gated phase 2.
  No production design is selected automatically.


## Phase 1 implementation review — 2026-10-19

Built `mockups/studio.html`, `mockups/quiet.html`, `mockups/index.html` and
`mockups/README.md`; captures are in `output/playwright/`. Both concepts now
contain only company copy, support contact and legal footer. Original app assets
were removed following the owner's explicit content selection.

`$review-loop` reviewed the HTML/CSS, comparison notes and revised plan. One
MEDIUM visual finding (overly tight headline tracking) was fixed and captures
refreshed; browser scratch files were excluded with `.gitignore`. One fix round,
converged; no open findings, disputes or debt. No fresh pass requested or required.

Checks: Chromium at 1440×1000 and 390×844, full-page captures, 320px overflow,
visible keyboard focus, support anchors and mailto; source checks confirmed one
h1, valid anchor targets and no app imagery/product links. Diff whitespace check
passed. No automated suite, lint/type gates, extra gates or review stamp are
configured. WebKit, 200% text zoom and full production acceptance remain phase 3.
No commits, pushes, domain changes or deployment performed. The unrelated
`pangufu-website.iml` was preserved.

Review snapshots: T0 `0051e1d3bc347767c0d83630d13631ca2407fd3c`;
initial phase T1 `2a071be77c1f15e6593b39fbff02076fe6e64b7b`;
company-only revision `a641e62c6da65a15984c98785d805b54d8e327a9`.
At that point, phase 2 awaited the owner's choice between Studio and Quiet.


## Latest implementation decision — 2026-10-19

The owner selected sleek dark Studio and asked to build it with both apps. The
company-only constraints in the historical phase 1 brief and its review describe
past mockups; the current Goal and Content sections govern phases 2–3. Keep old
mockups as comparison history. Do not update app repositories or live settings.

- Subsequent owner correction: exclude Purrcade as a test app; feature only
  Blackjack & Video Poker Coach. This supersedes the two-app showcase decision.

- Owner prefers the captioned CardTrainer App Store screenshot; use that export,
  preserving readable captions, instead of a raw screen or generated mockup.

- Owner requested removing Vancouver, BC. Do not include a location in homepage
  copy or metadata; company name and support address are sufficient.

- Remove the redundant “Independent software company” hero label; retain the
  headline, concise company introduction and CTA for a cleaner composition.

- Owner requested a fuller page. Add substantive Coach training-mode panels for
  blackjack basic strategy, Hi-Lo counting and video poker; explain feedback and
  progress, privacy/no account, no ads/subscription and purchase model. Use only
  facts from the app listing. No invented metrics, testimonials or filler sections.

- Use PANGUFU as the public brand and in hero copy. Keep the full legal name
  only in the small footer; no prominent legal suffix in main content.


## Production implementation review — 2026-10-19

Implemented the Studio homepage, full captioned Coach screenshot, app facts,
three training modes, privacy/purchase information and support. PANGUFU is the
public brand; the legal name appears only in the footer. No Purrcade, location
or redundant company-category eyebrow in production copy. Both original mockups
remain historical artifacts.

Review covered root HTML/CSS, assets/provenance, README and Pages workflow against
latest owner decisions. Screenshot cropping found during visual review was fixed;
a final tablet max-height mismatch was fixed inline and verified at 768px with
no overflow and the complete image fitting its frame. No remaining findings or debt.
No fresh pass or stamp required. Local checks: Chromium 1440/390/320, anchors,
assets, mailto, keyboard focus, console, and 2x computed text sizing at 390/320;
reduced-motion CSS present. WebKit unavailable (binary not installed); actual
browser text zoom was not available, so text-size simulation was used.

Production bundle contains only index.html, styles.css and assets; below 1 MB.
Pages workflow prepared and checked against current official GitHub instructions;
no remote settings, DNS, deployment, commits or pushes changed. Live HTTPS/domain
and post-DNS email verification remain launch checks. Unrelated IDE file preserved.

Snapshots: base `3baf6dd962c7db20ad415644e485118a1d0ccab7`, initial build
`a365f31850a0786acf4883618589a8fe906c2f31`, expanded content
`1fdac99c6b968c27fccc19ef057a07cb62d0e000`.

- Added captioned counting and video-poker exports, giving three app screenshots
  overall. Blackjack remains in the featured section; two additional training
  panels show counting and poker. Verified full-image loading and no horizontal
  overflow at 1440, 768, 390 and 320px; visually reviewed the two-panel section.


## Full website review — 2026-10-19

`$review-loop` reviewed production HTML/CSS, workflow, asset sources, README,
current plan and historical mockups (unchanged since their prior review). Review
base is the empty tree because main has no initial commit. The unrelated
`pangufu-website.iml` is excluded. Generated images/evidence received stat and
visual inspection rather than source review.

Converged after one inline fix round: MEDIUM small training-number contrast
improved from 4.05:1 to 7.24:1 against the lightest panel background; MEDIUM stale
current plan content/navigation corrected and historical decisions labelled.
Both fixes re-reviewed as a delta; no open/disputed findings or technical debt.
Contrast reference: https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html

Checks passed: Chromium widths 320/390/600/768/800/1024/1440, no overflow, one h1,
all image loads and anchor targets, no cropped screenshots or page errors;
200% computed text-size check at 390px; external privacy link HTTP 200; production
bundle allowlist, local asset existence and whitespace checks. Reduced-motion CSS
and focus styling remain present. WebKit/Safari and actual browser text-zoom
remain unverified; previous binary availability limitation still applies.
No configured lint/types/test suite, extra gates, review stamp or branch sync.
No fresh pass requested or required for this small static site.

Optional future improvements: open screenshots at full size; create an original
social sharing image before adding social preview metadata. Purrcade remains
excluded per the owner's decision. No commits, pushes, deployment or DNS changes.

Review snapshots: S0 `3d801a37b99b872cba1c016d5aecce26cec63667`;
fix round S1 `98c4a3af5916d10d5d73df2f5ca5abad43c4ab88`.


## Featured screenshot gradient review — 2026-10-19

Reviewed the styles.css background change with `$review-loop auto`: the featured
screenshot frame now uses the same 145-degree grey gradient as the training cards.
No findings, fix rounds or debt. Chromium checks at 1440/768/390 confirmed equal
computed gradients, loaded/full-fit image and no overflow; visual review and
whitespace checks passed. No extra gates or stamp configured. No fresh pass
required for this single styling change; no automated tests added under the
personal-project testing policy. Scope: styles.css and this review record;
unrelated IDE file excluded. Initial review snapshot:
`983bddf8893cfa5d5a0daa76e9a097bdfd071485`. Auto authorizes commit and push.


## Privacy URL migration review — 2026-10-19

Policies for Purrcade, Blackjack & Video Poker Coach, and Canada Citizenship Test
Coach now have canonical paths under `https://pangufu.ca/`. The Pages artifact
includes each policy directory; policy content is unchanged from the app sources.
The homepage links to the CardTrainer policy on the company domain. Original
public policy repositories remain available for older app versions.

One MEDIUM finding fixed: deployment instructions now include the policy
directories. Verification: staged pages return HTTP 200 and match their sources;
CitizenCoach retains English and French. No fresh pass or fingerprint stamp is
required for this small static hosting change. Deployment must precede release of
app builds and App Store Connect metadata using these URLs.
