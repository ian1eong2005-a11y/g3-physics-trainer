"""Chapter 12 Electric Charge and Current: extra calculation templates (Q = I t, R = V / I, V = W / Q, R ∝ L / A)."""
from .. import figs
from .. import sketches2 as sk
from .base import calc_q, fmt, md_table, nice, template


# ---------------------------------------------------------------- L1
@template("c12_current_from_q_t", chapter=12, level=1, lo="12c")
def current_from_q_t(rng):
    Q = nice(rng, 20, 30, 60, 90, 120)
    t = nice(rng, 10, 15, 20, 30, 60)
    I = Q / t
    return calc_q(rng, f"Fig. 1 shows a lamp in a circuit. **{Q} C** of charge flows through it in **{t} s**. What is the current?", I, [
        (Q * t, "Current = charge ÷ time."),
        (t / Q, "I = Q ÷ t, not t ÷ Q."),
        (Q, "That is the charge; divide by the time."),
    ], "A", "I = Q ÷ t", [f"I = {Q} ÷ {t}", f"= **{fmt(I)} A**"],
        ["Current is the rate of flow of charge.", "I = Q ÷ t.", f"{Q} ÷ {t}."],
        figure=sk.circuit(series=[("lamp", None), ("A", "I = ?")], emf=""))


@template("c12_pd_from_ir_simple", chapter=12, level=1, lo="12i")
def pd_from_ir_simple(rng):
    I = nice(rng, 0.5, 1, 2, 3)
    R = nice(rng, 4, 5, 6, 10, 12)
    V = I * R
    return calc_q(rng, f"Fig. 1 shows a current of **{fmt(I)} A** through a **{R} Ω** resistor. What does the voltmeter read?", V, [
        (R / I, "V = I × R, not R ÷ I."),
        (I / R, "V = I × R."),
        (I + R, "Multiply current by resistance."),
    ], "V", "V = I R", [f"V = {fmt(I)} × {R}", f"= **{fmt(V)} V**"],
        ["R = V ÷ I.", "Rearrange for V.", f"{fmt(I)} × {R}."],
        figure=sk.circuit(series=[("R", f"{R} Ω")], emf="", ammeter="main", voltmeter=("series", 0)))


@template("c12_current_from_v_r", chapter=12, level=1, lo="12i")
def current_from_v_r(rng):
    V = nice(rng, 6, 9, 12, 24)
    R = nice(rng, 2, 3, 4, 6, 8)
    I = V / R
    return calc_q(rng, f"Fig. 1 shows a **{R} Ω** resistor connected to a **{V} V** battery. What current flows through it?", I, [
        (V * R, "I = V ÷ R, not V × R."),
        (R / V, "I = V ÷ R."),
        (V - R, "Divide, do not subtract."),
    ], "A", "I = V ÷ R", [f"I = {V} ÷ {R}", f"= **{fmt(I)} A**"],
        ["R = V ÷ I.", "Rearrange for I.", f"{V} ÷ {R}."],
        figure=sk.circuit(series=[("R", f"{R} Ω")], emf=f"{V} V", ammeter="main"))


@template("c12_lamp_resistance_meters", chapter=12, level=1, lo="12h")
def lamp_resistance_meters(rng):
    V = nice(rng, 3, 6, 12)
    I = nice(rng, 0.2, 0.25, 0.5, 1.5)
    R = V / I
    return calc_q(rng, f"Fig. 1 shows a lamp with an ammeter and voltmeter. The ammeter reads **{fmt(I)} A** and the voltmeter reads **{V} V**. What is the resistance of the lamp?", R, [
        (V * I, "R = V ÷ I, not V × I."),
        (I / V, "R = V ÷ I."),
        (V, "That is the p.d.; divide by the current."),
    ], "Ω", "R = V ÷ I", [f"R = {V} ÷ {fmt(I)}", f"= **{fmt(R)} Ω**"],
        ["Resistance = p.d. ÷ current.", "Read V and I from the meters.", f"{V} ÷ {fmt(I)}."],
        figure=sk.circuit(series=[("lamp", None)], emf="", ammeter="main", voltmeter=("series", 0)))


