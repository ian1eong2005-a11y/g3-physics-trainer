"""Chapter 16 Radioactivity: 50 more written-answer questions (10 per level), marked by keywords/phrases."""
from .. import sketches2 as sk
from ..marker import Pitfall, Point
from .base import written

P = Point
PF = Pitfall
CH = 16


def Q(id, lv, lo, stem, points, model, hints, keywords, passes, fails, pitfalls=(), min_points=None, figure=None):
    written(id, CH, lv, lo, stem=stem, points=points, model_answer=model, hints=hints, keywords=keywords,
            pitfalls=pitfalls, min_points=min_points, figure=figure, sample_pass=passes, sample_fail=fails)


BECOMES_RADIOACTIVE = PF(["becomes radioactive", "food is radioactive", "makes it radioactive", "turns radioactive"],
                         "Irradiating with gamma does NOT make an object radioactive: no radioactive nuclei are added to it.")
HALF_LIFE_CHANGES = PF(["shortens the half-life", "half-life gets shorter", "speeds up the decay", "half-life changes with temperature"],
                       "Radioactive decay is spontaneous: heating, cooling or chemical changes do NOT change the half-life.")

# ---------------------------------------------------------------- L1
Q("w16b_proton_number", 1, "16b", "State what is meant by the proton number Z of a nucleus.",
  [P("the number of protons in the nucleus", ["number of protons", "how many protons", "protons in the nucleus"])],
  "The proton (atomic) number Z is the number of protons in the nucleus.",
  ["Z is also called the atomic number.", "It counts one kind of particle.", "State it."],
  "number of protons",
  ["The number of protons in the nucleus", "how many protons there are in the nucleus"],
  ["The number of protons and neutrons", "The number of neutrons"],
  pitfalls=[PF(["protons and neutrons", "number of neutrons", "number of nucleons"], "Z counts PROTONS only; protons + neutrons is the nucleon number A.")])

Q("w16b_nucleon_number", 1, "16b", "State what is meant by the nucleon number A of a nucleus.",
  [P("the total number of protons and neutrons in the nucleus", ["protons and neutrons", "protons plus neutrons", "number of nucleons", "neutrons and protons", "total number of particles in the nucleus"])],
  "The nucleon (mass) number A is the total number of protons and neutrons in the nucleus.",
  ["Nucleons are the particles in the nucleus.", "Which particles are those?", "State it."],
  "protons + neutrons",
  ["The total number of protons and neutrons in the nucleus", "the number of nucleons, protons plus neutrons"],
  ["The number of protons", "The number of electrons"],
  pitfalls=[PF(["number of electrons", "includes electrons"], "Electrons are NOT in the nucleus: A = protons + neutrons.")])

Q("w16b_alpha_what", 1, "16e", "State what an alpha particle is.",
  [P("a helium nucleus: 2 protons and 2 neutrons", ["helium nucleus", "2 protons and 2 neutrons", "two protons and two neutrons", "helium"])],
  "An alpha particle is a helium nucleus: 2 protons and 2 neutrons bound together, with a charge of +2.",
  ["It is the nucleus of a light element.", "How many protons and neutrons?", "State it."],
  "helium nucleus (2p + 2n)",
  ["A helium nucleus with 2 protons and 2 neutrons", "two protons and two neutrons, like a helium nucleus"],
  ["An electron", "An electromagnetic wave"])

Q("w16b_beta_what", 1, "16e", "State what a beta particle is and where it comes from.",
  [P("a fast-moving electron", ["electron", "fast electron", "high-speed electron", "fast-moving electron"]),
   P("emitted from the nucleus (not the electron shells)", ["from the nucleus", "nucleus", "neutron changes"])],
  "A beta particle is a fast-moving electron emitted from the nucleus, when a neutron changes into a proton.",
  ["It has a negative charge.", "Does it come from the shells or the nucleus?", "State both."],
  "fast electron from the nucleus",
  ["A fast-moving electron emitted from the nucleus", "a high-speed electron that comes out of the nucleus"],
  ["A helium nucleus", "An electron from the outer shell"], min_points=2,
  pitfalls=[PF(["from the outer shell", "from the electron shells", "outer shell"], "Beta particles come from the NUCLEUS, not the electron shells.")])

Q("w16b_gamma_what", 1, "16e", "State what gamma radiation is.",
  [P("a high-energy electromagnetic wave (no mass, no charge)", ["electromagnetic", "em wave", "electromagnetic wave", "electromagnetic radiation", "no mass", "no charge"])],
  "Gamma radiation is high-energy electromagnetic radiation emitted from the nucleus; it has no mass and no charge.",
  ["Is it a particle or a wave?", "Which family of waves?", "State it."],
  "electromagnetic wave, no mass or charge",
  ["High-energy electromagnetic radiation with no mass and no charge", "an electromagnetic wave from the nucleus"],
  ["A helium nucleus", "A fast electron"])

Q("w16b_beta_absorber", 1, "16e", "Fig. 1 shows radiation passing through absorbers. State what material and thickness is needed to stop beta radiation.",
  [P("a few millimetres of aluminium", ["few millimetres of aluminium", "few mm of aluminium", "aluminium", "5 mm of aluminium", "thin aluminium"])],
  "Beta radiation is stopped by a few millimetres of aluminium.",
  ["Paper does not stop beta.", "Lead is not needed.", "Which metal sheet stops it?"],
  "a few mm of aluminium",
  ["A few millimetres of aluminium", "a thin sheet of aluminium"],
  ["A sheet of paper", "Thick lead"],
  pitfalls=[PF(["sheet of paper", "thick lead", "paper"], "Beta passes through paper but is stopped by a few mm of ALUMINIUM.")],
  figure=lambda: sk.penetration_diagram())

Q("w16b_background_sources", 1, "16f", "Name two sources of background radiation.",
  [P("rocks and soil (e.g. granite) / radon gas", ["rocks", "radon", "granite", "soil", "ground", "buildings"]),
   P("cosmic rays from space", ["cosmic", "space", "sun"]),
   P("food and drink / medical sources / the body", ["food", "medical", "x-rays", "our bodies", "drink", "nuclear"])],
  "Sources of background radiation include radon gas from rocks such as granite, cosmic rays from space, and food and drink (and medical uses such as X-rays).",
  ["Some comes from the ground.", "Some comes from space.", "Name two."],
  "radon/rocks; cosmic rays; food; medical",
  ["Radon gas from rocks and cosmic rays from space", "cosmic rays and food"],
  ["Mobile phones and Wi-Fi", "Light bulbs"], min_points=2)

