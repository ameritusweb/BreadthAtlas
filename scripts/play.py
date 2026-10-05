"""Play engine for the Breadth Atlas.

  python scripts/play.py <question-id> [--mode duel|blind|extend] [--turns N] [--players N]
                         [--duelist MODEL] [--referee MODEL] [--backend cli]

Modes
  duel    two players alternate; a chain that loses ends the round; challenges allowed
  blind   N independent players each submit one chain against the frontier as of game start
  extend  one player makes up to N attempts against the live frontier (the benchmark call)

Form is checked in code (REFEREE.md section 1). Only soundness, novelty and challenges go to the
referee model. Every played chain is written to routes/ or attempts/, its landmarks appended to
landmarks.md, the raw game archived under games/, and LEADERBOARD.md regenerated.
"""
import argparse
import datetime as dt
import re
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TODAY = dt.date.today().isoformat()
CRITERION = "v2"

# ----------------------------------------------------------------------------- model backend

def ask(model, prompt, timeout=600, tools="", retries=3, allowed=None):
    """`tools` names the tools available; `allowed` (optional) is the permission rule list, which may
    scope a tool to a path pattern, e.g. ["Read", "Write(/path/to/scorers/**)"]. Defaults to `tools`."""
    cmd = ["claude", "-p", "--model", model, "--output-format", "text", "--tools", tools]
    if tools:
        cmd += ["--allowedTools", ",".join(allowed) if allowed else tools]   # headless runs auto-deny unapproved tool calls
    last = ""
    for attempt in range(retries):
        r = subprocess.run(cmd, input=prompt, capture_output=True, text=True, encoding="utf-8", timeout=timeout, shell=(sys.platform == "win32"))
        out = r.stdout.strip()
        if r.returncode == 0 and out:
            return out
        last = r.stderr.strip()[:500] or "(empty output)"
        time.sleep(5 * (attempt + 1))
    raise RuntimeError(f"claude -p failed ({model}) after {retries} attempts: {last}")

# ----------------------------------------------------------------------------- repo access

def read(path):
    return path.read_text(encoding="utf-8")

def section(text, heading):
    m = re.search(rf"^#+\s*{re.escape(heading)}.*?\n(.*?)(?=^#|\Z)", text, re.S | re.M)
    return m.group(1).strip() if m else ""

def frontmatter(text):
    m = re.match(r"---\n(.*?)\n---", text, re.S)
    meta = {}
    if m:
        for line in m.group(1).splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                meta[k.strip()] = v.strip()
    return meta

