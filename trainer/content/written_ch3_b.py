"""Chapter 3 Force and Pressure: 50 more written-answer questions (10 per level), marked by keywords/phrases."""
from .. import figs, sketches
from ..marker import Pitfall, Point
from .base import written

P = Point
PF = Pitfall
CH = 3


def Q(id, lv, lo, stem, points, model, hints, keywords, passes, fails, pitfalls=(), min_points=None, figure=None):
    written(id, CH, lv, lo, stem=stem, points=points, model_answer=model, hints=hints, keywords=keywords,
            pitfalls=pitfalls, min_points=min_points, figure=figure, sample_pass=passes, sample_fail=fails)


MASS_IS_WEIGHT = PF(["weight is measured in kg", "weight is in kg", "weight in kilograms", "mass is measured in newtons", "mass is in newtons"],
                    "Mass is measured in kilograms; weight is a force measured in newtons.")

# ---------------------------------------------------------------- L1
Q("w3b_unit_pressure", 1, "3h", "State the SI unit of pressure and what it is equal to in terms of other units.",
  [P("the pascal (Pa)", ["pascal", "pa"]),
   P("1 Pa = 1 N/m² (one newton per square metre)", ["n/m2", "newton per square metre", "newtons per square metre", "1 n/m2"])],
  "The SI unit of pressure is the pascal (Pa). One pascal is a force of one newton acting on an area of one square metre: 1 Pa = 1 N/m².",
  ["Pressure = force ÷ area.", "What is the unit of force divided by the unit of area?", "It also has its own name."],
  "pascal; 1 Pa = 1 N/m²",
  ["The pascal, which is 1 N/m²", "pressure is in Pa, equal to newtons per square metre"],
  ["The newton", "N m"], min_points=2)

Q("w3b_density_units", 1, "3g", "State two units in which density can be measured.",
  [P("kg/m³ (SI unit)", ["kg/m3", "kilograms per cubic metre", "kg per m3"]),
   P("g/cm³", ["g/cm3", "grams per cubic centimetre", "g per cm3"])],
  "Density can be measured in kilograms per cubic metre (kg/m³), the SI unit, or in grams per cubic centimetre (g/cm³).",
  ["Density = mass ÷ volume.", "Combine a unit of mass with a unit of volume.", "Give two different combinations."],
  "kg/m³ and g/cm³",
  ["kg/m³ and g/cm³", "kilograms per cubic metre and grams per cubic centimetre"],
  ["N and Pa", "kg and m³"])

Q("w3b_weight_def", 1, "3e", "State what is meant by the weight of a body.",
  [P("the gravitational force acting on the body (pull of gravity on its mass)", ["gravitational force", "force of gravity", "pull of gravity", "force due to gravity", "gravity pulling", "gravitational pull"])],
  "The weight of a body is the gravitational force acting on it, the pull of gravity on its mass.",
  ["Is weight a mass or a force?", "Which force acts on every object near the Earth?", "Put that into a definition."],
  "gravitational force on a body",
  ["Weight is the gravitational force acting on a body", "the pull of gravity on an object"],
  ["Weight is the amount of matter in a body", "Weight is how big an object is"],
  pitfalls=[PF(["amount of matter", "quantity of matter"], "The amount of matter in a body is its MASS; weight is a force.")])

Q("w3b_three_contact", 1, "3a", "Name three contact forces.",
  [P("friction", ["friction"]), P("normal (reaction) force", ["normal force", "normal reaction", "reaction force", "normal"]),
   P("tension / air resistance / upthrust", ["tension", "air resistance", "drag", "upthrust", "water resistance"])],
  "Friction, the normal force and tension are contact forces (air resistance is another). They act only when objects touch.",
  ["Contact forces need the objects to touch.", "Think of a box on a floor, being pulled by a rope.", "Name three."],
  "friction, normal force, tension, air resistance",
  ["friction, normal force and tension", "air resistance, friction and the normal reaction force"],
  ["gravity, magnetism and electrostatic force", "weight, mass and speed"], min_points=3)

Q("w3b_three_noncontact", 1, "3a", "Name three non-contact forces.",
  [P("gravitational force (weight)", ["gravitational", "gravity", "weight"]), P("magnetic force", ["magnetic", "magnetism"]),
   P("electrostatic (electric) force", ["electrostatic", "electric force", "electrical force", "static"])],
  "Gravitational, magnetic and electrostatic forces are non-contact forces: they act between objects that are not touching.",
  ["Non-contact forces act at a distance.", "Think of what pulls a dropped ball, what pulls a paper clip to a magnet, and what makes a rubbed balloon stick.", "Name three."],
  "gravitational, magnetic, electrostatic",
  ["gravitational, magnetic and electrostatic forces", "weight, magnetism and electric force"],
  ["friction, tension and normal force", "air resistance and push"], min_points=3)

Q("w3b_units_w_g", 1, "3e", "State the unit of weight and the unit of gravitational field strength.",
  [P("weight: newton (N)", ["newton", "n"]), P("g: newton per kilogram (N/kg)", ["n/kg", "newton per kilogram", "newtons per kilogram"])],
  "Weight is a force, so it is measured in newtons (N). Gravitational field strength is measured in newtons per kilogram (N/kg).",
  ["Weight is a force.", "g is force per unit mass.", "Give both units."],
  "weight N; g N/kg",
  ["Weight is in newtons and g is in N/kg", "N for weight and newtons per kilogram for g"],
  ["Weight is in kg and g is in m", "Both are in kg"], pitfalls=[MASS_IS_WEIGHT])

Q("w3b_weight_formula", 1, "3e", "State the relationship between weight, mass and gravitational field strength, saying what each symbol means.",
  [P("W = m g (weight = mass × gravitational field strength)", ["w = m g", "w = mg", "weight = mass × g", "weight = mass times", "mass × gravitational field strength", "mass multiplied by"]),
   P("W in N, m in kg, g in N/kg", ["newton", "kg", "n/kg", "kilogram"])],
  "Weight = mass × gravitational field strength, W = m g, where W is the weight in newtons, m is the mass in kilograms and g is the gravitational field strength in N/kg.",
  ["Weight depends on mass and on the field.", "Which operation links them?", "State the units of each."],
  "W = m g; N, kg, N/kg",
  ["W = mg, where W is weight in N, m is mass in kg and g is field strength in N/kg", "weight = mass × gravitational field strength, in newtons, kilograms and N/kg"],
  ["W = m ÷ g", "weight = mass + gravity"], min_points=1,
  pitfalls=[PF(["w = m / g", "w = m ÷ g", "mass divided by g"], "Weight = mass × g, not mass ÷ g.")])

Q("w3b_density_formula", 1, "3g", "Write down the formula for density, stating what each symbol means and its unit.",
  [P("ρ = m / V (density = mass ÷ volume)", ["mass ÷ volume", "mass / volume", "mass divided by volume", "m / v", "m ÷ v"]),
   P("mass in kg (or g), volume in m³ (or cm³), density in kg/m³ (or g/cm³)", ["kg/m3", "g/cm3", "kg", "m3", "cm3"])],
  "Density = mass ÷ volume, ρ = m / V, where m is the mass in kg, V is the volume in m³ and ρ is the density in kg/m³ (or g, cm³ and g/cm³).",
  ["Density relates mass and volume.", "Which is divided by which?", "Give the units."],
  "ρ = m ÷ V; kg/m³",
  ["density = mass ÷ volume, in kg/m³", "ρ = m/V with mass in kg and volume in m³"],
  ["density = volume ÷ mass", "density = mass × volume"], min_points=1,
  pitfalls=[PF(["volume ÷ mass", "volume / mass", "volume divided by mass", "mass × volume", "mass times volume"], "Density = mass ÷ volume.")])

