"""Chapter 1 Measurement: 50 more written-answer questions (10 per level), marked by keywords/phrases."""
from .. import figs, sketches
from ..marker import Pitfall, Point
from .base import written

P = Point
PF = Pitfall
CH = 1


def Q(id, lv, lo, stem, points, model, hints, keywords, passes, fails, pitfalls=(), min_points=None, figure=None):
    written(id, CH, lv, lo, stem=stem, points=points, model_answer=model, hints=hints, keywords=keywords,
            pitfalls=pitfalls, min_points=min_points, figure=figure, sample_pass=passes, sample_fail=fails)


# ---------------------------------------------------------------- L1
Q("w1b_why_units", 1, "1a", "A student writes 'the length of the bench is 2'. Explain why this is not a complete measurement.",
  [P("a measurement needs a unit as well as a number", ["needs a unit", "no unit", "missing a unit", "unit is missing", "without a unit", "must have a unit", "include the unit", "give a unit"]),
   P("without the unit we cannot tell the size (2 m, 2 cm, 2 km are very different)", ["2 m", "2 cm", "2 km", "cannot tell", "do not know how long", "could be metres", "could mean", "size is unknown", "very different"])],
  "A physical quantity has a numerical magnitude and a unit. '2' has no unit, so we cannot tell whether the bench is 2 m, 2 cm or 2 km long; the measurement should be written as, for example, 2 m.",
  ["What are the two parts of a physical quantity?", "Which part is missing?", "Explain why the missing part matters."],
  "number + unit; without the unit the size is unknown",
  ["It has no unit, so you cannot tell if it means 2 m or 2 cm", "the unit is missing: it could be 2 cm or 2 km, which are very different"],
  ["The number should be bigger", "Benches cannot be measured"], min_points=2)

Q("w1b_mega_micro", 1, "1c", "State what the prefixes mega (M) and micro (μ) mean, giving an example of each.",
  [P("mega means a million (10^6, × 1 000 000)", ["mega means a million", "mega is a million", "million", "1 000 000", "megawatt", "megahertz", "10^6"]),
   P("micro means a millionth (10^-6, ÷ 1 000 000)", ["millionth", "micro means one millionth", "0.000001", "micrometre", "microsecond", "10^-6", "micro is a millionth"])],
  "Mega (M) means a million, 10⁶: for example 1 MW = 1 000 000 W. Micro (μ) means a millionth, 10⁻⁶: for example 1 μm = 0.000001 m.",
  ["One prefix is very large and the other very small.", "Mega appears in 'megawatt'; micro in 'micrometre'.", "Give the factor and an example for each."],
  "mega = 10⁶ (million); micro = 10⁻⁶ (millionth)",
  ["Mega means a million, as in a megawatt, and micro means a millionth, as in a micrometre", "mega is 1 000 000 times and micro is one millionth"],
  ["Mega means a thousand and micro means a hundredth", "They both mean small"],
  pitfalls=[PF(["mega means a thousand", "mega is a thousand", "micro means a thousandth", "micro is a thousandth"], "A thousand is kilo and a thousandth is milli. Mega = 10⁶ and micro = 10⁻⁶.")])

Q("w1b_giga_nano", 1, "1c", "State what the prefixes giga (G) and nano (n) mean, giving an example of where each is used.",
  [P("giga means a thousand million (10^9)", ["thousand million", "billion", "1 000 000 000", "gigabyte", "gigahertz", "10^9"]),
   P("nano means a thousand-millionth (10^-9)", ["thousand millionth", "billionth", "0.000000001", "nanometre", "nanosecond", "10^-9"])],
  "Giga (G) means a thousand million, 10⁹, as in a 2 GHz processor. Nano (n) means a thousand-millionth, 10⁻⁹, as in the wavelength of light, about 500 nm.",
  ["Both are powers of ten with 9 in them.", "One multiplies by a thousand million, the other divides by it.", "Give the meaning and an example of each."],
  "giga = 10⁹; nano = 10⁻⁹",
  ["Giga is a thousand million as in gigahertz, and nano is a thousand millionth as in nanometres", "giga means a billion and nano means a billionth, for example a nanosecond"],
  ["Giga means a hundred and nano means ten", "They are units of mass"])

Q("w1b_two_vectors", 1, "1f", "Name two vector quantities and state what they have in common.",
  [P("names two vectors, e.g. velocity, displacement, force, acceleration, weight", ["velocity", "displacement", "force", "acceleration", "weight", "momentum"]),
   P("vectors have both magnitude (size) and direction", ["magnitude and direction", "size and direction", "have a direction", "direction as well", "both size and direction", "need a direction"])],
  "Velocity and force are vector quantities. Both have a magnitude (size) and a direction, so a direction must be given to describe them fully.",
  ["Think of quantities you would describe with an arrow.", "What does a vector have that a scalar does not?", "Name two and give the common feature."],
  "e.g. velocity, force; magnitude and direction",
  ["Velocity and force are vectors; they have magnitude and direction", "displacement and acceleration both have a size and a direction"],
  ["Mass and time, which have only size", "Speed and energy are vectors"], min_points=2,
  pitfalls=[PF(["speed is a vector", "mass is a vector", "energy is a vector", "time is a vector"], "Speed, mass, energy and time are SCALARS: they have magnitude only.")])

Q("w1b_two_scalars", 1, "1f", "Name two scalar quantities and explain why they are scalars.",
  [P("names two scalars, e.g. mass, time, speed, distance, energy, temperature, volume", ["mass", "time", "speed", "distance", "energy", "temperature", "volume", "density"]),
   P("scalars have magnitude only, no direction", ["magnitude only", "only magnitude", "size only", "only size", "no direction", "do not have a direction", "without direction", "direction is not needed"])],
  "Mass and temperature are scalars. They have magnitude only: a mass of 3 kg or a temperature of 20 °C needs no direction to describe it fully.",
  ["Which quantities can you describe with just a number and a unit?", "Does a temperature point anywhere?", "Name two and explain."],
  "e.g. mass, time, energy; magnitude only",
  ["Mass and time are scalars because they have magnitude only", "temperature and energy have size only and no direction"],
  ["Force and velocity, because they have direction", "Scalars are measured with a scale"], min_points=2,
  pitfalls=[PF(["force is a scalar", "velocity is a scalar", "displacement is a scalar", "acceleration is a scalar"], "Force, velocity, displacement and acceleration are VECTORS: they have direction.")])

Q("w1b_precision_meaning", 1, "1e", "State what is meant by the precision of a measuring instrument, using a metre rule as an example.",
  [P("precision is the smallest change / smallest division the instrument can measure", ["smallest division", "smallest change", "smallest value it can measure", "smallest scale division", "smallest difference", "smallest unit it can read", "smallest reading"]),
   P("a metre rule has a precision of 1 mm (0.1 cm)", ["1 mm", "0.1 cm", "one millimetre", "nearest millimetre", "nearest mm"])],
  "The precision of an instrument is the smallest change in a quantity it can measure, set by its smallest scale division. A metre rule has a precision of 1 mm (0.1 cm).",
  ["Look at the smallest marks on a metre rule.", "Precision is about the smallest step the instrument can show.", "Define it and give the metre rule's value."],
  "smallest division it can measure; metre rule 1 mm",
  ["The smallest division it can measure; for a metre rule it is 1 mm", "precision is the smallest change the instrument can read, 0.1 cm for a metre rule"],
  ["The largest length the instrument can measure", "How heavy the instrument is"])

Q("w1b_range_meaning", 1, "1e", "State what is meant by the range of a measuring instrument, and give the range of a typical metre rule.",
  [P("range is the span of values from the smallest to the largest the instrument can measure", ["largest value", "biggest value", "maximum", "smallest to the largest", "from 0 to", "span of values", "how much it can measure", "largest reading"]),
   P("a metre rule measures from 0 to 1 m (100 cm)", ["1 m", "100 cm", "one metre", "0 to 100", "up to a metre", "up to 1 m"])],
  "The range of an instrument is the span of values it can measure, from the smallest to the largest reading. A metre rule has a range of 0 to 1 m (0 to 100 cm).",
  ["Range is about how BIG a quantity the instrument can handle.", "What is the longest length a metre rule can measure in one go?", "Define range and give the value."],
  "span from smallest to largest value; metre rule 0–1 m",
  ["Range is the largest value it can measure; for a metre rule 0 to 100 cm", "the span from the smallest to the largest reading, up to 1 m for a metre rule"],
  ["Range is the smallest division", "The colour of the scale"])

