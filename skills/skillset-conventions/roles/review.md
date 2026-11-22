# Role: review

**Job.** Decide whether an artefact counts, on two axes (adapted from Matt Pocock's `code-review`): **validity** (does it pass the checks, is it correct, consistent, within the boundary) and **purpose** (does it serve the decision, goal or user it was made for). Run each axis in its own sub-agent where possible, then aggregate.

**Steps.**
1. Inputs: the artefact, the canvas, the plan, the checks file, the latest walk-through or dry run.
2. Each axis: run every check that applies; findings marked **blocking** or **note**, with evidence and a suggested fix.
3. Report one list, then a recommendation: **accept** (release, publish), **fix then accept** (list the fixes), or **hold**.

**Stop point.** The verdict is the user's, and so is every finding with more than one reasonable fix. Ask as multiple-choice questions that carry their own context (what and where, why it matters, constraints, options with consequences, recommendation first); ask the verdict last. Apply only the chosen fixes, rerun failed checks, log the verdict.

Explain the severity words in one plain sentence ("blocking means: clear this up before you build on it"). Name the follow-up skill for each possible verdict.

**Done when** the verdict is logged and the artefact's status is set. Offer a commit.
