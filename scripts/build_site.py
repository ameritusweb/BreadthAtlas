"""Render the archive as a static site: site/index.html (ranked questions, question-by-year grid,
models by routes, where intuition overreached) and site/q/<id>.html (every route and attempt with its
chain, verdict, reason, landmarks, typed landmarks). Built from the folders, not from LEADERBOARD.md.

  python scripts/build_site.py
"""
import html
import re
from collections import defaultdict
from pathlib import Path

from play import frontmatter, read, section, ROOT

SITE = ROOT / "site"
CSS = """
body{font:15px/1.5 system-ui,sans-serif;max-width:1100px;margin:2rem auto;padding:0 1rem;color:#1c1e24;background:#fafaf8}
table{border-collapse:collapse;width:100%;margin:1rem 0}th,td{border:1px solid #ddd;padding:.4rem .6rem;text-align:left;vertical-align:top}
th{background:#f0f0ec}code,pre{font-family:ui-monospace,Consolas,monospace}pre{background:#f4f4f1;padding:.8rem;white-space:pre-wrap}
.v-VALID{color:#1a7f37;font-weight:600}.v-WRONG{color:#b42318;font-weight:600}.v-DUPLICATE{color:#8a6d00;font-weight:600}.v-ILL-FORMED{color:#666;font-weight:600}
.chain{border-left:4px solid #ddd;padding-left:1rem;margin:1rem 0}.meta{color:#555;font-size:.9em}a{color:#0b57d0}
"""

def esc(s):
    return html.escape(str(s if s is not None else ""))

def load():
    questions = {}
    for qdir in sorted(p for p in (ROOT / "questions").iterdir() if p.is_dir()):
        text = read(qdir / "question.md") if (qdir / "question.md").exists() else ""
        q = {"id": qdir.name, "meta": frontmatter(text), "question": section(text, "Question"), "routes": [], "attempts": []}
        for kind in ("routes", "attempts"):
            for f in sorted((qdir / kind).glob("*.md")) if (qdir / kind).exists() else []:
                t = read(f)
                q[kind].append({"meta": frontmatter(t), "body": t.split("---", 2)[-1].strip(), "file": f.name})
        questions[qdir.name] = q
    return questions

def chain_html(c):
    m = c["meta"]
    typed = [m[k] for k in sorted(k for k in m if k.startswith("typed_"))]
    extra = "".join(f"<div class='meta'><b>{esc(k)}:</b> {esc(m[k])}</div>" for k in ("empirical", "repeats", "supersedes", "note") if m.get(k))
    return f"""<div class='chain'>
<h4>{esc(m.get('title', c['file']))} <span class='v-{esc(m.get('verdict'))}'>{esc(m.get('verdict'))}</span></h4>
<div class='meta'>{esc(m.get('contributor'))} · {esc(m.get('date'))} · strategy <code>{esc(m.get('strategy'))}</code>{' · depth ' + esc(m['depth']) if m.get('depth') else ''} · {esc(m.get('referee'))} / criterion {esc(m.get('criterion'))}</div>
<div class='meta'><b>reason:</b> {esc(m.get('reason'))}</div>{extra}
<pre>{esc(c['body'])}</pre>
{('<div class="meta"><b>typed landmarks</b><br>' + '<br>'.join(esc(t) for t in typed) + '</div>') if typed else ''}
</div>"""

def question_page(q):
    m = q["meta"]
    glossary = ""
    qtext = read(ROOT / "questions" / q["id"] / "question.md")
    g = section(qtext, "Glossary")
    if g:
        glossary = f"<h3>Glossary</h3><pre>{esc(g)}</pre>"
    parts = [f"<html><head><meta charset='utf-8'><title>{esc(m.get('title', q['id']))}</title><style>{CSS}</style></head><body>",
             f"<p><a href='../index.html'>← atlas</a></p><h1>{esc(m.get('title', q['id']))}</h1>",
             f"<div class='meta'>family: {esc(m.get('family'))} · status: {esc(m.get('status'))} · attractor: {esc(m.get('attractor'))}" + (f" · discriminator: {esc(m.get('discriminator'))}" if m.get('discriminator') else "") + "</div>",
             f"<h3>Question</h3><pre>{esc(q['question'])}</pre>", glossary,
             f"<h2>Accepted routes ({len(q['routes'])})</h2>"] + [chain_html(c) for c in sorted(q["routes"], key=lambda c: int(c["meta"].get("depth", 0)))] + \
            [f"<h2>Attempts ({len(q['attempts'])}) — the boundary</h2>"] + [chain_html(c) for c in q["attempts"]] + ["</body></html>"]
    return "\n".join(parts)

