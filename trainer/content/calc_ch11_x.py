"""Chapter 11 Light: extra calculation templates (reflection angles, sin i / sin r, n = c / v)."""
import math

from .. import figs
from .. import sketches2 as sk
from .base import calc_q, fmt, md_table, nice, template

S = math.sin
R = math.radians


def deg_asin(x):
    return math.degrees(math.asin(x))


# ---------------------------------------------------------------- L1
@template("c11_mirror_image_distance", chapter=11, level=1, lo="11b")
def mirror_image_distance(rng):
    d = nice(rng, 0.5, 1.2, 1.5, 2, 2.5, 3)
    return calc_q(rng, f"A candle stands **{fmt(d)} m** in front of a plane mirror. The table summarises this. How far BEHIND the mirror is its image?\n\n" + md_table(["object", "distance in front of mirror / m"], [["candle", fmt(d)]]), d, [
        (2 * d, "That is the distance from the candle to its image. The image is as far BEHIND the mirror as the object is in front."),
        (d / 2, "The image is the same distance behind the mirror as the object is in front."),
        (d + 1, "Image distance = object distance for a plane mirror."),
    ], "m", "plane mirror: image distance behind = object distance in front", [f"image is **{fmt(d)} m** behind the mirror"],
        ["Plane mirror images are as far behind the mirror as the object is in front.", "Which distance does the question ask for?", "Mirror to image, not candle to image."])


@template("c11_reflected_to_mirror", chapter=11, level=1, lo="11b")
def reflected_to_mirror(rng):
    i = nice(rng, 20, 25, 35, 40, 50, 65)
    ans = 90 - i
    return calc_q(rng, f"Fig. 1 shows a ray striking a plane mirror with an angle of incidence of **{i}°**. What angle does the REFLECTED ray make with the mirror surface?", ans, [
        (i, "That is the angle of reflection, measured from the NORMAL. The mirror is at 90° to the normal."),
        (2 * i, "That is the angle between the incident and reflected rays."),
        (180 - i, "The reflected ray and the mirror make an angle of 90° − r."),
    ], "°", "angle with mirror = 90° − angle of reflection", [f"r = i = {i}°", f"angle with mirror = 90° − {i}°", f"= **{ans}°**"],
        ["The angle of reflection equals the angle of incidence.", "Angles of reflection are measured from the normal.", "The normal is perpendicular to the mirror."],
        figure=sk.reflection_diagram(i, show_r=True, label_i=f"{i}°", label_r=""), sf=None)


@template("c11_incidence_from_reflection", chapter=11, level=1, lo="11b")
def incidence_from_reflection(rng):
    r = nice(rng, 15, 25, 32, 40, 48, 60)
    return calc_q(rng, f"Fig. 1 shows a ray reflected by a plane mirror. The angle of reflection is **{r}°**. What is the angle of incidence?", r, [
        (90 - r, "Both angles are measured from the normal; they are equal."),
        (2 * r, "The angles are equal; do not double."),
        (180 - r, "Angle of incidence = angle of reflection."),
    ], "°", "law of reflection: i = r", [f"i = r = **{r}°**"],
        ["State the law of reflection.", "Both angles are measured from the normal.", "They are equal."],
        figure=sk.reflection_diagram(r, show_r=True, label_i="i", label_r=f"{r}°"), sf=None)


@template("c11_angle_between_mirror_rays_small", chapter=11, level=1, lo="11b")
def angle_between_mirror_rays_small(rng):
    i = nice(rng, 10, 15, 20, 25, 30)
    return calc_q(rng, f"Fig. 1 shows a ray hitting a plane mirror with an angle of incidence of **{i}°**. What is the angle between the incident ray and the reflected ray?", 2 * i, [
        (i, "That is only the angle of incidence. Add the angle of reflection."),
        (90 - i, "The angle between the rays is i + r."),
        (180 - 2 * i, "Measure the angle between the two rays, which straddle the normal."),
    ], "°", "angle between rays = i + r = 2i", [f"r = i = {i}°", f"angle between rays = {i}° + {i}°", f"= **{2 * i}°**"],
        ["The normal lies between the two rays.", "r = i.", "Add i and r."],
        figure=sk.reflection_diagram(i, show_r=True, label_i=f"{i}°", label_r="r"), sf=None)