Q("w16b_nuclide_meaning", 1, "16c", "State what is meant by a nuclide.",
  [P("a particular type of nucleus, with a given proton number and nucleon number", ["particular nucleus", "type of nucleus", "proton number and nucleon number", "specific number of protons and neutrons", "given proton number", "particular type of nucleus"])],
  "A nuclide is a particular type of nucleus, specified by its proton number Z and nucleon number A.",
  ["It describes one kind of nucleus.", "Which two numbers specify it?", "State it."],
  "nucleus with given Z and A",
  ["A particular type of nucleus with a given proton number and nucleon number", "a specific nucleus defined by its numbers of protons and neutrons"],
  ["A type of electron", "Any element"])

Q("w16b_neutron_count", 1, "16b", "A nucleus of lithium has nucleon number 7 and proton number 3. State the number of neutrons, and how you found it.",
  [P("4 neutrons", ["4 neutrons", "four neutrons", "4"]),
   P("neutrons = nucleon number − proton number = 7 − 3", ["7 − 3", "7 - 3", "a − z", "a - z", "subtract", "nucleon number minus proton number"])],
  "Number of neutrons = nucleon number − proton number = 7 − 3 = 4.",
  ["A counts protons and neutrons.", "Z counts protons.", "Subtract."],
  "7 − 3 = 4",
  ["4 neutrons, because 7 − 3 = 4", "subtract the proton number from the nucleon number: 4"],
  ["10 neutrons", "3 neutrons"], min_points=2,
  figure=lambda: sk.atom_diagram(3, 4, symbol="⁷₃Li"))

Q("w16b_hazards", 1, "16h", "State two hazards of exposure to radioactive radiation.",
  [P("it can damage or kill living cells", ["damage cells", "kill cells", "damages cells", "kills cells", "cell damage"]),
   P("it can cause cancer or mutations (damage to DNA)", ["cancer", "mutation", "mutations", "dna"]),
   P("radiation burns / radiation sickness", ["burns", "sickness", "radiation sickness"])],
  "Radiation can damage or kill living cells, and it can damage DNA, causing mutations and cancer. Large doses cause radiation burns and radiation sickness.",
  ["What does ionising radiation do to cells?", "What long-term illness can it cause?", "State two."],
  "cell damage/death; cancer/mutations",
  ["It can kill cells and cause cancer", "damage to DNA causing mutations, and radiation burns"],
  ["It makes you glow", "It gives you magnetism"], min_points=2)

# ---------------------------------------------------------------- L2
Q("w16b_alpha_most_ionising", 2, "16e", "Explain why alpha particles are the most strongly ionising of the three radiations.",
  [P("they have a large charge (+2)", ["large charge", "+2", "charge of 2", "double positive", "highly charged", "2+"]),
   P("and a large mass, so they move relatively slowly", ["large mass", "heavy", "slow", "move slowly", "massive"]),
   P("so they interact strongly with atoms, knocking out many electrons over a short distance", ["knock out electrons", "many ions", "interact strongly", "collide", "short distance", "many collisions"])],
  "Alpha particles have a large charge (+2) and a large mass, so they move relatively slowly. They interact strongly with the atoms they pass, knocking electrons out of very many of them over a short distance, so they are the most strongly ionising.",
  ["What is the charge of an alpha particle?", "Is it heavy or light?", "How does that affect its interactions with atoms?"],
  "large charge and mass → strong interactions → most ionising",
  ["They have a large charge and mass, so they interact strongly with atoms and knock out many electrons", "alpha is heavy and has a +2 charge, so it causes many ionisations over a short distance"],
  ["Because they are electromagnetic waves", "Because they travel the fastest"], min_points=2)

Q("w16b_gamma_weak_ionising", 2, "16e", "Explain why gamma radiation is only weakly ionising but very penetrating.",
  [P("gamma has no charge (and no mass)", ["no charge", "uncharged", "no mass", "electromagnetic"]),
   P("so it interacts with few atoms (weakly ionising)", ["few atoms", "rarely interacts", "weakly ionising", "few ionisations", "interacts weakly"]),
   P("it loses energy slowly, so it travels a long way and passes through thick materials", ["loses energy slowly", "travels a long way", "passes through", "penetrating", "long range"])],
  "Gamma radiation has no charge and no mass, so it interacts with relatively few atoms and causes few ionisations. Because it loses its energy only slowly, it can travel a long way and pass through thick materials; only thick lead or concrete greatly reduces it.",
  ["Does gamma have a charge?", "How often does it interact with atoms?", "Why does that make it penetrating?"],
  "no charge → few interactions → loses energy slowly → penetrating",
  ["Gamma has no charge so it rarely interacts with atoms, so it is weakly ionising and travels a long way", "it is uncharged, causes few ionisations and so passes through thick materials"],
  ["Because gamma is heavy", "Because gamma has a large charge"], min_points=2)

Q("w16b_read_half_life", 2, "16g", "Fig. 1 shows a decay curve whose activity starts at 800 counts per minute. Describe how to read the half-life from the graph, and give its value.",
  [P("find the time for the activity to fall from 800 to 400 (half)", ["800 to 400", "half of 800", "falls to 400", "400", "halve"]),
   P("half-life = 4 min", ["4 min", "4 minutes", "4.0 min"])],
  "Read the time for the activity to fall from 800 to half of that, 400 counts per minute. This time is the half-life: 4 minutes. (It also takes another 4 minutes to fall from 400 to 200.)",
  ["What is half of the starting activity?", "At what time does the curve reach it?", "State the half-life."],
  "800 → 400 in 4 min",
  ["Find when the activity falls from 800 to 400: the half-life is 4 min", "it takes 4 minutes to halve to 400"],
  ["8 min, when it reaches 200", "It is when the activity reaches zero"], min_points=2,
  pitfalls=[PF(["reaches zero", "becomes zero", "falls to zero"], "The half-life is the time to HALVE, not to reach zero.")],
  figure=lambda: sk.decay_curve(800, 4))

Q("w16b_correct_background", 2, "16f", "Explain why the background count rate must be subtracted from the readings when measuring the count rate of a radioactive source.",
  [P("the detector also records background radiation", ["background radiation", "also records", "background", "counts from background"]),
   P("subtracting it gives the count rate due to the source alone (corrected count rate)", ["source alone", "corrected count", "due to the source", "only from the source", "just the source"])],
  "The detector also records background radiation, which is present everywhere. Subtracting the background count rate gives the corrected count rate, which is due to the source alone.",
  ["Is the source the only radiation the detector picks up?", "What is left after subtraction?", "Explain."],
  "detector records background too; subtract → source alone",
  ["The detector also picks up background radiation, so subtracting it gives the count rate from the source alone", "to get the corrected count rate due only to the source"],
  ["Because the source is weaker in the morning", "To make the numbers bigger"], min_points=1)

