"""Chapter 11 Light: reflection angles, Snell's law, refractive index, focal length."""
import math

from .. import sketches2 as sk
from .base import fmt, md_table, nice, numeric_options, template

C = 3.0e8


def _r_from(n, i):
    return math.degrees(math.asin(math.sin(math.radians(i)) / n))


# ---------------------------------------------------------------- L1
@template("c11_reflection_angle", chapter=11, level=1, lo="11b")
def reflection_angle(rng):
    i = nice(rng, 20, 25, 30, 35, 40, 45, 50, 55, 60)
    opts, key, mis = numeric_options(rng, i, [
        (90 - i, "You gave the angle between the ray and the mirror. Angles are measured from the NORMAL, and r = i."),
        (2 * i, "That is the angle between the incident and reflected rays. The angle of reflection equals the angle of incidence."),
        (i / 2, "You halved. The law of reflection says r = i."),
    ], unit="°")
    return dict(
        stem=f"Fig. 1 shows a ray of light striking a plane mirror. The angle of incidence is **{i}°**. What is the angle of reflection?",
        figure=sk.reflection_diagram(i, show_r=False, label_i=f"{i}°"),
        options=opts, key=key, misconceptions=mis,
        formula="angle of reflection = angle of incidence (both measured from the normal)",
        working=["law of reflection: r = i", f"r = **{i}°**"],
        hints=["What does the law of reflection say about the two angles?",
               "Both angles are measured between the ray and the normal.",
               f"The angle of incidence is {i}°, so the angle of reflection is the same."],
    )


@template("c11_incidence_from_mirror_angle", chapter=11, level=1, lo="11a")
def incidence_from_mirror_angle(rng):
    theta = nice(rng, 20, 25, 30, 35, 40, 50, 55, 60, 65, 70)
    i = 90 - theta
    opts, key, mis = numeric_options(rng, i, [
        (theta, "That is the angle between the ray and the MIRROR. The angle of incidence is measured from the normal."),
        (2 * theta, "You doubled the angle with the mirror. Subtract it from 90° instead."),
        (180 - theta, "You subtracted from 180°. The normal is at 90° to the mirror, so i = 90° − angle with the mirror."),
    ], unit="°")
    return dict(
        stem=f"Fig. 1 shows a ray striking a plane mirror. The ray makes an angle of **{theta}°** with the surface of the mirror. What is the angle of incidence?",
        figure=sk.reflection_diagram(i, show_r=False, label_i="i"),
        options=opts, key=key, misconceptions=mis,
        formula="angle of incidence = 90° − angle between the ray and the mirror surface",
        working=["the normal is perpendicular to the mirror", f"i = 90° − {theta}° = **{i}°**"],
        hints=["The angle of incidence is measured from the NORMAL, not from the mirror. Where is the normal?",
               "The normal is at 90° to the mirror, so the two angles add up to 90°.",
               f"i = 90° − {theta}°."],
    )


# ---------------------------------------------------------------- L2
@template("c11_refractive_index_from_angles", chapter=11, level=2, lo="11d")
def refractive_index_from_angles(rng):
    n = nice(rng, 1.33, 1.5, 1.6, 2.4)
    i = nice(rng, 30, 40, 45, 50, 60)
    r = round(_r_from(n, i), 1)
    n_calc = math.sin(math.radians(i)) / math.sin(math.radians(r))
    opts, key, mis = numeric_options(rng, n_calc, [
        (math.sin(math.radians(r)) / math.sin(math.radians(i)), "You divided the wrong way round: n = sin i ÷ sin r, which must be greater than 1 for light entering glass."),
        (i / r, "You divided the angles themselves. Use the SINES of the angles."),
        (math.sin(math.radians(i - r)), "You took sin of the difference. Use sin i ÷ sin r."),
    ], unit="", dp=2)
    medium = {1.33: "water", 1.5: "glass", 1.6: "a plastic block", 2.4: "diamond"}[n]
    return dict(
        stem=f"Fig. 1 shows a ray of light passing from air into **{medium}**. The angle of incidence is **{i}°** and the angle of refraction is **{r}°**. What is the refractive index of {medium}?",
        figure=sk.refraction_diagram(i, r, medium=medium.replace("a plastic block", "plastic"), label_i=f"{i}°", label_r=f"{r}°"),
        options=opts, key=key, misconceptions=mis,
        formula="refractive index n = sin i ÷ sin r",
        working=[f"n = sin {i}° ÷ sin {r}°", f"= {fmt(math.sin(math.radians(i)), dp=3)} ÷ {fmt(math.sin(math.radians(r)), dp=3)}", f"= **{fmt(n_calc, dp=2)}**"],
        hints=["Which relationship links the angle of incidence, the angle of refraction and the refractive index?",
               f"Find sin {i}° and sin {r}° on your calculator (in degrees mode).",
               f"n = sin {i}° ÷ sin {r}°."],
    )


