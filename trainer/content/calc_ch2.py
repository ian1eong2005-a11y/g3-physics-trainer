"""Chapter 2 Kinematics: speed, acceleration, graphs."""
from .. import figs, sketches
from ..config import G
from .base import fmt, md_table, nice, numeric_options, template


def _axes(xmax_raw, ymax_raw):
    """Nice axis limits and steps for a graph."""
    def pick(v):
        for lim, step in ((5, 1), (10, 2), (20, 4), (25, 5), (30, 5), (40, 8), (50, 10), (60, 10), (80, 20), (100, 20), (120, 20), (150, 30), (200, 40), (250, 50), (300, 50), (400, 80), (500, 100), (600, 100), (800, 200), (1000, 200), (1500, 300), (2000, 400)):
            if v <= lim:
                return lim, step
        return v, v / 5
    (xmax, xstep), (ymax, ystep) = pick(xmax_raw), pick(ymax_raw)
    return xmax, ymax, xstep, ystep


# ---------------------------------------------------------------- L1
@template("c2_speed_from_distance_time", chapter=2, level=1, lo="2b")
def speed_from_distance_time(rng):
    v = nice(rng, 2.5, 3, 4, 5, 6, 8, 10, 12, 15, 20)
    t = nice(rng, 8, 10, 12, 15, 20, 24, 25, 30)
    d = round(v * t, 2)
    opts, key, mis = numeric_options(rng, v, [
        (t / d, "You divided time by distance. Speed = distance ÷ time."),
        (d * t, "You multiplied distance by time. Speed = distance ÷ time."),
        (d / t / 60, "You divided by 60 as well. The time is already in seconds."),
    ], unit="m/s")
    return dict(
        stem=f"Fig. 1 shows a car that travels **{fmt(d)} m in {t} s**. What is the average speed of the car?",
        figure=sketches.motion_sketch("start", "finish", f"{fmt(d)} m in {t} s"),
        options=opts, key=key, misconceptions=mis,
        formula="average speed = distance travelled ÷ time taken",
        working=["average speed = distance ÷ time", f"= {fmt(d)} ÷ {t}", f"= **{fmt(v)} m/s**"],
        hints=["Which formula links distance, time and average speed?",
               f"Distance = {fmt(d)} m and time = {t} s. Speed is how many metres are covered each second.",
               f"average speed = {fmt(d)} ÷ {t}."],
    )


@template("c2_acceleration_from_speeds", chapter=2, level=1, lo="2c")
def acceleration_from_speeds(rng):
    u = nice(rng, 0, 2, 4, 5, 6, 8, 10, 12)
    a = nice(rng, 1.5, 2, 2.5, 3, 4, 5)
    t = nice(rng, 4, 5, 6, 8, 10)
    v = u + a * t
    wrongs = [((v + u) / t, "You ADDED the speeds. Acceleration uses the CHANGE in speed, v − u.")]
    if u:
        wrongs.append((v / t, "You used the final speed instead of the change in speed, v − u."))
    else:
        wrongs.append(((v - u) * t, "You multiplied by time. Acceleration = change in speed ÷ time."))
    wrongs.append((t / (v - u), "You divided time by the change in speed, the wrong way round."))
    opts, key, mis = numeric_options(rng, a, wrongs, unit="m/s²")
    return dict(
        stem=f"Fig. 1 shows a car whose speed increases uniformly from **{fmt(u)} m/s to {fmt(v)} m/s in {fmt(t)} s**. What is the acceleration of the car?",
        figure=sketches.motion_sketch(f"u = {fmt(u)} m/s", f"v = {fmt(v)} m/s", f"t = {fmt(t)} s"),
        options=opts, key=key, misconceptions=mis,
        formula="acceleration = change in velocity ÷ time taken = (v − u) ÷ t",
        working=["acceleration = (v − u) ÷ t", f"= ({fmt(v)} − {fmt(u)}) ÷ {fmt(t)}", f"= **{fmt(a)} m/s²**"],
        hints=["Acceleration is the rate of change of velocity. Which formula uses the initial speed, final speed and time?",
               f"Change in speed = final − initial = {fmt(v)} − {fmt(u)} = {fmt(v - u)} m/s. This change took {fmt(t)} s.",
               f"a = {fmt(v - u)} ÷ {fmt(t)}."],
    )