Q("w1b_rule_precision_use", 1, "1e", "State the precision of a metre rule and name one length it is suitable for measuring, explaining your choice.",
  [P("precision 1 mm (0.1 cm)", ["1 mm", "0.1 cm", "one millimetre", "nearest millimetre", "nearest mm"]),
   P("suitable for lengths of a few cm up to 1 m, e.g. a desk, a book, a pendulum length", ["desk", "table", "book", "pendulum", "length of a", "between", "up to 1 m", "few centimetres", "door", "bench"]),
   P("because the length is large compared with 1 mm, so the error is small", ["large compared", "much bigger than 1 mm", "error is small", "small percentage", "small compared", "within the range"])],
  "A metre rule has a precision of 1 mm. It is suitable for measuring the length of a pendulum or a book, because these lengths are within its 1 m range and are large compared with 1 mm, so the reading error is small.",
  ["What are the smallest marks on a metre rule?", "Which everyday lengths fit within 1 m but are much bigger than 1 mm?", "Give the precision, an example and a reason."],
  "precision 1 mm; lengths of a few cm to 1 m",
  ["It reads to 1 mm, so it is good for measuring the length of a book, which is large compared with 1 mm", "precision 0.1 cm; use it for a pendulum length up to 1 m because the error is small"],
  ["It reads to 0.01 mm and is used for wires", "It is used to measure mass"], min_points=2)

Q("w1b_vernier_precision_use", 1, "1e", "Fig. 1 shows a pair of vernier calipers. State their precision and name one thing they are suitable for measuring.",
  [P("precision 0.01 cm (0.1 mm)", ["0.01 cm", "0.1 mm", "tenth of a millimetre", "nearest 0.1 mm", "nearest 0.01 cm"]),
   P("suitable for lengths/diameters of a few mm to about 15 cm, including internal diameters and depths", ["diameter of a", "internal diameter", "test tube", "beaker", "coin", "bolt", "pipe", "depth", "marble", "up to 15 cm", "inside jaws"])],
  "Vernier calipers have a precision of 0.01 cm (0.1 mm). They are suitable for measuring objects from a few millimetres up to about 15 cm, such as the diameter of a coin or the internal diameter of a test tube.",
  ["What is the value of the smallest reading on the vernier scale?", "Calipers have outside jaws, inside jaws and a depth probe.", "Give the precision and an example."],
  "0.01 cm; diameters of coins, tubes, internal diameters",
  ["They read to 0.01 cm and can measure the diameter of a coin", "precision 0.1 mm, good for the internal diameter of a test tube"],
  ["They read to 1 cm and measure the length of a room", "They measure mass to 0.1 g"],
  figure=lambda: figs.vernier(23.4))

Q("w1b_one_oscillation", 1, "1e", "Fig. 1 shows a simple pendulum. Describe what is meant by one complete oscillation of the pendulum.",
  [P("the bob moves from one end of its swing to the other end and back again", ["to the other side and back", "to the other end and back", "back to where it started", "returns to its starting position", "there and back", "one side to the other and back", "back to the same position"]),
   P("(or) it passes the same point twice, moving in the same direction the second time", ["same point", "same direction", "same position moving the same way", "passes the centre twice"])],
  "One complete oscillation is a full swing: the bob moves from one end of its swing to the other end and then back to where it started, so that it passes the same point again moving in the same direction.",
  ["Is half a swing (one side to the other) a complete oscillation?", "The bob must get back to where it began.", "Describe the full journey."],
  "from one end to the other and back again",
  ["The bob swings from one side to the other and back to where it started", "it goes there and back, returning to its starting position"],
  ["The bob swings from one side to the other side once", "The time it takes to stop swinging"], min_points=1,
  pitfalls=[PF(["one side to the other side once", "from one side to the other only"], "A swing from one side to the other is only HALF an oscillation; it must come back.")],
  figure=lambda: sketches.pendulum_sketch())

# ---------------------------------------------------------------- L2
Q("w1b_worn_rule_end", 2, "1e", "The end of a wooden rule is worn. Explain how a student should measure the length of a pencil with it.",
  [P("do not start from the worn zero end; line the pencil up with another mark, e.g. 1.0 cm", ["do not use the end", "start from 1 cm", "start at the 1.0", "another mark", "not from the end", "start at a clear mark", "clear mark", "begin at 1", "line up with the 1 cm", "1.0 cm", "line it up with a mark"]),
   P("read both ends and subtract the starting reading from the end reading", ["subtract", "difference between", "minus the starting", "take away", "end reading − start", "end reading minus"])],
  "Because the zero end is worn, the student should not measure from it. Instead, line one end of the pencil up with a clear mark such as 1.0 cm, read the mark at the other end, and subtract the starting reading to find the length.",
  ["Why is measuring from a worn end a problem?", "Start from another mark instead.", "How do you then get the length?"],
  "start from a clear mark (e.g. 1 cm) and subtract",
  ["Start from the 1 cm mark instead of the worn end and subtract 1 cm from the reading", "line it up with another mark and take the difference between the two readings"],
  ["Start from the worn end because it is zero", "Press harder on the rule"])

Q("w1b_m2_to_cm2", 2, "1c", "Explain why 1 m² is equal to 10 000 cm², not 100 cm².",
  [P("1 m = 100 cm", ["1 m = 100 cm", "100 cm in a metre", "a metre is 100 cm", "1 m is 100 cm", "sides are 100 cm", "side is 100 cm", "sides of 100 cm"]),
   P("an area of 1 m² is 100 cm × 100 cm = 10 000 cm² (the conversion is squared)", ["100 cm × 100 cm", "100 × 100", "10 000", "squared", "both sides", "multiply by 100 twice", "two dimensions"])],
  "1 m = 100 cm. A square of side 1 m has sides of 100 cm, so its area is 100 cm × 100 cm = 10 000 cm². The conversion factor is squared because area involves two lengths.",
  ["How many cm are in 1 m?", "A 1 m² square has two sides, each 100 cm.", "Multiply."],
  "1 m = 100 cm; area = 100 × 100 = 10 000 cm²",
  ["1 m is 100 cm, so 1 m² is 100 cm × 100 cm = 10 000 cm²", "both sides are 100 cm so the factor is 100 × 100, which is 10 000"],
  ["Because 1 m = 100 cm so 1 m² = 100 cm²", "Because area has no unit"],
  pitfalls=[PF(["1 m2 = 100 cm2", "1 m2 is 100 cm2"], "Area needs the factor twice: 100 × 100 = 10 000.")])

Q("w1b_m3_to_cm3", 2, "1c", "Explain why 1 m³ is equal to 1 000 000 cm³.",
  [P("1 m = 100 cm", ["1 m = 100 cm", "100 cm in a metre", "a metre is 100 cm", "1 m is 100 cm", "sides of 100 cm", "sides are 100 cm", "side is 100 cm"]),
   P("a cube of side 1 m has volume 100 × 100 × 100 cm³ = 1 000 000 cm³ (factor cubed)", ["100 × 100 × 100", "100 cm × 100 cm × 100 cm", "1 000 000", "million", "cubed", "three dimensions", "three times"])],
  "1 m = 100 cm. A cube of side 1 m measures 100 cm on each side, so its volume is 100 × 100 × 100 = 1 000 000 cm³. The factor is cubed because volume involves three lengths.",
  ["How many cm are in 1 m?", "A cube has three dimensions.", "Multiply 100 by itself three times."],
  "1 m = 100 cm; 100³ = 10⁶ cm³",
  ["1 m is 100 cm so 1 m³ is 100 × 100 × 100 = 1 000 000 cm³", "the cube has sides of 100 cm, so the volume is a million cm³ because the factor is cubed"],
  ["Because 1 m = 100 cm so 1 m³ = 100 cm³", "Volume is always a million"])