Q("w3b_pressure_formula", 1, "3h", "Write down the formula for pressure, stating what each symbol means and its unit.",
  [P("p = F / A (pressure = force ÷ area)", ["force ÷ area", "force / area", "force divided by area", "f / a", "f ÷ a"]),
   P("F in N, A in m², p in Pa", ["pa", "pascal", "n/m2", "m2", "newton"])],
  "Pressure = force ÷ area, p = F / A, where F is the force acting at right angles to the surface in newtons, A is the area in m², and p is the pressure in pascals (N/m²).",
  ["Pressure relates force and area.", "Which is divided by which?", "Give the units."],
  "p = F ÷ A; N, m², Pa",
  ["pressure = force ÷ area, measured in pascals", "p = F/A with force in N and area in m²"],
  ["pressure = force × area", "pressure = area ÷ force"], min_points=1,
  pitfalls=[PF(["force × area", "force times area", "area ÷ force", "area / force"], "Pressure = force ÷ area.")])

Q("w3b_g_value_meaning", 1, "3d", "State the value of the gravitational field strength at the Earth's surface and explain what it means.",
  [P("about 10 N/kg", ["10 n/kg", "9.8 n/kg", "10 newtons per kilogram"]),
   P("each kilogram of mass experiences a gravitational force of about 10 N", ["each kilogram", "every kilogram", "1 kg", "per kilogram", "force of 10 n on"])],
  "The gravitational field strength at the Earth's surface is about 10 N/kg. This means that each kilogram of mass experiences a gravitational force of about 10 N.",
  ["g has the unit N/kg.", "What does 'per kilogram' mean?", "Give the value and its meaning."],
  "≈ 10 N/kg; 10 N on each kg",
  ["About 10 N/kg, meaning each kilogram experiences a force of 10 N", "g is 10 N/kg, so a 1 kg mass has a weight of 10 N"],
  ["10 kg", "1 N/kg, meaning objects fall slowly"], min_points=2)

# ---------------------------------------------------------------- L2
Q("w3b_friction_contact", 2, "3a", "Explain why friction is described as a contact force.",
  [P("it acts only where two surfaces are touching", ["touching", "in contact", "surfaces touch", "two surfaces", "rub against"]),
   P("it opposes the sliding (relative motion) of the surfaces", ["opposes", "against the motion", "resists sliding", "opposite to the motion", "slows"])],
  "Friction acts only where two surfaces are in contact, and it opposes the sliding (or attempted sliding) of one surface over the other. Without contact there is no friction, so it is a contact force.",
  ["Where does friction act?", "Can friction act between objects that are not touching?", "What does friction do?"],
  "acts where surfaces touch; opposes sliding",
  ["It only acts when two surfaces are touching and it opposes their motion", "friction needs surfaces in contact, rubbing against each other"],
  ["It acts from a distance like gravity", "It is caused by magnets"], min_points=1)

Q("w3b_magnet_noncontact", 2, "3a", "A magnet pulls a steel paper clip towards it from a few centimetres away. Explain why the magnetic force is a non-contact force.",
  [P("it acts between objects that are not touching (across a gap / at a distance)", ["not touching", "at a distance", "across a gap", "without touching", "without contact", "from a distance"]),
   P("the clip is in the magnet's magnetic field", ["magnetic field", "field"])],
  "The magnet pulls the clip even though they are not touching: the force acts across the gap, at a distance, because the clip is in the magnet's magnetic field. So it is a non-contact force.",
  ["Are the magnet and the clip touching?", "How can the force act across the gap?", "Explain."],
  "acts at a distance; in the magnetic field",
  ["It acts at a distance without the magnet touching the clip", "the clip is in the magnetic field so it is pulled without contact"],
  ["Because the magnet touches the clip", "Because it is a type of friction"], min_points=1)

Q("w3b_normal_force", 2, "3a", "Fig. 1 shows a book resting on a table. Describe the normal force on the book.",
  [P("it is the push of the table surface on the book", ["push of the table", "table pushes", "force from the table", "surface pushes", "table on the book"]),
   P("it acts at right angles (perpendicular) to the surface, upwards here", ["right angles", "perpendicular", "upwards", "at 90"]),
   P("it is equal and opposite to the weight when the book is at rest", ["equal to the weight", "balances the weight", "equal and opposite", "same size as the weight"])],
  "The normal force is the push of the table's surface on the book. It acts at right angles to the surface, here upwards, and since the book is at rest it is equal in size to the book's weight.",
  ["Which surface is pushing on the book?", "In which direction does a normal force act?", "How big is it when the book is at rest?"],
  "table's push; perpendicular to surface; balances weight",
  ["It is the upward push of the table on the book, at right angles to the surface, equal to the weight", "the table pushes up perpendicular to the surface and balances the weight"],
  ["It is the weight of the table", "It is friction pulling the book sideways"], min_points=2,
  figure=lambda: figs.force_diagram([("N", "up", 1.4), ("W", "down", 1.4)], label_body="book"))

Q("w3b_tension_sledge", 2, "3a", "A child pulls a sledge across snow with a rope. Name the force in the rope and describe it.",
  [P("tension", ["tension"]),
   P("it is a pulling force acting along the rope, pulling the sledge towards the child", ["pull", "pulling force", "along the rope", "towards the child"])],
  "The force in the rope is tension. It is a pulling force that acts along the length of the rope, pulling the sledge towards the child.",
  ["What is the name for the force in a stretched rope?", "Which way does it act?", "Name and describe it."],
  "tension: pull along the rope",
  ["Tension, a pulling force along the rope", "the rope has tension which pulls the sledge along the rope towards the child"],
  ["Friction pushing the sledge", "Weight of the rope"], min_points=2)

Q("w3b_astronaut_mass_space", 2, "3f", "An astronaut has a mass of 70 kg on Earth. Explain what happens to her mass and her weight when she is far out in space, away from planets.",
  [P("her mass stays 70 kg (amount of matter does not change)", ["mass stays", "mass is still 70", "mass is the same", "mass does not change", "same mass", "mass remains"]),
   P("her weight becomes (almost) zero because the gravitational field is very weak", ["weight becomes zero", "almost zero", "weight is zero", "very small weight", "no weight", "weight decreases", "weaker gravity", "weak field"])],
  "Her mass is still 70 kg, because the amount of matter in her body has not changed. Her weight, the gravitational force on her, becomes almost zero, because far from any planet the gravitational field is extremely weak.",
  ["Does the amount of matter in her change?", "What does weight depend on besides mass?", "Comment on each."],
  "mass unchanged; weight ≈ 0 (weak field)",
  ["Her mass stays 70 kg but her weight becomes almost zero because gravity is so weak", "the mass does not change; the weight decreases to nearly nothing"],
  ["Her mass becomes zero", "Both stay the same"], min_points=2,
  pitfalls=[PF(["mass becomes zero", "mass is zero", "mass decreases", "loses mass"], "Mass is the amount of matter; it does not change in space.")])