@template("c2_distance_from_speed_time", chapter=2, level=1, lo="2b")
def distance_from_speed_time(rng):
    v = nice(rng, 1.5, 2, 4, 5, 8, 12, 15, 25, 30)
    t = nice(rng, 6, 8, 12, 15, 20, 30, 40, 60)
    d = v * t
    opts, key, mis = numeric_options(rng, d, [
        (v / t, "You divided speed by time. Distance = speed × time."),
        (t / v, "You divided time by speed. Distance = speed × time."),
        (v + t, "You added the numbers. Distance = speed × time."),
    ], unit="m")
    return dict(
        stem=f"Fig. 1 shows a car travelling at a constant speed of **{fmt(v)} m/s for {t} s**. What distance does it travel in this time?",
        figure=sketches.motion_sketch(f"{fmt(v)} m/s", f"{fmt(v)} m/s", f"t = {t} s,  distance = ?"),
        options=opts, key=key, misconceptions=mis,
        formula="distance = speed × time",
        working=["distance = speed × time", f"= {fmt(v)} × {t}", f"= **{fmt(d)} m**"],
        hints=["Speed tells you how many metres are covered EACH second. How do you turn that into a distance for several seconds?",
               f"Every second the car covers {fmt(v)} m. There are {t} seconds.",
               f"distance = {fmt(v)} × {t}."],
    )


# ---------------------------------------------------------------- L2
@template("c2_kmh_distance", chapter=2, level=2, lo="2b")
def kmh_distance(rng):
    v_kmh = nice(rng, 36, 54, 72, 90, 108)
    t = nice(rng, 5, 10, 15, 20, 30)
    v = v_kmh / 3.6
    d = v * t
    opts, key, mis = numeric_options(rng, d, [
        (v_kmh * t, f"You used {v_kmh} km/h as if it were {v_kmh} m/s. Convert km/h to m/s first: × 1000 ÷ 3600."),
        (v_kmh * t / 60, "You divided by 60 only. 1 km/h = 1000 m ÷ 3600 s."),
        (v, "That is the speed in m/s. You still need to multiply by the time."),
    ], unit="m")
    return dict(
        stem=f"Fig. 1 shows a train travelling at a constant speed of **{v_kmh} km/h**. How far does it travel in **{t} s**?",
        figure=sketches.motion_sketch(f"{v_kmh} km/h", f"{v_kmh} km/h", f"t = {t} s,  distance = ?", body="box"),
        options=opts, key=key, misconceptions=mis,
        formula="distance = speed × time, with speed in m/s (km/h × 1000 ÷ 3600)",
        working=[f"{v_kmh} km/h = {v_kmh} × 1000 ÷ 3600 = {fmt(v)} m/s", f"distance = {fmt(v)} × {t}", f"= **{fmt(d)} m**"],
        hints=["The time is in seconds but the speed is in km/h. What must you do before using distance = speed × time?",
               f"1 km = 1000 m and 1 h = 3600 s, so {v_kmh} km/h = {v_kmh} × 1000 ÷ 3600 m/s = {fmt(v)} m/s.",
               f"distance = {fmt(v)} × {t}."],
    )


