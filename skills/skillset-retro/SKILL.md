---
name: skillset-retro
description: After a dry run or real use of a skillset - turn what happened into fixes, checks, canvas changes, and improvements to the skillset, the builder or the core.
disable-model-invocation: true
---

# Skillset retro

Make the skillset, and the builder that made it, better from what happened. Read `design/SIGNALS.md`, `design/SKILLSET-CANVAS.md`, `design/SKILL-MAP.md`, the skills concerned and, for feedback from real use, the issues in the skillset repository.

## 1. Collect signals

Ask the maintainer what happened, in one round: where users got stuck, where the agent decided something it should have asked, which outputs were wrong or unhelpful, which questions came up more than once. Add what you can look up yourself (issues, pasted transcripts, retros of the skillset's own retro skill). Write each as an entry in `design/SIGNALS.md`; no personal names.

## 2. Explain each signal

Find the cause before proposing anything, then ask **why no check or dry run caught it**. Locate the cause at the right level:

- **skillset**: a skill, the canvas, a template, a source read wrongly;
- **builder**: a builder skill, a role skeleton or `skillset-conventions` that let the problem through, so every future skillset would repeat it;
- **core**: a core file (renderer, check script, release skill, templates).

## 3. Propose

A numbered list, each with evidence and a recommendation:

- **Fix now**: the change to the skillset, as a diff.
- **Check**: the check that would have caught it, with its type; automated checks that apply to all skillsets go into `check_skillset.py` in the builder's core.
- **Canvas and sources**: blocks, owners or adopted elements that turned out wrong.
- **Builder rule**: a change to a builder skill, role skeleton or `skillset-conventions`, as a diff, to file as an issue or pull request in the Agentic Skillset Builder repository.
- **Core change**: a change to a core file, made in the builder and synced with `/sync-core`.

Prefer a check over a rule.

## 4. Apply

Apply only what the maintainer picks. Update each signal's status in `design/SIGNALS.md`, block 11 of the Skillset Canvas, and `CHANGELOG.md` under `## Unreleased`.

Done when every picked item is written to its file and every signal has a status.
