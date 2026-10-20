# AGENTS.md

PANGUFU company website: a static, dependency-free homepage for https://pangufu.ca,
deployed to GitHub Pages by `.github/workflows/pages.yml`. Plan:
`docs/plan-company-homepage.md`.

## Repo rules

- Personal project, no JIRA, no second developer. Trunk is `main`; work and commit
  directly on `main`, no branches or PRs. Push only when the developer asks.
  This opts the repo out of the global block-trunk-commit guard — marker, do not
  remove: `claude:allow-trunk-commit`
- Published files: `index.html`, `styles.css`, `assets/`, and the privacy policy
  directories `purrcade/`, `blackjack-video-poker-coach/`, `citizen-coach-privacy/`.
  `mockups/`, `docs/` and the git-ignored `output/` are not published.