# ---------------------------------------------------------------- L3
@template("c2_distance_after_acceleration", chapter=2, level=3, lo="2h")
def distance_after_acceleration(rng):
    u = nice(rng, 0, 0, 2, 4, 5, 6, 8, 10)
    a = nice(rng, 1, 1.5, 2, 2.5, 3, 4)
    t = nice(rng, 4, 5, 6, 8, 10)
    v = u + a * t
    s = 0.5 * (u + v) * t
    wrongs = [(v * t, "You used the final speed for the whole time. The speed was rising, so use the AVERAGE speed, (u + v) ÷ 2.")]
    if u:
        wrongs.append((u * t, "You used the initial speed for the whole time. The car was speeding up."))
        wrongs.append((0.5 * a * t * t, "You found only the extra distance due to the acceleration and forgot the u × t part."))
    else:
        wrongs.append((v, "That is the final speed, not the distance."))
        wrongs.append((a * t * t, "You forgot the ½. Distance = ½ × final speed × time when starting from rest."))
    opts, key, mis = numeric_options(rng, s, wrongs, unit="m")
    return dict(
        stem=f"Fig. 1 shows a car that accelerates uniformly from **{fmt(u)} m/s** at **{fmt(a)} m/s²** for **{t} s**. How far does it travel during this time?",
        figure=sketches.motion_sketch(f"u = {fmt(u)} m/s", f"after {t} s", f"a = {fmt(a)} m/s²,  distance = ?"),
        options=opts, key=key, misconceptions=mis,
        formula="v = u + at, then distance = average speed × time = ½(u + v) × t",
        working=[f"final speed v = u + at = {fmt(u)} + {fmt(a)} × {t} = {fmt(v)} m/s",
                 f"average speed = ({fmt(u)} + {fmt(v)}) ÷ 2 = {fmt((u + v) / 2)} m/s",
                 f"distance = {fmt((u + v) / 2)} × {t} = **{fmt(s)} m**"],
        hints=["Two steps. First find the final speed from the acceleration. Which formula gives v from u, a and t?",
               f"v = {fmt(u)} + {fmt(a)} × {t} = {fmt(v)} m/s. Now, because the speed changed steadily, use the AVERAGE of u and v for the distance.",
               f"distance = ½ × ({fmt(u)} + {fmt(v)}) × {t}. (This is the area under the speed–time graph.)"],
    )


@template("c2_gradient_speed_time_graph", chapter=2, level=3, lo="2e")
def gradient_speed_time_graph(rng):
    u = nice(rng, 0, 0, 4, 5, 10)
    a = nice(rng, 1, 1.5, 2, 2.5, 3, 4)
    t = nice(rng, 4, 5, 8, 10)
    v = u + a * t
    xmax, ymax, xstep, ystep = _axes(t, v)
    wrongs = [((v + u) / t, "You added the speeds. Gradient = change in speed ÷ time, so use v − u."),
              (0.5 * (u + v) * t, "That is the AREA under the graph, which gives the distance, not the acceleration.")]
    if u:
        wrongs.append((v / t, "You used the final speed instead of the change in speed. The graph does not start at zero."))
    else:
        wrongs.append((t / v, "You divided time by speed, the wrong way round for a gradient."))
    opts, key, mis = numeric_options(rng, a, wrongs, unit="m/s²")
    return dict(
        stem="Fig. 1 shows the speed–time graph of a trolley. What is the acceleration of the trolley?",
        figure=figs.graph([(0, u), (t, v)], xmax, ymax, xstep, ystep),
        options=opts, key=key, misconceptions=mis,
        formula="acceleration = gradient of the speed–time graph = (v − u) ÷ t",
        working=[f"from the graph: speed rises from {fmt(u)} m/s to {fmt(v)} m/s in {t} s",
                 f"acceleration = gradient = ({fmt(v)} − {fmt(u)}) ÷ {t}", f"= **{fmt(a)} m/s²**"],
        hints=["On a speed–time graph, what does the gradient (slope) represent?",
               f"Read two points: at t = 0 the speed is {fmt(u)} m/s; at t = {t} s it is {fmt(v)} m/s.",
               f"gradient = rise ÷ run = ({fmt(v)} − {fmt(u)}) ÷ {t}."],
    )


