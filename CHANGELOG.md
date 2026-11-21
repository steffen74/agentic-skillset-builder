# Changelog

## Unreleased

- `/setup-skillset` prints the exact `gh repo create` command when the session cannot create the repository itself.
- First draft: Skillset Canvas (guide, printed SVG and PDF, template), process, principles, eleven user-invoked skills, two reference skills (`skillset-conventions` with role catalogue and skeletons, `skillset-core`) and the maintainer skill `release-skillset`.
- Core 0.1.1: `render_canvas.py` (from Agentic Data Science and Agentic Course Creation, unchanged HTML output) gains `--print`/`--pdf` for the printed A4 canvas, `print:` prompt lines, labels in English and German (`--lang`) and owner labels from the canvas's own legend; new `check_skillset.py`; `core_sync.py` with a lock file for verbatim and adapted core files.
