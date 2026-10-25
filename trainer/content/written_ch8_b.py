"""Chapter 8 Thermal Processes: 50 more written-answer questions (10 per level), marked by keywords/phrases."""
from .. import figs, sketches
from ..marker import Pitfall, Point
from .base import written

P = Point
PF = Pitfall
CH = 8


def Q(id, lv, lo, stem, points, model, hints, keywords, passes, fails, pitfalls=(), min_points=None, figure=None):
    written(id, CH, lv, lo, stem=stem, points=points, model_answer=model, hints=hints, keywords=keywords,
            pitfalls=pitfalls, min_points=min_points, figure=figure, sample_pass=passes, sample_fail=fails)


COLD_FLOWS = PF(["cold flows", "cold moves", "cold gets in", "cold enters", "keeps the cold", "cold travels", "lets cold in", "coldness"],
                "'Cold' does not flow; energy flows from the warmer place to the colder place.")
HEAT_RISES = PF(["heat rises"], "It is the warm FLUID (air or water) that rises because it is less dense; 'heat' itself does not rise.")

# ---------------------------------------------------------------- L1
Q("w8b_name_convection", 1, "8c", "Name the process by which energy is transferred through a liquid or gas by the movement of the fluid itself.",
  [P("convection", ["convection", "convection current"])],
  "This process is convection: warmer fluid rises and cooler fluid sinks, carrying energy with it.",
  ["The fluid itself moves.", "Warm fluid rises, cool fluid sinks.", "Name the process."],
  "convection", ["Convection", "convection currents"], ["Conduction", "Radiation"])

Q("w8b_conductors_insulators", 1, "8b", "Give two examples of good thermal conductors and two examples of thermal insulators.",
  [P("conductors: metals, e.g. copper, aluminium, iron, steel", ["copper", "aluminium", "iron", "steel", "silver", "metal", "gold"]),
   P("insulators: e.g. air, plastic, wood, wool, polystyrene, glass", ["air", "plastic", "wood", "wool", "polystyrene", "glass", "fibreglass", "cork", "rubber"])],
  "Good thermal conductors include metals such as copper and aluminium. Thermal insulators include air, plastic, wood and wool.",
  ["Which materials are used for saucepans?", "Which are used for handles or clothing?", "Give two of each."],
  "metals conduct; air, plastic, wood, wool insulate",
  ["Copper and aluminium conduct well; plastic and wood are insulators", "metals like iron are conductors, while air and wool are insulators"],
  ["Plastic and wood are good conductors", "Air and copper are insulators"], min_points=2,
  pitfalls=[PF(["plastic is a good conductor", "wood is a good conductor", "plastic and wood are good conductors", "air and copper are insulators", "copper is an insulator"], "Metals are good conductors; plastic, wood and air are insulators.")])

Q("w8b_best_emitter", 1, "8d", "State which type of surface is the best emitter and absorber of infrared radiation.",
  [P("a dull (matt) black surface", ["dull black", "matt black", "black", "dark and dull", "dull dark"])],
  "A dull (matt) black surface is the best emitter and the best absorber of infrared radiation.",
  ["Think of what colour gets hottest in sunshine.", "Is it shiny or dull?", "Name the surface."],
  "dull black",
  ["A dull black surface", "matt black"], ["Shiny silver", "White and shiny"],
  pitfalls=[PF(["shiny silver", "shiny white", "white"], "Shiny and light surfaces are POOR emitters and absorbers.")])

Q("w8b_poor_emitter", 1, "8d", "State which type of surface is the worst emitter of infrared radiation, and what it does to radiation that falls on it.",
  [P("a shiny silver (light, polished) surface", ["shiny silver", "shiny", "silver", "polished", "light coloured", "white"]),
   P("it reflects most of the radiation (poor absorber)", ["reflects", "reflector", "poor absorber", "bounces off"])],
  "A shiny silver surface is the worst emitter of infrared radiation. It reflects most of the radiation falling on it, so it is also a poor absorber.",
  ["Think of a vacuum flask's walls.", "What does a mirror-like surface do to radiation?", "State both."],
  "shiny silver; reflects radiation",
  ["A shiny silver surface; it reflects most radiation", "polished silver is the worst emitter and reflects radiation"],
  ["Dull black; it absorbs radiation", "Rough dark surfaces"], min_points=2)

Q("w8b_convection_where", 1, "8c", "State in which states of matter convection can take place, and explain why not in the other.",
  [P("liquids and gases (fluids)", ["liquids and gases", "fluids", "liquid and gas", "gases and liquids"]),
   P("not in solids, because the particles cannot flow / move from place to place", ["not in solids", "solids cannot flow", "particles cannot move", "cannot flow", "fixed positions"])],
  "Convection takes place in liquids and gases (fluids). It cannot happen in solids, because their particles are in fixed positions and the material cannot flow.",
  ["Convection needs the material to move.", "Which states can flow?", "Why can't a solid?"],
  "liquids and gases; not solids (cannot flow)",
  ["Liquids and gases, but not solids because solids cannot flow", "only in fluids; in solids the particles are in fixed positions"],
  ["Solids only", "All three states"], min_points=2)

Q("w8b_conduction_where", 1, "8b", "State in which state of matter conduction is most important, and name the particles' motion that passes energy on.",
  [P("solids (especially metals)", ["solids", "solid", "metals"]),
   P("vibrations of particles (and movement of free electrons in metals)", ["vibration", "vibrate", "free electrons", "electrons"])],
  "Conduction is most important in solids, especially metals. Energy is passed on by the vibrations of particles, and in metals also by the movement of free electrons.",
  ["Particles must be close together for conduction.", "How do they pass energy to their neighbours?", "State both."],
  "solids; vibrations (and free electrons)",
  ["In solids, by vibrating particles and free electrons", "solids, where particles vibrate and pass energy on"],
  ["Gases, by particles rising", "A vacuum, by waves"], min_points=2)

Q("w8b_sun_radiation", 1, "8d", "State how energy from the Sun reaches the Earth, and why it cannot be by conduction or convection.",
  [P("by (infrared/electromagnetic) radiation", ["radiation", "infrared", "electromagnetic waves", "em waves"]),
   P("space is a vacuum with no particles, so conduction and convection cannot happen", ["vacuum", "no particles", "no medium", "nothing in space", "empty space"])],
  "Energy from the Sun reaches the Earth by radiation, mainly infrared and visible electromagnetic waves. Space is a vacuum with no particles, so neither conduction nor convection is possible.",
  ["What is between the Sun and the Earth?", "Which processes need particles?", "Which one does not?"],
  "radiation; space is a vacuum",
  ["By radiation, because space is a vacuum with no particles for conduction or convection", "infrared waves travel through the empty space of the vacuum"],
  ["By convection currents in space", "By conduction through the air"], min_points=2)