@template("c2_triangle_area_distance", chapter=2, level=3, lo="2h")
def triangle_area_distance(rng):
    vmax = nice(rng, 4, 6, 8, 10, 12, 15, 20)
    t1 = nice(rng, 4, 5, 6, 8, 10)
    t2 = t1 + nice(rng, 2, 4, 5, 6, 10)
    d = 0.5 * vmax * t2
    xmax, ymax, xstep, ystep = _axes(t2, vmax)
    opts, key, mis = numeric_options(rng, d, [
        (vmax * t2, "That is the area of the whole rectangle. The graph is a triangle, so use ½ × base × height."),
        (0.5 * vmax * t1, "That is only the distance during the speeding-up part. Include the slowing-down part too."),
        (vmax / t1, "That is the acceleration (the gradient), not the distance."),
    ], unit="m")
    return dict(
        stem="Fig. 1 shows the speed–time graph of a lift moving between two floors. What is the total distance travelled by the lift?",
        figure=figs.graph([(0, 0), (t1, vmax), (t2, 0)], xmax, ymax, xstep, ystep, shade=(0, t2)),
        options=opts, key=key, misconceptions=mis,
        formula="distance = area under the speed–time graph = ½ × base × height for a triangle",
        working=["distance = area under the graph (a triangle)", f"= ½ × {t2} × {fmt(vmax)}", f"= **{fmt(d)} m**"],
        hints=["What does the area under a speed–time graph represent?",
               f"The shaded shape is a triangle with base {t2} s (the whole journey) and height {fmt(vmax)} m/s.",
               f"area = ½ × {t2} × {fmt(vmax)}."],
    )


# ---------------------------------------------------------------- L4
def _trapezium(rng):
    vmax = nice(rng, 8, 10, 12, 15, 16, 20, 24)
    t1 = nice(rng, 4, 5, 6, 8)
    t2 = t1 + nice(rng, 10, 12, 15, 20)
    t3 = t2 + nice(rng, 4, 5, 6, 8, 10)
    area = 0.5 * (t3 + (t2 - t1)) * vmax
    return vmax, t1, t2, t3, area


@template("c2_trapezium_distance", chapter=2, level=4, lo="2h")
def trapezium_distance(rng):
    vmax, t1, t2, t3, area = _trapezium(rng)
    xmax, ymax, xstep, ystep = _axes(t3, vmax)
    opts, key, mis = numeric_options(rng, area, [
        (vmax * t3, "That is the full rectangle. The car was not at top speed the whole time: use the trapezium area."),
        (0.5 * vmax * t3, "That is a triangle over the whole time. Only the first and last sections are triangles."),
        (vmax * (t2 - t1), "That is only the constant-speed section. Add the two triangles at the start and end."),
    ], unit="m")
    return dict(
        stem="Fig. 1 shows the speed–time graph of a car. What is the total distance travelled by the car?",
        figure=figs.graph([(0, 0), (t1, vmax), (t2, vmax), (t3, 0)], xmax, ymax, xstep, ystep, shade=(0, t3)),
        options=opts, key=key, misconceptions=mis,
        formula="distance = area under the speed–time graph = ½ × (sum of parallel sides) × height for a trapezium",
        working=["distance = area under the graph (a trapezium)",
                 f"parallel sides: {t3} s (bottom) and {t2 - t1} s (top); height {fmt(vmax)} m/s",
                 f"= ½ × ({t3} + {t2 - t1}) × {fmt(vmax)} = **{fmt(area)} m**"],
        hints=["Distance is the area under the graph. What shape is the shaded area, and how do you find its area?",
               f"Split it into a triangle (0 to {t1} s), a rectangle ({t1} to {t2} s) and a triangle ({t2} to {t3} s), or use the trapezium rule with parallel sides {t3} s and {t2 - t1} s.",
               f"area = ½ × ({t3} + {t2 - t1}) × {fmt(vmax)}."],
    )