Q("w1b_displacement_volume", 2, "1e", "Fig. 1 shows a measuring cylinder before and after a stone is added. Describe how to find the volume of an irregular stone this way.",
  [P("partly fill a measuring cylinder with water and read the volume", ["partly fill", "pour water", "fill with water", "read the initial", "first reading", "volume before"]),
   P("lower the stone in gently (e.g. on a thread) so it is fully submerged, then read the new volume", ["lower the stone", "put the stone in", "add the stone", "fully submerged", "completely covered", "on a thread", "new volume", "second reading", "volume after"]),
   P("volume of stone = final reading − initial reading", ["subtract", "difference", "minus", "final − initial", "rise in level", "increase in volume"])],
  "Partly fill a measuring cylinder with water and record the volume. Lower the stone in gently on a thread so that it is completely under water and record the new volume. The volume of the stone is the final reading minus the initial reading.",
  ["What happens to the water level when the stone goes in?", "You need two readings.", "How do you get the stone's volume from them?"],
  "water level before and after; subtract",
  ["Read the water level, lower the stone in until it is fully submerged, read again and subtract", "fill with water, note the volume, add the stone, then the rise in level is its volume"],
  ["Measure its length, width and height with a ruler", "Weigh the stone on a balance"], min_points=2,
  figure=lambda: figs.two_cylinders(40, 56))

Q("w1b_fiducial_marker", 2, "1e", "Fig. 1 shows a pendulum. When timing it, a student places a marker at the centre of the swing and starts and stops the stopwatch as the bob passes the marker. Explain why.",
  [P("the bob moves fastest at the centre (lowest point)", ["fastest", "moving quickly", "highest speed", "moves fastest at the centre", "quickest"]),
   P("so the moment it passes is easier to judge precisely, reducing timing error", ["easier to judge", "easier to see", "more precise", "reduces error", "less error", "more accurate", "exact moment"]),
   P("at the ends the bob moves slowly/stops briefly, so it is hard to tell exactly when it turns", ["at the ends it slows", "slow at the ends", "stops at the ends", "hard to judge at the end", "turning point", "difficult to tell"])],
  "The bob moves fastest as it passes the centre of its swing, so the instant it passes the marker is easy to judge precisely. At the ends of the swing it slows down and stops briefly, so it is hard to tell exactly when it turns. Using the marker reduces the timing error.",
  ["Where is the bob moving fastest?", "Is it easier to judge the moment a fast or a slow object passes a point?", "Compare the centre with the ends."],
  "fastest at centre, easier to judge; slow at ends",
  ["The bob is fastest at the centre so it is easier to judge exactly when it passes, giving less error", "at the ends it slows and stops so it is hard to judge; at the centre it moves quickly so timing is more precise"],
  ["The bob is slowest at the centre", "The marker makes the pendulum swing faster"], min_points=2,
  pitfalls=[PF(["slowest at the centre", "slowest in the middle"], "The bob is FASTEST at the centre and slowest at the ends.")],
  figure=lambda: sketches.pendulum_sketch("marker at the centre"))

Q("w1b_coin_stack", 2, "1e", "Describe how to find the thickness of one coin using a ruler and 20 identical coins.",
  [P("stack the 20 coins and measure the height of the stack with the ruler", ["stack", "pile", "height of the stack", "measure the stack", "put them on top of each other"]),
   P("divide the height by 20", ["divide by 20", "÷ 20", "/ 20", "divided by 20", "divide the height by the number"]),
   P("this gives a more precise value because the ruler's 1 mm error is shared over 20 coins", ["more precise", "more accurate", "error is shared", "smaller error", "1 mm is small", "reduces the error"])],
  "Stack the 20 coins neatly and measure the height of the stack with the ruler. Divide the height by 20 to get the thickness of one coin. This is more precise than measuring one coin, because the 1 mm uncertainty of the ruler is shared over 20 coins.",
  ["One coin is too thin to measure accurately with a ruler.", "What if you measure many coins together?", "Then divide."],
  "stack, measure height, divide by 20; error shared",
  ["Stack the 20 coins, measure the height of the stack and divide by 20, which is more precise", "measure the pile of coins with the ruler and divide by 20"],
  ["Measure one coin with the ruler and multiply by 20", "Weigh the coins"], min_points=2)

Q("w1b_circumference_string", 2, "1e", "Describe how to measure the circumference of a can using a piece of string and a metre rule.",
  [P("wrap the string once round the can and mark (or hold) where it meets", ["wrap the string", "wind the string", "around the can", "round the can", "mark the string", "where it overlaps", "where it meets"]),
   P("straighten the string and measure that length with the metre rule", ["straighten", "lay it along the rule", "measure the length of the string", "against the metre rule", "measure the string"])],
  "Wrap the string tightly once around the can and mark the point where it meets itself. Then straighten the string out along the metre rule and measure the length between the marks; this is the circumference.",
  ["A rule cannot bend round a can.", "What can bend round it?", "How do you then measure that length?"],
  "wrap string once round, mark, straighten, measure",
  ["Wrap the string round the can, mark where it meets, then straighten it and measure it with the rule", "wind string around once, mark it and measure the string against the metre rule"],
  ["Measure across the top of the can with the ruler", "Weigh the string"])

Q("w1b_balance_liquid_mass", 2, "1e", "Describe how to find the mass of some water in a beaker using an electronic balance.",
  [P("measure the mass of the empty beaker (or zero/tare the balance with the beaker on it)", ["empty beaker", "tare", "zero the balance", "mass of the beaker", "reset to zero", "press zero"]),
   P("add the water and measure the mass again", ["add the water", "pour in the water", "with the water", "measure again", "full beaker"]),
   P("mass of water = full − empty (or the reading after taring)", ["subtract", "difference", "minus", "take away", "reading after taring", "full minus empty"])],
  "Place the empty beaker on the balance and record its mass (or press 'tare' to zero the balance with the beaker on it). Pour in the water and record the new reading. The mass of the water is the full reading minus the empty reading, or simply the reading after taring.",
  ["The balance measures everything on it, including the beaker.", "How can you remove the beaker's mass?", "Two readings, or use the zero button."],
  "empty beaker mass (or tare), then with water; subtract",
  ["Weigh the empty beaker, add the water, weigh again and subtract", "put the beaker on the balance, press tare to zero it, then add the water and read the mass"],
  ["Pour the water straight onto the balance pan", "Use a ruler to measure the water"], min_points=2)

Q("w1b_read_thermometer", 2, "1e", "Describe how to read a liquid-in-glass thermometer correctly when measuring the temperature of warm water.",
  [P("keep the bulb in the water and wait until the reading is steady", ["wait", "steady", "stops rising", "stops changing", "stable", "bulb in the water", "keep the bulb"]),
   P("read with the eye level with the top of the liquid thread to avoid parallax error", ["eye level", "level with", "perpendicular", "avoid parallax", "parallax", "straight on"])],
  "Keep the bulb fully in the water and wait until the liquid thread stops moving so the reading is steady. Then read the scale with your eye level with the top of the thread, to avoid parallax error.",
  ["Does the thermometer show the right temperature immediately?", "Where should your eye be?", "Describe both steps."],
  "bulb in water, wait for steady reading; eye level, avoid parallax",
  ["Keep the bulb in the water, wait until it is steady and read with my eye level with the liquid", "wait for the reading to stop changing and avoid parallax by reading straight on"],
  ["Take it out of the water and read it later", "Shake it before reading"], min_points=2)

Q("w1b_velocity_incomplete", 2, "1f", "A report says 'the plane's velocity was 250 m/s'. Explain why this statement is incomplete, and how to correct it.",
  [P("velocity is a vector, so it needs a direction", ["vector", "needs a direction", "direction is missing", "no direction", "must give a direction", "without a direction"]),
   P("add a direction, e.g. 250 m/s due north (or call 250 m/s the speed)", ["due north", "north", "east", "south", "west", "add the direction", "call it speed", "it is the speed", "250 m/s towards"])],
  "Velocity is a vector quantity, so it needs a direction as well as a magnitude. The statement should give the direction, for example '250 m/s due north'; otherwise 250 m/s is only the plane's speed.",
  ["Is velocity a scalar or a vector?", "What does a vector need besides a size?", "How would you rewrite the statement?"],
  "velocity is a vector; add a direction",
  ["Velocity is a vector so it needs a direction, for example 250 m/s due east", "the direction is missing; say 250 m/s north, or call it a speed"],
  ["The number is too large", "It should be in km/h"], min_points=2)