Q("w16b_c12_c14", 2, "16b", "Carbon-12 and carbon-14 both have proton number 6. Compare the particles in their nuclei.",
  [P("both have 6 protons", ["6 protons", "same number of protons", "six protons", "both have 6"]),
   P("carbon-12 has 6 neutrons and carbon-14 has 8 neutrons", ["6 neutrons", "8 neutrons", "different number of neutrons", "two more neutrons", "more neutrons"]),
   P("so they are isotopes of carbon", ["isotopes"])],
  "Both nuclei have 6 protons. Carbon-12 has 12 − 6 = 6 neutrons and carbon-14 has 14 − 6 = 8 neutrons. Same protons but different neutrons means they are isotopes of carbon.",
  ["How many protons does each have?", "Work out the neutrons with A − Z.", "What are such nuclei called?"],
  "6 p each; 6 n vs 8 n; isotopes",
  ["Both have 6 protons, but carbon-12 has 6 neutrons and carbon-14 has 8, so they are isotopes", "the same number of protons and a different number of neutrons"],
  ["Carbon-14 has 8 protons", "They have different numbers of protons"], min_points=2,
  pitfalls=[PF(["carbon-14 has 8 protons", "have different numbers of protons", "have a different number of protons"], "Isotopes have the SAME number of protons; only the neutrons differ.")])

Q("w16b_why_emit", 2, "16d", "Explain why some nuclei emit radiation.",
  [P("these nuclei are unstable", ["unstable"]),
   P("they emit radiation to lose energy and become more stable", ["lose energy", "more stable", "become stable", "give out energy", "release energy"])],
  "Some nuclei are unstable. They emit radiation (alpha, beta or gamma) spontaneously to lose energy and become more stable.",
  ["Are all nuclei stable?", "What does emitting radiation do to the nucleus's energy?", "Explain."],
  "unstable → emits to lose energy → more stable",
  ["They are unstable, so they emit radiation to lose energy and become more stable", "an unstable nucleus gives out energy as radiation"],
  ["Because they are heated", "Because electrons hit them"], min_points=2)

Q("w16b_cannot_predict", 2, "16d", "Explain why it is impossible to predict when a particular nucleus in a radioactive sample will decay.",
  [P("decay is random", ["random", "chance"]),
   P("each nucleus has the same chance of decaying in any given time, so we can only predict for large numbers (half-life)", ["same chance", "probability", "large number", "on average", "only for large numbers", "average"])],
  "Radioactive decay is random: each unstable nucleus has the same chance of decaying in a given time, so we cannot say when any one nucleus will decay. We can only predict the behaviour of a large number of nuclei, such as the time for half of them to decay.",
  ["What word describes decay?", "What can we predict instead?", "Explain."],
  "random; only large-number behaviour predictable",
  ["Decay is random, so each nucleus only has a chance of decaying; we can only predict what happens to large numbers", "it is random; only the average behaviour, like the half-life, is predictable"],
  ["Because nuclei decay in order", "Because the detector is too slow"], min_points=1)

Q("w16b_counts_fluctuate", 2, "16d", "The readings on a GM counter near a source go up and down from second to second. Explain why, and how to get a reliable value.",
  [P("decay is random, so the number of decays per second varies", ["random", "varies", "fluctuates", "chance"]),
   P("count over a long time (or repeat and average) to get a reliable count rate", ["long time", "longer time", "repeat", "average", "count for longer"])],
  "Radioactive decay is random, so the number of nuclei decaying each second varies, and so do the readings. A reliable count rate is obtained by counting over a long time (several minutes) or by repeating and averaging.",
  ["What property of decay causes this?", "How do you reduce the effect of random variation?", "Explain."],
  "random → fluctuations; count longer / average",
  ["Decay is random so the readings fluctuate; count for a long time or average several readings", "because decay is random; average over a longer time"],
  ["The GM tube is broken", "The source is moving"], min_points=2)

Q("w16b_beta_paper_al", 2, "16e", "Describe what happens when beta radiation meets (a) a sheet of paper and (b) a few millimetres of aluminium.",
  [P("(a) most passes through the paper", ["passes through the paper", "goes through paper", "through paper", "not stopped by paper", "passes through", "paper does not stop"]),
   P("(b) it is stopped (absorbed) by the aluminium", ["stopped by the aluminium", "absorbed by aluminium", "stopped by aluminium", "aluminium stops it", "stopped"])],
  "(a) Beta radiation passes through a sheet of paper. (b) It is stopped (absorbed) by a few millimetres of aluminium.",
  ["Is beta more or less penetrating than alpha?", "What stops beta?", "Describe both."],
  "passes paper; stopped by few mm Al",
  ["It passes through paper but is stopped by a few mm of aluminium", "paper does not stop it, aluminium does"],
  ["It is stopped by paper", "It passes through aluminium and lead"], min_points=2,
  pitfalls=[PF(["stopped by paper", "paper stops it"], "PAPER stops ALPHA; beta needs a few mm of aluminium.")])

Q("w16b_leak_detection", 2, "16h", "Describe how a radioactive source can be used to find a leak in an underground water pipe.",
  [P("a gamma-emitting tracer is added to the water", ["gamma", "tracer", "added to the water", "radioactive tracer"]),
   P("a detector (GM tube) is moved along the ground above the pipe", ["detector", "gm tube", "geiger", "above the pipe", "along the ground"]),
   P("the count rate is higher where water leaks out and collects", ["higher count", "count rate increases", "more radiation", "higher reading", "count rate rises"])],
  "A small amount of a gamma-emitting tracer is added to the water in the pipe. A detector such as a GM tube is moved along the ground above the pipe. Where water leaks out, the tracer collects in the soil and the count rate is higher, showing the leak.",
  ["What is added to the water?", "How is it detected?", "What shows the leak?"],
  "gamma tracer; detector above; higher count at leak",
  ["Add a gamma tracer to the water and move a detector along the ground; the count rate is higher at the leak", "a radioactive tracer collects where the water leaks, so the GM tube reading rises there"],
  ["Use an alpha source because it is safer underground", "Listen for the sound of the leak"], min_points=2,
  pitfalls=[PF(["alpha source", "use alpha"], "Alpha cannot pass through soil: a GAMMA tracer is needed.")])

# ---------------------------------------------------------------- L3
Q("w16b_three_half_lives", 3, "16g", "A sample has an activity of 1600 counts per minute. Explain what its activity will be after three half-lives.",
  [P("each half-life halves the activity", ["halves", "half", "each half-life", "1/8"]),
   P("1600 → 800 → 400 → 200", ["800", "400", "1600 → 800", "1/8 of 1600"]),
   P("200 counts per minute", ["200"])],
  "Each half-life halves the activity: 1600 → 800 → 400 → 200. After three half-lives the activity is 200 counts per minute (1/8 of the original).",
  ["What happens in one half-life?", "Halve three times.", "State the final value."],
  "1600/8 = 200",
  ["It halves three times: 1600 to 800 to 400 to 200 counts per minute", "1/8 of 1600 = 200"],
  ["0, it has all decayed", "533, a third of 1600"], min_points=2)

