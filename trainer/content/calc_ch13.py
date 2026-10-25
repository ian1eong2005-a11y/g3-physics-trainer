"""Chapter 13 D.C. Circuits: series and parallel rules, effective resistance, whole-circuit calculations."""
from .. import sketches2 as sk
from .base import fmt, nice, numeric_options, template


# ---------------------------------------------------------------- L1
@template("c13_series_total_resistance", chapter=13, level=1, lo="13f")
def series_total_resistance(rng):
    R1 = nice(rng, 2, 3, 4, 5, 6, 8)
    R2 = nice(rng, 2, 3, 4, 6, 10, 12)
    opts, key, mis = numeric_options(rng, R1 + R2, [
        (R1 * R2 / (R1 + R2), "That is the PARALLEL combination. Resistors in series simply add."),
        (R1 * R2, "You multiplied. Series resistances add: R = R₁ + R₂."),
        (abs(R1 - R2) or (R1 + R2) / 2, "You subtracted. Series resistances add."),
    ], unit="Ω")
    return dict(
        stem=f"Fig. 1 shows a **{fmt(R1)} Ω** resistor and a **{fmt(R2)} Ω** resistor connected in series. What is the effective resistance of the combination?",
        figure=sk.circuit(series=[("R", f"{fmt(R1)} Ω"), ("R", f"{fmt(R2)} Ω")], emf=""),
        options=opts, key=key, misconceptions=mis,
        formula="series: R = R₁ + R₂",
        working=["R = R₁ + R₂", f"= {fmt(R1)} + {fmt(R2)}", f"= **{fmt(R1 + R2)} Ω**"],
        hints=["How do you combine resistors that are in series (one after the other)?",
               "The current passes through both, so the resistances add.",
               f"R = {fmt(R1)} + {fmt(R2)}."],
    )


@template("c13_parallel_pd_same", chapter=13, level=1, lo="13e")
def parallel_pd_same(rng):
    V = nice(rng, 3, 4.5, 6, 9, 12)
    R1 = nice(rng, 2, 3, 4, 6)
    R2 = nice(rng, 3, 6, 8, 12)
    opts, key, mis = numeric_options(rng, V, [
        (V / 2, "You halved the p.d. In PARALLEL, each branch gets the full p.d. of the supply."),
        (V * R2 / (R1 + R2), "You shared the p.d. as if the resistors were in series. Parallel branches have the same p.d."),
        (V * 2, "You doubled. Each branch has the same p.d. as the supply."),
    ], unit="V")
    return dict(
        stem=f"Fig. 1 shows two resistors, **{fmt(R1)} Ω** and **{fmt(R2)} Ω**, connected in parallel to a **{fmt(V)} V** battery. What is the p.d. across the {fmt(R2)} Ω resistor?",
        figure=sk.circuit(parallel=[[("R", f"{fmt(R1)} Ω")], [("R", f"{fmt(R2)} Ω")]], emf=f"{fmt(V)} V"),
        options=opts, key=key, misconceptions=mis,
        formula="the p.d. across each branch of a parallel circuit is the same as the p.d. across the whole combination",
        working=["parallel branches have the same p.d. as the supply", f"p.d. across the {fmt(R2)} Ω resistor = **{fmt(V)} V**"],
        hints=["What is the rule for p.d. in a parallel circuit?",
               "Each branch is connected directly across the battery terminals.",
               f"The p.d. across each branch equals the battery p.d., {fmt(V)} V."],
    )


# ---------------------------------------------------------------- L2
@template("c13_series_current", chapter=13, level=2, lo="13g")
def series_current(rng):
    R1 = nice(rng, 2, 3, 4, 6)
    R2 = nice(rng, 2, 4, 6, 8)
    V = nice(rng, 6, 9, 12, 20, 24)
    I = V / (R1 + R2)
    opts, key, mis = numeric_options(rng, I, [
        (V / R1, "You used only the first resistor. In series the current is limited by the TOTAL resistance."),
        (V / R2, "You used only the second resistor. Add the resistances first."),
        (V * (R1 + R2), "You multiplied. I = V ÷ R."),
    ], unit="A")
    return dict(
        stem=f"Fig. 1 shows a **{fmt(V)} V** battery connected in series with resistors of **{fmt(R1)} Ω** and **{fmt(R2)} Ω**. What current does the ammeter read?",
        figure=sk.circuit(series=[("R", f"{fmt(R1)} Ω"), ("R", f"{fmt(R2)} Ω")], emf=f"{fmt(V)} V", ammeter="main"),
        options=opts, key=key, misconceptions=mis,
        formula="total resistance = R₁ + R₂, then I = V ÷ R_total",
        working=[f"R_total = {fmt(R1)} + {fmt(R2)} = {fmt(R1 + R2)} Ω", f"I = {fmt(V)} ÷ {fmt(R1 + R2)}", f"= **{fmt(I)} A**"],
        hints=["First find the total resistance of the series circuit.",
               f"R_total = {fmt(R1 + R2)} Ω. Then use I = V ÷ R.",
               f"I = {fmt(V)} ÷ {fmt(R1 + R2)}."],
    )


