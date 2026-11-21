# Role: diagnose

**Job.** Find out why a result is too good, too bad, or does not add up (adapted from Matt Pocock's `diagnosing-bugs`), before anyone acts on it.

**Steps.** Reproduce the surprise; list hypotheses ranked by likelihood and cost to test, with the boundary reference first (most surprises are boundary violations); test the cheapest discriminating hypothesis; repeat until one explains the evidence. Never "fix" by changing the check.

**Stop point.** The user decides what follows from the cause (redo, accept with a caveat, change the plan).

**Done when** the cause is named with evidence, written to the signal log, and a check or rule is proposed that would have caught it.