Q("w16b_half_life_table", 3, "16g", "Explain how to find the half-life from the table below of corrected count rate against time.\n\n| time / min | 0 | 3 | 6 | 9 | 12 |\n|---|---|---|---|---|---|\n| count rate / per min | 640 | 452 | 320 | 226 | 160 |",
  [P("find the time for the count rate to halve: 640 → 320", ["640 to 320", "halve", "half of 640", "320"]),
   P("this takes 6 min, so the half-life is 6 min", ["6 min", "6 minutes"]),
   P("check: 320 → 160 also takes 6 min", ["160", "check", "again"])],
  "Find the time for the count rate to halve. It falls from 640 to 320 between 0 and 6 min, so the half-life is 6 minutes. Check: it falls from 320 to 160 between 6 and 12 min, another 6 minutes.",
  ["What is half of 640?", "When is that count rate reached?", "Check with another pair."],
  "640 → 320 in 6 min",
  ["It halves from 640 to 320 in 6 minutes, so the half-life is 6 min", "the half-life is 6 min, as 320 to 160 also takes 6 min"],
  ["3 min", "12 min"], min_points=2)

Q("w16b_smoke_alarm_safe", 3, "16e", "A smoke detector in a living room contains an alpha source. Explain why the people in the room are not harmed by its radiation.",
  [P("alpha particles have a very short range (a few cm of air)", ["short range", "few cm of air", "few centimetres", "range in air"]),
   P("they are stopped by the plastic casing (or paper)", ["stopped by the casing", "plastic casing", "casing", "stopped by paper", "absorbed by the plastic"]),
   P("so no radiation reaches the people outside the detector", ["does not reach", "no radiation reaches", "cannot reach", "not reach the people"])],
  "Alpha particles have a very short range: only a few centimetres in air. They are absorbed by the detector's plastic casing, so no radiation reaches the people in the room.",
  ["How far does alpha travel in air?", "What stops alpha?", "Explain."],
  "alpha short range, stopped by casing → does not reach people",
  ["Alpha only travels a few cm in air and is stopped by the plastic casing, so it does not reach anyone", "the casing absorbs the alpha particles because they have a short range"],
  ["Because alpha is not ionising", "Because the source is too weak to decay"], min_points=2,
  pitfalls=[PF(["alpha is not ionising", "alpha is harmless"], "Alpha IS strongly ionising; it is safe here because it cannot reach people.")])

Q("w16b_sr90_beta", 3, "16e", "Strontium-90 (proton number 38, nucleon number 90) decays by beta emission. Explain how the proton number and nucleon number change.",
  [P("a neutron in the nucleus changes into a proton, emitting an electron", ["neutron changes into a proton", "neutron becomes a proton", "neutron turns into a proton", "neutron to proton"]),
   P("proton number increases by 1 to 39", ["39", "increases by 1", "goes up by one"]),
   P("nucleon number stays 90", ["stays 90", "remains 90", "unchanged", "stays the same", "90"])],
  "In beta decay a neutron in the nucleus changes into a proton and emits a fast electron. The proton number increases by 1, from 38 to 39, while the nucleon number stays at 90 because the total number of protons and neutrons is unchanged.",
  ["What change inside the nucleus produces a beta particle?", "What happens to the number of protons?", "And to the total number of nucleons?"],
  "neutron → proton; Z 38 → 39; A stays 90",
  ["A neutron changes into a proton, so Z rises to 39 and A stays 90", "proton number increases by 1 and nucleon number is unchanged at 90"],
  ["Z decreases by 2 and A by 4", "A decreases by 1"], min_points=2,
  pitfalls=[PF(["decreases by 2", "decreases by 4"], "That is ALPHA decay. Beta: Z rises by 1, A unchanged.")])

Q("w16b_po210_alpha", 3, "16e", "Polonium-210 (proton number 84) decays by alpha emission. Explain the proton number and nucleon number of the new nucleus.",
  [P("an alpha particle carries away 2 protons and 2 neutrons", ["2 protons and 2 neutrons", "two protons and two neutrons", "helium nucleus", "alpha particle"]),
   P("proton number 84 − 2 = 82", ["82", "decreases by 2"]),
   P("nucleon number 210 − 4 = 206", ["206", "decreases by 4"])],
  "An alpha particle carries away 2 protons and 2 neutrons. So the proton number falls by 2, from 84 to 82, and the nucleon number falls by 4, from 210 to 206 (a nucleus of lead).",
  ["What does an alpha particle contain?", "Subtract from Z.", "Subtract from A."],
  "Z 84 → 82; A 210 → 206",
  ["The alpha particle takes 2 protons and 2 neutrons, so Z = 82 and A = 206", "proton number decreases by 2 to 82 and nucleon number by 4 to 206"],
  ["Z = 85 and A = 210", "Z = 82 and A = 208"], min_points=2)

Q("w16b_gamma_no_change", 3, "16e", "Explain why emitting a gamma ray does not change the proton number or nucleon number of a nucleus.",
  [P("gamma radiation has no charge and no mass", ["no charge", "no mass", "uncharged", "massless"]),
   P("no particles leave the nucleus; it only loses energy", ["only loses energy", "no particles", "just energy", "only energy", "loses energy"]),
   P("so Z and A stay the same", ["stay the same", "unchanged", "do not change", "same"])],
  "Gamma radiation is electromagnetic radiation with no charge and no mass. No protons or neutrons leave the nucleus; it only loses energy. So the proton number and nucleon number stay the same.",
  ["Does a gamma ray carry charge or mass?", "Do any nucleons leave?", "Explain."],
  "no charge or mass; only energy lost; Z and A unchanged",
  ["Gamma has no charge or mass, so no particles leave and Z and A are unchanged; the nucleus just loses energy", "only energy is emitted, so the numbers stay the same"],
  ["Because gamma rays are too fast", "Z increases by 1"], min_points=2)

Q("w16b_tongs", 3, "16h", "Explain why radioactive sources are handled with long tongs and never with the fingers.",
  [P("tongs keep the source further from the body", ["further from the body", "distance", "further away", "away from the hand", "keeps the source away"]),
   P("the radiation received decreases with distance (alpha/beta absorbed by air)", ["decreases with distance", "less radiation", "weaker further away", "absorbed by air", "less exposure"]),
   P("so less damage to cells / reduces the dose", ["less damage", "reduces the dose", "lower dose", "less harm"])],
  "Long tongs keep the source further from the hand and body. The radiation received decreases with distance, as it spreads out and alpha and beta are absorbed by the air, so the dose received and the risk of damage to cells are reduced.",
  ["How do tongs change the distance?", "How does radiation change with distance?", "What is the benefit?"],
  "more distance → less radiation → smaller dose",
  ["The tongs keep the source further away, and the radiation decreases with distance, so the dose is lower", "distance reduces exposure, so less damage to cells"],
  ["Tongs stop the source decaying", "Tongs make the source less radioactive"], min_points=2)

