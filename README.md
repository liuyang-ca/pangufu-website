# PANGUFU website

A static, dependency-free company homepage for GitHub Pages.

## Preview locally

From this directory, run:

```sh
python3 -m http.server 8000
```

Then open <http://localhost:8000>.

## Citizenship practice pages

`canada-citizenship-test/<chapter>/index.html` and the block between the
`generated:questions` markers in `canada-citizenship-test/index.html` (and the same pages under
`fr/examen-citoyennete-canadienne/`, in French) are generated from the
app's question files (free chapters only, no `current` questions), and so is the
citizenship part of `sitemap.xml`. Do not edit those by hand. After the app's questions
change, run from this directory, then check the diff:

```sh
python3 tools/make_citizenship_pages.py            # English, reads ../citizencoach/.../Resources
python3 tools/make_citizenship_pages.py --lang fr  # French
python3 tools/make_citizenship_pages.py --resources <folder with questions-*.json and sections-*.json>
python3 -m unittest tools/test_make_citizenship_pages.py
```

The US pages work the same way: `us-citizenship-test/<section>/` and the
`generated:questions` block of `us-citizenship-test/index.html` (and the same under
`es/examen-ciudadania-estados-unidos/`, in Spanish) come from `../uscitizencoach/.../Resources/questions-{en,es}.json`
(every question except the 8 that depend on where you live or who holds office):

```sh
python3 tools/make_us_citizenship_pages.py            # English
python3 tools/make_us_citizenship_pages.py --lang es  # Spanish, not yet read by a native speaker
python3 -m unittest discover -s tools -p 'test_*.py'
```

The two hand-written Canadian main pages carry the hreflang alternates and the language switch; the
generator points the chapter pages' own alternates at their translation. The French copy has
not been reviewed by a French speaker. `tools/` is not published.

## Hosting

The Pages workflow stages `index.html`, `404.html`, `styles.css`, `robots.txt`, `sitemap.xml`, `assets/`, the app page directories `canada-citizenship-test/`, `fr/`, `us-citizenship-test/`, `es/` and `blackjack-video-poker-coach/`, and the three other privacy policy directories (`purrcade/`, `citizen-coach-privacy/`, `uscitizencoach-privacy/`) into `_site/`, then deploys that directory with GitHub Pages Actions. Configure the repository's Pages source to **GitHub Actions**. The canonical domain is `https://pangufu.ca/`.

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
| US Citizen Test Coach (uscitizencoach) | https://pangufu.ca/uscitizencoach-privacy/privacy.html | `../uscitizencoach/docs/privacy.html` |

The Blackjack & Video Poker Coach directory also holds its app page (`index.html`); only `privacy.html` is copied from the app repository. `purrcade/privacy.html` is published for App Store Connect, but the site has no Purrcade page or card.

Copy each source policy into its matching directory here when its content changes.
Deploy these pages before releasing app builds or saving App Store Connect metadata
that uses the new URLs. Existing public policy repositories can remain available for
older app versions.
