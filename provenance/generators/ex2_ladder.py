"""Example 2: a swap ladder (ghost-leg) with 12 rails and 41 rungs: 20 rungs, one stray middle rung,
then the 20 rungs mirrored. Simulates the swaps (the calculation route) and renders the ladder.

  python ex2_ladder.py [seed] [out.png] [key.json]   # questions/swap-ladder (seed 11), swap-ladder-b"""
import json
import random
from PIL import Image, ImageDraw, ImageFont

import sys

RAILS = 12
HALF = 20
TOKENS = "ABCDEFGHJKLM"
SEED = int(sys.argv[1]) if len(sys.argv) > 1 else 11
OUT_PNG = sys.argv[2] if len(sys.argv) > 2 else "ex2_ladder.png"
OUT_KEY = sys.argv[3] if len(sys.argv) > 3 else "ex2_key.json"
rng = random.Random(SEED)

while True:
    top = []
    while len(top) < HALF:
        a = rng.randrange(RAILS - 1)
        if top and top[-1] == a:
            continue
        top.append(a)                      # rung between rails a and a+1 (0-based)
    mid = rng.randrange(RAILS - 1)
    rungs = top + [mid] + top[::-1]
    state = list(TOKENS)
    for a in rungs:
        state[a], state[a + 1] = state[a + 1], state[a]
    moved = [i for i, t in enumerate(state) if t != TOKENS[i]]
    if len(moved) == 2 and mid not in (top[-1],):
        break

ask_pos = moved[0] + 1
answer_token = state[moved[0]]
home = RAILS - len(moved)

W, H = 70 * (RAILS - 1) + 160, 24 * len(rungs) + 210
img = Image.new("RGB", (W, H), (250, 250, 248))
dr = ImageDraw.Draw(img)
font = ImageFont.truetype("arialbd.ttf", 20)
small = ImageFont.truetype("arial.ttf", 14)
ox, oy, dx, dy = 80, 80, 70, 24
for r in range(RAILS):
    x = ox + r * dx
    dr.line((x, oy, x, oy + dy * (len(rungs) + 1)), fill=(150, 152, 158), width=2)
    dr.text((x - 7, oy - 32), TOKENS[r], font=font, fill=(28, 30, 36))
    dr.text((x - 8, oy + dy * (len(rungs) + 1) + 8), str(r + 1), font=font, fill=(28, 30, 36))
for row, a in enumerate(rungs):
    y = oy + dy * (row + 1)
    x1, x2 = ox + a * dx, ox + (a + 1) * dx
    dr.line((x1, y, x2, y), fill=(28, 30, 36), width=5)
    if row % 5 == 4:
        dr.text((ox - 40, y - 8), str(row + 1), font=small, fill=(120, 123, 130))
dr.text((ox - 60, H - 36), "Tokens start at the top on the rail below their letter. Rungs are applied top to bottom; each rung swaps the two tokens on its rails.", font=small, fill=(90, 92, 100))
img.save(OUT_PNG)

json.dump({"rungs_1based": [a + 1 for a in rungs], "final_positions": state, "moved_positions_1based": [m + 1 for m in moved],
           "ask_position": ask_pos, "answer_token": answer_token, "tokens_home": home, "middle_rung_rails": [mid + 1, mid + 2]},
          open(OUT_KEY, "w"), indent=1)
print(f"rungs: {len(rungs)}; middle rung rails {mid+1}-{mid+2}; final: {''.join(state)}")
print(f"moved positions: {[m+1 for m in moved]} -> tokens {[state[m] for m in moved]}; ask position {ask_pos}: {answer_token}; tokens home: {home}")