Q("w3b_oil_floats", 2, "3g", "Oil floats on top of water. Explain what this tells you about their densities.",
  [P("oil is less dense than water", ["oil is less dense", "lower density", "less dense than water", "water is denser", "water is more dense"]),
   P("a less dense liquid floats on a denser one", ["less dense floats", "floats on the denser", "denser sinks", "denser liquid sinks", "less dense liquids float", "lower density floats", "floats on a liquid with a higher density"])],
  "Oil is less dense than water. A liquid with a lower density floats on a liquid with a higher density, so the oil stays on top.",
  ["Which liquid ends up on top?", "What decides which floats?", "Compare the densities."],
  "oil less dense than water",
  ["Oil is less dense than water, so it floats on it", "water is denser, and less dense liquids float on denser ones"],
  ["Oil is denser than water", "Oil is heavier than water"],
  pitfalls=[PF(["oil is denser", "oil is more dense", "oil is heavier"], "The liquid on top is the LESS dense one.")])

Q("w3b_same_steel_density", 2, "3g", "A small steel nail and a large steel girder are made of the same steel. Explain how their densities compare.",
  [P("they have the same density", ["same density", "equal density", "density is the same", "same"]),
   P("density depends on the material, not the size (mass and volume increase together)", ["depends on the material", "not on the size", "property of the material", "mass and volume", "both increase", "ratio"])],
  "They have the same density. Density is a property of the material: the girder has much more mass but also much more volume, so mass ÷ volume is the same as for the nail.",
  ["Is density about the material or the size?", "What happens to mass and volume when the object is bigger?", "Compare."],
  "same density; property of material",
  ["They have the same density because density depends on the material, not the size", "the girder has more mass but more volume too, so the density is the same"],
  ["The girder is denser because it is heavier", "The nail is denser because it is small"],
  pitfalls=[PF(["girder is denser", "heavier so denser", "nail is denser"], "Density depends on the material, not on the size of the object.")])

Q("w3b_pressure_area_general", 2, "3h", "Explain how the pressure under an object changes when the same force acts on a smaller area. Give an everyday example.",
  [P("smaller area gives a larger pressure (p = F ÷ A)", ["larger pressure", "greater pressure", "pressure increases", "more pressure", "higher pressure"]),
   P("example: knife, needle, nail, high heels, drawing pin", ["knife", "needle", "nail", "heels", "drawing pin", "pin", "axe", "skate"])],
  "For the same force, a smaller area gives a larger pressure, since p = F ÷ A. For example, a nail's sharp point has a tiny area, so a hammer blow produces a very large pressure that drives it into wood.",
  ["Use p = F ÷ A.", "What happens to p if A decreases and F stays the same?", "Think of something sharp."],
  "smaller area → larger pressure; example",
  ["A smaller area gives a larger pressure, like the sharp point of a nail", "pressure increases, for example a knife edge cuts easily"],
  ["A smaller area gives a smaller pressure", "Pressure does not depend on area"],
  pitfalls=[PF(["smaller pressure", "less pressure", "pressure decreases"], "Same force on a smaller area gives a LARGER pressure.")])

Q("w3b_balance_types", 2, "3f", "Explain which quantity a beam balance measures and which a spring balance measures.",
  [P("a beam balance compares masses, so it measures mass", ["beam balance measures mass", "beam balance compares masses", "beam balance gives mass", "beam balance: mass"]),
   P("a spring balance measures the force stretching the spring, i.e. weight", ["spring balance measures weight", "spring balance measures force", "spring balance gives weight", "stretching force", "spring balance: weight"])],
  "A beam balance compares the unknown mass with standard masses, so it measures mass. A spring balance measures the force stretching its spring, which is the object's weight.",
  ["A beam balance has two pans.", "A spring balance has a spring that stretches.", "Which quantity does each respond to?"],
  "beam: mass; spring: weight",
  ["A beam balance measures mass because it compares masses, and a spring balance measures weight", "the beam balance gives mass; the spring balance measures the force stretching it, the weight"],
  ["Both measure mass", "Both measure density"], min_points=2)

Q("w3b_weight_different_planets", 2, "3e", "Explain why the same rock has different weights on different planets, even though its mass is the same.",
  [P("weight = mass × g", ["w = mg", "w = m g", "mass × g", "weight = mass"]),
   P("g (the gravitational field strength) is different on each planet", ["g is different", "different g", "gravitational field strength is different", "field strength varies", "different field strength", "gravity is different"])],
  "Weight = mass × gravitational field strength. The mass is the same everywhere, but the gravitational field strength g is different on each planet, so the weight is different.",
  ["Write down the formula for weight.", "Which factor stays the same, and which changes from planet to planet?", "Explain."],
  "W = m g; g differs between planets",
  ["W = mg and g is different on each planet, so the weight changes even though the mass is the same", "the gravitational field strength is different, so weight = mass × g changes"],
  ["Because the rock loses mass in space", "Because the rock gets bigger"], min_points=2)

# ---------------------------------------------------------------- L3
Q("w3b_bed_of_nails", 3, "3i", "A performer lies on a bed of 1000 nails without being hurt, but would be injured lying on a single nail. Explain why.",
  [P("the weight is shared over many nails, so the total contact area is large", ["shared", "spread", "many nails", "large area", "total area", "bigger area"]),
   P("so the pressure from each nail is small (p = F ÷ A)", ["small pressure", "pressure is small", "low pressure", "less pressure", "pressure is low"]),
   P("on one nail all the weight acts on a tiny area, giving a huge pressure", ["one nail", "single nail", "tiny area", "huge pressure", "very large pressure", "high pressure"])],
  "On the bed of nails the performer's weight is shared among 1000 nails, so the total area in contact is large and the pressure from each nail is small. On a single nail the whole weight would act on one tiny point, giving a huge pressure that would pierce the skin.",
  ["Is the force the same in both cases?", "How does the contact area compare?", "Use p = F ÷ A."],
  "weight spread over many nails → large area, small pressure",
  ["The weight is spread over many nails so the area is large and the pressure is small; one nail gives a huge pressure", "with 1000 nails the total area is big so pressure is low, but on a single nail the pressure is very high"],
  ["The nails are blunt", "The performer has no weight"], min_points=2)

Q("w3b_tractor_tyres", 3, "3i", "Explain why tractors that work in muddy fields have very wide tyres.",
  [P("wide tyres give a large area of contact with the ground", ["large area", "bigger area", "wide area", "more area", "larger contact area"]),
   P("so the tractor's weight produces a smaller pressure", ["smaller pressure", "less pressure", "lower pressure", "pressure is reduced", "reduces the pressure"]),
   P("so the tractor sinks less into the soft mud", ["sink less", "does not sink", "not sink", "less likely to sink", "stuck"])],
  "Wide tyres have a large area in contact with the ground, so the tractor's weight is spread out and the pressure on the mud is smaller. With a lower pressure the tractor does not sink as far into the soft ground.",
  ["The tractor's weight is fixed.", "How do wide tyres change the area?", "What does that do to the pressure?"],
  "wide tyres → large area → small pressure → less sinking",
  ["Wide tyres give a large area so the pressure is smaller and the tractor does not sink into the mud", "the bigger area reduces the pressure so it sinks less"],
  ["Wide tyres make the tractor lighter", "Wide tyres increase the pressure for better grip"], min_points=2,
  pitfalls=[PF(["increase the pressure", "more pressure", "makes it lighter"], "Wide tyres DECREASE the pressure by increasing the area; the weight is unchanged.")])

