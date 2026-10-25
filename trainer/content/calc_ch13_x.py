"""Chapter 13 D.C. Circuits: extra calculation templates (series and parallel rules, combinations)."""
from .. import sketches2 as sk
from .base import calc_q, fmt, md_table, nice, template


def par(a, b):
    return a * b / (a + b)


# ---------------------------------------------------------------- L1
@template("c13_series_three", chapter=13, level=1, lo="13f")
def series_three(rng):
    a, b, c = nice(rng, 2, 3, 4), nice(rng, 5, 6, 8), nice(rng, 10, 12, 15)
    return calc_q(rng, f"Fig. 1 shows three resistors, **{a} Ω**, **{b} Ω** and **{c} Ω**, in series. What is their effective resistance?", a + b + c, [
        (1 / (1 / a + 1 / b + 1 / c), "That is the PARALLEL formula. In series, resistances add."),
        ((a + b + c) / 3, "Do not average: add them."),
        (a * b * c, "Add the resistances; do not multiply."),
    ], "Ω", "series: R = R₁ + R₂ + R₃", [f"R = {a} + {b} + {c}", f"= **{a + b + c} Ω**"],
        ["Are the resistors in series or in parallel?", "In series, resistances add.", "Add all three."],
        figure=sk.circuit(series=[("R", f"{a} Ω"), ("R", f"{b} Ω"), ("R", f"{c} Ω")], emf=""))


@template("c13_parallel_currents_sum", chapter=13, level=1, lo="13d")
def parallel_currents_sum(rng):
    I1, I2 = nice(rng, 0.2, 0.3, 0.5, 1.2), nice(rng, 0.4, 0.6, 0.8, 1.5)
    return calc_q(rng, f"Fig. 1 shows two lamps in parallel. The branch currents are **{fmt(I1)} A** and **{fmt(I2)} A**. What is the current from the battery?", I1 + I2, [
        (abs(I1 - I2), "The branch currents ADD to give the main current."),
        ((I1 + I2) / 2, "Do not average: add."),
        (max(I1, I2), "Both branches draw current from the battery."),
    ], "A", "parallel: I = I₁ + I₂", [f"I = {fmt(I1)} + {fmt(I2)}", f"= **{fmt(I1 + I2)} A**"],
        ["Current splits at a junction and rejoins.", "The main current is the sum of the branch currents.", "Add them."],
        figure=sk.circuit(parallel=[[("lamp", None), ("A", f"{fmt(I1)} A")], [("lamp", None), ("A", f"{fmt(I2)} A")]], emf="", ammeter="main"))


@template("c13_series_pds_add", chapter=13, level=1, lo="13c")
def series_pds_add(rng):
    V1, V2 = nice(rng, 2, 3, 4.5, 5), nice(rng, 1.5, 3, 4, 6)
    return calc_q(rng, f"Fig. 1 shows two resistors in series with a battery. The p.d.s across them are **{fmt(V1)} V** and **{fmt(V2)} V**. What is the p.d. across the battery?", V1 + V2, [
        (abs(V1 - V2), "In series, the p.d.s ADD to give the total."),
        ((V1 + V2) / 2, "Do not average: add."),
        (max(V1, V2), "Both p.d.s count."),
    ], "V", "series: V = V₁ + V₂", [f"V = {fmt(V1)} + {fmt(V2)}", f"= **{fmt(V1 + V2)} V**"],
        ["In a series circuit, the battery p.d. is shared.", "The shares add up to the battery p.d.", "Add them."],
        figure=sk.circuit(series=[("R", f"{fmt(V1)} V"), ("R", f"{fmt(V2)} V")], emf="?"))


@template("c13_series_same_current", chapter=13, level=1, lo="13b")
def series_same_current(rng):
    I = nice(rng, 0.2, 0.3, 0.5, 0.8)
    return calc_q(rng, f"Fig. 1 shows a lamp and a resistor in series. The ammeter before the lamp reads **{fmt(I)} A**. What is the current through the resistor?", I, [
        (I / 2, "Current is not shared in a series circuit; it is the same everywhere."),
        (2 * I, "Current does not increase along a series circuit."),
        (0, "Current flows through every component in a complete series circuit."),
    ], "A", "series: the current is the same at every point", [f"I = **{fmt(I)} A** everywhere in the series circuit"],
        ["How many paths are there in a series circuit?", "Charge cannot pile up or disappear.", "So the current is the same at every point."],
        figure=sk.circuit(series=[("A", f"{fmt(I)} A"), ("lamp", None), ("R", "R")], emf=""), sf=None)


