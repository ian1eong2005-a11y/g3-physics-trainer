"""Chapter 12 Electric Charge and Current: Q = It, V = IR, p.d. as work per unit charge, R ∝ L/A."""
from .. import sketches2 as sk
from .base import fmt, nice, numeric_options, template


# ---------------------------------------------------------------- L1
@template("c12_charge_from_current_time", chapter=12, level=1, lo="12e")
def charge_from_current_time(rng):
    I = nice(rng, 0.2, 0.5, 1.5, 2, 2.5, 3, 4)
    t = nice(rng, 5, 10, 20, 30, 40, 60)
    Q = I * t
    opts, key, mis = numeric_options(rng, Q, [
        (I / t, "You divided. Charge = current × time."),
        (t / I, "You divided time by current. Q = I t."),
        (I + t, "You added. Q = I × t."),
    ], unit="C")
    return dict(
        stem=f"Fig. 1 shows a circuit in which the ammeter reads **{fmt(I)} A**. How much charge passes through the ammeter in **{t} s**?",
        figure=sk.circuit(series=[("A", f"{fmt(I)} A"), ("lamp", None)], emf=""),
        options=opts, key=key, misconceptions=mis,
        formula="charge = current × time (Q = I t)",
        working=["Q = I t", f"= {fmt(I)} × {t}", f"= **{fmt(Q)} C**"],
        hints=["Current is the rate of flow of charge: coulombs per second. How do you get the total charge?",
               f"{fmt(I)} coulombs pass every second, for {t} seconds.",
               f"Q = {fmt(I)} × {t}."],
    )


@template("c12_resistance_direct", chapter=12, level=1, lo="12i")
def resistance_direct(rng):
    I = nice(rng, 0.2, 0.25, 0.5, 1.5, 2, 3, 4)
    R = nice(rng, 2, 3, 4, 5, 6, 8, 10, 12)
    V = I * R
    opts, key, mis = numeric_options(rng, R, [
        (V * I, "You multiplied V by I. Resistance = p.d. ÷ current."),
        (I / V, "You divided the wrong way round: R = V ÷ I."),
        (V - I, "You subtracted. R = V ÷ I."),
    ], unit="Ω")
    return dict(
        stem=f"Fig. 1 shows a resistor with a p.d. of **{fmt(V)} V** across it and a current of **{fmt(I)} A** through it. What is its resistance?",
        figure=sk.circuit(series=[("R", "R")], emf=f"{fmt(V)} V", ammeter="main", voltmeter=("series", 0)),
        options=opts, key=key, misconceptions=mis,
        formula="resistance = p.d. ÷ current (R = V ÷ I)",
        working=["R = V ÷ I", f"= {fmt(V)} ÷ {fmt(I)}", f"= **{fmt(R)} Ω**"],
        hints=["Which equation defines resistance in terms of p.d. and current?",
               f"The p.d. is {fmt(V)} V and the current is {fmt(I)} A. Divide.",
               f"R = {fmt(V)} ÷ {fmt(I)}."],
    )


# ---------------------------------------------------------------- L2
@template("c12_current_from_charge_minutes", chapter=12, level=2, lo="12e")
def current_from_charge_minutes(rng):
    I = nice(rng, 0.2, 0.25, 0.5, 1.5, 2, 2.5)
    t_min = nice(rng, 2, 3, 4, 5, 10)
    Q = I * t_min * 60
    opts, key, mis = numeric_options(rng, I, [
        (Q / t_min, "You left the time in minutes. Convert to seconds (× 60) first."),
        (Q * t_min * 60, "You multiplied. Current = charge ÷ time."),
        (Q / (t_min * 60) / 60, "You divided by 60 twice."),
    ], unit="A")
    return dict(
        stem=f"Fig. 1 shows a lamp in a circuit. A charge of **{fmt(Q)} C** flows through the lamp in **{t_min} minutes**. What is the current?",
        figure=sk.circuit(series=[("lamp", None), ("A", "A")], emf=""),
        options=opts, key=key, misconceptions=mis,
        formula="current = charge ÷ time, with the time in seconds",
        working=[f"t = {t_min} min = {t_min * 60} s", f"I = Q ÷ t = {fmt(Q)} ÷ {t_min * 60}", f"= **{fmt(I)} A**"],
        hints=["Current is charge per SECOND. Which given quantity needs converting?",
               f"{t_min} minutes = {t_min * 60} seconds.",
               f"I = {fmt(Q)} ÷ {t_min * 60}."],
    )


