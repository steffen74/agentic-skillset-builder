---
name: dry-run
description: "Run the new skillset on its example case as a user persona, in a scratch project, and report every place where a skill stalls, guesses or skips a stop point. Optionally type a skill or role group to limit the run."
disable-model-invocation: true
---

# Dry run

Find out whether the skillset works for its users before a real user finds out. The author of a skill knows every missing step and cannot see it; a dry run by someone who knows only what a user knows can. Read `design/SKILL-MAP.md`, `design/PERSONAS.md`, the example case in `examples/<case>/` and `design/SIGNALS.md`.

## 1. Fix the scope

- **Skills**: the ones typed with the command, otherwise every skill in process order, starting with the setup skill.
- **Persona**: the weakest user in `design/PERSONAS.md`, and any persona whose setting differs (alone vs. in a course). The persona answers stop-point questions from the example case and their knowledge state, and says "I don't know" where the persona would.
- **Case**: the example case. Missing details are invented once, written to `examples/<case>/README.md`, and reused, so later runs are comparable.

## 2. Set up the run

- A **scratch project**: a fresh folder outside the skillset repo (scratch or temp directory), with `git init`.
- Two roles, in separate sub-agents where your environment supports it:
  - the **runner** knows only the installed skills (copy `skills/` into the scratch project's skill folder, or read each `SKILL.md` from there) and follows them literally;
  - the **persona** knows only the persona's knowledge state and the case, and answers the runner's questions.
  Without sub-agents, play both in turn and keep their knowledge in separate lists. Never let the runner read `design/`: it holds the knowledge the skills are supposed to carry.

## 3. Run and observe

Run each skill as the persona would invoke it. Record for every step:

- **stall**: the skill refers to a file, tool, section or skill that does not exist at that point, or the runner cannot tell whether the step is done;
- **guess**: the runner had to invent a rule, a file location or a decision the skill does not give;
- **overreach**: the runner decided something the canvas gives to the user (the judgement boundary), or skipped a stop point;
- **friction**: the persona could not answer a question as asked (jargon, missing context, too many questions at once);
- **drift**: the output contradicts a source in `design/SOURCES.md` or a decision.

Execute what can be executed: scripts run, files are written, the canvas renders (`show-canvas`), checks run.

## 4. Report

A table, ordered by process step:

| # | Skill · step | Finding | Kind | Severity (blocker · friction · note) | Evidence | Suggested fix (skill, file) |
|---|---|---|---|---|---|---|

Then: steps run without finding; what was executed vs. only read; the artefacts the run produced (keep them in `examples/<case>/run-YYYY-MM-DD/` when they are useful as an example, otherwise discard the scratch project).

Append a dated entry to `design/SIGNALS.md` (source: *dry run*, persona, skills, counts per kind and severity) and set the dry-run status in `design/SKILL-MAP.md`.

Done when every step of every skill in scope has a row or is listed as run without finding. Suggest `/review-skillset`, or `/skillset-retro` when a finding points to a gap in the builder itself.