# ---------------------------------------------------------------- L3
Q("w1b_repeat_average", 3, "1e", "Explain why a student should take repeated readings of a measurement and calculate the average.",
  [P("individual readings vary because of random errors (e.g. reaction time, reading the scale)", ["readings vary", "random error", "each reading is different", "reaction time", "not exactly the same", "slightly different"]),
   P("averaging reduces the effect of these errors / gives a more reliable or accurate value", ["more reliable", "more accurate", "reduces the error", "reduces the effect", "errors cancel", "closer to the true value", "average out"]),
   P("repeats also let you spot and discard anomalous readings", ["anomalous", "odd reading", "spot mistakes", "outlier", "identify errors", "discard"])],
  "Repeated readings of the same quantity vary slightly because of random errors, such as reaction time or misreading a scale. Averaging the readings reduces the effect of these errors and gives a more reliable value, and repeats also make it easy to spot and discard an anomalous reading.",
  ["Do repeated measurements of the same thing always agree exactly?", "What happens to random errors when you average?", "What else do repeats allow you to do?"],
  "random errors; averaging reduces them; spot anomalies",
  ["Readings vary because of random errors, so averaging gives a more reliable value and lets you spot anomalous ones", "each reading is slightly different; taking the average reduces the effect of errors"],
  ["To make the experiment take longer", "Because the first reading is always wrong"], min_points=2)

Q("w1b_zero_error_averaging", 3, "1e", "A micrometer has a zero error of +0.04 mm. Explain why taking an average of many readings does not remove this error, and how it should be dealt with.",
  [P("the zero error affects every reading by the same amount (systematic), so the average has it too", ["every reading", "each reading", "same amount", "all readings", "systematic", "always too large", "does not average out", "same error"]),
   P("subtract the zero error from each reading (or from the average): corrected = reading − 0.04 mm", ["subtract", "minus 0.04", "take away 0.04", "reading − zero error", "correct each reading", "corrected reading"])],
  "A zero error makes every reading too large by the same amount, 0.04 mm, so averaging many readings still gives a result 0.04 mm too large. It must be corrected by subtracting the zero error from each reading (or from the mean): corrected reading = reading − 0.04 mm.",
  ["Does a zero error make some readings too big and others too small?", "What happens when you average readings that are all 0.04 mm too big?", "How do you correct for it?"],
  "zero error is the same in every reading; subtract it",
  ["The zero error is in every reading by the same amount so averaging does not remove it; subtract 0.04 mm from each", "it is a systematic error, so I must subtract the zero error from the average"],
  ["Averaging cancels every kind of error", "Add 0.04 mm to each reading"],
  pitfalls=[PF(["averaging cancels every", "averaging removes all errors", "add 0.04", "add the zero error"], "A positive zero error is SUBTRACTED, and averaging cannot remove an error that is the same every time.")])

Q("w1b_stopwatch_vs_clock", 3, "1e", "Explain why a stopwatch is more suitable than a wall clock for timing a 100 m sprint.",
  [P("a sprint lasts only about 10–15 s, so the time must be measured precisely", ["only a few seconds", "short time", "about 10 s", "short event", "small time", "10 seconds"]),
   P("a stopwatch reads to 0.01 s (or 0.1 s), a wall clock only to the nearest second", ["0.01 s", "0.1 s", "nearest second", "1 s", "more precise", "smaller divisions", "hundredths"]),
   P("so the stopwatch gives a much smaller percentage error / can tell close runners apart", ["smaller error", "percentage error", "more accurate", "tell runners apart", "close finishes", "big error"])],
  "A 100 m sprint takes only about 10–15 s, so the time must be measured precisely. A stopwatch reads to 0.01 s, whereas a wall clock reads only to the nearest second, which would be a large percentage error and could not separate close runners.",
  ["How long does a sprint take?", "Compare the smallest time each device can show.", "Why does that matter for a short event?"],
  "short event; stopwatch 0.01 s vs clock 1 s; smaller error",
  ["The race is only about 10 s, and a stopwatch reads to 0.01 s while a clock reads to 1 s, so the error is much smaller", "a stopwatch is more precise, reading hundredths of a second, which matters for a short event"],
  ["A wall clock is bigger and easier to see", "Stopwatches are cheaper"], min_points=2)

Q("w1b_micrometer_or_vernier", 3, "1e", "A student must measure (a) the diameter of a ball bearing about 3 mm across and (b) the internal diameter of a pipe about 3 cm across. Choose an instrument for each and explain.",
  [P("(a) a micrometer screw gauge, because it reads to 0.01 mm for a small external diameter", ["micrometer", "screw gauge", "0.01 mm"]),
   P("(b) vernier calipers using the inside jaws, because a micrometer cannot measure an internal diameter", ["vernier", "calipers", "inside jaws", "internal jaws", "cannot measure inside", "internal"]),
   P("the precision suits each size (0.01 mm for 3 mm; 0.1 mm for 3 cm)", ["0.1 mm", "0.01 cm", "small object", "precise enough", "range"])],
  "For the 3 mm ball bearing, use a micrometer screw gauge: it measures small external diameters to 0.01 mm. For the internal diameter of the pipe, use vernier calipers with the inside jaws: a micrometer cannot measure internal dimensions, and calipers read to 0.1 mm, which is precise enough for 3 cm.",
  ["Which instrument is most precise for small external diameters?", "Which instrument has jaws for measuring inside a tube?", "Give a reason for each choice."],
  "(a) micrometer 0.01 mm; (b) vernier inside jaws",
  ["Use a micrometer for the ball bearing because it reads to 0.01 mm, and vernier calipers with the inside jaws for the pipe", "micrometer screw gauge for (a); vernier calipers for the internal diameter in (b) since a micrometer cannot measure inside"],
  ["A metre rule for both", "A measuring cylinder for the pipe"], min_points=2)

Q("w1b_paper_thickness_rule", 3, "1e", "Explain how a student could measure the thickness of one sheet of paper using only a ruler, and why this method works.",
  [P("measure the thickness of a large stack (e.g. 100 or 200 sheets) with the ruler", ["stack", "pile", "100 sheets", "200 sheets", "many sheets", "ream", "whole book"]),
   P("divide by the number of sheets", ["divide by", "÷", "per sheet", "divided by the number"]),
   P("the ruler's 1 mm uncertainty is small compared with the thick stack, so the result is precise", ["1 mm is small", "small compared", "error is shared", "smaller percentage error", "more precise", "more accurate"])],
  "Measure the thickness of a large stack of, say, 200 identical sheets with the ruler, then divide by 200. One sheet is far thinner than the ruler's 1 mm divisions, but the stack is several centimetres thick, so the 1 mm uncertainty becomes small compared with the measurement and is shared among all the sheets.",
  ["One sheet is much thinner than 1 mm.", "How can you make the thing being measured bigger?", "Then how do you get back to one sheet?"],
  "stack of many sheets, measure, divide; error becomes small",
  ["Measure a stack of 200 sheets with the ruler and divide by 200, so the 1 mm error is small compared with the stack", "measure many sheets together, divide by the number of sheets; the error is shared"],
  ["Measure one sheet with the ruler very carefully", "Fold the sheet in half"], min_points=2)

Q("w1b_resultant_same_opposite", 3, "1f", "Two forces of 6 N and 8 N act on an object. Explain what their resultant is when they act (a) in the same direction and (b) in opposite directions.",
  [P("(a) same direction: they add, 14 N", ["14 n", "6 + 8", "add", "add together"]),
   P("(b) opposite directions: they subtract, 2 N in the direction of the 8 N force", ["2 n", "8 − 6", "8 - 6", "subtract", "difference", "direction of the 8"]),
   P("because forces are vectors, so direction affects how they combine", ["vector", "direction matters", "direction affects", "depends on direction"])],
  "Forces are vectors, so their directions affect how they combine. (a) In the same direction they add: 6 + 8 = 14 N. (b) In opposite directions they subtract: 8 − 6 = 2 N, acting in the direction of the 8 N force.",
  ["Forces have direction.", "Same direction: combine how? Opposite: combine how?", "Give both values."],
  "same: 14 N; opposite: 2 N; vectors",
  ["In the same direction they add to 14 N; in opposite directions the resultant is 2 N in the direction of the 8 N force", "14 N when they act the same way and 2 N when opposite, because force is a vector"],
  ["Always 14 N", "Always 2 N"], min_points=2)

