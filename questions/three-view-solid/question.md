---
id: three-view-solid
title: Faces of a solid from its three views
status: answered
added: 2026-10-05
image: drawing.png
key: answer_key.json
family: multi-view reconstruction
attractor: none (novel instance; generator provenance/generators/ex1_threeview.py)
guess_target: 12
guess_scale: linear
guess_unit: number of faces
---

# Question

The drawing shows the top, front and right-side views of one solid in third-angle projection. Solid
lines are visible edges; dashed lines are edges hidden behind the solid. The front view looks along −z,
the top view looks down −y, the right-side view looks along −x. Every face is flat and every edge is
parallel to an axis. **How many faces does the solid have?** A face is one flat region of the surface,
whatever its outline shape.

# Reference answer (referee only)

**12.** The solid is a 4×4×4 block with a 2-wide, 2-deep channel through the top running the full
depth (along z) and a 1×1 step cut along the bottom-back edge across the full width. Faces: bottom,
back, front, two L-shaped sides, two top strips, two channel walls, channel floor, step tread, step
riser. Tolerance: exact. (Generated from a voxel model; the hidden/visible edges in the drawing are
computed, not drawn by hand.)

# Why it is in the atlas

Reconstruction family. The calculation route is a search for solids consistent with three drawings;
the holistic route is reading the drawing as a machinist does. Hidden lines are the trap: read as
visible, or ignored, they produce a different solid.

# Breadth

No routes yet.