Q("w3b_hollow_ball_floats", 3, "3g", "A solid steel ball sinks in water, but a hollow steel ball of the same size floats. Explain why.",
  [P("the hollow ball contains air, so its total mass is much smaller for the same volume", ["contains air", "full of air", "less mass", "smaller mass", "lighter", "air inside"]),
   P("so its average density is less than that of water", ["average density", "overall density", "less dense than water", "density less than water", "lower density"]),
   P("the solid ball's density (steel) is greater than water's", ["steel is denser", "denser than water", "greater than water", "more dense than water"])],
  "Steel is denser than water, so the solid ball sinks. The hollow ball has the same volume but contains air, so its total mass is much smaller; its average density is less than that of water, so it floats.",
  ["What is inside the hollow ball?", "How does that change its mass for the same volume?", "Compare its average density with water."],
  "hollow → less mass for same volume → average density < water",
  ["The hollow ball has air inside, so its average density is less than water and it floats; solid steel is denser than water", "less mass for the same volume, so the overall density is lower than water"],
  ["The hollow ball is made of a lighter type of steel", "Solid balls always float"], min_points=2)

Q("w3b_shops_sell_kg", 3, "3f", "Fruit is sold by the kilogram. Explain why the amount of fruit you get for 1 kg would be the same on the Moon, though the fruit would weigh less there.",
  [P("the kilogram is a unit of mass, the amount of matter, which is the same everywhere", ["mass", "amount of matter", "same everywhere", "does not change", "same amount"]),
   P("weight = m g, and g is smaller on the Moon, so the weight is smaller", ["g is smaller", "weaker gravity", "smaller g", "weighs less", "less weight", "1.6"])],
  "The kilogram measures mass, the amount of matter, which does not depend on where you are, so 1 kg of fruit is the same amount anywhere. Its weight is m g, and the Moon's gravitational field strength is smaller, so the same fruit weighs less there.",
  ["Is the kilogram a unit of mass or of weight?", "Does the amount of matter change on the Moon?", "Why is the weight smaller?"],
  "kg measures mass (unchanged); weight smaller because g smaller",
  ["1 kg is a mass, the amount of matter, which is the same everywhere, but the fruit weighs less because g is smaller on the Moon", "mass stays the same; weight = mg and the Moon has weaker gravity"],
  ["Fruit is lighter on the Moon so you get more of it", "Kilograms measure weight"], min_points=2, pitfalls=[MASS_IS_WEIGHT])

Q("w3b_find_g_planet", 3, "3d", "Describe how an astronaut could find the gravitational field strength on another planet using a 1 kg mass and a spring balance.",
  [P("hang the 1 kg mass on the spring balance and read its weight in newtons", ["hang the mass", "hang it on the spring balance", "read the weight", "measure the weight", "spring balance reading", "reading in newtons"]),
   P("g = weight ÷ mass (here, g in N/kg equals the reading in N)", ["weight ÷ mass", "weight divided by mass", "g = w / m", "reading equals g", "divide by the mass", "w ÷ m", "divided by 1 kg"])],
  "Hang the 1 kg mass on the spring balance and read the force (its weight) in newtons. Then g = weight ÷ mass; with a 1 kg mass, the value of g in N/kg is simply the reading in N.",
  ["What does a spring balance measure?", "What is g defined as?", "Combine these with the known mass."],
  "measure weight of known mass; g = W ÷ m",
  ["Hang the 1 kg mass on the spring balance, read the weight, then g = weight ÷ mass", "the reading in newtons divided by 1 kg gives g"],
  ["Use a beam balance to find g", "Drop the mass and listen"], min_points=2)

Q("w3b_cheese_wire", 3, "3i", "Explain why a thin wire cuts through a block of cheese more easily than a thick knife blade pressed with the same force.",
  [P("the thin wire has a very small area of contact", ["small area", "tiny area", "smaller area", "thin"]),
   P("so it exerts a much larger pressure for the same force", ["larger pressure", "greater pressure", "higher pressure", "more pressure"])],
  "The thin wire touches the cheese over a very small area, so for the same force it exerts a much larger pressure (p = F ÷ A) than the thick blade, and cuts through more easily.",
  ["Compare the areas in contact with the cheese.", "The force is the same.", "Use p = F ÷ A."],
  "small area → large pressure",
  ["The thin wire has a smaller area, so the pressure is greater for the same force", "tiny contact area gives a higher pressure"],
  ["The wire is sharper because it is heavier", "The wire uses more force"], min_points=2)

Q("w3b_steel_ship_floats", 3, "3g", "Steel is about 8 times denser than water, yet a steel ship floats. Explain how.",
  [P("the ship is hollow and contains a large volume of air", ["hollow", "contains air", "full of air", "air inside", "large volume"]),
   P("so its average density (total mass ÷ total volume) is less than that of water", ["average density", "overall density", "less than water", "less dense than water", "total mass ÷ total volume"])],
  "The ship is hollow and encloses a large volume of air. Its average density, its total mass divided by its total volume, is therefore less than the density of water, so it floats even though steel itself is denser than water.",
  ["Is the ship solid steel?", "What fills most of its volume?", "Compare its average density with water."],
  "hollow; average density < water",
  ["The ship is hollow with air inside, so its average density is less than water", "its overall density, total mass divided by total volume, is lower than water's"],
  ["Steel becomes lighter in water", "The ship is pushed up by the engines"], min_points=1)

Q("w3b_field_towards_centre", 3, "3c", "Explain what is meant by the Earth's gravitational field and in which direction it pulls on objects.",
  [P("a region in which a mass experiences a force due to gravitational attraction", ["region", "space around", "mass experiences a force", "experiences a force", "gravitational attraction"]),
   P("the force (weight) acts towards the centre of the Earth (vertically downwards)", ["towards the centre", "centre of the earth", "downwards", "vertically down", "towards the earth"])],
  "The Earth's gravitational field is the region around the Earth in which any mass experiences a force due to gravitational attraction. This force, the object's weight, acts towards the centre of the Earth, which we call vertically downwards.",
  ["A field is a region of space.", "What experiences the force in a gravitational field?", "In which direction does the force act?"],
  "region where mass feels gravitational force; towards Earth's centre",
  ["It is the region around the Earth where a mass experiences a force, which acts towards the centre of the Earth", "a space in which masses feel gravitational attraction, pulling them downwards towards the Earth's centre"],
  ["The layer of air around the Earth", "A region where magnets work"], min_points=2)

