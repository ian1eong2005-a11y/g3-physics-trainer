"""O level 2026 MCQ practice: learning outcomes with no SEAB Ten-Year-Series MCQ, covered by MCQs ADAPTED from other schools'
2024 preliminary examination papers (question-bank/, board 'school'). Added 31 Oct 2026 so that every 5086 outcome has a question."""
import math

from .. import figs, sketches4 as k4
from .base import calc_q, explain_mcqs, fmt, md_table, nice, template, text_options

CAT = "olevel"


def src(text):
    return f"_Adapted from {text}._"


# ================================================================== Ch 1-5
explain_mcqs([
    dict(id="o26s_magnitude_unit", chapter=1, level=1, lo="1a", source="BGSS 2024 Prelim MCQ 1",
         stem="Length, temperature and mass are all physical quantities. What do they all have?",
         correct="a numerical magnitude and a unit only",
         wrongs={"a numerical magnitude only": "A number on its own is meaningless: 5 what? Every physical quantity needs a unit.",
                 "a magnitude and a direction only": "These are scalars, with no direction, and they still need a unit.",
                 "a magnitude, a direction and a unit": "Length, temperature and mass are scalars: they have no direction."},
         hints=["Think of '5 kg': what are the two parts?", "Do length, temperature and mass need a direction?", "Choose number + unit."]),
    dict(id="o26s_speed_velocity", chapter=2, level=2, lo="2a", source="PRSS 2024 Prelim MCQ 2",
         stem="Each pair is a vector and a scalar describing a moving car. In which pair is the **size** of the vector **always** equal to the scalar?",
         correct="the velocity of the car and the speed of the car",
         wrongs={"the displacement of the car and the distance it travels": "They are equal only if the car moves in one straight line without turning back.",
                 "the weight of the car and the mass of the car": "W = mg: weight is about 10 times the mass number, and the units differ.",
                 "the acceleration of the car and the speed of the car": "Acceleration is the rate of change of velocity, a different quantity."},
         hints=["Speed is how fast; velocity is how fast in a stated direction.", "So the size of the velocity is the speed.",
                "Check whether the other pairs can ever differ."]),
    dict(id="o26s_dt_graph_shape", chapter=2, level=2, lo="2f", source="CHIJ 2024 Prelim MCQ 3",
         stem="Fig. 1 is the distance-time graph of an object moving in a straight line. Which describes its motion from P to Q and from Q to R?",
         correct="P to Q: moving with uniform speed; Q to R: at rest",
         wrongs={"P to Q: uniform acceleration; Q to R: uniform speed": "On a DISTANCE-time graph a straight slope means constant speed, and a flat line means not moving.",
                 "P to Q: increasing speed; Q to R: uniform speed": "Increasing speed would be a curve getting steeper. A flat line means the distance is not changing.",
                 "P to Q: increasing acceleration; Q to R: at rest": "The slope P to Q is straight, so the speed is constant: no acceleration."},
         hints=["The gradient of a distance-time graph is the speed.", "A straight line has a constant gradient.", "A horizontal line: the distance is not changing."],
         figure=lambda: figs.graph([(0, 0), (4, 8), (10, 8)], 10, 10, 2, 2, xlabel="time / s", ylabel="distance / m",
                                   labels=[(0, 0, "P", 8, 8), (4, 8, "Q", 0, 10), (10, 8, "R", -8, 10)])),
    dict(id="o26s_free_fall_constant", chapter=2, level=1, lo="2i", source="SCSS 2024 Prelim MCQ 3",
         stem="A ball falls freely near the Earth's surface with no air resistance. Which quantity stays constant during the fall?",
         correct="its acceleration (about 10 m/s²)",
         wrongs={"its speed": "The speed increases by about 10 m/s every second.",
                 "its velocity": "The velocity increases (downwards) all the time.",
                 "the distance it falls in each second": "It falls further each second because it is moving faster."},
         hints=["What does gravity do to a falling object's speed?", "Near the Earth the acceleration of free fall is about 10 m/s².",
                "Which quantity does not change?"]),
    dict(id="o26s_contact_force", chapter=3, level=1, lo="3a", source="JYSS 2024 Prelim MCQ 3",
         stem="Which of these is a **contact** force?",
         correct="friction",
         wrongs={"electrostatic force": "Charged objects attract or repel without touching: non-contact.",
                 "gravitational force": "Weight acts at a distance: non-contact.",
                 "magnetic force": "Magnets attract iron without touching: non-contact."},
         hints=["A contact force needs the objects to touch.", "Which force acts only where two surfaces rub?", "The other three act across a gap."]),
    dict(id="o26s_liquid_volume_shape", chapter=7, level=2, lo="7a", source="FCS 2024 Prelim MCQ 11",
         stem="Which explains why a liquid has a fixed volume but does **not** have a fixed shape?",
         correct="strong forces keep the molecules close together, but the molecules can move past one another",
         wrongs={"strong forces keep the molecules close together, and they vibrate about fixed positions": "That describes a SOLID, which has a fixed shape.",
                 "weak forces between the molecules, which move freely and far apart": "That describes a GAS, which has no fixed volume.",
                 "weak forces between the molecules, which vibrate about fixed positions": "Molecules in fixed positions would give a fixed shape."},
         hints=["Fixed volume: what keeps the molecules close together?", "No fixed shape: can the molecules change places?", "Combine the two."]),
    dict(id="o26s_temperature_rises", chapter=7, level=2, lo="7d", source="BRD 2024 Prelim MCQ 9",
         stem="The temperature of a solid body rises (no change of state). Which statements are true?\n\n"
              "1 The average speed of its particles increases.\n\n2 The total kinetic energy of its particles increases.\n\n3 Its internal energy increases.",
         correct="1, 2 and 3",
         wrongs={"1 only": "Faster particles mean more kinetic energy, and that is part of the internal energy.",
                 "1 and 2 only": "Internal energy = total kinetic energy + total potential energy of the particles, so it rises too.",
                 "2 and 3 only": "A higher temperature means a higher average kinetic energy, so the particles move faster on average."},
         hints=["Temperature is linked to the average kinetic energy of the particles.", "Internal energy = total KE + total PE of the particles.",
                "If the KE goes up and the PE stays the same, what happens to the total?"]),
    dict(id="o26s_thermal_equilibrium", chapter=8, level=1, lo="8a", source="ZHSS 2024 Prelim MCQ 9",
         stem="Two bodies are in contact and are in **thermal equilibrium**. Which quantity must be the same for both?",
         correct="temperature",
         wrongs={"internal energy": "A large body can store more internal energy than a small one at the same temperature.",
                 "mass": "Bodies of any mass can reach the same temperature.",
                 "volume": "Volume has nothing to do with whether thermal energy flows."},
         hints=["Thermal energy flows from hot to cold.", "When does the flow stop?", "Thermal equilibrium = no net flow = same ...?"]),
    dict(id="o26s_conduction_statement", chapter=8, level=2, lo="8b", source="GYSS 2024 Prelim MCQ 8",
         stem="Which statement about conduction is correct?",
         correct="Conduction transfers thermal energy without the material itself flowing.",
         wrongs={"Conduction can take place in a vacuum.": "Conduction needs particles to pass on vibrations; a vacuum has none.",
                 "Conduction takes place only in solids.": "Liquids and gases conduct too, just very poorly.",
                 "Conduction is faster in non-metals than in metals.": "Metals conduct far better: their free electrons carry energy quickly."},
         hints=["Conduction: vibrating particles pass energy to their neighbours.", "Do the particles travel through the material?",
                "Metals also have free electrons."]),
    dict(id="o26s_convection_cause", chapter=8, level=1, lo="8c", source="HYSS 2024 Prelim MCQ 10",
         stem="In liquids and gases, thermal energy is transferred by convection. What causes convection?",
         correct="a change in density when part of the fluid is heated",
         wrongs={"a change in the mass of the fluid": "Heating does not change the mass.",
                 "the molecules themselves getting bigger": "Molecules do not expand; they move further apart.",
                 "vibrating particles passing energy to their neighbours": "That is conduction."},
         hints=["Heated fluid expands.", "Same mass, bigger volume: what happens to the density?", "Less dense fluid rises."]),
    dict(id="o26s_wave_energy_not_matter", chapter=9, level=2, lo="9b", source="HYSS 2024 Prelim MCQ 12",
         stem="A ball floating in a ripple tank moves up and down as a wave passes under it, but it does not move along with the wave. Which statement is correct?",
         correct="Energy is transferred in the direction of the wave, but the water is not.",
         wrongs={"Both energy and water are transferred in the direction of the wave.": "If the water moved along, the ball would be carried with it.",
                 "Water is transferred in the direction of the wave, but energy is not.": "The ball gains energy (it moves) but stays in place.",
                 "Neither energy nor water is transferred in the direction of the wave.": "The ball starts moving, so energy has reached it."},
         hints=["The ball only bobs up and down.", "Does the water travel along? Does energy?", "Waves transfer energy without transferring matter."]),
    dict(id="o26s_spectrum_hazard", chapter=10, level=2, lo="10d", source="BGSS 2024 Prelim MCQ 16",
         stem="Which statement about over-exposure to electromagnetic waves is correct?",
         correct="Over-exposure to ultraviolet radiation can cause sunburn and skin cancer.",
         wrongs={"Over-exposure to radio waves damages DNA because they are ionising.": "Radio waves have low energy and are not ionising.",
                 "Microwaves are harmless however strong they are.": "Strong microwaves heat body tissue (as in a microwave oven).",
                 "X-rays only affect the surface of the skin.": "X-rays pass deep into the body and ionise cells inside it."},
         hints=["Which radiation from the Sun causes sunburn?", "Which regions are ionising?", "Which regions mainly heat tissue?"]),
    dict(id="o26s_parallel_beam_lens", chapter=11, level=2, lo="11f", source="HGV 2024 Prelim MCQ 14",
         stem="A beam of light parallel to the principal axis falls on a thin converging lens. What happens to the light after it passes through the lens?",
         correct="It converges to the principal focus on the other side, then spreads out.",
         wrongs={"It spreads out as if it came from a point in front of the lens.": "That is what a DIVERGING lens does.",
                 "It stays parallel to the principal axis.": "Only a ray along the axis (or through the optical centre) goes straight on.",
                 "It converges to a point at twice the focal length.": "Parallel rays meet at F, one focal length from the lens."},
         hints=["A converging lens brings light together.", "Where do rays parallel to the axis meet?", "After crossing, do they stop or carry on?"]),
    dict(id="o26s_focal_length", chapter=11, level=1, lo="11g", source="Woodgrove 2024 Prelim MCQ 10",
         stem="In a ray diagram for a thin converging lens, a ray from the top of the object travels parallel to the principal axis. "
              "The focal length is the distance from the lens to which point?",
         correct="where this ray crosses the principal axis after the lens",
         wrongs={"where the image is formed": "The image is at F only for a very distant object.",
                 "where the object is placed": "The object can be at any distance from the lens.",
                 "midway between the object and the image": "That has no special meaning."},
         hints=["Rays parallel to the axis meet at the principal focus.", "Focal length = distance from the lens to the principal focus.",
                "Follow the parallel ray after the lens."]),
    dict(id="o26s_one_coulomb", chapter=12, level=1, lo="12a", source="FHSS 2024 Prelim MCQ 16",
         stem="Charge is measured in coulombs. Which is equal to one coulomb?",
         correct="one ampere second",
         wrongs={"one ampere per volt": "A per V is the unit of conductance (1 ÷ ohm).",
                 "one volt ampere": "V × A is power, measured in watts.",
                 "one volt per ampere": "V ÷ A is resistance, measured in ohms."},
         hints=["Q = I t.", "Current in amperes, time in seconds.", "So the coulomb is A × s."]),
    dict(id="o26s_measure_r_circuit", chapter=13, level=1, lo="13a", source="BSS 2024 Prelim MCQ 17",
         stem="Students draw a circuit to measure the resistance of resistor R using an ammeter and a voltmeter. Which arrangement is correct?",
         correct="ammeter in series with R; voltmeter in parallel with R",
         wrongs={"ammeter in parallel with R; voltmeter in series with R": "Both meters are the wrong way round.",
                 "ammeter and voltmeter both in series with R": "A voltmeter must be connected ACROSS (in parallel with) R.",
                 "ammeter and voltmeter both in parallel with R": "An ammeter must be in series so the current passes through it."},
         hints=["An ammeter measures the current THROUGH R.", "A voltmeter measures the p.d. ACROSS R.", "Through = series, across = parallel."]),
    dict(id="o26s_heating_element", chapter=14, level=1, lo="14a", source="FCS 2024 Prelim MCQ 18",
         stem="An electric oven cooks food using the heating effect of a current. What happens in its heating element?",
         correct="Electrical energy is converted to thermal energy as current passes through its resistance.",
         wrongs={"Thermal energy is converted to electrical energy.": "The oven USES electrical energy to heat; it does not generate electricity.",
                 "Its very low resistance stops it from getting hot.": "The element is made of high-resistance wire so that it gets hot.",
                 "The current is used up in the element.": "Current is not used up: the same current flows back along the neutral wire."},
         hints=["What is the energy input to an oven?", "What is the useful energy output?", "Where does the change happen?"]),
    dict(id="o26s_not_hazard", chapter=14, level=1, lo="14d", source="JYSS 2024 Prelim MCQ 16",
         stem="Which of these is **not** an electrical hazard?",
         correct="using a plug fitted with a correctly rated fuse",
         wrongs={"damaged insulation on a cable": "Bare live wires can give a shock or cause a short circuit.",
                 "overheating of cables": "Hot cables can melt their insulation and start a fire.",
                 "using an appliance in damp conditions": "Water conducts, so damp skin or surfaces can give a shock."},
         hints=["The syllabus lists three hazards.", "Damaged insulation, overheating cables, damp conditions.", "Which option is a safety feature?"]),
    dict(id="o26s_live_neutral_equal", chapter=14, level=2, lo="14g", source="HGV 2024 Prelim MCQ 17",
         stem="The cable to an electric cooker has a live, a neutral and an earth wire. When the cooker is working correctly, in which wires are the currents equal?",
         correct="the live and the neutral only",
         wrongs={"the live, the neutral and the earth": "The earth wire carries current only when there is a fault.",
                 "the live and the earth only": "In normal use the current returns along the NEUTRAL wire.",
                 "the neutral and the earth only": "The current goes out along the live and back along the neutral."},
         hints=["Current flows to the appliance and back.", "Which wire brings it back?", "When does the earth wire carry a current?"]),
    dict(id="o26s_plug_wiring", chapter=14, level=1, lo="14h", source="BRD 2024 Prelim MCQ 19",
         stem="A three-pin plug has an earth (E), a live (L) and a neutral (N) terminal; the fuse is next to L. How should the three wires of the cable be connected?",
         correct="brown to L, blue to N, green-and-yellow to E",
         wrongs={"blue to L, brown to N, green-and-yellow to E": "Live is BROWN; neutral is BLUE.",
                 "brown to L, green-and-yellow to N, blue to E": "Earth is always green-and-yellow.",
                 "green-and-yellow to L, blue to N, brown to E": "Brown is live and must go to the fused L terminal."},
         hints=["Live: brown. Neutral: blue. Earth: green-and-yellow.", "The fuse is on the L terminal.", "Match each colour."]),
    dict(id="o26s_induced_magnetism", chapter=15, level=2, lo="15b", source="BPGHS 2024 Prelim MCQ 18",
         stem="Which is an example of induced magnetism?",
         correct="A magnet attracts an unmagnetised iron nail.",
         wrongs={"A magnet deflects a compass needle.": "The compass needle is already a magnet.",
                 "A freely suspended magnet comes to rest pointing north-south.": "That is a magnet lining up with the Earth's field.",
                 "Two like poles of magnets repel.": "Both are already magnets; nothing is induced."},
         hints=["'Induced' means magnetism is created in a material that was not a magnet.", "Which option starts with an unmagnetised object?",
                "Iron near a magnet becomes a magnet."]),
    dict(id="o26s_compass_needle", chapter=15, level=1, lo="15d", source="BLS 2024 Prelim MCQ 18",
         stem="A bar magnet lies across the page with its S pole on the left and its N pole on the right. A plotting compass is placed just to the right "
              "of the N pole. Which way does the compass needle (its N end) point?",
         correct="to the right, away from the N pole",
         wrongs={"to the left, towards the N pole": "The N end of the needle is repelled by the magnet's N pole.",
                 "up the page": "Next to the end of the magnet the field points straight out of the pole.",
                 "down the page": "Next to the end of the magnet the field points straight out of the pole."},
         hints=["A compass needle points along the field.", "Field lines leave an N pole.", "Like poles repel."]),
    dict(id="o26s_isotope_row", chapter=16, level=2, lo="16b", source="FMSS 2024 Prelim MCQ 24",
         stem="One isotope of chlorine has the nuclide notation ³⁵₁₇Cl. Which describes a nucleus of a **different** isotope of chlorine?",
         correct="17 protons and 20 neutrons",
         wrongs={"17 protons and 18 neutrons": "That is ³⁵₁₇Cl itself (35 − 17 = 18 neutrons).",
                 "18 protons and 17 neutrons": "18 protons would be a different element (argon).",
                 "16 protons and 20 neutrons": "Isotopes of chlorine all have 17 protons."},
         hints=["Isotopes of an element have the same number of protons.", "They differ in the number of neutrons.",
                "Find the option with 17 protons that is not ³⁵₁₇Cl."]),
    dict(id="o26s_nuclide_u238", chapter=16, level=1, lo="16c", source="YTSS 2024 Prelim MCQ 19",
         stem="Uranium-238 has the nuclide notation ²³⁸₉₂U. Which statement is correct?",
         correct="A uranium-238 nucleus contains 146 neutrons.",
         wrongs={"A uranium-238 nucleus contains 92 neutrons.": "92 is the proton number.",
                 "A uranium-238 nucleus contains 238 protons.": "238 is the nucleon number: protons + neutrons.",
                 "A neutral uranium-238 atom has 146 electrons.": "A neutral atom has as many electrons as protons: 92."},
         hints=["Top number A = protons + neutrons.", "Bottom number Z = protons.", "Neutrons = A − Z."]),
    dict(id="o26s_nucleus_composition", chapter=16, level=1, lo="16a", source="GDLS 2024 Prelim MCQ 19",
         stem="An iron nucleus has the nuclide notation ⁵⁹₂₆Fe. What is in this nucleus?",
         correct="26 protons and 33 neutrons",
         wrongs={"26 protons and 59 neutrons": "59 is the total number of nucleons, not just neutrons.",
                 "33 protons and 26 neutrons": "The bottom number is the number of protons.",
                 "26 protons, 33 neutrons and 26 electrons": "Electrons orbit outside the nucleus."},
         hints=["The nucleus contains protons and neutrons only.", "Z = number of protons.", "Neutrons = A − Z."]),
    dict(id="o26s_decay_random", chapter=16, level=1, lo="16d", source="FMSS 2024 Prelim MCQ 20",
         stem="Which statement about radioactive decay is correct?",
         correct="It cannot be predicted when a particular nucleus will decay.",
         wrongs={"Keeping a source in a lead-lined box stops it decaying.": "Lead absorbs the radiation; the nuclei still decay at the same rate.",
                 "The half-life of a nuclide gets shorter as it gets older.": "The half-life of a nuclide is constant.",
                 "The decay rate increases if the substance is dissolved in water.": "Decay is spontaneous: chemical and physical changes do not affect it."},
         hints=["Decay is random and spontaneous.", "Can anything outside the nucleus change it?", "What does 'random' mean for one nucleus?"]),
    dict(id="o26s_alpha_makeup", chapter=16, level=1, lo="16e", source="AMKSS 2024 Prelim MCQ 20",
         stem="What does an alpha particle consist of?",
         correct="two protons and two neutrons",
         wrongs={"two electrons and four neutrons": "An alpha particle has a positive charge, so it has protons and no electrons.",
                 "two protons and four neutrons": "An alpha particle is a helium-4 nucleus: 4 nucleons in total.",
                 "four protons and two neutrons": "Its charge is +2, so it has 2 protons."},
         hints=["An alpha particle is a helium nucleus.", "Helium-4: Z = 2, A = 4.", "Neutrons = 4 − 2."]),
    dict(id="o26s_background", chapter=16, level=1, lo="16f", source="HGV 2024 Prelim MCQ 20",
         stem="A teacher measures the radiation from a radioactive rock and says that background radiation must be taken into account. What is background radiation?",
         correct="ionising radiation present in the laboratory when the rock is not there",
         wrongs={"infrared radiation from warm objects in the laboratory": "Background radiation is IONISING radiation, not infrared.",
                 "infrared radiation from the Sun": "Background radiation is ionising radiation from many sources around us.",
                 "ionising radiation from the rock itself": "That is what is being measured; background is what is there WITHOUT it."},
         hints=["Background radiation is there all the time.", "It comes from rocks, the air (radon), space and food.", "Measure it with the source removed."]),
    dict(id="o26s_tracer_choice", chapter=16, level=2, lo="16h", source="YSS 2024 Prelim MCQ 20",
         stem="A radioactive tracer is injected into a patient, and a detector above the patient shows where it goes. Which is the best tracer?",
         correct="a gamma emitter with a half-life of a few hours",
         wrongs={"an alpha emitter with a half-life of a few hours": "Alpha cannot get out of the body to the detector, and it badly damages cells.",
                 "an alpha emitter with a half-life of a few years": "Alpha cannot leave the body, and it would stay active for years.",
                 "a gamma emitter with a half-life of a few years": "The patient would stay radioactive for years."},
         hints=["The radiation must pass out of the body to the detector.", "Which radiation is most penetrating and least ionising?",
                "The tracer should not stay active for long."]),
], category=CAT)