Q("w16b_lead_box", 3, "16h", "Explain why radioactive sources are stored in lead-lined boxes.",
  [P("lead absorbs radiation, including most gamma radiation", ["absorbs", "lead absorbs", "stops gamma", "absorbs gamma", "blocks", "stops radiation"]),
   P("so people nearby are not exposed (dose kept low)", ["not exposed", "protect", "reduce exposure", "people nearby", "less radiation escapes"])],
  "Lead is dense and absorbs radiation, including most gamma radiation (alpha and beta are stopped completely). Storing sources in lead-lined boxes keeps people nearby from being exposed.",
  ["Which material absorbs gamma best?", "What would happen without the box?", "Explain."],
  "lead absorbs radiation → protects people",
  ["Lead absorbs the radiation, including gamma, so people nearby are protected", "the lead stops radiation escaping, reducing exposure"],
  ["Lead slows down the decay", "Lead keeps the source cold"], min_points=2, pitfalls=[HALF_LIFE_CHANGES])

Q("w16b_film_badge", 3, "16h", "Hospital radiographers wear badges that record the radiation they receive. Explain why.",
  [P("to monitor (measure) the total dose received over time", ["monitor", "measure the dose", "total dose", "how much radiation", "record the dose", "dose received"]),
   P("radiation damage builds up / large doses increase the risk of cancer", ["builds up", "cancer", "damage", "risk", "accumulate"]),
   P("so workers can be moved away if the safe limit is reached", ["safe limit", "limit", "moved away", "stop working", "too high"])],
  "The badge monitors the total radiation dose a worker receives over time. The risk of damage such as cancer increases with dose, so if a worker's dose approaches the safe limit, they can be moved away from radiation work.",
  ["What does the badge measure?", "Why does the total dose matter?", "What can be done with the information?"],
  "monitor total dose; risk rises with dose; act at limit",
  ["To monitor the total dose they receive, because the risk of cancer increases with dose, so they can stop before the safe limit", "it records how much radiation they get so it does not exceed the limit"],
  ["To make them radioactive", "To block all the radiation"], min_points=2)

Q("w16b_radon", 3, "16f", "Radon is a radioactive gas from rocks and is a major part of background radiation. Explain why it is a health risk and how the risk is reduced.",
  [P("radon emits alpha particles", ["alpha"]),
   P("it is breathed in, so the alpha particles ionise cells inside the lungs", ["breathed in", "inside the lungs", "in the lungs", "inside the body", "inhaled"]),
   P("ventilation removes radon from buildings", ["ventilation", "ventilate", "open windows", "fans", "air flow"])],
  "Radon emits alpha particles. Because it is a gas, it is breathed in, and the strongly ionising alpha particles then damage cells inside the lungs, increasing the risk of cancer. Good ventilation of buildings removes the radon and reduces the risk.",
  ["What radiation does radon emit?", "How does it get inside the body?", "How can its level in buildings be reduced?"],
  "alpha emitter; inhaled → lung damage; ventilation",
  ["Radon emits alpha particles and is breathed in, damaging cells in the lungs; ventilation reduces the risk", "inhaled radon ionises lung cells, so buildings should be well ventilated"],
  ["Radon is safe because alpha cannot pass through skin", "Radon emits light"], min_points=2)

# ---------------------------------------------------------------- L4
Q("w16b_carbon_age_quarter", 4, "16g", "Wood from an ancient boat has a quarter of the carbon-14 activity of living wood. The half-life of carbon-14 is 5700 years. Explain how old the wood is.",
  [P("a quarter means two half-lives have passed (1 → ½ → ¼)", ["two half-lives", "2 half-lives", "1/2 then 1/4", "halved twice"]),
   P("age = 2 × 5700 = 11 400 years", ["11 400", "11400", "2 × 5700"])],
  "The activity has halved twice (1 → ½ → ¼), so two half-lives have passed. The age is 2 × 5700 = 11 400 years.",
  ["How many halvings give a quarter?", "Multiply by the half-life.", "State the age."],
  "¼ → 2 half-lives → 11 400 years",
  ["A quarter means two half-lives, so the wood is 2 × 5700 = 11 400 years old", "it has halved twice: 11 400 years"],
  ["1425 years", "22 800 years"], min_points=2)

Q("w16b_mixed_source", 4, "16e", "A source gives these corrected count rates with different absorbers. Explain which radiations the source emits.\n\n| absorber | none | paper | 5 mm aluminium | 2 cm lead |\n|---|---|---|---|---|\n| count rate / per min | 500 | 300 | 300 | 50 |",
  [P("paper reduces the count (500 → 300), so alpha is present", ["alpha"]),
   P("aluminium causes no further drop, so there is no beta", ["no beta", "not beta", "beta is absent", "no drop"]),
   P("radiation passes through aluminium and is reduced by lead, so gamma is present", ["gamma"])],
  "Paper reduces the count rate from 500 to 300, so alpha is present. Adding aluminium causes no further drop, so there is no beta. The radiation that passes through aluminium and is reduced (but not stopped) by lead is gamma. The source emits alpha and gamma.",
  ["What does paper stop?", "Does aluminium make any difference?", "What passes through aluminium but is reduced by lead?"],
  "alpha (paper drop) + gamma (through Al, reduced by lead); no beta",
  ["Alpha and gamma: paper reduces the count so there is alpha, aluminium makes no difference so no beta, and lead reduces the rest so gamma", "the source emits alpha and gamma but no beta"],
  ["Only beta", "Alpha and beta only"], min_points=3)

Q("w16b_storage_time", 4, "16g", "Hospital waste contains a nuclide with a half-life of 8 days. Explain how long it must be stored for its activity to fall to 1/16 of its original value.",
  [P("1/16 is four halvings (½, ¼, ⅛, 1/16)", ["four half-lives", "4 half-lives", "halved four times", "4 halvings"]),
   P("4 × 8 = 32 days", ["32 days", "32"])],
  "1/16 = ½ × ½ × ½ × ½, so four half-lives are needed. The storage time is 4 × 8 = 32 days.",
  ["How many halvings give 1/16?", "Multiply by the half-life.", "State the time."],
  "4 half-lives × 8 days = 32 days",
  ["1/16 is four half-lives, so 4 × 8 = 32 days", "it must be stored for 32 days"],
  ["128 days", "16 days"], min_points=1,
  pitfalls=[PF(["128 days", "16 days"], "1/16 needs FOUR halvings: 4 × 8 = 32 days.")])