# ---------------------------------------------------------------- L2
@template("c11_n_from_sines_table", chapter=11, level=2, lo="11d")
def n_from_sines_table(rng):
    n = nice(rng, 1.33, 1.4, 1.5, 1.6, 2.0)
    si = nice(rng, 0.5, 0.6, 0.7, 0.8)
    sr = si / n
    table = md_table(["sin i", "sin r"], [[fmt(si), fmt(sr, sf=3)]])
    return calc_q(rng, f"A ray passes from air into a transparent block. The table gives the sines of the angles.\n\n{table}\n\nWhat is the refractive index of the block?", n, [
        (sr / si, "n = sin i ÷ sin r, not sin r ÷ sin i."),
        (si - sr, "Divide, do not subtract."),
        (si * sr, "n = sin i ÷ sin r."),
    ], "", "n = sin i ÷ sin r", [f"n = {fmt(si)} ÷ {fmt(sr, sf=3)}", f"= **{fmt(n)}**"],
        ["Snell's law: sin i ÷ sin r = constant = n.", "i is in air, r is in the block.", "Divide."])


@template("c11_speed_in_water", chapter=11, level=2, lo="11e")
def speed_in_water(rng):
    name, n = rng.choice([("water", 1.33), ("glass", 1.5), ("diamond", 2.4), ("ice", 1.31), ("perspex", 1.5)])
    v = 3.0 / n
    table = md_table(["material", "refractive index"], [[name, fmt(n)]])
    return calc_q(rng, f"The table gives a refractive index. The speed of light in a vacuum is 3.0 × 10⁸ m/s.\n\n{table}\n\nWhat is the speed of light in {name}?", v, [
        (3.0 * n, "Light SLOWS DOWN in a denser medium: v = c ÷ n."),
        (n / 3.0, "v = c ÷ n."),
        (3.0, "That is the speed in a vacuum."),
    ], "× 10⁸ m/s", "n = c ÷ v, so v = c ÷ n", [f"v = 3.0 × 10⁸ ÷ {fmt(n)}", f"= **{fmt(v)} × 10⁸ m/s**"],
        ["Refractive index = speed in vacuum ÷ speed in medium.", "Rearrange for v.", f"3.0 ÷ {fmt(n)}."])


@template("c11_n_from_speed", chapter=11, level=2, lo="11e")
def n_from_speed(rng):
    v = nice(rng, 2.0, 2.25, 2.4, 1.5, 1.25)
    n = 3.0 / v
    table = md_table(["speed of light in vacuum / m/s", "speed of light in material / m/s"], [["3.0 × 10⁸", f"{fmt(v)} × 10⁸"]])
    return calc_q(rng, f"The table gives the speed of light in two places.\n\n{table}\n\nWhat is the refractive index of the material?", n, [
        (v / 3.0, "n = speed in vacuum ÷ speed in material."),
        (3.0 - v, "Divide the speeds."),
        (3.0 * v, "n = c ÷ v."),
    ], "", "n = c ÷ v", [f"n = 3.0 ÷ {fmt(v)}", f"= **{fmt(n)}**"],
        ["Refractive index is a ratio of speeds.", "Speed in vacuum on top.", f"3.0 ÷ {fmt(v)}."])


