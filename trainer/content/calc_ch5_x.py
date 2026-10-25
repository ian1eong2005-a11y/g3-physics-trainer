"""Chapter 5 Turning Effects of Forces: extra calculation templates."""
from .. import sketches
from .base import calc_q, fmt, nice, template

G = 10


# ---------------------------------------------------------------- L1
@template("c5_moment_door", chapter=5, level=1, lo="5b")
def moment_door(rng):
    F = nice(rng, 5, 8, 10, 12, 20)
    d = nice(rng, 0.6, 0.75, 0.8, 0.9)
    return calc_q(rng, f"Fig. 1 shows a door seen from above. A force of **{F} N** is applied at right angles to the door, **{fmt(d)} m** from the hinge. What is the moment about the hinge?", F * d, [
        (F / d, "Moment = force × distance, not force ÷ distance."),
        (F + d, "Multiply, do not add."),
        (F * d * 100, "The distance is already in metres."),
    ], "N m", "moment = force × perpendicular distance from the pivot", ["moment = F × d", f"= {F} × {fmt(d)}", f"= **{fmt(F * d)} N m**"],
        ["The hinge is the pivot.", "moment = F × d.", f"{F} × {fmt(d)}."],
        figure=sketches.beam(1.0, 0.0, [(f"{F} N", d, "up")], dist_labels=[(0, d, f"{fmt(d)} m")]))


@template("c5_moment_child", chapter=5, level=1, lo="5b")
def moment_child(rng):
    W = nice(rng, 200, 250, 300, 400)
    d = nice(rng, 1.0, 1.2, 1.5, 2.0)
    return calc_q(rng, f"Fig. 1 shows a child of weight **{W} N** sitting **{fmt(d)} m** from the pivot of a see-saw. What is the moment of the child's weight about the pivot?", W * d, [
        (W / d, "Moment = force × distance."),
        (W, "That is the weight; multiply by the distance."),
        (W * d / 2, "No ½ in the moment formula."),
    ], "N m", "moment = force × perpendicular distance", ["moment = W × d", f"= {W} × {fmt(d)}", f"= **{fmt(W * d)} N m**"],
        ["The child's weight acts downwards.", "Multiply by the distance from the pivot.", f"{W} × {fmt(d)}."],
        figure=sketches.beam(4.0, 2.0, [(f"{W} N", 2.0 - d, "down")], dist_labels=[(2.0 - d, 2.0, f"{fmt(d)} m")]))


@template("c5_moment_tap_cm", chapter=5, level=1, lo="5b")
def moment_tap_cm(rng):
    F = nice(rng, 4, 5, 6, 8)
    d_cm = nice(rng, 5, 8, 10, 12)
    M = F * d_cm / 100
    return calc_q(rng, f"Fig. 1 shows a tap handle turned by a force of **{F} N** applied **{d_cm} cm** from its axis. What is the moment in N m?", M, [
        (F * d_cm, "Convert cm to m (÷ 100) to get N m."),
        (F * d_cm / 10, "1 m = 100 cm, not 10 cm."),
        (F / (d_cm / 100), "Moment = F × d."),
    ], "N m", "moment = F × d with d in m", [f"d = {d_cm} cm = {fmt(d_cm / 100)} m", f"moment = {F} × {fmt(d_cm / 100)}", f"= **{fmt(M)} N m**"],
        ["The answer is in N m, so the distance must be in m.", "Divide cm by 100.", "Then multiply by the force."],
        figure=sketches.beam(0.2, 0.0, [(f"{F} N", d_cm / 100, "down")], dist_labels=[(0, d_cm / 100, f"{d_cm} cm")]))


