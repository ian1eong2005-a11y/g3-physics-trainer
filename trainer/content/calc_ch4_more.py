"""Chapter 4 Dynamics: more calculation templates (F = m a, resultant force)."""
from .. import figs
from .base import fmt, nice, numeric_options, template


# ---------------------------------------------------------------- L1
@template("c4_mass_from_F_a", chapter=4, level=1, lo="4c")
def mass_from_F_a(rng):
    m = nice(rng, 2, 4, 5, 8, 10, 20, 25, 40)
    a = nice(rng, 0.5, 1.5, 2, 2.5, 3, 4, 5)
    F = m * a
    opts, key, mis = numeric_options(rng, m, [
        (F * a, "You multiplied. F = m a, so m = F ÷ a."),
        (a / F, "You divided the wrong way round. m = F ÷ a."),
        (F - a, "You subtracted. m = F ÷ a."),
    ], unit="kg", sf=3)
    return dict(
        stem=f"Fig. 1 shows a resultant force of **{fmt(F)} N** acting on a trolley, which accelerates at **{fmt(a)} m/s²**. What is the mass of the trolley?",
        figure=figs.force_diagram([(f"{fmt(F)} N", "right", 2.0)], label_body="m = ?"),
        options=opts, key=key, misconceptions=mis,
        formula="F = m a, so m = F ÷ a",
        working=["m = F ÷ a", f"= {fmt(F)} ÷ {fmt(a)}", f"= **{fmt(m)} kg**"],
        hints=["Which equation links resultant force, mass and acceleration?",
               "Rearrange F = m a for m.",
               f"{fmt(F)} ÷ {fmt(a)}."],
    )


@template("c4_resultant_opposite_forces", chapter=4, level=1, lo="4b")
def resultant_opposite_forces(rng):
    F1 = nice(rng, 30, 45, 60, 80, 120, 150, 200)
    F2 = nice(rng, 10, 15, 20, 25, 40)
    R = F1 - F2
    opts, key, mis = numeric_options(rng, R, [
        (F1 + F2, "You added. The forces act in OPPOSITE directions, so subtract."),
        (F1, "That is only the larger force; the opposing force reduces the resultant."),
        (F2, "That is only the smaller force."),
    ], unit="N", sf=3)
    return dict(
        stem=f"Fig. 1 shows two horizontal forces acting on a box: **{F1} N** to the right and **{F2} N** to the left. What is the size of the resultant force?",
        figure=figs.force_diagram([(f"{F1} N", "right", 2.0), (f"{F2} N", "left", 1.1)], label_body="box"),
        options=opts, key=key, misconceptions=mis,
        formula="forces in opposite directions: resultant = larger − smaller (in the direction of the larger)",
        working=[f"resultant = {F1} − {F2}", f"= **{R} N** to the right"],
        hints=["The forces act along the same line but in opposite directions.",
               "Take one direction as positive and subtract the opposing force.",
               f"{F1} − {F2}."],
    )


# ---------------------------------------------------------------- L2
@template("c4_braking_force", chapter=4, level=2, lo="4c")
def braking_force(rng):
    m = nice(rng, 600, 800, 900, 1000, 1200, 1500)
    a = nice(rng, 2, 2.5, 3, 4, 5, 6)
    F = m * a
    opts, key, mis = numeric_options(rng, F, [
        (m / a, "You divided. F = m a."),
        (m * a / 10, "You divided by g. F = m a uses the mass in kg directly."),
        (m * a * 10, "You multiplied by g as well. F = m a: there is no g here."),
    ], unit="N", sf=3)
    return dict(
        stem=f"Fig. 1 shows a car of mass **{m} kg** braking. It decelerates uniformly at **{fmt(a)} m/s²**. What is the resultant (braking) force on the car?",
        figure=figs.force_diagram([("braking force = ?", "left", 2.0)], label_body=f"{m} kg"),
        options=opts, key=key, misconceptions=mis,
        formula="F = m a (a deceleration is an acceleration opposite to the motion)",
        working=["F = m a", f"= {m} × {fmt(a)}", f"= **{fmt(F)} N** (opposite to the motion)"],
        hints=["A deceleration is still an acceleration: use F = m a with its size.",
               f"m = {m} kg and a = {fmt(a)} m/s².",
               f"{m} × {fmt(a)}."],
    )


@template("c4_resultant_four_forces", chapter=4, level=2, lo="4b")
def resultant_four_forces(rng):
    W = nice(rng, 50, 80, 100, 200)
    P = nice(rng, 40, 60, 75, 90, 120)
    f = nice(rng, 10, 15, 20, 25, 30)
    R = P - f
    opts, key, mis = numeric_options(rng, R, [
        (P + f, "Friction acts against the push, so subtract it."),
        (P - f + W, "The weight and normal force are vertical and balance each other; they do not add to the horizontal resultant."),
        (P, "You left out friction."),
    ], unit="N", sf=3)
    return dict(
        stem=f"Fig. 1 shows the four forces acting on a crate being pushed along a floor: a push of **{P} N**, friction of **{f} N**, its weight of **{W} N** and the normal force of **{W} N**. What is the resultant force on the crate?",
        figure=figs.force_diagram([(f"{P} N", "right", 1.6), (f"{f} N", "left", 1.0), (f"{W} N", "up", 1.1), (f"{W} N", "down", 1.1)], label_body="crate"),
        options=opts, key=key, misconceptions=mis,
        formula="vertical forces balance; horizontal resultant = push − friction",
        working=[f"vertical: {W} N up and {W} N down cancel", f"horizontal: {P} − {f}", f"= **{R} N** to the right"],
        hints=["Deal with the vertical and the horizontal forces separately.",
               "The vertical forces are equal and opposite. What is their resultant?",
               f"Horizontal resultant = {P} − {f}."],
    )