# ---------------------------------------------------------------- L2
@template("c13_branch_from_main", chapter=13, level=2, lo="13d")
def branch_from_main(rng):
    I = nice(rng, 1.0, 1.5, 2.0, 2.5)
    I1 = nice(rng, 0.4, 0.6, 0.8)
    return calc_q(rng, f"Fig. 1 shows two resistors in parallel. The main current is **{fmt(I)} A** and the current in one branch is **{fmt(I1)} A**. What is the current in the other branch?", I - I1, [
        (I + I1, "The branch currents add to the main current, so subtract."),
        (I / 2, "The branches need not carry equal currents."),
        (I1, "That is the current in the first branch."),
    ], "A", "I = I₁ + I₂, so I₂ = I − I₁", [f"I₂ = {fmt(I)} − {fmt(I1)}", f"= **{fmt(I - I1)} A**"],
        ["The branch currents add to the main current.", "One branch is known.", "Subtract."],
        figure=sk.circuit(parallel=[[("R", None), ("A", f"{fmt(I1)} A")], [("R", None), ("A", "?")]], emf="", ammeter="main"))


@template("c13_series_three_current", chapter=13, level=2, lo="13g")
def series_three_current(rng):
    E = nice(rng, 6, 9, 12, 24)
    a, b, c = nice(rng, 2, 3), nice(rng, 4, 5), nice(rng, 6, 7)
    I = E / (a + b + c)
    return calc_q(rng, f"Fig. 1 shows a **{E} V** battery in series with **{a} Ω**, **{b} Ω** and **{c} Ω** resistors. What is the current?", I, [
        (E / a, "Use the TOTAL resistance of the series circuit."),
        (E * (a + b + c), "I = V ÷ R."),
        (E / (1 / (1 / a + 1 / b + 1 / c)), "The resistors are in series, so add them."),
    ], "A", "R = R₁ + R₂ + R₃; I = V ÷ R", [f"R = {a} + {b} + {c} = {a + b + c} Ω", f"I = {E} ÷ {a + b + c}", f"= **{fmt(I)} A**"],
        ["Find the total resistance first.", "In series, add the resistances.", "I = V ÷ R."],
        figure=sk.circuit(series=[("R", f"{a} Ω"), ("R", f"{b} Ω"), ("R", f"{c} Ω")], emf=f"{E} V", ammeter="main"))


@template("c13_three_equal_parallel", chapter=13, level=2, lo="13f")
def three_equal_parallel(rng):
    R = nice(rng, 6, 9, 12, 30, 60)
    return calc_q(rng, f"Fig. 1 shows three identical **{R} Ω** resistors connected in parallel. What is their effective resistance?", R / 3, [
        (3 * R, "That is the SERIES total."),
        (R, "Adding parallel paths reduces the total resistance."),
        (R / 2, "There are three resistors, not two."),
    ], "Ω", "n identical resistors in parallel: R ÷ n", [f"1/R = 3 × 1/{R}", f"R = {R} ÷ 3", f"= **{fmt(R / 3)} Ω**"],
        ["Parallel resistance is less than any one resistor.", "For n identical resistors in parallel, R_total = R ÷ n.", f"{R} ÷ 3."],
        figure=sk.circuit(parallel=[[("R", f"{R} Ω")], [("R", f"{R} Ω")], [("R", f"{R} Ω")]], emf=""))


@template("c13_pd_across_second", chapter=13, level=2, lo="13g")
def pd_across_second(rng):
    I = nice(rng, 0.2, 0.5, 1, 1.5)
    R2 = nice(rng, 4, 6, 8, 10)
    return calc_q(rng, f"Fig. 1 shows a series circuit with a current of **{fmt(I)} A**. What is the p.d. across the **{R2} Ω** resistor?", I * R2, [
        (R2 / I, "V = I × R."),
        (I / R2, "V = I × R."),
        (I * R2 * 2, "Use only this resistor's resistance."),
    ], "V", "V = I R for that resistor", [f"V = {fmt(I)} × {R2}", f"= **{fmt(I * R2)} V**"],
        ["The same current flows through every series component.", "Use V = I R for this resistor.", f"{fmt(I)} × {R2}."],
        figure=sk.circuit(series=[("R", "R₁"), ("R", f"{R2} Ω")], emf="", ammeter="main", voltmeter=("series", 1)))


