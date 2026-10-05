"""Seed eight structural questions and unjudged curator chains, without overwrites."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Chains are curator hypotheses, never accepted routes or player inputs.
BATCH = [
    dict(
        id="bridges-on-loops", title="Can a bridge on a loop be indispensable?",
        family="connectivity, failure tolerance", attractor="removing a bridge always breaks a connection",
        question="A finite connected network of islands has undirected bridges. Every bridge lies on at least one loop that returns to its starting island without repeating a bridge or an intermediate island. Exactly one bridge closes. Can the remaining network become disconnected?",
        answer="No. For the closed bridge's endpoints, the rest of its loop supplies an alternative path. Replace any use of the closed bridge in an original path with that alternative. All originally connected islands remain connected. Tolerance: exact yes/no with a general argument, not one example.",
        purpose="Introduces alternate-path substitution and contrasts local edge loss with global reachability.",
        steps=[
            "🗺️ (root) — The finite undirected island network is connected.",
            "🔁 (root) — Every bridge belongs to a loop with no repeated bridge or intermediate island.",
            "🔒 (root) — Exactly one bridge closes.",
            "❓ (← 1, 2, 3) — Can this closure disconnect the network?",
            "🌉 (← 2, 3) — The closed bridge belongs to a loop through its two endpoints.",
            "↪️ (← 3, 5) — The remainder of that loop still joins those endpoints using open bridges.",
            "🚶 (← 1) — Any chosen pair of islands had a connecting path before the closure.",
            "🔀 (← 6, 7) — If that path used the closed bridge, its crossing can be replaced by the open detour.",
            "✅ (← 3, 7) — If the path avoided the closed bridge, it remains available.",
            "🤝 (← 8, 9) — Every pair of islands remains connected after the closure.",
        ],
        landmarks=["The rest of a loop connects the closed bridge's endpoints.", "Any affected path can substitute that detour for the closed crossing."],
        short="No.", strategies="alternate-path substitution; contradiction through a supposed separating edge",
        boundary="Allow one bridge to belong to no loop; two otherwise connected groups joined only by it give a separating closure.",
    ),
    dict(
        id="two-bridges-per-island", title="Does local redundancy guarantee global redundancy?",
        family="connectivity, counterexample", attractor="at least two bridges per island means no single point of failure",
        question="A finite connected undirected network has at least two distinct bridges incident to every island. No bridge joins an island to itself, and there are no parallel bridges. Must the network remain connected after any single bridge closes? Give a concrete counterexample if the answer is no.",
        answer="No. Use two disjoint triangles, joined by one additional bridge between a vertex of each triangle. Each island has at least two incident bridges; the joining vertices have three. Closing the joining bridge separates the triangles. Tolerance: exact no with a counterexample satisfying every condition.",
        purpose="Tests the difference between local degree and a global cut; pairs with bridges-on-loops.",
        steps=[
            "🗺️ (root) — The network is finite, connected, undirected, and has no loops or parallel bridges.",
            "🌉 (root) — Every island has at least two incident bridges.",
            "❓ (← 1, 2) — Must every single-bridge closure preserve connectivity?",
            "🔺 (← 1, 3) — Build a triangle of distinct islands connected around its perimeter.",
            "🔻 (← 1, 3) — Build a second triangle using different islands.",
            "🔗 (← 4, 5) — Join one vertex of the first triangle to one vertex of the second with a single bridge.",
            "✅ (← 4, 5, 6) — This network is connected and satisfies the required bridge count at every island.",
            "✂️ (← 6) — The joining bridge is the only crossing between the two triangles.",
            "🔒 (← 7, 8) — Closing it leaves the triangles disconnected despite every island's initial local redundancy.",
            "🚫 (← 3, 7, 9) — The stated local condition does not guarantee survival of every closure.",
        ],
        landmarks=["Two triangles joined by one bridge satisfy the local degree condition.", "Their sole inter-triangle crossing is nevertheless a separating bridge."],
        short="No; two triangles joined by a single bridge are a counterexample.", strategies="explicit counterexample; local versus global constraint",
        boundary="Strengthen the premise to every bridge lying on a loop; the answer becomes yes, as in bridges-on-loops.",
    ),
    dict(
        id="one-way-central-island", title="All roads lead to the hub, but can anyone leave?",
        family="directed connectivity", attractor="a common reachable hub connects everyone to everyone",
        question="A finite network of islands uses one-way bridges. There is a central island H that every island can reach by following the bridge directions. Does this guarantee that every island can reach every other island? Give a counterexample if not.",
        answer="No. Take islands A, B, H with only the directed bridges A to H and B to H. Both outer islands reach H, and H reaches itself by staying put, but neither outer island can reach the other. Tolerance: exact no with a directed counterexample. A stronger condition that H also reaches every island would guarantee the result by concatenating paths through H.",
        purpose="Adds direction-sensitive composition and distinguishes a common destination from mutual accessibility.",
        steps=[
            "➡️ (root) — Bridges may be traversed only in their marked direction.",
            "🎯 (root) — Every island can reach the central island H.",
            "❓ (← 1, 2) — Does this ensure that every island can reach every other island?",
            "🏝️ (← 1, 3) — Consider distinct islands A, B, and H.",
            "↘️ (← 1, 4) — Give A a bridge to H and B a bridge to H, with no other bridges.",
            "✅ (← 2, 5) — Every island can reach H in this network, with H already at the destination.",
            "🛑 (← 5) — H has no outgoing bridge.",
            "🚶 (← 5, 7) — A traveller leaving A can only reach H and then stop.",
            "🚫 (← 4, 8) — That traveller cannot reach B.",
            "⚠️ (← 3, 6, 9) — A common reachable destination does not establish mutual reachability.",
        ],
        landmarks=["A directed hub can be reachable from every island while having no outgoing bridge.", "Arrival at a common destination supplies no path out to another island."],
        short="No.", strategies="directed counterexample; obstruction by a sink",
        boundary="Also require H to reach every island; a path into H followed by a path out reaches any destination.",
    ),
    dict(
        id="tetrahedron-mirror-information", title="Can distances reveal handedness?",
        family="information, spatial ambiguity", attractor="a complete distance description fixes every property of a shape",
        question="Four labelled vertices form a non-flat tetrahedron. You are given every pairwise distance, but no positions or orientation-sensitive measurements. Relative to a fixed external orientation, can those distances uniquely determine the tetrahedron's handedness?",
        answer="No. Reflect any compatible configuration. All corresponding pairwise distances stay unchanged while the labelled tetrahedron's handedness reverses. Thus the data permit opposite answers. Tolerance: exact no, supported by an observation-preserving transformation. Labels and the fixed external orientation are essential to defining the ask.",
        purpose="Introduces an indistinguishable-pair argument: the evidence is complete for distances but incomplete for orientation.",
        steps=[
            "🔺 (root) — The labelled tetrahedron is non-flat.",
            "📏 (root) — Only its pairwise vertex distances are supplied.",
            "🧭 (root) — Handedness is defined relative to a fixed external orientation.",
            "❓ (← 1, 2, 3) — Can these distances uniquely determine handedness?",
            "🪞 (← 1, 3) — Reflect a configuration to produce one of opposite handedness.",
            "↔️ (← 2, 5) — Reflection preserves every corresponding pairwise distance.",
            "📋 (← 2, 6) — The original and reflected configurations give the same observation record.",
            "🎭 (← 5, 7) — This record is compatible with opposite handednesses.",
            "🔍 (← 7, 8) — Evidence confined to the record cannot select between them.",
            "❔ (← 4, 8, 9) — The supplied data leave handedness unresolved.",
        ],
        landmarks=["Reflection changes handedness while preserving every supplied distance.", "A single observation record admits opposite answers."],
        short="No; a mirror ambiguity remains.", strategies="indistinguishable pair; observation-preserving transformation",
        boundary="Add a measurement that states on which oriented side of the labelled face ABC vertex D lies; this resolves handedness.",
    ),
    dict(
        id="pair-toggle-lamps", title="Can paired switches leave one lamp on?",
        family="invariants, reachability", attractor="enough switch operations can produce any lighting pattern",
        question="A panel has six lamps, all initially off. Each move chooses any two distinct lamps and toggles both: off becomes on and on becomes off. Can any sequence of moves leave exactly one lamp on?",
        answer="No. Pair toggles preserve the parity of the number of lit lamps: two off lamps add a pair, two on lamps remove a pair, and a mixed pair merely transfers the lit state. Initially the lit count is even; a single lit lamp is odd. Tolerance: exact no with a sequence-independent obstruction.",
        purpose="Transfers parity from walks to configuration reachability; no actual switching sequence needs tracing.",
        steps=[
            "💡 (root) — Six lamps are initially off.",
            "🔄 (root) — A move toggles any two distinct lamps.",
            "❓ (← 1, 2) — Can a sequence leave exactly one lamp on?",
            "➕ (← 2) — Toggling two off lamps adds a pair of lit lamps.",
            "➖ (← 2) — Toggling two on lamps removes a pair of lit lamps.",
            "↔️ (← 2) — Toggling a mixed pair moves the lit state without changing how many lamps are on.",
            "⚖️ (← 4, 5, 6) — Every move preserves whether the lit lamps can be paired without a leftover.",
            "🔒 (← 1, 7) — Starting from none, every reachable configuration has an even number of lit lamps.",
            "⚫ (← 3) — Exactly one lit lamp would be an unpaired leftover.",
            "💥 (← 8, 9) — The proposed target violates the preserved parity.",
        ],
        landmarks=["Every allowed toggle preserves lit-count parity.", "The initial configuration and the single-lamp target have different parity."],
        short="No.", strategies="parity invariant; reachability obstruction",
        boundary="Allow a move toggling one lamp; the target becomes reachable immediately.",
    ),
    dict(
        id="cyclic-task-prerequisites", title="Can a cycle of strict prerequisites ever start?",
        family="ordering, dependencies", attractor="choose the right order and all tasks can be completed",
        question="None of tasks A, B, and C has started. A may start only after B has finished; B may start only after C has finished; C may start only after A has finished. Each task requires a positive duration after starting to finish. No prerequisite can be waived. Can any schedule finish all three tasks?",
        answer="No. Any successful schedule would contain a first task to start, but each possible first task requires another task to have already finished, which would require an earlier start. Alternatively, follow the strict precedence requirements around the cycle to demand that a task precede itself. Tolerance: exact no; simultaneous starts do not satisfy prior completion.",
        purpose="Adds earliest-event contradiction and cyclic ordering obstruction, including a check against simultaneous-start escape.",
        steps=[
            "📋 (root) — None of tasks A, B, and C has started.",
            "🔗 (root) — A requires B finished, B requires C finished, and C requires A finished before starting.",
            "⏳ (root) — Each completion requires a positive duration after its task starts, and prerequisites cannot be waived.",
            "❓ (← 1, 2, 3) — Can a schedule finish all three tasks?",
            "🧪 (← 4) — Suppose such a successful schedule exists.",
            "🥇 (← 1, 3, 5) — Among the required starts there must be an earliest starting time.",
            "🔒 (← 2, 6) — Any task starting then requires a different task already finished.",
            "🕰️ (← 3, 7) — That finished task must have started strictly earlier.",
            "💥 (← 6, 8) — This contradicts the earliest starting time, even if some starts are simultaneous.",
            "🚫 (← 5, 9) — No successful schedule exists.",
        ],
        landmarks=["Any successful schedule has an earliest task start.", "Every possible first start requires a strictly earlier start."],
        short="No.", strategies="earliest-event contradiction; strict-order cycle",
        boundary="Remove C's prerequisite; complete C, then B, then A.",
    ),
    dict(
        id="sealed-box-transfers", title="Can transfers empty a sealed collection?",
        family="conservation, witness persistence", attractor="repeatedly emptying individual boxes eventually empties them all",
        question="A sealed collection of boxes contains at least one counter. Each allowed move takes a counter from one box and places it into a different box in the same collection. Counters cannot be destroyed or leave the collection. Can a sequence of moves make every box empty?",
        answer="No. Each transfer preserves the total number of counters, which is initially positive. An all-empty collection has none. An alternative argument follows one initial counter: every move either leaves it in its current box or places it in another box in the collection. Tolerance: exact no; local emptying is insufficient.",
        purpose="A simple conservation anchor with a second candidate spine based on persistence of an individual witness.",
        steps=[
            "📦 (root) — Counters occupy boxes in a sealed collection.",
            "⚫ (root) — At least one counter is initially present.",
            "🔄 (root) — Each allowed move transfers a counter between distinct boxes without destruction or escape.",
            "❓ (← 1, 2, 3) — Can a sequence make every box empty?",
            "➖ (← 3) — A transfer removes a counter from its source box.",
            "➕ (← 3) — That same counter is added to the destination box.",
            "⚖️ (← 5, 6) — Every transfer preserves the collection's total.",
            "🔒 (← 3, 7) — Any sequence of allowed transfers preserves the initial total.",
            "🕳️ (← 4) — Emptying every box would leave no counters in the collection.",
            "💥 (← 2, 8, 9) — That target contradicts the preserved presence of counters.",
        ],
        landmarks=["Every local transfer preserves the global total.", "The all-empty target has a different total from the initial state."],
        short="No.", strategies="conservation; persistence of an initial witness",
        boundary="Allow transfers outside the collection; the conserved system boundary changes and emptying becomes possible.",
    ),
    dict(
        id="mirrored-involutions", title="Do unfamiliar reversible actions cancel in a mirror?",
        family="reversibility, composition", attractor="actions must commute for a sequence to cancel",
        question="A device has actions A, B, and C. Each is always legal, deterministic, and applying the same action twice consecutively restores the state it acted on. They need not commute. Starting from any state, perform A, then B, then C, then C, then B, then A. Must the final state equal the starting state?",
        answer="Yes. The adjacent C actions cancel. The now adjacent B actions cancel, then the A actions cancel. No commutation is used; each pair acts on the same intervening state and restores it. Tolerance: exact yes with a general structural argument, not a simulated device state.",
        purpose="Transfers mirror cancellation beyond a token ladder and isolates self-inverse actions from merely reversible actions.",
        steps=[
            "🎛️ (root) — Actions A, B, and C are always legal and deterministic.",
            "↩️ (root) — Applying any one of these actions twice consecutively restores the state it acted on.",
            "📜 (root) — The sequence is A, B, C, C, B, A, and the actions need not commute.",
            "❓ (← 1, 2, 3) — Must the sequence restore every starting state?",
            "🪞 (← 3) — The action sequence mirrors itself around the adjacent C pair.",
            "✂️ (← 1, 2, 5) — The adjacent C pair can be removed without changing the sequence's effect.",
            "🔗 (← 3, 6) — Removing that pair exposes the B pair as adjacent operations.",
            "✂️ (← 1, 2, 7) — The exposed B pair can also be removed without changing the effect.",
            "✅ (← 2, 3, 8) — Only the A pair remains, and it restores its input state.",
            "🔒 (← 6, 8, 9) — Cancellation from the middle outward restores the starting state without reordering actions.",
        ],
        landmarks=["Adjacent self-inverse actions cancel regardless of the surrounding state.", "The mirrored sequence exposes cancelling pairs from the centre outward without commutation."],
        short="Yes.", strategies="mirror cancellation; nested restoration",
        boundary="Make C reversible but not self-inverse; the repeated C pair need not cancel. A and B as identity actions and C as a quarter-turn give a counterexample.",
    ),
]


def seed():
    targets = [ROOT / "questions" / q["id"] for q in BATCH]
    existing = [str(p) for p in targets if p.exists()]
    if existing:
        raise SystemExit("Refusing to overwrite existing question folders: " + ", ".join(existing))
    for q, target in zip(BATCH, targets):
        target.mkdir(parents=True)
        for name in ("routes", "attempts", "games"):
            (target / name).mkdir()
        question = f"""---
