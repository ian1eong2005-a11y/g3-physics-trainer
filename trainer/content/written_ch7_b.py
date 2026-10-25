"""Chapter 7 Kinetic Particle Model of Matter: 50 more written-answer questions (10 per level), marked by keywords/phrases."""
from .. import figs, sketches
from ..marker import Pitfall, Point
from .base import written

P = Point
PF = Pitfall
CH = 7


def Q(id, lv, lo, stem, points, model, hints, keywords, passes, fails, pitfalls=(), min_points=None, figure=None):
    written(id, CH, lv, lo, stem=stem, points=points, model_answer=model, hints=hints, keywords=keywords,
            pitfalls=pitfalls, min_points=min_points, figure=figure, sample_pass=passes, sample_fail=fails)


BIGGER = PF(["particles get bigger", "particles expand", "particles grow", "molecules get bigger", "particles become bigger"],
            "Particles do not change size; it is their speed and spacing that change.")
STOP = PF(["particles stop moving", "particles are not moving", "particles do not move", "stop vibrating"],
          "Particles never stop moving; in a solid they vibrate about fixed positions.")

# ---------------------------------------------------------------- L1
Q("w7b_liquid_arrangement", 1, "7b", "Fig. 1 shows the particles in a liquid. Describe their arrangement.",
  [P("close together (touching)", ["close together", "closely packed", "touching", "close to each other", "near each other"]),
   P("in a random (irregular) arrangement, not in fixed positions", ["random", "irregular", "no regular pattern", "not in a pattern", "disordered", "not fixed"])],
  "The particles in a liquid are close together, touching their neighbours, but arranged randomly with no regular pattern.",
  ["Are the particles close or far apart?", "Is there a regular pattern?", "Describe both features."],
  "close together, random arrangement",
  ["They are close together but in a random arrangement", "closely packed with no regular pattern"],
  ["Far apart and moving freely", "In a regular lattice"], min_points=2,
  figure=lambda: sketches.particles("liquid"))

Q("w7b_name_boiling", 1, "7e", "Name the change of state from liquid to gas that happens throughout a liquid at a fixed temperature.",
  [P("boiling", ["boiling", "boil"])],
  "This change of state is boiling; it happens throughout the liquid at the boiling point.",
  ["Think of a kettle.", "Bubbles of gas form throughout the liquid.", "Name the process."],
  "boiling", ["Boiling", "it is called boiling"], ["Melting", "Condensation"])

Q("w7b_name_solidification", 1, "7e", "Name the change of state from liquid to solid.",
  [P("solidification (freezing)", ["solidification", "solidifying", "freezing", "freeze", "solidify"])],
  "The change from liquid to solid is called solidification (freezing).",
  ["Think of water turning into ice.", "It is the reverse of melting.", "Name the process."],
  "solidification / freezing", ["Freezing", "solidification"], ["Melting", "Boiling"])

Q("w7b_solid_motion", 1, "7b", "Describe the motion of the particles in a solid.",
  [P("they vibrate (about fixed positions)", ["vibrate", "vibrating", "vibration", "jiggle"]),
   P("about fixed positions (they do not move from place to place)", ["fixed positions", "fixed position", "do not move around", "stay in place", "same place", "cannot move around"])],
  "The particles in a solid vibrate about fixed positions; they do not move from place to place.",
  ["Do particles in a solid stay still?", "Do they move around freely?", "Describe their motion."],
  "vibrate about fixed positions",
  ["They vibrate about fixed positions", "the particles vibrate but stay in the same place"],
  ["They move freely in all directions", "They do not move at all"], min_points=2, pitfalls=[STOP])

Q("w7b_gas_arrangement", 1, "7b", "Describe the arrangement of the particles in a gas.",
  [P("far apart (large spaces between them)", ["far apart", "large spaces", "spread out", "widely spaced", "lots of space", "big gaps"]),
   P("randomly arranged", ["random", "irregular", "no pattern", "no regular pattern", "disordered"])],
  "The particles in a gas are far apart, with large spaces between them, and are randomly arranged.",
  ["Are gas particles close together?", "Is there any pattern?", "Describe both."],
  "far apart, random",
  ["They are far apart and randomly arranged", "spread out with large spaces and no pattern"],
  ["Close together in rows", "Touching in a regular pattern"], min_points=2)

Q("w7b_temperature_falls", 1, "7c", "State what happens to the average kinetic energy of the particles in a body when its temperature falls.",
  [P("it decreases (particles move more slowly on average)", ["decreases", "falls", "goes down", "less kinetic energy", "slower", "move more slowly", "lower"])],
  "When the temperature falls, the average kinetic energy of the particles decreases, so they move more slowly on average.",
  ["Temperature is linked to the average kinetic energy of the particles.", "What happens to one when the other falls?", "State it."],
  "average KE decreases",
  ["It decreases", "the particles move more slowly, so their average kinetic energy falls"],
  ["It increases", "It stays the same"],
  pitfalls=[PF(["it increases", "increases", "stays the same"], "A lower temperature means a LOWER average kinetic energy.")])

Q("w7b_three_states", 1, "7a", "Name the three states of matter and give an example of each.",
  [P("solid (e.g. ice, iron)", ["solid"]), P("liquid (e.g. water, oil)", ["liquid"]), P("gas (e.g. steam, air, oxygen)", ["gas"])],
  "The three states of matter are solid (e.g. ice), liquid (e.g. water) and gas (e.g. steam).",
  ["Think of water in three forms.", "One keeps its shape, one flows, one fills its container.", "Name them."],
  "solid, liquid, gas",
  ["Solid like ice, liquid like water and gas like steam", "solid, liquid and gas"],
  ["Hot, warm and cold", "Ice, snow and frost"], min_points=3)

Q("w7b_gas_shape_volume", 1, "7a", "State whether a gas has a fixed shape and a fixed volume.",
  [P("no fixed shape", ["no fixed shape", "takes the shape", "not a fixed shape", "shape of its container", "neither a fixed shape", "not have a fixed shape"]),
   P("no fixed volume (it spreads to fill its container)", ["no fixed volume", "fills the container", "fills its container", "not a fixed volume", "spreads out", "fills any container"])],
  "A gas has neither a fixed shape nor a fixed volume: it spreads out to fill whatever container it is in.",
  ["Does a gas keep its own shape?", "Does it keep its own volume?", "Answer both."],
  "no fixed shape, no fixed volume",
  ["No fixed shape and no fixed volume; it fills its container", "it takes the shape of its container and fills the whole volume"],
  ["Fixed shape and fixed volume", "Fixed volume but no fixed shape"], min_points=2)