@template("c13_series_pd_across_one", chapter=13, level=2, lo="13c")
def series_pd_across_one(rng):
    R1 = nice(rng, 2, 3, 4, 6, 8)
    R2 = nice(rng, 2, 4, 6, 12)
    I = nice(rng, 0.5, 1, 1.5, 2)
    V1 = I * R1
    V = I * (R1 + R2)
    opts, key, mis = numeric_options(rng, V1, [
        (V, "That is the p.d. across the WHOLE circuit. The p.d. is shared between the two resistors."),
        (V / 2, "You halved the supply p.d. The p.d. is shared in proportion to the resistances, not equally (unless they are equal)."),
        (I * R2, "That is the p.d. across the OTHER resistor."),
    ], unit="V")
    return dict(
        stem=f"Fig. 1 shows a series circuit in which the current is **{fmt(I)} A**. What is the p.d. across the **{fmt(R1)} Ω** resistor?",
        figure=sk.circuit(series=[("R", f"{fmt(R1)} Ω"), ("R", f"{fmt(R2)} Ω")], emf=f"{fmt(V)} V", ammeter="main", voltmeter=("series", 0)),
        options=opts, key=key, misconceptions=mis,
        formula="same current through each series component; V₁ = I R₁",
        working=[f"the current through the {fmt(R1)} Ω resistor is {fmt(I)} A (same everywhere in series)", f"V₁ = I R₁ = {fmt(I)} × {fmt(R1)} = **{fmt(V1)} V**"],
        hints=["In a series circuit the same current flows through every component. Which equation then gives the p.d. across one resistor?",
               f"V = I R for that resistor alone.",
               f"V₁ = {fmt(I)} × {fmt(R1)}."],
    )


@template("c13_parallel_equal_resistors", chapter=13, level=2, lo="13f")
def parallel_equal_resistors(rng):
    R = nice(rng, 2, 4, 6, 8, 10, 12, 20)
    opts, key, mis = numeric_options(rng, R / 2, [
        (2 * R, "You added them. In PARALLEL the effective resistance is LESS than either resistor."),
        (R, "Two equal resistors in parallel give HALF the resistance of one."),
        (R / 4, "You divided by 4. Two equal resistors in parallel give R ÷ 2."),
    ], unit="Ω")
    return dict(
        stem=f"Fig. 1 shows two identical **{fmt(R)} Ω** resistors connected in parallel. What is their effective resistance?",
        figure=sk.circuit(parallel=[[("R", f"{fmt(R)} Ω")], [("R", f"{fmt(R)} Ω")]], emf=""),
        options=opts, key=key, misconceptions=mis,
        formula="parallel: 1/R = 1/R₁ + 1/R₂; for two equal resistors R_eff = R ÷ 2",
        working=[f"1/R = 1/{fmt(R)} + 1/{fmt(R)} = 2/{fmt(R)}", f"R = {fmt(R)} ÷ 2 = **{fmt(R / 2)} Ω**"],
        hints=["Parallel resistors give an effective resistance SMALLER than the smallest one. Which option is smaller?",
               "Use 1/R = 1/R₁ + 1/R₂.",
               f"1/R = 2/{fmt(R)}, so R = {fmt(R)} ÷ 2."],
    )