@template("c11_angle_of_refraction", chapter=11, level=2, lo="11d")
def angle_of_refraction(rng):
    n = nice(rng, 1.33, 1.5, 1.6)
    i = nice(rng, 30, 35, 40, 45, 50, 55, 60)
    r = _r_from(n, i)
    opts, key, mis = numeric_options(rng, r, [
        (i / n, "You divided the ANGLE by n. It is sin r = sin i ÷ n, then take the inverse sine."),
        (math.degrees(math.asin(min(1.0, math.sin(math.radians(i)) * n))) if math.sin(math.radians(i)) * n < 1 else i * n, "You multiplied sin i by n. Light entering a denser medium bends TOWARDS the normal, so r is smaller than i: sin r = sin i ÷ n."),
        (90 - i, "You subtracted from 90°. Use sin r = sin i ÷ n."),
    ], unit="°", dp=1)
    medium = {1.33: "water", 1.5: "glass", 1.6: "plastic"}[n]
    return dict(
        stem=f"Fig. 1 shows a ray of light entering **{medium}** (refractive index **{n}**) from air with an angle of incidence of **{i}°**. What is the angle of refraction?",
        figure=sk.refraction_diagram(i, r, medium=medium, label_i=f"{i}°", label_r="r"),
        options=opts, key=key, misconceptions=mis,
        formula="n = sin i ÷ sin r, so sin r = sin i ÷ n",
        working=[f"sin r = sin {i}° ÷ {n} = {fmt(math.sin(math.radians(i)), dp=3)} ÷ {n} = {fmt(math.sin(math.radians(i)) / n, dp=3)}",
                 f"r = sin⁻¹({fmt(math.sin(math.radians(i)) / n, dp=3)}) = **{fmt(r, dp=1)}°**"],
        hints=["Rearrange n = sin i ÷ sin r to make sin r the subject.",
               f"sin r = sin {i}° ÷ {n}. Work out the number, then use inverse sine.",
               f"r = sin⁻¹(sin {i}° ÷ {n})."],
    )


@template("c11_speed_in_medium", chapter=11, level=2, lo="11e")
def speed_in_medium(rng):
    n = nice(rng, 1.2, 1.25, 1.33, 1.5, 1.6, 2.0, 2.4)
    v8 = 3.0 / n
    opts, key, mis = numeric_options(rng, v8, [
        (3.0 * n, "You multiplied by n. Light is SLOWER in the medium: v = c ÷ n."),
        (3.0 - n, "You subtracted n. Use v = c ÷ n."),
        (3.0 / (n * n), "You divided by n twice. v = c ÷ n."),
    ], unit="× 10⁸ m/s", dp=2)
    return dict(
        stem=f"Fig. 1 shows light entering a medium of refractive index **{n}**. The speed of light in a vacuum is **3.0 × 10⁸ m/s**. What is the speed of light in the medium?",
        figure=sk.refraction_diagram(40, _r_from(n, 40), medium="medium", label_i="i", label_r="r"),
        options=opts, key=key, misconceptions=mis,
        formula="n = speed in vacuum ÷ speed in medium, so v = c ÷ n",
        working=["v = c ÷ n", f"= 3.0 × 10⁸ ÷ {n}", f"= **{fmt(v8, dp=2)} × 10⁸ m/s**"],
        hints=["Refractive index is defined as a ratio of two speeds. Which is on top?",
               "n = c ÷ v, and n is greater than 1, so v must be smaller than c.",
               f"v = 3.0 × 10⁸ ÷ {n}."],
    )


