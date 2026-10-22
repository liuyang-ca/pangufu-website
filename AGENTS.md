# AGENTS.md

PANGUFU company website: a static, dependency-free homepage for https://pangufu.ca,
deployed to GitHub Pages by `.github/workflows/pages.yml`. Plans:
`docs/plan-seo-practice-pages.md` (current), `docs/plan-company-homepage.md` (history).

## Repo rules

- Personal project, no JIRA, no second developer. Trunk is `main`; work and commit
  directly on `main`, no branches or PRs.
- **Never push on your own, not even after `/review-loop` or a commit.** A push to
  `main` deploys the live site at https://pangufu.ca. The developer first checks the
  change locally, then says to push. Approval for one push does not cover the next.
  This opts the repo out of the global block-trunk-commit guard — marker, do not
  remove: `claude:allow-trunk-commit`
- Published files: `index.html`, `styles.css`, `robots.txt`, `sitemap.xml`, `assets/`,
  the app page directories `canada-citizenship-test/` and `fr/` (its French pages), and the directories
  `purrcade/`, `blackjack-video-poker-coach/` (app page plus privacy policy),
  `citizen-coach-privacy/`.
  `mockups/`, `docs/` and the git-ignored `output/` are not published.
- Generated, never hand-edited: the citizenship chapter pages, the `generated:questions`
  block of both citizenship main pages, and the citizenship URLs in `sitemap.xml`. Edit
  `tools/make_citizenship_pages.py` and re-run it (default English, then `--lang fr`).
  Test: `python3 -m unittest discover -s tools -p 'test_*.py'`.