@template("c2_average_speed_from_graph", chapter=2, level=4, lo="2h")
def average_speed_from_graph(rng):
    vmax, t1, t2, t3, area = _trapezium(rng)
    avg = area / t3
    xmax, ymax, xstep, ystep = _axes(t3, vmax)
    opts, key, mis = numeric_options(rng, avg, [
        (vmax / 2, "You halved the top speed. That only works for a single triangle, not this shape."),
        (vmax, "That is the maximum speed. The average over the whole journey is lower because of the speeding up and slowing down."),
        (area / (t2 - t1), "You divided the total distance by the constant-speed time only. Use the TOTAL time."),
    ], unit="m/s")
    return dict(
        stem="Fig. 1 shows the speed–time graph of a bus between two stops. What is the average speed of the bus for the whole journey?",
        figure=figs.graph([(0, 0), (t1, vmax), (t2, vmax), (t3, 0)], xmax, ymax, xstep, ystep, shade=(0, t3)),
        options=opts, key=key, misconceptions=mis,
        formula="average speed = total distance ÷ total time, with total distance = area under the graph",
        working=[f"total distance = area = ½ × ({t3} + {t2 - t1}) × {fmt(vmax)} = {fmt(area)} m",
                 f"average speed = {fmt(area)} ÷ {t3}", f"= **{fmt(avg)} m/s**"],
        hints=["Average speed = total distance ÷ total time. How do you get the total distance from this graph?",
               f"Area of the trapezium = ½ × ({t3} + {t2 - t1}) × {fmt(vmax)} = {fmt(area)} m. The total time is {t3} s.",
               f"average speed = {fmt(area)} ÷ {t3}."],
    )


@template("c2_deceleration_from_graph", chapter=2, level=4, lo="2e")
def deceleration_from_graph(rng):
    vmax, t1, t2, t3, area = _trapezium(rng)
    dec = vmax / (t3 - t2)
    xmax, ymax, xstep, ystep = _axes(t3, vmax)
    opts, key, mis = numeric_options(rng, dec, [
        (vmax / t3, "You divided by the total time. The slowing down only happens in the last section."),
        (vmax / t1, "That is the gradient of the FIRST section, the acceleration at the start."),
        (0.5 * vmax * (t3 - t2), "That is the area of the last section, which is the distance travelled while braking."),
    ], unit="m/s²")
    return dict(
        stem=f"Fig. 1 shows the speed–time graph of a car. What is the deceleration of the car between **t = {t2} s and t = {t3} s**?",
        figure=figs.graph([(0, 0), (t1, vmax), (t2, vmax), (t3, 0)], xmax, ymax, xstep, ystep),
        options=opts, key=key, misconceptions=mis,
        formula="deceleration = magnitude of the gradient = change in speed ÷ time for that section",
        working=[f"between {t2} s and {t3} s the speed falls from {fmt(vmax)} m/s to 0",
                 f"deceleration = {fmt(vmax)} ÷ ({t3} − {t2})", f"= **{fmt(dec)} m/s²**"],
        hints=["Deceleration is the gradient of the graph in the section where the speed is falling. Which section is that?",
               f"In that section the speed drops by {fmt(vmax)} m/s over {t3 - t2} s.",
               f"deceleration = {fmt(vmax)} ÷ {t3 - t2}."],
    )