@template("c12_pd_from_current_resistance", chapter=12, level=2, lo="12i")
def pd_from_current_resistance(rng):
    I = nice(rng, 0.2, 0.3, 0.5, 1.5, 2, 2.5)
    R = nice(rng, 4, 5, 6, 8, 10, 12, 15, 20)
    V = I * R
    opts, key, mis = numeric_options(rng, V, [
        (R / I, "You divided R by I. p.d. = current × resistance."),
        (I / R, "You divided I by R. V = I R."),
        (I + R, "You added. V = I × R."),
    ], unit="V")
    return dict(
        stem=f"Fig. 1 shows a current of **{fmt(I)} A** flowing through a **{fmt(R)} Ω** resistor. What is the p.d. across the resistor?",
        figure=sk.circuit(series=[("R", f"{fmt(R)} Ω")], emf="", ammeter="main", voltmeter=("series", 0)),
        options=opts, key=key, misconceptions=mis,
        formula="V = I R (rearranged from R = V ÷ I)",
        working=["V = I R", f"= {fmt(I)} × {fmt(R)}", f"= **{fmt(V)} V**"],
        hints=["Rearrange R = V ÷ I to make V the subject.",
               f"Multiply the current by the resistance.",
               f"V = {fmt(I)} × {fmt(R)}."],
    )


@template("c12_current_in_milliamps", chapter=12, level=2, lo="12i")
def current_in_milliamps(rng):
    V = nice(rng, 3, 4.5, 6, 9, 12)
    R = nice(rng, 100, 150, 200, 300, 400, 600, 1200)
    I_mA = V / R * 1000
    opts, key, mis = numeric_options(rng, I_mA, [
        (V / R, "That is the current in amperes. 1 A = 1000 mA."),
        (R / V, "You divided R by V. I = V ÷ R."),
        (V * R / 1000, "You multiplied V by R. I = V ÷ R."),
    ], unit="mA")
    return dict(
        stem=f"Fig. 1 shows a **{fmt(R)} Ω** resistor connected to a **{fmt(V)} V** supply. What is the current, in milliamperes?",
        figure=sk.circuit(series=[("R", f"{fmt(R)} Ω")], emf=f"{fmt(V)} V", ammeter="main"),
        options=opts, key=key, misconceptions=mis,
        formula="I = V ÷ R, then × 1000 to convert A to mA",
        working=[f"I = {fmt(V)} ÷ {fmt(R)} = {fmt(V / R, sf=4)} A", f"= {fmt(V / R, sf=4)} × 1000 mA = **{fmt(I_mA)} mA**"],
        hints=["Find the current in amperes first using I = V ÷ R.",
               f"{fmt(V)} ÷ {fmt(R)} is a small number of amperes. How many milliamperes is that?",
               f"Multiply {fmt(V / R, sf=4)} A by 1000."],
    )


# ---------------------------------------------------------------- L3
@template("c12_resistance_from_vi_graph", chapter=12, level=3, lo="12i")
def resistance_from_vi_graph(rng):
    R = nice(rng, 2, 4, 5, 6, 8, 10, 12, 20)
    vmax = nice(rng, 6, 8, 10, 12)
    opts, key, mis = numeric_options(rng, R, [
        (1 / R, "You found current ÷ p.d. (the gradient of this I–V graph). Resistance = p.d. ÷ current, i.e. 1 ÷ gradient."),
        (vmax, "That is just the largest p.d. on the axis. Read a pair of values and divide V by I."),
        (R * vmax, "You multiplied V by I. R = V ÷ I."),
    ], unit="Ω")
    return dict(
        stem="Fig. 1 shows the current–p.d. graph for a resistor. What is its resistance?",
        figure=sk.vi_graph(R, vmax=vmax),
        options=opts, key=key, misconceptions=mis,
        formula="R = V ÷ I, using any point on the straight line (R = 1 ÷ gradient of an I against V graph)",
        working=[f"from the graph, at V = {fmt(vmax)} V the current is {fmt(vmax / R)} A", f"R = {fmt(vmax)} ÷ {fmt(vmax / R)} = **{fmt(R)} Ω**"],
        hints=["Pick a point on the line where both values are easy to read.",
               "Resistance = p.d. ÷ current. Careful: this graph has current on the vertical axis.",
               f"At {fmt(vmax)} V the current is {fmt(vmax / R)} A; divide."],
    )


