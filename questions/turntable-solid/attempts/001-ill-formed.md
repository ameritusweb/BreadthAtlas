---
id: 001
question: turntable-solid
title: Read the ring order from one view's dots
strategy: new: single-view-angular-ordering
contributor: sonnet (blind player 1)
date: 2026-10-05
referee: opus/v1
criterion: v1
verdict: WRONG
reason: Step 7 does not follow from its parents. Horizontal position plus filled/hollow in one view cannot give the cyclic order of a star whose vertices alternate between tips and inner corners, because position depends on radius and angle together and a hollow dot can be an inner corner on the front hidden by a tip; the chain also files the star as a plain octagonal prism, and its order puts the antipodal pair NZ/KA three places apart instead of four. (I judged this without the image because permission to open puzzle.png was denied.)
note: re-judged 2026-10-05; previously ILL-FORMED: no ❓ step stating what is asked
typed_1: structure | top ring | bottom ring | bijects | horizontal position | The points split into a top ring and a bottom ring, and each top point lies directly above a partner with the same horizontal position.
typed_2: structure | octagonal prism | cyclic order | exists | - | The solid is an octagonal prism whose cyclic order is read from the filled and hollow dots.
typed_3: structure | faces | - | = | face count | The faces are two octagons and eight vertical quadrilaterals.
---

CHAIN by blind player 1
1. 🧊 (root) — Given: the same sixteen labelled points appear in every view, so the views show one rigid solid turned about a vertical axis.
2. ↕️ (← 1) — A turntable axis is vertical, so each point keeps its height v in every view. Only its horizontal position u changes.
3. 📏 (← 2) — In every view, eight points sit at height plus one and eight at height minus one. The solid therefore has a top layer and a bottom layer.
4. 🔗 (← 3) — Each top point shares its horizontal position with one bottom point in every view. Pairs: NZ–UF, EV–CY, QA–HE, QN–EL, XS–WA, HW–CZ, GD–AZ, KA–KL. These pairs are vertical edges.
5. 🔄 (← 4) — Because the pairs are vertical edges and the layers are parallel, the solid is a prism.
6. ⚫ (← 1) — In View A, the filled (front) top points are NZ, QN, GD and KA. The hollow (back) ones are EV, QA, XS and HW.
7. 🧭 (← 2, 6) — A point's horizontal position reflects its angle around the axis, and filled versus hollow says which side it is on. Reading View A this way, the top points go around the ring in the order KA, GD, QN, NZ, EV, QA, XS, HW.
8. 🔷 (← 5, 7) — The top face is the eight-sided polygon KA, GD, QN, NZ, EV, QA, XS, HW. The bottom face has the paired labels in the same order: KL, AZ, EL, UF, CY, HE, WA, CZ.
9. 🟦 (← 4, 8) — Each side face joins two neighbouring top points to their paired bottom points. That gives eight quadrilateral faces.
10. 👀 (← 8) — Self-check: Views B, C and D show the same eight pairings, so the prism structure holds.
11. 🏁 (← 8, 9) — Ten faces in all: two octagons and eight rectangles-like side faces.

LANDMARKS:
- The points split into a top ring and a bottom ring, and each top point lies directly above a partner with the same horizontal position.
- The solid is an octagonal prism whose cyclic order is read from the filled and hollow dots.
- The faces are two octagons and eight vertical quadrilaterals.
ANSWER: Top: KA-GD-QN-NZ-EV-QA-XS-HW; Bottom: KL-AZ-EL-UF-CY-HE-WA-CZ; Sides: KA-GD-AZ-KL, GD-QN-EL-AZ, QN-NZ-UF-EL, NZ-EV-CY-UF, EV-QA-HE-CY, QA-XS-WA-HE, XS-HW-CZ-WA, HW-KA-KL-CZ