Q("w1b_why_prefixes", 3, "1c", "Explain why scientists use prefixes such as milli and mega when writing very small or very large quantities. Give an example.",
  [P("prefixes avoid writing many zeros / make numbers shorter and easier to read and compare", ["avoid zeros", "many zeros", "shorter", "easier to read", "easier to write", "convenient", "less mistakes", "fewer mistakes"]),
   P("example: 0.003 m = 3 mm, or 2 000 000 W = 2 MW", ["3 mm", "2 mw", "mm", "mw", "km", "kilogram", "microsecond", "megawatt", "millisecond", "e.g."])],
  "Prefixes let very large or very small numbers be written without long strings of zeros, so they are shorter, easier to read and compare, and less likely to be miscopied. For example, 0.003 m can be written as 3 mm, and 2 000 000 W as 2 MW.",
  ["Write 0.000005 s and 5 μs side by side.", "Which is easier to read?", "Explain and give an example."],
  "avoid long strings of zeros; easier to read; example",
  ["They avoid writing lots of zeros, so 2 000 000 W can be written as 2 MW, which is easier to read", "it is shorter and easier: 0.003 m is just 3 mm"],
  ["Because prefixes make the quantity bigger", "To change the unit into a different quantity"],
  pitfalls=[PF(["make the quantity bigger", "change the size of the quantity"], "A prefix does not change the size of the quantity, only how it is written.")])

Q("w1b_record_vernier_dp", 3, "1e", "A student reads vernier calipers and records the length as '2.4 cm'. The teacher says it should be '2.40 cm'. Explain why.",
  [P("vernier calipers have a precision of 0.01 cm", ["0.01 cm", "0.1 mm", "precision of the calipers", "read to two decimal places"]),
   P("a reading should be recorded to the precision of the instrument, so two decimal places in cm", ["to the precision", "two decimal places", "2 decimal places", "shows the precision", "same precision", "how precise"]),
   P("writing 2.4 cm suggests it was only measured to 0.1 cm", ["suggests 0.1 cm", "less precise", "only to 0.1", "loses information", "looks less precise"])],
  "Vernier calipers measure to 0.01 cm, so readings should be recorded to that precision, with two decimal places in centimetres. Writing 2.4 cm suggests the length was only measured to the nearest 0.1 cm and throws away information; 2.40 cm shows the reading really is 2.40 to the nearest 0.01 cm.",
  ["What is the precision of vernier calipers?", "How many decimal places does that need in cm?", "What does 2.4 cm suggest about the measurement?"],
  "precision 0.01 cm; record to 2 d.p.",
  ["The calipers read to 0.01 cm, so the reading should show two decimal places; 2.4 cm looks less precise", "you record to the precision of the instrument, which is 0.01 cm"],
  ["Because 2.40 is bigger than 2.4", "Zeros make the number look neater"], min_points=2)

Q("w1b_roundabout_velocity", 3, "1f", "A car drives round a roundabout at a steady 10 m/s. Explain whether its speed and its velocity are constant.",
  [P("its speed is constant (10 m/s)", ["speed is constant", "speed stays", "speed does not change", "constant speed", "same speed"]),
   P("its velocity changes because its direction keeps changing (velocity is a vector)", ["velocity changes", "direction changes", "direction keeps changing", "velocity is not constant", "changing direction"])],
  "The car's speed is constant at 10 m/s. Its velocity is not constant, because velocity is a vector and the car's direction keeps changing as it goes round the roundabout.",
  ["What does speed measure, and what does velocity measure?", "Does the car's direction change?", "Comment on each."],
  "speed constant; velocity changes (direction changes)",
  ["The speed is constant but the velocity changes because its direction keeps changing", "same speed of 10 m/s; velocity is a vector and the direction changes"],
  ["Both are constant because it goes at 10 m/s", "The speed changes but the velocity stays the same"],
  pitfalls=[PF(["velocity is constant", "velocity stays the same", "velocity does not change"], "Velocity includes direction, which changes all the way round.")])

Q("w1b_small_cylinder_better", 3, "1e", "A student needs to measure about 6 cm³ of liquid. Explain why a 10 cm³ measuring cylinder is better than a 100 cm³ one.",
  [P("the 10 cm³ cylinder has smaller divisions (e.g. 0.1 or 0.2 cm³) so it is more precise", ["smaller divisions", "more precise", "0.1 cm3", "0.2 cm3", "finer scale", "reads more precisely"]),
   P("in the 100 cm³ cylinder 6 cm³ is a small fraction / near the bottom, so the percentage error is large", ["percentage error", "large error", "small fraction", "near the bottom", "hard to read", "1 cm3", "2 cm3"])],
  "The 10 cm³ cylinder has much smaller scale divisions, about 0.2 cm³, so it can measure 6 cm³ precisely. In a 100 cm³ cylinder the divisions are about 1–2 cm³ and 6 cm³ barely fills the bottom, so the reading would have a large percentage error.",
  ["Compare the size of the smallest divisions.", "What fraction of each cylinder does 6 cm³ fill?", "Which gives the smaller percentage error?"],
  "smaller divisions → more precise; big cylinder → large % error",
  ["The 10 cm³ cylinder has smaller divisions so it is more precise; in the big one 6 cm³ would have a large percentage error", "it reads to 0.2 cm³ instead of 2 cm³, which is more precise"],
  ["The larger cylinder is more accurate because it holds more", "They are the same"], min_points=1)

# ---------------------------------------------------------------- L4
Q("w1b_plan_density_stone", 4, "1e", "Describe the measurements and instruments needed to find the density of a small irregular stone.",
  [P("mass: measure with an electronic balance", ["balance", "electronic balance", "weigh", "mass"]),
   P("volume: displacement in a measuring cylinder (reading before and after, subtract)", ["displacement", "measuring cylinder", "rise in water", "before and after", "subtract", "overflow can"]),
   P("density = mass ÷ volume", ["mass ÷ volume", "mass / volume", "mass divided by volume", "density = m / v", "divide the mass by the volume"])],
  "Measure the stone's mass on an electronic balance. Find its volume by displacement: read the volume of water in a measuring cylinder, lower the stone in until fully covered, read the new volume and subtract. Then density = mass ÷ volume.",
  ["Density needs two quantities.", "How do you measure each of them for an irregular stone?", "How do you combine them?"],
  "balance for mass; displacement for volume; ρ = m ÷ V",
  ["Weigh it on an electronic balance, find the volume by displacement in a measuring cylinder, then density = mass ÷ volume", "mass from a balance and volume from the rise in water; divide mass by volume"],
  ["Measure its length with a ruler and multiply by its weight", "Put it in water and see if it floats"], min_points=2)

Q("w1b_plan_wire_diameter", 4, "1e", "Fig. 1 shows a micrometer screw gauge. Describe how to measure the diameter of a wire accurately with it.",
  [P("check for zero error first (close the jaws) and correct for it", ["zero error", "close the jaws", "check the zero", "correct for"]),
   P("tighten using the ratchet so the wire is gripped without squashing it", ["ratchet", "do not overtighten", "gently", "without squashing", "until it clicks"]),
   P("measure at several points along the wire (and in different directions) and take the average", ["several points", "different places", "different positions", "average", "mean", "repeat", "different directions"])],
  "First close the jaws and check for zero error, so it can be subtracted from the readings. Grip the wire using the ratchet so that it is held firmly but not squashed. Take readings at several places along the wire and in different directions, and calculate the average diameter.",
  ["What should you check before measuring?", "How do you avoid squashing a soft wire?", "Why measure at more than one place?"],
  "zero error; ratchet; several readings, average",
  ["Check the zero error, use the ratchet so I do not squash the wire, and measure at several points and average", "close the jaws to find the zero error, then take repeat readings at different places along the wire and find the mean"],
  ["Use a metre rule instead", "Squeeze it as hard as possible"], min_points=2,
  figure=lambda: figs.micrometer(0.53))

Q("w1b_evaluate_ruler_coin", 4, "1e", "A student measures the diameter of a coin (about 2.2 cm) with a 30 cm ruler. Evaluate this choice and suggest a better method.",
  [P("the ruler reads only to 1 mm, which is a large fraction (about 5%) of 2.2 cm", ["1 mm", "0.1 cm", "large fraction", "percentage error", "not precise", "too coarse", "about 5"]),
   P("it is also hard to find the widest point / line up the edges", ["widest point", "hard to line up", "edges", "parallax", "not the diameter"]),
   P("better: use vernier calipers (0.01 cm), measuring several times at different angles and averaging", ["vernier", "calipers", "0.01 cm", "0.1 mm", "repeat", "average", "different angles"])],
  "A ruler reads only to 1 mm, which is about 5 % of 2.2 cm, and it is hard to be sure you are measuring across the widest point. Vernier calipers would be better: their jaws grip the coin across a diameter and read to 0.01 cm. Measure in several directions and take the average.",
  ["What is the precision of a ruler compared with the size of the coin?", "What other difficulty is there with a ruler?", "Which instrument would you use instead, and how?"],
  "ruler 1 mm too coarse; vernier calipers 0.01 cm; repeat",
  ["The ruler only reads to 1 mm, which is a big percentage error; use vernier calipers and average several readings", "too coarse: use calipers that read to 0.01 cm and measure at different angles"],
  ["The ruler is fine because it is long", "Use a measuring cylinder"], min_points=2)

