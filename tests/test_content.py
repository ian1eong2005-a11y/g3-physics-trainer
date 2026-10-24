"""Every template x 20 seeds: well-formed question, four distinct options, key present, hints, a PNG figure or a data table,
and 'Fig. 1' in the stem exactly when there is a figure."""
import random
from collections import Counter

import pytest

from trainer.content import TEMPLATES, inventory
from trainer.content.recall import RECALL
from trainer.content.recall2 import RECALL2
from trainer.content.recall3 import RECALL3

PNG = b"\x89PNG\r\n\x1a\n"
SEEDS = list(range(20))


def test_inventory():
    calc = [t for t in TEMPLATES if t.category == "calc"]
    expl = [t for t in TEMPLATES if t.category == "explain"]
    assert len(calc) >= 70
    levels = Counter(t.level for t in calc)
    assert set(levels) == {1, 2, 3, 4, 5} and min(levels.values()) >= 8
    assert {t.chapter for t in calc} >= {1, 2, 3, 4, 5, 6, 9, 10}
    assert len(expl) == len(RECALL) + len(RECALL2) + len(RECALL3) >= 50
    assert {t.chapter for t in expl} >= set(range(1, 11))
    ids = [t.id for t in TEMPLATES]
    assert len(ids) == len(set(ids)), "duplicate template ids"
    inv = inventory()
    assert ("calc", 5) in inv and ("explain", 8) in inv


MCQ = [t for t in TEMPLATES if t.category != "written"]


@pytest.mark.parametrize("tpl", MCQ, ids=lambda t: t.id)
def test_template_well_formed(tpl):
    for seed in SEEDS:
        q = tpl.make(seed)
        assert q.template_id == tpl.id and q.level == tpl.level and q.chapter == tpl.chapter and q.category == tpl.category
        assert q.stem.strip()
        assert list(q.options) == ["A", "B", "C", "D"], q.options
        texts = list(q.options.values())
        assert len(set(texts)) == 4, f"duplicate options in {tpl.id} seed {seed}: {texts}"
        assert all(t.strip() for t in texts)
        assert q.key in q.options
        assert set(q.misconceptions) <= set("ABCD") - {q.key}
        assert len(q.misconceptions) == 3, f"{tpl.id} seed {seed}: every wrong option needs a misconception message"
        assert len(q.hints) == 3 and all(h.strip() for h in q.hints)
        assert q.working
        if q.figure is not None:
            assert q.figure.startswith(PNG)
            assert "Fig. 1" in q.stem
        else:
            assert "Fig. 1" not in q.stem
        if q.category == "calc":
            assert q.formula
            assert q.figure is not None or "|" in q.stem, f"{tpl.id}: every calculation question needs a diagram or a data table"


def test_numbers_vary_between_seeds():
    for tpl in MCQ:
        if tpl.category != "calc":
            continue
        stems = {tpl.make(s).stem for s in range(30)}
        figs = {tpl.make(s).figure for s in range(6)}
        assert len(stems) > 1 or len(figs) > 1, f"{tpl.id} never varies"


def test_recall_shuffle_keeps_answer_and_misconceptions():
    tpl = next(t for t in TEMPLATES if t.category == "explain")
    q = tpl.make(0)
    rng = random.Random(5)
    for _ in range(10):
        s = q.shuffled(rng)
        assert s.options[s.key] == q.options[q.key]
        assert sorted(s.options.values()) == sorted(q.options.values())
        assert {s.options[k]: v for k, v in s.misconceptions.items()} == {q.options[k]: v for k, v in q.misconceptions.items()}


# ------------------------------------------------------------------ written answers
from trainer.marker import mark  # noqa: E402

WRITTEN = [t for t in TEMPLATES if t.category == "written"]


def test_written_inventory():
    chapters = {t.chapter for t in WRITTEN}
    assert chapters >= {6, 7, 8}
    for ch in chapters:
        assert Counter(t.level for t in WRITTEN if t.chapter == ch) == {1: 5, 2: 5, 3: 5, 4: 5, 5: 5}, f"chapter {ch}"
    assert len(WRITTEN) == 25 * len(chapters)


def test_no_fill_in_the_blank_hints():
    for t in TEMPLATES:
        q = t.make(0)
        for h in q.hints:
            assert "___" not in h, f"{t.id}: cloze hint {h!r}"


@pytest.mark.parametrize("tpl", WRITTEN, ids=lambda t: t.id)
def test_written_marking(tpl):
    q = tpl.make(0)
    assert q.kind == "written" and q.points and q.model_answer and q.formula and len(q.hints) == 3
    if "Fig. 1" in q.stem:
        assert q.figure is not None, f"{tpl.id}: stem mentions Fig. 1 but has no figure"
    if q.figure is not None:
        assert q.figure.startswith(PNG)
    r = mark(q.model_answer, q.points, q.pitfalls, q.min_points)
    assert r.passed, f"{tpl.id}: model answer fails its own marking: missed {r.missed}, pitfalls {r.pitfalls}"
    assert not mark("", q.points, q.pitfalls, q.min_points).passed
    passes, fails = q.samples
    assert passes and fails, f"{tpl.id}: give sample answers"
    for a in passes:
        r = mark(a, q.points, q.pitfalls, q.min_points)
        assert r.passed, f"{tpl.id}: should PASS: {a!r} -> missed {r.missed}, pitfalls {r.pitfalls}"
    for a in fails:
        r = mark(a, q.points, q.pitfalls, q.min_points)
        assert not r.passed, f"{tpl.id}: should FAIL: {a!r} -> hit {r.hit}"
