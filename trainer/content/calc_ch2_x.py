"""Chapter 2 Kinematics: extra calculation templates (tripling the bank)."""
from .. import figs, sketches
from .base import calc_q, fmt, md_table, nice, template


def _vt(pts, ymax=None, shade=None, ylabel="speed / m/s", xlabel="time / s"):
    xmax = max(p[0] for p in pts)
    ymax = ymax or max(p[1] for p in pts)
    xstep = next(s for s in (1, 2, 5, 10, 20, 50) if xmax / s <= 8)
    ystep = next(s for s in (1, 2, 5, 10, 20, 50, 100, 200) if ymax / s <= 6)
    ytop = -(-ymax // ystep) * ystep
    xtop = -(-xmax // xstep) * xstep
    return figs.graph(pts, xtop, ytop, xstep, ystep, xlabel=xlabel, ylabel=ylabel, shade=shade)


# ---------------------------------------------------------------- L1
@template("c2_speed_runner", chapter=2, level=1, lo="2b")
def speed_runner(rng):
    v = nice(rng, 4, 5, 8, 10)
    d = nice(rng, 100, 200, 400, 800)
    t = d / v
    return calc_q(rng, f"Fig. 1 shows a runner who covers **{d} m** in **{fmt(t)} s**. What is her average speed?", v, [
        (t / d, "You divided time by distance. Speed = distance ÷ time."),
        (d * t, "You multiplied. Speed = distance ÷ time."),
        (d / t / 2, "There is no ½ in average speed = distance ÷ time."),
    ], "m/s", "average speed = distance ÷ time", ["speed = d ÷ t", f"= {d} ÷ {fmt(t)}", f"= **{fmt(v)} m/s**"],
        ["Which formula gives average speed?", "Divide the distance by the time.", f"{d} ÷ {fmt(t)}."],
        figure=sketches.motion_sketch("start", "finish", f"{d} m in {fmt(t)} s", body="box", body_label="runner"))


@template("c2_distance_walker", chapter=2, level=1, lo="2b")
def distance_walker(rng):
    v = nice(rng, 1.2, 1.5, 2, 2.5)
    t = nice(rng, 60, 120, 300, 600)
    d = v * t
    return calc_q(rng, f"Fig. 1 shows a man walking at a steady **{fmt(v)} m/s** for **{t} s**. How far does he walk?", d, [
        (t / v, "You divided. distance = speed × time."),
        (v / t, "You divided. distance = speed × time."),
        (d / 60, "The time is already in seconds; no conversion is needed."),
    ], "m", "distance = speed × time", ["d = v × t", f"= {fmt(v)} × {t}", f"= **{fmt(d)} m**"],
        ["Rearrange speed = distance ÷ time.", "distance = speed × time.", f"{fmt(v)} × {t}."],
        figure=sketches.motion_sketch("", "", f"{fmt(v)} m/s for {t} s", body="box", body_label="walker"))


@template("c2_accel_from_rest", chapter=2, level=1, lo="2c")
def accel_from_rest(rng):
    v = nice(rng, 12, 18, 24, 30)
    t = nice(rng, 3, 4, 6)
    a = v / t
    return calc_q(rng, f"Fig. 1 shows a motorbike that starts from rest and reaches **{v} m/s** in **{t} s**. What is its acceleration?", a, [
        (v * t, "You multiplied. a = change in velocity ÷ time."),
        (t / v, "You divided the wrong way round."),
        (v, "That is the change in velocity; divide it by the time."),
    ], "m/s²", "acceleration = change in velocity ÷ time", ["a = (v − u) ÷ t", f"= ({v} − 0) ÷ {t}", f"= **{fmt(a)} m/s²**"],
        ["Starting from rest means u = 0.", "Acceleration = change in velocity ÷ time.", f"{v} ÷ {t}."],
        figure=sketches.motion_sketch("0 m/s", f"{v} m/s", f"t = {t} s", body="car"))


@template("c2_speed_cm_s", chapter=2, level=1, lo="2b")
def speed_cm_s(rng):
    d = nice(rng, 24, 30, 36, 45, 60)
    t = nice(rng, 60, 120, 150)
    v = d / t
    return calc_q(rng, f"Fig. 1 shows a snail that crawls **{d} cm** in **{t} s**. What is its average speed in cm/s?", v, [
        (t / d, "Speed = distance ÷ time, not time ÷ distance."),
        (d * t, "You multiplied. Divide distance by time."),
        (v / 100, "You converted to m/s; the question asks for cm/s."),
    ], "cm/s", "average speed = distance ÷ time", ["speed = d ÷ t", f"= {d} ÷ {t}", f"= **{fmt(v)} cm/s**"],
        ["Keep the distance in cm.", "Speed = distance ÷ time.", f"{d} ÷ {t}."],
        figure=sketches.motion_sketch("", "", f"{d} cm in {t} s", body="box", body_label="snail"))


@template("c2_simple_deceleration", chapter=2, level=1, lo="2c")
def simple_deceleration(rng):
    u = nice(rng, 15, 20, 24, 30)
    t = nice(rng, 3, 4, 5, 6)
    a = u / t
    return calc_q(rng, f"Fig. 1 shows a car travelling at **{u} m/s** that brakes and stops uniformly in **{t} s**. What is the size of its deceleration?", a, [
        (u * t, "You multiplied. Deceleration = change in speed ÷ time."),
        (t / u, "You divided the wrong way round."),
        (u / t / 2, "There is no ½ here: a = Δv ÷ t."),
    ], "m/s²", "deceleration = decrease in speed ÷ time", ["a = (0 − u) ÷ t", f"= −{u} ÷ {t}", f"deceleration = **{fmt(a)} m/s²**"],
        ["The final speed is 0.", "Deceleration = decrease in speed ÷ time.", f"{u} ÷ {t}."],
        figure=sketches.motion_sketch(f"{u} m/s", "0 m/s", f"stops in {t} s", body="car"))


@template("c2_velocity_gain", chapter=2, level=1, lo="2c")
def velocity_gain(rng):
    a = nice(rng, 2, 2.5, 3, 4)
    t = nice(rng, 4, 5, 6, 8)
    dv = a * t
    return calc_q(rng, f"Fig. 1 shows a trolley accelerating uniformly at **{fmt(a)} m/s²** for **{t} s**. By how much does its velocity increase?", dv, [
        (a / t, "Rearrange a = Δv ÷ t to get Δv = a × t."),
        (t / a, "Δv = a × t."),
        (a * t * t, "There is no t² here: Δv = a × t."),
    ], "m/s", "change in velocity = acceleration × time", ["Δv = a × t", f"= {fmt(a)} × {t}", f"= **{fmt(dv)} m/s**"],
        ["a = Δv ÷ t.", "Rearrange for Δv.", f"{fmt(a)} × {t}."],
        figure=sketches.motion_sketch("u", "u + Δv", f"a = {fmt(a)} m/s² for {t} s", body="box", body_label="trolley"))


# ---------------------------------------------------------------- L3
@template("c2_area_rectangle_vt", chapter=2, level=3, lo="2h")
def area_rectangle_vt(rng):
    v = nice(rng, 8, 12, 15, 20)
    T = nice(rng, 10, 20, 25, 30)
    d = v * T
    return calc_q(rng, "Fig. 1 shows the speed–time graph of a cyclist. What distance does she travel in this time?", d, [
        (v / T, "Distance is the AREA under the graph, not the gradient."),
        (v * T / 2, "The graph is a rectangle, not a triangle: no ½."),
        (v + T, "Multiply speed by time to get the area."),
    ], "m", "distance = area under speed–time graph", [f"area = {v} × {T}", f"= **{fmt(d)} m**"],
        ["What does the area under a speed–time graph represent?", "The shape is a rectangle.", f"{v} × {T}."],
        figure=_vt([(0, v), (T, v)], ymax=v * 1.5, shade=(0, T)))


@template("c2_final_speed", chapter=2, level=3, lo="2c")
def final_speed(rng):
    u = nice(rng, 5, 8, 10)
    a = nice(rng, 1.5, 2, 3)
    t = nice(rng, 4, 5, 6)
    v = u + a * t
    return calc_q(rng, f"Fig. 1 shows a car moving at **{u} m/s** that accelerates uniformly at **{fmt(a)} m/s²** for **{t} s**. What is its final speed?", v, [
        (a * t, "That is the GAIN in speed. Add it to the starting speed."),
        (u * a * t, "Final speed = initial speed + a × t."),
        (u + a / t, "The gain in speed is a × t, not a ÷ t."),
    ], "m/s", "final speed = initial speed + acceleration × time", ["v = u + a t", f"= {u} + {fmt(a)} × {t}", f"= **{fmt(v)} m/s**"],
        ["How much speed does it gain?", "Gain = a × t.", "Add the gain to the initial speed."],
        figure=sketches.motion_sketch(f"{u} m/s", "v = ?", f"a = {fmt(a)} m/s², t = {t} s", body="car"))


@template("c2_gradient_dt_line", chapter=2, level=3, lo="2e")
def gradient_dt_line(rng):
    v = nice(rng, 2, 3, 4, 5, 6)
    T = nice(rng, 10, 20, 25, 40)
    D = v * T
    return calc_q(rng, "Fig. 1 shows the distance–time graph of a toy car. What is its speed?", v, [
        (D * T, "Speed is the GRADIENT of a distance–time graph: distance ÷ time."),
        (T / D, "Gradient = rise ÷ run = distance ÷ time."),
        (D, "That is the distance travelled; divide by the time."),
    ], "m/s", "speed = gradient of distance–time graph", [f"gradient = {D} ÷ {T}", f"= **{fmt(v)} m/s**"],
        ["What does the gradient of a distance–time graph give?", "Pick two points on the line far apart.", f"{D} ÷ {T}."],
        figure=_vt([(0, 0), (T, D)], ylabel="distance / m"))


@template("c2_time_to_reach_speed", chapter=2, level=3, lo="2c")
def time_to_reach_speed(rng):
    u = nice(rng, 4, 6, 10)
    a = nice(rng, 2, 2.5, 4)
    t = nice(rng, 3, 4, 6, 8)
    v = u + a * t
    return calc_q(rng, f"Fig. 1 shows a train that speeds up uniformly from **{u} m/s** to **{fmt(v)} m/s** with an acceleration of **{fmt(a)} m/s²**. How long does this take?", t, [
        (v / a, "Use the CHANGE in velocity: (v − u) ÷ a."),
        ((v - u) * a, "t = (v − u) ÷ a, not × a."),
        (a / (v - u), "t = (v − u) ÷ a."),
    ], "s", "time = change in velocity ÷ acceleration", ["t = (v − u) ÷ a", f"= ({fmt(v)} − {u}) ÷ {fmt(a)}", f"= **{fmt(t)} s**"],
        ["Find the change in velocity first.", "a = Δv ÷ t, so t = Δv ÷ a.", f"({fmt(v)} − {u}) ÷ {fmt(a)}."],
        figure=sketches.motion_sketch(f"{u} m/s", f"{fmt(v)} m/s", f"a = {fmt(a)} m/s²", body="box", body_label="train"))


@template("c2_free_fall_speed", chapter=2, level=3, lo="2i")
def free_fall_speed(rng):
    t = nice(rng, 1.5, 2, 2.5, 3)
    v = 10 * t
    return calc_q(rng, f"A stone is dropped from rest and falls freely (air resistance negligible, acceleration of free fall 10 m/s²). Fig. 1 shows its speed–time graph. What is its speed after **{fmt(t)} s**?", v, [
        (10 / t, "v = a × t, not a ÷ t."),
        (5 * t * t, "That is the distance fallen, not the speed."),
        (10 * t * t, "v = a × t; there is no t²."),
    ], "m/s", "v = u + a t with u = 0, a = 10 m/s²", ["v = 0 + 10 × t", f"= 10 × {fmt(t)}", f"= **{fmt(v)} m/s**"],
        ["Free fall near the Earth has a constant acceleration of about 10 m/s².", "It starts from rest.", f"10 × {fmt(t)}."],
        figure=_vt([(0, 0), (4, 40)]))


@template("c2_average_two_parts", chapter=2, level=3, lo="2b")
def average_two_parts(rng):
    d1, t1 = nice(rng, (300, 60), (240, 40), (500, 50), (180, 30))
    d2, t2 = nice(rng, (200, 40), (120, 60), (300, 100), (100, 20))
    v = (d1 + d2) / (t1 + t2)
    return calc_q(rng, f"Fig. 1 shows a journey in two parts: **{d1} m in {t1} s**, then **{d2} m in {t2} s**. What is the average speed for the whole journey?", v, [
        ((d1 / t1 + d2 / t2) / 2, "You averaged the two speeds. Use total distance ÷ total time."),
        (d1 / t1, "That is the speed for the first part only."),
        ((d1 + d2) / t1, "Divide by the TOTAL time."),
    ], "m/s", "average speed = total distance ÷ total time",
        [f"total distance = {d1} + {d2} = {d1 + d2} m", f"total time = {t1} + {t2} = {t1 + t2} s", f"average speed = **{fmt(v)} m/s**"],
        ["Average speed uses totals, not the mean of the speeds.", "Add the distances and add the times.", "Divide total distance by total time."],
        figure=sketches.journey_sketch([(f"{d1} m", f"{t1} s"), (f"{d2} m", f"{t2} s")]))


# ---------------------------------------------------------------- L4
@template("c2_constant_stage_distance", chapter=2, level=4, lo="2h")
def constant_stage_distance(rng):
    V = nice(rng, 10, 12, 15, 20)
    T1 = nice(rng, 4, 5, 6)
    T2 = T1 + nice(rng, 10, 15, 20)
    d = V * (T2 - T1)
    return calc_q(rng, f"Fig. 1 shows the speed–time graph of a car. What distance does it travel while moving at constant speed (from t = {T1} s to t = {T2} s)?", d, [
        (V * T2, "Use only the time at constant speed, not the whole time from t = 0."),
        (V * T2 - 0.5 * V * T1, "That is the total distance; the question asks for the constant-speed part only."),
        (V * (T2 - T1) / 2, "The constant-speed part is a rectangle, not a triangle."),
    ], "m", "distance = area of rectangle = speed × time interval",
        [f"time at constant speed = {T2} − {T1} = {T2 - T1} s", f"distance = {V} × {T2 - T1}", f"= **{fmt(d)} m**"],
        ["Find the part of the graph where the line is horizontal.", "Its area is a rectangle.", f"{V} × ({T2} − {T1})."],
        figure=_vt([(0, 0), (T1, V), (T2, V)], ymax=V * 1.3, shade=(T1, T2)))


@template("c2_kmh_acceleration", chapter=2, level=4, lo="2c")
def kmh_acceleration(rng):
    vk = nice(rng, 36, 54, 72, 90, 108)
    t = nice(rng, 4, 5, 6, 8, 10)
    a = vk / 3.6 / t
    return calc_q(rng, f"Fig. 1 shows a car that accelerates uniformly from rest to **{vk} km/h** in **{t} s**. What is its acceleration in m/s²?", a, [
        (vk / t, "Convert km/h to m/s (÷ 3.6) before dividing by the time."),
        (vk * 3.6 / t, "To convert km/h to m/s, DIVIDE by 3.6."),
        (vk / 60 / t, "1 km/h = 1000 m ÷ 3600 s; divide by 3.6, not by 60."),
    ], "m/s²", "convert km/h to m/s (÷ 3.6), then a = Δv ÷ t",
        [f"{vk} km/h = {vk} ÷ 3.6 = {fmt(vk / 3.6)} m/s", f"a = {fmt(vk / 3.6)} ÷ {t}", f"= **{fmt(a)} m/s²**"],
        ["The acceleration must be in m/s², so the speed must be in m/s.", "km/h ÷ 3.6 = m/s.", "Then divide by the time."],
        figure=sketches.motion_sketch("0 km/h", f"{vk} km/h", f"t = {t} s", body="car"))


@template("c2_braking_distance_graph", chapter=2, level=4, lo="2h")
def braking_distance_graph(rng):
    v = nice(rng, 12, 16, 20, 24, 30)
    t = nice(rng, 3, 4, 5, 6)
    d = 0.5 * v * t
    return calc_q(rng, "Fig. 1 shows the speed–time graph of a car braking uniformly to rest. How far does it travel while braking?", d, [
        (v * t, "The area is a TRIANGLE: ½ × base × height."),
        (v / t, "That is the deceleration (gradient), not the distance."),
        (v * t / 4, "Area of a triangle = ½ × base × height, not ¼."),
    ], "m", "distance = area of triangle = ½ × time × initial speed", ["area = ½ × base × height", f"= ½ × {t} × {v}", f"= **{fmt(d)} m**"],
        ["Distance is the area under the graph.", "The shape is a triangle.", f"½ × {t} × {v}."],
        figure=_vt([(0, v), (t, 0)], shade=(0, t)))


@template("c2_final_speed_from_distance", chapter=2, level=4, lo="2h")
def final_speed_from_distance(rng):
    v = nice(rng, 8, 10, 12, 16, 20)
    t = nice(rng, 4, 5, 6, 8)
    d = 0.5 * v * t
    table = md_table(["start", "time taken / s", "distance travelled / m"], [["from rest, uniform acceleration", t, fmt(d)]])
    return calc_q(rng, f"A cyclist starts from rest and accelerates uniformly.\n\n{table}\n\nWhat is her speed at the end of this time?", v, [
        (d / t, "That is the AVERAGE speed. With uniform acceleration from rest, the final speed is twice the average."),
        (d * t, "Distance = ½ × v × t, so v = 2d ÷ t."),
        (2 * d * t, "v = 2d ÷ t, not 2d × t."),
    ], "m/s", "area under v–t graph: d = ½ v t, so v = 2d ÷ t",
        [f"average speed = {fmt(d)} ÷ {t} = {fmt(d / t)} m/s", "from rest, final speed = 2 × average speed", f"v = **{fmt(v)} m/s**"],
        ["Sketch the speed–time graph: a straight line from 0.", "The distance is the area of the triangle, ½ × t × v.", "Rearrange for v."])


@template("c2_dt_with_rest_average", chapter=2, level=4, lo="2f")
def dt_with_rest_average(rng):
    D1 = nice(rng, 200, 300, 400)
    T1 = nice(rng, 40, 50, 60)
    rest = nice(rng, 20, 30, 40)
    D2 = D1 + nice(rng, 200, 300)
    T3 = T1 + rest + nice(rng, 40, 60)
    v = D2 / T3
    return calc_q(rng, "Fig. 1 shows the distance–time graph of a walker who stops for a rest. What is her average speed for the whole journey?", v, [
        (D2 / (T3 - rest), "The rest time counts: average speed = total distance ÷ TOTAL time."),
        (D1 / T1, "That is the speed for the first stage only."),
        ((D1 / T1 + (D2 - D1) / (T3 - T1 - rest)) / 2, "Do not average the two speeds; use total distance ÷ total time."),
    ], "m/s", "average speed = total distance ÷ total time (including stops)",
        [f"total distance = {D2} m, total time = {T3} s", f"average = {D2} ÷ {T3}", f"= **{fmt(v)} m/s**"],
        ["Read the final distance and the final time from the graph.", "The flat part (rest) still counts as time.", f"{D2} ÷ {T3}."],
        figure=_vt([(0, 0), (T1, D1), (T1 + rest, D1), (T3, D2)], ylabel="distance / m"))


@template("c2_acceleration_from_table", chapter=2, level=4, lo="2c")
def acceleration_from_table(rng):
    u = nice(rng, 2, 3, 4, 5)
    a = nice(rng, 1.5, 2, 2.5, 3)
    rows = [[t, fmt(u + a * t)] for t in (0, 2, 4, 6)]
    table = md_table(["time / s", "speed / m/s"], rows)
    return calc_q(rng, f"The table shows the speed of a trolley rolling down a ramp.\n\n{table}\n\nWhat is the acceleration of the trolley?", a, [
        ((u + 6 * a) / 6, "You divided the final speed by the time. Use the CHANGE in speed: (final − initial) ÷ time."),
        (6 * a, "That is the change in speed over 6 s; divide by the time."),
        (a / 2, "Check the time interval: the readings are 2 s apart."),
    ], "m/s²", "a = change in speed ÷ time taken", [f"change in speed from 0 to 6 s = {fmt(u + 6 * a)} − {u} = {fmt(6 * a)} m/s", f"a = {fmt(6 * a)} ÷ 6", f"= **{fmt(a)} m/s²**"],
        ["The trolley is not starting from rest.", "Use the change in speed between two rows.", "Divide by the time between those rows."])


@template("c2_braking_kmh", chapter=2, level=4, lo="2c")
def braking_kmh(rng):
    vk = nice(rng, 36, 54, 72, 90)
    t = nice(rng, 2, 3, 4, 5)
    a = vk / 3.6 / t
    return calc_q(rng, f"Fig. 1 shows a car travelling at **{vk} km/h** that brakes uniformly to rest in **{t} s**. What is the size of its deceleration?", a, [
        (vk / t, "Convert km/h to m/s first (÷ 3.6)."),
        (vk * 3.6 / t, "km/h → m/s means DIVIDING by 3.6."),
        (vk / 3.6 * t, "Deceleration = change in speed ÷ time."),
    ], "m/s²", "convert to m/s, then deceleration = Δv ÷ t",
        [f"{vk} km/h = {fmt(vk / 3.6)} m/s", f"deceleration = {fmt(vk / 3.6)} ÷ {t}", f"= **{fmt(a)} m/s²**"],
        ["Change the speed into m/s.", "km/h ÷ 3.6.", "Then divide by the stopping time."],
        figure=sketches.motion_sketch(f"{vk} km/h", "0", f"stops in {t} s", body="car"))


@template("c2_first_stage_distance", chapter=2, level=4, lo="2h")
def first_stage_distance(rng):
    V = nice(rng, 8, 10, 12, 16)
    T1 = nice(rng, 4, 5, 6, 8)
    T2 = T1 + nice(rng, 6, 10)
    d = 0.5 * V * T1
    return calc_q(rng, "Fig. 1 shows the speed–time graph of a lift. How far does it travel while it is accelerating?", d, [
        (V * T1, "The accelerating part is a TRIANGLE: ½ × base × height."),
        (V * T2, "Use only the accelerating part of the graph."),
        (V / T1, "That is the acceleration, not the distance."),
    ], "m", "distance = area of triangle under the accelerating section",
        [f"area = ½ × {T1} × {V}", f"= **{fmt(d)} m**"],
        ["Which section of the graph shows acceleration?", "Its area is a triangle.", f"½ × {T1} × {V}."],
        figure=_vt([(0, 0), (T1, V), (T2, V)], ymax=V * 1.3, shade=(0, T1)))


# ---------------------------------------------------------------- L5
@template("c2_stopping_distance_table", chapter=2, level=5, lo="2h")
def stopping_distance_table(rng):
    v = nice(rng, 15, 20, 25)
    tr = nice(rng, 0.6, 0.8, 1.0)
    dec = nice(rng, 5, 2.5, 6.25) if v == 25 else nice(rng, 5, 2.5)
    tb = v / dec
    total = v * tr + 0.5 * v * tb
    table = md_table(["speed / m/s", "reaction time / s", "deceleration when braking / m/s²"], [[v, fmt(tr), fmt(dec)]])
    return calc_q(rng, f"The table gives data for a car that stops for a hazard.\n\n{table}\n\nWhat is the total stopping distance?", total, [
        (0.5 * v * tb, "Include the thinking distance travelled during the reaction time."),
        (v * tr + v * tb, "The braking part is a triangle on the v–t graph: ½ × v × braking time."),
        (v * tr, "That is only the thinking distance."),
    ], "m", "stopping distance = thinking distance (v × reaction time) + braking distance (½ × v × braking time)",
        [f"thinking distance = {v} × {fmt(tr)} = {fmt(v * tr)} m", f"braking time = {v} ÷ {fmt(dec)} = {fmt(tb)} s; braking distance = ½ × {v} × {fmt(tb)} = {fmt(0.5 * v * tb)} m",
         f"total = **{fmt(total)} m**"],
        ["Split the stopping into reaction (constant speed) and braking (uniform deceleration).", "Braking time = speed ÷ deceleration.", "Add the two areas under the v–t graph."])


@template("c2_round_trip_average", chapter=2, level=5, lo="2b")
def round_trip_average(rng):
    v1, v2 = rng.choice([(4, 6), (10, 15), (20, 30), (3, 6), (12, 4), (6, 3)])
    d = nice(rng, 600, 1200, 1800)
    avg = 2 * d / (d / v1 + d / v2)
    return calc_q(rng, f"Fig. 1 shows a cyclist who rides **{d} m** to a shop at **{v1} m/s** and returns along the same road at **{v2} m/s**. What is the average speed for the round trip?", avg, [
        ((v1 + v2) / 2, "The cyclist spends LONGER at the slower speed, so the simple average of the speeds is wrong."),
        (d / (d / v1 + d / v2), "The total distance is there AND back: 2 × the one-way distance."),
        (max(v1, v2), "Use total distance ÷ total time."),
    ], "m/s", "average speed = total distance ÷ total time",
        [f"time out = {d} ÷ {v1} = {fmt(d / v1)} s; time back = {d} ÷ {v2} = {fmt(d / v2)} s", f"average = {2 * d} ÷ {fmt(d / v1 + d / v2)}", f"= **{fmt(avg)} m/s**"],
        ["Find the time for each half of the trip.", "Total distance = 2 × one-way distance.", "Average speed = total distance ÷ total time."],
        figure=sketches.journey_sketch([(f"{d} m out", f"{v1} m/s"), (f"{d} m back", f"{v2} m/s")]))


@template("c2_find_end_time", chapter=2, level=5, lo="2h")
def find_end_time(rng):
    V = nice(rng, 10, 12, 20)
    T1 = nice(rng, 4, 6, 10)
    extra = nice(rng, 10, 15, 20, 25)
    D = 0.5 * V * T1 + V * extra
    T2 = T1 + extra
    table = md_table(["stage", "motion"], [["1", f"from rest, uniform acceleration to {V} m/s in {T1} s"], ["2", f"constant {V} m/s"],
                                           ["whole journey", f"total distance {fmt(D)} m"]])
    return calc_q(rng, f"The table describes the motion of a train.\n\n{table}\n\nAt what time after starting does the train reach the end of the {fmt(D)} m?", T2, [
        (D / V, "The train is slower during stage 1, so it needs longer than D ÷ V."),
        (extra, "That is only the time at constant speed; add the stage 1 time."),
        (T1 + D / V, "Subtract the stage 1 distance before dividing by V."),
    ], "s", "stage 1 distance = ½ V T₁; remaining distance ÷ V gives stage 2 time",
        [f"stage 1 distance = ½ × {V} × {T1} = {fmt(0.5 * V * T1)} m", f"stage 2 time = ({fmt(D)} − {fmt(0.5 * V * T1)}) ÷ {V} = {extra} s", f"total time = {T1} + {extra} = **{fmt(T2)} s**"],
        ["Sketch the speed–time graph.", "Work out the distance covered in stage 1 (a triangle).", "The rest of the distance is covered at constant speed."])


@template("c2_cliff_height", chapter=2, level=5, lo="2i")
def cliff_height(rng):
    t = nice(rng, 2, 2.5, 3, 4)
    h = 5 * t * t
    return calc_q(rng, f"A stone is dropped from rest from a cliff and hits the sea **{fmt(t)} s** later. Air resistance is negligible and g = 10 m/s². Fig. 1 shows its speed–time graph. How high is the cliff?", h, [
        (10 * t * t, "The area is a TRIANGLE: ½ × t × (10 t)."),
        (10 * t, "That is the final speed, not the height."),
        (5 * t, "The final speed is 10 × t; the area is ½ × t × 10t."),
    ], "m", "height = area under v–t graph = ½ × t × (g t)",
        [f"final speed = 10 × {fmt(t)} = {fmt(10 * t)} m/s", f"height = ½ × {fmt(t)} × {fmt(10 * t)}", f"= **{fmt(h)} m**"],
        ["Find the speed when it hits the sea: v = g t.", "The distance fallen is the area under the graph.", "Area of the triangle = ½ × base × height."],
        figure=_vt([(0, 0), (t, 10 * t)], shade=(0, t)))


@template("c2_gap_after_time", chapter=2, level=5, lo="2h")
def gap_after_time(rng):
    vA = nice(rng, 10, 12, 15, 20)
    a = nice(rng, 2, 3, 4)
    t = nice(rng, 4, 5, 6)
    dA, dB = vA * t, 0.5 * a * t * t
    gap = abs(dA - dB)
    if gap == 0:
        t += 1
        dA, dB = vA * t, 0.5 * a * t * t
        gap = abs(dA - dB)
    table = md_table(["car", "motion from t = 0 (side by side)"], [["A", f"constant {vA} m/s"], ["B", f"from rest, acceleration {a} m/s²"]])
    return calc_q(rng, f"Two cars start side by side.\n\n{table}\n\nHow far apart are they after **{t} s**?", gap, [
        (vA * t - a * t * t, "B's distance is the area of a triangle: ½ × t × (a t)."),
        (abs(vA - a * t) * t, "Work out each car's distance first, then subtract."),
        (dA + dB, "They travel in the same direction, so subtract the distances."),
    ], "m", "distance for each car from the area under its speed–time graph; gap = difference",
        [f"A: {vA} × {t} = {fmt(dA)} m", f"B: ½ × {t} × ({a} × {t}) = {fmt(dB)} m", f"gap = **{fmt(gap)} m**"],
        ["Draw both speed–time graphs.", "A gives a rectangle; B gives a triangle.", "Subtract the two areas."])


@template("c2_mixed_units_average", chapter=2, level=5, lo="2b")
def mixed_units_average(rng):
    t1min, v1, d2, v2 = rng.choice([(30, 60, 10, 40), (20, 90, 30, 60), (45, 80, 20, 40), (15, 120, 40, 80)])
    d1 = v1 * t1min / 60
    t2 = d2 / v2
    avg = (d1 + d2) / (t1min / 60 + t2)
    return calc_q(rng, f"Fig. 1 shows a car journey: **{t1min} min at {v1} km/h**, then **{d2} km at {v2} km/h**. What is the average speed for the whole journey in km/h?", avg, [
        ((v1 + v2) / 2, "Do not average the speeds; use total distance ÷ total time."),
        ((d1 + d2) / (t1min + t2), "Convert the minutes to hours first."),
        ((d1 + d2) / t2, "Use the TOTAL time, including the first stage."),
    ], "km/h", "average speed = total distance ÷ total time (in hours)",
        [f"stage 1: {v1} × {t1min}/60 = {fmt(d1)} km", f"stage 2 time: {d2} ÷ {v2} = {fmt(t2)} h", f"average = {fmt(d1 + d2)} ÷ {fmt(t1min / 60 + t2)} = **{fmt(avg)} km/h**"],
        ["Work in km and hours throughout.", "Find the distance of stage 1 and the time of stage 2.", "Total distance ÷ total time."],
        figure=sketches.journey_sketch([(f"{t1min} min", f"{v1} km/h"), (f"{d2} km", f"{v2} km/h")]))
