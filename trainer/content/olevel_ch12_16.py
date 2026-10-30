"""O level 2026 MCQ practice, Ch 12-16: adapted SEAB O-Level MCQs on learning outcomes the 2026 Paper 2 (Q1-7) did not test
(charge and Q = It, parallel circuits, cost of electricity, earthing and fuses, magnets and forces on currents, half-life).
Magnetic force directions come from F = I x B (sketches3.force_on_wire), never from a hand-written key."""
from .. import sketches2 as sk, sketches3 as k3
from .base import calc_q, explain_mcqs, fmt, md_table, nice, numeric_options, template, text_options

CAT = "olevel"


def src(text):
    return f"_Adapted from {text}._"


def money(rng, answer, wrongs):
    """Numeric options shown as dollars ($4.20)."""
    opts, key, mis = numeric_options(rng, answer, wrongs, dp=2)
    return {k: "$" + v for k, v in opts.items()}, key, mis


# ================================================================== Ch 12 Charge and current
explain_mcqs([
    dict(id="o26_charge_signs", chapter=12, level=3, lo="12b", source="SEAB O-Level 2015 MCQ 15 and 2018 MCQ 14",
         stem="A positively charged rod attracts a small ball X. Ball X then repels another small ball Y.\n\n"
              + md_table(["", "observation"], [["rod (+) and X", "attract"], ["X and Y", "repel"]]) + "\n\nWhat are the charges on X and Y?",
         correct="X negative, Y negative",
         wrongs={"X positive, Y positive": "X is attracted to a POSITIVE rod, so X cannot be positive.",
                 "X negative, Y positive": "X repels Y, so they carry the SAME sign of charge.",
                 "X uncharged, Y negative": "Repulsion only happens between two charged objects, so X must be charged."},
         hints=["Unlike charges attract; like charges repel.", "Repulsion is the sure test: both objects must be charged with the same sign.",
                "Work out X first from the rod."]),
], category=CAT)


@template("o26_battery_charge", chapter=12, level=2, lo="12e", category=CAT)
def battery_charge(rng):
    I = nice(rng, 2.0, 2.5, 4.0)
    h = nice(rng, 2, 3, 4)
    Q = I * h * 3600
    return calc_q(rng, f"A battery for a cordless drill is fully charged by a current of **{fmt(I)} A** for **{h} hours**. How much charge does it store?\n\n"
                  + md_table(["current / A", "time / h"], [[fmt(I), h]]),
                  Q, [(I * h, "Change hours to seconds: Q = I t with t in s."), (I * h * 60, "One hour is 3600 s, not 60 s."), (I / (h * 3600), "Q = I × t, not I ÷ t.")],
                  "C", "Q = I t", [f"t = {h} × 3600 = {h * 3600} s", f"Q = {fmt(I)} × {h * 3600} = **{fmt(Q)} C**", src("SEAB O-Level 2017 MCQ 17")],
                  ["Charge = current × time.", "Time must be in seconds.", "1 hour = 3600 s."])


@template("o26_battery_lasts", chapter=12, level=3, lo="12e", category=CAT)
def battery_lasts(rng):
    I1 = nice(rng, 600, 900, 1200)
    t1 = nice(rng, 1, 2)
    I2 = nice(rng, 1.5, 2.0, 3.0)
    t2 = I1 / 1000 * t1 / I2
    return calc_q(rng, f"A fully charged battery can supply **{I1} mA** for **{t1} hour{'s' if t1 > 1 else ''}**. For how long can it supply a current of **{fmt(I2)} A**?\n\n"
                  + md_table(["current", "time"], [[f"{I1} mA", f"{t1} h"], [f"{fmt(I2)} A", "?"]]),
                  t2, [(I1 * t1 / I2, "Change mA to A first."), (I2 * t1 / (I1 / 1000), "The bigger current empties the battery FASTER, so the time is shorter."),
                       (t1 * I2, "The charge stored is fixed: I₁ t₁ = I₂ t₂.")], "hours", "charge stored Q = I t is fixed",
                  [f"charge = {fmt(I1 / 1000)} A × {t1} h", f"time = {fmt(I1 / 1000 * t1)} ÷ {fmt(I2)} = **{fmt(t2)} h**", src("SEAB O-Level 2020 MCQ 17")],
                  ["The battery stores a fixed amount of charge.", "Q = I t, so I₁ t₁ = I₂ t₂.", "Use the same units for both currents."], sf=2)