@template("c5_moment_crane_kN", chapter=5, level=1, lo="5b")
def moment_crane_kN(rng):
    F = nice(rng, 2, 5, 8, 10)
    d = nice(rng, 4, 6, 10, 12)
    return calc_q(rng, f"Fig. 1 shows a crane arm holding a load of **{F} kN** at **{d} m** from the tower. What is the moment of the load about the tower?", F * d * 1000, [
        (F * d, "1 kN = 1000 N; the moment in N m is 1000 times larger."),
        (F * 1000 / d, "Moment = force × distance."),
        (F * d * 100, "1 kN = 1000 N, not 100 N."),
    ], "N m", "moment = F × d (convert kN to N)", [f"F = {F} kN = {F * 1000} N", f"moment = {F * 1000} × {d}", f"= **{fmt(F * d * 1000)} N m**"],
        ["Convert kN to N.", "moment = F × d.", f"{F * 1000} × {d}."],
        figure=sketches.beam(d + 2, 1.0, [(f"{F} kN", 1.0 + d, "down")], dist_labels=[(1.0, 1.0 + d, f"{d} m")]))


# ---------------------------------------------------------------- L3
@template("c5_balance_find_weight", chapter=5, level=3, lo="5d")
def balance_find_weight(rng):
    W1, d1 = nice(rng, 300, 400, 500), nice(rng, 1.0, 1.2, 1.5)
    d2 = nice(rng, 1.5, 2.0, 2.5)
    W2 = W1 * d1 / d2
    return calc_q(rng, f"Fig. 1 shows a see-saw balanced on a central pivot. A man of weight **{W1} N** sits **{fmt(d1)} m** to the left; a boy sits **{fmt(d2)} m** to the right. What is the boy's weight?", W2, [
        (W1 * d2 / d1, "Clockwise moment = anticlockwise moment: W₂ × d₂ = W₁ × d₁."),
        (W1, "Equal weights balance only at equal distances."),
        (W1 * d1 * d2, "W₂ = W₁ d₁ ÷ d₂."),
    ], "N", "principle of moments: W₁ d₁ = W₂ d₂", [f"{W1} × {fmt(d1)} = W × {fmt(d2)}", f"W = {fmt(W1 * d1)} ÷ {fmt(d2)}", f"= **{fmt(W2)} N**"],
        ["The see-saw is balanced.", "Anticlockwise moment = clockwise moment.", "Solve for the unknown weight."],
        figure=sketches.beam(6.0, 3.0, [(f"{W1} N", 3.0 - d1, "down"), ("W = ?", 3.0 + d2, "down")],
                             dist_labels=[(3.0 - d1, 3.0, f"{fmt(d1)} m"), (3.0, 3.0 + d2, f"{fmt(d2)} m")]))


@template("c5_metre_rule_mass", chapter=5, level=3, lo="5d")
def metre_rule_mass(rng):
    m1 = nice(rng, 100, 150, 200)
    x1 = nice(rng, 10, 20, 30)
    x2 = nice(rng, 70, 80, 90)
    m2 = m1 * (50 - x1) / (x2 - 50)
    return calc_q(rng, f"Fig. 1 shows a uniform metre rule balanced at its 50 cm mark. A **{m1} g** mass hangs at the **{x1} cm** mark and an unknown mass hangs at the **{x2} cm** mark. What is the unknown mass?", m2, [
        (m1 * x1 / x2, "Measure distances from the PIVOT (50 cm mark), not from the end of the rule."),
        (m1 * (x2 - 50) / (50 - x1), "Set the moments equal: m₁ × d₁ = m₂ × d₂, then solve for m₂."),
        (m1, "Equal masses balance only at equal distances from the pivot."),
    ], "g", "moments about the pivot: m₁ d₁ = m₂ d₂ (the rule's weight acts at the pivot)",
        [f"d₁ = 50 − {x1} = {50 - x1} cm, d₂ = {x2} − 50 = {x2 - 50} cm", f"m₂ = {m1} × {50 - x1} ÷ {x2 - 50}", f"= **{fmt(m2)} g**"],
        ["The rule is uniform and pivoted at its centre, so its own weight has no moment.", "Measure each distance from the 50 cm mark.", "Set the moments equal."],
        figure=sketches.beam(100, 50, [(f"{m1} g", x1, "down"), ("m = ?", x2, "down")], dist_labels=[(x1, 50, f"{50 - x1} cm"), (50, x2, f"{x2 - 50} cm")]))


