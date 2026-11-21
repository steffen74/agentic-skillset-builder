---
name: draft-skill
description: "Draft one skill of a skillset from its row in the skill map and its role skeleton, in the skillset's language. Type the skill name after the command, or a role group to draft the group."
disable-model-invocation: true
---

# Draft a skill

Write one `SKILL.md` that an agent will run the same way every time. Read `design/SKILL-MAP.md`, `design/SKILLSET-CANVAS.md`, the domain canvas template, `canvas/README.md`, `design/SOURCES.md`, `design/PERSONAS.md` and `design/DECISIONS.md`. Load `skillset-conventions` (its `LANGUAGE.md` when the language is not English) and Matt Pocock's `writing-for-agents` if it is installed. If the skill map is missing, stop and suggest `/to-skill-map`.

## 1. Gather

- The skill's row in the skill map: role, invocation, files read and written, canvas blocks, *adapted from*.
- The role skeleton from `skillset-conventions/roles/`.
- The sibling-skillset skill of the same role, if one exists (see the role catalogue): read it as a worked example of the skeleton.
- Every source element in `design/SOURCES.md` that the skill's blocks and steps adopt. Each domain rule in the skill must trace to one of them or to a decision; list rules that trace to neither as questions.

Done when every step of the skeleton has domain content or an open question.

## 2. Draft

Write `skills/<name>/SKILL.md` (and templates, scripts or disclosed reference files the skill needs):

- **Frontmatter**: `name` equal to the folder; user-invoked skills get `disable-model-invocation: true` and a one-line description for humans; reference skills get a model-facing description that starts with what the skill is and lists its triggers. Description in the skillset's language.
- **Body**: the skeleton's steps in the domain's words, each ending on a completion criterion; stop points as multiple-choice questions with their own context; files exactly as named in the skill map; leading words instead of restated triads; positive instructions; reference that only some runs need goes into a sibling file behind a pointer.
- Add the skill to `skills` in `.claude-plugin/plugin.json` and set its status in the skill map to *drafted*. Add its row to `NOTICE.md` when it is adapted from Matt Pocock's skills.

Before presenting, check the draft against the skeleton and `skillset-conventions/CHECKS.md`, and run `python3 scripts/check_skillset.py`.

## 3. Stop point

Present the drafts of the current role group together (default groups: core and setup; grill and plan; produce and check; retro and reference). For each skill: what it does in two lines, the decisions it puts to the user, the rules that trace to no source (as questions), and anything you changed from the skeleton. The maintainer approves, or asks for changes, per skill. Log choices that affect several skills in `design/DECISIONS.md`.

Done when every skill of the group is approved or has its changes listed. After the last group of the skill map, suggest `/dry-run`; otherwise the next group.
