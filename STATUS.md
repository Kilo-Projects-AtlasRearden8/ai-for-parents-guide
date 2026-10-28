# STATUS — AI for Family Life Beginner Manual

## What was built

A beginner manual and static HTML site on using free AI for family life: school forms, meal ideas, activities, and bedtime stories.

- `README.md` — overview, credits, license pointer, privacy promise
- `LICENSE` — MIT License, copyright line exactly `Copyright (c) 2026 Asdale Dynamics, LLC`
- `docs/` — plain-English, step-by-step Markdown manual:
  - `index.md` — overview, free model options, how to use the manual
  - `getting-started.md` — picking a free model, first chat, prompt tips
  - `privacy-safety.md` — never-paste rule, placeholder convention, medical disclaimer
  - `school-forms.md` — anonymized form handling, draft emails, deadline tracker
  - `meal-ideas.md` — pantry-based planning, budget/low-energy/picky-eater prompts
  - `activities.md` — rainy-day, weekend, low-energy/ADHD-friendly activities
  - `bedtime-stories.md` — safe story prompts, read-aloud tips, story log
  - `printable-planners.md` — meal planner, school forms tracker, activity planner, bedtime story log
- `site/` — static HTML version of the manual with shared `css/style.css`; printer-friendly `@media print` styles; every page credits Asdale Dynamics, LLC
- `scripts/verify.py` + `scripts/verify.sh` — automated verification (files, LICENSE line, README credit, link validity, no secrets, no `.github/workflows`)

## How to run it

This is a static site — no build step, no server, no install.

- Read the manual: open any file in `docs/` in a text editor or Markdown reader.
- Browse the site: open `site/index.html` in any web browser.
- Print planners: open `site/printable-planners.html` and press Ctrl+P (Cmd+P on Mac).
- Run verification: `bash scripts/verify.sh` (requires Python 3).

No network is required except to download an optional AI model (e.g., Ollama) or visit linked external resources.

## Verification results

`bash scripts/verify.sh` — PASSED: all 21 required files present, LICENSE contains the exact copyright line, README credits Asdale Dynamics, LLC, all HTML/Markdown links resolve, no `.github/workflows`, no secrets or personal-data patterns detected, privacy placeholder convention documented.

## Known gaps

- Site pages are Markdown conversions maintained by hand; `docs/` and `site/` can drift if one is edited without the other.
- No automated spell-check or HTML linter beyond `scripts/verify.py`.
- External links (Ollama, author hub) were not network-checked.
- No search function on the static site.

## Credit

Written by Dylan Asdale, founder of Asdale Dynamics, LLC (Indiana, formed October 2026). MIT License — Copyright (c) 2026 Asdale Dynamics, LLC.