Q("w1b_reaction_time_effect", 4, "1e", "A student times two events by hand: a ball dropping (0.5 s) and a candle burning down (60 s). Reaction time is about 0.2 s. Explain why the error matters much more for the first event.",
  [P("the reaction-time error is about the same (≈ 0.2 s) for both", ["same error", "0.2 s for both", "about the same", "same reaction time", "same size"]),
   P("0.2 s is a large fraction (≈ 40 %) of 0.5 s but tiny (< 1 %) compared with 60 s", ["large fraction", "40", "percentage", "small fraction", "tiny compared", "less than 1", "compared with 60", "big compared"])],
  "Reaction time adds an error of roughly 0.2 s to both measurements. For the 0.5 s drop this is a very large fraction, about 40 %, but for the 60 s candle it is less than 1 %. So the percentage error is huge for the short event and negligible for the long one.",
  ["Is the reaction-time error bigger for one event than the other?", "Compare 0.2 s with 0.5 s and with 60 s.", "Think in terms of percentage error."],
  "same 0.2 s error; large % of 0.5 s, small % of 60 s",
  ["The error is about 0.2 s for both, but that is a large percentage of 0.5 s and a tiny percentage of 60 s", "0.2 s is 40 % of 0.5 s but less than 1 % of 60 s"],
  ["The ball moves faster so the stopwatch cannot keep up", "The candle is easier to see"], min_points=1)

Q("w1b_boat_current", 4, "1f", "A boat heads east at 3 m/s through water that is flowing west at 1 m/s. Explain how to find the boat's resultant velocity, and state it.",
  [P("velocities are vectors, so take direction into account (opposite directions subtract)", ["vector", "opposite directions", "subtract", "take away", "direction"]),
   P("resultant = 3 − 1 = 2 m/s east", ["2 m/s", "2 m/s east", "3 − 1", "3 - 1"]),
   P("direction is east (the larger velocity)", ["east", "towards the east", "same direction as the boat"])],
  "Velocities are vectors, so their directions matter. The boat's 3 m/s east and the water's 1 m/s west are opposite, so they subtract: the resultant velocity is 3 − 1 = 2 m/s towards the east.",
  ["Are the two velocities in the same or opposite directions?", "How do you combine opposite vectors?", "Give the size and direction."],
  "opposite vectors subtract; 2 m/s east",
  ["They are in opposite directions so subtract: 2 m/s east", "velocity is a vector; 3 − 1 = 2 m/s towards the east"],
  ["4 m/s east because you add them", "The boat stops"], min_points=2,
  pitfalls=[PF(["4 m/s", "add them to get 4"], "The velocities are opposite, so they subtract, not add.")])

Q("w1b_check_zero_micrometer", 4, "1e", "Describe how to check a micrometer screw gauge for zero error, and how a negative zero error is corrected.",
  [P("close the jaws gently using the ratchet with nothing between them and read the scale", ["close the jaws", "nothing between", "ratchet", "jaws together", "fully closed"]),
   P("if the reading is not zero, that reading is the zero error (negative if the thimble zero is above the datum line)", ["not zero", "the reading is the zero error", "below zero", "above the datum", "negative", "zero mark"]),
   P("corrected reading = reading − zero error, so a negative error is ADDED", ["reading − zero error", "subtract the zero error", "add", "added", "minus a negative"])],
  "Close the jaws gently with the ratchet, with nothing between them, and read the scale. If it does not read zero, that reading is the zero error; it is negative if the zero mark on the thimble has passed the datum line. Corrected reading = reading − zero error, so for a negative zero error the size of the error is added to each reading.",
  ["What should the micrometer read when the jaws are closed?", "What does it mean if it reads below zero?", "How do you correct a reading?"],
  "close jaws; read the error; corrected = reading − zero error (negative error is added)",
  ["Close the jaws with nothing between them; if it is not zero that is the zero error, and for a negative error you add it to each reading", "close it fully and read it; corrected reading = reading − zero error, so a negative one is added"],
  ["Open the jaws wide and read the scale", "Ignore it because it is small"], min_points=2)

Q("w1b_density_units_convert", 4, "1c", "Explain how to convert a density of 2.7 g/cm³ into kg/m³.",
  [P("1 g = 0.001 kg (÷ 1000)", ["0.001 kg", "1000 g", "divide by 1000", "g to kg"]),
   P("1 cm³ = 0.000001 m³ (1 m³ = 1 000 000 cm³)", ["1 000 000", "million", "0.000001", "cm3 to m3"]),
   P("so multiply by 1000: 2.7 g/cm³ = 2700 kg/m³", ["2700", "× 1000", "multiply by 1000", "times 1000"])],
  "1 g = 0.001 kg and 1 cm³ = 0.000001 m³. So 1 g/cm³ = 0.001 ÷ 0.000001 = 1000 kg/m³, and 2.7 g/cm³ = 2.7 × 1000 = 2700 kg/m³.",
  ["Convert the mass unit and the volume unit separately.", "1 m³ = 1 000 000 cm³ and 1 kg = 1000 g.", "Combine the two factors."],
  "g→kg ÷1000; cm³→m³ ÷10⁶; overall × 1000",
  ["1 g is 0.001 kg and 1 cm³ is 0.000001 m³, so multiply by 1000 to get 2700 kg/m³", "the factor is 1 000 000 ÷ 1000 = 1000, so 2700 kg/m³"],
  ["Divide by 1000 to get 0.0027 kg/m³", "It stays 2.7"], min_points=2,
  pitfalls=[PF(["0.0027"], "Density in kg/m³ is a LARGER number: multiply by 1000.")])

Q("w1b_wire_coil_method", 4, "1e", "Without a micrometer, a student finds the diameter of a thin wire by winding it closely around a pencil 25 times. Explain how this gives the diameter.",
  [P("wind 25 turns side by side with no gaps and measure the length of the coil with a ruler", ["side by side", "no gaps", "closely", "length of the coil", "measure the coil", "width of the coil"]),
   P("divide the coil length by 25 (the number of turns)", ["divide by 25", "÷ 25", "/ 25", "divided by the number of turns"]),
   P("this makes the measured length much larger than 1 mm, so the ruler's error is small", ["error is small", "more precise", "small compared", "1 mm is small", "percentage error", "shared"])],
  "Wind the wire 25 times round the pencil so the turns lie side by side with no gaps. Measure the length of the coil with a ruler and divide by 25 to get the diameter of the wire. The coil is much longer than 1 mm, so the ruler's 1 mm uncertainty becomes a small fraction of the measurement.",
  ["The coil's length is made of 25 wire diameters.", "How do you get one diameter?", "Why is this better than measuring one wire?"],
  "25 close turns; coil length ÷ 25; ruler error small",
  ["Wind 25 turns side by side, measure the length of the coil and divide by 25; the ruler error is then small", "measure the coil with the ruler and divide by the number of turns, which is more precise"],
  ["Measure one turn with the ruler", "Multiply the coil length by 25"], min_points=2)

Q("w1b_choose_balance_ring", 4, "1e", "A jeweller must find the mass of a gold ring of about 4 g. Explain why an electronic balance reading to 0.01 g is better than a spring balance reading to 0.5 N.",
  [P("the ring's weight is only about 0.04 N, far smaller than the spring balance's 0.5 N divisions", ["0.04 n", "too small", "smaller than 0.5", "would not register", "cannot read", "much smaller"]),
   P("the electronic balance reads to 0.01 g, a tiny fraction of 4 g, so it is precise", ["0.01 g", "more precise", "small fraction", "precise", "percentage error"])],
  "The ring weighs only about 0.04 N, much less than one 0.5 N division on the spring balance, so the spring balance could not measure it meaningfully. The electronic balance reads to 0.01 g, a tiny fraction of 4 g, so it measures the mass precisely.",
  ["Work out the weight of a 4 g ring (g = 10 N/kg).", "Compare it with the spring balance's divisions.", "What is the precision of the electronic balance by comparison?"],
  "ring weighs 0.04 N < 0.5 N divisions; balance reads 0.01 g",
  ["The ring weighs only 0.04 N, which is too small for 0.5 N divisions; the electronic balance reads to 0.01 g so it is more precise", "the spring balance cannot read such a small weight, while the electronic balance is precise to 0.01 g"],
  ["The spring balance is better because gold is heavy", "Both are equally good"], min_points=2)