# ---------------------------------------------------------------- L2
@template("c12_time_for_charge", chapter=12, level=2, lo="12e")
def time_for_charge(rng):
    I = nice(rng, 0.5, 2, 2.5, 4)
    t = nice(rng, 20, 40, 60, 120)
    Q = I * t
    return calc_q(rng, f"Fig. 1 shows a circuit carrying a current of **{fmt(I)} A**. How long does it take for **{fmt(Q)} C** of charge to pass the ammeter?", t, [
        (Q * I, "t = Q ÷ I."),
        (I / Q, "t = Q ÷ I, not I ÷ Q."),
        (t / 60, "That is in minutes; the answer should be in seconds."),
    ], "s", "t = Q ÷ I", [f"t = {fmt(Q)} ÷ {fmt(I)}", f"= **{fmt(t)} s**"],
        ["Q = I t.", "Rearrange for t.", f"{fmt(Q)} ÷ {fmt(I)}."],
        figure=sk.circuit(series=[("R", None), ("A", f"{fmt(I)} A")], emf=""))


@template("c12_charge_hours", chapter=12, level=2, lo="12e")
def charge_hours(rng):
    I = nice(rng, 0.1, 0.2, 0.5, 2)
    h = nice(rng, 1, 2, 3, 5)
    Q = I * h * 3600
    table = md_table(["current / A", "time / h"], [[fmt(I), h]])
    return calc_q(rng, f"A phone charger supplies a steady current.\n\n{table}\n\nHow much charge flows?", Q, [
        (I * h, "Convert hours to seconds (× 3600)."),
        (I * h * 60, "1 h = 3600 s, not 60 s."),
        (h * 3600 / I, "Q = I × t."),
    ], "C", "Q = I t with t in s", [f"t = {h} × 3600 = {h * 3600} s", f"Q = {fmt(I)} × {h * 3600}", f"= **{fmt(Q)} C**"],
        ["Charge = current × time.", "Time must be in seconds.", "1 h = 3600 s."])


@template("c12_resistance_kohm", chapter=12, level=2, lo="12i")
def resistance_kohm(rng):
    V = nice(rng, 3, 6, 9, 12)
    I_ma = nice(rng, 1, 2, 3, 4)
    R_k = V / I_ma
    return calc_q(rng, f"Fig. 1 shows a resistor with **{V} V** across it and a current of **{I_ma} mA** through it. What is its resistance in kΩ?", R_k, [
        (V / I_ma * 1000, "That is in Ω; the question asks for kΩ."),
        (V * I_ma, "R = V ÷ I."),
        (V / I_ma / 1000, "Check the conversion: V ÷ mA gives kΩ directly."),
    ], "kΩ", "R = V ÷ I (I in A), then ÷ 1000 for kΩ", [f"I = {I_ma} mA = {fmt(I_ma / 1000)} A", f"R = {V} ÷ {fmt(I_ma / 1000)} = {fmt(V / I_ma * 1000)} Ω", f"= **{fmt(R_k)} kΩ**"],
        ["Convert mA to A.", "R = V ÷ I.", "1 kΩ = 1000 Ω."],
        figure=sk.circuit(series=[("R", "R = ?")], emf=f"{V} V", ammeter="main"))


@template("c12_work_from_pd_charge", chapter=12, level=2, lo="12g")
def work_from_pd_charge(rng):
    V = nice(rng, 1.5, 3, 6, 12)
    Q = nice(rng, 5, 10, 20, 50)
    W = V * Q
    return calc_q(rng, f"Fig. 1 shows a component with a p.d. of **{fmt(V)} V** across it. **{Q} C** of charge passes through it. How much energy is transferred in the component?", W, [
        (V / Q, "p.d. = work done per unit charge, so W = V × Q."),
        (Q / V, "W = V Q."),
        (V + Q, "Multiply p.d. by charge."),
    ], "J", "V = W ÷ Q, so W = V Q", [f"W = {fmt(V)} × {Q}", f"= **{fmt(W)} J**"],
        ["1 V = 1 J per coulomb.", "W = V × Q.", f"{fmt(V)} × {Q}."],
        figure=sk.circuit(series=[("R", None)], emf="", voltmeter=("series", 0)))


