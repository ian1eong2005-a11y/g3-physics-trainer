"""Constants for the G3 Science (Physics) adaptive trainer. Change class lists and rules here only."""

APP_TITLE = "G3 Physics Trainer"
SCHOOL = "Queenstown Secondary School"

# Login dropdown, grouped by level. Add Sec 4 classes here when known.
CLASSES = {
    "Sec 3": ["3SG2", "3SG3", "3SG4", "3SG8"],
    "Sec 4": ["4SG4"],
}
CLASS_LIST = [c for group in CLASSES.values() for c in group]

CHAPTERS = {
    1: "Measurement",
    2: "Kinematics",
    3: "Force and Pressure",
    4: "Dynamics",
    5: "Turning Effects of Forces",
    6: "Energy",
    7: "Kinetic Particle Model of Matter",
    8: "Thermal Processes",
    9: "General Wave Properties",
    10: "Electromagnetic Spectrum",
}

CATEGORIES = {
    "calc": "Calculation",
    "explain": "Explanation",
    "written": "Written answer",
}

WRITTEN_LEVEL_NAMES = {
    1: "L1 - state or define in a phrase",
    2: "L2 - state two facts or describe simply",
    3: "L3 - explain with a reason",
    4: "L4 - explain with a chain of reasoning",
    5: "L5 - apply or evaluate in a new situation",
}

LEVEL_NAMES = {
    1: "L1 - one formula, direct substitution",
    2: "L2 - one formula with a conversion, reading or rearrangement",
    3: "L3 - two steps, usually with a figure",
    4: "L4 - graphs and linked formulas",
    5: "L5 - multi-step with a trap",
}
EXPLAIN_LEVEL_NAMES = {
    1: "L1 - recall and definitions",
    2: "L2 - identify and classify",
    3: "L3 - apply a concept",
    4: "L4 - explain with reasoning",
    5: "L5 - evaluate",
}

# Adaptive rules (confirmed by the teacher, 24 Oct 2026)
UP_STREAK = 5          # correct in a row at a level -> level + 1
DOWN_STREAK = 3        # wrong in a row at a level -> level - 1
MIN_LEVEL, MAX_LEVEL = 1, 5
START_LEVEL = 1
RECENT_AVOID = 10      # do not repeat any of the last N template ids

ONLINE_SECONDS = 120   # "online" on the dashboard if active within this many seconds
DASHBOARD_REFRESH_S = 5

DEFAULT_TEACHER_PASSWORD = "physics"   # used only when no TEACHER_PASSWORD secret / env var is set

G = 10.0               # N/kg, as used in school papers