@template("o26_heater_charge", chapter=12, level=1, lo="12e", category=CAT)
def heater_charge(rng):
    I = nice(rng, 5, 8, 12)
    m = nice(rng, 4, 5, 10)
    Q = I * m * 60
    return calc_q(rng, f"The current in an electric heater is **{I} A**. It is switched on for **{m} minutes**. How much charge flows through it?\n\n"
                  + md_table(["current / A", "time / min"], [[I, m]]),
                  Q, [(I * m, "Change minutes into seconds."), (I / m, "Q = I × t."), (I * m / 60, "Multiply minutes by 60 to get seconds; do not divide.")],
                  "C", "Q = I t", [f"t = {m} × 60 = {m * 60} s", f"Q = {I} × {m * 60} = **{Q} C**", src("SEAB specimen 2024 MCQ 13")],
                  ["Q = I t.", "t in seconds.", f"{m} min = {m * 60} s."])


# ================================================================== Ch 13 D.C. circuits
explain_mcqs([
    dict(id="o26_lamp_fails", chapter=13, level=4, lo="13e", source="SEAB O-Level 2014 MCQ 17",
         stem="Fig. 1 shows four identical lamps. Lamp P is in the main circuit; lamp Q is in one branch; lamps R and S are in series in the other branch. "
              "One lamp breaks. The other three stay lit. Which lamp broke?",
         correct="Q", wrongs={"P": "P is in the main circuit: if it breaks, ALL the lamps go out.",
                              "R": "R is in series with S: if R breaks, S goes out too.", "S": "S is in series with R: if S breaks, R goes out too."},
         hints=["A break in series stops the current through everything in that loop.", "Which lamp is alone in its own branch?",
                "Breaking that one leaves a complete path through the others."],
         figure=lambda: sk.circuit(series=[("lamp", "P")], parallel=[[("lamp", "Q")], [("lamp", "R"), ("lamp", "S")]])),
    dict(id="o26_short_circuit", chapter=13, level=4, lo="13e", source="SEAB O-Level 2018 MCQ 17",
         stem="Fig. 1 shows three identical lamps P, Q and R and a cell. A thick copper wire (the bottom branch) has just been connected across lamps Q and R. What happens?",
         correct="Q and R go out and P becomes brighter.",
         wrongs={"Q and R go out and P does not change.": "With Q and R short-circuited the total resistance falls, so the current through P rises.",
                 "R goes out and P and Q become brighter.": "The wire is across BOTH Q and R: the current bypasses both.",
                 "Nothing changes.": "The copper wire has almost no resistance, so almost all the current goes through it."},
         hints=["Current takes the path of least resistance.", "The copper wire is in parallel with Q and R.", "What happens to the total resistance and the current through P?"],
         figure=lambda: sk.circuit(series=[("lamp", "P")], parallel=[[("lamp", "Q")], [("lamp", "R")], [("wire", "")]])),
], category=CAT)


@template("o26_parallel_ammeter", chapter=13, level=2, lo="13e", category=CAT)
def parallel_ammeter(rng):
    E = nice(rng, 6, 9, 12)
    R1, R2 = nice(rng, (6, 3), (4, 12), (3, 6), (2, 6))
    I = E / R1 + E / R2
    return calc_q(rng, f"A **{E} V** battery is connected across a {R1} Ω resistor and a {R2} Ω resistor in parallel (Fig. 1). What is the reading on the ammeter?",
                  I, [(E / (R1 + R2), "The resistors are in PARALLEL, not series."), (E / R1, f"That is only the current in the {R1} Ω branch."),
                      (E / R2, f"That is only the current in the {R2} Ω branch.")], "A", "each branch has the full p.d.; I = sum of branch currents",
                  [f"I₁ = {E} ÷ {R1} = {fmt(E / R1)} A", f"I₂ = {E} ÷ {R2} = {fmt(E / R2)} A", f"ammeter = **{fmt(I)} A**", src("SEAB O-Level 2015 MCQ 18")],
                  ["Each parallel branch has the full battery p.d.", "Find the current in each branch with I = V ÷ R.", "The ammeter in the main wire reads the sum."],
                  figure=sk.circuit(parallel=[[("R", f"{R1} Ω")], [("R", f"{R2} Ω")]], emf=f"{E} V", ammeter="main"))