class Question:
    def __init__(self, qid):
        self.id = qid
        self.dir = ROOT / "questions" / qid
        if not self.dir.exists():
            sys.exit(f"no such question: {qid}")
        text = read(self.dir / "question.md")
        self.meta = frontmatter(text)
        self.title = self.meta.get("title", qid)
        self.question = section(text, "Question")
        glossary = section(text, "Glossary")
        if glossary:
            self.question += "\n\nGLOSSARY (shared emoji vocabulary for this question; use it where it fits):\n" + glossary
        self.vocabulary = section(text, "Vocabulary")   # controlled subject/object phrases for typed landmarks
        # `attach:` — files (relative to the question folder) whose contents are appended to the question text
        for rel in [a.strip() for a in self.meta.get("attach", "").split(",") if a.strip()]:
            fp = self.dir / rel
            if fp.exists():
                self.question += f"\n\n=== ATTACHED: {rel} ===\n" + read(fp).strip()
        self.reference = section(text, "Reference answer")
        self.open = self.meta.get("status", "") == "open"
        self.image = (self.dir / self.meta["image"]).resolve() if self.meta.get("image") else None
        # tools a player may use: Read for image questions; a question may add more via `tools:` (e.g. "Read,Write"
        # for questions whose routes include an executable scorer — note this executes model-written code locally)
        extra = [t.strip() for t in self.meta.get("tools", "").split(",") if t.strip()]
        base = ["Read"] if self.image else []
        self.tools = ",".join(dict.fromkeys(base + extra))
        # permission rules: Write is scoped to the question's scorers folder
        scorers = (self.dir / "scorers").resolve().as_posix()
        self.allowed = [("Write(" + scorers + "/**)") if t == "Write" else t for t in self.tools.split(",") if t] or None
        for sub in ("routes", "attempts", "games"):
            (self.dir / sub).mkdir(parents=True, exist_ok=True)

    def image_block(self):
        out = ""
        if self.image:
            out += (f"\nTHE IMAGE. The question refers to an image at {self.image}. Use your Read tool on that exact path "
                    f"to view it before reasoning; do not read any other file.\n")
        if self.meta.get("scorer_inline"):
            out += (f"\nSCORER FILES. Your route must include an executable scorer. Do NOT try to write files. Instead, include the "
                    f"scorer's full Python source in your reply, immediately BEFORE the chain, as:\n"
                    f"SCORER FILE: scorers/<fresh-name>.py\n```python\n<source>\n```\n"
                    f"The runner saves it under {self.dir / 'scorers'} (it refuses to overwrite) and the referee runs it. Cite the same "
                    f"path in the ANSWER line. You may Read existing files in that folder for the contract and the helpers "
                    f"(poc4_components.py, mech_family_linear.py).\n")
        return out

    def routes(self):
        return sorted((self.dir / "routes").glob("*.md"))

    def attempts(self):
        return sorted((self.dir / "attempts").glob("*.md"))

    def next_id(self, kind):
        files = self.routes() if kind == "routes" else self.attempts()
        return f"{len(files) + 1:03d}"

    def landmark_rows(self):
        path = self.dir / "landmarks.md"
        if not path.exists():
            return []
        rows = []
        for line in read(path).splitlines():
            m = re.match(r"\|\s*(\d+)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|", line)
            if m:
                rows.append({"n": int(m.group(1)), "landmark": m.group(2), "chain": m.group(3), "verdict": m.group(4)})
        return rows

    def used_landmarks_text(self):
        rows = self.landmark_rows()
        if not rows:
            return "(none yet — the frontier is empty)"
        binding = [r for r in rows if r["verdict"] == "VALID"]
        rejected = [r for r in rows if r["verdict"] != "VALID"]
        out = []
        if binding:
            out.append("BINDING (accepted routes — a new chain must introduce a landmark not here):")
            out += [f"{r['n']}. {r['landmark']}  [{r['chain']}, VALID]" for r in binding]
        else:
            out.append("BINDING: none yet — no chain has been accepted; only accepted chains' landmarks bind.")
        if rejected:
            out.append("CHARTED DEAD ENDS (rejected chains — not binding; a chain that re-walks one is marked REPEATS):")
            out += [f"{r['n']}. {r['landmark']}  [{r['chain']}, {r['verdict']}]" for r in rejected]
        return "\n".join(out)

    def append_landmarks(self, landmarks, chain_ref, verdict):
        path = self.dir / "landmarks.md"
        rows = self.landmark_rows()
        n = rows[-1]["n"] if rows else 0
        if not path.exists() or "| # |" not in read(path):
            path.write_text(f"# Frontier — landmarks used so far ({self.id})\n\nRows marked VALID bind the frontier; the rest record what was tried and how it failed.\n\n| # | landmark | chain | verdict |\n|---|---|---|---|\n", encoding="utf-8")
        text = read(path).rstrip("\n")
        if text.endswith("No chains played yet."):
            text += "\n\n| # | landmark | chain | verdict |\n|---|---|---|---|"
        for lm in landmarks:
            n += 1
            text += f"\n| {n} | {lm} | {chain_ref} | {verdict} |"
        path.write_text(text + "\n", encoding="utf-8")

    def typed_vocabulary(self):
        """Typed landmarks already recorded on this question's routes, as reference vocabulary —
        preceded by the question's controlled vocabulary when it has one."""
        lines = []
        if self.vocabulary:
            lines.append("CONTROLLED VOCABULARY — subject and object MUST be one of these phrases (or '-'); if none fits, use the closest and append '?' to flag it for review:")
            lines.append(self.vocabulary)
            lines.append("Already-typed landmarks on this question:")
        for f in self.routes():
            meta = frontmatter(read(f))
            for k in sorted(k for k in meta if k.startswith("typed_")):
                lines.append(f"{meta[k]}  [route {meta.get('id')}]")
        return "\n".join(lines) if lines else "(none typed yet)"

    def prior_chain_texts(self):
        out = []
        for f in self.routes() + self.attempts():
            t = read(f)
            meta = frontmatter(t)
            body = t.split("---", 2)[-1].strip()
            out.append((f.parent.name[:-1] + " " + meta.get("id", "?"), meta.get("verdict", "?"), body))
        return out