@template("c2_free_fall_table", chapter=2, level=4, lo="2i")
def free_fall_table(rng):
    dt = nice(rng, 0.5, 1.0, 2.0)
    times = [0, dt, 2 * dt, 3 * dt]
    t_end = times[-1]
    speeds = [G * t for t in times]
    d = 0.5 * G * t_end ** 2
    opts, key, mis = numeric_options(rng, d, [
        (G * t_end * t_end, "You multiplied the final speed by the time and forgot the ½. The stone started from rest, so use the AVERAGE speed."),
        (G, "That is the acceleration of free fall, not a distance."),
        (G * t_end, "That is the final speed, not the distance fallen."),
    ], unit="m")
    table = md_table(["time / s", "speed / m/s"], [[fmt(t), fmt(v)] for t, v in zip(times, speeds)])
    return dict(
        stem=f"The table shows the speed of a stone at different times after it is dropped from rest. Air resistance is negligible.\n\n{table}\n\nHow far does the stone fall in the first **{fmt(t_end)} s**?",
        options=opts, key=key, misconceptions=mis,
        formula="distance = average speed × time = ½ × (0 + final speed) × time",
        working=[f"speed increases steadily (acceleration = {fmt(G)} m/s²), so the speed–time graph is a straight line from the origin",
                 f"distance = area under the graph = ½ × {fmt(G * t_end)} × {fmt(t_end)}", f"= **{fmt(d)} m**"],
        hints=["The speed is changing, so you cannot just multiply one speed by the time. What is the average speed between 0 and the end?",
               f"The speed rises steadily from 0 to {fmt(G * t_end)} m/s, so the average speed is ½ × {fmt(G * t_end)} = {fmt(G * t_end / 2)} m/s.",
               f"distance = {fmt(G * t_end / 2)} × {fmt(t_end)}."],
    )


# ---------------------------------------------------------------- L5
@template("c2_two_stage_average_speed", chapter=2, level=5, lo="2b")
def two_stage_average_speed(rng):
    v1 = nice(rng, 4, 5, 8, 10, 20)
    t1 = nice(rng, 10, 20, 30, 50)
    v2 = nice(rng, 2, 2.5, 4, 5, 12, 15)
    if v2 == v1:
        v2 = v1 * 2
    t2 = nice(rng, 10, 20, 30, 40)
    d1, d2 = v1 * t1, v2 * t2
    avg = (d1 + d2) / (t1 + t2)
    opts, key, mis = numeric_options(rng, avg, [
        ((v1 + v2) / 2, "You averaged the two speeds. That only works if the two parts take the same TIME. Use total distance ÷ total time."),
        ((d1 + d2) / t1, "You divided the total distance by the first time only."),
        (max(v1, v2), "That is the faster of the two speeds, not the average."),
    ], unit="m/s")
    return dict(
        stem=f"Fig. 1 shows the journey of a delivery robot. It travels **{fmt(d1)} m at a constant speed of {fmt(v1)} m/s**, then immediately a further **{fmt(d2)} m at {fmt(v2)} m/s**. What is its average speed for the whole journey?",
        figure=sketches.journey_sketch([(f"{fmt(d1)} m", f"{fmt(v1)} m/s"), (f"{fmt(d2)} m", f"{fmt(v2)} m/s")]),
        options=opts, key=key, misconceptions=mis,
        formula="average speed = total distance ÷ total time (find the time for each part first)",
        working=[f"time for part 1 = {fmt(d1)} ÷ {fmt(v1)} = {fmt(t1)} s; time for part 2 = {fmt(d2)} ÷ {fmt(v2)} = {fmt(t2)} s",
                 f"total distance = {fmt(d1 + d2)} m; total time = {fmt(t1 + t2)} s",
                 f"average speed = {fmt(d1 + d2)} ÷ {fmt(t1 + t2)} = **{fmt(avg)} m/s**"],
        hints=["Average speed is NOT the average of the two speeds. What is the definition of average speed?",
               f"Find the time for each part: {fmt(d1)} ÷ {fmt(v1)} = {fmt(t1)} s and {fmt(d2)} ÷ {fmt(v2)} = {fmt(t2)} s.",
               f"average speed = ({fmt(d1)} + {fmt(d2)}) ÷ ({fmt(t1)} + {fmt(t2)})."],
    )