@template("c13_branch_current_simple", chapter=13, level=2, lo="13e")
def branch_current_simple(rng):
    V = nice(rng, 6, 9, 12)
    R1, R2 = nice(rng, 3, 4, 6), nice(rng, 12, 18, 24)
    return calc_q(rng, f"Fig. 1 shows a **{V} V** battery connected to a **{R1} Ω** and a **{R2} Ω** resistor in parallel. What is the current in the **{R2} Ω** resistor?", V / R2, [
        (V / (R1 + R2), "Each parallel branch has the FULL battery p.d. across it."),
        (V / R1, "That is the current in the other branch."),
        (V * R2, "I = V ÷ R."),
    ], "A", "parallel: same p.d. across each branch; I = V ÷ R", [f"p.d. across {R2} Ω = {V} V", f"I = {V} ÷ {R2}", f"= **{fmt(V / R2)} A**"],
        ["What p.d. is across each parallel branch?", "It equals the battery p.d.", "I = V ÷ R for that branch."],
        figure=sk.circuit(parallel=[[("R", f"{R1} Ω")], [("R", f"{R2} Ω")]], emf=f"{V} V"))


@template("c13_series_find_resistor", chapter=13, level=2, lo="13f")
def series_find_resistor(rng):
    R1 = nice(rng, 4, 5, 8, 10)
    R2 = nice(rng, 6, 12, 15, 20)
    return calc_q(rng, f"Fig. 1 shows two resistors in series with an effective resistance of **{R1 + R2} Ω**. One is **{R1} Ω**. What is the other?", R2, [
        (R1 + R2 + R1, "Subtract the known resistor from the total."),
        ((R1 + R2) / R1, "In series, resistances add, so subtract."),
        (R1, "The resistors need not be equal."),
    ], "Ω", "R = R₁ + R₂, so R₂ = R − R₁", [f"R₂ = {R1 + R2} − {R1}", f"= **{R2} Ω**"],
        ["Series resistances add.", "The total is known.", "Subtract the known resistor."],
        figure=sk.circuit(series=[("R", f"{R1} Ω"), ("R", "R = ?")], emf=""), sf=None)


# ---------------------------------------------------------------- L3
@template("c13_parallel_main_current", chapter=13, level=3, lo="13g")
def parallel_main_current(rng):
    V = nice(rng, 6, 12)
    R1, R2 = rng.choice([(3, 6), (4, 12), (6, 12), (2, 6), (4, 4)])
    I = V / R1 + V / R2
    return calc_q(rng, f"Fig. 1 shows a **{V} V** battery connected to **{R1} Ω** and **{R2} Ω** resistors in parallel. What does the ammeter in the main circuit read?", I, [
        (V / (R1 + R2), "The resistors are in PARALLEL, not series."),
        (V / R1, "Add the current in the other branch too."),
        (V / R2, "Add the current in the other branch too."),
    ], "A", "I = V/R₁ + V/R₂", [f"I₁ = {V} ÷ {R1} = {fmt(V / R1)} A", f"I₂ = {V} ÷ {R2} = {fmt(V / R2)} A", f"I = **{fmt(I)} A**"],
        ["Each branch has the full battery p.d.", "Find each branch current.", "Add them."],
        figure=sk.circuit(parallel=[[("R", f"{R1} Ω")], [("R", f"{R2} Ω")]], emf=f"{V} V", ammeter="main"))