@template("c5_balance_distance_cm", chapter=5, level=3, lo="5d")
def balance_distance_cm(rng):
    F1, d1 = nice(rng, 6, 8, 12), nice(rng, 20, 30, 40)
    F2 = nice(rng, 3, 4, 6, 10)
    d2 = F1 * d1 / F2
    return calc_q(rng, f"Fig. 1 shows a light rod balanced on a pivot. A **{F1} N** weight hangs **{d1} cm** to the left. Where must a **{F2} N** weight hang on the right, measured from the pivot?", d2, [
        (F2 * d1 / F1, "F₁ d₁ = F₂ d₂, so d₂ = F₁ d₁ ÷ F₂."),
        (d1, "Different weights need different distances."),
        (F1 * d1 * F2, "Divide by F₂."),
    ], "cm", "principle of moments: F₁ d₁ = F₂ d₂", [f"{F1} × {d1} = {F2} × d", f"d = {F1 * d1} ÷ {F2}", f"= **{fmt(d2)} cm**"],
        ["The rod is in equilibrium.", "Anticlockwise moment = clockwise moment.", "Keep distances in cm; the units cancel."],
        figure=sketches.beam(1.6, 0.8, [(f"{F1} N", 0.8 - d1 / 100, "down"), (f"{F2} N", 1.5, "down")], dist_labels=[(0.8 - d1 / 100, 0.8, f"{d1} cm"), (0.8, 1.5, "d = ?")]))


@template("c5_crowbar_effort", chapter=5, level=3, lo="5d")
def crowbar_effort(rng):
    L = nice(rng, 600, 800, 1000, 1200)
    dL = nice(rng, 0.05, 0.1, 0.15)
    dE = nice(rng, 0.8, 1.0, 1.2)
    E = L * dL / dE
    return calc_q(rng, f"Fig. 1 shows a crowbar used as a lever. A load of **{L} N** acts **{fmt(dL)} m** from the pivot; the effort is applied **{fmt(dE)} m** from the pivot. What effort is needed?", E, [
        (L * dE / dL, "Effort × its distance = load × its distance; the effort is the SMALLER force."),
        (L, "A lever lets a small effort balance a large load."),
        (L * dL * dE, "E = L d_L ÷ d_E."),
    ], "N", "E × d_E = L × d_L", [f"E × {fmt(dE)} = {L} × {fmt(dL)}", f"E = {fmt(L * dL)} ÷ {fmt(dE)}", f"= **{fmt(E)} N**"],
        ["Take moments about the pivot.", "The moment of the effort must equal the moment of the load.", "Solve for the effort."],
        figure=sketches.beam(dE + dL + 0.2, dL + 0.1, [(f"{L} N", 0.1, "down"), ("E = ?", dL + 0.1 + dE, "down")],
                             dist_labels=[(0.1, dL + 0.1, f"{fmt(dL)} m"), (dL + 0.1, dL + 0.1 + dE, f"{fmt(dE)} m")]))


# ---------------------------------------------------------------- L4
@template("c5_rule_weight_off_centre", chapter=5, level=4, lo="5d")
def rule_weight_off_centre(rng):
    p = nice(rng, 30, 35, 40)
    x = nice(rng, 5, 10, 15)
    F = nice(rng, 1.0, 1.5, 2.0)
    W = F * (p - x) / (50 - p)
    return calc_q(rng, f"Fig. 1 shows a uniform metre rule balanced on a pivot at the **{p} cm** mark when a **{fmt(F)} N** weight hangs at the **{x} cm** mark. What is the weight of the rule?", W, [
        (F * (p - x) / 50, "The rule's weight acts at its CENTRE (50 cm), so its distance from the pivot is 50 − pivot."),
        (F * (50 - p) / (p - x), "Set F × (p − x) = W × (50 − p) and solve for W."),
        (F, "The distances are not equal, so the weights are not equal."),
    ], "N", "the rule's weight acts at 50 cm; moments about the pivot balance",
        [f"F × ({p} − {x}) = W × (50 − {p})", f"W = {fmt(F)} × {p - x} ÷ {50 - p}", f"= **{fmt(W)} N**"],
        ["Where does the weight of a uniform rule act?", "Measure both distances from the pivot.", "Set the moments equal."],
        figure=sketches.beam(100, p, [(f"{fmt(F)} N", x, "down"), ("W", 50, "down")], dist_labels=[(x, p, f"{p - x} cm"), (p, 50, f"{50 - p} cm")]))


