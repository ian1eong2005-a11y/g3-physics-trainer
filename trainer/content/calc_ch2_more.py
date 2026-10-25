"""Chapter 2 Kinematics: more calculation templates."""
from .. import figs, sketches
from .base import fmt, md_table, nice, numeric_options, template


# ---------------------------------------------------------------- L2
@template("c2_time_from_distance_speed", chapter=2, level=2, lo="2b")
def time_from_distance_speed(rng):
    v = nice(rng, 4, 5, 8, 12, 15, 20, 25)
    t = nice(rng, 6, 8, 12, 15, 20, 30, 40)
    d = v * t
    opts, key, mis = numeric_options(rng, t, [
        (v / d, "You divided speed by distance. time = distance ÷ speed."),
        (d * v, "You multiplied. A longer distance at the same speed takes MORE time, so divide."),
        (d / v / 2, "There is no ½ here: the speed is constant."),
    ], unit="s", sf=3)
    return dict(
        stem=f"Fig. 1 shows a cyclist moving at a constant speed of **{v} m/s**. How long does the cyclist take to travel **{d} m**?",
        figure=sketches.motion_sketch("start", "finish", f"{d} m at {v} m/s", body="box", body_label="cyclist"),
        options=opts, key=key, misconceptions=mis,
        formula="time = distance ÷ speed",
        working=["speed = distance ÷ time, so time = distance ÷ speed", f"= {d} ÷ {v}", f"= **{fmt(t)} s**"],
        hints=["Which equation links speed, distance and time?",
               "Rearrange speed = distance ÷ time to make time the subject.",
               f"{d} ÷ {v}."],
    )


@template("c2_ms_to_kmh", chapter=2, level=2, lo="2b")
def ms_to_kmh(rng):
    v = nice(rng, 5, 10, 15, 20, 25, 30, 12.5, 7.5)
    kmh = v * 3.6
    opts, key, mis = numeric_options(rng, kmh, [
        (v / 3.6, "You divided by 3.6. To go from m/s to km/h, MULTIPLY by 3.6 (km/h numbers are larger)."),
        (v * 60, "You multiplied by 60 only. 1 m/s = 3600 m per hour = 3.6 km/h."),
        (v * 1000 / 60, "Check the conversion: × 3600 s per hour ÷ 1000 m per km = × 3.6."),
    ], unit="km/h", sf=3)
    table = md_table(["vehicle", "speed / m/s"], [["bus", fmt(v)]])
    return dict(
        stem=f"The table gives the speed of a bus.\n\n{table}\n\nWhat is this speed in **km/h**?",
        options=opts, key=key, misconceptions=mis,
        formula="speed in km/h = speed in m/s × 3.6",
        working=[f"{fmt(v)} m/s = {fmt(v)} m every second = {fmt(v)} × 3600 m per hour", f"= {fmt(v * 3600)} ÷ 1000 km/h", f"= **{fmt(kmh)} km/h**"],
        hints=["In one hour there are 3600 s. How far does the bus go in that time?",
               "Change that distance from m to km by dividing by 1000.",
               f"{fmt(v)} × 3.6."],
    )
