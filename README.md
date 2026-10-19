# PANGUFU website

A static, dependency-free company homepage for GitHub Pages.

## Preview locally

From this directory, run:

```sh
python3 -m http.server 8000
```

Then open <http://localhost:8000>.

## Hosting

The Pages workflow stages only `index.html`, `styles.css` and `assets/` into `_site/`, then deploys that directory with GitHub Pages Actions. Configure the repository's Pages source to **GitHub Actions**. The canonical domain is `https://pangufu.ca/`.

The website can launch while the app is in development. Before replacing that label with a download link, verify public App Store availability. The Apple Canada lookup returned no results on 2026-10-19.