Q("w16b_curve_after_15", 4, "16g", "Fig. 1 shows a decay curve with an initial activity of 800 counts per minute and a half-life of 5 minutes. Explain how to find the activity after 15 minutes, and give the value.",
  [P("15 minutes is three half-lives", ["three half-lives", "3 half-lives", "15 ÷ 5"]),
   P("800 → 400 → 200 → 100", ["400", "200"]),
   P("100 counts per minute", ["100"])],
  "15 minutes is 15 ÷ 5 = 3 half-lives. The activity halves three times: 800 → 400 → 200 → 100 counts per minute. (Reading the curve at 15 min gives the same value.)",
  ["How many half-lives is 15 minutes?", "Halve the activity that many times.", "Check on the curve."],
  "3 half-lives → 100 counts/min",
  ["15 minutes is three half-lives, so 800 halves to 400, 200, then 100 counts per minute", "after 3 half-lives the activity is 100"],
  ["0 counts per minute", "266 counts per minute"], min_points=2,
  figure=lambda: sk.decay_curve(800, 5))

Q("w16b_beta_tracer_worse", 4, "16h", "Explain why a beta-emitting tracer would be a poor choice for imaging an organ inside the body, compared with a gamma emitter.",
  [P("beta is absorbed by body tissue, so little reaches the detector outside", ["absorbed by the body", "absorbed by tissue", "does not escape", "cannot leave the body", "would not reach the detector"]),
   P("it is more ionising, so it damages more cells inside the body", ["more ionising", "damages more cells", "more damage", "ionises cells"]),
   P("gamma passes out of the body to the detector and is weakly ionising", ["gamma passes out", "gamma escapes", "gamma passes through", "weakly ionising", "reaches the detector"])],
  "Beta particles are absorbed within a few millimetres of tissue, so few would leave the body to reach the detector, and the image would be poor. Being more ionising, they would also damage more cells inside the body. Gamma passes out of the body to the detector and is only weakly ionising.",
  ["Can beta escape from inside the body?", "Which is more ionising?", "Why is gamma better?"],
  "beta absorbed in body (poor image, more damage); gamma escapes",
  ["Beta is absorbed by the body so it does not reach the detector and damages more cells, while gamma passes out of the body", "gamma escapes the body and is weakly ionising; beta is absorbed and causes more damage"],
  ["Beta is better because it is more penetrating than gamma", "Beta has a longer half-life"], min_points=2)

Q("w16b_sterilise_food", 4, "16h", "Some food is treated with gamma radiation before packing. Explain why this keeps the food fresh for longer, and why it is safe to eat.",
  [P("gamma kills bacteria and microbes in the food", ["kills bacteria", "kills microbes", "kills germs", "destroys bacteria", "destroys microbes"]),
   P("so the food does not go off (decay) as quickly", ["does not go off", "lasts longer", "stays fresh", "slows decay"]),
   P("the food does not become radioactive (no radioactive nuclei are added)", ["does not become radioactive", "not radioactive", "no radioactive", "not made radioactive"])],
  "Gamma radiation passes into the food and kills bacteria and other microbes, so the food does not go off as quickly. The food is safe to eat because it does not become radioactive: it is only exposed to radiation, and no radioactive nuclei are added to it.",
  ["What does gamma do to bacteria?", "How does that keep food fresh?", "Does the food become radioactive?"],
  "kills bacteria; food not made radioactive",
  ["Gamma kills the bacteria so the food lasts longer, and the food does not become radioactive", "it destroys microbes; no radioactive material is added so it is safe"],
  ["The food becomes radioactive but only slightly", "Gamma freezes the food"], min_points=2, pitfalls=[BECOMES_RADIOACTIVE])

Q("w16b_read_nuclide", 4, "16c", "A nuclide is written as ²³⁵₉₂U. Explain what the two numbers tell you and find the number of neutrons.",
  [P("235 is the nucleon number (protons + neutrons)", ["235 is the nucleon number", "nucleon number", "mass number", "protons and neutrons"]),
   P("92 is the proton number", ["92 is the proton number", "proton number", "atomic number", "number of protons"]),
   P("neutrons = 235 − 92 = 143", ["143"])],
  "The top number, 235, is the nucleon number A (protons + neutrons). The bottom number, 92, is the proton number Z. The number of neutrons is 235 − 92 = 143.",
  ["Which number is on top, and what does it count?", "What does the bottom number count?", "Subtract."],
  "A = 235, Z = 92, N = 143",
  ["235 is the nucleon number and 92 the proton number, so there are 143 neutrons", "the nucleus has 92 protons and 235 − 92 = 143 neutrons"],
  ["235 neutrons", "92 neutrons and 235 protons"], min_points=2)

Q("w16b_random_but_constant", 4, "16d", "Decay is random, yet a source's half-life is constant. Explain how both can be true.",
  [P("each individual nucleus decays at a random, unpredictable time", ["random", "individual nucleus", "unpredictable", "each nucleus"]),
   P("a sample contains a very large number of nuclei", ["very large number", "huge number", "millions", "large number"]),
   P("so on average a fixed fraction decays in a given time, giving a constant half-life", ["on average", "fixed fraction", "same fraction", "average", "half decay"])],
  "Each individual nucleus decays at a random, unpredictable moment. But a sample contains a very large number of nuclei, so on average the same fraction of them decays in each interval of time. That makes the time for half of them to decay, the half-life, constant.",
  ["Can you predict one nucleus?", "How many nuclei are in a sample?", "What does averaging over many give?"],
  "random individually; huge numbers → fixed fraction on average → constant half-life",
  ["Each nucleus decays randomly, but there are so many nuclei that on average a fixed fraction decays in a given time, so the half-life is constant", "random for one nucleus, predictable on average for a large number"],
  ["Because all nuclei decay at the same time", "Because half-life is random"], min_points=2)

Q("w16b_pilots", 4, "16f", "Airline pilots receive more background radiation than most people on the ground. Explain why.",
  [P("cosmic rays from space are a source of background radiation", ["cosmic rays", "cosmic", "from space"]),
   P("at high altitude there is less atmosphere above to absorb them", ["less atmosphere", "less air", "thinner atmosphere", "atmosphere absorbs", "high altitude"]),
   P("pilots spend many hours at altitude, so the dose builds up", ["many hours", "long time", "builds up", "frequently", "often"])],
  "Cosmic rays from space are a source of background radiation. The atmosphere absorbs much of it, but at high altitude there is less air above to absorb it. Pilots spend many hours at altitude, so their dose builds up.",
  ["Which background source comes from space?", "What normally shields us from it?", "Why does altitude matter?"],
  "cosmic rays; less atmosphere at altitude; many hours",
  ["They receive more cosmic rays because at high altitude there is less atmosphere to absorb them", "less air above them shields them from cosmic radiation, and they fly often"],
  ["Because aircraft engines are radioactive", "Because they are closer to the Sun's light"], min_points=2)