@template("c12_charge_with_milliamps", chapter=12, level=3, lo="12e")
def charge_with_milliamps(rng):
    I_mA = nice(rng, 20, 50, 150, 200, 250, 400, 500)
    t = nice(rng, 20, 30, 40, 60, 90, 120)
    Q = I_mA / 1000 * t
    opts, key, mis = numeric_options(rng, Q, [
        (I_mA * t, "You used the current in mA as if it were amperes. Convert mA to A (÷ 1000)."),
        (I_mA / 1000 / t, "You divided by the time. Q = I × t."),
        (I_mA * t / 60, "You divided by 60 instead of 1000; the time is already in seconds."),
    ], unit="C")
    return dict(
        stem=f"Fig. 1 shows an LED circuit. A current of **{fmt(I_mA)} mA** flows for **{t} s**. How much charge passes through the LED?",
        figure=sk.circuit(series=[("R", "R"), ("A", f"{fmt(I_mA)} mA")], emf=""),
        options=opts, key=key, misconceptions=mis,
        formula="Q = I t with I in amperes (mA ÷ 1000)",
        working=[f"I = {fmt(I_mA)} mA = {fmt(I_mA / 1000)} A", f"Q = {fmt(I_mA / 1000)} × {t}", f"= **{fmt(Q)} C**"],
        hints=["The current is in milliamperes. Convert to amperes before using Q = I t.",
               f"{fmt(I_mA)} mA = {fmt(I_mA / 1000)} A.",
               f"Q = {fmt(I_mA / 1000)} × {t}."],
    )


@template("c12_resistance_longer_wire", chapter=12, level=3, lo="12j")
def resistance_longer_wire(rng):
    R1 = nice(rng, 2, 3, 4, 5, 6, 8)
    k = nice(rng, 1.5, 2, 2.5, 3, 4)
    R2 = R1 * k
    opts, key, mis = numeric_options(rng, R2, [
        (R1 / k, "You divided. Resistance is PROPORTIONAL to length: a longer wire has more resistance."),
        (R1, "Length matters: a longer wire of the same thickness has more resistance."),
        (R1 + k, "You added the factor. Multiply the resistance by the ratio of the lengths."),
    ], unit="Ω")
    return dict(
        stem=f"Fig. 1 shows two wires of the same material and the same thickness. Wire X has a resistance of **{fmt(R1)} Ω**. Wire Y is **{fmt(k)} times** as long. What is the resistance of wire Y?",
        figure=sk.wire_pair(1, 1, k, 1),
        options=opts, key=key, misconceptions=mis,
        formula="resistance is proportional to length (same material and cross-sectional area)",
        working=[f"R ∝ L, so R_Y = {fmt(k)} × R_X", f"= {fmt(k)} × {fmt(R1)} = **{fmt(R2)} Ω**"],
        hints=["How does the resistance of a wire depend on its length, if nothing else changes?",
               "Doubling the length doubles the resistance: they are proportional.",
               f"R_Y = {fmt(k)} × {fmt(R1)}."],
    )


# ---------------------------------------------------------------- L4
@template("c12_resistance_length_and_area", chapter=12, level=4, lo="12j")
def resistance_length_and_area(rng):
    R1 = nice(rng, 2, 3, 4, 6, 8, 10)
    kL = nice(rng, 2, 3, 4)
    kA = nice(rng, 2, 3, 4)
    R2 = R1 * kL / kA
    opts, key, mis = numeric_options(rng, R2, [
        (R1 * kL * kA, "You multiplied by both factors. A LARGER area gives LESS resistance: divide by the area factor."),
        (R1 * kA / kL, "You have the factors the wrong way round: R ∝ L ÷ A."),
        (R1 * kL, "You allowed for the length but not the area. Resistance is inversely proportional to cross-sectional area."),
    ], unit="Ω")
    return dict(
        stem=f"Fig. 1 shows two wires of the same material. Wire X has a resistance of **{fmt(R1)} Ω**. Wire Y is **{kL} times** as long and has **{kA} times** the cross-sectional area. What is the resistance of wire Y?",
        figure=sk.wire_pair(1, 1, kL, kA),
        options=opts, key=key, misconceptions=mis,
        formula="R ∝ L ÷ A: resistance is proportional to length and inversely proportional to cross-sectional area",
        working=[f"R_Y = R_X × (length factor) ÷ (area factor)", f"= {fmt(R1)} × {kL} ÷ {kA}", f"= **{fmt(R2)} Ω**"],
        hints=["Two changes: length and area. Which one increases the resistance and which one decreases it?",
               f"Longer by {kL} times: resistance × {kL}. Thicker by {kA} times: resistance ÷ {kA}.",
               f"R_Y = {fmt(R1)} × {kL} ÷ {kA}."],
    )