@template("c13_series_pd_share", chapter=13, level=3, lo="13c")
def series_pd_share(rng):
    E = nice(rng, 9, 12, 18, 24)
    R1, R2 = rng.choice([(1, 2), (2, 1), (1, 3), (3, 1), (1, 5)])
    R1, R2 = R1 * 2, R2 * 2
    V2 = E * R2 / (R1 + R2)
    return calc_q(rng, f"Fig. 1 shows a **{E} V** battery in series with a **{R1} Ω** and a **{R2} Ω** resistor. What is the p.d. across the **{R2} Ω** resistor?", V2, [
        (E * R1 / (R1 + R2), "That is the p.d. across the OTHER resistor."),
        (E / 2, "The p.d. is shared in proportion to the resistances, not equally."),
        (E, "The battery p.d. is shared between the resistors."),
    ], "V", "I = E ÷ (R₁ + R₂); V₂ = I R₂", [f"I = {E} ÷ {R1 + R2} = {fmt(E / (R1 + R2))} A", f"V₂ = {fmt(E / (R1 + R2))} × {R2}", f"= **{fmt(V2)} V**"],
        ["Find the current first.", "The current is the same in both.", "V = I R for the chosen resistor."],
        figure=sk.circuit(series=[("R", f"{R1} Ω"), ("R", f"{R2} Ω")], emf=f"{E} V", voltmeter=("series", 1)))


@template("c13_series_find_emf", chapter=13, level=3, lo="13g")
def series_find_emf(rng):
    I = nice(rng, 0.5, 1, 1.5, 2)
    R1, R2 = nice(rng, 2, 3, 4), nice(rng, 4, 5, 6)
    return calc_q(rng, f"Fig. 1 shows a battery in series with **{R1} Ω** and **{R2} Ω** resistors. The ammeter reads **{fmt(I)} A**. What is the p.d. across the battery?", I * (R1 + R2), [
        (I * R1, "Include the p.d. across both resistors."),
        (I * R2, "Include the p.d. across both resistors."),
        ((R1 + R2) / I, "V = I × R_total."),
    ], "V", "V = I (R₁ + R₂)", [f"R_total = {R1 + R2} Ω", f"V = {fmt(I)} × {R1 + R2}", f"= **{fmt(I * (R1 + R2))} V**"],
        ["Find the total resistance.", "V = I R.", "Use the total resistance."],
        figure=sk.circuit(series=[("R", f"{R1} Ω"), ("R", f"{R2} Ω")], emf="?", ammeter="main"))


@template("c13_parallel_unknown_r", chapter=13, level=3, lo="13g")
def parallel_unknown_r(rng):
    V = nice(rng, 6, 12)
    R1 = nice(rng, 3, 4, 6)
    R2 = nice(rng, 6, 12, 24)
    I = V / R1 + V / R2
    return calc_q(rng, f"Fig. 1 shows a **{V} V** battery with a **{R1} Ω** resistor and an unknown resistor in parallel. The main current is **{fmt(I)} A**. What is the unknown resistance?", R2, [
        (V / I, "That is the EFFECTIVE resistance of the pair."),
        (V / (I - V / R1) / 2, "Find the current in the unknown branch, then R = V ÷ I."),
        (V / R1, "That is the current in the known branch."),
    ], "Ω", "I₂ = I − V/R₁; R₂ = V ÷ I₂", [f"I₁ = {V} ÷ {R1} = {fmt(V / R1)} A", f"I₂ = {fmt(I)} − {fmt(V / R1)} = {fmt(V / R2)} A", f"R₂ = {V} ÷ {fmt(V / R2)} = **{fmt(R2)} Ω**"],
        ["Find the current in the known branch.", "Subtract it from the main current.", "R = V ÷ I for the unknown branch."],
        figure=sk.circuit(parallel=[[("R", f"{R1} Ω")], [("R", "R = ?")]], emf=f"{V} V", ammeter="main"))


@template("c13_identical_lamps_parallel", chapter=13, level=3, lo="13d")
def identical_lamps_parallel(rng):
    n = nice(rng, 3, 4, 5)
    I = nice(rng, 0.6, 1.2, 1.5, 2.0)
    return calc_q(rng, f"**{n}** identical lamps are connected in parallel to a battery. The table gives the main current. What is the current in each lamp?\n\n" + md_table(["number of lamps", "main current / A"], [[n, fmt(I)]]), I / n, [
        (I, "The main current is shared between the branches."),
        (I * n, "Each branch takes a SHARE of the main current."),
        (I / (n - 1), f"Divide by {n}, the number of branches."),
    ], "A", "identical branches share the main current equally", [f"each lamp = {fmt(I)} ÷ {n}", f"= **{fmt(I / n)} A**"],
        ["The branch currents add to the main current.", "Identical lamps take equal currents.", f"{fmt(I)} ÷ {n}."])


