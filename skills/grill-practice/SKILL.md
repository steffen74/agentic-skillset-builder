---
name: grill-practice
description: Interview the maintainer until the practice, users, outcomes, evidence and judgement boundary of a new skillset are sharp. Writes the Skillset Canvas, personas and decision log as answers come in.
disable-model-invocation: true
---

# Grill the practice

Interview the maintainer relentlessly until blocks 1–4 and 6 of `design/SKILLSET-CANVAS.md` and `design/PERSONAS.md` are sharp. Read the canvas, `design/PERSONAS.md`, `design/SOURCES.md`, `design/DECISIONS.md` and the example case first; never re-ask what is already decided or written down. Hold the conversation in the skillset's language.

## How to interview

Map the open points as a **decision tree**: the practice (block 1) gates the users (2) and the outcomes (3); outcomes gate the evidence (4); users and outcomes gate the judgement boundary (6).

Work in **rounds**. The **frontier** is every point whose prerequisites are settled. Ask the whole frontier in one round, number each question, and give your recommended answer:

```
❓ **Q1** - **<title>**: <question, with options where useful>

➡️ <your recommended answer, and why>
```

Wait for the answers, write them down (below), recompute the frontier, and ask the next round. A question whose answer depends on another open question of this round belongs to a later round.

**Facts are your job; decisions are the maintainer's.** What the handbook says, which canvases it uses, which steps its method prescribes, how the sibling skillsets solved the same question: look it up (dispatch a sub-agent for long reads, and ask the rest of the frontier meanwhile). Never ask for something you can find.

## What to probe

- **Practice**: which work, in which setting, and what goes wrong today when people do it with an agent and no skills. Ask for one concrete failure story; it becomes the README's "the skill that would have caught it".
- **Users**: role, domain knowledge, agent experience, language, time. How will they learn the skillset – README and router enough, or a worked example and a course in the repository? Who installs the agent for them? Who is the weakest user the skillset still serves? Write that persona first. Distinguish users from beneficiaries (a course skillset is used by instructors, a method skillset may be used by participants with an instructor beside them).
- **Outcomes**: the artefacts and decisions the skillset should lead to, observable. What it deliberately does not do.
- **Evidence**: per outcome, the criterion and where its expected value comes from. Outcomes without evidence are dropped or given evidence; ask which.
- **Judgement boundary**: go through the domain's typical decisions and settle for each: agent does, agent drafts and user approves, or user decides. Invent concrete scenarios from the example case that force a precise answer ("the agent finds three competitors on the web: does it rate them, or list them for the team to rate?"). Find the place where an agent would most likely cross the line unnoticed; that becomes the skillset's signature check.

Sharpen fuzzy terms as they come up and write the precise meaning into the glossary of `design/SKILL-MAP.md`.

## Write as you go

- Each settled answer goes into its canvas block immediately, in a few lines.
- Each persona goes into `design/PERSONAS.md`, with the knowledge state `/dry-run` will play.
- Each choice between alternatives goes into `design/DECISIONS.md` with reason and alternatives.
- Anything left open goes to **Open questions** on the canvas, with who resolves it.

Done when the frontier is empty: blocks 1–4 and 6 each hold a settled answer or an explicit open question, and at least the weakest persona exists. Show the updated blocks and ask the maintainer to confirm before suggesting `/map-sources`.
