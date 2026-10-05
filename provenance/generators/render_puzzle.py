"""Turntable puzzle renderer (questions/turntable-solid). Takes a derivation-benchmark instance and its
answer and draws the labelled orthographic views; the view angles and which panel shows its angle are
given on the command line. The instance shipped here (star4tilt.*) is the tilted star4 solid.

  python render_puzzle.py instance.json answer.json out.png key.json A:30:shown,B:0,C:110,D:230 [label-seed]
"""
import json
import math
import os
from PIL import Image, ImageDraw, ImageFont

import random
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
if len(sys.argv) >= 6:
    INSTANCE, ANSWER, OUT, KEY = sys.argv[1:5]
    PANELS = []
    for spec in sys.argv[5].split(","):
        parts = spec.split(":")
        PANELS.append((parts[0], int(parts[1]), len(parts) > 2 and parts[2] == "shown"))
    LABEL_SEED = int(sys.argv[6]) if len(sys.argv) > 6 else 7
else:
    INSTANCE = os.path.join(HERE, "star4tilt.interior.instance.json")
    ANSWER = os.path.join(HERE, "star4tilt.answer.json")
    OUT = "puzzle.png"
    KEY = "answer_key.json"
    PANELS = [("A", 30, True), ("B", 0, False), ("C", 110, False), ("D", 230, False)]
    LABEL_SEED = 7

S = 90                      # px per world unit
U_RANGE = (-3.2, 3.2)
V_RANGE = (-2.5, 2.5)
PLOT_W = int((U_RANGE[1] - U_RANGE[0]) * S)
PLOT_H = int((V_RANGE[1] - V_RANGE[0]) * S)
LABEL_BAND = 70
PAD = 40
PANEL_W = PLOT_W + 2 * PAD
PANEL_H = PLOT_H + 2 * LABEL_BAND + 2 * PAD + 30
HEADER = 135

INK = (28, 30, 36)
GRID_MINOR = (222, 224, 228)
GRID_MAJOR = (190, 193, 200)
AXIS = (120, 123, 130)
LEADER = (150, 152, 158)
BG = (250, 250, 248)

def font(size, bold=False):
    name = "arialbd.ttf" if bold else "arial.ttf"
    try:
        return ImageFont.truetype(name, size)
    except OSError:
        return ImageFont.load_default()

F_TITLE = font(30, True)
F_SUB = font(17)
F_PANEL = font(22, True)
F_TICK = font(13)
F_LABEL = font(15)

inst = json.load(open(INSTANCE))
views = {v["angle"]: v for v in inst["views"]}

rng = random.Random(LABEL_SEED)
codes = [a + b for a in "ABCDEFGHJKLMNPQRSTUVWXYZ" for b in "ABCDEFGHJKLMNPQRSTUVWXYZ" if a != b]
rng.shuffle(codes)
label = {p["id"]: codes[i] for i, p in enumerate(inst["points"])}

img = Image.new("RGB", (2 * PANEL_W + 3 * PAD, HEADER + 2 * PANEL_H + 3 * PAD), BG)
d = ImageDraw.Draw(img)

d.text((PAD, 28), "TURNTABLE VIEWS OF ONE SOLID", font=F_TITLE, fill=INK)
d.text((PAD, 70), "Orthographic projections. The solid rotates about a vertical axis through the origin;"
                  " u is horizontal in the view, v is world y.", font=F_SUB, fill=INK)
lx, ly = PAD, 100
d.ellipse((lx, ly + 2, lx + 14, ly + 16), fill=INK)
d.text((lx + 22, ly), "visible", font=F_SUB, fill=INK)
d.ellipse((lx + 110, ly + 2, lx + 124, ly + 16), outline=INK, width=3, fill=BG)
d.text((lx + 132, ly), "hidden", font=F_SUB, fill=INK)