# ----------------------------------------------------------------------------- chain parsing & form

STEP_RE = re.compile(r"^\s*(\d+)\.\s+(.+?)\s*(\(root\)|\(\s*←[^)]*\))?\s*(?:[—–-]+|:)\s*(.+)$")
PARENT_RE = re.compile(r"\d+")
# arithmetic = digits combined by an operator AND a stated numeric result ("8 × 8 is 64", "= 64");
# bare dimensions ("8×8 board"), fractions ("2/3") and ranges are values, not calculation
CALC_RE = re.compile(r"\d[\d,.]*[^\d.;:,]{0,14}?(?:[×*/÷+]|\bx\b|\btimes\b|divided by|\bplus\b|\bminus\b)\s*\d[\d,.]*[^.;:]{0,30}?(?:=|\b(?:is|equals|makes|gives|comes to|leaves)\b)\s*(?:about |roughly |around )?\d", re.I)

class Chain:
    def __init__(self, text):
        self.text = text.strip()
        self.steps = []          # dicts: n, emoji, root, parents, explanation
        self.landmarks = []
        self.answer = ""
        self.errors = []
        self.parse()

    def parse(self):
        lines = self.text.splitlines()
        in_landmarks = False
        for line in lines:
            s = line.strip()
            if not s:
                continue
            if s.upper().startswith("LANDMARKS"):
                in_landmarks = True
                continue
            if s.upper().startswith("ANSWER"):
                in_landmarks = False
                self.answer = s.split(":", 1)[1].strip() if ":" in s else s
                continue
            if in_landmarks:
                if s.startswith(("-", "•", "*")):
                    self.landmarks.append(s.lstrip("-•* ").strip())
                continue
            m = STEP_RE.match(s)
            if m:
                n = int(m.group(1))
                emoji = m.group(2).strip()
                tag = m.group(3) or ""
                root = tag.strip() == "(root)"
                parents = [int(x) for x in PARENT_RE.findall(tag)] if not root else []
                self.steps.append({"n": n, "emoji": emoji, "root": root, "parents": parents, "explanation": m.group(4).strip()})

    def check_form(self, require_question=True):
        e = self.errors
        if len(self.steps) < 10:
            e.append(f"only {len(self.steps)} emoji steps; at least 10 required")
        seen = set()
        referenced = set()
        for i, st in enumerate(self.steps):
            if st["n"] != i + 1:
                e.append(f"step numbering breaks at {st['n']}")
                break
            if not st["root"] and not st["parents"] and i > 0:
                e.append(f"step {st['n']} has no parent tag and is not marked (root)")
            for p in st["parents"]:
                if p >= st["n"] or p not in seen:
                    e.append(f"step {st['n']} names parent {p}, which is not an earlier step")
                referenced.add(p)
            if not st["explanation"]:
                e.append(f"step {st['n']} has no explanation")
            if CALC_RE.search(st["explanation"]):
                e.append(f"step {st['n']} performs arithmetic: '{st['explanation'][:60]}…'")
            seen.add(st["n"])
        self.notes = []
        if self.steps:
            last = self.steps[-1]["n"]
            # Unreferenced steps are reported to the referee as a form note, not failed by code: whether a
            # step "does work" is semantic (a stated partial conclusion does; a decorative step does not).
            # 👀 and ❓ are exempt by convention.
            idle = [st["n"] for st in self.steps if st["n"] != last and st["n"] not in referenced and not any(x in st["emoji"] for x in ("👀", "❓"))]
            if idle:
                self.notes.append(f"steps {idle} are not cited by any later step; rule ILL-FORMED only if they do no work in the argument (a stated partial conclusion or a self-check written in the explanation does work)")
        q_steps = [st["n"] for st in self.steps if "❓" in st["emoji"]]
        if not q_steps:
            if require_question:
                e.append("no ❓ step stating what is asked")
        else:
            first_inference = next((st["n"] for st in self.steps if not st["root"] and "❓" not in st["emoji"]), None)
            if first_inference is not None and q_steps[0] > first_inference:
                e.append(f"the ❓ step ({q_steps[0]}) comes after the argument starts (step {first_inference})")
        if not (2 <= len(self.landmarks) <= 4):
            e.append(f"{len(self.landmarks)} landmarks; 2–4 required")
        if not self.answer:
            e.append("no ANSWER line")
        elif self.text.strip().splitlines()[-1].strip().upper().startswith("ANSWER") is False:
            e.append("the answer is not the last line")
        return not e

