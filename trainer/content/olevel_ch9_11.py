"""O level 2026 MCQ practice, Ch 9-11 (Waves; Electromagnetic Spectrum; Light): adapted SEAB O-Level MCQs on learning outcomes
the 2026 Paper 2 (Q1-7) did not test (sound, echoes, EM spectrum, reflection, refraction, lenses)."""
from .. import sketches, sketches2 as sk, sketches3 as k3
from .base import calc_q, explain_mcqs, fmt, md_table, nice, template, text_options

CAT = "olevel"


def src(text):
    return f"_Adapted from {text}._"


def degrees(q):
    """Show angle options as 40° (no space before the degree sign)."""
    q["options"] = {k: v.replace(" °", "°") for k, v in q["options"].items()}
    return q


# ================================================================== Ch 9 Sound and echoes
@template("o26_two_bangs", chapter=9, level=4, lo="9i", category=CAT)
def two_bangs(rng):
    d1, dt = nice(rng, (160, 1.0), (170, 1.0), (192, 1.2), (204, 1.2))
    d2 = nice(rng, 300, 340, 400)
    v = 2 * d1 / dt
    return calc_q(rng, f"A girl stands **{d1} m** in front of a tall building and fires a starting pistol. A boy stands **{d2} m** behind her (Fig. 1). "
                  f"He hears two bangs **{fmt(dt)} s** apart. What is the speed of sound in air?",
                  v, [(d2 / dt, "The extra distance the echo travels does not depend on where the boy stands."), ((d1 + d2) / dt, "Only the extra path of the echo matters."),
                      (d1 / dt, "The echo goes to the building AND back: extra distance = 2 × " + str(d1) + " m.")], "m/s", "speed = distance ÷ time",
                  [f"the echo travels an extra 2 × {d1} = {2 * d1} m (to the building and back)", f"v = {2 * d1} ÷ {fmt(dt)} = **{fmt(v)} m/s**", src("SEAB O-Level 2014 MCQ 14")],
                  ["Both sounds travel from the girl to the boy; the echo goes a longer way.", "How much further does the echo travel?", "Speed = extra distance ÷ time difference."],
                  figure=k3.building_echo(f"{d1} m", f"{d2} m"))


@template("o26_between_cliffs", chapter=9, level=4, lo="9i", category=CAT)
def between_cliffs(rng):
    v = nice(rng, 320, 340)
    gap = nice(rng, 0.25, 0.50)
    dR = nice(rng, 100, 120, 150)
    dL = dR + v * gap / 2
    t1, t2 = 2 * dL / v, 2 * dR / v
    return calc_q(rng, f"A man stands between two cliffs (Fig. 1) and claps once. The speed of sound is **{v} m/s**. What is the time between the two echoes he hears?",
                  gap, [((dL - dR) / v, "Each echo travels to the cliff AND back: use 2 × distance."), (t1, "That is the time of the later echo only."),
                        (t2, "That is the time of the first echo only.")], "s", "time = 2 × distance ÷ speed",
                  [f"echo from the far cliff: 2 × {fmt(dL)} ÷ {v} = {fmt(t1)} s", f"echo from the near cliff: 2 × {dR} ÷ {v} = {fmt(t2)} s",
                   f"difference = **{fmt(gap)} s**", src("SEAB O-Level 2015 MCQ 14")],
                  ["Find the time for each echo separately.", "Each echo goes there and back.", "Subtract the two times."],
                  figure=k3.between_cliffs(f"{fmt(dL)} m", f"{dR} m"), sf=2)


@template("o26_sonar_depth", chapter=9, level=2, lo="9i", category=CAT)
def sonar_depth(rng):
    t = nice(rng, 0.16, 0.20, 0.32, 0.40)
    v = 1500
    d = v * t / 2
    return calc_q(rng, f"A ship sends a pulse of sound down to the sea bed and detects the echo **{fmt(t)} s** later (Fig. 1). The speed of sound in water is **1500 m/s**. How deep is the sea?",
                  d, [(v * t, "The pulse goes down AND back up: halve the distance."), (v * t / 4, "Halve only once."), (v / t / 2, "distance = speed × time.")],
                  "m", "depth = speed × time ÷ 2",
                  [f"distance there and back = 1500 × {fmt(t)} = {fmt(v * t)} m", f"depth = **{fmt(d)} m**", src("SEAB O-Level 2017 MCQ 15")],
                  ["The time is for the journey down and back.", "distance = speed × time.", "Halve it for the depth."],
                  figure=sketches.echo_sketch("depth = ?", f"echo after {fmt(t)} s", left="ship", right="sea bed", wave="pulse", person=False))


