# Signals

Everything that shows how the work is going: dry runs and checks before something counts, and what happened after. Newest first. The retro skill turns signals into fixes, checks and rules.

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
