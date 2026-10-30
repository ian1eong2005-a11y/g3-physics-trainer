"""The 'O level 2026 MCQ practice' category: adapted SEAB MCQs on the learning outcomes the 2026 O-Level Paper 2 (Q1-7) did not test."""
from collections import Counter

from trainer.config import CATEGORIES, OLEVEL_LEVEL_NAMES
from trainer.content import TEMPLATES

OLEVEL = [t for t in TEMPLATES if t.category == "olevel"]

# Learning outcomes tested in 2026 5086/02 Q1-7 (pages 1-10 of the scan). 14c appeared only as the kW h unit in Q1,
# so electricity-cost calculations are kept on purpose.
TESTED_2026_P2 = {"1b", "1e", "3a", "3i", "4a", "4b", "5b", "5c", "5d", "5e", "9a", "9c", "9d", "12c", "12d", "12g", "12i", "12j",
                  "13a", "13b", "13c", "13d", "13f", "13g", "14b", "14e", "14f", "15b", "15d", "15f"}


def test_category_registered():
    assert CATEGORIES["olevel"] == "O level 2026 MCQ practice"
    assert set(OLEVEL_LEVEL_NAMES) == {1, 2, 3, 4, 5}


def test_inventory():
    assert len(OLEVEL) >= 95
    chapters = {t.chapter for t in OLEVEL}
    assert chapters >= set(range(1, 17)) - {5}, "Ch 5 is the only chapter with no untested outcome"
    assert set(Counter(t.level for t in OLEVEL)) == {1, 2, 3, 4, 5}


def test_only_untested_outcomes():
    for t in OLEVEL:
        assert t.lo not in TESTED_2026_P2, f"{t.id}: LO {t.lo} was already tested in the 2026 Paper 2"


def test_every_item_cites_its_source():
    for t in OLEVEL:
        q = t.make(0)
        assert any("Adapted from SEAB" in w for w in q.working), f"{t.id}: say which SEAB question it was adapted from"