Q("w3b_parachutist_forces", 3, "3a", "A parachutist falls through the air. Name one contact force and one non-contact force acting on her and explain the difference.",
  [P("contact: air resistance (drag) from the air touching her", ["air resistance", "drag"]),
   P("non-contact: her weight (gravitational force)", ["weight", "gravity", "gravitational"]),
   P("contact forces need touching; non-contact forces act at a distance", ["touching", "contact", "at a distance", "without touching"])],
  "Air resistance is a contact force: it comes from the air in contact with her. Her weight, the gravitational pull of the Earth, is a non-contact force: it acts at a distance without anything touching her.",
  ["Which force comes from the air around her?", "Which force acts without touching?", "Explain the difference."],
  "air resistance (contact); weight (non-contact)",
  ["Air resistance is a contact force because the air touches her, and her weight is a non-contact force acting at a distance", "contact: drag; non-contact: gravity, which acts without touching"],
  ["Both are contact forces", "Her weight is a contact force"], min_points=2,
  pitfalls=[PF(["weight is a contact force", "both are contact forces", "gravity is a contact force"], "Weight (gravity) acts at a distance: it is a NON-contact force.")])

Q("w3b_moon_jump", 3, "3f", "Explain why an astronaut can jump much higher on the Moon than on Earth.",
  [P("her mass is the same but her weight is smaller on the Moon", ["weight is smaller", "weighs less", "less weight", "smaller weight", "lighter"]),
   P("because the Moon's gravitational field strength is smaller (about 1.6 N/kg)", ["g is smaller", "weaker gravity", "1.6", "smaller gravitational field", "weaker field", "less gravity"]),
   P("so the same push gives a greater upward motion before gravity brings her back", ["same push", "same force", "goes higher", "pulled back less", "takes longer to come down"])],
  "Her mass is unchanged, but the Moon's gravitational field strength is only about 1.6 N/kg, so her weight is much smaller. The same push from her legs therefore lifts her much higher before gravity brings her back down.",
  ["What changes on the Moon: mass or weight?", "Why?", "How does that affect a jump?"],
  "smaller g → smaller weight → higher jump",
  ["Her weight is smaller because the Moon's gravity is weaker, so the same push takes her higher", "g is only 1.6 N/kg on the Moon, so she weighs less and can jump higher"],
  ["Her mass is smaller on the Moon", "There is no gravity on the Moon"], min_points=2,
  pitfalls=[PF(["mass is smaller", "less mass", "no gravity", "there is no gravity"], "Her mass is unchanged, and the Moon does have gravity, just weaker.")])

# ---------------------------------------------------------------- L4
Q("w3b_identify_metal", 4, "3g", "Describe how you could identify an unknown metal cube by measuring its density and using a table of densities.",
  [P("measure the mass on a balance", ["balance", "mass", "weigh"]),
   P("measure the sides with vernier calipers/ruler and calculate the volume (l × b × h)", ["vernier", "ruler", "length", "volume = l", "l × b × h", "length × breadth", "measure the sides", "calculate the volume"]),
   P("density = mass ÷ volume, then compare with the table to find the closest match", ["mass ÷ volume", "mass divided by volume", "compare with the table", "match", "closest value", "look up"])],
  "Measure the cube's mass on a balance. Measure its sides with vernier calipers and calculate its volume as length × breadth × height. Calculate density = mass ÷ volume and compare the value with the table of densities: the metal with the closest density is the likely one.",
  ["What two quantities give density?", "How do you find the volume of a cube?", "What do you do with the result?"],
  "mass (balance); volume from sides; ρ = m ÷ V; compare with table",
  ["Weigh it, measure the sides to find the volume, work out mass ÷ volume and compare it with the table", "find the density from mass and volume and match it to the closest value in the table"],
  ["Look at its colour", "Measure how hot it gets"], min_points=2)

Q("w3b_least_pressure_box", 4, "3i", "A heavy box must be stored on a soft floor. Explain how it should be placed to exert the least pressure, and why.",
  [P("rest it on its largest face", ["largest face", "biggest face", "largest side", "biggest side", "largest area", "flat side"]),
   P("the weight is the same whichever face it rests on", ["weight is the same", "same weight", "force is the same", "same force"]),
   P("pressure = force ÷ area, so the largest area gives the smallest pressure", ["force ÷ area", "largest area gives", "smallest pressure", "least pressure", "lower pressure"])],
  "The box should rest on its largest face. Its weight is the same whichever face it rests on, and pressure = force ÷ area, so the largest area gives the smallest pressure on the floor.",
  ["Does the weight change when you turn the box?", "Which changes: force or area?", "Use p = F ÷ A."],
  "largest face; same weight; largest area → least pressure",
  ["Put it on its largest face because the weight is the same, so the largest area gives the least pressure", "the force is the same, so rest it on the biggest side for the lowest pressure"],
  ["Stand it on its smallest face", "It makes no difference"], min_points=2,
  pitfalls=[PF(["smallest face", "smallest side"], "The smallest face gives the GREATEST pressure.")])

Q("w3b_helium_balloon", 4, "3g", "A balloon filled with helium rises, but the same balloon filled with air from your lungs sinks. Explain in terms of density.",
  [P("helium is much less dense than air", ["helium is less dense", "lower density than air", "less dense than air", "helium is lighter"]),
   P("so the helium balloon's average density is less than the surrounding air, and it rises", ["average density", "less dense than the air", "rises", "floats up"]),
   P("air from your lungs makes the balloon (plus rubber) denser than the surrounding air, so it sinks", ["denser than the air", "more dense than the air", "sinks", "falls", "rubber adds"])],
  "Helium is much less dense than air, so the average density of the helium-filled balloon (helium plus rubber) is less than that of the surrounding air, and it rises. Filled with air, the balloon's average density is a little more than the surrounding air because of the rubber (and the slightly compressed air), so it sinks.",
  ["Compare the density of helium with air.", "What is the average density of each balloon?", "When does something rise in air?"],
  "helium less dense; average density compared with surrounding air",
  ["Helium is less dense than air so the balloon's average density is lower than the air and it rises; with air inside it is denser than the air around it and sinks", "the helium balloon has an average density less than air so it floats up, but the air-filled one is denser and falls"],
  ["Helium is heavier than air", "The air balloon has less mass"], min_points=2)

Q("w3b_ice_rescue", 4, "3i", "A person has fallen through thin ice. Explain why a rescuer should lie flat on the ice, or on a ladder, rather than walk towards them.",
  [P("lying flat (or on a ladder) spreads the weight over a large area", ["spread", "large area", "bigger area", "larger area", "spread the weight"]),
   P("so the pressure on the ice is smaller", ["smaller pressure", "less pressure", "lower pressure", "reduces the pressure"]),
   P("walking puts the weight on the small area of the feet, giving a large pressure that may break the ice", ["feet", "small area", "large pressure", "break the ice", "crack"])],
  "Lying flat, or on a ladder, spreads the rescuer's weight over a large area, so the pressure on the ice is small and it is less likely to break. Walking puts the whole weight on the small area of the feet, giving a large pressure that could crack the ice.",
  ["Is the rescuer's weight the same either way?", "How does lying flat change the area?", "What does that do to the pressure on the ice?"],
  "lying flat → large area → small pressure; feet → large pressure",
  ["Lying flat spreads the weight over a large area so the pressure on the ice is smaller and it will not break", "walking puts the weight on a small area of the feet so the pressure is large and the ice may crack"],
  ["Lying flat makes the rescuer lighter", "It is warmer lying down"], min_points=2,
  pitfalls=[PF(["makes the rescuer lighter", "reduces the weight", "weighs less lying"], "Lying flat does not change the weight; it changes the area.")])