# ------------------------------------------------------------------ number-varying items adapted from school papers
@template("o26s_table_pressure", chapter=3, level=2, lo="3h", category=CAT)
def table_pressure(rng):
    W, a = nice(rng, (60, 0.0015), (48, 0.002), (36, 0.0012), (80, 0.004))
    p = W / (4 * a)
    return calc_q(rng, "Pressure is defined as force per unit area. A small table stands on four legs (table). What pressure does it exert on the floor?\n\n"
                  + md_table(["quantity", "value"], [["weight of table", f"{W} N"], ["area of each leg", f"{fmt(a)} m²"], ["number of legs", 4]]),
                  p, [(W / a, "The weight is shared by FOUR legs: divide by the total area."), (W * 4 * a, "Pressure = force ÷ area, not force × area."),
                      (W / (2 * a), "There are four legs, not two.")],
                  "N/m²", "p = F ÷ A", [f"total area = 4 × {fmt(a)} = {fmt(4 * a)} m²", f"p = {W} ÷ {fmt(4 * a)} = **{fmt(p)} N/m²**",
                                         src("Outram 2024 Prelim MCQ 8")],
                  ["Pressure = force ÷ area.", "The area is the total area of all four legs.", "Divide."])


@template("o26s_everyday_moments", chapter=5, level=2, lo="5a", category=CAT)
def everyday_moments(rng):
    sets = [((12, 0.25), (6, 0.80), (3, 0.50)), ((15, 0.30), (8, 0.50), (2, 0.90)), ((20, 0.15), (5, 0.70), (4, 0.60)), ((10, 0.40), (9, 0.30), (5, 0.50))]
    (fs, ds), (fd, dd), (fr, dr) = nice(rng, *sets)
    mom = {"spanner": fs * ds, "door": fd * dd, "fishing rod": fr * dr}
    order = sorted(mom, key=mom.get)
    correct = " < ".join(order)
    import itertools
    rev = " < ".join(reversed(order))
    perms = [" < ".join(p) for p in itertools.permutations(mom) if " < ".join(p) not in (correct, rev)]
    rng.shuffle(perms)
    wrongs = {rev: "That is largest to smallest; the question asks for the smallest first."}
    for p_ in perms[:2]:
        wrongs[p_] = "Work out force × perpendicular distance for each object, then put them in order."
    opts, key, mis = text_options(rng, correct, wrongs)
    return dict(stem="Forces are applied to three everyday objects to turn them (table). Which order goes from the **smallest** moment to the **largest**?\n\n"
                     + md_table(["object", "force / N", "perpendicular distance from pivot / m"],
                                [["spanner", fs, fmt(ds)], ["door (at the handle)", fd, fmt(dd)], ["fishing rod", fr, fmt(dr)]]),
                options=opts, key=key, misconceptions=mis, formula="moment = force × perpendicular distance from the pivot",
                working=[f"spanner: {fs} × {fmt(ds)} = {fmt(mom['spanner'])} N m", f"door: {fd} × {fmt(dd)} = {fmt(mom['door'])} N m",
                         f"fishing rod: {fr} × {fmt(dr)} = {fmt(mom['fishing rod'])} N m", f"order: **{correct}**", src("GYSS 2024 Prelim MCQ 5")],
                hints=["Moment = force × perpendicular distance.", "Work out all three.", "Put them in order, smallest first."], figure=None)