@template("c11_walk_towards_mirror", chapter=11, level=2, lo="11b")
def walk_towards_mirror(rng):
    d = nice(rng, 3, 4, 5, 6)
    x = nice(rng, 1, 1.5, 2)
    ans = 2 * (d - x)
    return calc_q(rng, f"A boy stands in front of a plane mirror and then walks straight towards it. The table gives the distances. How far is he now from his image?" + chr(10) + chr(10) + md_table(["starting distance from mirror / m", "distance walked towards mirror / m"], [[d, fmt(x)]]), ans, [
        (d - x, "That is his distance to the MIRROR. The image is the same distance behind it."),
        (2 * d - x, "Both he and his image move closer: the separation falls by 2x."),
        (2 * d, "That was the separation before he moved."),
    ], "m", "distance to image = 2 × distance to mirror", [f"new distance to mirror = {d} − {fmt(x)} = {fmt(d - x)} m", f"distance to image = 2 × {fmt(d - x)}", f"= **{fmt(ans)} m**"],
        ["Find his new distance from the mirror.", "His image is the same distance behind the mirror.", "Add the two distances."])


@template("c11_r_in_water", chapter=11, level=2, lo="11d")
def r_in_water(rng):
    i = nice(rng, 30, 40, 45, 50, 60)
    n = 1.33
    r = deg_asin(S(R(i)) / n)
    return calc_q(rng, f"Fig. 1 shows a ray of light entering water (refractive index **1.33**) from air at an angle of incidence of **{i}°**. What is the angle of refraction?", r, [
        (i / n, "Snell's law uses the SINES of the angles: sin r = sin i ÷ n."),
        (deg_asin(min(0.99, S(R(i)) * n)) if S(R(i)) * n < 1 else i + 10, "Divide sin i by n, do not multiply."),
        (i, "The ray bends towards the normal, so r is smaller than i."),
    ], "°", "sin r = sin i ÷ n", [f"sin r = sin {i}° ÷ 1.33 = {fmt(S(R(i)) / n)}", f"r = **{fmt(r)}°**"],
        ["sin i ÷ sin r = n.", "Rearrange: sin r = sin i ÷ n.", "Use the inverse sine."],
        figure=sk.refraction_diagram(i, r, medium="water", label_i=f"{i}°", label_r="r"))


@template("c11_deviation_angle", chapter=11, level=2, lo="11c")
def deviation_angle(rng):
    i, r = rng.choice([(50, 30), (60, 35), (45, 28), (40, 25), (55, 33)])
    return calc_q(rng, f"Fig. 1 shows a ray refracted at an air–glass boundary. The angle of incidence is **{i}°** and the angle of refraction is **{r}°**. Through what angle has the ray been bent (deviated)?", i - r, [
        (i + r, "The deviation is the DIFFERENCE between the angles."),
        (90 - r, "Compare the direction of the ray before and after: i − r."),
        (r, "That is the angle of refraction itself."),
    ], "°", "deviation = i − r", [f"deviation = {i}° − {r}°", f"= **{i - r}°**"],
        ["The ray would have gone straight on at angle i.", "It now travels at angle r to the normal.", "The change is i − r."],
        figure=sk.refraction_diagram(i, r, medium="glass", label_i=f"{i}°", label_r=f"{r}°"), sf=None)


# ---------------------------------------------------------------- L3
@template("c11_i_from_r_water", chapter=11, level=3, lo="11d")
def i_from_r_water(rng):
    r = nice(rng, 20, 25, 30, 35)
    n = 1.33
    i = deg_asin(S(R(r)) * n)
    return calc_q(rng, f"Fig. 1 shows light refracted into water (refractive index **1.33**). The angle of refraction is **{r}°**. What was the angle of incidence in air?", i, [
        (r * n, "Snell's law uses the sines: sin i = n × sin r."),
        (deg_asin(S(R(r)) / n), "sin i = n × sin r, not ÷ n."),
        (r, "The ray bends towards the normal entering water, so i is bigger than r."),
    ], "°", "sin i = n × sin r", [f"sin i = 1.33 × sin {r}° = {fmt(n * S(R(r)))}", f"i = **{fmt(i)}°**"],
        ["sin i ÷ sin r = n.", "Rearrange for sin i.", "Then take the inverse sine."],
        figure=sk.refraction_diagram(i, r, medium="water", label_i="i", label_r=f"{r}°"))


