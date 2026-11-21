# Sources

## Inventory

| # | Source | Kind | Location | License | Accessed | Used for |
|---|---|---|---|---|---|---|
| S1 | Agentic Data Science | sibling skillset | github.com/steffen74/agentic-data-science | MIT (skills), CC BY 4.0 (canvas, docs) | 2026-11-21 | blueprint, roles, `render_canvas.py`, `release-plugin` |
| S2 | Agentic Course Creation | sibling skillset | github.com/steffen74/agentic-course-creation | MIT, CC BY 4.0 | 2026-11-21 | blueprint, roles, stop-point question format, walk-through |
| S3 | Matt Pocock's skills | skills | github.com/mattpocock/skills | MIT | 2026-11-21 | skill structure, `writing-for-agents`, `grilling`, `ask-matt`, `to-spec`, `code-review`, `retro`, `diagnosing-bugs` |

## What is adopted

| Element | From | How | Note |
|---|---|---|---|
| Canvas grammar, three columns, owners | S1, S2 | adopted | generalised: block names free |
| `render_canvas.py` | S1, S2 | adapted | `--print`, `--pdf`, `--lang`, legend labels; HTML output unchanged |
| `release-skillset` | S1 `release-plugin` | adapted | generic paths from `AGENTS.md`, printed canvas, check script |
| Role skeletons | S1, S2, S3 | adapted | attributed in `NOTICE.md` |
| Grill rounds and frontier | S3 `grilling` | adapted | in role `grill` and `grill-practice` |
| Two-axis review, multiple-choice decisions | S3 `code-review`, S2 `review-unit` | adapted | |
| Writing rules | S3 `writing-for-agents` | referenced and summarised | not copied |

## Conflicts between sources

None found.

## Left out

Domain-specific skills of S1 and S2 (leakage, quizzes, slides): they belong to their skillsets.