@template("o26_branch_currents", chapter=13, level=4, lo="13e", category=CAT)
def branch_currents(rng):
    R3 = nice(rng, 2.0, 3.0, 4.0)
    I3 = nice(rng, 2.0, 3.0)
    Ra, Rb = nice(rng, (2.0, 4.0), (1.0, 5.0), (3.0, 3.0))
    V = I3 * R3
    I2 = V / (Ra + Rb)
    It = I3 + I2
    correct = f"V = {fmt(V)} V, I = {fmt(It)} A"
    wrongs = {f"V = {fmt(V)} V, I = {fmt(I3)} A": "The battery current is the SUM of both branch currents.",
              f"V = {fmt(2 * V)} V, I = {fmt(It)} A": f"The p.d. across each branch equals the battery e.m.f.: V = {fmt(I3)} × {fmt(R3)}.",
              f"V = {fmt(2 * V)} V, I = {fmt(I3 + 2 * I2)} A": "Both the p.d. and the current are doubled by mistake."}
    opts, key, mis = text_options(rng, correct, wrongs)
    return dict(stem=f"A battery of e.m.f. V is connected to the circuit in Fig. 1. The ammeter reads **{fmt(I3)} A**. What are V and the current I from the battery?",
                figure=sk.circuit(parallel=[[("A", f"{fmt(I3)} A"), ("R", f"{fmt(R3)} Ω")], [("R", f"{fmt(Ra)} Ω"), ("R", f"{fmt(Rb)} Ω")]], emf="V"),
                options=opts, key=key, misconceptions=mis, formula="V = I R; parallel branches have the same p.d.",
                working=[f"p.d. across the top branch = {fmt(I3)} × {fmt(R3)} = {fmt(V)} V = e.m.f.", f"bottom branch: I = {fmt(V)} ÷ ({fmt(Ra)} + {fmt(Rb)}) = {fmt(I2)} A",
                         f"I = {fmt(I3)} + {fmt(I2)} = **{fmt(It)} A**", src("SEAB O-Level 2017 MCQ 18")],
                hints=["Use the ammeter branch to find the p.d.", "Both branches have this same p.d.", "Add the two branch currents."])


@template("o26_three_ammeters", chapter=13, level=4, lo="13e", category=CAT)
def three_ammeters(rng):
    k = nice(rng, 1, 2, 3)
    a1, a2, a3 = 3 * k, 2 * k, k
    correct = f"A₁ = {a1} A, A₂ = {a2} A, A₃ = {a3} A"
    wrongs = {f"A₁ = {a1} A, A₂ = {a3} A, A₃ = {a2} A": "The branch with TWO resistors has more resistance, so it carries LESS current.",
              f"A₁ = {2 * k} A, A₂ = {k} A, A₃ = {k} A": "The branches have different resistances, so the currents are not equal.",
              f"A₁ = {4 * k} A, A₂ = {2 * k} A, A₃ = {k} A": "A₁ must equal the sum of A₂ and A₃."}
    opts, key, mis = text_options(rng, correct, wrongs)
    return dict(stem="Fig. 1 shows a battery, three identical resistors and three ammeters. Which row gives possible ammeter readings?",
                figure=sk.circuit(series=[("A", "A₁")], parallel=[[("A", "A₂"), ("R", "")], [("A", "A₃"), ("R", ""), ("R", "")]]),
                options=opts, key=key, misconceptions=mis, formula="branch currents add up; same p.d. across each branch",
                working=["Branch 2 has twice the resistance of branch 1, so half the current: A₂ = 2 × A₃.", f"A₁ = A₂ + A₃ → **{correct}**", src("SEAB O-Level 2020 MCQ 19")],
                hints=["Both branches have the same p.d.", "More resistance → less current.", "Main current = sum of branch currents."])


