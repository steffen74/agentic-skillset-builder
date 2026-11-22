# Signals

Everything that shows how the work is going: dry runs and checks before something counts, and what happened after. Newest first. The retro skill turns signals into fixes, checks and rules.

## 2026-11-22 · core · design-canvas (Agentic Business Model Canvas)

- **What happened:** The printed canvas of the first skillset built with the builder had a subtitle running into the header field lines, and a long block title shrunk to 11 px.
- **Who:** maintainer, reviewing the printed canvas as `/design-canvas` asks
- **Severity:** friction
- **Status:** subtitle fixed in core 0.1.2; long block titles stay the skillset's job (shorten the name), as `/design-canvas` says

## 2026-11-21 · setup-skillset · session

- **What happened:** `gh repo create` was refused in a cloud session that may only reach repositories already attached to it. The maintainer had to ask for the exact command, and expects to need it every time.
- **Who:** maintainer, setting up the builder and the Agentic Business Model Canvas skillset
- **Severity:** friction
- **Status:** fixed in `setup-skillset` (prints the exact `gh repo create` command for an empty repository, plus the github.com/new alternative)

## 2026-11-21 · core · dry run (smoke test)

- **What happened:** In a scaffolded test skillset, `check_skillset.py` failed `skill-refs`: `design/`, `AGENTS.md` and the release skill refer to builder skills (`/dry-run`, `/sync-core`, `/setup-skillset`), which are not skills of the skillset itself.
- **Who:** smoke test of setup → core init → German canvas → print → checks
- **Severity:** blocker (every new skillset would fail its checks)
- **Status:** fixed in core 0.1.1 (`check_skillset.py` accepts builder skill names); the update path of `core_sync.py` (status → apply) was exercised on the test skillset.

## 2026-11-21 · core · check

- **What happened:** The first printed canvas rendered a long block title ("7 Process and stop points") over its owner badge.
- **Who:** maintainer, reviewing the printed Skillset Canvas
- **Severity:** friction
- **Status:** fixed in `render_canvas.py` (title shrinks to fit); the screenshot review stays a step of `/design-canvas`.