# ------------------------------------------------------------------ Ch 9-12
@template("o26s_sound_particles", chapter=9, level=2, lo="9g", category=CAT)
def sound_particles(rng):
    mark = rng.choice(["compression", "rarefaction"])
    other = "rarefaction" if mark == "compression" else "compression"
    c = f"longitudinal; a {mark}"
    wrongs = {f"longitudinal; a {other}": f"At X the particles are {'crowded together' if mark == 'compression' else 'spread out'}: that is a {mark}.",
              f"transverse; a {mark}": "In sound the particles vibrate along the direction the wave travels: longitudinal.",
              f"transverse; a {other}": "Sound is longitudinal, and check how crowded the particles are at X."}
    opts, key, mis = text_options(rng, c, wrongs)
    return dict(stem="Fig. 1 shows the positions of air particles at one instant as a sound wave passes through. What type of wave is sound, and what is at X?",
                figure=k4.sound_particles(mark), options=opts, key=key, misconceptions=mis, formula=None,
                working=["Sound is a longitudinal wave: the particles vibrate along the direction of travel.",
                         f"At X the particles are {'close together' if mark == 'compression' else 'far apart'}: a **{mark}**.", src("AMKSS 2024 Prelim MCQ 14")],
                hints=["Do the air particles move along or across the direction of the wave?", "Compression = particles crowded; rarefaction = spread out.",
                       "Look at the particles at X."])