@template("c5_three_forces_distance", chapter=5, level=4, lo="5d")
def three_forces_distance(rng):
    A, dA = nice(rng, 20, 30), nice(rng, 1.0, 1.5)
    B, dB = nice(rng, 10, 15), nice(rng, 0.5, 1.0)
    C = nice(rng, 20, 25, 40)
    dC = (A * dA + B * dB) / C
    return calc_q(rng, f"Fig. 1 shows a light beam balanced on a pivot. On the left, **{A} N** acts at **{fmt(dA)} m** and **{B} N** at **{fmt(dB)} m** from the pivot. How far to the right must a **{C} N** force act?", dC, [
        (A * dA / C, "Include BOTH anticlockwise moments."),
        ((A + B) / C, "Use moments (force × distance), not just forces."),
        ((A * dA - B * dB) / C, "Both left-hand forces turn the beam the same way: add their moments."),
    ], "m", "sum of anticlockwise moments = sum of clockwise moments",
        [f"anticlockwise = {A} × {fmt(dA)} + {B} × {fmt(dB)} = {fmt(A * dA + B * dB)} N m", f"d = {fmt(A * dA + B * dB)} ÷ {C}", f"= **{fmt(dC)} m**"],
        ["Add the moments on the left.", "The single force on the right must balance their total.", "d = total moment ÷ C."],
        figure=sketches.beam(4.0, 2.0, [(f"{A} N", 2.0 - dA, "down"), (f"{B} N", 2.0 - dB, "down"), (f"{C} N", 3.6, "down")],
                             dist_labels=[(2.0 - dA, 2.0, f"{fmt(dA)} m"), (2.0, 3.6, "d = ?")]))


@template("c5_wheelbarrow_force", chapter=5, level=4, lo="5d")
def wheelbarrow_force(rng):
    W = nice(rng, 400, 500, 600, 800)
    dW = nice(rng, 0.3, 0.4, 0.5)
    dF = nice(rng, 1.2, 1.4, 1.5)
    F = W * dW / dF
    return calc_q(rng, f"Fig. 1 shows a loaded wheelbarrow. The total weight of **{W} N** acts **{fmt(dW)} m** from the wheel axle; the handles are **{fmt(dF)} m** from the axle. What upward force at the handles holds it level?", F, [
        (W * dF / dW, "Take moments about the axle: F × d_F = W × d_W, so F is smaller than W."),
        (W, "The lever means a smaller force is needed."),
        (W - W * dW / dF, "F = W d_W ÷ d_F."),
    ], "N", "moments about the wheel axle: F × d_F = W × d_W", [f"F × {fmt(dF)} = {W} × {fmt(dW)}", f"F = {fmt(W * dW)} ÷ {fmt(dF)}", f"= **{fmt(F)} N**"],
        ["The wheel axle is the pivot.", "The lifting force and the weight have opposite turning effects.", "Set their moments equal."],
        figure=sketches.beam(dF + 0.2, 0.1, [(f"{W} N", 0.1 + dW, "down"), ("F = ?", 0.1 + dF, "up")],
                             dist_labels=[(0.1, 0.1 + dW, f"{fmt(dW)} m"), (0.1, 0.1 + dF, f"{fmt(dF)} m")]))