def draw_panel(ox, oy, name, angle, show_angle):
    view = views[angle]
    px0 = ox + PAD
    py0 = oy + PAD + 30 + LABEL_BAND
    def to_px(u, v):
        return (px0 + (u - U_RANGE[0]) * S, py0 + (V_RANGE[1] - v) * S)

    title = f"View {name}   θ = {angle}°" if show_angle else f"View {name}   θ = ?"
    d.text((ox + PAD, oy + PAD - 8), title, font=F_PANEL, fill=INK)

    d.rectangle((px0, py0, px0 + PLOT_W, py0 + PLOT_H), outline=AXIS, width=1, fill=(255, 255, 255))
    u = math.ceil(U_RANGE[0] * 2) / 2
    while u <= U_RANGE[1]:
        x, _ = to_px(u, 0)
        d.line((x, py0, x, py0 + PLOT_H), fill=GRID_MAJOR if float(u).is_integer() else GRID_MINOR, width=1)
        if abs(u - round(u * 2) / 2) < 1e-9:
            t = f"{u:g}"
            w = d.textlength(t, font=F_TICK)
            d.text((x - w / 2, py0 + PLOT_H + 4), t, font=F_TICK, fill=AXIS)
        u += 0.5
    v = math.ceil(V_RANGE[0] * 2) / 2
    while v <= V_RANGE[1]:
        _, y = to_px(0, v)
        d.line((px0, y, px0 + PLOT_W, y), fill=GRID_MAJOR if float(v).is_integer() else GRID_MINOR, width=1)
        t = f"{v:g}"
        w = d.textlength(t, font=F_TICK)
        d.text((px0 - w - 6, y - 8), t, font=F_TICK, fill=AXIS)
        v += 0.5
    x0, y0 = to_px(0, 0)
    d.line((x0, py0, x0, py0 + PLOT_H), fill=AXIS, width=2)
    d.line((px0, y0, px0 + PLOT_W, y0), fill=AXIS, width=2)
    d.text((px0 + PLOT_W - 14, y0 + 6), "u", font=F_LABEL, fill=AXIS)
    d.text((x0 + 8, py0 + 2), "v", font=F_LABEL, fill=AXIS)

    for row_sign, pts in ((1, [p for p in view["points"] if p["v"] > 0]),
                          (-1, [p for p in view["points"] if p["v"] < 0])):
        pts = sorted(pts, key=lambda p: p["u"])
        n = len(pts)
        slot_w = PLOT_W / n
        for i, p in enumerate(pts):
            x, y = to_px(p["u"], p["v"])
            lxc = px0 + slot_w * (i + 0.5)
            ly = py0 - LABEL_BAND + 18 if row_sign > 0 else py0 + PLOT_H + LABEL_BAND - 18
            d.line((x, y, lxc, ly + (14 if row_sign > 0 else -4)), fill=LEADER, width=1)
            r = 7
            if p["visible"]:
                d.ellipse((x - r, y - r, x + r, y + r), fill=INK)
            else:
                d.ellipse((x - r, y - r, x + r, y + r), outline=INK, width=3, fill=(255, 255, 255))
            w = d.textlength(label[p["id"]], font=F_LABEL)
            d.text((lxc - w / 2, ly - 8), label[p["id"]], font=F_LABEL, fill=INK)

for i, (name, angle, show) in enumerate(PANELS):
    col, row = i % 2, i // 2
    draw_panel(PAD + col * (PANEL_W + PAD), HEADER + PAD + row * (PANEL_H + PAD), name, angle, show)

img.save(OUT)

ans = json.load(open(ANSWER))
ids = [p["id"] for p in inst["points"]]
key = {
    "shape": inst["name"],
    "description": inst["description"],
    "panels": [{"view": n, "angle": a, "angleShown": s} for n, a, s in PANELS],
    "labels": label,
    "points": {label[p["id"]]: p["position"] for p in inst["points"]},
    "outlineColumnOrder": [[label[f"c{i}.a"], label[f"c{i}.b"]] for i in range(8)],
    "totalArea": inst["totalArea"],
    "creases": ans["signature"],
    "faces": [[label[ids[i]] for i in f] for f in ans["faces"]],
    "visibility": {str(a): {label[p["id"]]: p["visible"] for p in views[a]["points"]} for _, a, _ in PANELS},
}
json.dump(key, open(KEY, "w"), indent=1)
print(f"wrote {OUT} ({img.width}x{img.height}) and {KEY}")