Q("w3b_pressure_cm2_convert", 4, "3i", "A force of 500 N acts on an area of 20 cm². Explain how to calculate the pressure in pascals, and give the answer.",
  [P("convert the area to m²: 20 cm² = 0.002 m² (÷ 10 000)", ["0.002 m2", "10 000", "÷ 10 000", "convert to m2", "into m2"]),
   P("p = F ÷ A = 500 ÷ 0.002", ["500 ÷ 0.002", "force ÷ area", "500 / 0.002", "f ÷ a"]),
   P("= 250 000 Pa", ["250 000", "250000", "2.5 × 10"])],
  "The pressure in pascals needs the area in m². 1 m² = 10 000 cm², so 20 cm² = 0.002 m². Then p = F ÷ A = 500 ÷ 0.002 = 250 000 Pa.",
  ["Which unit must the area be in to give pascals?", "1 m² = 10 000 cm².", "Then divide the force by the area."],
  "area to m² (÷ 10 000); p = F ÷ A; 250 000 Pa",
  ["Convert 20 cm² to 0.002 m², then 500 ÷ 0.002 = 250 000 Pa", "divide the area by 10 000 to get m², then force ÷ area gives 250000 Pa"],
  ["500 ÷ 20 = 25 Pa", "500 × 20 = 10 000 Pa"], min_points=2,
  pitfalls=[PF(["25 pa", "500 ÷ 20", "500 / 20"], "Convert cm² to m² before dividing.")])

Q("w3b_mixture_between", 4, "3g", "Water (1.0 g/cm³) and alcohol (0.8 g/cm³) are mixed. Explain why the density of the mixture is between the two values, and which it is closer to if there is much more water.",
  [P("the mixture's density is its total mass divided by its total volume", ["total mass ÷ total volume", "total mass divided by total volume", "total mass", "total volume"]),
   P("so it lies between the two densities (between 0.8 and 1.0 g/cm³)", ["between", "in between", "between 0.8 and 1.0"]),
   P("with much more water, it is closer to 1.0 g/cm³", ["closer to 1.0", "closer to water", "nearer to 1", "nearer to the water"])],
  "The density of the mixture is its total mass divided by its total volume, a weighted average of the two densities, so it lies between 0.8 and 1.0 g/cm³. If there is much more water, the water contributes most of the mass and volume, so the density is closer to 1.0 g/cm³.",
  ["How do you find the density of a mixture?", "Can the average be outside the range of the two values?", "Which liquid dominates if there is much more of it?"],
  "total mass ÷ total volume; between the values; closer to the major part",
  ["Its density is total mass divided by total volume, so it is between 0.8 and 1.0 g/cm³, and closer to 1.0 if there is more water", "the mixture is in between the two densities and nearer to water's when there is much more water"],
  ["It is 1.8 g/cm³ because you add them", "It is always exactly 0.9 g/cm³"], min_points=2,
  pitfalls=[PF(["1.8", "add the densities"], "Densities do not add; the mixture's density lies between the two values.")])

Q("w3b_layered_column", 4, "3g", "A column contains syrup at the bottom, water in the middle and oil at the top. A small plastic bead sinks through the oil but floats on the water. What can you say about its density? Explain.",
  [P("the bead is denser than oil (it sinks through the oil)", ["denser than oil", "more dense than oil", "greater than oil", "sinks through the oil"]),
   P("the bead is less dense than water (it floats on the water)", ["less dense than water", "lower than water", "floats on the water", "smaller than water"]),
   P("so its density is between those of oil and water", ["between", "in between", "between oil and water"])],
  "The bead sinks through the oil, so it is denser than oil. It floats on the water, so it is less dense than water. Its density therefore lies between the densities of oil and water.",
  ["What does sinking through a liquid tell you?", "What does floating on a liquid tell you?", "Combine the two."],
  "denser than oil, less dense than water → between",
  ["It is denser than oil but less dense than water, so its density is between the two", "it sinks in oil so it is more dense than oil, and floats on water so it is less dense than water"],
  ["It is denser than syrup", "It has no density"], min_points=2)

Q("w3b_space_station_push", 4, "3f", "Objects on a space station float, as if weightless. Explain why it is still hard to push a large toolbox across the station.",
  [P("the toolbox still has its full mass (amount of matter)", ["still has mass", "mass is the same", "same mass", "mass does not change", "large mass"]),
   P("a large mass needs a large force to accelerate it (it resists changes in motion)", ["large force", "hard to accelerate", "resists", "inertia", "f = ma", "needs a big force"]),
   P("floating means its weight is not felt, but mass is unchanged", ["weight", "weightless", "floats", "not felt"])],
  "Floating means the toolbox's weight is not felt, but it still has its full mass. A large mass needs a large force to accelerate it (F = m a), so it is still hard to get it moving or to stop it.",
  ["Does the toolbox lose mass in orbit?", "What does mass have to do with starting something moving?", "Explain the difference between not feeling weight and having no mass."],
  "mass unchanged; large mass needs large force to accelerate",
  ["It still has its large mass, so a large force is needed to accelerate it even though it floats", "mass does not change in space, and F = ma means a big mass needs a big force"],
  ["Because it is heavy in space", "Because there is no air"], min_points=2)

Q("w3b_g_meaning_apply", 4, "3d", "Using the meaning of gravitational field strength, explain why a 3 kg mass has a weight of 30 N on Earth.",
  [P("g = 10 N/kg means each kilogram experiences a force of 10 N", ["each kilogram", "every kilogram", "per kilogram", "10 n on each kg", "10 n/kg"]),
   P("so 3 kg experiences 3 × 10 = 30 N (W = m g)", ["3 × 10", "w = mg", "w = m g", "30 n", "three kilograms"])],
  "The Earth's gravitational field strength is 10 N/kg, which means each kilogram of mass experiences a gravitational force of 10 N. A 3 kg mass therefore experiences 3 × 10 = 30 N, so W = m g = 30 N.",
  ["What does 10 N/kg mean?", "How many kilograms are there?", "Combine."],
  "10 N on each kg; 3 × 10 = 30 N",
  ["g = 10 N/kg means each kilogram feels 10 N, so 3 kg feels 3 × 10 = 30 N", "W = mg: every kilogram has a weight of 10 N, so 3 kg weighs 30 N"],
  ["Because 3 + 27 = 30", "Because 3 kg is 30 N in any place"], min_points=2)