Q("w7b_melting_point_def", 1, "7e", "State what is meant by the melting point of a substance.",
  [P("the temperature at which the solid changes into a liquid", ["solid changes into a liquid", "solid turns into a liquid", "solid becomes a liquid", "solid to liquid", "starts to melt", "melts"]),
   P("it stays at this fixed temperature while melting", ["fixed temperature", "constant temperature", "stays the same", "specific temperature", "particular temperature"])],
  "The melting point is the fixed temperature at which a solid changes into a liquid; the temperature stays constant while it melts.",
  ["Melting is a change of state.", "It happens at a particular temperature.", "Define it."],
  "temperature at which solid becomes liquid (fixed)",
  ["The temperature at which a solid changes into a liquid", "the fixed temperature where the solid melts"],
  ["The temperature at which a liquid boils", "When a gas becomes a liquid"], min_points=1)

Q("w7b_liquid_shape_volume", 1, "7a", "State whether a liquid has a fixed shape and a fixed volume.",
  [P("fixed volume", ["fixed volume", "volume is fixed", "definite volume", "keeps its volume", "same volume"]),
   P("no fixed shape (takes the shape of its container)", ["no fixed shape", "takes the shape", "shape of its container", "shape of the container", "not a fixed shape", "flows"])],
  "A liquid has a fixed volume but no fixed shape: it takes the shape of its container.",
  ["Pour water from a jug into a glass.", "Does its volume change? Its shape?", "Answer both."],
  "fixed volume, no fixed shape",
  ["It has a fixed volume but no fixed shape", "the volume stays the same but it takes the shape of the container"],
  ["Fixed shape and fixed volume", "No fixed volume"], min_points=2)

# ---------------------------------------------------------------- L2
Q("w7b_solid_hard_compress", 2, "7b", "Fig. 1 shows the particles in a solid. Explain why a solid is very difficult to compress.",
  [P("the particles are already very close together (touching)", ["close together", "closely packed", "touching", "no space", "very little space", "no gaps"]),
   P("so there is no room to push them closer (strong repulsion)", ["no room", "cannot be pushed closer", "cannot get closer", "repel", "nowhere to go"])],
  "The particles in a solid are already closely packed, touching their neighbours, so there is almost no space to push them closer together.",
  ["How much space is there between particles in a solid?", "What would compressing it need?", "Explain."],
  "particles closely packed; no space",
  ["The particles are already touching, so there is no room to push them closer", "they are closely packed with no space between them"],
  ["The particles are soft", "The particles are far apart"], min_points=1,
  figure=lambda: sketches.particles("solid"))

Q("w7b_gas_low_density", 2, "7b", "Explain, using the particle model, why gases have much lower densities than solids and liquids.",
  [P("gas particles are far apart with large spaces between them", ["far apart", "large spaces", "spread out", "lots of space", "big gaps"]),
   P("so a given volume contains far fewer particles (less mass per unit volume)", ["fewer particles", "less mass", "less mass per", "fewer particles in the same volume", "mass per unit volume"])],
  "Gas particles are far apart with large spaces between them, so a given volume of gas contains far fewer particles and therefore much less mass than the same volume of a solid or liquid. Density is mass per unit volume, so it is much lower.",
  ["How far apart are gas particles?", "How many particles fit in 1 cm³?", "Link to mass per unit volume."],
  "far apart → fewer particles per volume → less mass per volume",
  ["Gas particles are far apart, so the same volume has fewer particles and less mass", "large spaces mean less mass per unit volume"],
  ["Gas particles are lighter than solid particles", "Gases are hotter"], min_points=2)

Q("w7b_boil_constant", 2, "7e", "Explain why the temperature of boiling water stays at 100 °C even though it is still being heated.",
  [P("the energy supplied is used to separate the particles / overcome the attractive forces", ["overcome the forces", "overcome the attractive forces", "separate the particles", "break the forces", "pull the particles apart"]),
   P("this increases the potential energy, not the average kinetic energy, so the temperature stays constant", ["potential energy", "not the kinetic", "kinetic energy stays", "average kinetic energy does not", "temperature stays"])],
  "During boiling, the energy supplied is used to overcome the attractive forces between the particles and separate them into a gas. This increases their potential energy, not their average kinetic energy, so the temperature stays at 100 °C.",
  ["Where does the energy go during boiling?", "Which part of the internal energy increases?", "Why does the temperature not rise?"],
  "energy overcomes forces → PE up, KE same",
  ["The energy is used to overcome the attractive forces between the particles, increasing potential energy rather than kinetic energy", "it separates the particles, so the potential energy increases and the temperature stays the same"],
  ["The heater stops working", "Water cannot get hotter than 100 °C because it is too hot"], min_points=1)

Q("w7b_forces_solid_liquid", 2, "7b", "Compare the forces between particles in a solid and in a liquid, and explain how this affects their shapes.",
  [P("forces are strongest in a solid, holding particles in fixed positions", ["strong forces", "strongest in a solid", "stronger in the solid", "fixed positions", "hold them in place"]),
   P("forces in a liquid are weaker, letting particles slide past each other", ["weaker", "slide past", "move past each other", "less strong"]),
   P("so a solid keeps its shape while a liquid flows / takes the shape of its container", ["keeps its shape", "fixed shape", "flows", "takes the shape"])],
  "The attractive forces between particles are strongest in a solid, holding them in fixed positions, so a solid keeps its shape. In a liquid the forces are weaker, so the particles can slide past each other, and the liquid flows and takes the shape of its container.",
  ["Which state has the strongest attractive forces?", "What can liquid particles do that solid particles cannot?", "Link this to shape."],
  "solid: strong forces, fixed shape; liquid: weaker, slide, flows",
  ["The forces are stronger in a solid, holding particles in place so it keeps its shape; in a liquid they are weaker so particles slide past each other and it flows", "solids have strong forces and a fixed shape; liquids have weaker forces and flow"],
  ["Liquids have stronger forces than solids", "There are no forces in a solid"], min_points=2)

Q("w7b_heating_gas_speed", 2, "7c", "A gas is heated in a sealed container. Describe what happens to the motion of its particles.",
  [P("the particles move faster", ["move faster", "faster", "speed up", "higher speed", "more quickly"]),
   P("because their average kinetic energy increases as the temperature rises", ["kinetic energy increases", "more kinetic energy", "average kinetic energy", "temperature rises"])],
  "As the gas is heated its temperature rises, so the average kinetic energy of its particles increases and they move faster.",
  ["What is temperature linked to?", "What happens to that quantity when the gas is heated?", "Describe the motion."],
  "particles move faster (average KE up)",
  ["The particles move faster because their average kinetic energy increases", "they speed up as the temperature rises"],
  ["The particles get bigger", "The particles stop"], min_points=1, pitfalls=[BIGGER, STOP])