# ---------------------------------------------------------------- L3
@template("c11_refractive_index_from_speeds", chapter=11, level=3, lo="11e")
def refractive_index_from_speeds(rng):
    v8 = nice(rng, 1.25, 1.5, 1.875, 2.0, 2.25, 2.4, 2.5)
    n = 3.0 / v8
    opts, key, mis = numeric_options(rng, n, [
        (v8 / 3.0, "You divided the wrong way round. n = c ÷ v, which must be greater than 1."),
        (3.0 - v8, "You subtracted the speeds. n is a RATIO: c ÷ v."),
        (3.0 / v8 / 2, "Check the division: 3.0 ÷ the speed in the medium (both in units of 10⁸ m/s)."),
    ], unit="", dp=2)
    return dict(
        stem=f"Light travels at **3.0 × 10⁸ m/s** in a vacuum and at **{fmt(v8, dp=3) if v8 % 0.5 else fmt(v8, dp=1)} × 10⁸ m/s** in a certain plastic (Fig. 1). What is the refractive index of the plastic?",
        figure=sk.refraction_diagram(45, _r_from(n, 45), medium="plastic", label_i="i", label_r="r"),
        options=opts, key=key, misconceptions=mis,
        formula="refractive index n = speed of light in vacuum ÷ speed of light in the medium",
        working=["n = c ÷ v", f"= 3.0 × 10⁸ ÷ {v8} × 10⁸", f"= **{fmt(n, dp=2)}**"],
        hints=["Write the definition of refractive index in terms of speeds.",
               "The powers of ten cancel, so divide 3.0 by the speed in the medium.",
               f"n = 3.0 ÷ {v8}."],
    )


@template("c11_angle_of_incidence_from_r", chapter=11, level=3, lo="11d")
def angle_of_incidence_from_r(rng):
    n = nice(rng, 1.33, 1.5, 1.6)
    r = nice(rng, 15, 18, 20, 22, 25, 28, 30)
    i = math.degrees(math.asin(n * math.sin(math.radians(r))))
    opts, key, mis = numeric_options(rng, i, [
        (r * n, "You multiplied the ANGLE by n. Multiply sin r by n, then take the inverse sine."),
        (_r_from(n, r), "You divided sin r by n. Going from the refracted angle back to the incident angle, sin i = n × sin r."),
        (90 - r, "You subtracted from 90°. Use sin i = n sin r."),
    ], unit="°", dp=1)
    medium = {1.33: "water", 1.5: "glass", 1.6: "plastic"}[n]
    return dict(
        stem=f"Fig. 1 shows light refracted into **{medium}** (refractive index **{n}**) with an angle of refraction of **{r}°**. What was the angle of incidence in air?",
        figure=sk.refraction_diagram(i, r, medium=medium, label_i="i", label_r=f"{r}°"),
        options=opts, key=key, misconceptions=mis,
        formula="n = sin i ÷ sin r, so sin i = n × sin r",
        working=[f"sin i = {n} × sin {r}° = {n} × {fmt(math.sin(math.radians(r)), dp=3)} = {fmt(n * math.sin(math.radians(r)), dp=3)}",
                 f"i = sin⁻¹({fmt(n * math.sin(math.radians(r)), dp=3)}) = **{fmt(i, dp=1)}°**"],
        hints=["Rearrange n = sin i ÷ sin r to make sin i the subject.",
               f"sin i = {n} × sin {r}°. The angle in air must be larger than {r}°.",
               f"i = sin⁻¹({n} × sin {r}°)."],
    )