CHALLENGE_RE = re.compile(r"CHALLENGE\s+(?:chain|route)\s+(\d+)\s+step\s+(\d+)\s*:\s*(.+)", re.I | re.S)
SCORER_RE = re.compile(r"SCORER FILE:\s*scorers/([\w\-]+\.py)\s*\n```(?:python)?\s*\n(.*?)\n```", re.S)

def save_inline_scorer(q, raw, game_log):
    """If the reply carries an inline scorer, write it under the question's scorers/ (never overwriting)
    and strip it from the text so the chain parser sees only the chain."""
    m = SCORER_RE.search(raw)
    if not m or not q.meta.get("scorer_inline"):
        return raw
    name, src = m.group(1), m.group(2)
    dest = q.dir / "scorers" / name
    if dest.exists():
        game_log.append(f"\n<!-- inline scorer {name} NOT saved: file exists -->\n")
    else:
        dest.parent.mkdir(exist_ok=True)
        dest.write_text(src.rstrip() + "\n", encoding="utf-8")
        game_log.append(f"\n<!-- inline scorer saved: {dest} ({len(src)} chars) -->\n")
    return raw[:m.start()] + raw[m.end():]

# ----------------------------------------------------------------------------- prompts

def rules_text():
    return read(ROOT / "REFEREE.md")

def duelist_prompt(q, player, prior, mode, allow_challenge):
    prior_block = "\n\n".join(f"--- {ref} ({verdict}) ---\n{body}" for ref, verdict, body in prior) if prior else "(no chains played yet)"
    challenge = ("\nInstead of playing, you may CHALLENGE the most recent accepted chain by writing exactly:\n"
                 "CHALLENGE chain <n> step <k>: <one or two sentences naming the flaw>\n"
                 "A successful challenge wins the round; a failed one loses it.\n") if allow_challenge else ""
    return f"""You are {player} in the Breadth Atlas game. Do not use tools or search; respond from your own judgment.

THE GAME. Players produce emoji reasoning chains for a question. A referee rules each chain VALID, WRONG (a step does not follow or a claim or the answer is false), DUPLICATE (the same line of reasoning as any chain already played, merely re-dressed), or ILL-FORMED (breaks the chain rules). Only a VALID chain that passes through at least one landmark no earlier chain used counts. Accuracy matters as much as novelty: a false claim loses.

THE QUESTION ({q.title}):
{q.question}
{q.image_block()}
CHAIN RULES.
- No calculation: no equations, arithmetic, code, or multiplying numbers. Rough magnitudes in words by comparison are allowed ("a bathtub a week"); setting two magnitudes against each other in words is allowed.
- No simulation: do not write out the intermediate state of a system step by step (the row after rung 30, the board after move 12). On state-tracking questions your landmarks must be structural — a symmetry, an invariant, a decomposition, a cancellation, a bound — not snapshots.
- At least 10 emoji. Each emoji after the givens carries a parent tag naming one or more EARLIER steps it follows from, written (← 3, 7). An emoji with no parent must state a given (a premise of the problem or a factual premise from general knowledge) and be marked (root).
- Every emoji gets a one-sentence explanation of what it contributes, and every emoji except the last (and 👀 self-checks) must be used by a later step.
- The chain must be self-contained: open with the givens as (root) steps, then one ❓ step (parented to the givens) stating what is asked, and only then the argument. If the question differs from a familiar version, DEPICT the difference in emoji in a step at or before ❓ (for example 🥈 for "second-to-last", 🗓️ for "months", 4️⃣🚪 for "four doors") — a reader shown the emoji alone must be able to tell this question from the famous one.
- Changing the yardstick (another container, vehicle, body, or unit of time) does NOT make a new route; the referee treats "measure both quantities in a common unit and compare" as one route whatever the unit.
- After the chain: 2–4 LANDMARKS (the intermediate claims your route passes through, in plain words). The ANSWER is the last line.
- Conventions: a side branch ending in 👀 is a self-check; a merge into 💥 is a contradiction.

USED-UP LANDMARKS (from accepted chains; your chain must introduce at least one landmark not here):
{q.used_landmarks_text()}

CHAINS ALREADY PLAYED{" (you can see them; sidestep them)" if mode == "duel" else ""}:
{prior_block}
{challenge}
OUTPUT FORMAT (exactly, nothing before or after):
CHAIN by {player}
1. <emoji> (root) — <a given>
2. <emoji> (root) — <a given>
3. ❓ (← 1, 2) — <what is asked>
4. <emoji> (← …) — <explanation>
…
LANDMARKS:
- …
ANSWER: <the answer in the form the question asks for>
"""