Q("w7b_freezing_releases", 2, "7e", "Explain why energy is released to the surroundings when water freezes.",
  [P("as water freezes the particles are pulled closer by attractive forces into fixed positions", ["pulled together", "closer together", "fixed positions", "attractive forces", "bonds form"]),
   P("their potential energy decreases, and this energy is transferred to the surroundings", ["potential energy decreases", "lose potential energy", "lowers the potential energy", "released", "transferred to the surroundings", "gives out energy", "giving out energy"])],
  "As water freezes, the attractive forces pull the particles closer together into fixed positions. Their potential energy decreases, and this energy is released to the surroundings, while the temperature stays at 0 °C.",
  ["What happens to the particles' arrangement on freezing?", "Which part of their internal energy changes?", "Where does that energy go?"],
  "particles pulled into fixed positions; PE decreases; energy released",
  ["The particles are pulled together into fixed positions, so their potential energy decreases and energy is released to the surroundings", "freezing lowers the potential energy of the particles, giving out energy"],
  ["Freezing absorbs energy from the surroundings", "No energy is involved"], min_points=1,
  pitfalls=[PF(["freezing absorbs energy", "absorbs energy"], "Freezing RELEASES energy; melting absorbs it.")])

Q("w7b_ke_pe_melting", 2, "7d", "During melting, describe what happens to the kinetic energy and the potential energy of the particles.",
  [P("the average kinetic energy stays the same (temperature constant)", ["kinetic energy stays the same", "kinetic energy does not change", "kinetic energy is constant", "same kinetic energy", "temperature constant"]),
   P("the potential energy increases (particles move further apart, forces overcome)", ["potential energy increases", "more potential energy", "potential energy rises", "gain potential energy"])],
  "During melting the temperature is constant, so the average kinetic energy of the particles stays the same. The energy supplied overcomes the forces holding the particles in fixed positions, so their potential energy increases.",
  ["What happens to the temperature during melting?", "So what happens to the average kinetic energy?", "Where does the energy supplied go?"],
  "KE constant; PE increases",
  ["The kinetic energy stays the same and the potential energy increases", "temperature constant so kinetic energy does not change; potential energy rises"],
  ["Both increase", "Kinetic energy increases and potential energy stays the same"], min_points=2,
  pitfalls=[PF(["kinetic energy increases", "potential energy stays the same", "both increase"], "During melting the temperature is constant: the kinetic energy stays the same and the potential energy increases.")])

Q("w7b_sloping_sections", 2, "7c", "Fig. 1 shows a heating curve. Explain what is happening to the particles during a sloping (rising) section of the graph.",
  [P("the temperature is rising", ["temperature is rising", "temperature increases", "getting hotter", "temperature rises", "temperature goes up"]),
   P("so the average kinetic energy of the particles is increasing (they move faster)", ["kinetic energy increases", "kinetic energy is increasing", "move faster", "speed up", "more kinetic energy"])],
  "During a sloping section the temperature is rising, so the energy supplied increases the average kinetic energy of the particles: they move (or vibrate) faster.",
  ["What is the temperature doing in a sloping section?", "What does that mean for the particles?", "Explain."],
  "temperature rising → average KE increasing",
  ["The temperature is rising, so the particles' average kinetic energy increases and they move faster", "the particles speed up because the temperature goes up"],
  ["The substance is changing state", "The particles are getting bigger"], min_points=2, pitfalls=[BIGGER],
  figure=lambda: figs.graph([(0, 20), (4, 60), (10, 60), (14, 100)], 14, 120, 2, 20, xlabel="time / min", ylabel="temperature / °C"))

Q("w7b_liquid_not_compressible", 2, "7b", "Explain why a liquid is very difficult to compress.",
  [P("liquid particles are close together (touching)", ["close together", "closely packed", "touching", "no space", "little space", "no gaps"]),
   P("so there is no space to push them closer", ["no room", "cannot be pushed closer", "no space", "nowhere to go"])],
  "Although liquid particles can move, they are still close together and touching, so there is almost no space to push them closer, which makes a liquid very hard to compress.",
  ["Can liquid particles move? Are they far apart?", "What would compressing need?", "Explain."],
  "particles close together; no space",
  ["The particles are close together with no space between them", "liquid particles are touching so they cannot be pushed closer"],
  ["Liquids are easily compressed", "The particles are far apart"], min_points=1)

Q("w7b_heating_internal_energy", 2, "7d", "State what happens to the internal energy of a block of metal when it is heated, and explain in terms of its particles.",
  [P("the internal energy increases", ["internal energy increases", "more internal energy", "internal energy rises", "increases"]),
   P("its particles vibrate faster (more kinetic energy), and (slightly) further apart", ["vibrate faster", "more kinetic energy", "kinetic energy increases", "move faster", "further apart"])],
  "The internal energy of the block increases. Its particles gain kinetic energy and vibrate faster (and move slightly further apart, so their potential energy also increases slightly).",
  ["What is internal energy made of?", "What happens to the particles when the block is heated?", "Explain."],
  "internal energy increases; particles vibrate faster",
  ["The internal energy increases because the particles vibrate faster with more kinetic energy", "it increases: the particles gain kinetic energy"],
  ["The internal energy decreases", "The particles get bigger"], min_points=2, pitfalls=[BIGGER])

# ---------------------------------------------------------------- L3
Q("w7b_steam_burn", 3, "7e", "A scald from steam at 100 °C is much worse than one from water at 100 °C. Explain why.",
  [P("steam condenses on the skin", ["condenses", "condensation", "turns into water", "becomes water"]),
   P("condensing releases a lot of energy (the energy that was needed to boil it)", ["releases energy", "gives out energy", "releases a lot of energy", "extra energy", "latent"]),
   P("this extra energy is transferred to the skin, on top of the energy from the hot water", ["to the skin", "extra energy", "more energy", "in addition", "as well as"])],
  "Steam at 100 °C first condenses on the skin. Condensing releases a large amount of energy, the energy that was needed to turn the water into steam, and this is transferred to the skin in addition to the energy given out as the resulting hot water cools. So steam transfers much more energy to the skin.",
  ["What happens to steam when it touches cooler skin?", "Does condensing release or absorb energy?", "Compare the total energy transferred."],
  "steam condenses, releasing extra energy to the skin",
  ["The steam condenses on the skin and releases a lot of extra energy, so more energy is transferred to the skin", "condensation gives out energy as well as the energy from the hot water"],
  ["Steam is hotter than 100 °C", "Water at 100 °C is not hot"], min_points=2)

Q("w7b_gas_pressure_cause", 3, "7b", "Explain, using the particle model, how a gas in a container exerts pressure on the walls.",
  [P("gas particles move randomly at high speed", ["move randomly", "moving quickly", "high speed", "random motion", "constantly moving"]),
   P("they collide with (hit) the walls", ["collide with the walls", "hit the walls", "bounce off the walls", "collisions with the walls", "strike the walls"]),
   P("each collision exerts a force; force per unit area is the pressure", ["force", "force per unit area", "pressure", "push on the walls"])],
  "Gas particles move randomly at high speed and continually collide with the walls of the container. Each collision exerts a small force on the wall; the total force per unit area is the gas pressure.",
  ["How do gas particles move?", "What happens when they reach the walls?", "What does that produce?"],
  "particles hit walls; force per unit area",
  ["The particles move quickly and collide with the walls, exerting a force; force per unit area is pressure", "gas particles hit the walls of the container, pushing on them"],
  ["The gas is heavy and presses down", "Gas particles stick to the walls"], min_points=2)