Q("w1b_period_length_trend", 4, "1e", "The table shows the period of a pendulum for different lengths. Describe the trend and explain why several lengths and repeat timings are used.\n\n| length / m | period / s |\n|---|---|\n| 0.20 | 0.90 |\n| 0.40 | 1.27 |\n| 0.60 | 1.55 |\n| 0.80 | 1.79 |",
  [P("the period increases as the length increases", ["period increases", "longer period", "increases as the length", "longer pendulum", "longer length gives"]),
   P("but not in proportion (doubling length does not double the period)", ["not proportional", "not in proportion", "does not double", "less than double", "not directly proportional"]),
   P("several lengths show the pattern; repeats and averages reduce timing errors", ["show the pattern", "see the trend", "repeat", "average", "reduce errors", "reliable"])],
  "The period increases as the length increases, but not in proportion: doubling the length from 0.40 m to 0.80 m increases the period only from 1.27 s to 1.79 s. Using several lengths shows the pattern clearly, and repeating each timing and averaging reduces the effect of timing errors.",
  ["What happens to the period as the length grows?", "Does doubling the length double the period?", "Why is one length, timed once, not enough?"],
  "period increases with length, not proportionally; many lengths and repeats",
  ["The period increases as the length increases but does not double when the length doubles; repeats and averages reduce errors", "longer pendulum, longer period, but not proportional; several lengths show the trend"],
  ["The period stays the same", "The period decreases with length"], min_points=2,
  pitfalls=[PF(["period decreases", "shorter period for longer"], "The table shows the period INCREASES with length.")])

# ---------------------------------------------------------------- L5
Q("w1b_evaluate_big_cylinder", 5, "1e", "A student finds the volume of a small bead (about 0.5 cm³) by putting it in a 250 cm³ measuring cylinder of water. Evaluate the method and suggest improvements.",
  [P("the rise (0.5 cm³) is far smaller than the cylinder's divisions (about 2–10 cm³), so it cannot be read", ["cannot be read", "too small", "smaller than the divisions", "divisions", "2 cm3", "10 cm3", "not precise", "large percentage error"]),
   P("use a smaller (e.g. 10 cm³) cylinder with finer divisions", ["smaller cylinder", "10 cm3", "finer divisions", "smaller measuring cylinder"]),
   P("put many identical beads in together and divide by the number", ["many beads", "50 beads", "several beads", "lots of beads", "divide by the number", "divide by 50"])],
  "The bead raises the water by only about 0.5 cm³, far less than one division on a 250 cm³ cylinder, so the change cannot be read and the error would be huge. Use a narrow 10 cm³ cylinder with finer divisions, and add many identical beads at once, then divide the total rise by the number of beads.",
  ["How big is 0.5 cm³ compared with the divisions on a 250 cm³ cylinder?", "How could you make the change in level easier to read?", "Suggest at least two improvements."],
  "change far smaller than divisions; smaller cylinder; many beads ÷ number",
  ["The rise is smaller than one division so it cannot be read; use a 10 cm³ cylinder and add 50 beads then divide by 50", "too small a change for that cylinder: put many beads in and divide by the number, or use a smaller cylinder"],
  ["The method is good because the cylinder is large", "Weigh the bead instead of measuring its volume"], min_points=2)

Q("w1b_too_many_digits", 5, "1e", "A student times 20 oscillations as 31.4 s on a stopwatch and records the period as 1.570000 s from a calculator. Evaluate this.",
  [P("the extra digits are not justified / the period should be given to a sensible number of figures (e.g. 1.57 s)", ["not justified", "too many", "1.57 s", "3 significant figures", "sensible", "round", "should be 1.57"]),
   P("the precision is limited by the stopwatch reading and the reaction time (about 0.2 s), not by the calculator", ["reaction time", "0.2 s", "limited by", "stopwatch", "instrument", "measurement"]),
   P("the extra zeros falsely suggest a precision of a millionth of a second", ["falsely", "suggests", "millionth", "misleading", "pretends", "more precise than"])],
  "The extra digits are not justified. The precision of the result is limited by the measurement, a stopwatch time of 31.4 s with a reaction-time error of about 0.2 s, not by the calculator. Writing 1.570000 s falsely suggests the period is known to a millionth of a second; it should be given as about 1.57 s.",
  ["How precisely was the time actually measured?", "Does a calculator make a measurement more precise?", "What should be recorded?"],
  "too many figures; precision set by measurement and reaction time; give 1.57 s",
  ["Too many digits: the precision is limited by the stopwatch and reaction time, so it should be 1.57 s", "the zeros are misleading and suggest it is more precise than the measurement; round to 1.57 s"],
  ["More digits always make an answer more accurate", "It should be 2 s"], min_points=2,
  pitfalls=[PF(["more digits always", "more decimal places make it more accurate"], "Extra digits from a calculator do not add precision; the measurement limits it.")])

Q("w1b_page_thickness_design", 5, "1e", "Design a method to find the thickness of one page of a textbook using a micrometer or vernier calipers, and explain how to make it reliable.",
  [P("measure a stack of many pages (not the covers), e.g. 100 pages = 50 sheets, squeezed together", ["stack", "many pages", "100 pages", "50 sheets", "not the covers", "exclude the covers", "squeeze"]),
   P("divide by the number of sheets (remembering 2 pages per sheet)", ["divide by", "number of sheets", "two pages per sheet", "2 pages per sheet", "÷ 50"]),
   P("repeat at different places / with different stacks and average; check zero error", ["repeat", "average", "different places", "zero error", "several times"])],
  "Open the book and measure the thickness of a block of, say, 100 pages (50 sheets), excluding the covers and pressing them together firmly. Divide by the number of sheets (two pages make one sheet). Check the instrument for zero error, repeat at different parts of the block and average the results.",
  ["One page is too thin to measure directly.", "Remember that each sheet has two numbered pages.", "How do you make the result reliable?"],
  "measure many sheets (no covers), divide; zero error, repeats, average",
  ["Measure 50 sheets without the covers using vernier calipers, divide by 50, check the zero error and average several readings", "measure a stack of 100 pages, divide by the number of sheets, and repeat to average"],
  ["Measure the whole book including the covers and divide by 2", "Measure one page with a metre rule"], min_points=2)

Q("w1b_forgot_zero_error", 5, "1e", "A student uses vernier calipers with a zero error of −0.02 cm but forgets to correct for it. Evaluate the effect on her results and say how to fix them.",
  [P("every reading is 0.02 cm too small (systematic error)", ["too small", "0.02 cm too small", "every reading", "all readings", "systematic", "too low"]),
   P("averaging does not remove it", ["averaging does not", "average still", "repeats do not", "cannot be removed by averaging"]),
   P("correct by subtracting the zero error, i.e. adding 0.02 cm to each reading", ["add 0.02", "adding 0.02", "minus a negative", "subtract −0.02", "reading − zero error", "+ 0.02"])],
  "A negative zero error means every reading is 0.02 cm too small, so all her results are too low by the same amount. Repeating and averaging will not remove this. She should correct each reading using corrected = reading − (−0.02) cm, which means adding 0.02 cm.",
  ["What does a negative zero error do to each reading?", "Does averaging help with an error that is the same every time?", "How is the correction applied?"],
  "all readings 0.02 cm too small; not removed by averaging; add 0.02 cm",
  ["Every reading is 0.02 cm too small and averaging does not fix it; she should add 0.02 cm to each", "it is a systematic error making all readings too low, so correct by adding 0.02 cm"],
  ["It makes her readings too large, so she should subtract 0.02 cm", "It has no effect because it is small"], min_points=2,
  pitfalls=[PF(["readings too large", "too big", "subtract 0.02"], "A NEGATIVE zero error makes readings too SMALL; correct by adding 0.02 cm.")])