def referee_prompt(q, chain_text, chain_ref, notes=None):
    ref = "(open problem: no reference answer; judge soundness and novelty only)" if q.open else q.reference
    notes_block = ("\n=== FORM NOTES FROM THE CODE CHECKER ===\n" + "\n".join(notes) + "\n") if notes else ""
    return f"""You are the REFEREE for the Breadth Atlas. Do not use tools or search. Apply the specification below exactly. Mechanical form (emoji count, parent tags, ❓, landmarks, answer last, numeral arithmetic) has already been checked by code; you judge SOUNDNESS, NOVELTY, and the one form rule code cannot check: NO SIMULATION (section 1) — a chain whose steps or landmarks are step-by-step state snapshots is ILL-FORMED.

=== SPECIFICATION ===
{rules_text()}

=== QUESTION ({q.title}) ===
{q.question}
{q.image_block()}
=== REFERENCE (for you only) ===
{ref}

=== USED LANDMARKS (from ACCEPTED chains only; rejected chains' landmarks are recorded but do not bind) ===
{q.used_landmarks_text()}

=== CHAIN TO JUDGE ({chain_ref}) ===
{chain_text}
{notes_block}
DISCRIMINATOR CHECK (a measurement, not a verdict): the question's discriminator — what distinguishes it from the
familiar version — is: {q.meta.get('discriminator') or (('what makes the attractor "' + q.meta['attractor'] + '" wrong here') if q.meta.get('attractor') and q.meta['attractor'].lower() != 'none' else '(none; answer n/a)')}. Does some step at or before the ❓
step depict it in emoji (not only in the explanation)?

Reply in exactly this format and nothing else:
VERDICT on {chain_ref}: VALID | WRONG | DUPLICATE | ILL-FORMED
REASON: <one or two sentences; name the step for WRONG; name the earlier chain and shared landmarks for DUPLICATE; name the new landmark(s) for VALID>
ROUTE: <5–10 word label>
STRATEGY: <an id from STRATEGIES.md if one fits, otherwise "new: <proposed-name>">
REPEATS: <"attempt NNN" if this chain re-walks the route of an earlier REJECTED chain listed in the used landmarks (same landmarks in substance, whatever this chain's own verdict), otherwise "-">
DISCRIMINATOR: <depicted | not depicted | n/a>
TYPED LANDMARKS:
<one line per landmark of the chain, in order, as:  kind | subject | object | relation | yardstick | text>

Typing rules: kind ∈ size, rate, limit, share, structure, symmetry, state, construction, obstruction, reduction, bound.
relation ∈ ≈, ≫, ≪, =, ∈, bijects, alternates, invariant, forbids, exists, reduces-to. Use "-" for an empty
field. subject and object are the two things the claim relates (the pool, a lifetime of drinking, the
decisive seats); a UNIT or YARDSTICK (tanker load, bathtub, litres per day, body-full) goes ONLY in the
yardstick field, never in subject or object — a claim that sizes one thing in a unit has object "-".
REUSE the exact phrase already used for the same thing in this question's vocabulary below, so identity
can be computed by matching.
Vocabulary already typed on this question:
{q.typed_vocabulary()}
"""