SPECTRUM = ["gamma rays", "X-rays", "ultraviolet", "visible light", "infrared", "microwaves", "radio waves"]


@template("o26s_spectrum_gaps", chapter=10, level=2, lo="10b", category=CAT)
def spectrum_gaps(rng):
    i, j = nice(rng, (1, 4), (2, 5), (1, 5), (2, 4))
    row = [("P" if k == i else "Q" if k == j else name) for k, name in enumerate(SPECTRUM)]
    c = f"P: {SPECTRUM[i]}; Q: {SPECTRUM[j]}"
    swap = f"P: {SPECTRUM[j]}; Q: {SPECTRUM[i]}"
    n1 = f"P: {SPECTRUM[i]}; Q: {SPECTRUM[j + 1 if j + 1 < 6 else j - 1]}"
    n2 = f"P: {SPECTRUM[i - 1 if i > 1 else i + 1]}; Q: {SPECTRUM[j]}"
    wrongs = {swap: "The order runs from SHORT wavelength (gamma) to LONG wavelength (radio): P and Q are swapped.",
              n1: "Q is one place out: list the regions in order.", n2: "P is one place out: list the regions in order."}
    wrongs = {k: v for k, v in wrongs.items() if k != c}
    opts, key, mis = text_options(rng, c, wrongs)
    return dict(stem="The table shows the regions of the electromagnetic spectrum in order of **increasing wavelength**, with two regions replaced by P and Q. "
                     "What are P and Q?\n\n" + md_table(["short wavelength →"] + [""] * 5 + ["→ long wavelength"], [row]),
                options=opts, key=key, misconceptions=mis, formula=None,
                working=["In order of increasing wavelength: " + ", ".join(SPECTRUM), f"**{c}**", src("BLS 2024 Prelim MCQ 8")],
                hints=["Start from gamma rays (shortest wavelength).", "Then X-rays, ultraviolet, visible, infrared, microwaves, radio.", "Count along to P and Q."],
                figure=None)


