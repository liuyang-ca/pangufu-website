# PANGUFU website

A static, dependency-free company homepage for GitHub Pages.

## Preview locally

From this directory, run:

```sh
python3 -m http.server 8000
```

Then open <http://localhost:8000>.

## Hosting

The Pages workflow stages `index.html`, `styles.css`, `assets/`, and the three privacy policy directories into `_site/`, then deploys that directory with GitHub Pages Actions. Configure the repository's Pages source to **GitHub Actions**. The canonical domain is `https://pangufu.ca/`.

Pages must be enabled in the repository before the workflow can run. For a new
repository, enable it under Settings → Pages → Source → GitHub Actions, or run
`gh api --method POST repos/liuyang-ca/pangufu-website/pages -f build_type=workflow`.
Then rerun the workflow. For a `configure-pages` HTTP 404, check that Pages is
enabled and that the workflow has permission to access it.

The website can launch while the app is in development. Before replacing that label with a download link, verify public App Store availability. The Apple Canada lookup returned no results on 2026-10-19.

## Privacy policies

| App | Canonical URL | Source |
| --- | --- | --- |
| Purrcade (catgame) | https://pangufu.ca/purrcade/privacy.html | `../catgame/docs/privacy.html` |
| Blackjack & Video Poker Coach (cardtrainer) | https://pangufu.ca/blackjack-video-poker-coach/privacy.html | `../cardtrainer/docs/privacy.html` |
| Canada Citizenship Test Coach (citizencoach) | https://pangufu.ca/citizen-coach-privacy/privacy.html | `../citizencoach/docs/privacy.html` |

Copy each source policy into its matching directory here when its content changes.
Deploy these pages before releasing app builds or saving App Store Connect metadata
that uses the new URLs. Existing public policy repositories can remain available for
older app versions.