Q("w7b_ice_cools_drink", 3, "7e", "Explain why ice at 0 °C cools a drink much more than the same mass of cold water at 0 °C.",
  [P("the ice must first melt, absorbing energy from the drink", ["melt", "melting", "absorbs energy", "takes energy"]),
   P("melting needs a lot of energy without any rise in temperature", ["a lot of energy", "large amount of energy", "without a rise in temperature", "temperature stays at 0", "extra energy"]),
   P("so more energy is removed from the drink, cooling it more", ["more energy", "removes more energy", "cools it more", "from the drink"])],
  "Ice must melt before it can warm up, and melting absorbs a large amount of energy from the drink while the ice stays at 0 °C. Cold water at 0 °C cannot absorb this extra energy, so the ice removes much more energy from the drink and cools it more.",
  ["What must happen to ice before it can warm up?", "Does melting absorb or release energy?", "Compare with cold water."],
  "melting absorbs much energy → more cooling",
  ["The ice has to melt, which absorbs a lot of energy from the drink at 0 °C, so it removes more energy than cold water", "melting takes extra energy from the drink"],
  ["Ice is colder than 0 °C water", "Water cannot cool a drink"], min_points=2)

Q("w7b_compare_two_temps", 3, "7c", "Compare the motion of the particles in a cup of water at 20 °C and a cup of water at 60 °C.",
  [P("particles at 60 °C move faster on average", ["move faster", "faster at 60", "60 °c move faster", "higher speed", "more quickly"]),
   P("because they have a greater average kinetic energy", ["greater average kinetic energy", "more kinetic energy", "higher kinetic energy", "average kinetic energy"])],
  "The particles in the water at 60 °C move faster on average than those at 20 °C, because a higher temperature means a greater average kinetic energy of the particles.",
  ["What does a higher temperature mean for the particles?", "Compare their speeds.", "Explain."],
  "60 °C: faster, greater average KE",
  ["The particles at 60 °C move faster because they have more average kinetic energy", "higher temperature, so the particles have greater kinetic energy and move faster"],
  ["The particles at 60 °C are bigger", "The particles at 20 °C move faster"], min_points=2, pitfalls=[BIGGER])

Q("w7b_turn_up_heat_boil", 3, "7e", "A pan of water is boiling. Explain why turning up the heat does not make the water hotter, but makes it boil away faster.",
  [P("the temperature stays at the boiling point (100 °C) while boiling", ["stays at 100", "boiling point", "temperature stays", "constant temperature", "does not rise"]),
   P("the extra energy is used to change more water into steam per second (overcome forces)", ["more water into steam", "boils away faster", "more steam", "faster", "overcome the forces", "separate the particles"])],
  "While the water is boiling its temperature stays at its boiling point, 100 °C. Turning up the heat supplies more energy per second, which is used to overcome the attractive forces and turn more water into steam each second, so it boils away faster without getting hotter.",
  ["What happens to the temperature during boiling?", "Where does the extra energy go?", "Explain."],
  "temperature fixed at boiling point; extra energy → more steam per second",
  ["The temperature stays at 100 °C; the extra energy turns more water into steam each second, so it boils away faster", "it stays at the boiling point, and more energy just separates more particles"],
  ["Turning up the heat makes the water hotter than 100 °C", "The water stops boiling"], min_points=2)

Q("w7b_window_condensation", 3, "7e", "On a cold morning, water droplets form on the inside of a window. Explain this using the particle model.",
  [P("water vapour particles in the air hit the cold glass and lose energy (slow down)", ["lose energy", "slow down", "cooled", "lose kinetic energy", "cold glass"]),
   P("attractive forces pull them close together, forming liquid water (condensation)", ["attractive forces", "pulled together", "closer together", "condense", "condensation", "become liquid"])],
  "Water vapour particles in the warm air hit the cold glass and transfer energy to it, so they slow down. The attractive forces between them can then pull them close together, forming liquid water droplets: the vapour condenses.",
  ["What happens to fast-moving vapour particles when they hit cold glass?", "What can the attractive forces then do?", "Name the change."],
  "vapour cooled by glass → particles slow → pulled together → condenses",
  ["The water vapour particles lose energy on the cold glass and slow down, so the attractive forces pull them together into liquid; it condenses", "the vapour is cooled and condenses into water"],
  ["The glass is leaking", "The window is melting"], min_points=2)

Q("w7b_compressed_cylinder", 3, "7b", "Explain why a large amount of gas can be stored in a small steel cylinder, but the same is not possible for a liquid.",
  [P("gas particles are far apart, so they can be pushed much closer together (compressed)", ["far apart", "compressed", "pushed closer", "squeezed", "large spaces"]),
   P("liquid particles are already close together, so a liquid cannot be compressed", ["liquid particles are close", "already close", "cannot be compressed", "no space", "touching"])],
  "Gas particles are far apart with large spaces between them, so a gas can be compressed: pushed into a much smaller volume. Liquid particles are already close together and touching, so a liquid cannot be compressed in the same way.",
  ["How far apart are gas particles?", "And liquid particles?", "Link to compression."],
  "gas compressible (far apart); liquid not (close)",
  ["Gas particles are far apart so they can be compressed into the cylinder, but liquid particles are already close together", "a gas can be squeezed because of the large spaces; a liquid has no space"],
  ["Gases are lighter so more fit", "Liquids leak out"], min_points=2)

Q("w7b_potential_energy_meaning", 3, "7d", "The internal energy of a body includes the potential energy of its particles. Explain what this potential energy is linked to.",
  [P("the positions of the particles relative to each other (their separation)", ["separation", "distance apart", "how far apart", "positions", "spacing"]),
   P("and the attractive forces between them", ["attractive forces", "forces between", "forces"]),
   P("the further apart the particles (e.g. in a gas), the greater the potential energy", ["further apart", "gas has more", "greater potential energy", "more potential energy"])],
  "The potential energy of the particles depends on their separation and the attractive forces between them. Pulling particles further apart against these forces increases their potential energy, so particles in a gas have more potential energy than in a liquid or solid.",
  ["What do particles exert on each other?", "What happens to the potential energy when they are pulled apart?", "Explain."],
  "PE linked to separation and attractive forces",
  ["It is linked to the separation of the particles and the attractive forces between them; further apart means more potential energy", "the potential energy depends on how far apart the particles are, against the attractive forces"],
  ["It is the energy of the particles' movement", "It depends only on temperature"], min_points=2,
  pitfalls=[PF(["energy of the particles movement", "energy of motion", "depends only on temperature"], "The energy of motion is KINETIC energy; potential energy depends on separation and forces.")])

