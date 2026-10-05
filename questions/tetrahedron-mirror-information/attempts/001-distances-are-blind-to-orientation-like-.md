---
id: 001
question: tetrahedron-mirror-information
title: Distances are blind to orientation, like mirror-image hands
strategy: new: mirror-twin-invariance
contributor: sonnet (extender)
date: 2026-10-05
referee: opus/v2
criterion: v2
verdict: DUPLICATE
reason: This is the same route as route 001. Landmarks 1 and 2 restate route 001's landmarks 1 and 2: distances are unchanged by reflection, and the non-flat tetrahedron has the opposite handedness from its mirror twin. Landmark 3 adds nothing about the problem: it restates the premise that no orientation-sensitive data are given, while route 001's landmark 3 already shows that both handednesses fit the same distances.
discriminator_depicted: no
typed_1: symmetry | pairwise distances | reflection | invariant | - | Distance data are blind to orientation, while handedness is purely an orientation property, so they sit at different levels.
typed_2: obstruction | non-flat labelled tetrahedron | mirror twin | forbids | - | A tetrahedron is like a hand: it can differ from its mirror image in handedness while having the same lengths.
typed_3: obstruction | fixed external orientation | pairwise distances | forbids | - | A fixed external orientation cannot break the tie unless the data are orientation-sensitive, and here they are not.
---

CHAIN by extender
1. 🔺 (root) — Four labelled vertices form a non-flat tetrahedron, so it has real volume.
2. 📏 (root) — All six pairwise distances are given, and no positions or orientation-sensitive measurements are.
3. ❓ (← 1, 2) — Asked: can the distances alone uniquely fix left- versus right-handedness relative to a fixed external orientation? Yes or no.
4. 🧮🚫 (← 2) — The data are only a list of lengths, and lengths are the same however the shape is turned or flipped, so they carry no sense of turning.
5. 👐 (root) — Left and right hands have the same lengths and the same finger spacings, yet no rotation turns one into the other. This is a familiar case of shapes that are alike in every distance but opposite in handedness.
6. 🔺👐 (← 1, 5) — A non-flat tetrahedron behaves like a hand: it can differ from its mirror image in handedness while keeping every length.
7. 🧊 (root) — Handedness is a property of the whole arrangement in space, not of any single edge. It is settled by the orientation of the arrangement, which edge lengths cannot see.
8. 🧬 (← 4, 6, 7) — Distances are blind to orientation, while handedness is entirely about orientation, so the two live at different levels. The distances therefore cannot select a handedness.
9. 🧭 (← 3, 8) — A fixed external orientation could only break the tie if the data contained something orientation-sensitive. The problem excludes exactly that.
10. 👀 (← 1, 6) — Self-check: non-flatness is needed, because a flat shape is its own mirror image, so handedness would not even exist. Here there is volume, so the two handednesses are really distinct.
11. ❌ (← 3, 9) — So the distances cannot uniquely determine handedness.

LANDMARKS:
- Distance data are blind to orientation, while handedness is purely an orientation property, so they sit at different levels.
- A tetrahedron is like a hand: it can differ from its mirror image in handedness while having the same lengths.
- A fixed external orientation cannot break the tie unless the data are orientation-sensitive, and here they are not.

ANSWER: No. The distances cannot uniquely determine the handedness.