@template("c13_voltmeter_across_two", chapter=13, level=3, lo="13c")
def voltmeter_across_two(rng):
    E = nice(rng, 12, 18, 24)
    a, b, c = nice(rng, 2, 4), nice(rng, 4, 6), nice(rng, 6, 8)
    I = E / (a + b + c)
    return calc_q(rng, f"A **{E} V** battery is connected in series with resistors of **{a} Ω**, **{b} Ω** and **{c} Ω**. The table summarises this. What is the total p.d. across the **{a} Ω** and **{b} Ω** resistors together?\n\n" + md_table(["battery / V", "R₁ / Ω", "R₂ / Ω", "R₃ / Ω"], [[E, a, b, c]]), I * (a + b), [
        (I * a, "Include both resistors."),
        (E - I * (a + b), "That is the p.d. across the third resistor."),
        (E * (a + b) / (a + b + c) / 2, "Find the current, then V = I × (R₁ + R₂)."),
    ], "V", "I = E ÷ R_total; V = I (R₁ + R₂)", [f"I = {E} ÷ {a + b + c} = {fmt(I)} A", f"V = {fmt(I)} × {a + b}", f"= **{fmt(I * (a + b))} V**"],
        ["Find the current from the total resistance.", "The same current flows in all three.", "V = I × combined resistance of the two."])


# ---------------------------------------------------------------- L4
@template("c13_combo_resistance_only", chapter=13, level=4, lo="13f")
def combo_resistance_only(rng):
    Rs = nice(rng, 2, 4, 5, 8)
    R1, R2 = rng.choice([(6, 3), (12, 6), (4, 12), (10, 10), (20, 5)])
    R = Rs + par(R1, R2)
    return calc_q(rng, f"Fig. 1 shows a **{Rs} Ω** resistor in series with a parallel pair of **{R1} Ω** and **{R2} Ω**. What is the effective resistance of the whole arrangement?", R, [
        (Rs + R1 + R2, "The pair is in PARALLEL: combine them with the parallel formula first."),
        (par(R1, R2), "Add the series resistor."),
        (par(Rs + R1, R2), "Combine the parallel pair first, then add the series resistor."),
    ], "Ω", "R = R_s + (R₁ R₂ ÷ (R₁ + R₂))", [f"pair: {R1} × {R2} ÷ ({R1} + {R2}) = {fmt(par(R1, R2))} Ω", f"R = {Rs} + {fmt(par(R1, R2))}", f"= **{fmt(R)} Ω**"],
        ["Deal with the parallel pair first.", "Use the parallel formula (product ÷ sum).", "Then add the series resistor."],
        figure=sk.circuit(series=[("R", f"{Rs} Ω")], parallel=[[("R", f"{R1} Ω")], [("R", f"{R2} Ω")]], emf=""))


@template("c13_combo_series_pd", chapter=13, level=4, lo="13g")
def combo_series_pd(rng):
    E = nice(rng, 6, 12)
    Rs = nice(rng, 2, 4)
    R1, R2 = rng.choice([(6, 3), (12, 6), (4, 4), (12, 12)])
    I = E / (Rs + par(R1, R2))
    return calc_q(rng, f"Fig. 1 shows a **{E} V** battery, a **{Rs} Ω** resistor and a parallel pair of **{R1} Ω** and **{R2} Ω**. What is the p.d. across the **{Rs} Ω** resistor?", I * Rs, [
        (E - I * Rs, "That is the p.d. across the parallel pair."),
        (E * Rs / (Rs + R1 + R2), "Combine the parallel pair before sharing the p.d."),
        (E / 2, "The p.d. is shared in proportion to resistance."),
    ], "V", "R_total = R_s + R_pair; I = E ÷ R_total; V = I R_s",
        [f"R_pair = {fmt(par(R1, R2))} Ω; R_total = {fmt(Rs + par(R1, R2))} Ω", f"I = {E} ÷ {fmt(Rs + par(R1, R2))} = {fmt(I)} A", f"V = {fmt(I)} × {Rs} = **{fmt(I * Rs)} V**"],
        ["Find the total resistance.", "Find the current from the battery.", "V = I R for the series resistor."],
        figure=sk.circuit(series=[("R", f"{Rs} Ω")], parallel=[[("R", f"{R1} Ω")], [("R", f"{R2} Ω")]], emf=f"{E} V"))