def model_of(contributor):
    name = (contributor or "").split("(")[0].strip().lower()
    for alias, canon in (("claude-sonnet", "sonnet"), ("claude-opus", "opus"), ("claude fable", "fable")):
        if name.startswith(alias):
            return canon
    return name or "unknown"

def index_page(questions):
    ranked = sorted(questions.values(), key=lambda q: -len(q["routes"]))
    years = sorted({c["meta"].get("date", "")[:4] for q in questions.values() for c in q["routes"] if c["meta"].get("date")})
    rows = []
    for i, q in enumerate(ranked, 1):
        v = [c["meta"].get("verdict") for c in q["attempts"]]
        strategies = ", ".join(sorted({c["meta"].get("strategy", "?") for c in q["routes"]})) or "—"
        rows.append(f"<tr><td>{i}</td><td><a href='q/{q['id']}.html'>{esc(q['meta'].get('title', q['id']))}</a></td><td>{len(q['routes'])}</td><td>{esc(strategies)}</td><td>{len(v)} ({v.count('WRONG')} / {v.count('DUPLICATE')} / {v.count('ILL-FORMED')})</td><td>{esc(q['meta'].get('status'))}</td></tr>")
    grid = []
    for q in ranked:
        cells = "".join(f"<td>{sum(1 for c in q['routes'] if c['meta'].get('date', '').startswith(y))}</td>" for y in years)
        grid.append(f"<tr><td>{esc(q['id'])}</td>{cells}<td>{len(q['routes'])}</td></tr>")
    models = defaultdict(lambda: {"routes": 0, "score": 0, "qs": set()})
    for q in questions.values():
        for c in q["routes"]:
            mdl = model_of(c["meta"].get("contributor"))
            models[mdl]["routes"] += 1
            models[mdl]["score"] += int(c["meta"].get("depth", 1))
            models[mdl]["qs"].add(q["id"])
    mrows = [f"<tr><td>{esc(mname)}</td><td>{d['routes']}</td><td>{d['score']}</td><td>{len(d['qs'])}</td></tr>" for mname, d in sorted(models.items(), key=lambda kv: -kv[1]["routes"])]
    over = [f"<tr><td><a href='q/{q['id']}.html'>{esc(q['id'])}</a></td><td>{esc(c['meta'].get('title'))}</td><td class='v-{esc(c['meta'].get('verdict'))}'>{esc(c['meta'].get('verdict'))}</td><td>{esc((c['meta'].get('reason') or '')[:220])}</td></tr>" for q in ranked for c in q["attempts"]]
    total_r = sum(len(q["routes"]) for q in questions.values()); total_a = sum(len(q["attempts"]) for q in questions.values())
    return f"""<html><head><meta charset='utf-8'><title>Breadth Atlas</title><style>{CSS}</style></head><body>
<h1>Breadth Atlas</h1>
<p>How many genuinely different ways can a problem be seen? {len(questions)} questions · {total_r} accepted routes · {total_a} attempts kept as the boundary. Every chain is an emoji route with no calculation; accepted routes bind the frontier; rejected ones map where intuition overreached.</p>
<h2>Questions by breadth</h2><table><tr><th>#</th><th>question</th><th>breadth</th><th>strategies</th><th>attempts (wrong / dup / ill-formed)</th><th>status</th></tr>{''.join(rows)}</table>
<h2>Accepted routes by question and year</h2><table><tr><th>question</th>{''.join(f'<th>{esc(y)}</th>' for y in years)}<th>total</th></tr>{''.join(grid)}</table>
<h2>Models by routes discovered</h2><table><tr><th>model</th><th>routes</th><th>depth-weighted score</th><th>questions</th></tr>{''.join(mrows)}</table>
<h2>Where intuition overreached</h2><table><tr><th>question</th><th>attempt</th><th>verdict</th><th>reason</th></tr>{''.join(over)}</table>
<p class='meta'>Generated by scripts/build_site.py from the archive folders. Rules: REFEREE.md · Strategies: STRATEGIES.md · End goal: GOAL.md</p>
</body></html>"""

def main():
    questions = load()
    (SITE / "q").mkdir(parents=True, exist_ok=True)
    (SITE / "index.html").write_text(index_page(questions), encoding="utf-8")
    for q in questions.values():
        (SITE / "q" / f"{q['id']}.html").write_text(question_page(q), encoding="utf-8")
    print(f"site: {SITE / 'index.html'} + {len(questions)} question pages")

if __name__ == "__main__":
    main()