Q("w3b_needle_injection", 4, "3i", "A nurse uses a fine needle to give an injection. Explain why the needle is very sharp.",
  [P("the sharp tip has a very small area", ["small area", "tiny area", "very small area", "point"]),
   P("so a small force from the nurse produces a very large pressure", ["large pressure", "high pressure", "great pressure", "small force"]),
   P("which pierces the skin easily (with less pain and damage)", ["pierce", "through the skin", "penetrate", "less pain", "easily"])],
  "The sharp tip of the needle has a very small area, so even a small force from the nurse produces a very large pressure (p = F ÷ A). This large pressure lets the needle pierce the skin easily, causing less pain.",
  ["How big is the area at the tip?", "What does that do to the pressure for a given force?", "Why is that useful?"],
  "small area → large pressure → pierces easily",
  ["The sharp tip has a tiny area so a small force gives a large pressure that pierces the skin easily", "a small area means high pressure, so it goes through the skin with little force"],
  ["Sharp needles are lighter", "It makes the medicine flow faster"], min_points=2)

# ---------------------------------------------------------------- L5
Q("w3b_big_wood_denser_claim", 5, "3g", "A student says: 'A large log is denser than a small twig of the same wood because it is heavier.' Evaluate this claim.",
  [P("wrong: both have the same density", ["wrong", "same density", "equal density", "incorrect"]),
   P("the log has more mass but also proportionally more volume", ["more volume", "more mass", "volume increases", "both increase", "larger volume"]),
   P("density = mass ÷ volume is a property of the material, not the size", ["property of the material", "depends on the material", "not the size", "mass ÷ volume", "mass divided by volume"])],
  "The claim is wrong. The log is heavier because it has more mass, but it also has proportionally more volume. Density = mass ÷ volume is a property of the material, so the log and the twig have the same density.",
  ["What does density measure?", "If the log has more mass, what else does it have more of?", "Does density depend on size?"],
  "same density; more mass and more volume; property of material",
  ["Wrong: the log has more mass but also more volume, so mass ÷ volume is the same", "they have the same density because density depends on the material, not the size"],
  ["Correct, heavier things are denser", "Correct, the log is denser"], min_points=2,
  pitfalls=[PF(["heavier things are denser", "heavier objects are denser", "log is denser"], "Being heavier does not make something denser.")])

Q("w3b_shoe_prints_design", 5, "3i", "Design an experiment to compare the pressures exerted on soft sand by a flat shoe and a high-heeled shoe worn by the same person.",
  [P("the same person (same weight) stands in each shoe on the same smooth, soft sand", ["same person", "same weight", "same sand", "smooth sand", "fair test"]),
   P("measure the depth of each print (deeper print = larger pressure)", ["depth of the print", "how deep", "depth", "deeper", "measure the depth"]),
   P("or estimate each contact area and use p = weight ÷ area", ["contact area", "area of the sole", "weight ÷ area", "force ÷ area", "draw round", "squared paper"])],
  "Smooth a tray of soft sand. The same person (so the same weight) stands still in each shoe for the same time, and the depth of each print is measured: the deeper print shows the larger pressure. Alternatively, find each contact area by drawing round the parts that touch on squared paper and calculate pressure = weight ÷ area.",
  ["What must be kept the same?", "How can you show which shoe exerts more pressure?", "Could you calculate the pressures too?"],
  "same weight, same sand; compare depth or calculate weight ÷ area",
  ["The same person stands on the same sand in each shoe and I measure the depth of the prints; the deeper one has the larger pressure", "keep the weight the same, find each contact area on squared paper and work out weight ÷ area"],
  ["Weigh the shoes", "Ask which shoe is more comfortable"], min_points=2)

Q("w3b_kitchen_scale_moon", 5, "3f", "A kitchen scale works by measuring the force with which an object presses on it, but it shows the result in kilograms. Evaluate how well it would work on the Moon.",
  [P("it actually measures weight (force), calibrated for Earth's g", ["measures weight", "measures force", "calibrated for earth", "set for 10 n/kg", "assumes g"]),
   P("on the Moon the weight is about one-sixth, so it would show a mass about one-sixth of the true value", ["one-sixth", "1/6", "too small", "too low", "less than the true", "smaller reading"]),
   P("a beam balance would give the correct mass because it compares masses", ["beam balance", "compares masses", "correct mass"])],
  "The scale really measures weight, the force pressing on it, and converts it to kilograms assuming Earth's g. On the Moon the weight is only about one-sixth as large, so it would show a mass about one-sixth of the true value. A beam balance, which compares masses, would give the correct mass on the Moon.",
  ["What does the scale actually detect?", "How does that change on the Moon?", "What instrument would still give the right mass?"],
  "measures weight calibrated for Earth; reads ~1/6 on Moon; beam balance correct",
  ["It measures weight using Earth's g, so on the Moon it would read about one-sixth of the true mass; a beam balance would be correct", "the reading would be too low because the force is smaller on the Moon"],
  ["It works perfectly because mass does not change", "It would read six times too much"], min_points=1)

Q("w3b_egg_salt_water", 5, "3g", "An egg sinks in tap water but floats in very salty water. Explain this, and describe how you could find the salt concentration at which it just floats.",
  [P("the egg is denser than tap water but less dense than the salty water", ["denser than tap water", "less dense than the salty", "less dense than salt water", "salty water is denser", "higher density than the egg", "denser than the egg"]),
   P("dissolving salt increases the density of the water", ["salt increases the density", "salt makes the water denser", "increases the density", "denser"]),
   P("add salt gradually (stirring), testing until the egg just floats; measure the salt added", ["add salt gradually", "a little at a time", "stir", "until it just floats", "measure the mass of salt", "gradually"])],
  "The egg is denser than tap water, so it sinks, but dissolving salt increases the density of the water. In very salty water the water is denser than the egg, so the egg floats. To find the concentration at which it just floats, add salt a little at a time, stirring, until the egg just rises, recording the mass of salt added to a known volume of water.",
  ["How does salt change the water?", "Compare the egg's density with each liquid.", "How could you find the point where it just floats?"],
  "salt raises water's density; egg between; add salt gradually",
  ["The egg is denser than tap water but salt makes the water denser than the egg; add salt gradually and stir until it just floats", "salty water has a higher density than the egg, so add a little salt at a time and measure how much is needed"],
  ["Salt makes the egg lighter", "The egg absorbs salt and floats"], min_points=2)

Q("w3b_moon_no_air_claim", 5, "3a", "A student says: 'There is no gravity on the Moon because there is no air there.' Evaluate this claim.",
  [P("wrong: gravity does not need air (it is a non-contact force acting through empty space)", ["wrong", "does not need air", "no need for air", "non-contact", "acts through a vacuum", "acts through space", "incorrect"]),
   P("the Moon has a gravitational field (g about 1.6 N/kg), which is why astronauts have weight there", ["1.6", "has gravity", "gravitational field", "astronauts have weight", "things fall"]),
   P("its gravity is weaker because the Moon's mass is smaller, not because there is no air", ["weaker", "smaller mass", "less mass", "not because of air"])],
  "The claim is wrong. Gravity is a non-contact force and does not need air; it acts through empty space. The Moon has a gravitational field of about 1.6 N/kg, which is why astronauts have weight and dropped objects fall there. Its gravity is weaker than the Earth's because the Moon has a much smaller mass, not because it has no air.",
  ["Does gravity need a medium such as air?", "Do objects fall on the Moon?", "Why is the Moon's gravity weaker?"],
  "gravity needs no air; Moon g ≈ 1.6 N/kg; weaker due to smaller mass",
  ["Wrong: gravity does not need air; the Moon has g of 1.6 N/kg because it has mass, just weaker than Earth's", "incorrect, gravity is a non-contact force that acts through space, and things still fall on the Moon"],
  ["Correct, gravity needs air", "Correct, there is no gravity on the Moon"], min_points=2,
  pitfalls=[PF(["gravity needs air", "no gravity on the moon"], "Gravity acts through empty space; the Moon has a gravitational field.")])