Q("w8b_insulator_def", 1, "8b", "State what is meant by a thermal insulator, giving an example.",
  [P("a material that does not conduct energy (heat) well / poor conductor", ["poor conductor", "does not conduct well", "conducts badly", "slows the transfer", "reduces energy transfer"]),
   P("example: plastic, wood, air, wool, polystyrene", ["plastic", "wood", "air", "wool", "polystyrene", "rubber", "cork", "fibreglass"])],
  "A thermal insulator is a poor conductor of heat: it slows down the transfer of energy through it. Examples are plastic, wood, wool and air.",
  ["Insulators are the opposite of good conductors.", "Think of what pan handles are made of.", "Define and give an example."],
  "poor conductor; e.g. plastic, wood, air",
  ["A poor conductor of heat, such as plastic", "a material that conducts badly, like wool or air"],
  ["A good conductor like copper", "Something that gives out heat"], min_points=2)

Q("w8b_hot_to_cold_until", 1, "8a", "A hot drink is left in a room. State the direction of energy transfer and when it stops.",
  [P("from the hot drink to the cooler room/air", ["from the drink", "from the hot drink", "from hot to cold", "to the surroundings", "to the room", "to the air"]),
   P("until the drink and room are at the same temperature (thermal equilibrium)", ["same temperature", "thermal equilibrium", "equal temperature", "room temperature"])],
  "Energy is transferred from the hot drink to the cooler room until the drink and the room are at the same temperature (thermal equilibrium).",
  ["Which is hotter, the drink or the room?", "Energy always flows from hotter to colder.", "When does it stop?"],
  "drink → room until same temperature",
  ["From the hot drink to the room until they are at the same temperature", "energy flows from the drink to the surroundings until thermal equilibrium"],
  ["From the room into the drink", "It never stops"], min_points=2, pitfalls=[COLD_FLOWS])

Q("w8b_hotter_more_radiation", 1, "8d", "State how the temperature of a surface affects the rate at which it emits infrared radiation.",
  [P("a hotter surface emits radiation at a greater rate", ["hotter", "higher temperature", "greater rate", "more radiation", "faster"])],
  "The higher the temperature of a surface, the greater the rate at which it emits infrared radiation.",
  ["Compare a hot iron with a cold one.", "Which radiates more?", "State the relationship."],
  "hotter → more radiation",
  ["A hotter surface emits more radiation", "the higher the temperature, the greater the rate of emission"],
  ["A colder surface emits more", "Temperature has no effect"],
  pitfalls=[PF(["colder surface emits more", "no effect", "cooler emits more"], "A HOTTER surface emits radiation at a greater rate.")])

# ---------------------------------------------------------------- L2
Q("w8b_saucepan", 2, "8e", "A saucepan has a copper base and a plastic handle. Explain the choice of each material.",
  [P("copper base: a good conductor, so energy passes quickly from the cooker to the food", ["copper is a good conductor", "good conductor", "conducts well", "passes energy quickly", "heats the food quickly"]),
   P("plastic handle: a poor conductor (insulator), so it stays cool to hold", ["plastic is an insulator", "insulator", "poor conductor", "stays cool", "does not get hot", "safe to hold"])],
  "Copper is a good conductor, so energy is transferred quickly from the cooker through the base to the food. Plastic is a poor conductor (an insulator), so the handle stays cool enough to hold safely.",
  ["Which part should let energy through?", "Which part should not?", "Match each material to its job."],
  "copper conducts (base); plastic insulates (handle)",
  ["Copper is a good conductor so the food heats quickly, and plastic is an insulator so the handle stays cool", "the base conducts well, the plastic handle does not get hot"],
  ["Copper is used because it is cheap", "Plastic conducts heat to the hand"], min_points=2)

Q("w8b_freezer_top", 2, "8c", "In many old fridges the freezer compartment is at the top. Explain how this cools the whole fridge.",
  [P("air near the freezer is cooled, becomes denser and sinks", ["cooled", "denser", "sinks", "cold air sinks", "more dense"]),
   P("warmer air from below rises to replace it", ["warmer air rises", "warm air rises", "rises to replace", "replaced"]),
   P("setting up a convection current that circulates through the fridge", ["convection current", "convection", "circulates"])],
  "Air next to the freezer at the top is cooled, contracts and becomes denser, so it sinks. Warmer air from lower down rises to take its place and is cooled in turn. This sets up a convection current that circulates and cools the whole fridge.",
  ["What happens to the density of air when it is cooled?", "Does it rise or sink?", "What sets up the circulation?"],
  "cool air sinks, warm air rises → convection current",
  ["Air near the freezer is cooled, becomes denser and sinks, while warmer air rises, making a convection current", "cold dense air sinks and warmer air rises, circulating by convection"],
  ["Cold air rises to the top", "The freezer conducts cold through the walls"], min_points=2, pitfalls=[COLD_FLOWS])

Q("w8b_loft_insulation", 2, "8e", "Explain how a thick layer of fibreglass in a loft reduces energy loss from a house.",
  [P("fibreglass traps air in small pockets", ["traps air", "trapped air", "pockets of air", "air is trapped"]),
   P("air is a poor conductor", ["poor conductor", "insulator", "air does not conduct"]),
   P("and the trapped air cannot move, so convection is reduced", ["cannot move", "cannot circulate", "no convection", "reduces convection", "stops convection"])],
  "Fibreglass traps air in many small pockets. Air is a poor conductor, so little energy is conducted through it, and because the air is trapped it cannot move to carry energy away by convection. So less energy escapes through the roof.",
  ["What does fibreglass trap?", "Is that a good or poor conductor?", "Can the trapped air move?"],
  "traps air; poor conductor; no convection",
  ["It traps air, which is a poor conductor, and the trapped air cannot move, so convection is reduced", "the fibreglass holds pockets of air, an insulator that cannot circulate"],
  ["Fibreglass reflects the heat", "Fibreglass produces cold"], min_points=2)

Q("w8b_white_houses", 2, "8d", "Houses in hot countries are often painted white. Explain why.",
  [P("white surfaces are poor absorbers / good reflectors of radiation", ["poor absorber", "reflect", "reflects", "reflector", "absorb less", "absorbs little"]),
   P("so less energy from the Sun is absorbed and the house stays cooler", ["stays cooler", "keeps cool", "less energy absorbed", "cooler", "absorb less"])],
  "White surfaces are poor absorbers and good reflectors of radiation, so they absorb less of the Sun's radiation. The house therefore stays cooler inside.",
  ["Do white surfaces absorb or reflect radiation?", "What does that do to the energy entering the house?", "Explain."],
  "white reflects radiation → absorbs less → cooler",
  ["White surfaces reflect the Sun's radiation and absorb less, so the house stays cooler", "a white house is a poor absorber, keeping it cool"],
  ["White paint is cheaper", "White surfaces absorb more radiation"], min_points=2,
  pitfalls=[PF(["absorb more radiation", "white absorbs more", "good absorber"], "White surfaces are POOR absorbers.")])

Q("w8b_free_electrons", 2, "8b", "Explain why metals are much better thermal conductors than non-metals.",
  [P("metals have free (delocalised) electrons", ["free electrons", "delocalised electrons", "mobile electrons", "electrons that can move"]),
   P("which move quickly through the metal, carrying energy from hot to cold regions", ["move quickly", "carry energy", "transfer energy", "move through the metal", "quickly"]),
   P("in addition to energy passed on by vibrating atoms", ["vibrating", "vibrations", "as well as"])],
  "Metals contain free electrons that can move through the metal. In the hot region these electrons gain energy and move quickly to colder regions, carrying energy with them. This is much faster than energy passed on only by the vibrations of atoms, which is how non-metals conduct.",
  ["What do metals have that non-metals do not?", "How do these particles transfer energy?", "Compare with vibrations alone."],
  "free electrons carry energy quickly (plus vibrations)",
  ["Metals have free electrons that move quickly and carry energy, as well as vibrating atoms", "free electrons in metals transfer energy much faster than vibrations alone"],
  ["Metals are always hotter", "Non-metals have more electrons"], min_points=2)