@template("o26s_reflection_total_angle", chapter=11, level=1, lo="11a", category=CAT)
def reflection_total_angle(rng):
    t = nice(rng, 70, 100, 64, 110)
    i = t / 2
    return calc_q(rng, f"A ray of light strikes a plane mirror. The angle between the incident ray and the reflected ray is **{t}°**. What is the angle of incidence?\n\n"
                  + md_table(["angle between incident and reflected rays"], [[f"{t}°"]]),
                  i, [(t, "That is the angle between the two RAYS. The normal splits it into two equal halves."),
                      (90 - i, "That is the angle between the ray and the MIRROR. Angles are measured from the normal."),
                      (180 - t, "Measure from the normal: the normal bisects the angle between the rays.")],
                  "°", "angle of incidence = angle of reflection, both measured from the normal",
                  [f"i = r, and i + r = {t}°", f"i = {t}° ÷ 2 = **{fmt(i)}°**", src("USS 2024 Prelim MCQ 12")],
                  ["The angle of incidence is measured from the normal.", "The angle of reflection equals the angle of incidence.", "Together they make the angle between the rays."],
                  figure=None)


@template("o26s_n_from_surface_angles", chapter=11, level=3, lo="11d", category=CAT)
def n_from_surface_angles(rng):
    a, b = nice(rng, (40, 62), (30, 55), (25, 52), (35, 59))
    i, r = 90 - a, 90 - b
    n = math.sin(math.radians(i)) / math.sin(math.radians(r))
    return calc_q(rng, "A ray of light passes from air into a transparent block. The angles are measured **from the surface** of the block (table). "
                       "What is the refractive index of the block?\n\n"
                  + md_table(["ray", "angle between ray and surface"], [["incident ray (in air)", f"{a}°"], ["refracted ray (in block)", f"{b}°"]]),
                  n, [(math.sin(math.radians(a)) / math.sin(math.radians(b)), "Angles of incidence and refraction are measured from the NORMAL, not the surface."),
                      (i / r, "Use the SINES of the angles: n = sin i ÷ sin r."),
                      (math.sin(math.radians(r)) / math.sin(math.radians(i)), "Upside down: n = sin i ÷ sin r, with i in air.")],
                  "", "n = sin i ÷ sin r (angles from the normal)",
                  [f"i = 90° − {a}° = {i}°, r = 90° − {b}° = {r}°", f"n = sin {i}° ÷ sin {r}° = **{fmt(n)}**", src("AMKSS 2024 Prelim MCQ 12")],
                  ["Change each angle to an angle from the normal: 90° − angle.", "i is in air, r is in the block.", "n = sin i ÷ sin r."], figure=None)