@template("c12_current_from_vi_graph", chapter=12, level=2, lo="12i")
def current_from_vi_graph(rng):
    R = nice(rng, 4, 5, 8, 10, 20)
    V = nice(rng, 4, 6, 8)
    I = V / R
    return calc_q(rng, f"Fig. 1 shows the current–p.d. graph of a resistor. What current flows when the p.d. is **{V} V**?", I, [
        (V * R, "Read the current at that p.d. (or use I = V ÷ R)."),
        (R / V, "I = V ÷ R."),
        (I * 2, "Read carefully from the graph at the given p.d."),
    ], "A", "read from the graph, or I = V ÷ R", [f"R from the graph = {R} Ω", f"I = {V} ÷ {R}", f"= **{fmt(I)} A**"],
        ["Find the given p.d. on the horizontal axis.", "Go up to the line and across.", "Check: I = V ÷ R."],
        figure=sk.vi_graph(R, vmax=12))


@template("c12_wire_cut_half", chapter=12, level=2, lo="12j")
def wire_cut_half(rng):
    R = nice(rng, 4, 6, 10, 12, 20)
    k = nice(rng, 2, 4)
    return calc_q(rng, f"Fig. 1 shows a wire of resistance **{R} Ω**. It is cut into **{k}** equal lengths. What is the resistance of one piece?", R / k, [
        (R * k, "A SHORTER wire has LESS resistance: R ∝ length."),
        (R, "Resistance depends on length; the pieces are shorter."),
        (R / (k * k), "R is proportional to length (not length²)."),
    ], "Ω", "R ∝ length", [f"length ÷ {k} → R ÷ {k}", f"R = {R} ÷ {k}", f"= **{fmt(R / k)} Ω**"],
        ["How does resistance depend on length?", "Each piece is 1/" + str(k) + " of the length.", "So R is …"],
        figure=sk.wire_pair(1.0, 1.0, 1.0 / k, 1.0))


# ---------------------------------------------------------------- L3
@template("c12_area_doubled", chapter=12, level=3, lo="12j")
def area_doubled(rng):
    R = nice(rng, 6, 8, 12, 15, 20)
    k = nice(rng, 2, 3, 4)
    return calc_q(rng, f"Fig. 1 shows two wires of the same material and length. Wire X has a resistance of **{R} Ω**. Wire Y has **{k} times** the cross-sectional area. What is the resistance of Y?", R / k, [
        (R * k, "A THICKER wire has LESS resistance: R ∝ 1 ÷ A."),
        (R, "Resistance depends on cross-sectional area."),
        (R / (k * k), "R ∝ 1 ÷ A, and A has increased by " + str(k) + " (not " + str(k * k) + ")."),
    ], "Ω", "R ∝ 1 ÷ A", [f"A × {k} → R ÷ {k}", f"R = {R} ÷ {k}", f"= **{fmt(R / k)} Ω**"],
        ["How does resistance depend on cross-sectional area?", "R is inversely proportional to A.", f"{R} ÷ {k}."],
        figure=sk.wire_pair(1.0, 1.0, 1.0, float(k)))


@template("c12_charge_ma_minutes", chapter=12, level=3, lo="12e")
def charge_ma_minutes(rng):
    I_ma = nice(rng, 20, 50, 200, 250, 400)
    m = nice(rng, 2, 5, 10, 15)
    Q = I_ma / 1000 * m * 60
    table = md_table(["current / mA", "time / min"], [[I_ma, m]])
    return calc_q(rng, f"A small motor runs for a while.\n\n{table}\n\nHow much charge flows through it?", Q, [
        (I_ma * m, "Convert mA to A and minutes to seconds."),
        (I_ma * m * 60, "Convert mA to A (÷ 1000)."),
        (I_ma / 1000 * m, "Convert minutes to seconds (× 60)."),
    ], "C", "Q = I t (A and s)", [f"I = {fmt(I_ma / 1000)} A; t = {m * 60} s", f"Q = {fmt(I_ma / 1000)} × {m * 60}", f"= **{fmt(Q)} C**"],
        ["Q = I t.", "Change mA to A and min to s.", "Multiply."])


@template("c12_mean_resistance_table", chapter=12, level=3, lo="12i")
def mean_resistance_table(rng):
    R = nice(rng, 5, 8, 10, 12, 20)
    Is = [0.2, 0.4, 0.6]
    Vs = [round(R * i * f, 2) for i, f in zip(Is, (1.02, 0.99, 0.99))]
    Rs = [v / i for v, i in zip(Vs, Is)]
    mean = sum(Rs) / 3
    table = md_table(["p.d. / V", "current / A"], [[fmt(v, sf=3), fmt(i)] for v, i in zip(Vs, Is)])
    return calc_q(rng, f"A student measures the p.d. across a resistor for three currents.\n\n{table}\n\nWhat is the mean resistance?", mean, [
        (sum(Vs) / 3 / (sum(Is) / 3) * 1.1, "Work out R = V ÷ I for each row, then average."),
        (Rs[0], "That uses only the first row."),
        (1 / mean, "R = V ÷ I, not I ÷ V."),
    ], "Ω", "R = V ÷ I for each row; mean of the three", [f"R values: {fmt(Rs[0])}, {fmt(Rs[1])}, {fmt(Rs[2])} Ω", f"mean = **{fmt(mean)} Ω**"],
        ["Find R for each pair of readings.", "R = V ÷ I.", "Average the three values."])