Q("w7b_candle_wax", 3, "7e", "Wax near a candle flame melts. Explain this using the particle model.",
  [P("the wax particles gain energy from the flame", ["gain energy", "absorb energy", "energy from the flame", "heated"]),
   P("they vibrate more and overcome the forces holding them in fixed positions", ["overcome the forces", "vibrate more", "break free", "leave fixed positions", "overcome the attractive forces"]),
   P("so they can slide past each other: the wax becomes liquid", ["slide past", "move past", "becomes liquid", "flow", "liquid"])],
  "Wax particles near the flame gain energy and vibrate more strongly, until they overcome the attractive forces holding them in fixed positions. The particles can then slide past each other, so the wax becomes a liquid.",
  ["Where do the wax particles get energy from?", "What holds the particles in place in a solid?", "What happens when that is overcome?"],
  "gain energy → overcome forces → slide past (liquid)",
  ["The wax particles gain energy from the flame, vibrate more and overcome the forces holding them, so they slide past each other and the wax becomes liquid", "they absorb energy and break free of fixed positions"],
  ["The flame makes the wax particles smaller", "The wax burns away"], min_points=2, pitfalls=[BIGGER])

Q("w7b_balloon_freezer", 3, "7c", "A balloon is put into a freezer and shrinks. Explain why, using the particle model.",
  [P("the gas particles lose kinetic energy and move more slowly", ["lose kinetic energy", "move more slowly", "slower", "less kinetic energy", "slow down", "slows the particles", "particles slow"]),
   P("they hit the inside of the balloon less often and with less force", ["less often", "less force", "fewer collisions", "weaker collisions", "less pressure"]),
   P("so the pressure inside falls and the balloon is squeezed smaller", ["pressure falls", "lower pressure", "pressure decreases", "shrinks", "smaller"])],
  "In the freezer the gas particles lose kinetic energy and move more slowly, so they hit the inside of the balloon less often and with less force. The pressure inside falls, so the balloon is pushed into a smaller volume.",
  ["What happens to the particles' speed when cooled?", "How does that affect their collisions with the balloon?", "Link this to the balloon's size."],
  "particles slower → fewer, weaker collisions → lower pressure → shrinks",
  ["The particles move more slowly, so they hit the balloon less often and with less force; the pressure falls and it shrinks", "cooling slows the particles, lowering the pressure"],
  ["The particles get smaller", "The air leaks out"], min_points=2, pitfalls=[BIGGER])

# ---------------------------------------------------------------- L4
Q("w7b_water_vs_ice_0c", 4, "7d", "Compare the internal energy of 1 kg of ice at 0 °C with 1 kg of water at 0 °C, and explain.",
  [P("the water has more internal energy", ["water has more", "more internal energy", "water has greater"]),
   P("both are at the same temperature, so the particles have the same average kinetic energy", ["same temperature", "same kinetic energy", "same average kinetic"]),
   P("energy was absorbed during melting, increasing the particles' potential energy", ["potential energy", "melting absorbs", "energy was absorbed", "extra energy", "absorbed energy to melt"])],
  "The water has more internal energy. Both are at 0 °C, so their particles have the same average kinetic energy, but energy had to be absorbed to melt the ice, which increased the potential energy of the particles in the water.",
  ["Compare the temperatures, and so the average kinetic energies.", "What had to happen to turn the ice into water?", "Which has more potential energy?"],
  "water more: same KE, more PE (energy absorbed on melting)",
  ["The water has more internal energy because energy was absorbed to melt it, increasing the potential energy, while the kinetic energy is the same", "same temperature so same kinetic energy, but the water's particles have more potential energy"],
  ["They have the same internal energy because they are at the same temperature", "The ice has more internal energy"], min_points=2,
  pitfalls=[PF(["same internal energy", "ice has more"], "At the same temperature, the WATER has more internal energy because melting added potential energy.")])

Q("w7b_density_order", 4, "7b", "Use the particle model to explain why most substances are densest as a solid, slightly less dense as a liquid and least dense as a gas.",
  [P("solid particles are closely packed in a regular arrangement (most particles per volume)", ["closely packed", "regular", "most particles", "tightly packed"]),
   P("liquid particles are close but a little more spread out / randomly arranged", ["slightly further", "a little more spread", "random", "slightly less", "close but"]),
   P("gas particles are far apart, so there is much less mass per unit volume", ["far apart", "much less mass", "large spaces", "least mass per"])],
  "In a solid the particles are closely packed in a regular pattern, so a given volume contains the most particles and the most mass. In a liquid they are still close but randomly arranged and slightly more spread out, so the density is a little lower. In a gas they are far apart, so a given volume contains far less mass, giving a much lower density.",
  ["How closely packed are the particles in each state?", "How does that affect the mass in a fixed volume?", "Put the states in order."],
  "solid: packed; liquid: close, random; gas: far apart → density order",
  ["Solid particles are closely packed so it is densest; liquid particles are slightly more spread out; gas particles are far apart so the gas has much less mass per volume", "gas particles are far apart, giving the lowest density, while solid particles are tightly packed"],
  ["Gas particles are smaller", "Solids are colder so they are denser"], min_points=2)

Q("w7b_two_plateaus", 4, "7e", "A heating curve for water shows two flat sections. Explain what each represents and why the boiling section is much longer than the melting section.",
  [P("the first flat section is melting (at 0 °C), the second is boiling (at 100 °C)", ["melting", "boiling", "0 °c", "100 °c"]),
   P("during each, energy is absorbed without a rise in temperature (overcoming forces)", ["without a rise", "temperature constant", "no change in temperature", "overcome the forces", "potential energy"]),
   P("boiling takes longer because much more energy is needed to separate the particles completely into a gas", ["more energy", "separate completely", "far apart", "much more energy", "pull them far apart"])],
  "The first flat section is melting at 0 °C and the second is boiling at 100 °C. In each, energy is absorbed to overcome the forces between particles, so the temperature does not rise. Boiling takes much longer because far more energy is needed to separate the particles completely into a gas than to loosen them from fixed positions when melting.",
  ["Which changes of state happen at the two flat sections?", "What is the energy used for in each?", "Why might one need more energy?"],
  "melting and boiling; constant temperature; boiling needs more energy",
  ["The flat parts are melting and boiling, where energy overcomes forces without a temperature rise; boiling needs much more energy to separate the particles completely", "melting at 0 °C and boiling at 100 °C; boiling is longer because more energy is needed"],
  ["Both flat parts are where the heater was switched off", "The water gets hotter in the flat parts"], min_points=2)

Q("w7b_sealed_can_pressure", 4, "7b", "A sealed can containing air is heated. Explain, using the particle model, why the pressure inside rises.",
  [P("the air particles gain kinetic energy and move faster", ["move faster", "more kinetic energy", "gain kinetic energy", "speed up"]),
   P("they collide with the walls more often", ["more often", "more frequently", "more collisions"]),
   P("and with greater force, so the pressure (force per unit area) increases", ["greater force", "harder", "more force", "pressure increases"])],
  "Heating the air gives its particles more kinetic energy, so they move faster. They collide with the walls of the can more often and with greater force, so the force per unit area, the pressure, increases. The volume cannot change because the can is sealed.",
  ["What happens to the particles' speed?", "How does that change their collisions with the walls?", "Link to pressure."],
  "faster particles → more frequent, harder collisions → higher pressure",
  ["The particles move faster and hit the walls more often and with greater force, so the pressure increases", "more kinetic energy means more frequent and harder collisions with the can"],
  ["The particles get bigger and press on the walls", "More air enters the can"], min_points=2, pitfalls=[BIGGER])