@template("o26_cliff_echo", chapter=9, level=2, lo="9i", category=CAT)
def cliff_echo(rng):
    t = nice(rng, 1.20, 1.60, 2.40)
    v = nice(rng, 320, 340)
    d = v * t / 2
    return calc_q(rng, f"Sound travels at **{v} m/s** in air. A boy shouts and hears the echo from a cliff **{fmt(t)} s** later (Fig. 1). How far is he from the cliff?",
                  d, [(v * t, "The sound goes to the cliff and back: halve it."), (v * t / 4, "Halve only once."), (v / t, "distance = speed × time.")],
                  "m", "distance = speed × time ÷ 2",
                  [f"distance there and back = {v} × {fmt(t)} = {fmt(v * t)} m", f"distance to the cliff = **{fmt(d)} m**", src("SEAB O-Level 2019 MCQ 14")],
                  ["Echo time = time to the cliff AND back.", "Work out the total distance.", "Halve it."],
                  figure=sketches.echo_sketch("distance = ?", f"echo after {fmt(t)} s", left="boy", right="cliff"))


explain_mcqs([
    dict(id="o26_echo_quieter", chapter=9, level=3, lo="9h", source="SEAB O-Level 2015 MCQ 13",
         stem="A girl hears the echo of her shout. The echo has the same pitch as the shout but is quieter. How does the echo compare with the shout?",
         correct="same wavelength, smaller amplitude",
         wrongs={"same wavelength, same amplitude": "Quieter means a SMALLER amplitude.",
                 "longer wavelength, smaller amplitude": "Same pitch = same frequency, and in the same air the same wavelength.",
                 "shorter wavelength, same amplitude": "Same pitch: wavelength unchanged; quieter: amplitude smaller."},
         hints=["Pitch depends on frequency; loudness on amplitude.", "Same pitch → same frequency → same wavelength (same speed).", "Quieter → smaller amplitude."]),
    dict(id="o26_louder_note", chapter=9, level=1, lo="9h", source="SEAB O-Level 2020 MCQ 15",
         stem="A guitarist plays a note and then plays the same note more loudly. What happens to the amplitude and frequency of the sound wave?",
         correct="amplitude increases, frequency unchanged",
         wrongs={"amplitude increases, frequency increases": "The SAME note has the same pitch, so the same frequency.",
                 "amplitude unchanged, frequency increases": "Louder means a larger amplitude; the pitch is unchanged.",
                 "amplitude unchanged, frequency unchanged": "Louder means a larger amplitude."},
         hints=["Loudness ↔ amplitude.", "Pitch ↔ frequency.", "Same note = same pitch."]),
    dict(id="o26_springs_waves", chapter=9, level=2, lo="9e", source="SEAB O-Level 2021 MCQ 10",
         stem="Ropes and slinky springs are both used to show wave motion. Which statement is correct?",
         correct="A slinky spring can show both transverse and longitudinal waves.",
         wrongs={"A rope can show only longitudinal waves.": "A rope shows TRANSVERSE waves (side-to-side shakes).",
                 "A rope can show both transverse and longitudinal waves.": "You cannot push and pull a rope along its length to make compressions.",
                 "A slinky spring can show only longitudinal waves.": "Shaking a slinky from side to side makes a transverse wave."},
         hints=["Transverse: vibration at right angles to the direction of travel.", "Longitudinal: vibration along the direction of travel (compressions).",
                "Which of the two can you both shake sideways and push back and forth?"]),
    dict(id="o26_sound_far", chapter=9, level=2, lo="9h", source="SEAB O-Level 2021 MCQ 13",
         stem="What happens to a sound wave as it travels a long distance through air?",
         correct="Its amplitude decreases.",
         wrongs={"Its frequency decreases.": "The frequency is set by the source; it does not change.",
                 "Its speed decreases.": "The speed depends on the medium (air), not on the distance travelled.",
                 "Its wavelength increases.": "Same speed and same frequency mean the same wavelength."},
         hints=["The sound gets quieter far away.", "Quieter means …?", "Frequency, speed and wavelength stay the same in the same air."]),
], category=CAT)