# ================================================================== Ch 14 Practical electricity
@template("o26_lamp_hours", chapter=14, level=3, lo="14c", category=CAT)
def lamp_hours(rng):
    c = nice(rng, 0.20, 0.25, 0.30)
    P = nice(rng, 40, 50, 60, 100)
    h = nice(rng, 20, 40, 50)
    C = c * P / 1000 * h
    return calc_q(rng, f"Electrical energy costs **${fmt(c, dp=2)} per kW h**. A **{P} W** lamp (Fig. 1) is used until the cost is **${fmt(C, dp=2)}**. For how long is it used?\n\n"
                  + md_table(["cost per kW h", "power", "total cost"], [[f"${fmt(c, dp=2)}", f"{P} W", f"${fmt(C, dp=2)}"]]),
                  h, [(C / (c * P), "Change the power to kW first."), (C / c, "That is the energy in kW h; divide by the power in kW."),
                      (C / c * P, "Time = energy ÷ power, not energy × power.")], "hours", "energy (kW h) = power (kW) × time (h)",
                  [f"energy = {fmt(C, dp=2)} ÷ {fmt(c, dp=2)} = {fmt(C / c)} kW h", f"time = {fmt(C / c)} ÷ {fmt(P / 1000)} = **{fmt(h)} h**", src("SEAB O-Level 2016 MCQ 18")],
                  ["Find the energy bought from the cost.", "Energy in kW h = power in kW × time in h.", f"{P} W = {fmt(P / 1000)} kW."],
                  figure=sk.rating_plate([f"{P} W", "230 V"], title="lamp"))


@template("o26_bulb_saving", chapter=14, level=4, lo="14c", category=CAT)
def bulb_saving(rng):
    n = nice(rng, 4, 5, 8)
    P1 = nice(rng, 60, 100)
    P2 = nice(rng, 12, 15)
    h = nice(rng, 4, 5, 6)
    c = nice(rng, 0.25, 0.30)
    save = n * (P1 - P2) / 1000 * h * 7 * c
    opts, key, mis = money(rng, save, [(save / 7, "That is the saving for ONE day; the question asks for a week."),
                                       (n * P1 / 1000 * h * 7 * c, "That is the cost of the old bulbs; the saving uses the DIFFERENCE in power."),
                                       (n * (P1 - P2) / 1000 * h * c * 30, "A week is 7 days, not 30.")])
    return dict(stem=f"A family replaces **{n}** lamps of **{P1} W** with {n} LED lamps of **{P2} W**. The lamps are on for **{h} hours** a day. Electricity costs **${fmt(c, dp=2)} per kW h**. "
                     "How much money is saved each week?\n\n" + md_table(["", "power / W", "number"], [["old lamp", P1, n], ["LED lamp", P2, n]]),
                options=opts, key=key, misconceptions=mis, formula="energy (kW h) = power (kW) × time (h); cost = energy × price",
                working=[f"power saved = {n} × ({P1} − {P2}) = {n * (P1 - P2)} W = {fmt(n * (P1 - P2) / 1000)} kW",
                         f"energy saved per week = {fmt(n * (P1 - P2) / 1000)} × {h} × 7 = {fmt(n * (P1 - P2) / 1000 * h * 7)} kW h",
                         f"saving = × ${fmt(c, dp=2)} = **${fmt(save, dp=2)}**", src("SEAB O-Level 2019 MCQ 18")],
                hints=["Find the power saved by all the lamps.", "Energy saved in kW h = kW × hours in a week.", "Multiply by the price."])


@template("o26_microwave_year", chapter=14, level=5, lo="14c", category=CAT)
def microwave_year(rng):
    I = nice(rng, 4.0, 5.0)
    V = 230
    m = nice(rng, 2, 3, 5)
    c = nice(rng, 0.25, 0.30)
    kW = I * V / 1000
    hours = m / 60 * 365
    cost = kW * hours * c
    opts, key, mis = money(rng, cost, [(cost * 60, "Change the minutes into hours (÷ 60)."), (cost / 365, "That is the cost for ONE day."),
                                       (I * V * hours * c, "Change W to kW (÷ 1000) before multiplying by the price.")])
    return dict(stem=f"A microwave oven (Fig. 1) takes **{fmt(I)} A** from the **230 V** mains. It is used for **{m} minutes** every day. Electricity costs **${fmt(c, dp=2)} per kW h**. "
                     "What is the cost of using it for a year (365 days)?",
                figure=sk.rating_plate(["230 V", f"{fmt(I)} A"], title="microwave oven"),
                options=opts, key=key, misconceptions=mis, formula="P = V I; energy (kW h) = kW × h; cost = energy × price",
                working=[f"P = 230 × {fmt(I)} = {fmt(I * V)} W = {fmt(kW)} kW", f"time = {m} min × 365 = {fmt(hours)} h",
                         f"energy = {fmt(kW)} × {fmt(hours)} = {fmt(kW * hours)} kW h", f"cost = × ${fmt(c, dp=2)} = **${fmt(cost, dp=2)}**", src("SEAB O-Level 2021 MCQ 19")],
                hints=["Find the power in kW with P = V I.", "Find the total time in hours for the year.", "Energy in kW h × price."])