Q("w8b_wooden_spoon", 2, "8b", "Explain why a wooden spoon left in a pan of boiling soup stays cool at the handle, while a metal spoon does not.",
  [P("wood is a poor conductor (insulator)", ["wood is a poor conductor", "poor conductor", "insulator", "wood does not conduct"]),
   P("so very little energy is conducted up the wooden handle", ["little energy", "slowly", "very little", "does not reach"]),
   P("the metal spoon is a good conductor and its handle gets hot", ["metal is a good conductor", "good conductor", "metal conducts", "gets hot"])],
  "Wood is a poor conductor (an insulator), so very little energy is conducted from the soup up to the handle, which stays cool. Metal is a good conductor, so energy quickly travels up the metal spoon and its handle becomes hot.",
  ["Which material is a good conductor?", "Which is an insulator?", "Compare the handles."],
  "wood insulator → handle cool; metal conductor → handle hot",
  ["Wood is a poor conductor so little energy reaches the handle, but metal is a good conductor so its handle gets hot", "the wooden spoon is an insulator; the metal spoon conducts"],
  ["Wood absorbs the cold", "The wooden spoon is lighter"], min_points=2, pitfalls=[COLD_FLOWS])

Q("w8b_radiation_space", 2, "8d", "Explain why radiation is the only way energy can be transferred between the Sun and the Earth.",
  [P("space between them is a vacuum (no particles)", ["vacuum", "no particles", "empty space", "no medium"]),
   P("conduction and convection need particles (a medium)", ["need particles", "need a medium", "conduction and convection need", "require particles"]),
   P("radiation (electromagnetic waves) can travel through a vacuum", ["radiation can travel through a vacuum", "electromagnetic waves", "does not need a medium", "travels through a vacuum", "em waves"])],
  "Space between the Sun and the Earth is a vacuum, with no particles. Conduction and convection both need particles, but radiation is electromagnetic waves, which can travel through a vacuum. So radiation is the only possible way.",
  ["What fills the space between the Sun and the Earth?", "Which processes need particles?", "Which does not?"],
  "vacuum; conduction/convection need particles; radiation does not",
  ["Space is a vacuum, so conduction and convection cannot happen; radiation can travel through a vacuum", "there are no particles in space, but electromagnetic waves do not need a medium"],
  ["The Sun is too hot for conduction", "Convection currents carry the heat through space"], min_points=2)

Q("w8b_radiator_fins", 2, "8e", "The back of a fridge has black metal fins. Explain how the fins help the fridge get rid of energy.",
  [P("fins give a large surface area", ["large surface area", "bigger surface area", "more surface", "increase the surface area"]),
   P("black surfaces are good emitters of radiation", ["good emitter", "black", "emit well", "emits radiation"]),
   P("metal is a good conductor, so energy reaches the fins quickly (and air around them convects away)", ["good conductor", "metal conducts", "convection", "air rises"])],
  "The fins give a large surface area, so more energy can be lost to the air. They are black, which is a good emitter of infrared radiation, and made of metal, a good conductor, so energy reaches the surface quickly. Air warmed by the fins also rises, carrying energy away by convection.",
  ["Why so many fins?", "Why black?", "Why metal?"],
  "large area; black emits well; metal conducts",
  ["The fins have a large surface area, are black so they emit radiation well, and are metal so they conduct well", "large surface area and black colour help them lose energy quickly"],
  ["The fins make the fridge colder by letting cold in", "Black fins absorb cold"], min_points=2, pitfalls=[COLD_FLOWS])

Q("w8b_warm_air_rises", 2, "8c", "Explain, in terms of density, why warm air rises.",
  [P("when air is warmed its particles move faster and spread out (it expands)", ["expands", "spreads out", "particles move apart", "volume increases"]),
   P("so the warm air is less dense than the cooler air around it", ["less dense", "lower density", "density decreases"]),
   P("less dense air rises (cooler, denser air sinks)", ["rises", "floats up", "denser air sinks", "cooler air sinks"])],
  "When air is warmed, its particles move faster and spread out, so the air expands. The same mass then takes up more volume, so it is less dense than the cooler air around it, and it rises while the denser cooler air sinks.",
  ["What happens to air when it is warmed?", "How does that change its density?", "What happens to less dense fluid?"],
  "warm air expands → less dense → rises",
  ["Warm air expands, becomes less dense than the cool air around it, and rises", "heating makes the air spread out so its density decreases and it floats up"],
  ["Heat rises", "Warm air is lighter because heat has no mass"], min_points=2, pitfalls=[HEAT_RISES])

Q("w8b_bird_feathers", 2, "8e", "On cold days birds fluff up their feathers. Explain how this keeps them warm.",
  [P("fluffing up traps more air between the feathers", ["traps air", "trapped air", "more air", "pockets of air"]),
   P("air is a poor conductor (and trapped air cannot convect)", ["poor conductor", "insulator", "cannot move", "no convection"]),
   P("so less energy is lost from the bird's body", ["less energy is lost", "reduces energy loss", "keeps energy in", "stays warm", "less heat lost"])],
  "Fluffing up the feathers traps a thicker layer of air. Air is a poor conductor, and because it is trapped it cannot move to carry energy away by convection. So less energy is lost from the bird's body.",
  ["What is trapped between the feathers?", "Is it a good or poor conductor?", "What is the effect on energy loss?"],
  "trapped air (poor conductor, no convection) reduces energy loss",
  ["Fluffing traps more air, which is a poor conductor, so less energy is lost", "the trapped air insulates the bird and reduces energy loss"],
  ["The feathers produce heat", "Fluffing lets the cold out"], min_points=2, pitfalls=[COLD_FLOWS])

# ---------------------------------------------------------------- L3
Q("w8b_pot_lid", 3, "8e", "Explain why putting a lid on a pan of water makes it boil more quickly.",
  [P("the lid stops warm air and water vapour escaping (reduces convection losses)", ["stops warm air escaping", "reduces convection", "traps the warm air", "lid traps", "vapour cannot escape", "keeps the heat in"]),
   P("so less energy is lost to the surroundings, and more energy heats the water", ["less energy is lost", "more energy heats the water", "more energy goes into the water", "less heat lost", "reduces energy loss"])],
  "Without a lid, warm air and water vapour rise and escape from the pan, carrying energy away by convection (and evaporation). A lid traps them, so less energy is lost to the surroundings and more of the energy supplied heats the water, which boils sooner.",
  ["What escapes from an open pan?", "Which process carries that energy away?", "What difference does the lid make?"],
  "lid reduces convection/vapour losses → more energy heats water",
  ["The lid stops warm air and vapour escaping, so less energy is lost and the water heats faster", "it traps the warm air, reducing convection, so more energy goes into the water"],
  ["The lid makes the water heavier", "The lid lets cold out"], min_points=2, pitfalls=[COLD_FLOWS])

