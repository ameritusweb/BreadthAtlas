---
id: 001
question: tetrahedron-mirror-information
title: Mirror twin keeps distances but reverses handedness
strategy: new: invariance-witness-reflection
contributor: sonnet (blind player 1)
date: 2026-10-05
depth: 1
referee: opus/v2
criterion: v2
verdict: VALID
reason: The chain is sound. It shows that reflection keeps every distance (6), that a non-flat labelled tetrahedron can't be rotated into its mirror image (7–8), and so two opposite-handed shapes share the same distance data (9). It reaches the correct "No" with no calculation or simulation. The frontier was empty, so all three landmarks are new: reflection keeps the distances, the mirror twin can't be reached by rotation, and both handednesses fit the same data.
discriminator_depicted: yes
typed_1: symmetry | pairwise distances | reflection | invariant | - | Reflection in a mirror preserves all pairwise distances, so the mirror twin has identical distance data.
typed_2: obstruction | non-flat labelled tetrahedron | mirror twin | forbids | - | A non-flat labelled tetrahedron is not rotation-equivalent to its mirror image, so the twin has opposite handedness.
typed_3: construction | both handednesses | pairwise distances | exists | - | Both handednesses are consistent with the same distances, so a unique verdict would be contradictory.
---

CHAIN by blind player 1
1. 🔺 (root) — Four labelled vertices form a non-flat tetrahedron, so it has real volume.
2. 📏 (root) — All six pairwise distances between the labelled vertices are given, and nothing orientation-sensitive is.
3. ❓🧭 (← 1, 2) — Compared with the famous shape-from-distances question, this asks whether the distances alone can pick left-handed versus right-handed relative to a fixed outside orientation.
4. 🪞 (root) — Reflecting space in a mirror plane keeps every distance between points unchanged.
5. 🪞🔺 (← 1, 4) — Reflect the tetrahedron in a mirror, keeping the same vertex labels, to get a mirror twin.
6. 📏🟰 (← 2, 4, 5) — The mirror twin has exactly the same six distances as the original.
7. 🔄 (root) — A non-flat labelled tetrahedron cannot be turned into its mirror image by any rotation or move, because the labelled corners go around in opposite senses.
8. 🧩 (← 5, 7) — The mirror twin therefore has the opposite handedness from the original.
9. 🤝 (← 6, 8) — Two tetrahedra exist with identical distance data and opposite handedness.
10. 🔒💥 (← 3, 9) — Suppose the distances fixed the handedness. Then the original and the twin would have to receive the same verdict, yet they differ, which is a contradiction.
11. 👀 (← 1, 7) — Self-check: non-flatness matters, because a flat shape equals its own mirror image by a rotation. Here the shape has volume, so the twin really is different.
12. ❌ (← 10) — The distances cannot uniquely determine handedness.

LANDMARKS:
- Reflection in a mirror preserves all pairwise distances, so the mirror twin has identical distance data.
- A non-flat labelled tetrahedron is not rotation-equivalent to its mirror image, so the twin has opposite handedness.
- Both handednesses are consistent with the same distances, so a unique verdict would be contradictory.

ANSWER: No. The distances are the same for a tetrahedron and its mirror image, so they cannot fix handedness.