Q("w16b_alpha_range_gm", 4, "16e", "A GM tube is moved slowly away from a source. The count rate falls sharply to background at about 5 cm. Explain what this suggests about the source.",
  [P("the source emits alpha particles", ["alpha"]),
   P("alpha has a range of only a few centimetres in air", ["few centimetres", "few cm", "short range", "range in air", "absorbed by air"]),
   P("no beta or gamma, as these would still be detected beyond 5 cm", ["no beta or gamma", "no beta", "no gamma", "would still be detected", "only alpha"])],
  "The source emits alpha particles: alpha has a range of only a few centimetres in air, so beyond about 5 cm none reach the tube. Since the count falls all the way to background, the source emits no beta or gamma, which would still be detected further away.",
  ["Which radiation has a range of a few cm in air?", "What would beta or gamma do beyond 5 cm?", "Conclude."],
  "alpha only (short range in air)",
  ["It emits only alpha, because alpha has a range of a few cm in air and beta or gamma would still be detected", "the short range shows alpha with no beta or gamma"],
  ["It emits gamma", "The GM tube has broken"], min_points=2)

# ---------------------------------------------------------------- L5
Q("w16b_claim_irradiated", 5, "16h", "A student says: 'Medical instruments sterilised with gamma radiation become radioactive and are dangerous to use.' Evaluate this.",
  [P("wrong: exposing an object to gamma does not make it radioactive", ["wrong", "does not make it radioactive", "not radioactive", "does not become radioactive"]),
   P("no radioactive nuclei are added; the gamma passes through or is absorbed", ["no radioactive nuclei", "nothing radioactive is added", "passes through", "absorbed", "no radioactive material"]),
   P("the gamma kills bacteria, so the instruments are sterile and safe", ["kills bacteria", "sterile", "safe", "kills microbes"])],
  "The statement is wrong. Exposure to gamma radiation does not make an object radioactive, because no radioactive nuclei are added; the gamma simply passes through or is absorbed. It kills bacteria on the instruments, so they are sterile and safe to use.",
  ["Does irradiation add radioactive nuclei?", "What does the gamma do?", "Evaluate."],
  "wrong; irradiated ≠ radioactive; kills bacteria",
  ["Wrong: irradiating with gamma does not make the instruments radioactive; it just kills bacteria", "no radioactive material is added, so they are sterile and safe"],
  ["Correct, they glow afterwards", "Correct, gamma stays in the metal"], min_points=2, pitfalls=[BECOMES_RADIOACTIVE])

Q("w16b_claim_heat_half_life", 5, "16d", "A student suggests heating radioactive waste to make it decay faster. Evaluate this suggestion.",
  [P("it will not work: decay is spontaneous", ["will not work", "spontaneous", "does not work", "wrong"]),
   P("the half-life is not affected by temperature, pressure or chemical reactions", ["not affected", "temperature", "chemical", "unaffected", "cannot be changed", "does not change the half-life"]),
   P("the waste must instead be stored safely until its activity falls", ["stored", "storage", "wait", "store it safely"])],
  "The suggestion will not work. Radioactive decay is spontaneous: it happens inside the nucleus and is not affected by temperature, pressure or chemical reactions, so the half-life cannot be changed. The waste must instead be stored safely until its activity has fallen.",
  ["Does temperature affect the nucleus?", "Can the half-life be changed?", "What must be done instead?"],
  "won't work; spontaneous, unaffected by temperature; store",
  ["It will not work because decay is spontaneous and not affected by temperature, so the waste must be stored", "heating does not change the half-life; it must be stored safely"],
  ["Correct, heating speeds up decay", "Correct, it shortens the half-life"], min_points=2, pitfalls=[HALF_LIFE_CHANGES])

Q("w16b_claim_background_harmless", 5, "16f", "A student says: 'Background radiation is harmless because it is natural.' Evaluate this claim.",
  [P("natural radiation is just as ionising as artificial radiation", ["just as ionising", "still ionising", "same radiation", "ionising"]),
   P("the dose from background is usually low, so the risk is small but not zero", ["low dose", "small risk", "not zero", "low", "small"]),
   P("some places/sources (e.g. radon) give higher doses and increase the cancer risk", ["radon", "higher doses", "cancer", "some places", "granite"])],
  "The claim is wrong. Natural radiation is just as ionising as artificial radiation. Background doses are usually low, so the risk is small but not zero, and in some places, such as homes with high radon levels, the dose is higher and increases the risk of cancer.",
  ["Is natural radiation different from artificial radiation?", "How large is the usual dose?", "Are there places where it is higher?"],
  "wrong; still ionising; low dose, small risk; radon",
  ["Wrong: natural radiation is still ionising; the dose is usually low so the risk is small but not zero, and radon can give higher doses", "being natural does not make it harmless: it is still ionising, though the risk is small"],
  ["Correct, natural things are always safe", "Correct, background radiation is not ionising"], min_points=2)

Q("w16b_design_absorbers", 5, "16e", "Design an experiment to find which types of radiation a source emits.",
  [P("measure the background count rate first (and subtract it)", ["background", "subtract"]),
   P("measure the count rate with no absorber, then with paper, a few mm of aluminium and thick lead between the source and GM tube", ["paper", "aluminium", "lead", "absorbers"]),
   P("a drop with paper shows alpha, a drop with aluminium shows beta, radiation getting through aluminium and reduced by lead shows gamma", ["drop with paper", "alpha", "beta", "gamma"]),
   P("keep the distance fixed and count for a long time to reduce random error", ["same distance", "fixed distance", "long time", "repeat", "random"])],
  "Measure the background count rate with no source present. Place the source at a fixed distance from a GM tube and measure the count rate with no absorber, then with a sheet of paper, a few mm of aluminium and a thick lead sheet in between, counting each for several minutes. Subtract the background from each. A large drop with paper shows alpha; a further drop with aluminium shows beta; radiation that passes through aluminium and is reduced by lead is gamma.",
  ["What must you measure first?", "Which absorbers do you use?", "How do you interpret the results?"],
  "background; paper/Al/lead; interpret drops; fixed distance, long counts",
  ["Measure background, then count with no absorber, paper, aluminium and lead at a fixed distance; a drop with paper means alpha, with aluminium means beta, and what passes aluminium is gamma", "use paper, aluminium and lead absorbers and subtract the background"],
  ["Weigh the source", "Measure the temperature of the source"], min_points=2)

Q("w16b_claim_gamma_worst", 5, "16h", "A student says: 'Gamma is always the most dangerous radiation because it is the most penetrating.' Evaluate this.",
  [P("outside the body gamma is the most dangerous, because it penetrates skin and reaches organs", ["outside the body", "penetrates the skin", "reaches organs", "outside"]),
   P("inside the body alpha is the most dangerous, because it is the most ionising", ["inside the body", "alpha", "most ionising", "swallowed", "breathed in"]),
   P("so the danger depends on where the source is", ["depends", "where the source is", "not always"])],
  "The claim is not always true. Outside the body gamma is the most dangerous, because it can penetrate the skin and reach organs, while alpha is stopped by the skin. Inside the body, if a source is swallowed or breathed in, alpha is the most dangerous because it is the most strongly ionising and deposits all its energy in nearby cells. So the danger depends on where the source is.",
  ["Which is most dangerous outside the body?", "Which inside?", "Evaluate."],
  "outside: gamma; inside: alpha; depends",
  ["Not always: outside the body gamma is most dangerous, but inside the body alpha is, because it is the most ionising", "it depends where the source is; swallowed alpha is the worst"],
  ["Correct, gamma is always the worst", "Correct, alpha is harmless"], min_points=2)