Q("w3b_tyres_sand_vs_race", 5, "3i", "A vehicle for soft desert sand needs different tyres from a racing car on a hard track. Suggest and explain suitable tyres for the desert vehicle.",
  [P("wide tyres (large contact area)", ["wide", "large area", "bigger area", "broad"]),
   P("give a small pressure on the sand", ["small pressure", "low pressure", "less pressure", "reduce the pressure"]),
   P("so the vehicle does not sink into the soft sand (the sand cannot support a large pressure)", ["not sink", "sink less", "does not sink", "soft sand", "cannot support"])],
  "The desert vehicle needs wide tyres with a large contact area. For the same weight, a large area gives a small pressure on the sand, so the vehicle does not sink into the soft sand, which cannot support a large pressure. A racing car on a hard track does not have this problem.",
  ["What is the problem with soft sand?", "How do you reduce the pressure for the same weight?", "Suggest a tyre design."],
  "wide tyres → large area → low pressure → no sinking",
  ["Wide tyres with a large area give a low pressure so the vehicle does not sink into the sand", "use broad tyres to reduce the pressure on the soft sand so it sinks less"],
  ["Thin tyres to cut through the sand", "Heavier tyres to press harder"], min_points=2,
  pitfalls=[PF(["thin tyres", "narrow tyres", "press harder"], "Thin tyres increase the pressure and make sinking worse.")])

Q("w3b_bubble_density_error", 5, "3g", "When measuring the volume of a stone by displacement, an air bubble is trapped against the stone under water. Evaluate the effect on the density obtained.",
  [P("the bubble adds to the displaced volume, so the measured volume is too large", ["volume is too large", "volume too big", "measured volume is larger", "adds to the volume", "overestimate the volume"]),
   P("so the calculated density (mass ÷ volume) is too small", ["density is too small", "density too low", "underestimate", "smaller density", "density is less"]),
   P("remove the bubble (tap the cylinder, lower slowly) and repeat", ["remove the bubble", "tap", "lower slowly", "shake off", "repeat"])],
  "The trapped bubble displaces water too, so the measured volume is larger than the stone's true volume. Since density = mass ÷ volume, the calculated density is too small. The bubble should be removed, for example by tapping the cylinder or lowering the stone slowly, and the measurement repeated.",
  ["What does the bubble do to the water level?", "How does that affect the volume measured?", "And the density?"],
  "volume too large → density too small; remove bubble",
  ["The bubble makes the measured volume too large, so the density is too small; tap the cylinder to remove it", "volume is overestimated so mass ÷ volume gives a lower density; lower the stone slowly and repeat"],
  ["The density is too large", "It has no effect on density"], min_points=2,
  pitfalls=[PF(["density is too large", "density too big", "density is higher"], "A larger measured volume makes the density SMALLER.")])

Q("w3b_planet_weights_table", 5, "3e", "The table gives g on three bodies. Explain how a 60 kg astronaut's mass and weight compare on them.\n\n| body | g / N/kg |\n|---|---|\n| Moon | 1.6 |\n| Mars | 3.7 |\n| Earth | 10 |",
  [P("her mass is 60 kg on all three", ["60 kg on all", "mass is the same", "mass stays 60", "same mass", "mass does not change"]),
   P("weight = m g: Moon 96 N, Mars 222 N, Earth 600 N", ["96 n", "222 n", "600 n", "w = mg", "m × g"]),
   P("so the weight is largest on Earth and smallest on the Moon", ["largest on earth", "smallest on the moon", "greatest on earth", "least on the moon", "heaviest on earth"])],
  "Her mass is 60 kg on all three, because the amount of matter in her does not change. Her weight is W = m g: about 96 N on the Moon, 222 N on Mars and 600 N on Earth, so her weight is largest on Earth and smallest on the Moon.",
  ["Does her mass change from place to place?", "Use W = m g with each value of g.", "Rank the weights."],
  "mass 60 kg everywhere; W = m g → 96, 222, 600 N",
  ["Her mass is 60 kg everywhere; her weight is 96 N on the Moon, 222 N on Mars and 600 N on Earth, so it is largest on Earth", "the mass is the same, but W = mg so she weighs most on Earth and least on the Moon"],
  ["Her mass is smallest on the Moon", "Her weight is the same everywhere"], min_points=2,
  pitfalls=[PF(["mass is smallest", "mass changes", "weight is the same everywhere"], "Mass is unchanged; weight changes with g.")])

Q("w3b_ice_skates", 5, "3i", "Ice-skate blades are very narrow. Explain how this helps the skater, using ideas about pressure.",
  [P("the narrow blade has a very small area in contact with the ice", ["small area", "narrow", "tiny area", "thin blade"]),
   P("so the skater's weight produces a very large pressure on the ice", ["large pressure", "high pressure", "great pressure", "very large pressure"]),
   P("the large pressure lets the blade grip / dig in (and helps a thin layer of ice melt so it glides)", ["grip", "dig into", "cut into", "melt", "glide", "water layer"])],
  "The narrow blade has a very small area in contact with the ice, so the skater's weight produces a very large pressure. This large pressure lets the blade bite into the ice for grip and control, and helps a thin layer of ice under the blade melt, so the skater glides.",
  ["How big is the contact area of a blade?", "What does that do to the pressure?", "How does a large pressure help on ice?"],
  "small area → large pressure → grip/glide",
  ["The blade has a tiny area so the pressure is very large, letting it dig into the ice and grip", "narrow blades give a high pressure, which helps the skate cut into the ice and glide"],
  ["Narrow blades make the skater lighter", "They reduce the pressure so the skater floats"], min_points=2)

Q("w3b_hollow_ball_test", 5, "3g", "A metal ball looks solid. Describe how you could use density to test whether it is hollow, using a table of metal densities.",
  [P("measure the ball's mass with a balance", ["balance", "mass", "weigh"]),
   P("find its volume (by displacement, or from its diameter)", ["displacement", "volume", "diameter", "measuring cylinder", "overflow can"]),
   P("calculate density = mass ÷ volume; if it is much less than the table value for that metal, the ball is hollow", ["less than the table", "lower than expected", "smaller than the value", "mass ÷ volume", "much less", "hollow"])],
  "Measure the ball's mass with a balance and its volume by displacement (or from its diameter). Calculate density = mass ÷ volume and compare it with the table value for the metal. If the measured density is much less than the table value, the ball must contain a hollow space.",
  ["How do you find the ball's density?", "What would the density be if it were solid?", "What would a hollow ball show?"],
  "measure m and V; ρ = m ÷ V; much lower than table → hollow",
  ["Weigh it, find its volume by displacement, work out mass ÷ volume and if it is much less than the table value it is hollow", "if the density is lower than expected for that metal, the ball is hollow"],
  ["Shake it and listen", "Look at its colour"], min_points=1)