@template("c5_seesaw_three_people", chapter=5, level=4, lo="5d")
def seesaw_three_people(rng):
    A, dA = nice(rng, 400, 500), nice(rng, 1.5, 2.0)
    B, dB = nice(rng, 300, 200), nice(rng, 1.0, 0.5)
    C = nice(rng, 500, 600, 800)
    dC = (A * dA - B * dB) / C if A * dA > B * dB else None
    if dC is None or dC <= 0:
        A, dA, B, dB, C = 500, 2.0, 200, 0.5, 600
        dC = (A * dA - B * dB) / C
    # A on the left; B and C on the right
    dC = (A * dA - B * dB) / C
    return calc_q(rng, f"Fig. 1 shows a see-saw pivoted at its centre. **{A} N** sits **{fmt(dA)} m** to the left. On the right, **{B} N** sits **{fmt(dB)} m** from the pivot. Where must a **{C} N** person sit on the right to balance it?", dC, [
        (A * dA / C, "Include the moment of the person already on the right."),
        ((A * dA + B * dB) / C, "The two people on the right turn the same way; subtract B's moment from A's."),
        (dA, "Unequal weights need unequal distances."),
    ], "m", "A d_A = B d_B + C d_C", [f"{A} × {fmt(dA)} = {B} × {fmt(dB)} + {C} × d", f"d = ({fmt(A * dA)} − {fmt(B * dB)}) ÷ {C}", f"= **{fmt(dC)} m**"],
        ["List the clockwise and anticlockwise moments.", "Both people on the right give clockwise moments.", "Solve for the unknown distance."],
        figure=sketches.beam(6.0, 3.0, [(f"{A} N", 3.0 - dA, "down"), (f"{B} N", 3.0 + dB, "down"), (f"{C} N", 5.6, "down")],
                             dist_labels=[(3.0 - dA, 3.0, f"{fmt(dA)} m"), (3.0, 5.6, "d = ?")]))


# ---------------------------------------------------------------- L5
@template("c5_support_reaction", chapter=5, level=5, lo="5d")
def support_reaction(rng):
    L = nice(rng, 4, 5, 6)
    Wp = nice(rng, 100, 200, 300)
    P = nice(rng, 500, 600, 700)
    x = nice(rng, 1, 1.5)
    R_far = (Wp * L / 2 + P * x) / L
    return calc_q(rng, f"Fig. 1 shows a uniform plank of length **{L} m** and weight **{Wp} N** resting on supports at its two ends. A person of weight **{P} N** stands **{fmt(x)} m** from the LEFT end. What upward force does the RIGHT support exert?", R_far, [
        ((Wp + P) / 2, "The supports share the load equally only if the person is in the middle."),
        ((Wp * L / 2 + P * (L - x)) / L, "Take moments about the LEFT support: the person is x from it, not L − x."),
        (Wp + P - (Wp * L / 2 + P * x) / L, "That is the LEFT support's force."),
    ], "N", "moments about the left support: R × L = W_plank × L/2 + P × x",
        [f"R × {L} = {Wp} × {fmt(L / 2)} + {P} × {fmt(x)}", f"R = {fmt(Wp * L / 2 + P * x)} ÷ {L}", f"= **{fmt(R_far)} N**"],
        ["Take moments about the left support, so its force has no moment.", "The plank's weight acts at its centre.", "Solve for the right-hand support force."],
        figure=sketches.beam(L, None, [("R₁", 0.05, "up"), (f"{P} N", x, "down"), ("R₂ = ?", L - 0.05, "up")], uniform=True, weight_label=f"{Wp} N"))


