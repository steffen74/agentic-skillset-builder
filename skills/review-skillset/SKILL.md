---
name: review-skillset
description: "Review a skillset before release on two axes: Conventions (structure, checks, language, licenses) and Practice (does it carry the domain faithfully and serve its users, based on a dry run). Ends with release, fix or hold."
disable-model-invocation: true
---

# Review a skillset

Two-axis review before users get the skillset. Run each axis as a separate sub-agent with a fresh context when your environment supports it; otherwise one after the other. Then aggregate. Inputs: the skillset repo, `design/` and the latest dry run in `design/SIGNALS.md`.

## Axis 1: Conventions

Load `skillset-conventions` and its `CHECKS.md`. Run `python3 scripts/check_skillset.py`, then every manual check in `CHECKS.md`:

- canvas grammar, owners, boundary block, `print:` lines; printed canvas current;
- every block settled or drafted by a skill, every file read has a writer, every user-owned decision is a stop point;
- each skill matches its role skeleton, each step has a completion criterion, descriptions follow the invocation rule;
- language rule; README, process and principles filled (no `{{placeholder}}` left: search for `{{`);
- `NOTICE.md` and `LICENSE-docs.md` match `design/SOURCES.md`.

## Axis 2: Practice

If no dry run exists, or skills changed after it, run `/dry-run` first. Then check:

- every blocker and overreach finding is fixed, or accepted by the maintainer with a reason;
- fixes did not move the problem: re-run only the steps that changed;
- the skills carry the sources faithfully: sample the domain rules in each skill and trace them to `design/SOURCES.md`; a rule without source or decision is a finding;
- the skillset reaches the outcomes in block 3 of the Skillset Canvas for the weakest persona.

## Report

One list, each finding marked **blocking** (a user would get stuck, be misled, or the agent would take their decision) or **note**, with evidence and a suggested fix. End with a recommendation: **release**, **fix then release** (list the fixes) or **hold**. When the repository is private and the dry run passed, recommend whether to make it public.

## Decisions

The verdict is the maintainer's, and so is every finding with more than one reasonable fix. Ask them as multiple-choice questions with their own context (what and where, why it matters, constraints, options with consequences, recommendation first); ask the verdict last. Apply only the fixes the maintainer picks, rerun the failed checks, record the verdict and each decision in `design/DECISIONS.md`, and set the statuses in `design/SKILL-MAP.md`.

Done when the verdict is logged. On **release**, suggest the maintainer skill `release-skillset`.