Q("w8b_survival_blanket", 3, "8d", "Marathon runners are wrapped in shiny foil blankets after a race. Explain how the blanket keeps them warm.",
  [P("the shiny surface is a poor emitter / good reflector of infrared radiation", ["shiny", "reflect", "reflects", "poor emitter", "reflector"]),
   P("it reflects the runner's infrared radiation back towards the body", ["back towards the body", "reflects it back", "back to the body", "returns"]),
   P("so less energy is lost by radiation (it also traps air, reducing convection)", ["less energy lost", "reduces radiation", "reduce energy loss", "traps air", "less heat lost"])],
  "The shiny foil is a poor emitter and a good reflector of infrared radiation. It reflects the infrared radiation emitted by the runner's body back towards them, so less energy is lost by radiation; the blanket also traps a layer of air, reducing convection.",
  ["What does a shiny surface do to infrared radiation?", "Where does the body's radiation go?", "What is the effect on energy loss?"],
  "shiny reflects IR back; less radiation loss",
  ["The shiny foil reflects the body's infrared radiation back, so less energy is lost", "it is a poor emitter and good reflector, reducing radiation loss"],
  ["The foil produces heat", "The foil absorbs cold"], min_points=2, pitfalls=[COLD_FLOWS])

Q("w8b_chimney_smoke", 3, "8c", "Smoke from a fire rises up the chimney. Explain this using convection.",
  [P("the fire heats the air, which expands and becomes less dense", ["less dense", "expands", "lower density", "heated air"]),
   P("the hot, less dense air rises up the chimney, carrying the smoke", ["rises", "carries the smoke", "goes up the chimney"]),
   P("cooler, denser air flows in below to replace it (convection current)", ["cooler air", "denser air", "flows in", "replace", "convection current", "by convection", "sinks"])],
  "The fire heats the air above it, which expands and becomes less dense. The hot air rises up the chimney, carrying the smoke with it, while cooler, denser air flows in at the bottom to replace it. This is a convection current.",
  ["What does the fire do to the air above it?", "Why does that air rise?", "What replaces it?"],
  "hot air less dense rises carrying smoke; cool air replaces it",
  ["The fire heats the air so it becomes less dense and rises up the chimney with the smoke, and cooler air flows in to replace it", "hot air rises by convection, carrying the smoke"],
  ["Smoke is pulled up by the wind only", "Heat rises"], min_points=2, pitfalls=[HEAT_RISES])

Q("w8b_land_breeze", 3, "8c", "At night, a breeze often blows from the land out to sea. Explain why.",
  [P("at night the land cools faster than the sea, so the sea is warmer", ["land cools faster", "sea is warmer", "land is cooler", "sea stays warm"]),
   P("air above the warm sea is heated, becomes less dense and rises", ["less dense", "rises", "air above the sea rises", "warm air rises"]),
   P("cooler, denser air from the land moves out to replace it (convection)", ["cooler air from the land", "denser air", "moves out to sea", "replace", "convection"])],
  "At night the land cools faster than the sea, so the sea becomes warmer than the land. The air above the warmer sea is heated, becomes less dense and rises; cooler, denser air from over the land moves out to replace it, giving a breeze from land to sea.",
  ["Which cools faster at night, land or sea?", "Above which is the air warmer?", "Which way must air flow to replace rising air?"],
  "land cooler at night; air over sea rises; land air flows out",
  ["The land cools faster, so the air above the warmer sea rises and cooler air from the land moves out to replace it", "warm air over the sea rises, and the denser land air flows out to sea by convection"],
  ["The sea pulls the air", "Cold flows from the land"], min_points=2, pitfalls=[COLD_FLOWS])

Q("w8b_cavity_foam", 3, "8e", "Many houses have a gap between their inner and outer walls, which is filled with foam. Explain how this reduces energy loss.",
  [P("foam traps air in small pockets", ["traps air", "trapped air", "pockets of air", "air bubbles"]),
   P("which stops air circulating in the gap (no convection currents)", ["stops convection", "no convection", "cannot circulate", "stops air circulating", "prevents convection", "reduces convection"]),
   P("foam and air are poor conductors", ["poor conductor", "insulator", "does not conduct"])],
  "Without foam, air in the wall cavity can circulate in convection currents, carrying energy from the warm inner wall to the cold outer wall. Foam traps the air in small pockets so it cannot circulate, and both the foam and the trapped air are poor conductors, so less energy is lost.",
  ["What happens to air in an empty cavity?", "What does the foam do to the air?", "Are foam and air good conductors?"],
  "foam traps air → no convection; poor conductors",
  ["The foam traps air so convection currents cannot form, and the foam and air are poor conductors", "it stops air circulating in the cavity and is an insulator"],
  ["The foam reflects the cold", "Foam is a good conductor"], min_points=2, pitfalls=[COLD_FLOWS])

Q("w8b_nonmetal_conduction", 3, "8b", "Explain how energy is conducted through a non-metal such as glass, and why this is slow.",
  [P("particles at the hot end vibrate more and pass energy to neighbouring particles", ["vibrate more", "vibrations", "pass energy to neighbouring", "collide with neighbours", "bump into"]),
   P("there are no free electrons in a non-metal", ["no free electrons", "no electrons to carry", "lacks free electrons"]),
   P("so energy is passed on only by vibrations, which is slow", ["only by vibrations", "slow", "slowly", "takes time"])],
  "At the hot end, the particles vibrate more strongly and pass energy to their neighbours, which then vibrate more, and so on along the material. A non-metal has no free electrons, so energy is passed on only by these vibrations, which is a slow process.",
  ["How do particles in a solid pass on energy?", "What do metals have that glass lacks?", "Why is glass a poor conductor?"],
  "vibrations only (no free electrons) → slow",
  ["The particles vibrate and pass energy to their neighbours, but there are no free electrons, so it is slow", "only vibrations carry the energy in glass, which is slow"],
  ["Glass conducts by convection", "Glass has many free electrons"], min_points=2)

Q("w8b_black_car", 3, "8d", "On a sunny day a black car becomes much hotter inside than an identical white car. Explain why.",
  [P("black is a good absorber of radiation", ["good absorber", "black absorbs", "absorbs more", "absorbs radiation", "absorbs well"]),
   P("white reflects most of the radiation", ["white reflects", "reflects", "poor absorber", "reflector"]),
   P("so the black car absorbs more energy from the Sun", ["more energy", "absorbs more energy", "heats up more", "gets hotter"])],
  "Black is a good absorber of infrared radiation, whereas white reflects most of it. So the black car absorbs much more energy from the Sun's radiation and becomes hotter.",
  ["Which colour absorbs radiation best?", "What does white do?", "Compare the energy absorbed."],
  "black absorbs, white reflects",
  ["Black is a good absorber, while white reflects radiation, so the black car absorbs more energy", "the black car absorbs more of the Sun's radiation and gets hotter"],
  ["Black cars have bigger engines", "White cars absorb more radiation"], min_points=2)

