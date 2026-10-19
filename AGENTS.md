# AGENTS.md

PANGUFU company website: a static, dependency-free homepage for https://pangufu.ca,
deployed to GitHub Pages by `.github/workflows/pages.yml`. Plan:
`docs/plan-company-homepage.md`.

## Repo rules

- Personal project, no JIRA, no second developer. Trunk is `main`; work and commit
  directly on `main`, no branches or PRs. Push only when the developer asks.
  This opts the repo out of the global block-trunk-commit guard — marker, do not
  remove: `claude:allow-trunk-commit`
- Only `index.html`, `styles.css` and `assets/` are published. `mockups/`, `docs/`
  and the git-ignored `output/` are not.