# ================================================================== Ch 10 EM spectrum
explain_mcqs([
    dict(id="o26_xray_welds", chapter=10, level=1, lo="10c", source="SEAB O-Level 2014 MCQ 12",
         stem="Engineers check welded steel pipes for hidden cracks. Which electromagnetic waves are used?",
         correct="X-rays", wrongs={"infrared": "Infrared does not pass through steel.", "microwaves": "Microwaves are used for cooking and communication.",
                                   "radio waves": "Radio waves are used for broadcasting."},
         hints=["The waves must pass through metal.", "They are also used to see bones in hospitals.", "Engineering applications are listed under X-rays in the syllabus."]),
    dict(id="o26_spectrum_gap", chapter=10, level=2, lo="10c", source="SEAB O-Level 2015 MCQ 12",
         stem="Fig. 1 shows the electromagnetic spectrum with one region replaced by the letter P. What is a use of region P?",
         correct="remote controls for televisions",
         wrongs={"sterilising medical equipment": "That is ultraviolet (or gamma rays).", "seeing broken bones": "That is X-rays.",
                 "satellite television signals": "That is microwaves."},
         hints=["Name region P first: it lies between microwaves and visible light.", "It is felt as warmth.", "What uses infrared?"],
         figure=lambda: sketches.em_spectrum(hidden=["infrared"])),
    dict(id="o26_ir_alarm", chapter=10, level=1, lo="10c", source="SEAB O-Level 2017 MCQ 13 and 2019 MCQ 13",
         stem="Which part of the electromagnetic spectrum is used in burglar (intruder) alarms?",
         correct="infrared", wrongs={"microwaves": "Microwaves are for cooking and satellite communication.", "radio waves": "Radio waves are for broadcasting and RFID tags.",
                                     "ultraviolet": "Ultraviolet is for sterilisation and security marking."},
         hints=["The alarm detects warm bodies.", "Warm bodies give out …", "… infrared radiation."]),
    dict(id="o26_microwave_speed_type", chapter=10, level=1, lo="10a", source="SEAB O-Level 2020 MCQ 14",
         stem="Radio waves travel through a vacuum. What is their speed, and what type of wave are they?",
         correct="3 × 10⁸ m/s, transverse",
         wrongs={"3 × 10⁸ m/s, longitudinal": "All electromagnetic waves are transverse.", "3 × 10² m/s, transverse": "3 × 10² m/s is about the speed of SOUND in air.",
                 "3 × 10² m/s, longitudinal": "That describes sound, not an electromagnetic wave."},
         hints=["Radio waves are electromagnetic waves.", "All EM waves travel at the same speed in a vacuum.", "All EM waves are transverse."]),
    dict(id="o26_transverse_group", chapter=10, level=2, lo="10a", source="SEAB specimen 2024 MCQ 10",
         stem="Which group contains **only** transverse waves?",
         correct="radio waves, microwaves, X-rays",
         wrongs={"radio waves, sound waves, X-rays": "Sound is longitudinal.", "microwaves, ultrasound, gamma rays": "Ultrasound is sound: longitudinal.",
                 "sound waves, light waves, infrared waves": "Sound is longitudinal."},
         hints=["All electromagnetic waves are transverse.", "Sound waves are longitudinal.", "Pick the group with no sound in it."]),
    dict(id="o26_sterilise", chapter=10, level=1, lo="10c", source="SEAB specimen 2024 MCQ 12",
         stem="A clinic needs to sterilise some equipment. Which electromagnetic waves could it use?",
         correct="ultraviolet", wrongs={"infrared": "Infrared heats but does not reliably kill microorganisms.", "microwaves": "Microwaves heat water in food.",
                                        "radio waves": "Radio waves are used for communication."},
         hints=["Sterilising kills bacteria.", "The waves need high frequency and enough energy to damage cells.", "Which is used in sterilising cabinets?"]),
], category=CAT)


