"""Chapter 5 Turning Effects of Forces: more calculation templates."""
from .. import sketches
from .base import fmt, nice, numeric_options, template


# ---------------------------------------------------------------- L2
@template("c5_distance_from_moment", chapter=5, level=2, lo="5b")
def distance_from_moment(rng):
    F = nice(rng, 10, 15, 20, 25, 40, 50)
    d = nice(rng, 0.2, 0.4, 0.5, 0.6, 0.8, 1.2)
    M = F * d
    opts, key, mis = numeric_options(rng, d, [
        (M * F, "You multiplied. d = moment ÷ force."),
        (F / M, "You divided the wrong way round. d = M ÷ F."),
        (d * 100, "That is the distance in cm, but the moment is in N m, so the answer is in m."),
    ], unit="m", sf=3)
    return dict(
        stem=f"Fig. 1 shows a force of **{F} N** on a lever. Its moment about the pivot is **{fmt(M)} N m**. How far from the pivot does the force act?",
        figure=sketches.beam(1.6, 0.2, [(f"{F} N", 1.2, "down")], dist_labels=[(0.2, 1.2, "d = ?")]),
        options=opts, key=key, misconceptions=mis,
        formula="moment = F × d, so d = moment ÷ F",
        working=["d = moment ÷ F", f"= {fmt(M)} ÷ {F}", f"= **{fmt(d)} m**"],
        hints=["Start from moment = force × perpendicular distance.",
               "Rearrange to make the distance the subject.",
               f"{fmt(M)} ÷ {F}."],
    )


@template("c5_total_moment_same_side", chapter=5, level=2, lo="5b")
def total_moment_same_side(rng):
    F1, d1 = nice(rng, 10, 20, 30), nice(rng, 0.5, 1.0, 1.5)
    F2, d2 = nice(rng, 5, 15, 25), nice(rng, 2.0, 2.5, 3.0)
    M = F1 * d1 + F2 * d2
    opts, key, mis = numeric_options(rng, M, [
        ((F1 + F2) * (d1 + d2), "Work out each moment separately (force × its own distance), then add."),
        (F1 * d1, "You left out the second force. Both forces turn the beam the same way."),
        (abs(F1 * d1 - F2 * d2), "Both forces are on the same side and both act downwards, so their moments ADD."),
    ], unit="N m", sf=3)
    return dict(
        stem=f"Fig. 1 shows two downward forces on the same side of a pivot: **{F1} N** at **{fmt(d1)} m** and **{F2} N** at **{fmt(d2)} m**. What is the total moment about the pivot?",
        figure=sketches.beam(3.5, 0.2, [(f"{F1} N", 0.2 + d1, "down"), (f"{F2} N", 0.2 + d2, "down")],
                             dist_labels=[(0.2, 0.2 + d1, f"{fmt(d1)} m"), (0.2, 0.2 + d2, f"{fmt(d2)} m")]),
        options=opts, key=key, misconceptions=mis,
        formula="total moment = F₁ d₁ + F₂ d₂ (both clockwise)",
        working=[f"moment of {F1} N = {F1} × {fmt(d1)} = {fmt(F1 * d1)} N m", f"moment of {F2} N = {F2} × {fmt(d2)} = {fmt(F2 * d2)} N m",
                 f"total = **{fmt(M)} N m**"],
        hints=["Each force has its own moment: force × its own distance from the pivot.",
               "Both forces turn the beam in the same direction.",
               "Add the two moments."],
    )