# ---------------------------------------------------------------- L3
@template("c13_parallel_two_different", chapter=13, level=3, lo="13f")
def parallel_two_different(rng):
    R1, R2 = rng.choice([(6, 3), (12, 4), (12, 6), (20, 5), (10, 10), (8, 8), (15, 10), (30, 6), (4, 12)])
    Reff = R1 * R2 / (R1 + R2)
    opts, key, mis = numeric_options(rng, Reff, [
        (R1 + R2, "You added them: that is the SERIES rule. In parallel use 1/R = 1/R₁ + 1/R₂."),
        ((R1 + R2) / 2, "You averaged them. The parallel resistance is less than the smaller resistor."),
        (R1 * R2, "That is the product alone. Divide by the sum: R = R₁R₂ ÷ (R₁ + R₂)."),
    ], unit="Ω")
    return dict(
        stem=f"Fig. 1 shows a **{fmt(R1)} Ω** resistor and a **{fmt(R2)} Ω** resistor connected in parallel. What is their effective resistance?",
        figure=sk.circuit(parallel=[[("R", f"{fmt(R1)} Ω")], [("R", f"{fmt(R2)} Ω")]], emf=""),
        options=opts, key=key, misconceptions=mis,
        formula="parallel: 1/R = 1/R₁ + 1/R₂, i.e. R = R₁R₂ ÷ (R₁ + R₂)",
        working=[f"1/R = 1/{fmt(R1)} + 1/{fmt(R2)} = {fmt(1 / R1 + 1 / R2, sf=4)}", f"R = {fmt(R1)} × {fmt(R2)} ÷ ({fmt(R1)} + {fmt(R2)}) = **{fmt(Reff)} Ω**"],
        hints=["Which formula combines resistors in parallel? The answer must be smaller than both.",
               "1/R = 1/R₁ + 1/R₂, or product ÷ sum for two resistors.",
               f"R = {fmt(R1)} × {fmt(R2)} ÷ ({fmt(R1)} + {fmt(R2)})."],
    )


@template("c13_parallel_branch_currents", chapter=13, level=3, lo="13d")
def parallel_branch_currents(rng):
    V = nice(rng, 6, 12, 24)
    R1 = nice(rng, 2, 3, 4, 6)
    R2 = nice(rng, 4, 6, 8, 12)
    I1, I2 = V / R1, V / R2
    opts, key, mis = numeric_options(rng, I1 + I2, [
        (V / (R1 + R2), "You treated the resistors as being in series. Each branch has the full p.d.; find each branch current and ADD them."),
        (max(I1, I2), "That is the current in one branch only. The ammeter in the main circuit reads the SUM of the branch currents."),
        (V / (R1 * R2 / (R1 + R2)) / 2, "Check: total current = V ÷ R_parallel, or the sum of the branch currents."),
    ], unit="A")
    return dict(
        stem=f"Fig. 1 shows a **{fmt(V)} V** battery connected to a **{fmt(R1)} Ω** resistor and a **{fmt(R2)} Ω** resistor in parallel. What does the ammeter in the main circuit read?",
        figure=sk.circuit(series=[("A", "A")], parallel=[[("R", f"{fmt(R1)} Ω")], [("R", f"{fmt(R2)} Ω")]], emf=f"{fmt(V)} V"),
        options=opts, key=key, misconceptions=mis,
        formula="each branch has the full p.d.: I₁ = V ÷ R₁, I₂ = V ÷ R₂; total current = I₁ + I₂",
        working=[f"I₁ = {fmt(V)} ÷ {fmt(R1)} = {fmt(I1)} A; I₂ = {fmt(V)} ÷ {fmt(R2)} = {fmt(I2)} A", f"I = {fmt(I1)} + {fmt(I2)} = **{fmt(I1 + I2)} A**"],
        hints=["What p.d. does each branch have? Then find the current in each branch separately.",
               f"I₁ = {fmt(V)} ÷ {fmt(R1)}, I₂ = {fmt(V)} ÷ {fmt(R2)}. The main current is the sum.",
               f"I = {fmt(I1)} + {fmt(I2)}."],
    )


@template("c13_series_missing_pd", chapter=13, level=3, lo="13c")
def series_missing_pd(rng):
    V = nice(rng, 6, 9, 12, 15, 24)
    V1 = nice(rng, 1.5, 2, 3, 4, 5, 8)
    while V1 >= V:
        V1 = V1 / 2
    opts, key, mis = numeric_options(rng, V - V1, [
        (V, "That is the supply p.d. In series the p.d.s across the components ADD UP to the supply p.d."),
        (V + V1, "You added. The second p.d. is the supply p.d. MINUS the first."),
        (V1, "That is the p.d. across the first lamp. The second gets the rest."),
    ], unit="V")
    return dict(
        stem=f"Fig. 1 shows two lamps in series with a **{fmt(V)} V** battery. The p.d. across lamp L1 is **{fmt(V1)} V**. What is the p.d. across lamp L2?",
        figure=sk.circuit(series=[("lamp", "L1"), ("lamp", "L2")], emf=f"{fmt(V)} V", voltmeter=("series", 0)),
        options=opts, key=key, misconceptions=mis,
        formula="series: V_supply = V₁ + V₂, so V₂ = V_supply − V₁",
        working=[f"V₂ = {fmt(V)} − {fmt(V1)}", f"= **{fmt(V - V1)} V**"],
        hints=["What is the rule for p.d.s in a series circuit?",
               "The two p.d.s add up to the battery p.d.",
               f"V₂ = {fmt(V)} − {fmt(V1)}."],
    )


