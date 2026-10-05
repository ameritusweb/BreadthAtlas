"""Regression tests for the form checker. Every case here was a real misjudgement during play.

  python scripts/test_form.py
"""
from play import Chain, CALC_RE

GOOD = """CHAIN by test
1. 🏊 (root) — Given: an Olympic pool holds a few million litres.
2. 🥤 (root) — Given: a person drinks a couple of litres a day.
3. ❓ (← 1, 2) — Asked: could one person drink the pool in a lifetime, and by what factor is the bigger quantity bigger?
4. 🗓️ (← 2) — Spreading the pool over a lifetime gives a daily quota.
5. 🌊 (← 1, 4) — That quota is on the order of a hundred litres a day.
6. 🫘 (root) — Given: kidneys clear about a litre an hour at best.
7. ⏱️ (← 6) — So sustained intake is capped at a few tens of litres a day.
8. 💥 (← 5, 7) — The quota contradicts the cap.
9. 👀 (← 8) — Self-check: the gap is not a close call.
10. 🚫 (← 8) — So no one could drink the pool.
11. 🏁 (← 10) — The pool is bigger by a factor in the tens.
LANDMARKS:
- Drinking the pool needs about a hundred litres a day.
- The body caps intake at a few tens of litres a day.
ANSWER: No; the pool is bigger by roughly 40 times.
"""

def run():
    failures = []
    c = Chain(GOOD)
    if not c.check_form():
        failures.append(f"GOOD chain rejected: {c.errors}")

    # a terminal 👀 and the ❓ step are never 'idle'  (turntable attempt 001; wire-cube attempts 001–003)
    assert "👀" in GOOD and "❓" in GOOD
    # an uncited partial conclusion is a NOTE for the referee, not a code failure (swap-ladder attempts 003–006)
    partial = GOOD.replace("10. 🚫 (← 8) — So no one could drink the pool.", "10. 🎯 (← 8) — So no one could drink the pool, which answers the first half.")
    partial = partial.replace("11. 🏁 (← 10)", "11. 🏁 (← 8)")
    c = Chain(partial)
    if not c.check_form() or not c.notes:
        failures.append(f"uncited partial conclusion should pass with a note: errors={c.errors} notes={c.notes}")

    # ❓ required and must precede the argument
    # same structure, but step 3 is an ordinary inference instead of ❓ (and is used later, so it is not idle)
    no_q = GOOD.replace("3. ❓ (← 1, 2) — Asked:", "3. 📌 (← 1, 2) — Note:").replace("4. 🗓️ (← 2) —", "4. 🗓️ (← 2, 3) —")
    c = Chain(no_q)
    if c.check_form() or not any("❓" in e for e in c.errors):
        failures.append("missing ❓ not caught")
    c = Chain(no_q)
    if not c.check_form(require_question=False):
        failures.append(f"form v1 should not require ❓: {c.errors}")

    # unparented non-root step  (pilot chain 1)
    bad = GOOD.replace("4. 🗓️ (← 2) —", "4. 🗓️ —")
    c = Chain(bad)
    if c.check_form() or not any("parent" in e for e in c.errors):
        failures.append("unparented step not caught")

    # arithmetic detector: false positives seen in play must pass, real arithmetic must fail
    must_pass = ["The board is a standard 8×8 chessboard whose squares alternate",
                 "the answer equals the answer for a shorter plane",
                 "a one-in-three chance, so 2/3 keep their seat",
                 "seats 1, 99 and 100 are symmetric",
                 "ten times a hundred is a thousand",
                 "about fifty metres long and two metres deep",
                 "Four orthographic turntable views (A at θ = 30°; B, C and D unknown)",   # a stated given, not a computation
                 "If the tips are all the same distance from the axis, NZ at the far left"]
    must_fail = ["10 times 100 is 1000", "2.5 million / 30000 = 83", "80 years x 365 days gives 29200 days", "so 4 + 4 = 8 faces"]
    for t in must_pass:
        if CALC_RE.search(t):
            failures.append(f"arithmetic false positive: {t!r}")
    for t in must_fail:
        if not CALC_RE.search(t):
            failures.append(f"arithmetic missed: {t!r}")

    # a colon separator and compound emoji tokens must parse (second SO game: Opus wrote "1. 🧑‍💻❓ (root): …")
    colon = GOOD.replace(" — ", ": ")
    c = Chain(colon)
    if len(c.steps) != 11 or not c.check_form():
        failures.append(f"colon-separated steps should parse: steps={len(c.steps)} errors={c.errors}")

    if failures:
        print("FAIL")
        for f in failures:
            print(" -", f)
        raise SystemExit(1)
    print("all form-checker regression tests pass")

if __name__ == "__main__":
    run()
