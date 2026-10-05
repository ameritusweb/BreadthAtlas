---
id: 002
question: turntable-solid
title: Antipodal pairs plus silhouette neighbours fix ring order
strategy: new: symmetry-then-silhouette-ordering
contributor: sonnet (blind player 2)
date: 2026-10-05
referee: opus/v1
criterion: v1
verdict: WRONG
reason: Steps 7–8 fail. They put tips next to each other (NZ–EV, KA–GD), but the four views fix the true ring order as KA, XS, EV, QA, NZ, QN, GD, HW: a four-pointed star whose tips alternate with inner corners. The chain's cycle NZ, EV, QA, XS, … crosses itself in the plane, so its two caps and eight side faces don't match the solid.
typed_1: symmetry | antipodal label pairs | turntable axis | invariant | horizontal screen coordinate | Several label pairs always have exactly opposite horizontal positions in all four views, so they are antipodal. This means the ring is centrally symmetric (NZ/KA, EV/GD, QA/HW, QN/XS).
typed_2: structure | silhouette neighbours | antipodal label pairs | = | cyclic order | Visible/hidden silhouette neighbours recur across views, and combined with the antipodal rule they fix a single cyclic order: NZ, EV, QA, XS, KA, GD, HW, QN.
typed_3: construction | lower ring | upper ring | bijects | - | The lower ring is the partner of each upper point in the same order, giving a prism with a symmetric octagonal cross-section.
---

CHAIN by blind player 2
1. 🧭 (root) — Given: each view is an orthographic projection of one solid on a turntable, and u is the horizontal screen coordinate.
2. 🔁 (root) — Given: sixteen points are plotted in every view, and rotating the solid only changes each point's u. Its height v stays fixed.
3. ⬆️⬇️ (← 2) — Every point has v at either the upper level or the lower level, so the points form two rings of eight. The labels line up in matching screen positions, so each upper point pairs with the lower point directly beneath it. The pairs are NZ/UF, EV/CY, QA/HE, QN/EL, XS/WA, HW/CZ, GD/AZ and KA/KL.
4. 🪞 (← 2) — Tracking one label across the four views shows that some labels always have exactly opposite u. NZ and KA are one such pair, and the same holds for EV and GD, QA and HW, and QN and XS. Each of these pairs is antipodal about the axis.
5. ⚖️ (← 4) — With four antipodal pairs, the eight-point ring is centrally symmetric about the turntable axis. In its cyclic order, each point sits four steps from its antipode.
6. 👁️ (← 1, 2) — The filled and hollow dots show which points face the viewer in each view. This hints at which points are neighbours along the silhouette. For example, the filled points in a view run along the front edge and the hollow ones along the back.
7. 🔗 (← 5, 6) — Neighbours that recur across views are NZ–EV, EV–QA, KA–GD, QN–GD or QN–NZ, and HW–XS or HW–QN. These recurring neighbours are the ring edges.
8. 🧩 (← 5, 7) — Combining the antipodal rule with the recurring neighbours gives one cycle: NZ, EV, QA, XS, KA, GD, HW, QN. The pairs NZ/KA, EV/GD, QA/HW and XS/QN each sit four steps apart. Every edge in this cycle shows up as a neighbour in at least one view.
9. 👀 (← 8, 4) — Self-check: the opposite points in this cycle are exactly the four antipodal pairs from step 4, and no label is used twice. The cycle passes.
10. 🧱 (← 3, 8) — The lower ring follows the same order through the partners from step 3: UF, CY, HE, WA, KL, AZ, CZ, EL. The two rings together bound a straight prism.
11. 📐 (← 10) — The faces are the top octagon, the bottom octagon, and one quadrilateral for each ring edge. Each quadrilateral takes two adjacent top points and their two partners below.
12. ✅ (← 9, 11) — All sixteen points are used, and every point lies on three faces. This gives the final face list.

LANDMARKS:
- Several label pairs always have exactly opposite horizontal positions in all four views, so they are antipodal. This means the ring is centrally symmetric (NZ/KA, EV/GD, QA/HW, QN/XS).
- Visible/hidden silhouette neighbours recur across views, and combined with the antipodal rule they fix a single cyclic order: NZ, EV, QA, XS, KA, GD, HW, QN.
- The lower ring is the partner of each upper point in the same order, giving a prism with a symmetric octagonal cross-section.

ANSWER: Octagonal prism with faces: top [NZ, EV, QA, XS, KA, GD, HW, QN]; bottom [UF, CY, HE, WA, KL, AZ, CZ, EL]; sides [NZ, EV, CY, UF], [EV, QA, HE, CY], [QA, XS, WA, HE], [XS, KA, KL, WA], [KA, GD, AZ, KL], [GD, HW, CZ, AZ], [HW, QN, EL, CZ], [QN, NZ, UF, EL]