@template("c5_crane_counterweight", chapter=5, level=5, lo="5d")
def crane_counterweight(rng):
    load = nice(rng, 5000, 8000, 10000)
    d_load = nice(rng, 10, 12, 15)
    d_cw = nice(rng, 4, 5, 6)
    cw = load * d_load / d_cw
    return calc_q(rng, f"Fig. 1 shows a tower crane lifting a load of **{load} N** at **{d_load} m** from the tower. A counterweight sits **{d_cw} m** from the tower on the other side. What counterweight balances the load?", cw, [
        (load * d_cw / d_load, "Counterweight × d_cw = load × d_load, so the counterweight is LARGER (it is closer)."),
        (load, "Equal weights balance only at equal distances."),
        (load * d_load * d_cw, "Divide by the counterweight's distance."),
    ], "N", "moments about the tower: C × d_C = L × d_L", [f"C × {d_cw} = {load} × {d_load}", f"C = {load * d_load} ÷ {d_cw}", f"= **{fmt(cw)} N**"],
        ["The tower is the pivot.", "The load and counterweight turn the arm in opposite directions.", "Set their moments equal."],
        figure=sketches.beam(d_load + d_cw + 2, d_cw + 1, [("C = ?", 1.0, "down"), (f"{load} N", d_cw + 1 + d_load, "down")],
                             dist_labels=[(1.0, d_cw + 1, f"{d_cw} m"), (d_cw + 1, d_cw + 1 + d_load, f"{d_load} m")]))


@template("c5_max_load_before_tipping", chapter=5, level=5, lo="5d")
def max_load_before_tipping(rng):
    Wp = nice(rng, 200, 300, 400)
    L = nice(rng, 4, 6)
    over = nice(rng, 1, 1.5)
    support_x = L - over
    d_w = support_x - L / 2
    Fmax = Wp * d_w / over
    return calc_q(rng, f"Fig. 1 shows a uniform plank of weight **{Wp} N** and length **{L} m**, resting on two supports: one under its left end and one **{fmt(over)} m** from its right end. What is the greatest weight that can stand at the right end before the plank starts to tip about the right-hand support?", Fmax, [
        (Wp * over / d_w, "Moments about the support: F × overhang = W × (distance of centre from support)."),
        (Wp, "The distances on each side are not equal."),
        (Wp * (L / 2) / over, "The plank's weight acts at its centre; measure its distance from the SUPPORT."),
    ], "N", "at the point of tipping, moment of load about the support = moment of plank's weight",
        [f"centre of plank is {fmt(L / 2)} m from the left end, {fmt(d_w)} m from the support", f"F × {fmt(over)} = {Wp} × {fmt(d_w)}", f"F = **{fmt(Fmax)} N**"],
        ["When the plank is about to tip, the left support pushes with zero force.", "Take moments about the support.", "The plank's weight acts at its centre."],
        figure=sketches.beam(L, support_x, [("R₁", 0.05, "up"), ("F = ?", L - 0.05, "down")], uniform=True, weight_label=f"{Wp} N",
                             dist_labels=[(support_x, L, f"{fmt(over)} m")]))


@template("c5_rule_weight_from_balance", chapter=5, level=5, lo="5e")
def rule_weight_from_balance(rng):
    W_rule = nice(rng, 1.0, 1.2, 1.5, 2.0)
    p = nice(rng, 20, 25, 30)
    x = nice(rng, 0, 5)
    F = W_rule * (50 - p) / (p - x)
    return calc_q(rng, f"Fig. 1 shows a uniform metre rule of weight **{fmt(W_rule)} N** balanced on a pivot at the **{p} cm** mark by a weight hung at the **{x} cm** mark. What is that weight?", F, [
        (W_rule * (p - x) / (50 - p), "Set F × (p − x) = W × (50 − p) and solve for F."),
        (W_rule, "The distances are different, so the weights are different."),
        (W_rule * 50 / (p - x), "The rule's weight acts at 50 cm: its distance from the pivot is 50 − p."),
    ], "N", "moments about the pivot; the rule's weight acts at the 50 cm mark",
        [f"F × ({p} − {x}) = {fmt(W_rule)} × (50 − {p})", f"F = {fmt(W_rule * (50 - p))} ÷ {p - x}", f"= **{fmt(F)} N**"],
        ["Where does the rule's weight act?", "Take moments about the pivot.", "Solve for the hanging weight."],
        figure=sketches.beam(100, p, [("F = ?", max(x, 1), "down"), (f"{fmt(W_rule)} N", 50, "down")], dist_labels=[(max(x, 1), p, f"{p - x} cm"), (p, 50, f"{50 - p} cm")]))