@template("c11_mean_n_two_rows", chapter=11, level=3, lo="11d")
def mean_n_two_rows(rng):
    n = nice(rng, 1.5, 1.52, 1.48)
    rows = []
    vals = []
    for i in (30, 60):
        r = deg_asin(S(R(i)) / n)
        r_round = round(r)
        vals.append(S(R(i)) / S(R(r_round)))
        rows.append([i, r_round])
    mean = sum(vals) / 2
    table = md_table(["i / °", "r / °"], rows)
    return calc_q(rng, f"A student measures two pairs of angles for light entering a glass block.\n\n{table}\n\nWhat is the mean refractive index from these results?", mean, [
        (sum(rr[0] / rr[1] for rr in rows) / 2, "Use the SINES of the angles, not the angles."),
        (vals[0], "That uses the first row only; take the mean of both."),
        (1 / mean, "n = sin i ÷ sin r."),
    ], "", "n = sin i ÷ sin r for each row; mean of the two", [f"row 1: sin {rows[0][0]}° ÷ sin {rows[0][1]}° = {fmt(vals[0])}", f"row 2: sin {rows[1][0]}° ÷ sin {rows[1][1]}° = {fmt(vals[1])}", f"mean = **{fmt(mean)}**"],
        ["Work out sin i ÷ sin r for each row.", "Use sines, not the angles themselves.", "Average the two values."])


@template("c11_two_mirrors_90", chapter=11, level=3, lo="11b")
def two_mirrors_90(rng):
    i1 = nice(rng, 20, 30, 35, 40, 50)
    i2 = 90 - i1
    return calc_q(rng, f"Two plane mirrors meet at 90°. A ray strikes the first mirror with an angle of incidence of **{i1}°** and then reflects off the second mirror. Fig. 1 shows the first reflection. What is the angle of incidence at the second mirror?", i2, [
        (i1, "The second mirror is at right angles to the first, so its normal is too."),
        (180 - i1, "Use the geometry: the two angles of incidence add up to 90°."),
        (2 * i1, "Draw the normals at both mirrors; the angles add to 90°."),
    ], "°", "for mirrors at 90°, i₁ + i₂ = 90°", [f"i₂ = 90° − {i1}°", f"= **{i2}°**"],
        ["Draw the normal at each mirror.", "The normals are at right angles to each other.", "The ray between the mirrors makes complementary angles with the two normals."],
        figure=sk.reflection_diagram(i1, show_r=True, label_i=f"{i1}°", label_r=""), sf=None)


@template("c11_speed_ratio_two_media", chapter=11, level=3, lo="11e")
def speed_ratio_two_media(rng):
    (a, na), (b, nb) = rng.choice([(("water", 1.33), ("diamond", 2.4)), (("glass", 1.5), ("diamond", 2.4)), (("water", 1.33), ("glass", 1.5)), (("ice", 1.3), ("glass", 1.56))])
    ratio = nb / na
    table = md_table(["material", "refractive index"], [[a, fmt(na)], [b, fmt(nb)]])
    return calc_q(rng, f"The table gives two refractive indices.\n\n{table}\n\nHow many times faster does light travel in {a} than in {b}?", ratio, [
        (na / nb, f"v ∝ 1 ÷ n, so light is faster in the material with the SMALLER n ({a})."),
        (nb - na, "Divide the indices; v = c ÷ n."),
        (na * nb, "Speed ratio = n_b ÷ n_a."),
    ], "", "v = c ÷ n, so v_a ÷ v_b = n_b ÷ n_a", [f"v_{a} ÷ v_{b} = {fmt(nb)} ÷ {fmt(na)}", f"= **{fmt(ratio)}**"],
        ["v = c ÷ n for each material.", "Write the ratio of the two speeds.", "c cancels."])