@template("c12_length_scaling", chapter=12, level=3, lo="12j")
def length_scaling(rng):
    L1 = nice(rng, 1, 2, 4)
    R1 = nice(rng, 2, 3, 5, 6)
    L2 = nice(rng, 3, 5, 6, 10)
    R2 = R1 * L2 / L1
    table = md_table(["length of wire / m", "resistance / Ω"], [[L1, R1], [L2, "?"]])
    return calc_q(rng, f"Two pieces are cut from the same reel of wire.\n\n{table}\n\nWhat is the resistance of the second piece?", R2, [
        (R1 * L1 / L2, "R ∝ length: a longer wire has MORE resistance."),
        (R1 + L2 - L1, "Resistance is proportional to length, not increased by a fixed amount."),
        (R1, "The second piece is a different length."),
    ], "Ω", "R ∝ L, so R₂ = R₁ × L₂ ÷ L₁", [f"R₂ = {R1} × {L2} ÷ {L1}", f"= **{fmt(R2)} Ω**"],
        ["Same material and thickness, so only the length differs.", "R is directly proportional to length.", "Scale R₁ by L₂ ÷ L₁."])


@template("c12_energy_from_current_time", chapter=12, level=3, lo="12g")
def energy_from_current_time(rng):
    V = nice(rng, 3, 6, 9, 12)
    I = nice(rng, 0.5, 1, 2)
    t = nice(rng, 10, 30, 60)
    Q = I * t
    W = V * Q
    return calc_q(rng, f"Fig. 1 shows a resistor with **{V} V** across it carrying **{fmt(I)} A** for **{t} s**. How much energy is transferred in the resistor?", W, [
        (V * I, "First find the charge (Q = I t), then W = V Q."),
        (V * t, "Use the charge, Q = I t, not just the time."),
        (Q, "That is the charge in C; multiply by the p.d."),
    ], "J", "Q = I t; W = V Q", [f"Q = {fmt(I)} × {t} = {fmt(Q)} C", f"W = {V} × {fmt(Q)}", f"= **{fmt(W)} J**"],
        ["The p.d. tells you the energy per coulomb.", "Find how many coulombs pass.", "Multiply."],
        figure=sk.circuit(series=[("R", None)], emf=f"{V} V", ammeter="main", voltmeter=("series", 0)))


@template("c12_pd_from_graph", chapter=12, level=3, lo="12i")
def pd_from_graph(rng):
    R = nice(rng, 2, 4, 5, 10)
    I = nice(rng, 0.5, 1, 1.5, 2)
    V = I * R
    if V > 12:
        I, V = 1, R
    return calc_q(rng, f"Fig. 1 shows the current–p.d. graph of a resistor. What p.d. is needed to drive a current of **{fmt(I)} A** through it?", V, [
        (I / R, "V = I × R."),
        (R / I, "V = I × R."),
        (V / 2, "Read across from the current to the line, then down to the p.d."),
    ], "V", "find R from the graph; V = I R", [f"R from the graph = {R} Ω", f"V = {fmt(I)} × {R}", f"= **{fmt(V)} V**"],
        ["Find the resistance from any point on the line.", "V = I R.", f"{fmt(I)} × {R}."],
        figure=sk.vi_graph(R, vmax=12))


