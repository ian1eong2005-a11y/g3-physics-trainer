"""The 'O level 2026 MCQ practice' category: every 5086 learning outcome, every in-syllabus SEAB Ten-Year-Series MCQ, and a
'NOT in P2 2026' note worked out from each question's learning outcome (rebuilt 31 Oct 2026)."""
import re
from collections import Counter

from trainer.config import CATEGORIES, OLEVEL_LEVEL_NAMES, P2_2026_NOT_TESTED, P2_2026_Q10_ONLY, P2_2026_Q11_ONLY, p2_2026_note
from trainer.content import TEMPLATES

OLEVEL = [t for t in TEMPLATES if t.category == "olevel"]

ALL_LOS = ("1a 1b 1c 1d 1e 1f 2a 2b 2c 2d 2e 2f 2g 2h 2i 3a 3b 3c 3d 3e 3f 3g 3h 3i 4a 4b 4c 4d 5a 5b 5c 5d 5e 6a 6b 6c 6d 6e "
           "7a 7b 7c 7d 7e 8a 8b 8c 8d 8e 9a 9b 9c 9d 9e 9f 9g 9h 9i 10a 10b 10c 10d 11a 11b 11c 11d 11e 11f 11g 11h 12a 12b 12c 12d "
           "12e 12f 12g 12h 12i 12j 13a 13b 13c 13d 13e 13f 13g 14a 14b 14c 14d 14e 14f 14g 14h 14i 15a 15b 15c 15d 15e 15f 15g 15h "
           "15i 16a 16b 16c 16d 16e 16f 16g 16h").split()

# "LOs not tested" sheet of Output documents/2026 O-Level 5086 P2 Table of Specifications.xlsx
TOS_NOT_TESTED = set("1a 1c 1d 1f 2a 2d 2e 2f 2g 2h 2i 3b 3c 3d 3e 3f 3g 3h 4d 5a 5c 6d 6e 7a 7d 8a 9b 9g 9h 9i 11a 11b 11f 11g "
                     "11h 12a 12b 12e 12f 12h 13e 14a 14d 14g 14h 14i 15a 15c 15e 15g 15h 15i 16f 16h".split())
TOS_Q10_ONLY = set("6c 7b 7c 7e 8b 8c 8d 8e".split())
TOS_Q11_ONLY = set("9e 9f 10a 10b 10c 10d 11c 11d 11e".split())

# Every SEAB physics MCQ in the bank: 5076 Paper 1 2014-2021 (the 2020 scan numbers its 20th physics MCQ 37) and the 5086 specimen P1.
TYS = {str(y): list(range(1, 21)) for y in range(2014, 2022)}
TYS["2020"] = list(range(1, 20)) + [37]
TYS["specimen"] = list(range(1, 21))
OUT_OF_SCOPE = {   # 5076 content that 5086 dropped
    ("2014", 8): "evaporation", ("2016", 10): "evaporation", ("2019", 9): "evaporation", ("2021", 9): "evaporation",
    ("2017", 16): "electric field lines", ("2020", 16): "electric field lines", ("2021", 15): "electric field lines",
    ("2018", 12): "critical angle / total internal reflection", ("2018", 2): "adding vectors (resultant of two forces)",
    ("2014", 19): "demagnetising with a.c.", ("2018", 20): "demagnetising with a.c.",
}


def cited_tys():
    """(year or 'specimen', number) of every SEAB question named in an O-level item's working."""
    out = set()
    for t in OLEVEL:
        text = " ".join(t.make(0).working)
        for m in re.finditer(r"SEAB (?:O-Level (\d{4})|5086 specimen paper 2024|specimen 2024) MCQ (\d+)((?: and (?:\d{4} )?MCQ \d+)*)", text):
            year = m.group(1) or "specimen"
            out.add((year, int(m.group(2))))
            for mm in re.finditer(r"and (?:(\d{4}) )?MCQ (\d+)", m.group(3)):
                out.add((mm.group(1) or year, int(mm.group(2))))
    return out


def test_category_registered():
    assert CATEGORIES["olevel"] == "O level 2026 MCQ practice"
    assert set(OLEVEL_LEVEL_NAMES) == {1, 2, 3, 4, 5}


def test_inventory():
    assert len(OLEVEL) >= 190
    assert {t.chapter for t in OLEVEL} == set(range(1, 17))
    assert set(Counter(t.level for t in OLEVEL)) == {1, 2, 3, 4, 5}


def test_every_learning_outcome_has_a_question():
    have = {t.lo for t in OLEVEL}
    assert not set(ALL_LOS) - have, f"no O-level question for {sorted(set(ALL_LOS) - have)}"
    assert have <= set(ALL_LOS), f"unknown LO tags {sorted(have - set(ALL_LOS))}"


def test_every_in_scope_tys_question_is_in():
    cited = cited_tys()
    missing = [(y, q) for y, qs in TYS.items() for q in qs if (y, q) not in OUT_OF_SCOPE and (y, q) not in cited]
    assert not missing, f"SEAB TYS MCQs in the 5086 syllabus with no O-level item: {missing}"
    assert not (cited & set(OUT_OF_SCOPE)), "an out-of-scope TYS question is used"


def test_notes_match_the_2026_p2_tos():
    assert P2_2026_NOT_TESTED == TOS_NOT_TESTED and len(TOS_NOT_TESTED) == 54
    assert P2_2026_Q10_ONLY == TOS_Q10_ONLY and P2_2026_Q11_ONLY == TOS_Q11_ONLY
    assert not (TOS_NOT_TESTED & TOS_Q10_ONLY) and not (TOS_NOT_TESTED & TOS_Q11_ONLY)
    for lo in ALL_LOS:
        note = p2_2026_note(lo)
        if lo in TOS_NOT_TESTED:
            assert note == "NOT in P2 2026"
        elif lo in TOS_Q10_ONLY | TOS_Q11_ONLY:
            assert note.startswith("NOT in P2 2026 Section A (only in either/or Q1")
        else:
            assert note is None, f"{lo} was tested in Paper 2, so it carries no note"


def test_every_item_cites_its_source():
    for t in OLEVEL:
        q = t.make(0)
        assert any("Adapted from" in w for w in q.working), f"{t.id}: say which past-paper question it was adapted from"