@template("c13_add_branch_change", chapter=13, level=4, lo="13d")
def add_branch_change(rng):
    V = nice(rng, 6, 12)
    R1 = nice(rng, 4, 6)
    R3 = nice(rng, 3, 12, 24)
    return calc_q(rng, f"A **{V} V** battery supplies a **{R1} Ω** resistor. A **{R3} Ω** resistor is then connected in parallel with it. The table summarises this. By how much does the battery current increase?\n\n" + md_table(["battery / V", "first resistor / Ω", "added resistor (parallel) / Ω"], [[V, R1, R3]]), V / R3, [
        (V / R1, "The first branch's current does not change; only the new branch adds current."),
        (V / (R1 + R3), "The new resistor is in parallel, so it has the full battery p.d."),
        (V / R1 + V / R3, "That is the new total, not the increase."),
    ], "A", "increase = current in the new branch = V ÷ R₃", [f"new branch current = {V} ÷ {R3}", f"= **{fmt(V / R3)} A**"],
        ["Does adding a parallel branch change the p.d. across the first resistor?", "The new branch draws its own current.", "That current is the increase."])


@template("c13_series_resistor_for_lamp", chapter=13, level=4, lo="13g")
def series_resistor_for_lamp(rng):
    E = nice(rng, 9, 12)
    Vl, I = rng.choice([(6, 0.5), (3, 0.3), (6, 0.25), (2.5, 0.25)])
    R = (E - Vl) / I
    return calc_q(rng, f"A lamp works normally at **{fmt(Vl)} V** and **{fmt(I)} A**. It is to be run from a **{E} V** battery with a resistor in series. The table summarises this. What resistance is needed?\n\n" + md_table(["battery / V", "lamp p.d. / V", "lamp current / A"], [[E, fmt(Vl), fmt(I)]]), R, [
        (E / I, "That is the TOTAL resistance; subtract the lamp's share."),
        (Vl / I, "That is the lamp's resistance."),
        ((E + Vl) / I, "The resistor takes the REST of the battery p.d.: E − V_lamp."),
    ], "Ω", "V_R = E − V_lamp; R = V_R ÷ I", [f"p.d. across resistor = {E} − {fmt(Vl)} = {fmt(E - Vl)} V", f"R = {fmt(E - Vl)} ÷ {fmt(I)}", f"= **{fmt(R)} Ω**"],
        ["The series resistor and lamp share the battery p.d.", "The same current flows in both.", "R = (its p.d.) ÷ I."])


# ---------------------------------------------------------------- L5
@template("c13_combo_branch_unequal", chapter=13, level=5, lo="13g")
def combo_branch_unequal(rng):
    E = nice(rng, 12, 18)
    Rs = nice(rng, 2, 4, 6)
    R1, R2 = rng.choice([(6, 3), (12, 6), (12, 4), (6, 12)])
    I = E / (Rs + par(R1, R2))
    Vp = I * par(R1, R2)
    I1 = Vp / R1
    return calc_q(rng, f"Fig. 1 shows a **{E} V** battery, a **{Rs} Ω** resistor, and a parallel pair of **{R1} Ω** and **{R2} Ω**. What is the current in the **{R1} Ω** resistor?", I1, [
        (E / R1, "The parallel pair does not get the full battery p.d.: some is across the series resistor."),
        (I / 2, "The branches have different resistances, so the current does not split equally."),
        (I, "That is the main current."),
    ], "A", "R_total → I → V across pair → I₁ = V_pair ÷ R₁",
        [f"R_pair = {fmt(par(R1, R2))} Ω; R_total = {fmt(Rs + par(R1, R2))} Ω", f"I = {E} ÷ {fmt(Rs + par(R1, R2))} = {fmt(I)} A; V_pair = {fmt(I)} × {fmt(par(R1, R2))} = {fmt(Vp)} V",
         f"I₁ = {fmt(Vp)} ÷ {R1} = **{fmt(I1)} A**"],
        ["Find the total resistance and main current.", "Find the p.d. across the parallel pair.", "Divide by the branch resistance."],
        figure=sk.circuit(series=[("R", f"{Rs} Ω")], parallel=[[("R", f"{R1} Ω")], [("R", f"{R2} Ω")]], emf=f"{E} V"))


