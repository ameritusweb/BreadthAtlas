"""Intuition test: guess the answer with no working, scored by tolerance.

  python scripts/guess_test.py <question-id> [--model MODEL] [--samples N]

Requires `guess_target` (a number) in the question's frontmatter; optional `guess_scale: log|linear`
(default log — error is |ln(guess/target)|) and `guess_unit` (shown to the model). Each sample is one
bare guess; the model is told not to calculate and to answer with a single number. Reports the share of
guesses within 10 %, 25 %, 50 % and a factor of 2 of the target, and the median error. Results go to
questions/<q>/guess/<model>-<date>.md.
"""
import argparse
import datetime as dt
import math
import re
import statistics

from play import Question, ask

PROMPT = """Answer the question below with a single number and nothing else. Do not calculate, do not write any working, do not search: give your immediate intuitive estimate. One line, one number.
{image}
REQUIRED ANSWER FORM: a single number expressing {unit}. Any other quantity or unit is wrong.

{question}
"""

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("question")
    ap.add_argument("--model", default="sonnet")
    ap.add_argument("--samples", type=int, default=5)
    args = ap.parse_args()
    q = Question(args.question)
    if "guess_target" not in q.meta:
        raise SystemExit(f"{q.id} has no guess_target in its frontmatter")
    target = float(q.meta["guess_target"])
    scale = q.meta.get("guess_scale", "log")
    unit = q.meta.get("guess_unit") or "the quantity the question asks for"
    image = (f"\nTHE IMAGE: the question refers to an image at {q.image}. Use your Read tool on that exact path to look at it once, then answer.\n" if q.image else "")
    guesses, errors, raws = [], [], []
    for i in range(args.samples):
        raw = ask(args.model, PROMPT.format(question=q.question, unit=unit, image=image), tools=q.tools, allowed=q.allowed)
        raws.append(raw)
        m = re.search(r"-?\d+(?:\.\d+)?(?:/\d+(?:\.\d+)?)?", raw.replace(",", ""))
        if not m:
            guesses.append(None); errors.append(None); continue
        s = m.group(0)
        g = (float(s.split("/")[0]) / float(s.split("/")[1])) if "/" in s else float(s)
        guesses.append(g)
        if scale == "log" and g > 0 and target > 0:
            errors.append(abs(math.log(g / target)))
        else:
            errors.append(abs(g - target) / abs(target) if target else abs(g - target))
    valid = [e for e in errors if e is not None]
    def within(frac):
        thr = math.log(1 + frac) if scale == "log" else frac
        return sum(1 for e in valid if e <= thr) / len(valid) if valid else 0
    summary = {"within 10%": within(0.10), "within 25%": within(0.25), "within 50%": within(0.50), "within 2x": within(1.0),
               "median error": statistics.median(valid) if valid else None, "n": len(valid)}
    out = q.dir / "guess"
    out.mkdir(exist_ok=True)
    date = dt.date.today().isoformat()
    lines = [f"---\nquestion: {q.id}\nmodel: {args.model}\ndate: {date}\ntarget: {target}\nscale: {scale}\nsamples: {args.samples}\n---\n",
             "| sample | raw | guess | error |", "|---|---|---|---|"]
    for i, (r, g, e) in enumerate(zip(raws, guesses, errors), 1):
        lines.append(f"| {i} | {r.strip()[:60]} | {g} | {'' if e is None else f'{e:.3f}'} |")
    lines.append("\n" + "\n".join(f"- {k}: {v if not isinstance(v, float) else round(v, 3)}" for k, v in summary.items()))
    (out / f"{args.model}-{date}.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"{q.id} / {args.model}: guesses {guesses}")
    print("summary:", {k: (round(v, 3) if isinstance(v, float) else v) for k, v in summary.items()})

if __name__ == "__main__":
    main()