@template("c11_angle_between_rays", chapter=11, level=3, lo="11b")
def angle_between_rays(rng):
    i = nice(rng, 20, 25, 30, 35, 40, 50, 55, 60)
    opts, key, mis = numeric_options(rng, 2 * i, [
        (i, "That is the angle of incidence only. The reflected ray is on the OTHER side of the normal, at the same angle."),
        (180 - 2 * i, "That is the angle between the rays measured the other way. The angle between the incident and reflected rays is i + r = 2i."),
        (90 - i, "That is the angle between the ray and the mirror."),
    ], unit="°")
    return dict(
        stem=f"Fig. 1 shows a ray of light reflected by a plane mirror. The angle of incidence is **{i}°**. What is the angle between the incident ray and the reflected ray?",
        figure=sk.reflection_diagram(i, show_r=True, label_i=f"{i}°", label_r="r"),
        options=opts, key=key, misconceptions=mis,
        formula="angle between the rays = i + r = 2i (since r = i)",
        working=[f"r = i = {i}°", f"angle between the rays = {i}° + {i}° = **{2 * i}°**"],
        hints=["The normal sits between the two rays. What is the angle on each side of it?",
               f"Angle of reflection = angle of incidence = {i}°.",
               f"Add the two angles: {i}° + {i}°."],
    )


# ---------------------------------------------------------------- L4
@template("c11_table_refractive_index", chapter=11, level=4, lo="11d")
def table_refractive_index(rng):
    n = nice(rng, 1.33, 1.5, 1.6)
    angles = sorted(rng.sample([20, 30, 40, 50, 60], 3))
    rows = [[f"{i}", f"{fmt(_r_from(n, i), dp=1)}"] for i in angles]
    i_pick = angles[1]
    r_pick = round(_r_from(n, i_pick), 1)
    n_calc = math.sin(math.radians(i_pick)) / math.sin(math.radians(r_pick))
    opts, key, mis = numeric_options(rng, n_calc, [
        (i_pick / r_pick, "You divided the angles. Use the ratio of their SINES."),
        (math.sin(math.radians(r_pick)) / math.sin(math.radians(i_pick)), "You inverted the ratio: n = sin i ÷ sin r > 1."),
        (n_calc * 1.5, "Check the arithmetic: sin i ÷ sin r for any row gives about the same value."),
    ], unit="", dp=2)
    table = md_table(["angle of incidence i / °", "angle of refraction r / °"], rows)
    return dict(
        stem=f"A student shines a ray into a block and records the angles in the table.\n\n{table}\n\nUse the results to find the refractive index of the block.",
        options=opts, key=key, misconceptions=mis,
        formula="n = sin i ÷ sin r for each pair (the ratio is constant)",
        working=[f"using the row i = {i_pick}°, r = {r_pick}°", f"n = sin {i_pick}° ÷ sin {r_pick}° = **{fmt(n_calc, dp=2)}**", "(the other rows give the same value within rounding)"],
        hints=["Which quantity stays constant for all rows of this table?",
               "Pick any row and divide the sine of i by the sine of r.",
               f"n = sin {i_pick}° ÷ sin {r_pick}°."],
    )


@template("c11_plane_mirror_distance", chapter=11, level=4, lo="11b")
def plane_mirror_distance(rng):
    d = nice(rng, 0.5, 0.8, 1.2, 1.5, 2.0, 2.5, 3.0)
    opts, key, mis = numeric_options(rng, 2 * d, [
        (d, "That is the distance from the object to the mirror. The image is the same distance BEHIND the mirror."),
        (d / 2, "You halved. The image is as far behind the mirror as the object is in front, so object to image is twice the distance."),
        (3 * d, "You tripled. Object-to-mirror plus mirror-to-image = d + d."),
    ], unit="m")
    return dict(
        stem=f"Fig. 1 shows a plane mirror. A student stands **{fmt(d)} m** in front of it. How far is the student from her image?",
        figure=sk.reflection_diagram(30, show_r=True),
        options=opts, key=key, misconceptions=mis,
        formula="image distance behind a plane mirror = object distance in front; separation = 2 × distance",
        working=[f"image is {fmt(d)} m behind the mirror", f"student to image = {fmt(d)} + {fmt(d)} = **{fmt(2 * d)} m**"],
        hints=["Where is the image formed by a plane mirror compared with the object?",
               "It is the same distance behind the mirror as the object is in front.",
               f"Add {fmt(d)} m in front to {fmt(d)} m behind."],
    )