Q("w7b_steam_to_ice", 4, "7e", "Steam is cooled until it becomes ice. Describe how the arrangement and motion of the particles change at each stage.",
  [P("gas: far apart, moving fast and randomly; on cooling they slow down and condense into a liquid", ["far apart", "condense", "liquid", "slow down"]),
   P("liquid: close together, sliding past each other; on further cooling they slow more", ["close together", "slide past", "liquid"]),
   P("on freezing they settle into fixed positions in a regular pattern, vibrating", ["fixed positions", "regular pattern", "vibrate", "solid", "freeze"])],
  "In steam, the particles are far apart and move quickly and randomly. As it cools, they slow down until attractive forces pull them together and the steam condenses into a liquid, where the particles are close together but slide past each other. Further cooling slows them more until they freeze into fixed positions in a regular pattern, where they only vibrate.",
  ["Start with the particles in steam.", "What happens when it condenses?", "And when it freezes?"],
  "gas (far, fast) → liquid (close, sliding) → solid (fixed, vibrating)",
  ["In steam they are far apart and fast; they condense into a liquid where they are close together and slide past each other, then freeze into fixed positions where they vibrate", "far apart and moving fast, then close together and sliding, then a regular pattern vibrating in fixed positions"],
  ["The particles shrink until they become ice", "The particles stop moving in steam"], min_points=2, pitfalls=[BIGGER])

Q("w7b_double_mass_ie", 4, "7d", "Block A and block B are made of the same metal and are at the same temperature, but B has twice the mass of A. Compare their internal energies.",
  [P("B has (about) twice the internal energy of A", ["twice", "double", "b has more", "two times"]),
   P("same temperature means the same average kinetic energy per particle", ["same average kinetic energy", "same temperature", "same kinetic energy per particle"]),
   P("but B has twice as many particles, so its total energy is twice as large", ["twice as many particles", "more particles", "total energy", "double the number"])],
  "Both are at the same temperature, so their particles have the same average kinetic energy. But B has twice the mass, so it has twice as many particles. Internal energy is the total energy of all the particles, so B has about twice the internal energy of A.",
  ["What does the same temperature tell you about each particle?", "How many particles does each block have?", "Internal energy is a total."],
  "same average KE; twice the particles → twice the internal energy",
  ["B has twice the internal energy, because it has twice as many particles at the same average kinetic energy", "same temperature, but B has double the particles, so double the total energy"],
  ["They have the same internal energy because they are at the same temperature", "A has more internal energy"], min_points=2,
  pitfalls=[PF(["same internal energy"], "Internal energy is a TOTAL over all particles, so it depends on mass too.")])

Q("w7b_freezer_food", 4, "7c", "Food in a freezer is at −18 °C. A student says its particles have stopped moving. Explain what is really happening to the particles.",
  [P("the particles are still moving (vibrating)", ["still moving", "still move", "still vibrate", "vibrating", "still vibrating", "not stopped"]),
   P("but with less kinetic energy (more slowly) than at room temperature", ["less kinetic energy", "more slowly", "slower", "lower kinetic energy"])],
  "The particles have not stopped moving: they are still vibrating. At −18 °C they simply have less kinetic energy and move more slowly than at room temperature.",
  ["Do particles ever stop moving at ordinary temperatures?", "What does a low temperature mean for them?", "Explain."],
  "still vibrating, but slower (less KE)",
  ["They are still vibrating, just more slowly with less kinetic energy", "the particles still move but have lower kinetic energy"],
  ["The particles have stopped moving", "The particles have shrunk"], min_points=2, pitfalls=[STOP, BIGGER])

Q("w7b_kettle_lid", 4, "7e", "When water boils in a kettle, droplets form on the inside of the lid. Explain the two changes of state involved.",
  [P("boiling: water particles gain enough energy to escape as steam (gas)", ["boiling", "steam", "gas", "escape", "evaporate"]),
   P("condensation: the steam hits the cooler lid, loses energy and turns back into liquid water", ["condense", "condensation", "cooler lid", "loses energy", "back into liquid", "turns back into water"])],
  "First, boiling: water particles gain enough energy to overcome the attractive forces and escape as steam. Then condensation: the steam particles hit the cooler lid, transfer energy to it and slow down, so attractive forces pull them together into liquid droplets.",
  ["What change of state produces the steam?", "What happens when steam meets the cooler lid?", "Name and explain both."],
  "boiling (water → steam); condensation (steam → water on cool lid)",
  ["Boiling turns water into steam, and the steam condenses back into water when it hits the cooler lid", "the water boils to a gas, then the gas loses energy on the lid and condenses"],
  ["The lid is melting", "Water seeps through the kettle"], min_points=2)

Q("w7b_brownian_motion", 4, "7b", "Through a microscope, smoke particles in air are seen moving in a jerky, random way. Explain what causes this and what it shows.",
  [P("the smoke particles are hit by fast-moving (invisible) air molecules", ["hit by air molecules", "air particles", "bombarded", "collide with air molecules", "struck by", "air molecules hit"]),
   P("the collisions are uneven/random, so the smoke particles move randomly", ["uneven", "random", "unequal", "more on one side", "different directions"]),
   P("this is evidence that air particles are constantly moving randomly", ["evidence", "shows that", "air particles are moving", "constantly moving", "random motion"])],
  "The smoke particles are being hit by fast-moving air molecules, which are too small to see. At any moment more molecules hit one side than the other, so the smoke particles are pushed in random directions. This jerky random motion is evidence that air particles are constantly moving at random.",
  ["What could be hitting the smoke particles?", "Why would the motion be random?", "What does it show about air?"],
  "air molecules hit smoke unevenly → random motion → evidence of moving particles",
  ["Fast-moving air molecules hit the smoke particles unevenly, making them move randomly; this shows air particles are always moving", "the smoke is bombarded by air particles from different directions, which is evidence that the particles are moving"],
  ["The smoke particles are alive", "Wind blows the smoke"], min_points=2)

Q("w7b_temp_vs_ie", 4, "7d", "Explain the difference between the temperature of a body and its internal energy.",
  [P("temperature is linked to the average kinetic energy of the particles", ["average kinetic energy", "average"]),
   P("internal energy is the total kinetic and potential energy of all the particles", ["total", "all the particles", "kinetic and potential", "sum of"]),
   P("so internal energy also depends on the amount (mass) and state of the substance", ["mass", "number of particles", "amount", "state", "how much"])],
  "Temperature is a measure of the average kinetic energy of the particles. Internal energy is the total kinetic and potential energy of all the particles, so it also depends on how much substance there is (its mass) and its state. A bath of warm water can have more internal energy than a cup of hot water.",
  ["Which quantity is an average?", "Which quantity is a total?", "What else does the total depend on?"],
  "temperature = average KE; internal energy = total KE + PE (depends on mass)",
  ["Temperature depends on the average kinetic energy, while internal energy is the total kinetic and potential energy of all the particles, so it depends on mass", "internal energy is a total and temperature is an average"],
  ["They are the same thing", "Temperature is the total energy"], min_points=2)