@template("c13_two_pairs_series", chapter=13, level=5, lo="13f")
def two_pairs_series(rng):
    a, b = rng.choice([(6, 3), (4, 4), (12, 6)])
    c, d = rng.choice([(10, 10), (12, 4), (6, 6)])
    R = par(a, b) + par(c, d)
    table = md_table(["pair", "resistors (in parallel) / Ω"], [["first", f"{a} and {b}"], ["second", f"{c} and {d}"]])
    return calc_q(rng, f"Two parallel pairs of resistors are connected in series with each other.\n\n{table}\n\nWhat is the effective resistance of the whole arrangement?", R, [
        (a + b + c + d, "Each pair is in parallel: combine each pair first."),
        (par(a + b, c + d), "Combine within each pair in parallel, then add the pairs in series."),
        (par(a, b), "Add the second pair as well."),
    ], "Ω", "each pair: product ÷ sum; then add the two results", [f"first pair = {fmt(par(a, b))} Ω", f"second pair = {fmt(par(c, d))} Ω", f"total = **{fmt(R)} Ω**"],
        ["Work out each parallel pair separately.", "The two pairs are in series.", "Add the two pair resistances."])


@template("c13_series_r_for_current_parallel", chapter=13, level=5, lo="13g")
def series_r_for_current_parallel(rng):
    E = nice(rng, 12, 24)
    R1, R2 = rng.choice([(6, 6), (12, 6), (6, 3)])
    Itarget = nice(rng, 1, 1.5, 2)
    Rtot = E / Itarget
    Rs = Rtot - par(R1, R2)
    if Rs <= 0:
        Itarget = 1
        Rtot = E / Itarget
        Rs = Rtot - par(R1, R2)
    table = md_table(["battery / V", "parallel pair / Ω", "required main current / A"], [[E, f"{R1} and {R2}", fmt(Itarget)]])
    return calc_q(rng, f"A resistor R is placed in series with a parallel pair of resistors.\n\n{table}\n\nWhat value of R gives the required current?", Rs, [
        (Rtot, "That is the TOTAL resistance needed; subtract the pair's resistance."),
        (Rtot - (R1 + R2), "The pair is in parallel: use product ÷ sum."),
        (par(R1, R2), "That is the resistance of the pair only."),
    ], "Ω", "R_total = E ÷ I; R = R_total − R_pair", [f"R_total = {E} ÷ {fmt(Itarget)} = {fmt(Rtot)} Ω", f"R_pair = {fmt(par(R1, R2))} Ω", f"R = **{fmt(Rs)} Ω**"],
        ["What total resistance gives the required current?", "Find the resistance of the parallel pair.", "The series resistor makes up the difference."])


@template("c13_combo_pd_across_pair", chapter=13, level=5, lo="13g")
def combo_pd_across_pair(rng):
    E = nice(rng, 9, 12, 18)
    Rs = nice(rng, 3, 6)
    R1, R2 = rng.choice([(6, 6), (12, 12), (6, 3)])
    Rp = par(R1, R2)
    Vp = E * Rp / (Rs + Rp)
    return calc_q(rng, f"Fig. 1 shows a **{E} V** battery, a **{Rs} Ω** resistor and a parallel pair of **{R1} Ω** and **{R2} Ω**, with a voltmeter across the pair. What does the voltmeter read?", Vp, [
        (E, "Part of the battery p.d. is across the series resistor."),
        (E - Vp, "That is the p.d. across the series resistor."),
        (E * (R1 + R2) / (Rs + R1 + R2), "Combine the parallel pair first: product ÷ sum."),
    ], "V", "V_pair = E × R_pair ÷ (R_s + R_pair)", [f"R_pair = {fmt(Rp)} Ω", f"I = {E} ÷ {fmt(Rs + Rp)} = {fmt(E / (Rs + Rp))} A", f"V_pair = {fmt(E / (Rs + Rp))} × {fmt(Rp)} = **{fmt(Vp)} V**"],
        ["Find the pair's effective resistance.", "Find the main current.", "V = I × R_pair."],
        figure=sk.circuit(series=[("R", f"{Rs} Ω")], parallel=[[("R", f"{R1} Ω")], [("R", f"{R2} Ω")]], emf=f"{E} V", voltmeter=("parallel", 0)))