id: {q['id']}
title: {q['title']}
status: answered
added: 2026-10-05
family: {q['family']}
attractor: {q['attractor']}
---

# Question

{q['question']}

# Reference answer (referee only)

{q['answer']}

# Why it is in the atlas

{q['purpose']}

# Breadth

No played or accepted routes yet. The unjudged draft in curator.md is not part of the frontier.
"""
        (target / "question.md").write_text(question, encoding="utf-8")
        (target / "landmarks.md").write_text(
            f"# Frontier — landmarks used so far ({q['id']})\n\n"
            "No played chains yet. Only VALID chains bind the frontier.\n\n"
            "| # | landmark | chain | verdict |\n|---|---|---|---|\n", encoding="utf-8")
        chain = "\n".join(f"{i}. {step}" for i, step in enumerate(q["steps"], 1))
        landmarks = "\n".join("- " + claim for claim in q["landmarks"])
        (target / "curator.md").write_text(
            "# Curator notes — unjudged candidate\n\n"
            "This file contains solution hypotheses. It is not a played route, is not scored, "
            "and must not be supplied as player input.\n\n"
            f"## Candidate chain\n\n{chain}\nLANDMARKS:\n{landmarks}\nANSWER: {q['short']}\n\n"
            f"## Other conceptual spines to investigate\n\n{q['strategies']}\n\n"
            f"## Boundary variant\n\n{q['boundary']}\n", encoding="utf-8")
    print(f"Added {len(BATCH)} questions with reference answers, empty frontiers, and unjudged curator chains.")


if __name__ == "__main__":
    seed()