def challenge_prompt(q, target_text, target_ref, step, claim):
    return f"""You are the REFEREE for the Breadth Atlas. A player challenges an accepted chain. Do not use tools or search.

=== SPECIFICATION ===
{rules_text()}

=== QUESTION ({q.title}) ===
{q.question}

=== REFERENCE (for you only) ===
{q.reference}

=== CHALLENGED CHAIN ({target_ref}) ===
{target_text}

=== CHALLENGE ===
Step {step}: {claim}

Rule: the challenge SUCCEEDS only if the named step is actually unsound (false claim, or does not follow from its parents) to a degree that would have made the chain WRONG. Looseness within the chain's own stated range does not count.

Reply in exactly this format:
VERDICT on challenge of {target_ref} step {step}: SUCCEEDS | FAILS
REASON: <one or two sentences>
"""

TYPED_RE = re.compile(r"^\s*([a-z\-]+)\s*\|\s*([^|]*?)\s*\|\s*([^|]*?)\s*\|\s*([^|]*?)\s*\|\s*([^|]*?)\s*\|\s*(.+?)\s*$")

def parse_typed(text):
    block = text.split("TYPED LANDMARKS:", 1)[1] if "TYPED LANDMARKS:" in text else ""
    out = []
    for line in block.splitlines():
        m = TYPED_RE.match(line)
        if m:
            out.append(" | ".join(g.strip() for g in m.groups()))
    return out

def parse_verdict(text):
    v = re.search(r"VERDICT[^:]*:\s*([A-Z\-]+)", text)
    reason = re.search(r"REASON:\s*(.+)", text)
    route = re.search(r"ROUTE:\s*(.+)", text)
    strat = re.search(r"STRATEGY:\s*(.+)", text)
    rep = re.search(r"REPEATS:\s*(.+)", text)
    repeats = rep.group(1).strip() if rep else "-"
    disc = re.search(r"DISCRIMINATOR:\s*(depicted|not depicted|n/a)", text, re.I)
    return {"verdict": v.group(1) if v else "UNPARSED", "reason": reason.group(1).strip() if reason else text[:300],
            "route": route.group(1).strip() if route else "", "strategy": strat.group(1).strip() if strat else "",
            "repeats": "" if repeats in ("-", "") else repeats, "typed": parse_typed(text),
            "discriminator": disc.group(1).lower() if disc else ""}

# ----------------------------------------------------------------------------- recording

def slug(s):
    s = re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")
    return s[:40] or "chain"

def record_chain(q, chain, player_model, player_label, verdict, meta_extra, game_log):
    accepted = verdict["verdict"] == "VALID"
    kind = "routes" if accepted else "attempts"
    cid = q.next_id(kind)
    depth = len(q.routes()) + 1 if accepted else None
    fm = [f"id: {cid}", f"question: {q.id}", f"title: {verdict.get('route') or 'untitled'}",
          f"strategy: {verdict.get('strategy') or 'unclassified'}", f"contributor: {player_model} ({player_label})",
          f"date: {TODAY}"]
    if depth:
        fm.append(f"depth: {depth}")
    fm += [f"referee: {meta_extra['referee']}/{CRITERION}", f"criterion: {CRITERION}", f"verdict: {verdict['verdict']}",
           f"reason: {verdict['reason']}"]
    if verdict.get("repeats"):
        fm.append(f"repeats: {verdict['repeats']}")
    if verdict.get("discriminator") and verdict["discriminator"] != "n/a":
        fm.append(f"discriminator_depicted: {'yes' if verdict['discriminator'] == 'depicted' else 'no'}")
    for i, t in enumerate(verdict.get("typed", []), 1):
        fm.append(f"typed_{i}: {t}")
    name = f"{cid}-{slug(verdict.get('route') or 'chain')}.md"
    (q.dir / kind / name).write_text("---\n" + "\n".join(fm) + "\n---\n\n" + chain.text + "\n", encoding="utf-8")
    ref = f"{kind[:-1]} {cid}"
    q.append_landmarks(chain.landmarks, ref, verdict["verdict"])
    game_log.append(f"\n### {ref} — {player_label} — {verdict['verdict']}\n{verdict['reason']}\n\n{chain.text}\n")
    return ref, name