# ---------------------------------------------------------------- L5
Q("w7b_particles_expand_claim", 5, "7b", "A student says: 'When a metal is heated it expands because its particles get bigger.' Evaluate this claim.",
  [P("wrong: the particles themselves do not change size", ["wrong", "do not change size", "same size", "not bigger", "incorrect"]),
   P("they vibrate more (more kinetic energy)", ["vibrate more", "vibrate faster", "more kinetic energy", "move more"]),
   P("so they push each other slightly further apart, and the metal expands", ["further apart", "more space", "spacing increases", "take up more room"])],
  "The claim is wrong. The particles do not get bigger. When the metal is heated, its particles gain kinetic energy and vibrate more strongly, so they push each other slightly further apart; the increased spacing makes the metal expand.",
  ["Can particles change size?", "What happens to their motion when heated?", "What causes the expansion?"],
  "wrong; particles vibrate more → further apart",
  ["Wrong: the particles stay the same size but vibrate more, so they move further apart and the metal expands", "the particles do not get bigger; they vibrate faster and take up more room"],
  ["Correct, the particles grow when heated", "Correct, heat makes particles expand"], min_points=2, pitfalls=[BIGGER])

Q("w7b_ice_particles_stop_claim", 5, "7b", "A student says: 'In a block of ice the water particles are completely still.' Evaluate this claim and describe the particles' motion.",
  [P("wrong: the particles are still moving", ["wrong", "still moving", "not still", "incorrect"]),
   P("they vibrate about fixed positions", ["vibrate", "vibrating", "fixed positions"]),
   P("they have kinetic energy because the ice has a temperature above absolute zero", ["kinetic energy", "temperature", "above absolute zero", "have energy"])],
  "The claim is wrong. The particles in ice are not still: they vibrate about fixed positions. Ice has a temperature (well above absolute zero), so its particles have kinetic energy; they just cannot move from place to place.",
  ["Do particles in a solid move at all?", "How do they move?", "Why must they have kinetic energy?"],
  "wrong; vibrate about fixed positions; have KE",
  ["Wrong: the particles vibrate about fixed positions because they still have kinetic energy", "they are not still; they vibrate in place"],
  ["Correct, particles in solids do not move", "Correct, ice is frozen so nothing moves"], min_points=2, pitfalls=[STOP])

Q("w7b_cooling_curve_design", 5, "7e", "Describe how to obtain a cooling curve for molten wax and how to find its freezing point from it.",
  [P("heat the wax until molten, then let it cool, with a thermometer in it", ["thermometer", "let it cool", "molten", "heat the wax", "cool"]),
   P("record the temperature at regular intervals (e.g. every 30 s) and plot temperature against time", ["regular intervals", "every 30 s", "every minute", "plot", "temperature against time", "record the temperature"]),
   P("the freezing point is the temperature of the flat section of the graph", ["flat section", "flat part", "constant temperature", "plateau", "horizontal part"])],
  "Heat a tube of wax in a water bath until it is molten, put a thermometer in it and let it cool. Record the temperature at regular intervals, for example every 30 s, and plot temperature against time. The freezing point is the temperature of the flat section of the graph, where the temperature stays constant while the wax solidifies.",
  ["What do you measure, and how often?", "What graph do you plot?", "Which part of the graph shows the freezing point?"],
  "cool molten wax; temperature at regular intervals; flat section = freezing point",
  ["Let the molten wax cool with a thermometer in it, record the temperature every 30 s, plot a graph, and the freezing point is the flat section", "record temperature against time as it cools; the plateau gives the freezing point"],
  ["Weigh the wax as it cools", "The freezing point is the highest temperature"], min_points=2)

Q("w7b_hotter_boil_claim", 5, "7e", "A student says: 'If I turn the cooker up to maximum, the water will boil at a higher temperature and cook the pasta faster.' Evaluate this claim.",
  [P("wrong: water boils at a fixed temperature (100 °C at normal pressure)", ["wrong", "fixed temperature", "100", "boiling point is fixed", "stays at 100", "same temperature"]),
   P("extra energy just turns water into steam faster; it does not raise the temperature", ["boils away faster", "more steam", "faster", "does not raise", "does not get hotter"]),
   P("so the pasta does not cook faster once the water is boiling", ["not cook faster", "same time", "no faster"])],
  "The claim is wrong. Once water is boiling, its temperature stays at its boiling point, 100 °C at normal pressure. Turning the cooker up only supplies energy faster, which turns more water into steam each second; it does not raise the temperature, so the pasta does not cook any faster.",
  ["What happens to the temperature of boiling water?", "Where does extra energy go?", "Does the pasta cook faster?"],
  "wrong; boiling point fixed; extra energy → more steam",
  ["Wrong: water boils at 100 °C whatever the heat; more heat just makes it boil away faster, so the pasta does not cook faster", "the temperature stays at 100 °C, so turning it up only produces more steam"],
  ["Correct, more heat means hotter water", "Correct, the pasta cooks twice as fast"], min_points=2)

Q("w7b_ie_stages_ice_to_steam", 5, "7d", "Ice at −10 °C is heated steadily until it becomes steam at 110 °C. Describe how the kinetic and potential energies of the particles change during the different stages.",
  [P("when the temperature rises (in solid, liquid or gas), the average kinetic energy increases", ["kinetic energy increases", "kinetic energy goes up", "temperature rises", "move faster", "vibrate faster"]),
   P("during melting and boiling, the potential energy increases while the kinetic energy stays the same", ["potential energy increases", "potential energy goes up", "kinetic energy stays the same", "constant temperature"]),
   P("boiling causes the largest increase in potential energy (particles separated far apart)", ["largest increase", "boiling", "far apart", "most potential energy", "separated"])],
  "Whenever the temperature is rising (heating the ice from −10 °C to 0 °C, the water from 0 °C to 100 °C, and the steam from 100 °C to 110 °C), the average kinetic energy of the particles increases. During melting and boiling the temperature is constant, so the kinetic energy stays the same while the potential energy increases as the particles are separated. Boiling gives the largest increase in potential energy, because the particles are pulled far apart.",
  ["What happens to the kinetic energy when the temperature rises?", "What happens during the changes of state?", "Which change of state increases potential energy most?"],
  "temperature rising → KE up; changes of state → PE up (boiling most)",
  ["When the temperature rises the kinetic energy increases; during melting and boiling the potential energy increases while the kinetic energy stays the same, with boiling giving the biggest increase", "kinetic energy goes up while heating; potential energy goes up during melting and boiling"],
  ["The kinetic energy increases all the time, including during melting", "The particles get bigger at each stage"], min_points=2,
  pitfalls=[BIGGER, PF(["increases all the time", "including during melting"], "During melting and boiling the temperature is constant, so the average kinetic energy does NOT increase.")])

