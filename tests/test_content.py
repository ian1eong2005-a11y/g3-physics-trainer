"""Every template x 20 seeds: well-formed question, four distinct options, key present, hints, PNG figure iff 'Fig. 1' in stem."""
import random
from collections import Counter

import pytest

from trainer.content import TEMPLATES
from trainer.content.recall import RECALL

PNG = b"\x89PNG\r\n\x1a\n"
SEEDS = list(range(20))


def test_inventory():
    calc = [t for t in TEMPLATES if t.category == "calc"]
    expl = [t for t in TEMPLATES if t.category == "explain"]
    assert len(calc) == 40
    assert Counter(t.level for t in calc) == {1: 8, 2: 8, 3: 8, 4: 8, 5: 8}
    assert {t.chapter for t in calc} == {1, 2, 3, 4}
    assert len(expl) == len(RECALL) >= 20
    assert {t.level for t in expl} == {1, 2}
    ids = [t.id for t in TEMPLATES]
    assert len(ids) == len(set(ids)), "duplicate template ids"


@pytest.mark.parametrize("tpl", TEMPLATES, ids=lambda t: t.id)
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


def test_numbers_vary_between_seeds():
    for tpl in TEMPLATES:
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