@template("o26_heater_cost", chapter=14, level=1, lo="14c", category=CAT)
def heater_cost(rng):
    P = nice(rng, 1.5, 2.0, 2.5)
    h = nice(rng, 4, 6)
    c = nice(rng, 25, 30)
    cost = P * h * c
    return calc_q(rng, f"An electric heater is rated **{fmt(P)} kW**. Electricity costs **{c} cents per kW h**. What is the cost of using the heater for **{h} hours**?\n\n"
                  + md_table(["power / kW", "time / h", "price / cents per kW h"], [[fmt(P), h, c]]),
                  cost, [(P * c, "You left out the time."), (P * h, "That is the energy in kW h; multiply by the price."), (P * 1000 * h * c, "The power is already in kW.")],
                  "cents", "cost = power (kW) × time (h) × price", [f"energy = {fmt(P)} × {h} = {fmt(P * h)} kW h", f"cost = {fmt(P * h)} × {c} = **{fmt(cost)} cents**",
                                                                    src("SEAB specimen 2024 MCQ 16")],
                  ["Energy in kW h = kW × hours.", "Multiply by the price per kW h.", "Keep the power in kW."])


explain_mcqs([
    dict(id="o26_fuse_position", chapter=14, level=2, lo="14i", source="SEAB O-Level 2019 MCQ 17",
         stem="A lamp and a heater are connected to the mains. Where should the fuse be placed?",
         correct="in the live wire, before the lamp and the heater",
         wrongs={"in the neutral wire, after the lamp and the heater": "If the fuse melted, the appliances would still be connected to the LIVE wire and could give a shock.",
                 "in the earth wire": "The earth wire carries no current in normal use, so a fuse there would never protect the circuit.",
                 "in parallel with the heater": "A fuse must be in SERIES so that all the current passes through it."},
         hints=["A fuse must carry the whole current, so it is in series.", "When it melts, the appliance must be cut off from the high voltage.", "Which wire is at high voltage?"]),
], category=CAT)


# ================================================================== Ch 15 Magnetism and electromagnetism
explain_mcqs([
    dict(id="o26_force_directions", chapter=15, level=3, lo="15g", source="SEAB O-Level 2014 MCQ 20 and 2017 MCQ 20",
         stem="A wire carrying a current is placed in the magnetic field shown in Fig. 1. The current and the magnetic field can each be reversed. "
              "Of the four directions up the page, down the page, left and right, in how many can a force act on the wire?",
         correct="2", wrongs={"1": "Reversing the current or the field reverses the force, so there are two directions.",
                               "3": "The force is always at right angles to the field, so never left or right (along the field).",
                               "4": "The force cannot act along the field lines."},
         hints=["The force is at right angles to both the current and the field.", "The field here is left to right.", "Reversing either one reverses the force."],
         figure=lambda: sk.flemings_lhr(field="right", current="into")),
    dict(id="o26_xyz_bars", chapter=15, level=4, lo="15a", source="SEAB O-Level 2016 MCQ 19",
         stem="Three metal bars X, Y and Z are tested.\n\n" + md_table(["test", "result"], [["X near either end of Y", "attracts"], ["Z near one end of Y", "repels"]])
              + "\n\nWhich describes the bars?",
         correct="X unmagnetised, Y magnetised, Z magnetised",
         wrongs={"X magnetised, Y magnetised, Z unmagnetised": "Repulsion needs TWO magnets, so Z must be magnetised.",
                 "X magnetised, Y unmagnetised, Z magnetised": "Repulsion between Y and Z means Y is magnetised too.",
                 "X unmagnetised, Y magnetised, Z unmagnetised": "Repulsion only happens between two magnets."},
         hints=["Repulsion is the only sure test for a magnet.", "A magnet attracts unmagnetised iron at BOTH of its ends.", "Start with the repulsion."]),
], category=CAT)

