# Worked example: the Agentic Business Model Canvas

The first skillset built with the builder, from an empty repository to release 0.9.0 in three working days (2026-11-21 to 2026-11-23). Repository: [opencampus-sh/agentic-business-model-canvas](https://github.com/opencampus-sh/agentic-business-model-canvas), website: [opencampus-sh.github.io/agentic-business-model-canvas](https://opencampus-sh.github.io/agentic-business-model-canvas/). The design files there (`design/`) are the full record; this page is the short version.

## The case

Teams in the opencampus.sh course “Become a Changemaker” develop an impact start-up from a social problem to a tested business model. The course handbook describes the canvases (Social Business Model Canvas, SEEd); the skillset lets a team work through them with a coding agent (Claude Code, OpenCode or Codex) without handing over its decisions. Language: German. Weakest user: a social-work student without agent or Git experience.

## Path through the builder

| Step | Skill | What came out |
|---|---|---|
| Set up | `/setup-skillset` | Repository scaffold, `AGENTS.md` section, core files; the `gh repo create` command printed because the session could not create repositories |
| Practice | `/grill-practice` | Questions in rounds: scope (problem analysis included), users, agents, rights holder (Campus Business Box e.V.), licences, how teams learn the skillset (a self-study course in the repository) |
| Sources | `/map-sources` | Course handbook, SEEd material, Business Model Canvas (CC BY-SA), Value Proposition Canvas (Strategyzer copyright: linked, not copied) |
| Canvas | `/design-canvas` | 11 blocks in three columns (Problem & Wirkung, Geschäftsmodell, Testen & Lernen); boundary in block 6: assumption vs. evidence |
| Skill map | `/to-skill-map` | 12 user-invoked skills in four groups, two reference skills (`assumptions`, `evidence-checks` with `check_project.py`) |
| Drafts | `/draft-skill` | One group at a time, each with its decisions (G1–G6) |
| Dry runs | `/dry-run` | Two runs with a runner agent and a persona, then a targeted re-run of the fixes (V1–V9 pass); two reference runs whose snapshots became the course's exercise material |
| Review | `/review-skillset` | Release after the course and a recap of Agentic Course Creation; public with the release |
| Release | `release-skillset` | 0.9.0 (1.0 after feedback from the course lead) |

## What the dry runs found

- The agent filled in canvas blocks in its own words before the team had spoken → **own words first** became a builder pattern.
- Notes pasted into the chat never reached the files → **input pasted in chat goes into files first**.
- A blanket “passt” approved a whole list of status changes at once → **approval in batches of at most five**; a blanket yes never sets *evidence*.
- Nothing suggested committing, so “threshold set before the result” could not be shown → **commit offer at the end of every writing skill**.
- Test thresholds that measured something weaker than the assumption, cards that tested several assumptions, results logged before their prerequisite → new automated checks in `check_project.py`.
- Walk-throughs of the course: Python missing on Windows (→ core 0.2.2/0.2.3), scripted learner replies drifting from the skills (→ exercises taken from a reference run).

The four patterns now live in the role skeletons (`skills/skillset-conventions/roles/`), so every skillset built later starts with them.

## What the builder learned

- Core 0.1.1–0.2.3: printed canvas from the template, `check_skillset.py`, lock file with *adopt*, built-in agent commands, `Other skillsets in:`, GitHub Pages site, Windows and no-Python fallbacks.
- `/setup-skillset` asks about the site; `/grill-practice` asks how users learn the skillset; `/dry-run` keeps its artefacts as worked example.
- A skillset can carry a self-study course in `course/`, planned with Agentic Course Creation; that run in turn improved Course Creation (course folder, self-study format, language).