@template("c12_pd_work_per_charge", chapter=12, level=4, lo="12g")
def pd_work_per_charge(rng):
    V = nice(rng, 1.5, 3, 4.5, 6, 9, 12)
    Q = nice(rng, 2, 4, 5, 10, 20, 50)
    W = V * Q
    opts, key, mis = numeric_options(rng, V, [
        (W * Q, "You multiplied. p.d. = work done ÷ charge."),
        (Q / W, "You divided the wrong way round: V = W ÷ Q."),
        (W, "That is the energy in joules. The p.d. is the energy per coulomb."),
    ], unit="V")
    return dict(
        stem=f"Fig. 1 shows a resistor in a circuit. **{fmt(W)} J** of work is done in driving **{fmt(Q)} C** of charge through the resistor. What is the p.d. across it?",
        figure=sk.circuit(series=[("R", "R")], emf="", voltmeter=("series", 0)),
        options=opts, key=key, misconceptions=mis,
        formula="p.d. = work done ÷ charge (V = W ÷ Q); 1 V = 1 J/C",
        working=["V = W ÷ Q", f"= {fmt(W)} ÷ {fmt(Q)}", f"= **{fmt(V)} V**"],
        hints=["Potential difference is defined as the work done per unit charge. What is 'per unit charge' in symbols?",
               f"{fmt(W)} J is shared among {fmt(Q)} C of charge.",
               f"V = {fmt(W)} ÷ {fmt(Q)}."],
    )


# ---------------------------------------------------------------- L5
@template("c12_resistance_from_charge_and_pd", chapter=12, level=5, lo="12i")
def resistance_from_charge_and_pd(rng):
    I = nice(rng, 0.2, 0.25, 0.5, 1.5, 2)
    t = nice(rng, 20, 30, 40, 50, 60)
    Q = I * t
    R = nice(rng, 4, 6, 8, 10, 12, 24)
    V = I * R
    opts, key, mis = numeric_options(rng, R, [
        (V / Q, "You divided the p.d. by the CHARGE. Find the current (Q ÷ t) first, then R = V ÷ I."),
        (V * I, "You multiplied V by I. R = V ÷ I."),
        (V / (Q * t), "You divided by Q × t. Current = Q ÷ t."),
    ], unit="Ω")
    return dict(
        stem=f"Fig. 1 shows a resistor connected to a **{fmt(V)} V** supply. **{fmt(Q)} C** of charge flows through it in **{t} s**. What is the resistance?",
        figure=sk.circuit(series=[("R", "R")], emf=f"{fmt(V)} V", ammeter="main"),
        options=opts, key=key, misconceptions=mis,
        formula="I = Q ÷ t, then R = V ÷ I",
        working=[f"I = Q ÷ t = {fmt(Q)} ÷ {t} = {fmt(I)} A", f"R = V ÷ I = {fmt(V)} ÷ {fmt(I)}", f"= **{fmt(R)} Ω**"],
        hints=["R = V ÷ I needs the current, which is not given directly. How do you get it from charge and time?",
               f"I = {fmt(Q)} ÷ {t} = {fmt(I)} A.",
               f"R = {fmt(V)} ÷ {fmt(I)}."],
    )


@template("c12_wire_diameter_doubled", chapter=12, level=5, lo="12j")
def wire_diameter_doubled(rng):
    R1 = nice(rng, 4, 6, 8, 12, 16, 20)
    kL = nice(rng, 1, 2, 3)
    kd = nice(rng, 2, 3)
    R2 = R1 * kL / (kd * kd)
    opts, key, mis = numeric_options(rng, R2, [
        (R1 * kL / kd, f"You halved for the diameter. Doubling the DIAMETER multiplies the cross-sectional AREA by {kd * kd} (area ∝ diameter²)."),
        (R1 * kL * kd * kd, "A larger area gives LESS resistance, so divide by the area factor."),
        (R1 * kL, "You ignored the thicker wire. Resistance is inversely proportional to cross-sectional area."),
    ], unit="Ω")
    length_text = "the same length" if kL == 1 else f"**{kL} times** the length"
    return dict(
        stem=f"Fig. 1 shows two wires of the same material. Wire X has a resistance of **{fmt(R1)} Ω**. Wire Y has {length_text} and **{kd} times** the diameter of X. What is the resistance of wire Y?",
        figure=sk.wire_pair(1, 1, kL, kd * kd),
        options=opts, key=key, misconceptions=mis,
        formula="R ∝ L ÷ A, and A ∝ diameter², so doubling the diameter quarters the resistance",
        working=[f"cross-sectional area ∝ diameter², so area factor = {kd}² = {kd * kd}",
                 f"R_Y = {fmt(R1)} × {kL} ÷ {kd * kd}", f"= **{fmt(R2)} Ω**"],
        hints=["The question gives the DIAMETER, but resistance depends on the cross-sectional AREA. How are they related?",
               f"Area ∝ diameter², so {kd} times the diameter means {kd * kd} times the area.",
               f"R_Y = {fmt(R1)} × {kL} ÷ {kd * kd}."],
    )