FIELD_ENDS = {"unlike_lr": ("north", "south"), "unlike_rl": ("south", "north"), "like_in": ("south", "south"), "like_out": ("north", "north")}


@template("o26_magnet_ends", chapter=15, level=2, lo="15e", category=CAT)
def magnet_ends(rng):
    kind = nice(rng, *FIELD_ENDS)
    x, y = FIELD_ENDS[kind]
    combos = [f"X {a}, Y {b}" for a in ("north", "south") for b in ("north", "south")]
    correct = f"X {x}, Y {y}"
    why = {c: ("Field lines go from N to S: check which way the arrows point at each end." if c != correct else "") for c in combos}
    wrongs = {c: why[c] for c in combos if c != correct}
    opts, key, mis = text_options(rng, correct, wrongs)
    return dict(stem="Fig. 1 shows the magnetic field between the ends X and Y of two bar magnets. What poles are X and Y?",
                figure=k3.field_between_ends(kind), options=opts, key=key, misconceptions=mis, formula="field lines run from N to S outside a magnet",
                working=["Arrows point away from a north pole and into a south pole.", f"So **{correct}**.", src("SEAB O-Level 2015 MCQ 20 and 2019 MCQ 19")],
                hints=["Which way do the arrows point at X?", "Lines leave a north pole and enter a south pole.",
                       "Lines that bend away from each other show like poles; lines going straight across show unlike poles."])


@template("o26_electron_flow_force", chapter=15, level=4, lo="15h", category=CAT)
def electron_flow_force(rng):
    flow = nice(rng, "right", "left")
    current = (-1, 0, 0) if flow == "right" else (1, 0, 0)          # conventional current is opposite to electron flow
    fx, fy, fz = k3.force_on_wire((0, 1, 0), current)
    answer = {1: "out of the page", -1: "into the page"}[fz]
    other = "into the page" if answer == "out of the page" else "out of the page"
    wrongs = {other: "Conventional current flows OPPOSITE to the electrons. Reverse the current arrow before using Fleming's left-hand rule.",
              "up the page, along the field": "The force is at right angles to the field, never along it.",
              "down the page, against the field": "The force is at right angles to the field."}
    opts, key, mis = text_options(rng, answer, wrongs)
    return dict(stem="Fig. 1 shows a wire in a magnetic field. The arrow shows the direction of **electron flow** in the wire. In which direction is the force on the wire?",
                figure=k3.wire_in_vertical_field(flow), options=opts, key=key, misconceptions=mis, formula="Fleming's left-hand rule uses conventional current",
                working=[f"electron flow to the {flow} → conventional current to the {'left' if flow == 'right' else 'right'}",
                         f"field up the page; Fleming's left-hand rule gives a force **{answer}**", src("SEAB O-Level 2016 MCQ 20")],
                hints=["Fleming's left-hand rule uses CONVENTIONAL current.", "Conventional current is opposite to electron flow.", "First finger = field, second finger = current, thumb = force."])


@template("o26_vertical_wire_force", chapter=15, level=5, lo="15h", category=CAT)
def vertical_wire_force(rng):
    down = nice(rng, True, False)
    n_left = nice(rng, "N", "S")
    field = (1, 0, 0) if n_left == "N" else (-1, 0, 0)
    current = (0, 0, -1) if down else (0, 0, 1)
    fx, fy, _ = k3.force_on_wire(field, current)
    name = next(n for n, d in k3.WIRE_DIRS.items() if d == (fx, fy))
    others = [n for n in k3.WIRE_DIRS if n != name]
    reason = {n: ("The force cannot be along the field (from N to S)." if k3.WIRE_DIRS[n][1] == 0 else "Reverse your answer: check the current direction with the thumb rule.")
              for n in others}
    opts, key, mis = text_options(rng, f"direction {name}", {f"direction {n}": reason[n] for n in others})
    return dict(stem="Fig. 1 shows a vertical wire seen from above, between the poles of a magnet. In which direction is the force on the wire?",
                figure=k3.vertical_wire_top_view(down, n_left), options=opts, key=key, misconceptions=mis, formula="Fleming's left-hand rule",
                working=[f"field from N to S: to the {'right' if n_left == 'N' else 'left'}", f"current {'into' if down else 'out of'} the page",
                         f"Fleming's left-hand rule: force towards **{name}**", src("SEAB O-Level 2019 MCQ 20")],
                hints=["Field goes from N to S.", "Current into the page (×) or out of it (•).", "Use Fleming's left-hand rule: the force is at right angles to both."])