Q("w7b_brownian_evidence", 5, "7b", "Explain how the random motion of pollen grains in water (Brownian motion) supports the kinetic particle model.",
  [P("the pollen grains are hit by water molecules that are too small to see", ["water molecules", "too small to see", "invisible", "bombarded", "hit by"]),
   P("the collisions are unequal on different sides at each moment, so the grains move randomly", ["unequal", "random", "more on one side", "uneven", "different sides"]),
   P("so the water molecules must be constantly moving randomly, as the model says", ["constantly moving", "always moving", "moving randomly", "supports the model", "evidence"])],
  "The pollen grains are continually hit by water molecules that are far too small to see. At each instant the hits on different sides are unequal, so the grains are pushed in random directions. The only explanation is that the water molecules themselves are constantly moving randomly, which is exactly what the kinetic particle model states.",
  ["What could make the pollen move?", "Why is the motion random?", "What does this tell us about the water molecules?"],
  "invisible molecules hit grains unevenly → random motion → molecules always moving",
  ["Invisible water molecules hit the pollen unevenly, making it move randomly, which is evidence that the molecules are constantly moving", "the random jiggling shows the water particles are always moving, supporting the model"],
  ["The pollen is swimming", "Currents in the water push the pollen"], min_points=2)

Q("w7b_gas_no_mass_claim", 5, "7b", "A student says: 'Gases have no mass because they are invisible and you can't feel them.' Evaluate this claim and suggest how to test it.",
  [P("wrong: gases are made of particles, which have mass", ["wrong", "made of particles", "particles have mass", "have mass", "incorrect"]),
   P("they seem weightless because the particles are far apart, so the density is low", ["far apart", "low density", "very light", "small mass per volume"]),
   P("test: weigh a container/ball, pump in more air (or remove air), and weigh again; the mass changes", ["weigh", "pump in air", "balance", "mass increases", "remove the air", "vacuum pump"])],
  "The claim is wrong. Gases are made of particles, and particles have mass; gases only seem weightless because their particles are far apart, giving them a very low density. To test it, weigh a ball or sealed container on a sensitive balance, pump more air into it, and weigh it again: its mass increases.",
  ["What are gases made of?", "Why do gases seem to have no mass?", "How could you show they have mass?"],
  "wrong; particles have mass; low density; weigh before and after adding air",
  ["Wrong: gas particles have mass, but they are far apart so the density is low; weigh a ball, pump in more air and weigh again", "gases have mass; you can show it by weighing a container before and after pumping in air"],
  ["Correct, gases weigh nothing", "Correct, air has no particles"], min_points=2)

Q("w7b_water_steam_density_claim", 5, "7b", "A student says: 'Liquid water and steam must have the same density because they are the same substance.' Evaluate this claim.",
  [P("wrong", ["wrong", "incorrect", "not true", "not the same"]),
   P("the particles (and their mass) are the same, but in steam they are much further apart", ["further apart", "far apart", "more spread out", "spread out", "large spaces"]),
   P("so steam has far less mass per unit volume: much lower density (about 1000 times less)", ["less mass per unit volume", "lower density", "much less dense", "1000", "less dense"])],
  "The claim is wrong. Water and steam are made of the same particles, but in steam the particles are much further apart. A given volume of steam therefore contains far fewer particles and much less mass, so steam's density is far lower, roughly a thousandth of liquid water's.",
  ["Are the particles the same?", "How does their spacing compare?", "How does that affect mass per unit volume?"],
  "wrong; same particles but far apart in steam → much lower density",
  ["Wrong: the particles are the same but much further apart in steam, so it has far less mass per unit volume and a much lower density", "steam is much less dense because its particles are spread out"],
  ["Correct, the same substance always has the same density", "Steam is denser because it is hotter"], min_points=2)

Q("w7b_heating_curve_more_mass", 5, "7e", "A heating curve is obtained for 100 g of ice using a heater. Predict and explain how the curve would differ for 200 g of ice with the same heater.",
  [P("the flat sections (melting, boiling) would be at the same temperatures (0 °C, 100 °C)", ["same temperatures", "same temperature", "0 °c", "100 °c", "still at"]),
   P("but they would last about twice as long, because twice as many particles need energy to change state", ["twice as long", "longer", "double the time", "twice as many particles", "more energy needed"]),
   P("the rising sections would also be less steep (temperature rises more slowly)", ["less steep", "rises more slowly", "more slowly", "gentler", "slower"])],
  "The flat sections would still be at 0 °C and 100 °C, since melting and boiling points do not depend on the mass. But with twice the mass, twice as much energy is needed, so with the same heater each flat section would last about twice as long, and the rising sections would be less steep because the temperature rises more slowly.",
  ["Do the melting and boiling points depend on mass?", "How much energy is needed for twice the mass?", "What does that do to the time and the slopes?"],
  "same plateau temperatures; plateaus twice as long; slopes less steep",
  ["The flat parts stay at 0 °C and 100 °C but last twice as long, and the sloping parts are less steep because twice the mass needs twice the energy", "same melting and boiling temperatures, but everything takes longer and the temperature rises more slowly"],
  ["The ice would melt at a higher temperature", "The curve would be identical"], min_points=2)

Q("w7b_thermometer_melting_ice", 5, "7e", "A heater is switched on in a beaker of crushed ice and water. A student is surprised that the thermometer stays at 0 °C for several minutes. Evaluate the reading and explain.",
  [P("the reading is correct: the temperature stays at 0 °C while the ice melts", ["correct", "stays at 0", "constant temperature", "melting point"]),
   P("the energy supplied is used to overcome the forces between particles (melting), not to raise the temperature", ["overcome the forces", "used to melt", "melting the ice", "separate the particles", "not raise the temperature"]),
   P("so the particles' potential energy increases while their average kinetic energy stays the same; the temperature rises only after all the ice has melted", ["potential energy increases", "kinetic energy stays", "after all the ice has melted", "once the ice has melted"])],
  "The reading is correct. While ice is melting, the energy from the heater is used to overcome the forces holding the particles in the solid, increasing their potential energy rather than their average kinetic energy. So the temperature stays at 0 °C until all the ice has melted; only then does it start to rise.",
  ["What happens to the temperature of a substance while it changes state?", "Where does the heater's energy go?", "When will the temperature start to rise?"],
  "reading correct; energy melts ice (PE up, KE same); rises after melting complete",
  ["The reading is correct: the energy is used to melt the ice, increasing potential energy, so the temperature stays at 0 °C until all the ice has melted", "it stays at 0 °C because the energy overcomes the forces between particles rather than raising the temperature"],
  ["The thermometer must be broken", "The heater is not working"], min_points=2)