# ---------------------------------------------------------------- L4
@template("c13_combination_total_current", chapter=13, level=4, lo="13g")
def combination_total_current(rng):
    Rs = nice(rng, 1, 2, 3, 4)
    R1, R2 = rng.choice([(6, 3), (12, 4), (6, 6), (12, 6), (4, 4)])
    Rp = R1 * R2 / (R1 + R2)
    Rt = Rs + Rp
    V = nice(rng, 6, 12, 18, 24)
    I = V / Rt
    opts, key, mis = numeric_options(rng, I, [
        (V / (Rs + R1 + R2), "You added all three resistors as if in series. Combine the parallel pair first."),
        (V / Rs, "You ignored the parallel pair."),
        (V / Rp, "You ignored the series resistor."),
    ], unit="A")
    return dict(
        stem=f"Fig. 1 shows a **{fmt(V)} V** battery, a **{fmt(Rs)} Ω** resistor in series with a parallel pair of **{fmt(R1)} Ω** and **{fmt(R2)} Ω**. What current does the ammeter read?",
        figure=sk.circuit(series=[("A", "A"), ("R", f"{fmt(Rs)} Ω")], parallel=[[("R", f"{fmt(R1)} Ω")], [("R", f"{fmt(R2)} Ω")]], emf=f"{fmt(V)} V"),
        options=opts, key=key, misconceptions=mis,
        formula="combine the parallel pair (R = R₁R₂ ÷ (R₁ + R₂)), add the series resistor, then I = V ÷ R_total",
        working=[f"parallel pair: R_p = {fmt(R1)} × {fmt(R2)} ÷ ({fmt(R1)} + {fmt(R2)}) = {fmt(Rp)} Ω", f"R_total = {fmt(Rs)} + {fmt(Rp)} = {fmt(Rt)} Ω",
                 f"I = {fmt(V)} ÷ {fmt(Rt)} = **{fmt(I)} A**"],
        hints=["Reduce the circuit step by step: combine the parallel pair into one resistor first.",
               f"R_parallel = {fmt(Rp)} Ω. Add the series resistor for the total.",
               f"I = {fmt(V)} ÷ {fmt(Rt)}."],
    )


@template("c13_combination_pd_across_pair", chapter=13, level=4, lo="13g")
def combination_pd_across_pair(rng):
    Rs = nice(rng, 2, 3, 4, 6)
    R1, R2 = rng.choice([(6, 3), (12, 4), (6, 6), (12, 6)])
    Rp = R1 * R2 / (R1 + R2)
    I = nice(rng, 0.5, 1, 1.5, 2)
    Vp = I * Rp
    V = I * (Rs + Rp)
    opts, key, mis = numeric_options(rng, Vp, [
        (V, "That is the whole supply p.d. Some of it is across the series resistor."),
        (I * Rs, "That is the p.d. across the SERIES resistor."),
        (I * (R1 + R2), "You used the sum of the parallel resistors. Combine them with the parallel rule first."),
    ], unit="V")
    return dict(
        stem=f"Fig. 1 shows a current of **{fmt(I)} A** from a **{fmt(V)} V** battery through a **{fmt(Rs)} Ω** resistor in series with a parallel pair of **{fmt(R1)} Ω** and **{fmt(R2)} Ω**. What is the p.d. across the parallel pair?",
        figure=sk.circuit(series=[("A", f"{fmt(I)} A"), ("R", f"{fmt(Rs)} Ω")], parallel=[[("R", f"{fmt(R1)} Ω")], [("R", f"{fmt(R2)} Ω")]], emf=f"{fmt(V)} V", voltmeter=("parallel", 0)),
        options=opts, key=key, misconceptions=mis,
        formula="V across the pair = I × R_parallel (or V_supply − I × R_series)",
        working=[f"R_p = {fmt(R1)} × {fmt(R2)} ÷ ({fmt(R1)} + {fmt(R2)}) = {fmt(Rp)} Ω", f"V_p = I R_p = {fmt(I)} × {fmt(Rp)} = **{fmt(Vp)} V**",
                 f"(check: {fmt(V)} − {fmt(I)} × {fmt(Rs)} = {fmt(V - I * Rs)} V)"],
        hints=["The whole current passes through the parallel pair as a unit. What is the pair's effective resistance?",
               f"R_p = {fmt(Rp)} Ω. Then V = I R for the pair.",
               f"V_p = {fmt(I)} × {fmt(Rp)}."],
    )