Q("w16b_evaluate_short_counts", 5, "16g", "A student measures the half-life of a source by recording the count for only 10 seconds every minute, and gets a jagged graph. Evaluate the method and suggest improvements.",
  [P("decay is random, so short counts vary a lot (large random error)", ["random", "vary", "fluctuate", "random error", "too short"]),
   P("count for longer (or repeat and average) to reduce the effect of randomness", ["count for longer", "longer", "repeat", "average"]),
   P("subtract background and draw a smooth best-fit curve before reading the half-life", ["background", "best-fit", "smooth curve", "best fit"])],
  "Because decay is random, counts taken over only 10 seconds vary a lot, giving a large random error and a jagged graph. The student should count for longer (or repeat and average), subtract the background count, and draw a smooth best-fit curve before reading the time for the corrected count rate to halve.",
  ["Why do short counts vary so much?", "How can you reduce the variation?", "What else should be done with the data?"],
  "random → short counts vary; count longer; subtract background; best-fit curve",
  ["Decay is random, so 10 s counts vary a lot; count for longer, subtract background and draw a best-fit curve", "the counts are too short; repeat and average and use a smooth best-fit curve"],
  ["The method is perfect", "Use a weaker source so it decays faster"], min_points=2)

Q("w16b_claim_beta_shell", 5, "16e", "A student says: 'Beta particles are electrons knocked out of the outer shells of the atom.' Evaluate this.",
  [P("wrong: beta particles come from the nucleus", ["wrong", "from the nucleus", "come from the nucleus", "nucleus"]),
   P("a neutron changes into a proton, emitting a fast electron", ["neutron changes into a proton", "neutron becomes a proton", "neutron turns into a proton", "neutron to proton"]),
   P("so the proton number increases by 1 (a new element), which shell electrons could not do", ["proton number increases", "increases by 1", "new element", "z increases"])],
  "The statement is wrong. Beta particles come from the nucleus: a neutron changes into a proton and emits a fast-moving electron. This increases the proton number by 1, forming a new element, which removing shell electrons could never do.",
  ["Where does a beta particle originate?", "What changes inside the nucleus?", "What happens to the proton number?"],
  "wrong; from nucleus (n → p + e); Z increases by 1",
  ["Wrong: beta particles come from the nucleus when a neutron changes into a proton, so the proton number increases by 1", "they are emitted from the nucleus when a neutron turns into a proton, not from the shells"],
  ["Correct, they come from the outer shells", "Correct, beta is an ion"], min_points=2,
  pitfalls=[PF(["come from the outer shells", "from the outer shell"], "Beta particles come from the NUCLEUS.")])

Q("w16b_choose_shielding", 5, "16h", "A hospital uses a beta source in one room and a gamma source in another. Evaluate the shielding needed for each.",
  [P("beta: a few mm of aluminium (or thick perspex) is enough", ["few mm of aluminium", "aluminium", "perspex", "few millimetres"]),
   P("gamma: thick lead or concrete is needed", ["thick lead", "lead", "concrete"]),
   P("because gamma is far more penetrating; even lead only reduces it", ["more penetrating", "only reduces", "most penetrating", "not completely stopped"])],
  "The beta source needs only a few millimetres of aluminium (or thick perspex), which absorbs beta completely. The gamma source needs thick lead or concrete walls, because gamma is far more penetrating; even thick lead only reduces its intensity rather than stopping it completely.",
  ["What stops beta?", "What is needed for gamma?", "Why the difference?"],
  "beta: few mm Al; gamma: thick lead/concrete (more penetrating)",
  ["The beta source needs a few mm of aluminium, but the gamma source needs thick lead or concrete because gamma is more penetrating", "aluminium for beta, lead for gamma"],
  ["Paper for both", "Aluminium for gamma"], min_points=2)

Q("w16b_claim_isotopes_elements", 5, "16b", "A student says: 'Carbon-12 and carbon-14 are different elements because their nucleon numbers are different.' Evaluate this.",
  [P("wrong: the element is decided by the proton number", ["wrong", "proton number", "number of protons"]),
   P("both have 6 protons, so both are carbon", ["6 protons", "both carbon", "same number of protons", "both have 6"]),
   P("different nucleon numbers mean different numbers of neutrons: they are isotopes", ["isotopes", "different neutrons", "different numbers of neutrons", "neutrons"])],
  "The statement is wrong. An element is decided by its proton number. Both nuclei have 6 protons, so both are carbon. Their different nucleon numbers mean they have different numbers of neutrons, so they are isotopes of the same element.",
  ["What decides which element a nucleus is?", "How many protons do both have?", "What are they called?"],
  "wrong; same Z = same element; isotopes",
  ["Wrong: both have 6 protons, so both are carbon; they are isotopes with different numbers of neutrons", "the proton number decides the element, so they are isotopes, not different elements"],
  ["Correct, different A means different elements", "Correct, carbon-14 is nitrogen"], min_points=2)

Q("w16b_long_vs_short", 5, "16g", "Source P and source Q contain the same number of radioactive nuclei. P has a half-life of 2 hours and Q a half-life of 2000 years. Evaluate which is more hazardous.",
  [P("P has a much higher activity at first (more decays per second)", ["higher activity", "more decays", "more intense", "decays faster", "much more active", "intense"]),
   P("but P's activity falls quickly; after a few days it is negligible", ["falls quickly", "few days", "short time", "soon", "negligible", "brief"]),
   P("Q is less active but remains radioactive for thousands of years, needing long-term storage", ["thousands of years", "long-term", "long time", "remains radioactive", "stored for"])],
  "It depends on the timescale. With the same number of nuclei, P decays much faster, so its activity is far higher at first and it is more hazardous in the short term. But P's activity falls to almost nothing within a few days. Q is much less active, but it stays radioactive for thousands of years, so it is a long-term hazard that needs secure storage.",
  ["Which source has more decays per second at first?", "How long does each stay active?", "Evaluate."],
  "P: high activity, short-lived; Q: low activity, long-lived",
  ["P is more active at first but falls quickly, while Q is less active but remains radioactive for thousands of years", "it depends: P is intense but brief, Q is weak but lasts a long time"],
  ["Q is more active because its half-life is longer", "They are equally hazardous at all times"], min_points=2,
  pitfalls=[PF(["q is more active", "longer half-life means more active"], "A LONGER half-life means FEWER decays per second for the same number of nuclei.")])
