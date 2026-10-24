"""Chapter 6 Energy: kinetic and potential energy, conservation, work done, power."""
import math

from .. import sketches
from ..config import G
from .base import fmt, nice, numeric_options, template


# ---------------------------------------------------------------- L1
@template("c6_kinetic_energy", chapter=6, level=1, lo="6b")
def kinetic_energy(rng):
    m = nice(rng, 2, 4, 5, 8, 10, 50, 800, 1200)
    v = nice(rng, 2, 3, 4, 5, 6, 10, 20)
    Ek = 0.5 * m * v * v
    opts, key, mis = numeric_options(rng, Ek, [
        (0.5 * m * v, "You forgot to square the speed. Ek = ½ m v²."),
        (m * v * v, "You forgot the ½. Ek = ½ m v²."),
        (m * v, "That is m × v (momentum). Kinetic energy = ½ m v²."),
    ], unit="J")
    return dict(
        stem=f"Fig. 1 shows an object of mass **{fmt(m)} kg** moving at a constant speed of **{fmt(v)} m/s**. What is its kinetic energy?",
        figure=sketches.motion_sketch(f"{fmt(m)} kg", f"v = {fmt(v)} m/s", "constant speed"),
        options=opts, key=key, misconceptions=mis,
        formula="kinetic energy Ek = ½ m v²",
        working=["Ek = ½ m v²", f"= ½ × {fmt(m)} × {fmt(v)}²", f"= **{fmt(Ek)} J**"],
        hints=["Which formula gives the kinetic energy of a moving object? Watch the square.",
               f"v² = {fmt(v)} × {fmt(v)} = {fmt(v * v)}. Then multiply by the mass and by ½.",
               f"Ek = ½ × {fmt(m)} × {fmt(v * v)}."],
    )


@template("c6_potential_energy", chapter=6, level=1, lo="6b")
def potential_energy(rng):
    m = nice(rng, 0.5, 2, 5, 8, 10, 20, 50)
    h = nice(rng, 1.5, 2, 3, 4, 5, 8, 12)
    Ep = m * G * h
    opts, key, mis = numeric_options(rng, Ep, [
        (m * h, "You forgot g. Ep = m g h, with g = 10 N/kg."),
        (m * G, "That is the weight. Multiply by the height as well."),
        (0.5 * m * G * h, "There is no ½ in m g h."),
    ], unit="J")
    return dict(
        stem=f"Fig. 1 shows a box of mass **{fmt(m)} kg** lifted through a height of **{fmt(h)} m**. Taking g = 10 N/kg, what is the gain in gravitational potential energy of the box?",
        figure=sketches.lift_sketch(f"h = {fmt(h)} m", body_label=f"{fmt(m)} kg"),
        options=opts, key=key, misconceptions=mis,
        formula="gravitational potential energy Ep = m g h",
        working=["Ep = m g h", f"= {fmt(m)} × 10 × {fmt(h)}", f"= **{fmt(Ep)} J**"],
        hints=["Which formula gives gravitational potential energy near the Earth's surface?",
               f"Weight = {fmt(m)} × 10 = {fmt(m * G)} N. Lifting it through {fmt(h)} m stores weight × height.",
               f"Ep = {fmt(m)} × 10 × {fmt(h)}."],
    )


# ---------------------------------------------------------------- L2
@template("c6_work_done", chapter=6, level=2, lo="6d")
def work_done(rng):
    F = nice(rng, 20, 25, 40, 50, 80, 120, 150)
    d = nice(rng, 2, 3, 4, 5, 6, 8, 12)
    W = F * d
    opts, key, mis = numeric_options(rng, W, [
        (F / d, "You divided. Work done = force × distance moved in the direction of the force."),
        (F + d, "You added. Work done = force × distance."),
        (F * d / 2, "There is no ½ in work done = F × d."),
    ], unit="J")
    return dict(
        stem=f"Fig. 1 shows a box pushed along a floor by a horizontal force of **{fmt(F)} N** through a distance of **{fmt(d)} m**. How much work is done by the force?",
        figure=sketches.push_sketch(f"F = {fmt(F)} N", f"d = {fmt(d)} m", body_label="box"),
        options=opts, key=key, misconceptions=mis,
        formula="work done = force × distance moved in the direction of the force",
        working=["work done = F × d", f"= {fmt(F)} × {fmt(d)}", f"= **{fmt(W)} J**"],
        hints=["Work is done when a force moves something. Which two quantities multiply to give it?",
               f"The force is {fmt(F)} N and the box moves {fmt(d)} m in the same direction as the force.",
               f"work done = {fmt(F)} × {fmt(d)}."],
    )