# ---------------------------------------------------------------- L5
@template("c11_time_through_block", chapter=11, level=5, lo="11e")
def time_through_block(rng):
    n = nice(rng, 1.5, 2.0, 2.4)
    d_cm = nice(rng, 6, 9, 12, 15, 18, 24)
    v = C / n
    t = d_cm / 100 / v
    t10 = t * 1e10
    opts, key, mis = numeric_options(rng, t10, [
        (d_cm / 100 / C * 1e10, "You used the speed of light in a VACUUM. Inside the block the speed is c ÷ n."),
        (d_cm / v * 1e10, "You left the thickness in cm. Convert to metres first."),
        (d_cm / 100 * v / 1e18 * 1e10, "You multiplied distance by speed. time = distance ÷ speed."),
    ], unit="× 10⁻¹⁰ s", dp=2)
    return dict(
        stem=f"Fig. 1 shows light passing straight through a block of thickness **{d_cm} cm** made of material with refractive index **{n}**. The speed of light in a vacuum is 3.0 × 10⁸ m/s. How long does the light take to pass through the block?",
        figure=sk.refraction_diagram(0.5, 0.3, medium="block", label_i="", label_r=""),
        options=opts, key=key, misconceptions=mis,
        formula="v = c ÷ n, then time = distance ÷ v (distance in m)",
        working=[f"v = 3.0 × 10⁸ ÷ {n} = {fmt(v / 1e8, dp=2)} × 10⁸ m/s", f"d = {d_cm} cm = {fmt(d_cm / 100)} m",
                 f"t = {fmt(d_cm / 100)} ÷ {fmt(v / 1e8, dp=2)} × 10⁸ = **{fmt(t10, dp=2)} × 10⁻¹⁰ s**"],
        hints=["Light is slower inside the block. Find that speed first from the refractive index.",
               f"v = c ÷ n = 3.0 × 10⁸ ÷ {n}. Then time = distance ÷ speed, with the thickness in metres.",
               f"t = {fmt(d_cm / 100)} ÷ ({fmt(v / 1e8, dp=2)} × 10⁸)."],
    )


@template("c11_parallel_block_exit", chapter=11, level=5, lo="11d")
def parallel_block_exit(rng):
    n = nice(rng, 1.33, 1.5, 1.6)
    i = nice(rng, 35, 40, 45, 50, 55, 60)
    r = round(_r_from(n, i), 1)
    opts, key, mis = numeric_options(rng, i, [
        (r, "That is the angle inside the block. At the parallel bottom face the ray bends AWAY from the normal by the same amount, back to the original angle."),
        (90 - i, "You subtracted from 90°. The emerging ray is parallel to the incident ray, so it makes the same angle with the normal."),
        (round(_r_from(n, r), 1), "You applied the refraction a second time in the same direction. On leaving the block the ray bends away from the normal, undoing the first bend."),
    ], unit="°", dp=1)
    return dict(
        stem=f"Fig. 1 shows a ray entering a rectangular glass block (refractive index **{n}**) with an angle of incidence of **{i}°**; the angle of refraction is **{r}°**. The ray then reaches the parallel bottom face of the block. At what angle to the normal does the ray emerge into the air?",
        figure=sk.refraction_diagram(i, r, medium="glass", label_i=f"{i}°", label_r=f"{r}°"),
        options=opts, key=key, misconceptions=mis,
        formula="at the second parallel face the angle of incidence inside the glass is r, and sin(exit angle) = n sin r = sin i",
        working=[f"inside the block the ray meets the bottom face at {r}° to the normal (parallel faces)",
                 f"sin(exit angle) = {n} × sin {r}° = sin {i}°", f"exit angle = **{i}°** (the emergent ray is parallel to the incident ray)"],
        hints=["The two faces of the block are parallel, so what is the angle of incidence at the bottom face?",
               f"It is {r}°, inside the glass. Now apply n = sin i ÷ sin r the other way round: the ray bends away from the normal.",
               f"sin(exit angle) = {n} × sin {r}°, which equals sin {i}°."],
    )