# ================================================================== Ch 11 Light
@template("o26_deviation_boundary", chapter=11, level=3, lo="11b", category=CAT)
def deviation_boundary(rng):
    i = nice(rng, 35, 40, 50, 55)
    theta = 180 - 2 * i
    return degrees(calc_q(rng, f"A ray of light is reflected at a boundary (Fig. 1). The angle of incidence is **{i}°**. What is the angle θ between the reflected ray and the path the ray would take if there were no boundary?",
                  theta, [(i, "That is the angle of incidence."), (2 * i, "2i is the angle between the incident and reflected rays, not θ."),
                          (90 - i, "That is the angle between the ray and the boundary.")], "°", "angle of incidence = angle of reflection",
                  [f"angle of reflection = {i}°", f"the straight-on path makes {i}° with the normal below the boundary",
                   f"θ = 180° − {i}° − {i}° = **{theta}°**", src("SEAB O-Level 2015 MCQ 11 and 2021 MCQ 11")],
                  ["i = r.", "The straight-on path and the incident ray are one straight line (180°).", "θ = 180° − 2i."],
                  figure=k3.boundary_deviation(i)))


@template("o26_mirror_xy", chapter=11, level=3, lo="11b", category=CAT)
def mirror_xy(rng):
    i = nice(rng, 25, 35, 40)
    correct = f"X = {2 * i}°, Y = {90 - i}°"
    wrongs = {f"X = {i}°, Y = {i}°": "X is between the two rays: it is i + r = 2i.",
              f"X = {2 * i}°, Y = {i}°": "Y is measured from the MIRROR, not the normal: 90° − i.",
              f"X = {i}°, Y = {90 - i}°": "X is the whole angle between the two rays: 2i."}
    opts, key, mis = text_options(rng, correct, wrongs)
    return dict(stem=f"A ray of light is reflected by a plane mirror (Fig. 1). The angle of incidence is **{i}°**. What are the angles X and Y?",
                figure=k3.mirror_angles(i), options=opts, key=key, misconceptions=mis, formula="i = r; the normal is at 90° to the mirror",
                working=[f"X = i + r = {i} + {i} = **{2 * i}°**", f"Y = 90° − r = **{90 - i}°**", src("SEAB O-Level 2016 MCQ 13")],
                hints=["Draw the normal (at 90° to the mirror).", "X = angle of incidence + angle of reflection.", "Y is between the ray and the mirror surface."])


@template("o26_two_mirrors", chapter=11, level=4, lo="11b", category=CAT)
def two_mirrors(rng):
    i = nice(rng, 60, 65, 70)
    return degrees(calc_q(rng, f"A ray of light hits the first of two plane mirrors placed at right angles (Fig. 1) with an angle of incidence of **{i}°**. It is then reflected by the second mirror. "
                  "Through what angle has the direction of the ray changed?",
                  180, [(2 * i, "That is the turn at the second mirror only; add the turn at the first mirror."),
                        (360, "A 360° turn would send the ray on in its original direction. Here it comes back parallel to its original path."),
                        (180 - 2 * i if 180 - 2 * i > 0 else 90, "That is the turn at the first mirror only; add the turn at the second mirror.")], "°", "i = r at each mirror",
                  [f"first mirror turns the ray through 180° − 2 × {i}° = {180 - 2 * i}°", f"second mirror: angle of incidence = 90° − {i}° = {90 - i}°, turn = 180° − 2 × {90 - i}° = {2 * i}°",
                   f"total = {180 - 2 * i}° + {2 * i}° = **180°** (the ray goes back parallel to its original path)", src("SEAB O-Level 2020 MCQ 13")],
                  ["Find the turn at each mirror: 180° − 2i.", "At the second mirror the angle of incidence is 90° − i.", "Add the two turns."],
                  figure=k3.two_mirrors(i)))


