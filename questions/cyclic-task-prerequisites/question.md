---
id: cyclic-task-prerequisites
title: Can a cycle of strict prerequisites ever start?
status: answered
added: 2026-10-05
family: ordering, dependencies
attractor: choose the right order and all tasks can be completed
---

# Question

None of tasks A, B, and C has started. A may start only after B has finished; B may start only after C has finished; C may start only after A has finished. Each task requires a positive duration after starting to finish. No prerequisite can be waived. Can any schedule finish all three tasks?

# Reference answer (referee only)

No. Any successful schedule would contain a first task to start, but each possible first task requires another task to have already finished, which would require an earlier start. Alternatively, follow the strict precedence requirements around the cycle to demand that a task precede itself. Tolerance: exact no; simultaneous starts do not satisfy prior completion.

# Why it is in the atlas

Adds earliest-event contradiction and cyclic ordering obstruction, including a check against simultaneous-start escape.

# Breadth

No played or accepted routes yet. The unjudged draft in curator.md is not part of the frontier.