@template("c6_power_from_energy", chapter=6, level=2, lo="6e")
def power_from_energy(rng):
    E = nice(rng, 600, 900, 1200, 1500, 2400, 3000, 6000)
    t = nice(rng, 5, 10, 12, 15, 20, 30, 60)
    P = E / t
    opts, key, mis = numeric_options(rng, P, [
        (E * t, "You multiplied. Power = energy transferred ÷ time taken."),
        (t / E, "You divided the wrong way round: power = energy ÷ time."),
        (E, "That is the energy in joules. Power is energy per second, in watts."),
    ], unit="W")
    return dict(
        stem=f"Fig. 1 shows a motor that does **{fmt(E)} J** of work lifting a load in **{fmt(t)} s**. What is the power of the motor?",
        figure=sketches.lift_sketch("", body_label="load", extra=f"work done = {fmt(E)} J in {fmt(t)} s"),
        options=opts, key=key, misconceptions=mis,
        formula="power = energy transferred ÷ time taken",
        working=["power = energy ÷ time", f"= {fmt(E)} ÷ {fmt(t)}", f"= **{fmt(P)} W**"],
        hints=["Power is how quickly energy is transferred. What is the formula, and what unit comes out?",
               f"{fmt(E)} J of energy over {fmt(t)} s. 1 W = 1 J per second.",
               f"power = {fmt(E)} ÷ {fmt(t)}."],
    )


# ---------------------------------------------------------------- L3
@template("c6_speed_at_bottom", chapter=6, level=3, lo="6c")
def speed_at_bottom(rng):
    h = nice(rng, 0.8, 1.25, 1.8, 2.45, 3.2, 5, 7.2, 20)
    v = math.sqrt(2 * G * h)
    m = nice(rng, 1, 2, 4, 5, 10)
    opts, key, mis = numeric_options(rng, v, [
        (math.sqrt(G * h), "You used v² = g h. From ½ m v² = m g h you get v² = 2 g h."),
        (2 * G * h, "That is v², not v. Take the square root."),
        (G * h, "That is g h. Set ½ v² = g h and solve for v."),
    ], unit="m/s")
    return dict(
        stem=f"Fig. 1 shows a trolley of mass **{fmt(m)} kg** released from rest at the top of a smooth slope of height **{fmt(h)} m**. Taking g = 10 N/kg and ignoring friction, what is its speed at the bottom?",
        figure=sketches.slope_sketch(f"h = {fmt(h)} m", top_label=f"{fmt(m)} kg, at rest", bottom_label="speed = ?"),
        options=opts, key=key, misconceptions=mis,
        formula="energy conservation: ½ m v² = m g h, so v = √(2 g h)",
        working=[f"Ep lost = m g h = {fmt(m)} × 10 × {fmt(h)} = {fmt(m * G * h)} J = Ek gained",
                 f"½ × {fmt(m)} × v² = {fmt(m * G * h)}  →  v² = {fmt(2 * G * h)}", f"v = √{fmt(2 * G * h)} = **{fmt(v)} m/s**"],
        hints=["No friction, so where does the gravitational potential energy go? Write the two energies and set them equal.",
               f"m g h = ½ m v². The mass cancels: v² = 2 × 10 × {fmt(h)} = {fmt(2 * G * h)}.",
               f"v = √{fmt(2 * G * h)}."],
    )


