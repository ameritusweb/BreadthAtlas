import math
import re

_STOP = set("""
a an the and or but if then else for to of in on at by with from as is are was were be been
being this that these those it its i you he she we they my your our their me him her them do
does did have has had not no yes can could should would will just so how what why when where
which who whom there here any some all one using use get set way want need like also into out
about than more most very only same other such each make does doing done""".split())

_TAG = re.compile(r"<[^>]+>")
_WORD = re.compile(r"[A-Za-z_][A-Za-z0-9_\.]*")


def _strip(text):
    return _TAG.sub(" ", text or "")


def _has_code(raw):
    if "<pre" in raw or "```" in raw or "<code" in raw:
        return True
    return any(line.startswith("    ") and line.strip() for line in raw.splitlines())


def _has_list(raw):
    if "<li" in raw:
        return True
    return bool(re.search(r"(?m)^\s*(?:[-*]|\d+\.)\s+\S", raw))


def _content_tokens(text):
    return {w.lower() for w in _WORD.findall(text) if len(w) > 3 and w.lower() not in _STOP}


def score(question: str, answer: str) -> float:
    raw = answer or ""
    plain = _strip(raw)
    words = _WORD.findall(plain)

    effort = math.log1p(len(words))
    code = 0.5 if _has_code(raw) else 0.0
    links = 0.15 * min(raw.count("http"), 3)
    listed = 0.2 if _has_list(raw) else 0.0

    q_terms = _content_tokens(_strip(question))
    a_terms = _content_tokens(plain)
    overlap = len(q_terms & a_terms) / len(q_terms) if q_terms else 0.0

    return effort + code + links + listed + overlap