explain_mcqs([
    dict(id="o26_lens_diverging", chapter=11, level=4, lo="11h", source="SEAB O-Level 2014 MCQ 11",
         stem="An object is placed 8 cm from a thin converging lens. Fig. 1 shows two rays from the top of the object. After the lens they are still spreading apart. What can you say about the focal length and the image?",
         correct="focal length greater than 8 cm, virtual image",
         wrongs={"focal length less than 8 cm, real image": "If f were less than 8 cm, the rays would converge to a real image.",
                 "focal length less than 8 cm, virtual image": "Diverging rays mean the object is INSIDE the focal length: f is greater than 8 cm.",
                 "focal length greater than 8 cm, real image": "Rays that never meet cannot form a real image; the image is virtual."},
         hints=["Rays that meet form a real image; rays that spread apart only seem to come from a virtual image.",
                "When does a converging lens fail to bring rays together?", "When the object is closer than F."],
         figure=lambda: k3.rays_after_lens("8 cm")),
    dict(id="o26_n_definition", chapter=11, level=1, lo="11e", source="SEAB O-Level 2016 MCQ 12",
         stem="Which is the definition of the refractive index of a medium?",
         correct="speed of light in a vacuum ÷ speed of light in the medium",
         wrongs={"speed of light in the medium ÷ speed of light in a vacuum": "Upside down: n is always greater than 1.",
                 "angle of refraction ÷ angle of incidence": "n = sin i ÷ sin r, using sines, not the angles.",
                 "speed of light in the medium × speed of light in a vacuum": "n is a ratio of two speeds."},
         hints=["n has no unit and is greater than 1.", "Light is slower in glass than in a vacuum.", "Divide the larger speed by the smaller."]),
    dict(id="o26_camera_image", chapter=11, level=2, lo="11h", source="SEAB O-Level 2017 MCQ 12",
         stem="A camera uses a converging lens to form an image of a distant tree on its sensor. What kind of image is formed?",
         correct="real, inverted, diminished",
         wrongs={"real, upright, same size": "A real image from a converging lens is always inverted; a distant object gives a small image.",
                 "virtual, inverted, magnified": "An image on a sensor is real.", "virtual, upright, diminished": "An image on a sensor is real and inverted."},
         hints=["The image is formed on a screen (the sensor): real or virtual?", "Real images from a converging lens are inverted.", "The object is far beyond 2F."]),
    dict(id="o26_object_2f", chapter=11, level=2, lo="11h", source="SEAB O-Level 2018 MCQ 13",
         stem="An object is placed at a distance of twice the focal length from a thin converging lens (Fig. 1). Which describes the image?",
         correct="real, inverted, same size",
         wrongs={"real, upright, same size": "Real images from a converging lens are inverted.", "virtual, inverted, magnified": "The object is beyond F, so the image is real.",
                 "virtual, upright, magnified": "That is a magnifying glass: object closer than F."},
         hints=["Object at 2F → image at 2F on the other side.", "Is it real or virtual?", "Compare the sizes."],
         figure=lambda: sk.lens_diagram(2.0, 1.0, show_image=False)),
    dict(id="o26_bends_away", chapter=11, level=3, lo="11c", source="SEAB O-Level 2019 MCQ 12",
         stem="Fig. 1 shows a ray of light travelling from medium S into medium T. Which row compares the two media?",
         correct="light is slower in S; T has the lower refractive index",
         wrongs={"light is faster in S; T has the higher refractive index": "The ray bends AWAY from the normal going into T: it speeds up.",
                 "light is faster in S; T has the lower refractive index": "Light bends away from the normal when it speeds up, so it is slower in S.",
                 "light is slower in S; T has the higher refractive index": "Higher refractive index = slower light. Light is faster in T."},
         hints=["Compare the angles with the normal in S and in T.", "Bending away from the normal = speeding up.", "Faster light ↔ lower refractive index."],
         figure=lambda: k3.boundary_ray_up(28, 46)),
    dict(id="o26_object_moved_away", chapter=11, level=3, lo="11h", source="SEAB O-Level 2021 MCQ 12",
         stem="A converging lens forms a real image of an object (Fig. 1). The object is moved further away from the lens. What happens to the image?",
         correct="It moves towards the lens and becomes smaller.",
         wrongs={"It moves away from the lens and becomes larger.": "That happens when the object moves TOWARDS F.",
                 "It moves away from the lens and becomes smaller.": "As the object moves away, the image moves closer to F on the other side.",
                 "It moves towards the lens and becomes larger.": "A more distant object gives a smaller image."},
         hints=["Very distant objects form small images at F.", "So moving the object away moves the image towards F.", "Is F nearer the lens than the image now?"],
         figure=lambda: sk.lens_diagram(3.0, 1.2)),
], category=CAT)
