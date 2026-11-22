# Role catalogue

Every skill of a skillset plays one role. The skeleton file of a role gives its job, what it reads, its steps, its stop point and its completion criterion; the domain fills in the content. Sibling examples are skills from [Agentic Data Science](https://github.com/steffen74/agentic-data-science) (DS) and [Agentic Course Creation](https://github.com/steffen74/agentic-course-creation) (CC).

| Role | Skeleton | Invoked by | Required | Sibling examples | Adapted from (Matt Pocock) |
|---|---|---|---|---|---|
| setup | [setup.md](setup.md) | user | yes | `setup-ds-project`, `setup-course` | `setup-matt-pocock-skills` |
| router | [router.md](router.md) | user | yes | `ask-ds`, `ask-course` | `ask-matt` |
| show-canvas | core (`skillset-core`) | user | yes | `show-canvas` | – |
| grill | [grill.md](grill.md) | user | yes | `grill-question`, `grill-course` | `grilling`, `grill-with-docs` |
| inventory | [inventory.md](inventory.md) | user | when the agent can collect facts | `explore-data`, `map-resources` | – |
| plan | [plan.md](plan.md) | user | yes | `to-analysis-plan`, `to-course-plan` | `to-spec` |
| produce | [produce.md](produce.md) | user | one or more | `implement-experiment`, `draft-unit`, `to-memo`, `to-slides` | `tdd`, `implement` |
| walk-through | [walk-through.md](walk-through.md) | user | when a persona can try the result | `walk-through` | – |
| review | [review.md](review.md) | user | yes | `review-results`, `review-unit` | `code-review` |
| diagnose | [diagnose.md](diagnose.md) | user | optional | `diagnose-surprise` | `diagnosing-bugs` |
| retro | [retro.md](retro.md) | user | yes | `ds-retro`, `course-retro` | `retro` |
| checks reference | [reference-checks.md](reference-checks.md) | model | yes | `data-checks`, `course-checks` | – |
| boundary reference | [reference-boundary.md](reference-boundary.md) | model | yes | `leakage`, `assumed-knowledge` | – |

Common to all user-invoked roles: read the canvas and the project files named in the skillset's section of `AGENTS.md` first; never re-ask what is written down; end every step on a completion criterion; log every decision the user owns. Four patterns every skillset needs (found in the first dry run of the Agentic Business Model Canvas, where a weak persona nodded along):

- **Own words first.** For content the user owns (a problem statement, a goal, a vision, a recommendation), ask for the user's words before offering a suggestion; when the user adopts the agent's wording unchanged, log that in the decision log. A ➡️ recommendation that is accepted with "ok" otherwise becomes the content.
- **Input in chat.** Users paste notes, results or data into the chat instead of the file the skill expects. A skill that reads a project file says what to do then: copy the input verbatim into the file, in the expected format, and confirm the mapping.
- **Approval in small steps.** Show at most about five items per approval; the consequential ones first. A blanket "ok" never approves a consequential change (one that turns an assumption into a fact, releases something, or changes a status); ask for those one by one.
- **Commit at the end.** Every skill that writes project files ends by offering a commit (when the project uses git), so later skills can rely on the history (for example, that a threshold was set before a result).