@template("c6_power_lifting", chapter=6, level=3, lo="6e")
def power_lifting(rng):
    m = nice(rng, 20, 40, 50, 60, 80, 120)
    h = nice(rng, 3, 4, 5, 6, 10, 12)
    t = nice(rng, 4, 5, 6, 8, 10, 15, 20)
    P = m * G * h / t
    opts, key, mis = numeric_options(rng, P, [
        (m * G * h, "That is the work done in joules. Divide by the time to get power."),
        (m * h / t, "You forgot g. Work done = m g h."),
        (m * G * h * t, "You multiplied by time. Power = energy ÷ time."),
    ], unit="W")
    return dict(
        stem=f"Fig. 1 shows a motor lifting a load of mass **{fmt(m)} kg** through a height of **{fmt(h)} m** in **{fmt(t)} s** at constant speed. Taking g = 10 N/kg, what is the useful power output of the motor?",
        figure=sketches.lift_sketch(f"h = {fmt(h)} m", body_label=f"{fmt(m)} kg", extra=f"time taken = {fmt(t)} s"),
        options=opts, key=key, misconceptions=mis,
        formula="work done = m g h; power = work done ÷ time",
        working=[f"work done = m g h = {fmt(m)} × 10 × {fmt(h)} = {fmt(m * G * h)} J", f"power = {fmt(m * G * h)} ÷ {fmt(t)}", f"= **{fmt(P)} W**"],
        hints=["Two steps: how much energy is transferred to the load, then how fast?",
               f"Energy = m g h = {fmt(m)} × 10 × {fmt(h)} = {fmt(m * G * h)} J, transferred in {fmt(t)} s.",
               f"power = {fmt(m * G * h)} ÷ {fmt(t)}."],
    )


# ---------------------------------------------------------------- L4
@template("c6_height_from_speed", chapter=6, level=4, lo="6c")
def height_from_speed(rng):
    v = nice(rng, 4, 5, 6, 8, 10, 12)
    h = v * v / (2 * G)
    m = nice(rng, 0.5, 1, 2, 3)
    opts, key, mis = numeric_options(rng, h, [
        (v * v / G, "You used v² = g h. It should be v² = 2 g h, so h = v² ÷ 2g."),
        (v / G, "You divided the speed by g: that gives a time, not a height. Use h = v² ÷ 2g."),
        (v * v, "That is v². Divide by 2g."),
    ], unit="m")
    return dict(
        stem=f"Fig. 1 shows a trolley of mass **{fmt(m)} kg** moving at **{fmt(v)} m/s** at the bottom of a smooth slope. It runs up the slope and comes to rest. Taking g = 10 N/kg and ignoring friction, what vertical height does it reach?",
        figure=sketches.slope_sketch("h = ?", top_label="comes to rest", bottom_label=f"v = {fmt(v)} m/s"),
        options=opts, key=key, misconceptions=mis,
        formula="½ m v² = m g h, so h = v² ÷ (2 g)",
        working=[f"Ek at bottom = ½ × {fmt(m)} × {fmt(v)}² = {fmt(0.5 * m * v * v)} J",
                 f"= Ep at top = {fmt(m)} × 10 × h", f"h = {fmt(0.5 * m * v * v)} ÷ {fmt(m * G)} = **{fmt(h)} m**"],
        hints=["All the kinetic energy becomes gravitational potential energy. Write ½ m v² = m g h.",
               f"The mass cancels, so h = v² ÷ (2g) = {fmt(v * v)} ÷ 20.",
               f"h = {fmt(v * v)} ÷ 20."],
    )


@template("c6_energy_lost_to_friction", chapter=6, level=4, lo="6c")
def energy_lost_to_friction(rng):
    m = nice(rng, 2, 4, 5, 10)
    h = nice(rng, 2, 3, 4, 5, 8)
    v = nice(rng, 4, 5, 6, 8)
    while 0.5 * v * v >= G * h:
        h += 1
    Ep = m * G * h
    Ek = 0.5 * m * v * v
    lost = Ep - Ek
    opts, key, mis = numeric_options(rng, lost, [
        (Ep, "That is the total potential energy lost. Some of it became kinetic energy; only the REST was lost to friction."),
        (Ek, "That is the kinetic energy at the bottom, not the energy transferred to the surroundings."),
        (Ep + Ek, "You added. Energy lost to friction = Ep lost − Ek gained."),
    ], unit="J")
    return dict(
        stem=f"Fig. 1 shows a box of mass **{fmt(m)} kg** sliding from rest down a rough slope of height **{fmt(h)} m**. It reaches the bottom with a speed of **{fmt(v)} m/s**. Taking g = 10 N/kg, how much energy is transferred to the surroundings because of friction?",
        figure=sketches.slope_sketch(f"h = {fmt(h)} m", top_label=f"{fmt(m)} kg, at rest", bottom_label=f"v = {fmt(v)} m/s"),
        options=opts, key=key, misconceptions=mis,
        formula="energy lost to friction = m g h − ½ m v²",
        working=[f"Ep lost = {fmt(m)} × 10 × {fmt(h)} = {fmt(Ep)} J", f"Ek gained = ½ × {fmt(m)} × {fmt(v)}² = {fmt(Ek)} J",
                 f"energy to surroundings = {fmt(Ep)} − {fmt(Ek)} = **{fmt(lost)} J**"],
        hints=["Energy is conserved. The potential energy lost splits into two parts: what are they?",
               f"Ep lost = {fmt(Ep)} J. Ek at the bottom = ½ × {fmt(m)} × {fmt(v * v)} = {fmt(Ek)} J.",
               f"friction losses = {fmt(Ep)} − {fmt(Ek)}."],
    )