@template("o26_coil_rotation", chapter=15, level=4, lo="15i", category=CAT)
def coil_rotation(rng):
    p_into = nice(rng, True, False)
    n_left = nice(rng, True, False)
    turn = k3.coil_rotation(p_into, n_left)
    other = "clockwise" if turn == "anticlockwise" else "anticlockwise"
    wrongs = {other: "Use Fleming's left-hand rule on each side separately: the forces are in opposite directions.",
              "it does not turn, because the forces on P and Q cancel": "The forces are equal and opposite but act along different lines, so they form a turning effect.",
              "it moves towards the N pole without turning": "The forces on the two sides are opposite, so there is no overall push towards a pole."}
    opts, key, mis = text_options(rng, turn, wrongs)
    return dict(stem="Fig. 1 shows a current-carrying coil between two magnetic poles, seen from above. Which way does the coil turn, as seen from above?",
                figure=k3.coil_between_poles(p_into, n_left), options=opts, key=key, misconceptions=mis, formula="Fleming's left-hand rule on each side of the coil",
                working=["Side P and side Q carry current in opposite directions, so the forces on them are opposite.",
                         f"Fleming's left-hand rule on each side gives a turning effect **{turn}**.", src("SEAB O-Level 2021 MCQ 20")],
                hints=["Find the force on side P with Fleming's left-hand rule.", "The force on side Q is in the opposite direction.", "Opposite forces on opposite sides make it turn."])


@template("o26_compass_wrong", chapter=15, level=3, lo="15e", category=CAT)
def compass_wrong(rng):
    wrong = nice(rng, "P", "Q", "R", "S")
    others = {f"compass {n}": "This needle points along the field (from N to S outside the magnets), so it is drawn correctly." for n in "PQRS" if n != wrong}
    opts, key, mis = text_options(rng, f"compass {wrong}", others)
    return dict(stem="Four plotting compasses are placed near two identical bar magnets (Fig. 1). Which compass is shown pointing in the **wrong** direction?",
                figure=k3.compasses_two_magnets(wrong), options=opts, key=key, misconceptions=mis, formula="a compass needle points along the field, from N to S",
                working=["Outside a magnet the field goes from N to S.", "A compass's north end points along the field.", f"Compass **{wrong}** points the other way.", src("SEAB specimen 2024 MCQ 18")],
                hints=["The north end of a needle points along the field.", "Near a south pole the needle points TOWARDS it.", "Check each compass in turn."])


# ================================================================== Ch 16 Radioactivity
@template("o26_half_life_time", chapter=16, level=2, lo="16g", category=CAT)
def half_life_time(rng):
    T = nice(rng, 8, 12, 20)
    n = nice(rng, 2, 3, 4)
    m0 = nice(rng, 16, 32, 48)
    m = m0 / 2 ** n
    t = n * T
    return calc_q(rng, f"The half-life of a radioactive nuclide is **{T} days**. A pure sample contains **{m0} g** of it. How long is it before only **{fmt(m)} g** is left?\n\n"
                  + md_table(["half-life / days", "start / g", "end / g"], [[T, m0, fmt(m)]]),
                  t, [((n + 1) * T, "Count the halvings carefully."), (2 ** n * T, f"The mass fell by a factor of {2 ** n}; that is {n} half-lives, not {2 ** n}."),
                      ((n - 1) * T, "Count every halving, including the first one.")], "days", "each half-life halves the amount",
                  [" → ".join(f"{fmt(m0 / 2 ** k)} g" for k in range(n + 1)), f"{n} half-lives × {T} days = **{t} days**", src("SEAB specimen 2024 MCQ 20")],
                  ["Halve the mass again and again until you reach the final value.", "Count how many halvings.", "Multiply by the half-life."])
