# STATUS — AI for Family Life Beginner Manual

## What was built

A beginner manual and static HTML site on using free AI for family life: school forms, meal ideas, activities, and bedtime stories. Written in plain English, step by step, with printable planners and a strict never-paste-privacy rule.

- `README.md` — overview, who it's for, what's inside, quick start, how to run, privacy promise, credit to Asdale Dynamics, LLC, MIT license pointer
- `LICENSE` — MIT License, copyright line exactly `Copyright (c) 2026 Asdale Dynamics, LLC`
- `STATUS.md` — this file
- `docs/` — plain-English, step-by-step Markdown manual:
  - `index.md` — welcome, the one privacy rule, what's inside, how to use, free model options
  - `getting-started.md` — pick a free model, first chat, prompt tips, example prompts
  - `privacy-safety.md` — never-paste rule, placeholder convention, medical disclaimer, pre-send checklist
  - `school-forms.md` — anonymized form handling, draft emails, deadline tracker, step-by-step example
  - `meal-ideas.md` — pantry-based planning, budget/low-energy/picky-eater/leftover/snack prompts, weekly routine
  - `activities.md` — rainy-day, weekend, low-energy/ADHD-friendly activities, activity ideas by type
  - `bedtime-stories.md` — safe story prompts, read-aloud tips, story log
  - `printable-planners.md` — Weekly Meal Planner, School Forms Tracker, Weekly Activity Planner, Bedtime Story Log
- `site/` — static HTML version of the manual with shared `css/style.css`; printer-friendly `@media print` styles; every page credits Asdale Dynamics, LLC and restates the never-paste rule
- `scripts/verify.py` + `scripts/verify.sh` — automated verification (files, exact LICENSE copyright line, README/LLC credit, link validity, CSS linkage, no `.github/workflows`, no secrets or personal-data patterns, privacy reminders on every page, all four printable planners present)

## How to run it

This is a static site — no build step, no server, nothing to install, no network required (except to download an optional AI model such as Ollama, or visit linked external resources).

- Read the manual: open any file in `docs/` in a text editor or Markdown reader.
- Browse the site: open `site/index.html` in any web browser.
- Print planners: open `site/printable-planners.html` and press `Ctrl+P` (`Cmd+P` on Mac).
- Run verification: `bash scripts/verify.sh` (requires Python 3).

## Verification results

`bash scripts/verify.sh` — PASSED, clean (no errors, no warnings):
- All 22 required files present
- `LICENSE` contains the exact line `Copyright (c) 2026 Asdale Dynamics, LLC` on its own line
- `README.md` credits Asdale Dynamics, LLC and includes the exact copyright line
- Every `docs/` page credits Asdale Dynamics, LLC and states the never-paste rule
- Every `site/` page links to `index.html`, links to `css/style.css`, credits Asdale Dynamics, LLC, and restates the never-paste rule
- All HTML and Markdown links resolve to existing files
- No `.github/workflows` directory
- No secrets, API keys, or personal-data patterns detected in any file
- Privacy placeholders (`[Child's name]`, etc.) documented in `docs/privacy-safety.md`
- All four printable planners present in `docs/printable-planners.md`

## Known gaps

- `docs/` and `site/` are maintained by hand and can drift if one is edited without the other.
- No automated spell-check or HTML linter beyond `scripts/verify.py`.
- External links (Ollama, author hub) were not network-checked.
- No search function on the static site.
- The manual covers family-life topics only; related LLC focus areas (agents/MCP, local AI, free AI coding, GitHub, automation, KDP/book publishing, marketing, reselling, bookkeeping, healthcare-worker AI aids, FFXIV, chess) are out of scope for this manual.

## Credit

Written by Dylan Asdale, a registered nurse turned AI author and founder of **Asdale Dynamics, LLC** (Indiana, formed October 2026). MIT License — Copyright (c) 2026 Asdale Dynamics, LLC.
