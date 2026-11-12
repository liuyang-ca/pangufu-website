# Production image sources

Production app imagery is copied from local app exports. The captioned screenshot was checked visually for personal information; none was present.

- `assets/cardtrainer-icon.png` — `cardtrainer/CardTrainer/Assets.xcassets/AppIcon.appiconset/AppIcon.png`, resized to 128px square.
- `assets/cardtrainer-practice.jpg` — `cardtrainer/scratch/appstore-screenshots/captioned/iphone-6.3/01-practise.png`, resized to 680px wide and JPEG quality 84.
- `assets/favicon.svg` — original PANGUFU monogram mark for the site.

- `assets/cardtrainer-counting.jpg` — `cardtrainer/scratch/appstore-screenshots/captioned/iphone-6.3/05-counting.png`, resized to 680px wide, JPEG quality 84.
- `assets/cardtrainer-video-poker.jpg` — `cardtrainer/scratch/appstore-screenshots/captioned/iphone-6.3/07-video-poker.png`, resized to 680px wide, JPEG quality 84.

- `assets/citizencoach-icon.png` — `citizencoach/CitizenCoach/Assets.xcassets/AppIcon.appiconset/AppIcon.png`, resized to 128px square.

- `assets/citizencoach-study.jpg`, `assets/citizencoach-study-fr.jpg` — `citizencoach/scratch/appstore-screenshots/captioned/{en,fr}/iphone/04-listen.png`, resized to 680px wide, JPEG quality 68 (84 gave 251 KB and 263 KB, over the 200 KB limit).
- `assets/citizencoach-quiz.jpg`, `assets/citizencoach-quiz-fr.jpg` — `citizencoach/scratch/appstore-screenshots/captioned/{en,fr}/iphone/02-quiz.png`, resized to 680px wide, JPEG quality 84.
- `assets/citizencoach-readiness.jpg`, `assets/citizencoach-readiness-fr.jpg` — `citizencoach/scratch/appstore-screenshots/captioned/{en,fr}/iphone/01-home.png`, resized to 680px wide, JPEG quality 84. All six were checked visually for personal information; none was present (sample study text and sample readiness figures only).

All nine screenshots were replaced on 2026-10-22 with the redesigned captioned exports from the same folders, same sizes and quality. The file names stay the same, so `citizencoach-study*.jpg` now holds the Read or Listen image.

Refreshed again later on 2026-10-22 from the same exports after the screenshot scripts stopped cutting off the phone (CardTrainer 6b53356, CitizenCoach bad71d2): every phone is now whole on the page. Same sizes and quality; all nine were checked visually again, with no personal information.

Refreshed on 2026-10-28 from the re-captioned exports. CitizenCoach now reads from `citizencoach/scratch/appstore-screenshots/captioned/{en,fr}/iphone/{01-home,03-quiz,04-listen}.png` (the quiz page was renumbered from 02). CardTrainer uses the same three files as before. Same 680px width; quality 84, except `citizencoach-study*.jpg` at 68, `citizencoach-readiness-fr.jpg` at 76 and `cardtrainer-video-poker.jpg` at 76 to stay under 200 KB. All nine were checked visually; no personal information.

Refreshed on 2026-11-08 from the CardTrainer exports regenerated that day: `cardtrainer-practice.jpg`, `cardtrainer-counting.jpg` and `cardtrainer-video-poker.jpg` from the same three files, 680px wide, quality 84 (video poker now fits under 200 KB at 84), and `og-cardtrainer.jpg` remade from the new practice image. Captions are unchanged. Checked visually; sample hands only, no personal information.

- `assets/euchre-icon.png` — `euchre/Euchre/Assets.xcassets/AppIcon.appiconset/AppIcon.png`, resized to 128px square.
- `assets/euchre-table.jpg`, `assets/euchre-hint.jpg`, `assets/euchre-scenario.jpg`, `assets/euchre-review.jpg` — `euchre/scratch/appstore-screenshots/captioned/iphone-6.9/{01-table,02-hint,03-scenario,05-review}.png`, resized to 680px wide, JPEG quality 84, each under 200 KB. Checked visually on 2026-11-08; sample deals only, no personal information. The home-page card uses table, hint and scenario; the app page uses table, hint and review.

- `assets/uscitizencoach-icon.png` — `uscitizencoach/USCitizenCoach/Assets.xcassets/AppIcon.appiconset/AppIcon.png`, resized to 128px square.
- `assets/uscitizencoach-home.jpg`, `assets/uscitizencoach-interview.jpg`, `assets/uscitizencoach-reading-writing.jpg` — `uscitizencoach/scratch/appstore-screenshots/captioned/en/iphone/{01-home,02-interview,03-writing}.png`, resized to 680px wide, JPEG quality 84 (home at 80, under 200 KB). Checked visually; sample progress and sample answers only, no personal information.
- `assets/uscitizencoach-home-es.jpg`, `assets/uscitizencoach-interview-es.jpg`, `assets/uscitizencoach-reading-writing-es.jpg` — `uscitizencoach/scratch/appstore-screenshots/captioned/es/iphone/{01-home,02-interview,03-writing}.png`, resized to 680px wide, JPEG quality 80 (home 181 KB, others under 150 KB). Checked visually; sample progress and sample answers only, no personal information.

Share images for Open Graph and Twitter cards, made on 2026-10-28 with a throwaway script (not committed), 1200x630 JPEG quality 85, all under 300 KB: dark `#10110f` panel with the app icon (the 128px PNG scaled to 160px) and the store name, and the top 630 rows of one existing captioned screenshot on the right. Not a store export, so nothing new to check for personal information.

- `assets/og-citizencoach.jpg`, `assets/og-citizencoach-fr.jpg` — `citizencoach-icon.png` + `citizencoach-readiness.jpg` / `citizencoach-readiness-fr.jpg` (French page gets the French caption and store name).
- `assets/og-uscitizencoach.jpg`, `assets/og-uscitizencoach-es.jpg` — `uscitizencoach-icon.png` + `uscitizencoach-home.jpg` / `uscitizencoach-home-es.jpg`.
- `assets/og-cardtrainer.jpg` — `cardtrainer-icon.png` + `cardtrainer-practice.jpg`.
- `assets/og-euchre.jpg` — `euchre-icon.png` + `euchre-table.jpg`, made on 2026-11-08 the same way, with the store name shortened to "Euchre".
- `assets/og-pangufu.jpg` — brand only, so it never needs remaking when an app is added: the `favicon.svg` P monogram on a `#171915` tile, the PANGUFU name and the home page headline "Small apps. Thoughtfully made." Remade on 2026-11-08 with a throwaway script (not committed), replacing the earlier three-icon version. On 2026-11-12 the subtitle "iPhone & iPad apps for learning and practice" was painted out with the background colour, because the site now also has a browser extension; 1200x630, quality 85, 26 KB.