# ---------------------------------------------------------------- L4
@template("c12_longer_thinner", chapter=12, level=4, lo="12j")
def longer_thinner(rng):
    R = nice(rng, 3, 4, 5, 6)
    kL, kA = rng.choice([(2, 2), (3, 2), (2, 4), (4, 2)])
    R2 = R * kL * kA
    return calc_q(rng, f"Fig. 1 shows two wires of the same material. X has resistance **{R} Ω**. Y is **{kL} times** as long and has **1/{kA}** of the cross-sectional area. What is the resistance of Y?", R2, [
        (R * kL / kA, "A SMALLER area INCREASES the resistance: multiply by " + str(kA) + "."),
        (R * kL, "You also need the effect of the smaller area."),
        (R * kA, "You also need the effect of the greater length."),
    ], "Ω", "R ∝ L ÷ A", [f"length × {kL} → R × {kL}", f"area ÷ {kA} → R × {kA}", f"R = {R} × {kL} × {kA} = **{fmt(R2)} Ω**"],
        ["Treat length and area one at a time.", "Longer → more R; thinner → more R.", "Multiply the two factors."],
        figure=sk.wire_pair(1.0, 1.0, float(kL), 1.0 / kA))


@template("c12_charge_from_it_graph", chapter=12, level=4, lo="12e")
def charge_from_it_graph(rng):
    I = nice(rng, 0.5, 1, 1.5, 2)
    t = nice(rng, 20, 30, 40, 60)
    Q = I * t
    return calc_q(rng, "Fig. 1 shows a current–time graph for a circuit. How much charge flows during the time shown?", Q, [
        (I / t, "Charge = current × time: the AREA under the graph."),
        (Q / 2, "The area is a rectangle, not a triangle."),
        (I, "That is the current; multiply by the time."),
    ], "C", "Q = area under the I–t graph", [f"Q = {fmt(I)} × {t}", f"= **{fmt(Q)} C**"],
        ["Q = I × t.", "On a current–time graph, I × t is the area.", "Find the area of the rectangle."],
        figure=figs.graph([(0, I), (t, I)], -(-t // 10) * 10 + 10, I * 2, 10, I / 2, xlabel="time / s", ylabel="current / A", shade=(0, t)))


@template("c12_resistance_per_metre", chapter=12, level=4, lo="12j")
def resistance_per_metre(rng):
    rpm = nice(rng, 0.5, 1.5, 2, 4)
    L = nice(rng, 2.5, 3.5, 5, 7.5)
    table = md_table(["length / m", "resistance / Ω"], [[1.0, fmt(rpm)], [2.0, fmt(2 * rpm)], [3.0, fmt(3 * rpm)]])
    return calc_q(rng, f"A student measures the resistance of different lengths of the same wire.\n\n{table}\n\nWhat would be the resistance of **{fmt(L)} m** of this wire?", rpm * L, [
        (rpm / L, "R is proportional to length: multiply the resistance per metre by the length."),
        (3 * rpm + L, "Use resistance per metre × length."),
        (rpm, "That is the resistance of 1 m."),
    ], "Ω", "R = (resistance per metre) × length", [f"resistance per metre = {fmt(rpm)} Ω/m", f"R = {fmt(rpm)} × {fmt(L)}", f"= **{fmt(rpm * L)} Ω**"],
        ["Find the resistance of 1 m from the table.", "R ∝ length.", "Multiply by the new length."])


@template("c12_time_for_energy", chapter=12, level=4, lo="12g")
def time_for_energy(rng):
    V = nice(rng, 6, 12)
    I = nice(rng, 0.5, 2, 3)
    t = nice(rng, 20, 40, 60, 100)
    W = V * I * t
    table = md_table(["p.d. / V", "current / A", "energy needed / J"], [[V, fmt(I), fmt(W)]])
    return calc_q(rng, f"A resistor must transfer a fixed amount of energy.\n\n{table}\n\nHow long must the current flow?", t, [
        (W / V, "W ÷ V gives the CHARGE; divide that by the current to get the time."),
        (W / I, "W = V Q and Q = I t: t = W ÷ (V I)."),
        (W * V * I, "t = W ÷ (V I)."),
    ], "s", "Q = W ÷ V; t = Q ÷ I", [f"Q = {fmt(W)} ÷ {V} = {fmt(W / V)} C", f"t = {fmt(W / V)} ÷ {fmt(I)}", f"= **{fmt(t)} s**"],
        ["The p.d. gives energy per coulomb.", "Find how many coulombs are needed.", "Then time = charge ÷ current."])


# ---------------------------------------------------------------- L5
@template("c12_diameter_halved", chapter=12, level=5, lo="12j")
def diameter_halved(rng):
    R = nice(rng, 2, 3, 5, 8)
    return calc_q(rng, f"Fig. 1 shows two wires of the same material and length. X has resistance **{R} Ω**. Y has HALF the diameter of X. What is the resistance of Y?", R * 4, [
        (R * 2, "Halving the DIAMETER quarters the AREA (A ∝ d²), so R is multiplied by 4."),
        (R / 4, "A thinner wire has MORE resistance."),
        (R / 2, "A thinner wire has more resistance, and the area depends on d²."),
    ], "Ω", "A ∝ d²; R ∝ 1 ÷ A", ["diameter ÷ 2 → area ÷ 4", "area ÷ 4 → R × 4", f"R = **{fmt(R * 4)} Ω**"],
        ["How does area depend on diameter?", "A = π d² ÷ 4.", "Then use R ∝ 1 ÷ A."],
        figure=sk.wire_pair(1.0, 1.0, 1.0, 0.25))


@template("c12_charge_two_stage_graph", chapter=12, level=5, lo="12e")
def charge_two_stage_graph(rng):
    I1, t1 = nice(rng, 2, 3), nice(rng, 10, 20)
    I2, t2 = nice(rng, 0.5, 1), nice(rng, 20, 30)
    Q = I1 * t1 + I2 * t2
    return calc_q(rng, "Fig. 1 shows how the current in a circuit changes with time. What total charge flows?", Q, [
        (I1 * (t1 + t2), "The current drops after the first stage; find each area separately."),
        ((I1 + I2) * (t1 + t2) / 2, "Add the two rectangles, do not average the currents."),
        (I1 * t1, "Include the second stage."),
    ], "C", "Q = total area under the I–t graph", [f"stage 1: {I1} × {t1} = {I1 * t1} C", f"stage 2: {fmt(I2)} × {t2} = {fmt(I2 * t2)} C", f"total = **{fmt(Q)} C**"],
        ["Charge = area under the current–time graph.", "Split it into two rectangles.", "Add the areas."],
        figure=figs.graph([(0, I1), (t1, I1), (t1, I2), (t1 + t2, I2)], t1 + t2 + 10, 4, 10, 1, xlabel="time / s", ylabel="current / A", shade=(0, t1 + t2)))


@template("c12_length_for_resistance", chapter=12, level=5, lo="12j")
def length_for_resistance(rng):
    R1, L1 = nice(rng, 2, 3, 4), nice(rng, 0.5, 1, 2)
    target = nice(rng, 12, 15, 18, 24)
    L = target * L1 / R1
    table = md_table(["sample", "length / m", "resistance / Ω"], [["test piece", fmt(L1), R1]])
    return calc_q(rng, f"A heater element needs a resistance of **{target} Ω**. A test piece of the same wire gives these results.\n\n{table}\n\nWhat length of wire is needed?", L, [
        (target * R1 / L1, "L = R_target × (L₁ ÷ R₁): metres per ohm × ohms."),
        (target / R1, "That gives the ratio of resistances; multiply by the test length."),
        (target * L1, "Divide by the test resistance as well."),
    ], "m", "R ∝ L, so L = L₁ × R ÷ R₁", [f"length per ohm = {fmt(L1)} ÷ {R1} = {fmt(L1 / R1)} m/Ω", f"L = {fmt(L1 / R1)} × {target}", f"= **{fmt(L)} m**"],
        ["Resistance is proportional to length.", "How many metres give 1 Ω?", "Scale up to the required resistance."])


@template("c12_pd_from_energy_current", chapter=12, level=5, lo="12g")
def pd_from_energy_current(rng):
    I = nice(rng, 0.5, 2, 2.5, 4)
    t = nice(rng, 30, 60, 120)
    V = nice(rng, 3, 6, 9, 12)
    W = V * I * t
    table = md_table(["energy transferred / J", "current / A", "time / s"], [[fmt(W), fmt(I), t]])
    return calc_q(rng, f"The table gives measurements for a component in a circuit.\n\n{table}\n\nWhat is the p.d. across the component?", V, [
        (W / t, "That is the power. p.d. = energy ÷ charge, and charge = I t."),
        (W / I, "Divide by the charge (I × t), not just the current."),
        (W / (I * t) * 2, "V = W ÷ Q with Q = I t."),
    ], "V", "Q = I t; V = W ÷ Q", [f"Q = {fmt(I)} × {t} = {fmt(I * t)} C", f"V = {fmt(W)} ÷ {fmt(I * t)}", f"= **{fmt(V)} V**"],
        ["p.d. is energy transferred per unit charge.", "Find the charge from the current and time.", "Divide the energy by the charge."])