@template("c11_refracted_to_surface", chapter=11, level=3, lo="11d")
def refracted_to_surface(rng):
    i = nice(rng, 40, 45, 50, 60)
    n = 1.5
    r = deg_asin(S(R(i)) / n)
    ans = 90 - r
    return calc_q(rng, f"Fig. 1 shows a ray entering glass (refractive index **1.5**) at an angle of incidence of **{i}°**. What angle does the refracted ray make with the glass SURFACE?", ans, [
        (r, "That is the angle with the NORMAL; the surface is at 90° to the normal."),
        (90 - i, "Use the refracted ray, not the incident ray."),
        (i / n, "Use sines: sin r = sin i ÷ n."),
    ], "°", "sin r = sin i ÷ n; angle with surface = 90° − r", [f"sin r = sin {i}° ÷ 1.5 → r = {fmt(r)}°", f"angle with surface = 90° − {fmt(r)}°", f"= **{fmt(ans)}°**"],
        ["Find the angle of refraction first.", "That angle is measured from the normal.", "Subtract it from 90°."],
        figure=sk.refraction_diagram(i, r, medium="glass", label_i=f"{i}°", label_r="r"))


@template("c11_distance_in_glass", chapter=11, level=3, lo="11e")
def distance_in_glass(rng):
    n = nice(rng, 1.5, 2.0)
    t_ns = nice(rng, 1, 2, 4, 5)
    v = 3e8 / n
    d_cm = v * t_ns * 1e-9 * 100
    return calc_q(rng, f"Light travels inside a block of material of refractive index **{fmt(n)}** for **{t_ns} ns** (1 ns = 10⁻⁹ s). The table summarises this. How far does it travel, in cm? Take c = 3.0 × 10⁸ m/s.\n\n" + md_table(["refractive index", "time / ns"], [[fmt(n), t_ns]]), d_cm, [
        (3e8 * t_ns * 1e-9 * 100, "Light is slower in the block: v = c ÷ n."),
        (d_cm / 100, "That is in metres; convert to cm."),
        (3e8 * n * t_ns * 1e-9 * 100, "v = c ÷ n, not c × n."),
    ], "cm", "v = c ÷ n; distance = v × t", [f"v = 3.0 × 10⁸ ÷ {fmt(n)} = {fmt(v / 1e8)} × 10⁸ m/s", f"d = {fmt(v / 1e8)} × 10⁸ × {t_ns} × 10⁻⁹ = {fmt(d_cm / 100)} m", f"= **{fmt(d_cm)} cm**"],
        ["Find the speed of light in the block.", "distance = speed × time.", "Convert m to cm."])


# ---------------------------------------------------------------- L4
@template("c11_rotate_mirror", chapter=11, level=4, lo="11b")
def rotate_mirror(rng):
    i = nice(rng, 20, 25, 30, 35)
    th = nice(rng, 5, 10, 15)
    ans = 2 * (i + th)
    return calc_q(rng, f"Fig. 1 shows a ray hitting a plane mirror at an angle of incidence of **{i}°**. The mirror is then turned so that the angle of incidence becomes **{i + th}°**. What is the new angle between the incident and reflected rays?", ans, [
        (2 * i, "That was the angle before the mirror was turned."),
        (i + th, "That is only the new angle of incidence; add the angle of reflection."),
        (2 * i + th, "Both i and r increase by the same amount."),
    ], "°", "angle between rays = 2 × angle of incidence", [f"new i = new r = {i + th}°", f"angle between rays = 2 × {i + th}°", f"= **{ans}°**"],
        ["After turning, what are the new angles of incidence and reflection?", "They are equal.", "The angle between the rays is their sum."],
        figure=sk.reflection_diagram(i, show_r=True, label_i=f"{i}°", label_r=""), sf=None)


@template("c11_n_from_graph", chapter=11, level=4, lo="11d")
def n_from_graph(rng):
    n = nice(rng, 1.25, 1.5, 2.0)
    pts = [(0, 0), (0.4, 0.4 * n)]
    return calc_q(rng, "Fig. 1 shows a graph of sin i (in air) against sin r (in a block) from a refraction experiment. What is the refractive index of the block?", n, [
        (1 / n, "Gradient = sin i ÷ sin r (y ÷ x), not the other way round."),
        (0.4 * n, "That is a single value of sin i; use the gradient."),
        (n + 0.5, "Find the gradient from two points on the line."),
    ], "", "n = sin i ÷ sin r = gradient of the sin i–sin r graph", [f"gradient = {fmt(0.4 * n)} ÷ 0.4", f"= **{fmt(n)}**"],
        ["Snell's law: sin i = n sin r.", "That is a straight line through the origin.", "Its gradient is n."],
        figure=figs.graph(pts, 0.5, 1.0, 0.1, 0.2, xlabel="sin r", ylabel="sin i"))