Q("w8b_shiny_kettle", 3, "8d", "Explain why a shiny metal kettle keeps water hot for longer than a dull black kettle of the same size.",
  [P("shiny surfaces are poor emitters of infrared radiation", ["poor emitter", "shiny surfaces are poor emitters", "emits less", "emit less"]),
   P("dull black surfaces are good emitters", ["good emitter", "black is a good emitter", "black emits more", "emits more"]),
   P("so the shiny kettle loses energy by radiation more slowly", ["loses energy more slowly", "less energy lost", "slower", "stays hot longer", "black kettle cools faster", "cools faster"])],
  "A shiny surface is a poor emitter of infrared radiation, while a dull black surface is a good emitter. So the shiny kettle loses energy by radiation more slowly, and the water stays hot for longer.",
  ["Which surface emits radiation better?", "Which kettle loses energy faster?", "Explain."],
  "shiny: poor emitter → slower energy loss",
  ["The shiny kettle is a poor emitter, so it loses energy by radiation more slowly than the black one", "black is a good emitter, so the black kettle cools faster"],
  ["Shiny kettles absorb more heat", "Black kettles keep heat in better"], min_points=2)

Q("w8b_engine_fins", 3, "8e", "Motorcycle engines have metal fins on the outside. Explain how these help to keep the engine cool.",
  [P("the fins greatly increase the surface area", ["surface area", "larger area", "bigger area", "more surface"]),
   P("so more energy is transferred to the air by convection and radiation", ["convection", "radiation", "more energy", "to the air", "lost faster", "faster energy loss"]),
   P("metal conducts energy from the engine to the fins quickly", ["metal conducts", "good conductor", "conducts"])],
  "The metal fins conduct energy away from the engine quickly and greatly increase its surface area, so more energy is transferred to the surrounding air by convection and radiation, keeping the engine cool.",
  ["What do the fins do to the surface area?", "How does energy leave the fins?", "Why metal?"],
  "large surface area; metal conducts; convection and radiation to air",
  ["The fins increase the surface area so more energy is lost to the air by convection and radiation, and metal conducts it there quickly", "a bigger surface area means faster energy loss"],
  ["The fins make the engine heavier", "The fins let cold into the engine"], min_points=2, pitfalls=[COLD_FLOWS])

Q("w8b_drink_ice_equilibrium", 3, "8a", "Ice is added to a warm drink and left until all the ice has melted. Explain what happens to the temperatures of the drink and the melted ice, and when the energy transfer stops.",
  [P("energy flows from the warmer drink to the colder ice", ["from the drink to the ice", "drink to the ice", "from warmer to colder", "warm drink transfers"]),
   P("the drink cools and the ice melts and then warms", ["drink cools", "ice melts", "warms", "drink gets colder"]),
   P("until everything reaches the same temperature (thermal equilibrium)", ["same temperature", "thermal equilibrium", "equal temperature"])],
  "Energy flows from the warmer drink to the colder ice. The drink cools, while the ice melts and the meltwater warms up. The transfer stops when the drink and the meltwater reach the same temperature: thermal equilibrium.",
  ["Which way does energy flow?", "What happens to each part?", "When does the net transfer stop?"],
  "drink → ice until same temperature (thermal equilibrium)",
  ["Energy flows from the drink to the ice, so the drink cools and the ice melts until they reach the same temperature", "the warm drink transfers energy to the ice until thermal equilibrium"],
  ["Cold flows from the ice into the drink", "The drink gets warmer"], min_points=2, pitfalls=[COLD_FLOWS])

# ---------------------------------------------------------------- L4
Q("w8b_compare_three_processes", 4, "8e", "Compare conduction, convection and radiation in terms of whether each needs a medium and in which materials each mainly occurs.",
  [P("conduction needs a medium; mainly in solids (especially metals)", ["conduction", "solids", "metals"]),
   P("convection needs a fluid medium: liquids and gases", ["convection", "liquids and gases", "fluids"]),
   P("radiation needs no medium and can travel through a vacuum", ["radiation", "no medium", "vacuum", "does not need"])],
  "Conduction needs a medium and occurs mainly in solids, especially metals. Convection needs a medium that can flow, so it occurs in liquids and gases. Radiation needs no medium at all and can travel through a vacuum.",
  ["Which processes need particles?", "Which needs a fluid?", "Which can cross a vacuum?"],
  "conduction: solids; convection: fluids; radiation: no medium",
  ["Conduction mainly happens in solids, convection in liquids and gases, and radiation needs no medium so it can cross a vacuum", "conduction and convection need a medium, radiation does not"],
  ["All three need a vacuum", "Radiation only happens in solids"], min_points=3)

Q("w8b_fridge_unit_top", 4, "8c", "The cooling unit of a fridge is placed at the top. Explain how this cools food on all the shelves.",
  [P("air near the cooling unit is cooled, becomes denser and sinks", ["cooled", "denser", "sinks", "more dense"]),
   P("warmer air near the bottom rises up to the unit", ["warmer air rises", "warm air rises", "rises"]),
   P("so a convection current circulates cold air past all the shelves", ["convection current", "circulates", "convection", "all the shelves"])],
  "Air next to the cooling unit at the top is cooled, so it contracts, becomes denser and sinks past the shelves. Warmer air near the bottom rises up to the unit to be cooled. This sets up a convection current that carries cold air past every shelf.",
  ["What happens to air that is cooled?", "What replaces it?", "How does this reach every shelf?"],
  "cooled air sinks; warmer air rises; convection current",
  ["Air at the top is cooled and sinks, warmer air rises to replace it, so a convection current cools all the shelves", "the dense cold air sinks past the shelves and warmer air rises, circulating"],
  ["Cold air rises from the bottom", "Cold flows down the walls"], min_points=2, pitfalls=[COLD_FLOWS])

Q("w8b_solar_cooker", 4, "8d", "A solar cooker has a curved shiny reflector that focuses sunlight onto a black cooking pot. Explain the purpose of each feature.",
  [P("shiny reflector reflects (and concentrates) the Sun's radiation onto the pot", ["shiny reflector", "reflector reflects", "reflects the sun", "reflects sunlight onto", "focuses", "concentrates", "directs"]),
   P("black pot is a good absorber of radiation", ["good absorber", "absorbs", "absorbs well"]),
   P("so the pot absorbs a lot of energy and heats the food", ["heats the food", "more energy", "gets hot", "cooks"])],
  "The curved shiny reflector reflects sunlight and concentrates it onto the pot. The pot is black because a dull black surface is a good absorber of radiation, so it absorbs as much of the concentrated energy as possible and heats the food.",
  ["What does a shiny surface do to radiation?", "What does a black surface do?", "How do they work together?"],
  "shiny reflector concentrates; black pot absorbs",
  ["The shiny reflector focuses the Sun's radiation onto the pot, and the black pot is a good absorber, so it heats the food", "reflector concentrates sunlight; black absorbs it well"],
  ["The black pot reflects the sunlight", "The reflector absorbs the sunlight"], min_points=2,
  pitfalls=[PF(["black pot reflects", "black reflects", "reflector absorbs"], "Black surfaces ABSORB radiation; shiny surfaces reflect it.")])

