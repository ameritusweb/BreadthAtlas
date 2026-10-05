"""Example 1: a solid from its three orthographic views (third-angle, hidden lines dashed).
Builds the solid as voxels, counts its flat faces (the answer), and renders the views
with correct visible/hidden edges derived from the voxel model.

  python ex1_threeview.py [out.png] [key.json]      # questions/three-view-solid/drawing.png"""
import itertools
import json
from PIL import Image, ImageDraw, ImageFont

N = 4
solid = set(itertools.product(range(N), repeat=3))        # cells (i,j,k) cover [i-2,i-1] x ...
solid -= {(i, j, k) for i in (1, 2) for j in (2, 3) for k in range(N)}   # channel through the top, along z
solid -= {(i, 0, 0) for i in range(N)}                                  # step cut along the bottom-back edge

def cell(i, j, k):
    return (i, j, k) in solid

# ---- faces: boundary unit squares merged by coplanar edge-adjacency ----
unit_faces = []
for (i, j, k) in solid:
    for axis, s in itertools.product(range(3), (-1, 1)):
        nb = [i, j, k]
        nb[axis] += s
        if tuple(nb) not in solid:
            plane = (i, j, k)[axis] + (1 if s > 0 else 0)
            others = tuple(c for a, c in enumerate((i, j, k)) if a != axis)
            unit_faces.append((axis, s, plane, others))
groups = {}
for f in unit_faces:
    groups.setdefault(f[:3], []).append(f[3])
face_count = 0
for key, squares in groups.items():
    sq = set(squares)
    while sq:
        stack = [sq.pop()]
        face_count += 1
        while stack:
            a, b = stack.pop()
            for d in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nb = (a + d[0], b + d[1])
                if nb in sq:
                    sq.remove(nb)
                    stack.append(nb)

# ---- edges: unit edges of the surface, classified as crease or not ----
def crease(e_axis, coords):
    # coords: integer position in the two non-edge axes; cells around the edge
    other = [a for a in range(3) if a != e_axis]
    pattern = []
    for da, db in ((-1, -1), (-1, 0), (0, -1), (0, 0)):
        c = [0, 0, 0]
        c[other[0]] = coords[0] + da
        c[other[1]] = coords[1] + db
        pattern.append((da, db, c))
    def solid_at(t, c):
        c = list(c); c[e_axis] = t
        return cell(*c)
    return pattern, other, solid_at

def view_segments(d, viewer_sign):
    """Return {(h_axis_line, segment): 'visible'|'hidden'} for a view along axis d."""
    segs = {}
    for e_axis in range(3):
        if e_axis == d:
            continue
        s_axis = [a for a in range(3) if a not in (d, e_axis)][0]
        for t in range(N):                      # edge runs t..t+1 along e_axis
            for D in range(N + 1):              # depth plane
                for S in range(N + 1):          # line position
                    coords = {d: D, s_axis: S}
                    other = [a for a in range(3) if a != e_axis]
                    cnt = 0; pat = []
                    for da, db in ((-1, -1), (-1, 0), (0, -1), (0, 0)):
                        c = [0, 0, 0]
                        c[other[0]] = coords[other[0]] + da
                        c[other[1]] = coords[other[1]] + db
                        c[e_axis] = t
                        v = cell(*c); pat.append(v); cnt += v
                    is_crease = cnt in (1, 3) or (cnt == 2 and pat[0] == pat[3])
                    if not is_crease:
                        continue
                    # occlusion: both cells beside the line, at any depth in front, solid
                    occluded = False
                    depths = range(D, N) if viewer_sign > 0 else range(D - 1, -1, -1)
                    for c_d in depths:
                        both = True
                        for ds in (-1, 0):
                            c = [0, 0, 0]
                            c[d] = c_d; c[s_axis] = S + ds; c[e_axis] = t
                            if not cell(*c):
                                both = False
                        if both:
                            occluded = True
                            break
                    key = (e_axis, s_axis, S, t)
                    state = 'hidden' if occluded else 'visible'
                    if segs.get(key) != 'visible':
                        segs[key] = state
    return segs

# ---- render ----
SC = 60
font = ImageFont.truetype("arialbd.ttf", 20)
small = ImageFont.truetype("arial.ttf", 15)
img = Image.new("RGB", (2 * N * SC + 3 * 80 + 420, 2 * N * SC + 3 * 80 + 40), (250, 250, 248))
dr = ImageDraw.Draw(img)

def draw_view(d, viewer_sign, ox, oy, to2d, title):
    segs = view_segments(d, viewer_sign)
    dr.text((ox, oy - 34), title, font=font, fill=(28, 30, 36))
    for (e_axis, s_axis, S, t), state in segs.items():
        p3a = {e_axis: t, s_axis: S}; p3b = {e_axis: t + 1, s_axis: S}
        (h1, v1), (h2, v2) = to2d(p3a), to2d(p3b)
        x1, y1 = ox + h1 * SC, oy + v1 * SC
        x2, y2 = ox + h2 * SC, oy + v2 * SC
        if state == 'visible':
            dr.line((x1, y1, x2, y2), fill=(28, 30, 36), width=4)
        else:
            steps = 6
            for s in range(0, steps, 2):
                fx1 = x1 + (x2 - x1) * s / steps; fy1 = y1 + (y2 - y1) * s / steps
                fx2 = x1 + (x2 - x1) * (s + 1) / steps; fy2 = y1 + (y2 - y1) * (s + 1) / steps
                dr.line((fx1, fy1, fx2, fy2), fill=(90, 92, 100), width=3)

# third-angle: top view above front view; right-side view to the right of front view.
# top view: horizontal = x, vertical = z with the front (large z) at the bottom.
# front view: horizontal = x, vertical = y (up). right view: horizontal = -z (front at left), vertical = y.
X0, Y0 = 80, 80
draw_view(1, +1, X0, Y0, lambda p: (p[0], p[2]), "TOP")
draw_view(2, +1, X0, Y0 + N * SC + 80, lambda p: (p[0], N - p[1]), "FRONT")
draw_view(0, +1, X0 + N * SC + 80, Y0 + N * SC + 80, lambda p: (N - p[2], N - p[1]), "RIGHT SIDE")
dr.text((X0, img.height - 30), "Third-angle projection. Dashed = hidden edge. Front view looks along -z; top view looks down -y; right side looks along -x.", font=small, fill=(90, 92, 100))
import sys
OUT_PNG = sys.argv[1] if len(sys.argv) > 1 else "ex1_threeview.png"
OUT_KEY = sys.argv[2] if len(sys.argv) > 2 else "ex1_key.json"
img.save(OUT_PNG)

json.dump({"faces": face_count, "cells": sorted(solid)}, open(OUT_KEY, "w"))
print(f"faces: {face_count}; solid cells: {len(solid)}")
