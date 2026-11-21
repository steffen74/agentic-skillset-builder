# Language rule

A skillset has one **language**, recorded as `- Language: <code>` in the `## Agentic skillset builder` section of the skillset repo's `AGENTS.md` and in the skillset's section of each project's `AGENTS.md`.

| Element | Language |
|---|---|
| Skill names, folder names, file names, frontmatter keys | English (`grill-model`, `CANVAS.md`, `DECISIONS.md`) |
| Canvas grammar keywords: `> Owners:`, `**Canvas:**` in decision entries, `print:` | English |
| Frontmatter `description`, skill bodies, templates, canvas block names and hints, README, docs | The skillset's language |
| Questions and recommendations to the user | The skillset's language |
| Maintainer files: `AGENTS.md` of the skillset repo, `CONTRIBUTING.md`, `CHANGELOG.md`, `.claude/skills/release-skillset/` | English, so maintainers of all skillsets share them |

English identifiers keep the skills tool-friendly and comparable across skillsets; the people using the skillset read and answer in their own language.

Writing rules for German skillsets:

- Address the user consistently, with *du* unless the skillset's users block says otherwise.
- Use the domain's established German terms (from the handbook in `design/SOURCES.md`) and keep an English term only where the domain itself uses it (*Business Model Canvas*, *Pitch*). Record each choice of term in the glossary of `design/SKILL-MAP.md`.
- `render_canvas.py --lang de` prints German labels; block owner labels come from the canvas's own `> Owners:` line.