Q("w8b_double_wall_cup", 4, "8e", "A drinks cup has two plastic walls with a sealed air gap between them. Explain why a hot drink stays hot longer in it than in a single-walled cup.",
  [P("the air gap is a poor conductor", ["poor conductor", "air is an insulator", "insulator", "does not conduct well", "air insulates", "reducing conduction"]),
   P("plastic is also a poor conductor", ["plastic", "poor conductor"]),
   P("the gap is sealed/narrow so air cannot circulate much (little convection)", ["little convection", "cannot circulate", "sealed", "no convection", "reduces convection"])],
  "Plastic and the air in the gap are both poor conductors, so energy is conducted through the walls only slowly. The air gap is narrow and sealed, so the air cannot circulate much and convection is also small. So less energy escapes and the drink stays hot longer.",
  ["Are plastic and air good conductors?", "Can the air in a sealed narrow gap move much?", "What is the overall effect?"],
  "air gap and plastic poor conductors; little convection",
  ["The air gap and plastic are poor conductors and the sealed air cannot circulate, so less energy is lost", "the trapped air insulates, reducing conduction and convection"],
  ["The cup produces heat", "The gap lets cold out"], min_points=2, pitfalls=[COLD_FLOWS])

Q("w8b_wetsuit", 4, "8e", "A surfer's wetsuit lets a thin layer of water in between the suit and the skin. Explain how the wetsuit still keeps the surfer warm.",
  [P("the thin water layer is trapped and warmed by the body", ["trapped", "warmed by the body", "heated by the body", "thin layer of water"]),
   P("the trapped water cannot circulate, so convection is reduced", ["cannot circulate", "cannot move", "no convection", "reduces convection"]),
   P("the neoprene suit (with gas bubbles) is a poor conductor", ["poor conductor", "insulator", "bubbles", "neoprene"])],
  "The thin layer of water between the suit and the skin is trapped and soon warmed by the body. Because it cannot circulate, little energy is carried away by convection. The suit material, which contains tiny gas bubbles, is a poor conductor, so energy is lost only slowly.",
  ["What happens to the water trapped next to the skin?", "Can it move away?", "What is the suit material like?"],
  "trapped warmed water, no circulation; suit is a poor conductor",
  ["The thin water layer is trapped and warmed by the body, it cannot circulate, and the suit is a poor conductor", "the suit traps water that the body warms, reducing convection"],
  ["The wetsuit generates heat", "The water keeps the cold out"], min_points=2, pitfalls=[COLD_FLOWS])

Q("w8b_coolbox_design", 4, "8e", "Describe and explain three features of a well-designed coolbox for keeping drinks cold on a hot day.",
  [P("walls made of a poor conductor, e.g. foam/polystyrene with trapped air, reducing conduction", ["polystyrene", "foam", "poor conductor", "insulator", "trapped air"]),
   P("light-coloured or shiny outer surface to reflect the Sun's radiation", ["shiny", "light coloured", "white", "reflect"]),
   P("a tight-fitting lid to stop warm air getting in (convection)", ["lid", "tight", "seal", "stops warm air", "convection"])],
  "A good coolbox has thick walls of a poor conductor such as polystyrene foam, which traps air, so little energy is conducted in. Its outer surface is white or shiny to reflect the Sun's radiation. A tight-fitting lid stops warm air from entering and circulating, reducing convection. All three slow the flow of energy into the box.",
  ["How can conduction into the box be reduced?", "How can radiation be reduced?", "How can convection be reduced?"],
  "insulating walls; reflective surface; tight lid",
  ["Polystyrene walls are poor conductors, a white shiny outside reflects radiation, and a tight lid stops warm air getting in", "foam walls, a shiny surface and a good seal reduce energy entering"],
  ["Black walls to absorb the cold", "Metal walls to conduct the cold out"], min_points=2, pitfalls=[COLD_FLOWS])

Q("w8b_radiation_rate_factors", 4, "8d", "State and explain three factors that affect the rate at which a hot object emits infrared radiation.",
  [P("surface colour and texture: dull black emits faster than shiny silver", ["colour", "texture", "dull black", "shiny", "matt"]),
   P("surface temperature: a hotter surface emits faster", ["temperature", "hotter"]),
   P("surface area: a larger area emits faster", ["surface area", "larger area", "bigger area"])],
  "The rate of emission depends on: the surface colour and texture (dull black surfaces emit faster than shiny silver ones); the surface temperature (a hotter surface emits faster); and the surface area (a larger area emits faster).",
  ["Think about colour and shininess.", "Think about how hot it is.", "Think about how big its surface is."],
  "colour/texture, temperature, surface area",
  ["Dull black surfaces emit faster, hotter surfaces emit faster, and larger surface areas emit faster", "the colour and texture, the temperature and the surface area"],
  ["Mass, volume and price", "The weight of the object"], min_points=3)

Q("w8b_house_heat_losses", 4, "8e", "Describe two ways energy escapes from a house in winter, and for each suggest a way to reduce it.",
  [P("through the roof (by convection/conduction): loft insulation", ["roof", "loft insulation", "loft"]),
   P("through the walls: cavity wall insulation", ["walls", "cavity", "cavity wall"]),
   P("through windows: double glazing / curtains; through gaps: draught excluders", ["windows", "double glazing", "curtains", "draught", "gaps"])],
  "Energy escapes through the roof, which can be reduced with loft insulation; through the walls, reduced with cavity-wall insulation; and through the windows, reduced with double glazing or thick curtains (draught excluders stop warm air escaping through gaps).",
  ["Where can warm air and energy escape from a house?", "What material traps air in each case?", "Give two pairs."],
  "roof/loft insulation; walls/cavity; windows/double glazing; draughts",
  ["Through the roof, reduced by loft insulation, and through the windows, reduced by double glazing", "through the walls, so use cavity wall insulation, and through gaps, so use draught excluders"],
  ["Cold gets in through the doors", "Open the windows to let the cold out"], min_points=2, pitfalls=[COLD_FLOWS])

Q("w8b_tiles_vs_carpet", 4, "8b", "A tiled floor and a carpet in the same room are at the same temperature, but the tiles feel much colder to bare feet. Explain why.",
  [P("both are at the same temperature (room temperature), lower than the feet", ["same temperature", "room temperature", "both are at"]),
   P("tiles are a better conductor than carpet", ["better conductor", "tiles conduct", "good conductor", "conduct better"]),
   P("so tiles conduct energy away from the feet faster", ["faster", "more quickly", "away from the feet", "energy leaves"])],
  "Both are at the same room temperature, which is lower than that of your feet. Tiles are a much better conductor than carpet (which traps air), so they conduct energy away from your feet much faster, making them feel colder.",
  ["Are the tiles actually colder?", "Which material conducts better?", "What does that do to energy leaving your feet?"],
  "same temperature; tiles conduct energy away faster",
  ["They are at the same temperature, but tiles are a better conductor, so they conduct energy away from your feet faster", "tiles conduct well, so energy leaves the feet more quickly than on carpet"],
  ["The tiles are at a lower temperature", "Carpet produces heat"], min_points=2, pitfalls=[COLD_FLOWS, PF(["tiles are at a lower temperature", "tiles are colder"], "Both are at the same temperature; tiles just conduct energy away faster.")])