def record_form_failure(q, raw, errors, player_model, player_label, meta_extra, game_log):
    cid = q.next_id("attempts")
    reason = "; ".join(errors)
    fm = [f"id: {cid}", f"question: {q.id}", "title: (form failure)", "strategy: unclassified",
          f"contributor: {player_model} ({player_label})", f"date: {TODAY}", f"referee: code/{CRITERION}",
          f"criterion: {CRITERION}", "verdict: ILL-FORMED", f"reason: {reason}"]
    (q.dir / "attempts" / f"{cid}-ill-formed.md").write_text("---\n" + "\n".join(fm) + "\n---\n\n" + raw.strip() + "\n", encoding="utf-8")
    chain = Chain(raw)
    if chain.landmarks:
        q.append_landmarks(chain.landmarks, f"attempt {cid}", "ILL-FORMED")
    game_log.append(f"\n### attempt {cid} — {player_label} — ILL-FORMED\n{reason}\n\n{raw.strip()}\n")

# ----------------------------------------------------------------------------- game loops

def play_turn(q, player_label, model, referee_model, prior, mode, allow_challenge, game_log, last_accepted):
    """Returns (outcome, record) where outcome in {'valid','lost','challenge-won','challenge-lost'}."""
    prompt = duelist_prompt(q, player_label, prior, mode, allow_challenge and last_accepted is not None)
    raw = ask(model, prompt, tools=q.tools, allowed=q.allowed)
    if q.image and re.search(r"could(?:n't| not) (?:read|view|open|see) the (?:image|drawing|picture)", raw, re.I):
        game_log.append(f"\n<!-- {player_label} reported it could not read the image; retrying once -->\n{raw.strip()}\n")
        raw = ask(model, prompt, tools=q.tools, allowed=q.allowed)
    game_log.append(f"\n<!-- raw output from {player_label} ({model}) -->\n{raw.strip()}\n")
    raw = save_inline_scorer(q, raw, game_log)
    m = CHALLENGE_RE.search(raw)
    if m and allow_challenge and last_accepted is not None:
        step, claim = int(m.group(2)), m.group(3).strip()
        ref, text = last_accepted
        verdict = parse_verdict(ask(referee_model, challenge_prompt(q, text, ref, step, claim), tools=q.tools, allowed=q.allowed))
        game_log.append(f"\n### CHALLENGE by {player_label} of {ref} step {step}: {claim}\n→ {verdict['verdict']}: {verdict['reason']}\n")
        print(f"  {player_label} challenges {ref} step {step} → {verdict['verdict']}")
        return ("challenge-won" if verdict["verdict"] == "SUCCEEDS" else "challenge-lost"), None
    chain = Chain(raw)
    if not chain.check_form():
        record_form_failure(q, raw, chain.errors, model, player_label, {"referee": referee_model}, game_log)
        print(f"  {player_label}: ILL-FORMED — {'; '.join(chain.errors)[:120]}")
        return "lost", None
    ref_label = f"chain {len(prior) + 1}"
    # Empirical referee (questions with `referee_script:` in their frontmatter): the script gets the
    # whole chain text and prints a verdict line `EMPIRICAL: forced | not forced | unverified | illegal | unparseable — <detail>`.
    # Its result is injected as a note for the model referee, and `not forced`/`illegal` override to WRONG.
    empirical = None
    if q.meta.get("referee_script"):
        script = (ROOT / q.meta["referee_script"]).resolve()
        if script.exists():
            r = subprocess.run([sys.executable, str(script), "--question", q.id], input=chain.text, capture_output=True, text=True, encoding="utf-8", timeout=900)
            empirical = (r.stdout.strip().splitlines() or [""])[-1]
            chain.notes.append(f"EMPIRICAL REFEREE RESULT (final on soundness of the cited line): {empirical}")
            game_log.append(f"\n<!-- empirical referee -->\n{empirical}\n")
    referee_raw = ask(referee_model, referee_prompt(q, chain.text, ref_label, chain.notes), tools=q.tools, allowed=q.allowed)
    # Overrides: code verdicts are final on soundness and on clear duplicates; `ambiguous` and `unverified` are left to the model referee.
    if empirical and re.search(r"EMPIRICAL:\s*(not forced|illegal|weak)", empirical, re.I):
        referee_raw = re.sub(r"VERDICT([^:]*):\s*[\w\-]+", r"VERDICT\1: WRONG", referee_raw, count=1)
        referee_raw += f"\n(verdict overridden to WRONG by the empirical referee: {empirical})"
    elif empirical and re.search(r"EMPIRICAL:\s*duplicate-of", empirical, re.I):
        referee_raw = re.sub(r"VERDICT([^:]*):\s*[\w\-]+", r"VERDICT\1: DUPLICATE", referee_raw, count=1)
        referee_raw += f"\n(verdict overridden to DUPLICATE by the empirical referee: {empirical})"
    game_log.append(f"\n<!-- raw referee output -->\n{referee_raw.strip()}\n")
    verdict = parse_verdict(referee_raw)
    ref, name = record_chain(q, chain, model, player_label, verdict, {"referee": referee_model}, game_log)
    print(f"  {player_label}: {verdict['verdict']} — {verdict['route']}")
    prior.append((ref, verdict["verdict"], chain.text))
    return ("valid" if verdict["verdict"] == "VALID" else "lost"), (ref, chain.text)

