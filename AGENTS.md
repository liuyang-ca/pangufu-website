# AGENTS.md

PANGUFU company website: a static, dependency-free homepage for https://pangufu.ca,
deployed to GitHub Pages by `.github/workflows/pages.yml`. Plans:
`docs/plan-seo-practice-pages.md` (current), `docs/plan-company-homepage.md` (history).

## Repo rules

- Personal project, no JIRA, no second developer. Trunk is `main`; work and commit
  directly on `main`, no branches or PRs. Push only when the developer asks.
  This opts the repo out of the global block-trunk-commit guard — marker, do not
  remove: `claude:allow-trunk-commit`
- Published files: `index.html`, `styles.css`, `robots.txt`, `sitemap.xml`, `assets/`,
  the app page directories `canada-citizenship-test/` and `fr/` (its French pages), and the directories
  `purrcade/`, `blackjack-video-poker-coach/` (app page plus privacy policy),
  `citizen-coach-privacy/`.
  `mockups/`, `docs/` and the git-ignored `output/` are not published.