Q("w8b_crystal_convection", 4, "8c", "A purple crystal is placed at the bottom corner of a beaker of water, and that corner is heated gently. Describe what is seen and explain it.",
  [P("purple streaks rise above the crystal", ["rise", "rises", "goes up", "purple streaks"]),
   P("then move across the top and sink on the other side, in a loop (convection current)", ["across the top", "sinks", "loop", "circulates", "convection current"]),
   P("because heated water expands, becomes less dense and rises; cooler denser water sinks", ["less dense", "expands", "denser water sinks", "cooler water sinks"])],
  "Purple streaks rise from the crystal, travel across the top of the beaker, sink down the far side and return along the bottom, showing a convection current. The heated water expands and becomes less dense, so it rises; cooler, denser water sinks to take its place.",
  ["What happens to the water above the heat?", "Where does the colour go next?", "Why does warm water rise?"],
  "colour rises, crosses, sinks: convection current (warm water less dense)",
  ["The purple colour rises above the heat, moves across the top and sinks on the other side, because heated water is less dense and rises while cooler water sinks", "it shows a convection current: warm water rises, cool denser water sinks"],
  ["The crystal sinks and stays at the bottom", "Heat rises"], min_points=2, pitfalls=[HEAT_RISES])

# ---------------------------------------------------------------- L5
Q("w8b_blanket_claim", 5, "8e", "A student says: 'A blanket warms you up because it gives out heat.' Evaluate this claim.",
  [P("wrong: a blanket does not produce energy", ["wrong", "does not produce", "does not give out heat", "no heat of its own", "incorrect"]),
   P("it is an insulator that traps air and reduces the rate of energy loss from your body", ["insulator", "traps air", "reduces energy loss", "slows the loss", "poor conductor"]),
   P("your body produces the energy; the blanket keeps it in", ["body produces", "your body", "keeps it in", "keeps the energy in"])],
  "The claim is wrong. A blanket does not produce any energy. Your body produces the energy, and the blanket, being a poor conductor that traps air, reduces the rate at which energy is lost from your body, so you stay warm.",
  ["Does the blanket have its own energy source?", "What does a blanket actually do to energy flow?", "Where does the energy come from?"],
  "wrong; blanket insulates (traps air), reducing energy loss from the body",
  ["Wrong: the blanket does not produce heat; it is an insulator that reduces energy loss from your body", "it traps air and keeps the body's energy in rather than giving out heat"],
  ["Correct, blankets give out heat", "Correct, the blanket keeps the cold out"], min_points=2, pitfalls=[COLD_FLOWS])

Q("w8b_colour_cooling_design", 5, "8d", "Design an experiment to find out whether a dull black can or a shiny silver can of hot water cools faster.",
  [P("same size cans, same volume of water, same starting temperature", ["same volume", "same starting temperature", "same size", "same amount of water", "fair test"]),
   P("record the temperature of each at regular intervals with thermometers", ["thermometer", "regular intervals", "every minute", "record the temperature"]),
   P("compare the temperature drops (or plot cooling curves); the faster drop shows the better emitter", ["compare", "plot", "graph", "cooling curve", "faster drop", "greater drop"])],
  "Use two identical cans, one painted dull black and one shiny silver. Fill both with the same volume of hot water at the same starting temperature, with lids on and in the same place. Record the temperature of each with a thermometer every minute and plot cooling curves. The can whose temperature falls faster is the better emitter (expected: the black can).",
  ["What must be kept the same for a fair test?", "What do you measure, and how often?", "How do you compare the results?"],
  "same volume, starting temperature; temperature at intervals; compare cooling",
  ["Use the same volume of water at the same starting temperature in each can, measure the temperature every minute with a thermometer and compare the cooling", "keep everything the same except the colour, record temperatures at regular intervals and plot cooling curves"],
  ["Weigh the cans before and after", "Feel which can is colder"], min_points=2)

Q("w8b_flask_cold_drinks", 5, "8e", "A student says: 'A vacuum flask keeps hot drinks hot, so it must make cold drinks warm up faster.' Evaluate this.",
  [P("wrong: the flask reduces energy transfer in both directions", ["wrong", "both directions", "either direction", "both ways", "reduces energy transfer"]),
   P("the vacuum stops conduction and convection; the silvered walls reduce radiation", ["vacuum", "conduction and convection", "silvered", "radiation"]),
   P("so a cold drink warms up more slowly, staying cold", ["warms up more slowly", "stays cold", "keeps it cold", "slower"])],
  "The claim is wrong. A vacuum flask reduces energy transfer in both directions: the vacuum stops conduction and convection, and the silvered walls reduce radiation. So energy from the warm surroundings enters a cold drink only slowly, and the drink stays cold for longer.",
  ["Does the flask only stop energy leaving?", "Which features reduce which processes?", "What happens to a cold drink?"],
  "flask reduces transfer both ways; cold drink stays cold",
  ["Wrong: the flask reduces energy transfer both ways, so a cold drink warms up more slowly and stays cold", "the vacuum and silver walls slow energy flow in either direction, keeping cold drinks cold"],
  ["Correct, flasks only keep heat in", "Correct, flasks heat cold drinks"], min_points=2)

Q("w8b_ice_in_blanket", 5, "8e", "A student wraps ice cubes in a woollen blanket, expecting them to melt faster 'because blankets are warm'. Evaluate this prediction.",
  [P("the prediction is wrong: the ice melts more slowly", ["wrong", "more slowly", "slower", "melts slower", "takes longer"]),
   P("the blanket is an insulator (traps air), reducing energy transfer from the warm room into the ice", ["insulator", "traps air", "reduces energy transfer", "slows energy", "poor conductor"]),
   P("a blanket does not produce energy; it only slows energy flow", ["does not produce", "no energy of its own", "only slows", "not warm itself"])],
  "The prediction is wrong. A blanket does not produce energy; it is an insulator that traps air and slows the transfer of energy. Here it slows the flow of energy from the warm room into the ice, so the ice melts more slowly.",
  ["Does the blanket give out energy?", "Which way does energy flow here?", "What does an insulator do to that flow?"],
  "wrong; blanket insulates → slows energy into ice → melts slower",
  ["Wrong: the blanket is an insulator, so it slows the energy flowing from the room into the ice, and the ice melts more slowly", "the blanket does not produce heat; it traps air and reduces energy transfer, so the ice lasts longer"],
  ["Correct, blankets are warm so the ice melts faster", "Correct, wool gives out heat"], min_points=2)

Q("w8b_heater_ceiling", 5, "8c", "A room heater is fixed high up near the ceiling. Evaluate this position.",
  [P("poor position: warm air from the heater rises and stays near the ceiling", ["poor position", "stays near the ceiling", "warm air rises", "stays at the top", "bad position"]),
   P("so no good convection current forms to circulate warm air down to people", ["no convection current", "does not circulate", "cannot circulate", "not reach the floor", "convection"]),
   P("a heater near the floor is better: warm air rises and cooler air sinks to be heated, warming the room", ["near the floor", "low down", "floor is better", "better low"])],
  "This is a poor position. Air warmed by the heater rises and simply stays near the ceiling, so no good convection current forms and the lower part of the room, where people are, stays cold. A heater near the floor is better: warmed air rises, cooler air sinks to be heated, and a convection current warms the whole room.",
  ["Where does warm air go?", "Will a convection current form if the heater is at the top?", "Where would be better?"],
  "poor: warm air stays at ceiling; low heater gives convection current",
  ["Poor position: the warm air rises and stays near the ceiling, so no convection current warms the room; a heater near the floor is better", "the warm air cannot circulate down, so the heater should be low down"],
  ["Good, because heat rises to the ceiling and warms it", "Good, because heat sinks"], min_points=2, pitfalls=[HEAT_RISES, PF(["heat sinks"], "Warm air rises; cool air sinks.")])