def run_duel(q, args, game_log):
    players = [("duelist A", args.duelist), ("duelist B", args.duelist)]
    score = {"duelist A": 0, "duelist B": 0}
    prior = []
    last_accepted = None
    turn = 0
    rnd = 1
    while turn < args.turns:
        label, model = players[turn % 2]
        print(f"round {rnd}, turn {turn + 1}: {label}")
        outcome, rec = play_turn(q, label, model, args.referee, prior, "duel", True, game_log, last_accepted)
        other = players[(turn + 1) % 2][0]
        if outcome == "valid":
            last_accepted = rec
        elif outcome == "lost":
            score[other] += 1
            game_log.append(f"\n**Round {rnd} → {other}.**\n")
            rnd += 1
            last_accepted = None
        elif outcome == "challenge-won":
            score[label] += 1
            game_log.append(f"\n**Round {rnd} → {label} (challenge).**\n")
            rnd += 1
            last_accepted = None
        else:
            score[other] += 1
            game_log.append(f"\n**Round {rnd} → {other} (failed challenge).**\n")
            rnd += 1
            last_accepted = None
        turn += 1
    game_log.append(f"\n**Final: A {score['duelist A']} – B {score['duelist B']}.**\n")
    print(f"final: A {score['duelist A']} – B {score['duelist B']}")

def run_blind(q, args, game_log):
    frozen_prior = []   # blind players see nothing played this game
    for i in range(args.players):
        label = f"blind player {i + 1}"
        print(f"{label}")
        play_turn(q, label, args.duelist, args.referee, list(frozen_prior), "blind", False, game_log, None)

def run_extend(q, args, game_log):
    prior = q.prior_chain_texts()
    for i in range(args.turns):
        print(f"extend attempt {i + 1}")
        outcome, rec = play_turn(q, "extender", args.duelist, args.referee, prior, "extend", False, game_log, None)

# ----------------------------------------------------------------------------- main

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("question")
    ap.add_argument("--mode", default="duel", choices=["duel", "blind", "extend"])
    ap.add_argument("--turns", type=int, default=6)
    ap.add_argument("--players", type=int, default=4)
    ap.add_argument("--duelist", default="sonnet")
    ap.add_argument("--referee", default="opus")
    args = ap.parse_args()

    q = Question(args.question)
    stamp = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    game_log = [f"# Game {stamp} — {q.id} — mode {args.mode}\n\nduelist model: {args.duelist} · referee model: {args.referee} · criterion {CRITERION}\n"]
    print(f"{q.title} — mode {args.mode} — {len(q.routes())} routes, {len(q.attempts())} attempts on file")
    try:
        {"duel": run_duel, "blind": run_blind, "extend": run_extend}[args.mode](q, args, game_log)
    finally:
        (q.dir / "games").mkdir(parents=True, exist_ok=True)
        (q.dir / "games" / f"{stamp}-{args.mode}.md").write_text("\n".join(game_log), encoding="utf-8")
        subprocess.run([sys.executable, str(ROOT / "scripts" / "build_leaderboard.py")], check=False)

if __name__ == "__main__":
    main()