# ---------------------------------------------------------------- L5
@template("c13_three_parallel", chapter=13, level=5, lo="13f")
def three_parallel(rng):
    R1, R2, R3 = rng.choice([(6, 3, 2), (12, 6, 4), (4, 4, 2), (10, 10, 5), (12, 12, 6), (3, 6, 6)])
    Reff = 1 / (1 / R1 + 1 / R2 + 1 / R3)
    opts, key, mis = numeric_options(rng, Reff, [
        (R1 + R2 + R3, "You added them (series rule). Parallel resistance is less than the smallest resistor."),
        ((R1 + R2 + R3) / 3, "You averaged. Use 1/R = 1/R₁ + 1/R₂ + 1/R₃."),
        (R1 * R2 * R3 / (R1 + R2 + R3), "Product over sum only works for TWO resistors. Use the reciprocal formula."),
    ], unit="Ω")
    return dict(
        stem=f"Fig. 1 shows three resistors, **{fmt(R1)} Ω**, **{fmt(R2)} Ω** and **{fmt(R3)} Ω**, connected in parallel. What is their effective resistance?",
        figure=sk.circuit(parallel=[[("R", f"{fmt(R1)} Ω")], [("R", f"{fmt(R2)} Ω")], [("R", f"{fmt(R3)} Ω")]], emf=""),
        options=opts, key=key, misconceptions=mis,
        formula="1/R = 1/R₁ + 1/R₂ + 1/R₃",
        working=[f"1/R = 1/{fmt(R1)} + 1/{fmt(R2)} + 1/{fmt(R3)} = {fmt(1 / R1 + 1 / R2 + 1 / R3, sf=4)}", f"R = **{fmt(Reff)} Ω**"],
        hints=["Three resistors in parallel: add the RECIPROCALS.",
               f"1/R = 1/{fmt(R1)} + 1/{fmt(R2)} + 1/{fmt(R3)}.",
               "Then take the reciprocal of your answer to get R."],
    )


@template("c13_combination_branch_current", chapter=13, level=5, lo="13g")
def combination_branch_current(rng):
    Rs = nice(rng, 2, 3, 4)
    R1, R2 = rng.choice([(6, 3), (12, 4), (12, 6), (8, 8)])
    Rp = R1 * R2 / (R1 + R2)
    V = nice(rng, 12, 18, 24)
    I = V / (Rs + Rp)
    Vp = I * Rp
    I1 = Vp / R1
    opts, key, mis = numeric_options(rng, I1, [
        (V / R1, "You used the full supply p.d. across the branch. Some p.d. is dropped across the series resistor first."),
        (I, "That is the TOTAL current. Only part of it flows through this branch."),
        (I / 2, "You halved the total current. The current divides in inverse proportion to the branch resistances."),
    ], unit="A")
    return dict(
        stem=f"Fig. 1 shows a **{fmt(V)} V** battery, a **{fmt(Rs)} Ω** resistor in series with a parallel pair of **{fmt(R1)} Ω** and **{fmt(R2)} Ω**. What is the current through the **{fmt(R1)} Ω** resistor?",
        figure=sk.circuit(series=[("R", f"{fmt(Rs)} Ω")], parallel=[[("R", f"{fmt(R1)} Ω")], [("R", f"{fmt(R2)} Ω")]], emf=f"{fmt(V)} V"),
        options=opts, key=key, misconceptions=mis,
        formula="R_p = R₁R₂ ÷ (R₁ + R₂); I_total = V ÷ (R_s + R_p); V_p = I_total × R_p; I₁ = V_p ÷ R₁",
        working=[f"R_p = {fmt(Rp)} Ω; R_total = {fmt(Rs + Rp)} Ω; I_total = {fmt(V)} ÷ {fmt(Rs + Rp)} = {fmt(I)} A",
                 f"p.d. across the pair = {fmt(I)} × {fmt(Rp)} = {fmt(Vp)} V", f"I₁ = {fmt(Vp)} ÷ {fmt(R1)} = **{fmt(I1)} A**"],
        hints=["Work through the circuit: total resistance, total current, p.d. across the parallel pair, then the branch current.",
               f"Total current = {fmt(I)} A; p.d. across the pair = {fmt(Vp)} V.",
               f"I₁ = {fmt(Vp)} ÷ {fmt(R1)}."],
    )