Q("w1b_light_gate_vs_hand", 5, "1e", "Two students time 20 oscillations of the same pendulum: one by hand with a stopwatch, the other with a light gate connected to a timer. Evaluate which method is better.",
  [P("hand timing includes reaction time (about 0.2 s) at start and stop, which varies", ["reaction time", "0.2 s", "human error", "varies", "start and stop"]),
   P("a light gate starts and stops automatically with no reaction time, so it is more accurate and precise", ["automatic", "no reaction time", "more accurate", "more precise", "electronic", "light gate is better"]),
   P("timing 20 oscillations already reduces the hand-timing error, so both can give good results", ["20 oscillations reduces", "error is shared", "spread over", "small fraction", "both are reasonable", "divided by 20"])],
  "Hand timing includes the person's reaction time, about 0.2 s, when starting and stopping, and this varies from trial to trial. A light gate triggers automatically with no reaction time, so it is more accurate and more precise. Timing 20 oscillations does reduce the effect of the hand-timing error, but the light gate is still the better method.",
  ["What extra error does hand timing introduce?", "How does a light gate avoid it?", "Does timing 20 oscillations help the hand-timer?"],
  "reaction time in hand timing; light gate automatic; 20 oscillations reduces error",
  ["Hand timing has a reaction time of about 0.2 s, but the light gate is automatic so it is more accurate; timing 20 oscillations reduces the hand error", "hand timing has a reaction time error, but the light gate is automatic so there is no reaction time and it is better"],
  ["Hand timing is better because people are more careful than machines", "They are always identical"], min_points=2)

Q("w1b_atoms_across_mm", 5, "1d", "An atom is about 10⁻¹⁰ m across. Estimate how many atoms would fit side by side across 1 mm, and explain how you got your answer.",
  [P("1 mm = 10^-3 m (0.001 m)", ["0.001 m", "10^-3", "1 mm = 0.001", "1 mm is 0.001", "thousandth of a metre"]),
   P("number = 10^-3 ÷ 10^-10 = 10^7 (about ten million)", ["10^7", "ten million", "10 000 000", "10 million", "divide"])],
  "1 mm = 10⁻³ m. The number of atoms across it is 10⁻³ ÷ 10⁻¹⁰ = 10⁷, so about ten million atoms would fit side by side across 1 mm.",
  ["Write 1 mm in metres.", "How many atom-widths fit in that length?", "Divide the length by the size of one atom."],
  "1 mm = 10⁻³ m; 10⁻³ ÷ 10⁻¹⁰ = 10⁷",
  ["1 mm is 0.001 m, and 0.001 divided by 10⁻¹⁰ is 10⁷, about ten million atoms", "divide 10⁻³ m by 10⁻¹⁰ m to get 10 million"],
  ["About 1000 atoms", "About 10 atoms"], min_points=2)

Q("w1b_resultant_range_claim", 5, "1f", "A student says: 'A 3 N force and a 4 N force acting on an object always give a resultant of 5 N.' Evaluate this claim.",
  [P("wrong: the resultant depends on the directions of the forces (they are vectors)", ["wrong", "depends on the direction", "depends on the angle", "vectors", "not always"]),
   P("same direction gives 7 N; opposite directions give 1 N", ["7 n", "1 n", "same direction", "opposite"]),
   P("5 N only when the forces are at right angles (Pythagoras)", ["right angles", "90", "perpendicular", "pythagoras", "only at right angles"])],
  "The claim is wrong, because forces are vectors and the resultant depends on their directions. In the same direction the resultant is 7 N; in opposite directions it is 1 N. Only when the forces are at right angles is the resultant 5 N, by Pythagoras' theorem.",
  ["Do the directions of the forces matter?", "Work out the resultant when they are parallel and when they are opposite.", "When is it exactly 5 N?"],
  "depends on direction: 7 N, 1 N, 5 N only at 90°",
  ["Wrong: it depends on direction; it is 7 N if they act the same way, 1 N if opposite, and 5 N only at right angles", "not always 5 N because force is a vector; 5 N only when perpendicular"],
  ["Correct, 3 + 4 = 5", "Correct, forces always make 5 N"], min_points=2,
  pitfalls=[PF(["3 + 4 = 5", "always 5 n"], "3 + 4 = 7, and the resultant depends on the angle between the forces.")])

Q("w1b_cork_volume_design", 5, "1e", "A cork floats in water. Design a method to find its volume using a measuring cylinder and a small metal sinker.",
  [P("measure the water level with only the sinker submerged", ["sinker alone", "only the sinker", "sinker first", "just the sinker", "with the sinker"]),
   P("attach the cork to the sinker so both are fully under water, and read the new level", ["tie the cork", "attach the cork", "cork and sinker", "both submerged", "fully under", "both under water"]),
   P("volume of cork = difference between the two readings", ["difference", "subtract", "minus", "take away"])],
  "Put the sinker alone into the water in the measuring cylinder and record the level. Then tie the cork to the sinker and lower them so both are completely under water, and record the new level. The volume of the cork is the difference between the two readings.",
  ["Why can't you just drop the cork in?", "The sinker holds it under; but the sinker also displaces water.", "How do you remove the sinker's volume from the result?"],
  "level with sinker only; level with cork + sinker submerged; subtract",
  ["Read the level with just the sinker in, then tie the cork to the sinker so both are submerged, read again and subtract", "use the sinker to hold the cork fully under water and take the difference between the two readings"],
  ["Drop the cork in and read the level", "Push the cork down with your finger and read the level"], min_points=2)

Q("w1b_coin_density_plan", 5, "1e", "Plan an accurate way to find the density of the metal in a type of coin, using an electronic balance and a measuring cylinder.",
  [P("use many identical coins (e.g. 20) to make the mass and volume large enough to measure precisely", ["many coins", "20 coins", "lots of coins", "several coins", "large enough", "more precise"]),
   P("measure the total mass on the balance", ["total mass", "weigh them", "balance", "mass of the coins"]),
   P("find the total volume by displacement (rise in water level) and divide mass by volume", ["displacement", "rise in water", "measuring cylinder", "mass ÷ volume", "mass divided by volume", "divide"])],
  "One coin displaces too little water to measure, so use many identical coins, for example 20. Weigh them together on the electronic balance. Find their total volume by displacement: read the water level in a measuring cylinder, add the coins and read again, and subtract. Density = total mass ÷ total volume.",
  ["Can the volume of one coin be read on a measuring cylinder?", "How can you make both measurements larger?", "How do you combine the readings?"],
  "many coins; total mass; total volume by displacement; ρ = m ÷ V",
  ["Use 20 coins, weigh them, find their volume by displacement and divide mass by volume", "many coins make the volume large enough to measure; density = mass ÷ volume"],
  ["Weigh one coin and measure it with a ruler", "Put one coin in a 250 cm³ cylinder"], min_points=2)

Q("w1b_drop_timing", 5, "1e", "A student times a ball dropping 1 m (about 0.45 s) with a hand-held stopwatch. Evaluate the method and suggest how to improve it.",
  [P("reaction time (about 0.2 s) is a very large fraction of 0.45 s, so the result is unreliable", ["reaction time", "0.2 s", "large fraction", "large percentage", "unreliable", "big error"]),
   P("improve: use light gates / a timer or video analysis instead of hand timing", ["light gate", "electronic timer", "video", "slow motion", "automatic", "sensor"]),
   P("or increase the drop height so the time is longer, and repeat and average", ["greater height", "higher drop", "longer time", "repeat", "average"])],
  "Reaction time, about 0.2 s, is nearly half of the 0.45 s being measured, so the result is very unreliable. The time should be measured automatically, for example with light gates and an electronic timer or by video analysis. Dropping from a greater height makes the time longer, and repeating and averaging reduces random errors.",
  ["Compare the reaction time with the time being measured.", "How can the timing be made automatic?", "What other changes would help?"],
  "reaction time large % of 0.45 s; use light gates/video; longer drop, repeat",
  ["The reaction time of 0.2 s is a large fraction of 0.45 s, so use light gates or video and repeat and average", "hand timing is unreliable here; use an electronic timer or drop it from higher"],
  ["The method is accurate because stopwatches read to 0.01 s", "Use a wall clock instead"], min_points=2,
  pitfalls=[PF(["accurate because stopwatches read", "stopwatch reads to 0.01 s so it is accurate"], "The stopwatch's 0.01 s resolution is irrelevant when reaction time is about 0.2 s.")])