@template("o26s_electrons_current", chapter=12, level=3, lo="12c", category=CAT)
def electrons_current(rng):
    N, h = nice(rng, (1.8e21, 5), (4.5e20, 2), (2.7e21, 6), (7.2e20, 4))
    Q = N * 1.6e-19
    t = h * 3600
    I = Q / t * 1000
    nstr = f"{N / 10 ** int(math.log10(N)):.1f} × 10" + str(int(math.log10(N))).translate(str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹"))
    return calc_q(rng, f"**{nstr}** electrons pass a point in a wire in **{h} hours**. Each electron carries a charge of 1.6 × 10⁻¹⁹ C. What is the current?\n\n"
                  + md_table(["quantity", "value"], [["number of electrons", nstr], ["time", f"{h} h"], ["charge on one electron", "1.6 × 10⁻¹⁹ C"]]),
                  I, [(Q / h * 1000, "Change the time into SECONDS before dividing."), (Q * 1000 / 60 / h, "There are 3600 s in an hour, not 60."),
                      (Q / t * 1000 * 10, "Check the powers of ten when you multiply by 1.6 × 10⁻¹⁹.")],
                  "mA", "Q = N × e; I = Q ÷ t",
                  [f"Q = {nstr} × 1.6 × 10⁻¹⁹ = {fmt(Q)} C", f"t = {h} × 3600 = {t} s", f"I = {fmt(Q)} ÷ {t} = {fmt(Q / t)} A = **{fmt(I)} mA**",
                   src("SSP 2024 Prelim MCQ 14")],
                  ["Total charge = number of electrons × charge on one electron.", "Change hours into seconds.", "Current = charge ÷ time."])


@template("o26s_electron_vs_conventional", chapter=12, level=3, lo="12d", category=CAT)
def electron_vs_conventional(rng):
    plus_right = rng.random() < 0.5
    e_p, c_q = ("→", "←") if plus_right else ("←", "→")
    flip = {"→": "←", "←": "→"}
    c = f"electron flow in P {e_p}; conventional current in Q {c_q}"
    wrongs = {f"electron flow in P {flip[e_p]}; conventional current in Q {c_q}": "Electrons flow the OPPOSITE way to the conventional current in the same branch.",
              f"electron flow in P {e_p}; conventional current in Q {flip[c_q]}": "P and Q are both connected between the same two points, so the conventional current goes the same way in both.",
              f"electron flow in P {flip[e_p]}; conventional current in Q {flip[c_q]}": "Conventional current leaves the + terminal; electrons leave the − terminal."}
    opts, key, mis = text_options(rng, c, wrongs)
    return dict(stem="Fig. 1 shows resistors P and Q connected in parallel with a cell. In which directions (along the page) do the electrons flow in P, "
                     "and the conventional current flow in Q?",
                figure=k4.parallel_with_cell(plus_right), options=opts, key=key, misconceptions=mis,
                formula="conventional current: + to − round the circuit; electrons: − to +",
                working=[f"The + terminal is on the {'right' if plus_right else 'left'}, so conventional current leaves it and flows through P and Q "
                         f"from {'right to left (←)' if plus_right else 'left to right (→)'}.",
                         f"Electrons flow the opposite way: in P they go {e_p}.", f"**{c}**", src("MSS 2024 Prelim MCQ 16")],
                hints=["Find the + terminal (long plate) of the cell.", "Conventional current goes out of + and round to −.", "Electrons go the other way."])


@template("o26s_resistance_from_vi", chapter=12, level=2, lo="12h", category=CAT)
def resistance_from_vi(rng):
    V, I = nice(rng, (3.0, 1.2), (4.5, 1.5), (2.4, 0.80), (6.0, 2.5))
    R = V / I
    return calc_q(rng, "A resistor is connected to a cell. The p.d. across it and the current through it are measured (table). What is its resistance?\n\n"
                  + md_table(["quantity", "value"], [["p.d. across resistor", f"{fmt(V)} V"], ["current", f"{fmt(I)} A"]]),
                  R, [(I / V, "Resistance = p.d. ÷ current, not current ÷ p.d."), (V * I, "That is the power in watts."), (V, "That is just the p.d.")],
                  "Ω", "R = V ÷ I", [f"R = {fmt(V)} ÷ {fmt(I)} = **{fmt(R)} Ω**", src("KCPSS 2024 Prelim MCQ 16")],
                  ["Resistance = p.d. ÷ current.", "Put V on top.", "The unit is the ohm."])


@template("o26s_series_contact", chapter=13, level=3, lo="13b", category=CAT)
def series_contact(rng):
    r1, r2, I1 = nice(rng, (12, 24, 0.5), (8, 12, 0.9), (20, 30, 0.45), (10, 30, 0.8))
    V = I1 * r1
    I2 = V / (r1 + r2)
    return calc_q(rng, f"A cell, an ammeter and two resistors are in series (table). When only the first resistor is in the circuit, the ammeter reads **{fmt(I1)} A**. "
                       "The second resistor is then added in series. What is the new ammeter reading?\n\n"
                  + md_table(["resistor", "resistance / Ω"], [["first", r1], ["second", r2]]),
                  I2, [(V / r2, "The current flows through BOTH resistors in series: use the total resistance."), (I1, "Adding resistance in series reduces the current."),
                       (I1 * r1 / (r1 + 2 * r2), "Total resistance in series = r₁ + r₂.")],
                  "A", "V = IR; in series R = r₁ + r₂ and the current is the same everywhere",
                  [f"cell p.d. V = {fmt(I1)} × {r1} = {fmt(V)} V", f"new total resistance = {r1} + {r2} = {r1 + r2} Ω",
                   f"I = {fmt(V)} ÷ {r1 + r2} = **{fmt(I2)} A**, the same at every point in the series circuit", src("USS 2024 Prelim MCQ 15")],
                  ["Find the cell's p.d. from the first reading.", "In series the resistances add.", "The current is the same everywhere in a series circuit."])


@template("o26s_core_specimens", chapter=15, level=3, lo="15c", category=CAT)
def core_specimens(rng):
    sets = [((40, 2), (25, 6), (35, 15)), ((30, 5), (45, 3), (20, 12)), ((22, 14), (38, 7), (44, 1)), ((50, 1), (28, 16), (36, 9))]
    data = dict(zip("XYZ", nice(rng, *sets)))
    em = max(data, key=lambda k: (data[k][0], -data[k][1]))
    perm = max(data, key=lambda k: data[k][1])
    other = [k for k in "XYZ" if k not in (em, perm)][0]
    c = f"Specimen {em} would make the best electromagnet core."
    wrongs = {f"Specimen {em} would make the best permanent magnet.": f"{em} keeps very few nails when switched off: it is a TEMPORARY magnet.",
              f"Specimen {perm} would make the best electromagnet core.": f"{perm} keeps many nails after switching off, so the electromagnet could not release its load.",
              f"Specimen {other} would make the best electromagnet core.": f"{other} picks up fewer nails than {em}."}
    opts, key, mis = text_options(rng, c, wrongs)
    return dict(stem="Three specimens X, Y and Z are tested as the core of a coil. With the current on, each picks up some iron nails; when the current is switched off, "
                     "some nails stay on (table). What can be deduced?\n\n"
                     + md_table(["specimen", "nails picked up (current on)", "nails left on (current off)"], [[k, *data[k]] for k in "XYZ"]),
                options=opts, key=key, misconceptions=mis, formula=None,
                working=["An electromagnet core should be strongly magnetised while the current flows, and lose its magnetism when it stops (temporary, like soft iron).",
                         f"{em} picks up the most and keeps the fewest: **{c}**", f"{perm} keeps the most: it behaves like a permanent magnet (steel).",
                         src("MSS 2024 Prelim MCQ 19")],
                hints=["What should an electromagnet do when the current is switched off?", "Which specimen keeps the fewest nails?",
                       "It should also pick up plenty while the current is on."], figure=None)