# ---------------------------------------------------------------- L5
@template("c6_braking_distance", chapter=6, level=5, lo="6d")
def braking_distance(rng):
    m = nice(rng, 800, 1000, 1200, 1500)
    v = nice(rng, 10, 15, 20, 25, 30)
    F = nice(rng, 4000, 5000, 6000, 7500, 9000)
    d = 0.5 * m * v * v / F
    opts, key, mis = numeric_options(rng, d, [
        (m * v * v / F, "You forgot the ½ in the kinetic energy."),
        (m * v / F, "You used m v instead of ½ m v². Work done by the brakes must equal the kinetic energy."),
        (0.5 * m * v / F, "You forgot to square the speed."),
    ], unit="m")
    return dict(
        stem=f"Fig. 1 shows a car of mass **{fmt(m)} kg** travelling at **{fmt(v)} m/s**. The brakes apply a constant force of **{fmt(F)} N** until the car stops. What is the braking distance?",
        figure=sketches.motion_sketch(f"v = {fmt(v)} m/s", "stops", f"braking force {fmt(F)} N", body_label=f"{fmt(m)} kg"),
        options=opts, key=key, misconceptions=mis,
        formula="work done by the braking force = kinetic energy lost: F × d = ½ m v²",
        working=[f"Ek = ½ × {fmt(m)} × {fmt(v)}² = {fmt(0.5 * m * v * v)} J", f"F × d = {fmt(0.5 * m * v * v)}",
                 f"d = {fmt(0.5 * m * v * v)} ÷ {fmt(F)} = **{fmt(d)} m**"],
        hints=["The brakes do work on the car. What energy must that work remove?",
               f"Ek = ½ × {fmt(m)} × {fmt(v * v)} = {fmt(0.5 * m * v * v)} J. Work done = F × d.",
               f"d = {fmt(0.5 * m * v * v)} ÷ {fmt(F)}."],
    )


@template("c6_power_climb_minutes", chapter=6, level=5, lo="6e")
def power_climb_minutes(rng):
    m = nice(rng, 50, 60, 70, 80)
    h = nice(rng, 30, 45, 60, 90, 120)
    t_min = nice(rng, 2, 3, 5, 6, 10)
    t = t_min * 60
    P = m * G * h / t
    opts, key, mis = numeric_options(rng, P, [
        (m * G * h / t_min, "You left the time in minutes. Power in watts needs the time in seconds (× 60)."),
        (m * G * h, "That is the work done in joules, not the power."),
        (m * h / t, "You forgot g: the work done against gravity is m g h."),
    ], unit="W")
    return dict(
        stem=f"Fig. 1 shows a hiker of mass **{fmt(m)} kg** who climbs a hill of vertical height **{fmt(h)} m** in **{t_min} minutes**. Taking g = 10 N/kg, what is the hiker's average useful power against gravity?",
        figure=sketches.slope_sketch(f"h = {fmt(h)} m", top_label=f"{fmt(m)} kg", bottom_label=f"time taken = {t_min} min"),
        options=opts, key=key, misconceptions=mis,
        formula="power = m g h ÷ t, with t in seconds",
        working=[f"work done = m g h = {fmt(m)} × 10 × {fmt(h)} = {fmt(m * G * h)} J", f"t = {t_min} min = {t} s",
                 f"power = {fmt(m * G * h)} ÷ {t} = **{fmt(P)} W**"],
        hints=["Power = energy ÷ time. Which given quantity is not yet in SI units?",
               f"Energy = m g h = {fmt(m * G * h)} J. Time = {t_min} × 60 = {t} s.",
               f"power = {fmt(m * G * h)} ÷ {t}."],
    )