@template("c2_distance_time_graph_speed", chapter=2, level=5, lo="2f")
def distance_time_graph_speed(rng):
    v1 = nice(rng, 2, 4, 5)
    t1 = nice(rng, 10, 20)
    d1 = v1 * t1
    t2 = t1 + nice(rng, 10, 20)
    v3 = nice(rng, 1.5, 2.5, 3, 6, 8)
    if v3 == v1:
        v3 = v1 * 1.5
    dt3 = nice(rng, 10, 20)
    t3 = t2 + dt3
    d_tot = d1 + v3 * dt3
    xmax, ymax, xstep, ystep = _axes(t3, d_tot)
    opts, key, mis = numeric_options(rng, v3, [
        (d_tot / t3, "That is the average speed for the WHOLE journey. The question asks about the last section only."),
        (d_tot / dt3, "You used the total distance. In the last section the distance increases from " + f"{fmt(d1)} m to {fmt(d_tot)} m, so use the change."),
        (v1, "That is the speed in the FIRST section (its gradient)."),
    ], unit="m/s")
    return dict(
        stem=f"Fig. 1 shows the distance–time graph of a jogger. What is the speed of the jogger between **t = {t2} s and t = {t3} s**?",
        figure=figs.graph([(0, 0), (t1, d1), (t2, d1), (t3, d_tot)], xmax, ymax, xstep, ystep, ylabel="distance / m"),
        options=opts, key=key, misconceptions=mis,
        formula="speed = gradient of the distance–time graph = change in distance ÷ change in time",
        working=[f"between {t2} s and {t3} s the distance changes from {fmt(d1)} m to {fmt(d_tot)} m",
                 f"speed = ({fmt(d_tot)} − {fmt(d1)}) ÷ ({t3} − {t2})", f"= **{fmt(v3)} m/s**"],
        hints=["On a distance–time graph, what does the gradient of a section give you?",
               f"Look only at the last section: at t = {t2} s the distance is {fmt(d1)} m, at t = {t3} s it is {fmt(d_tot)} m.",
               f"speed = ({fmt(d_tot)} − {fmt(d1)}) ÷ ({t3} − {t2})."],
    )


@template("c2_stopping_distance_graph", chapter=2, level=5, lo="2h")
def stopping_distance_graph(rng):
    v = nice(rng, 10, 12, 15, 20, 24, 30)
    tr = nice(rng, 0.5, 1.0, 1.5)
    tb = nice(rng, 2, 2.5, 3, 4, 5)
    t_stop = tr + tb
    thinking, braking = v * tr, 0.5 * v * tb
    total = thinking + braking
    xmax, ymax, xstep, ystep = _axes(t_stop, v)
    opts, key, mis = numeric_options(rng, total, [
        (braking, "That is only the braking distance. During the driver's reaction time the car keeps moving: add the thinking distance."),
        (v * t_stop, "That is the full rectangle. The car slows down during braking, so the second part is a triangle."),
        (0.5 * v * t_stop, "You treated the whole graph as one triangle. The first part is a rectangle (constant speed)."),
    ], unit="m")
    return dict(
        stem=f"Fig. 1 shows the speed–time graph of a car from the moment the driver sees a hazard until the car stops. The driver's reaction time is **{fmt(tr)} s**. What is the total stopping distance of the car?",
        figure=figs.graph([(0, v), (tr, v), (t_stop, 0)], xmax, ymax, xstep, ystep, shade=(0, t_stop)),
        options=opts, key=key, misconceptions=mis,
        formula="stopping distance = thinking distance (rectangle) + braking distance (triangle) = total area under the graph",
        working=[f"thinking distance = {fmt(v)} × {fmt(tr)} = {fmt(thinking)} m",
                 f"braking distance = ½ × {fmt(v)} × {fmt(tb)} = {fmt(braking)} m",
                 f"stopping distance = {fmt(thinking)} + {fmt(braking)} = **{fmt(total)} m**"],
        hints=["The total distance is the whole area under the graph. The shape is made of two parts: what are they?",
               f"Rectangle: {fmt(v)} m/s × {fmt(tr)} s (thinking distance). Triangle: ½ × {fmt(v)} × {fmt(tb)} (braking distance).",
               f"total = {fmt(v)} × {fmt(tr)} + ½ × {fmt(v)} × {fmt(tb)}."],
    )