@template("c11_speed_from_angles", chapter=11, level=4, lo="11e")
def speed_from_angles(rng):
    i, r = rng.choice([(60, 35), (50, 30), (45, 28), (70, 38)])
    n = S(R(i)) / S(R(r))
    v = 3.0 / n
    return calc_q(rng, f"Fig. 1 shows a ray entering a plastic block from air with i = **{i}°** and r = **{r}°**. Taking c = 3.0 × 10⁸ m/s, what is the speed of light in the plastic?", v, [
        (3.0 * n, "Light slows down in plastic: v = c ÷ n."),
        (3.0 * r / i, "Use the sines of the angles to find n."),
        (3.0 / (i / r), "n = sin i ÷ sin r, not i ÷ r."),
    ], "× 10⁸ m/s", "n = sin i ÷ sin r; v = c ÷ n", [f"n = sin {i}° ÷ sin {r}° = {fmt(n)}", f"v = 3.0 × 10⁸ ÷ {fmt(n)}", f"= **{fmt(v)} × 10⁸ m/s**"],
        ["Find n from the angles.", "Use the sines.", "Then v = c ÷ n."],
        figure=sk.refraction_diagram(i, r, medium="plastic", label_i=f"{i}°", label_r=f"{r}°"))


@template("c11_mirror_image_height_distance", chapter=11, level=4, lo="11b")
def mirror_image_height_distance(rng):
    d1 = nice(rng, 2, 3, 4)
    d2 = nice(rng, 1, 1.5)
    ans = d1 + d2 + d1
    return calc_q(rng, f"A girl stands **{d1} m** in front of a plane mirror. Her friend stands **{fmt(d2)} m** directly behind her (further from the mirror). The table summarises this. How far is the friend from the girl's image?\n\n" + md_table(["person", "distance from mirror / m"], [["girl", d1], ["friend", fmt(d1 + d2)]]), ans, [
        (2 * d1, "That is the girl's distance from her OWN image."),
        (d1 + d2, "That is the friend's distance from the mirror; the image is a further d₁ behind it."),
        (2 * (d1 + d2), "That is the friend's distance from the FRIEND's image."),
    ], "m", "image of the girl is d₁ behind the mirror", [f"friend to mirror = {fmt(d1 + d2)} m", f"mirror to girl's image = {d1} m", f"total = **{fmt(ans)} m**"],
        ["Where is the girl's image?", "It is as far behind the mirror as she is in front.", "Add the friend's distance to the mirror."])


# ---------------------------------------------------------------- L5
@template("c11_time_difference_glass", chapter=11, level=5, lo="11e")
def time_difference_glass(rng):
    n = nice(rng, 1.5, 2.0)
    d = nice(rng, 0.3, 0.6, 0.9, 1.2)
    dt_ns = d * (n - 1) / 3e8 * 1e9
    table = md_table(["path", "length / m"], [["through air", fmt(d)], [f"through glass (n = {fmt(n)})", fmt(d)]])
    return calc_q(rng, f"Two light pulses travel the same distance, one through air and one through glass. Take c = 3.0 × 10⁸ m/s in air.\n\n{table}\n\nHow much later, in ns, does the pulse through glass arrive?", dt_ns, [
        (d * n / 3e8 * 1e9, "That is the time through glass; subtract the time through air."),
        (d / 3e8 * 1e9, "That is the time through air."),
        (d * (n + 1) / 3e8 * 1e9, "Subtract the times, do not add them."),
    ], "ns", "t = d ÷ v; v_glass = c ÷ n; difference = d(n − 1) ÷ c",
        [f"t_air = {fmt(d)} ÷ 3 × 10⁸ = {fmt(d / 3e8 * 1e9)} ns", f"t_glass = {fmt(d)} × {fmt(n)} ÷ 3 × 10⁸ = {fmt(d * n / 3e8 * 1e9)} ns", f"difference = **{fmt(dt_ns)} ns**"],
        ["Find the time in each medium.", "Light is slower in glass by a factor n.", "Subtract."])


