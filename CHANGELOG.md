# Changelog

## Unreleased

## 0.1.0 (2026-11-23)

First release, after building the Agentic Business Model Canvas with the builder and a recap of Agentic Course Creation. Core 0.2.3.

- Core 0.2.3: `show-canvas` uses `python` or `py` on Windows, where `python3` may open the Microsoft Store.
- Core 0.2.2: `show-canvas` falls back to showing the canvas as text when Python is missing (found in a course walk-through: Python is not on a fresh Windows machine).
- Core 0.2.1: the Pages workflow runs only in public repositories.
- Core 0.2.0: a website for every skillset – `scripts/build_site.py` assembles README, course, canvas guide (printed and interactive blank canvas) and docs for MkDocs Material; `.github/workflows/pages.yml` builds and deploys it on GitHub Pages. Note: Material for MkDocs reaches end of life in May 2027 (successor: Zensical).
- Core 0.1.5: more built-in agent commands (OpenCode `/connect`, `/models`; Claude Code `/doctor`, `/reload-plugins` …) are not reported as missing skills.
- Core 0.1.4: `check_skillset.py` skips folders listed in the optional `AGENTS.md` line `- Other skillsets in:` (e.g. a course planned with Agentic Course Creation inside a skillset repo).
- Core 0.1.3: `check_skillset.py` ignores agent built-in commands (`/mcp`, `/help` …) and placeholders (`/command`) in skill references.
- `core_sync.py init` records files that already exist in the target as *adopt*, so `record` and `skip` work on them (found when adopting the core in Agentic Course Creation).
- Role skeletons carry four patterns from the first dry run of a built skillset: own words before suggestions, input pasted in chat, approval in small steps, a commit offer at the end of every writing skill. `setup` creates `CLAUDE.md` with `@AGENTS.md`.
- Skillsets can carry a self-study course in `course/` (built with Agentic Course Creation from dry-run material) and publish a site, GitHub Pages by default: new questions in `/setup-skillset` (F. Site) and `/grill-practice` (how users learn), new checks in `skillset-conventions/CHECKS.md` and `/review-skillset`; `/dry-run` keeps its artefacts as worked example.
- Core 0.1.2: `render_canvas.py --print` shrinks a long subtitle so it no longer runs into the header fields.
- `/setup-skillset` prints the exact `gh repo create` command when the session cannot create the repository itself.
- First draft: Skillset Canvas (guide, printed SVG and PDF, template), process, principles, eleven user-invoked skills, two reference skills (`skillset-conventions` with role catalogue and skeletons, `skillset-core`) and the maintainer skill `release-skillset`.
- Core 0.1.1: `render_canvas.py` (from Agentic Data Science and Agentic Course Creation, unchanged HTML output) gains `--print`/`--pdf` for the printed A4 canvas, `print:` prompt lines, labels in English and German (`--lang`) and owner labels from the canvas's own legend; new `check_skillset.py`; `core_sync.py` with a lock file for verbatim and adapted core files.