Q("w8b_cooling_slows", 5, "8a", "A cup of hot tea cools quickly at first, then more and more slowly. Explain this pattern.",
  [P("the rate of energy loss depends on the temperature difference between the tea and the room", ["temperature difference", "difference in temperature", "hotter than the room"]),
   P("at first the difference is large, so energy is lost quickly", ["large difference", "quickly at first", "big difference", "faster at first"]),
   P("as the tea cools the difference becomes smaller, so it cools more slowly, until it reaches room temperature", ["smaller difference", "more slowly", "room temperature", "equilibrium"])],
  "The rate at which the tea loses energy depends on how much hotter it is than the room. At first the temperature difference is large, so energy is lost quickly. As the tea cools, the difference becomes smaller, so it cools more and more slowly until it reaches room temperature.",
  ["What drives the energy transfer?", "How does that change as the tea cools?", "When does it stop?"],
  "rate ∝ temperature difference; difference shrinks → slower",
  ["The rate depends on the temperature difference; it is large at first so it cools quickly, then smaller so it cools more slowly until it reaches room temperature", "as the tea gets closer to room temperature, the difference is smaller and it cools more slowly"],
  ["The tea runs out of heat", "Cold flows into the tea faster later"], min_points=2, pitfalls=[COLD_FLOWS])

Q("w8b_satellite_foil", 5, "8d", "Many satellites are wrapped in shiny gold-coloured foil. Evaluate why this is useful in space.",
  [P("in space energy can only be gained or lost by radiation (vacuum)", ["only by radiation", "radiation", "vacuum", "no conduction or convection"]),
   P("the shiny foil reflects much of the Sun's radiation, so the satellite does not overheat", ["reflects", "does not overheat", "stays cool", "reflect the sun"]),
   P("it is also a poor emitter, so it does not lose too much energy when in shadow", ["poor emitter", "emits little", "does not lose too much", "in shadow", "keeps warm"])],
  "In the vacuum of space, energy can be gained or lost only by radiation. The shiny foil reflects much of the Sun's radiation, so the satellite does not overheat in sunlight, and as a poor emitter it does not lose energy too quickly when it is in the Earth's shadow. This keeps its temperature steadier.",
  ["Which energy transfer process works in space?", "What does a shiny surface do to incoming radiation?", "And to outgoing radiation?"],
  "only radiation in space; foil reflects (no overheating) and emits poorly (no over-cooling)",
  ["In space only radiation transfers energy; the shiny foil reflects the Sun's radiation so it does not overheat and is a poor emitter so it does not get too cold", "the foil reflects sunlight and emits little, keeping the temperature steady"],
  ["The foil conducts heat into space", "Gold keeps the cold out"], min_points=2, pitfalls=[COLD_FLOWS])

Q("w8b_insulation_test_plan", 5, "8e", "Plan an experiment to compare how well three materials (wool, cotton, bubble wrap) insulate a beaker of hot water.",
  [P("wrap identical beakers with the same thickness of each material (plus one unwrapped as a control)", ["same thickness", "identical beakers", "control", "unwrapped", "wrap each beaker"]),
   P("same volume of water at the same starting temperature", ["same volume", "same starting temperature", "same amount of water", "same temperature"]),
   P("measure the temperature after a fixed time (or every few minutes); the smallest drop is the best insulator", ["smallest drop", "fixed time", "every few minutes", "measure the temperature", "compare the temperature", "after 10 minutes", "thermometer", "least temperature drop"])],
  "Wrap identical beakers with the same thickness of wool, cotton and bubble wrap, and leave one unwrapped as a control. Fill each with the same volume of hot water at the same starting temperature. Record the temperature of each with a thermometer every few minutes for the same total time. The material whose beaker shows the smallest temperature drop is the best insulator.",
  ["What must be identical for a fair test?", "What do you measure?", "How do you decide which is best?"],
  "same beaker, thickness, volume, starting temperature; measure drops; smallest drop best",
  ["Wrap identical beakers with the same thickness of each material, use the same volume of water at the same starting temperature, and measure the temperature drop after a fixed time; the smallest drop is the best insulator", "keep the volume and starting temperature the same and compare the temperature after 10 minutes"],
  ["Feel which material is softest", "Weigh the materials"], min_points=2)

Q("w8b_dark_clothes_winter", 5, "8d", "A student suggests wearing dark clothes on a cold, sunny winter day. Evaluate this suggestion.",
  [P("dark clothes are good absorbers of the Sun's radiation, so they gain energy in sunlight", ["good absorber", "absorb", "absorbs radiation", "gain energy"]),
   P("this helps keep the wearer warm when in sunshine", ["keeps warm", "warmer", "helps"]),
   P("but dark surfaces are also good emitters, so in the shade/at night they lose energy faster; thickness and trapped air matter more", ["good emitter", "lose energy faster", "in the shade", "at night", "trapped air", "thickness"])],
  "It is partly sensible. Dark clothes are good absorbers of radiation, so in sunshine they absorb energy from the Sun and help keep the wearer warm. But dark surfaces are also good emitters, so in the shade or at night they lose energy by radiation faster. In practice, thick clothing that traps air matters more than colour.",
  ["What do dark surfaces do to incoming radiation?", "What do they do to outgoing radiation?", "What else affects how warm clothes keep you?"],
  "good absorber in sun; good emitter in shade; trapped air matters",
  ["Dark clothes absorb the Sun's radiation, which helps in sunshine, but they are also good emitters so they lose energy faster in the shade", "it helps in the sun because dark colours absorb, but thick clothes that trap air matter more"],
  ["Dark clothes keep the cold out", "Dark clothes reflect sunlight"], min_points=2, pitfalls=[COLD_FLOWS])

Q("w8b_convection_solid_claim", 5, "8c", "A student says: 'If you heat a block of metal strongly enough, convection currents will form inside it.' Evaluate this claim.",
  [P("wrong: convection cannot happen in a solid", ["wrong", "cannot happen in a solid", "not in solids", "solids cannot", "incorrect"]),
   P("convection needs the material to flow, but solid particles are fixed in position", ["flow", "fixed positions", "cannot move", "particles are fixed", "cannot flow"]),
   P("energy passes through the metal by conduction instead (vibrations and free electrons) — unless it melts", ["conduction", "free electrons", "vibrations", "melts", "unless it melts"])],
  "The claim is wrong. Convection requires the material itself to flow, carrying energy with it, but the particles in a solid are fixed in position and cannot flow. Energy travels through the metal by conduction instead, through vibrations and free electrons. Only if the metal melted could convection occur.",
  ["What does convection require the material to do?", "Can solid particles do that?", "How does energy move through the metal?"],
  "wrong; solids cannot flow; conduction instead",
  ["Wrong: convection needs the material to flow, but particles in a solid are fixed, so energy is transferred by conduction instead", "solids cannot flow, so there is no convection; the metal conducts the energy"],
  ["Correct, strong heating causes convection in metals", "Correct, metals have convection currents"], min_points=2)