@template("c11_wavelength_in_glass", chapter=11, level=5, lo="11e")
def wavelength_in_glass(rng):
    lam = nice(rng, 450, 500, 600, 660)
    n = nice(rng, 1.5, 1.33, 2.0)
    lam_g = lam / n
    table = md_table(["wavelength in air / nm", "refractive index of medium"], [[lam, fmt(n)]])
    return calc_q(rng, f"Light passes from air into a transparent medium. Its frequency does not change.\n\n{table}\n\nWhat is its wavelength in the medium?", lam_g, [
        (lam * n, "The light slows down; with f fixed, λ = v ÷ f gets SMALLER."),
        (lam, "The wavelength changes because the speed changes."),
        (lam - n * 100, "λ is divided by n."),
    ], "nm", "f unchanged; v ÷ n, so λ ÷ n", [f"λ = {lam} ÷ {fmt(n)}", f"= **{fmt(lam_g)} nm**"],
        ["Which quantity stays the same when light enters a new medium?", "v = f λ: if v is divided by n and f is fixed …", "… λ is also divided by n."])


@template("c11_graph_n_then_speed", chapter=11, level=5, lo="11e")
def graph_n_then_speed(rng):
    n = nice(rng, 1.25, 1.5, 2.0)
    v = 3.0 / n
    return calc_q(rng, "Fig. 1 shows a graph of sin i against sin r for light entering a material from air. Taking c = 3.0 × 10⁸ m/s, what is the speed of light in the material?", v, [
        (3.0 * n, "v = c ÷ n, and n is the gradient."),
        (n, "That is the refractive index; now find the speed."),
        (3.0 / (1 / n), "The gradient is sin i ÷ sin r = n."),
    ], "× 10⁸ m/s", "n = gradient; v = c ÷ n", [f"gradient = n = {fmt(n)}", f"v = 3.0 × 10⁸ ÷ {fmt(n)}", f"= **{fmt(v)} × 10⁸ m/s**"],
        ["Find the gradient of the graph.", "The gradient is the refractive index.", "v = c ÷ n."],
        figure=figs.graph([(0, 0), (0.4, 0.4 * n)], 0.5, 1.0, 0.1, 0.2, xlabel="sin r", ylabel="sin i"))


@template("c11_speeds_then_r", chapter=11, level=5, lo="11d")
def speeds_then_r(rng):
    v = nice(rng, 2.0, 2.25, 2.4)
    i = nice(rng, 40, 50, 60)
    n = 3.0 / v
    r = deg_asin(S(R(i)) / n)
    table = md_table(["speed in vacuum / m/s", "speed in liquid / m/s", "angle of incidence / °"], [["3.0 × 10⁸", f"{fmt(v)} × 10⁸", i]])
    return calc_q(rng, f"Light enters a liquid from air (take the speed in air as 3.0 × 10⁸ m/s).\n\n{table}\n\nWhat is the angle of refraction?", r, [
        (i * v / 3.0, "Use the sines: sin r = sin i ÷ n."),
        (deg_asin(min(0.999, S(R(i)) * v / 3.0 * 0.9)) + 3, "Find n = c ÷ v first, then sin r = sin i ÷ n."),
        (i, "The light slows down, so it bends towards the normal: r < i."),
    ], "°", "n = c ÷ v; sin r = sin i ÷ n", [f"n = 3.0 ÷ {fmt(v)} = {fmt(n)}", f"sin r = sin {i}° ÷ {fmt(n)} = {fmt(S(R(i)) / n)}", f"r = **{fmt(r)}°**"],
        ["Find the refractive index from the speeds.", "Then use Snell's law.", "Take the inverse sine."])
