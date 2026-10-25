"""Chapter 10 Electromagnetic Spectrum: 50 more written-answer questions (10 per level), marked by keywords/phrases."""
from .. import sketches
from ..marker import Pitfall, Point
from .base import written

P = Point
PF = Pitfall
CH = 10


def Q(id, lv, lo, stem, points, model, hints, keywords, passes, fails, pitfalls=(), min_points=None, figure=None):
    written(id, CH, lv, lo, stem=stem, points=points, model_answer=model, hints=hints, keywords=keywords,
            pitfalls=pitfalls, min_points=min_points, figure=figure, sample_pass=passes, sample_fail=fails)


SPEC = lambda: sketches.em_spectrum()
LONGITUDINAL = PF(["em waves are longitudinal", "electromagnetic waves are longitudinal", "they are longitudinal"], "All electromagnetic waves are TRANSVERSE.")
NOT_IONISING = PF(["microwaves are ionising", "radio waves are ionising", "infrared is ionising", "visible light is ionising"],
                  "Only the high-frequency end (ultraviolet, X-rays, gamma rays) is ionising.")

# ---------------------------------------------------------------- L1
Q("w10b_order_increasing_f", 1, "10b", "Fig. 1 shows the electromagnetic spectrum. List the seven regions in order of increasing frequency.",
  [P("radio waves first (lowest frequency)", ["radio waves, microwaves", "radio, microwaves", "radio waves microwaves", "radio microwaves"], ordered=True, window=4),
   P("then infrared, visible, ultraviolet", ["infrared, visible", "infrared visible", "visible, ultraviolet", "visible ultraviolet"], ordered=True, window=4),
   P("then X-rays, gamma rays (highest)", ["x-rays, gamma", "x-rays gamma", "x rays gamma", "x-ray, gamma"], ordered=True, window=4)],
  "In order of increasing frequency: radio waves, microwaves, infrared, visible light, ultraviolet, X-rays, gamma rays.",
  ["Which region has the lowest frequency?", "Visible light is in the middle.", "Which region has the highest frequency?"],
  "radio, microwaves, infrared, visible, ultraviolet, X-rays, gamma",
  ["radio waves, microwaves, infrared, visible, ultraviolet, X-rays, gamma rays", "radio microwaves infrared visible ultraviolet x-rays gamma"],
  ["gamma rays, X-rays, ultraviolet, visible, infrared, microwaves, radio waves", "visible, radio, gamma"], min_points=3, figure=SPEC)

Q("w10b_shortest_lambda", 1, "10b", "Name the region of the electromagnetic spectrum with the shortest wavelength and state how its frequency compares with the others.",
  [P("gamma rays", ["gamma"]),
   P("they have the highest frequency", ["highest frequency", "largest frequency", "greatest frequency", "highest"])],
  "Gamma rays have the shortest wavelength, and therefore the highest frequency, of all electromagnetic waves.",
  ["Which end of the spectrum has the shortest waves?", "All EM waves have the same speed.", "So how does frequency compare?"],
  "gamma rays; highest frequency",
  ["Gamma rays, which have the highest frequency", "gamma, with the greatest frequency"],
  ["Radio waves, lowest frequency", "Visible light"], min_points=2, figure=SPEC)

Q("w10b_radio_use", 1, "10c", "State one use of radio waves.",
  [P("radio and TV broadcasting / communication, astronomy (radio telescopes) or RFID tags", ["radio", "television", "tv", "broadcasting", "communication", "astronomy", "rfid", "telescope"])],
  "Radio waves are used for radio and television broadcasting (also radio astronomy and RFID tags).",
  ["What does a radio receive?", "Think of broadcasting.", "State one use."],
  "broadcasting, astronomy, RFID",
  ["Radio and television broadcasting", "RFID tags in library books"],
  ["Cooking food", "Sterilising instruments"])

Q("w10b_infrared_use", 1, "10c", "State one use of infrared radiation.",
  [P("remote controls, thermal imaging, grills/toasters, intruder alarms, optical fibres", ["remote control", "thermal imaging", "grill", "toaster", "alarm", "heater", "night vision", "optical fibre", "cooking"])],
  "Infrared radiation is used in television remote controls (also thermal imaging cameras, grills and toasters, and intruder alarms).",
  ["Infrared is linked to heat.", "Think of a TV remote or a toaster.", "State one use."],
  "remote controls, thermal imaging, grills",
  ["TV remote controls", "thermal imaging cameras"],
  ["Sterilising medical equipment", "X-ray photographs"])

Q("w10b_visible_use", 1, "10c", "State one use of visible light other than seeing.",
  [P("photography, optical fibres (medical endoscopes), illumination, lasers, displays", ["photography", "camera", "optical fibre", "endoscope", "laser", "lighting", "illumination", "screens"])],
  "Visible light is used in photography and in optical fibres, for example in medical endoscopes (also lasers and lighting).",
  ["What do cameras detect?", "How do doctors see inside the body without surgery?", "State one use."],
  "photography, optical fibres",
  ["Photography with cameras", "optical fibres in endoscopes"],
  ["Mobile phone signals", "Killing bacteria"])

Q("w10b_gamma_use", 1, "10c", "State one use of gamma rays.",
  [P("sterilising medical equipment or food, or killing cancer cells (radiotherapy)", ["sterilising", "sterilise", "cancer", "radiotherapy", "kill bacteria", "medical tracers", "tracer"])],
  "Gamma rays are used to sterilise medical equipment and food, and in radiotherapy to kill cancer cells.",
  ["Gamma rays are very penetrating and kill cells.", "Where is killing cells useful?", "State one use."],
  "sterilising; cancer treatment",
  ["Sterilising medical instruments", "treating cancer by killing cancer cells"],
  ["Mobile phones", "TV remote controls"])

Q("w10b_name_ionising", 1, "10d", "Name two regions of the electromagnetic spectrum that are ionising.",
  [P("X-rays", ["x-rays", "x-ray", "x rays"]), P("gamma rays (also ultraviolet)", ["gamma", "ultraviolet", "uv"])],
  "X-rays and gamma rays are ionising (and so is part of the ultraviolet region).",
  ["Ionising radiation is at the high-frequency end.", "Which two regions are used in hospitals and are most dangerous?", "Name them."],
  "X-rays, gamma rays (UV)",
  ["X-rays and gamma rays", "gamma rays and X-rays"],
  ["Radio waves and microwaves", "Infrared and visible light"], min_points=2, pitfalls=[NOT_IONISING])

Q("w10b_vacuum_travel", 1, "10a", "State whether electromagnetic waves can travel through a vacuum, and give evidence.",
  [P("yes, they can travel through a vacuum (no medium needed)", ["yes", "can travel through a vacuum", "do not need a medium", "no medium"]),
   P("evidence: light and infrared from the Sun reach the Earth through space", ["sun", "space", "stars", "sunlight"])],
  "Yes. Electromagnetic waves do not need a medium, so they can travel through a vacuum; for example, light and infrared from the Sun reach the Earth through the vacuum of space.",
  ["Is there air between the Sun and the Earth?", "Does sunlight reach us?", "Answer and give evidence."],
  "yes; e.g. sunlight through space",
  ["Yes, light from the Sun travels through the vacuum of space", "they do not need a medium; sunlight reaches us through space"],
  ["No, they need air", "Only radio waves can"], min_points=2)

Q("w10b_red_violet", 1, "10b", "Within visible light, state which colour has the longest wavelength and which has the highest frequency.",
  [P("red has the longest wavelength", ["red has the longest", "red is longest", "red"]),
   P("violet has the highest frequency", ["violet has the highest", "violet is highest", "violet"])],
  "Red light has the longest wavelength in the visible spectrum, and violet light has the highest frequency (and shortest wavelength).",
  ["Infrared is next to which colour?", "Ultraviolet is next to which colour?", "Answer both."],
  "red longest wavelength; violet highest frequency",
  ["Red has the longest wavelength and violet the highest frequency", "red is longest, violet is highest frequency"],
  ["Blue has the longest wavelength", "Red has the highest frequency"], min_points=2,
  pitfalls=[PF(["red has the highest frequency", "violet has the longest wavelength"], "Red: longest wavelength (lowest frequency); violet: shortest wavelength (highest frequency).")])

Q("w10b_transfer_energy", 1, "10a", "State what electromagnetic waves transfer from one place to another.",
  [P("energy", ["energy"])],
  "Electromagnetic waves transfer energy from one place to another (for example from the Sun to the Earth), without transferring matter.",
  ["Waves in general transfer this.", "Sunlight warms you up.", "State it."],
  "energy", ["Energy", "they transfer energy, not matter"], ["Matter", "Air particles"],
  pitfalls=[PF(["transfer matter", "they transfer particles", "transfer air"], "EM waves transfer energy, not matter.")])

# ---------------------------------------------------------------- L2
Q("w10b_radio_vs_gamma", 2, "10b", "Fig. 1 shows the electromagnetic spectrum. Compare radio waves and gamma rays in terms of wavelength, frequency and speed in a vacuum.",
  [P("radio waves have a much longer wavelength", ["radio waves have a longer wavelength", "radio longer wavelength", "radio waves have the longest", "gamma shorter wavelength"]),
   P("gamma rays have a much higher frequency", ["gamma rays have a higher frequency", "gamma higher frequency", "gamma has the highest frequency", "radio lower frequency"]),
   P("both travel at the same speed in a vacuum", ["same speed", "both travel at", "3 × 10", "speed of light"])],
  "Radio waves have a much longer wavelength than gamma rays, while gamma rays have a much higher frequency. Both travel at the same speed in a vacuum, 3 × 10⁸ m/s.",
  ["Where is each on the spectrum?", "Compare wavelength and frequency.", "Do they differ in speed?"],
  "radio: long λ, low f; gamma: short λ, high f; same speed",
  ["Radio waves have a longer wavelength, gamma rays a higher frequency, and both travel at the same speed in a vacuum", "gamma has a shorter wavelength and higher frequency than radio, but the same speed"],
  ["Gamma rays travel faster than radio waves", "Radio waves have the higher frequency"], min_points=2, figure=SPEC,
  pitfalls=[PF(["gamma rays travel faster", "radio waves travel faster", "travel faster than"], "All EM waves travel at the same speed in a vacuum.")])

Q("w10b_phones_microwaves", 2, "10c", "State which region of the electromagnetic spectrum mobile phones use, and give one other use of the same region.",
  [P("microwaves", ["microwave"]),
   P("other use: satellite communication, Wi-Fi, cooking in microwave ovens, radar", ["satellite", "wi-fi", "wifi", "oven", "cooking", "radar"])],
  "Mobile phones use microwaves. Microwaves are also used for satellite communication, Wi-Fi and cooking in microwave ovens.",
  ["Which region is used for mobile signals?", "What else uses that region?", "State both."],
  "microwaves; satellites, Wi-Fi, ovens",
  ["Microwaves, which are also used in satellite communication", "microwaves; microwave ovens use them too"],
  ["Radio waves only", "Gamma rays"], min_points=2)

Q("w10b_rfid_astronomy", 2, "10c", "Give two different uses of radio waves.",
  [P("radio/television broadcasting (communication)", ["broadcasting", "radio", "television", "tv", "communication"]),
   P("radio astronomy (radio telescopes) or RFID tags", ["astronomy", "telescope", "rfid", "tags", "contactless"])],
  "Radio waves are used for radio and television broadcasting, in radio telescopes for astronomy, and in RFID tags such as those in library books and contactless cards.",
  ["Think of communication.", "Think of telescopes and tags.", "Give two."],
  "broadcasting; astronomy; RFID",
  ["Television broadcasting and RFID tags", "radio broadcasting and radio telescopes for astronomy"],
  ["Cooking and sterilising", "X-ray imaging"], min_points=2)

Q("w10b_infrared_hazard", 2, "10d", "State the main hazard of over-exposure to infrared radiation and explain it.",
  [P("burns to the skin", ["burns", "skin burns", "burn"]),
   P("infrared is absorbed by the skin and heats it (heating effect)", ["heating", "absorbed by the skin", "heats the skin", "heating effect"])],
  "Over-exposure to infrared can burn the skin, because the skin absorbs infrared radiation and is heated by it.",
  ["What do you feel from infrared?", "What happens if the skin is heated too much?", "State and explain."],
  "skin burns from heating",
  ["Skin burns, because infrared heats the skin when absorbed", "it can burn you through its heating effect"],
  ["It causes cancer by ionising cells", "It breaks bones"], min_points=2, pitfalls=[NOT_IONISING])

Q("w10b_infrared_cooking", 2, "10c", "Explain how a toaster or grill uses infrared radiation to cook food.",
  [P("the hot element emits infrared radiation", ["emits infrared", "gives out infrared", "infrared radiation", "hot element", "infrared from the element", "from the element"]),
   P("the food absorbs the infrared and is heated (its internal store increases)", ["absorbs", "absorbed", "heated", "heats the food", "internal store"])],
  "The hot element of the toaster or grill emits infrared radiation. The food absorbs this radiation and is heated, cooking its surface.",
  ["What does the glowing element give out?", "What happens when the food absorbs it?", "Explain."],
  "element emits IR; food absorbs it and heats",
  ["The hot element emits infrared, which the food absorbs and is heated by", "infrared from the element is absorbed by the bread and heats it"],
  ["The toaster uses microwaves", "Gamma rays cook the food"], min_points=2)

Q("w10b_satellite_tv", 2, "10c", "Satellite television signals are sent using microwaves. Suggest why microwaves are suitable.",
  [P("microwaves pass through the atmosphere (and clouds) to and from satellites", ["pass through the atmosphere", "through the atmosphere", "through clouds", "not absorbed by the atmosphere"]),
   P("they can be sent as a narrow beam to a dish and carry a lot of information", ["narrow beam", "dish", "carry information", "carry a lot of", "directed"])],
  "Microwaves pass easily through the atmosphere and clouds, so they can travel between the ground and satellites in space. They can also be sent as narrow beams to dishes and carry a lot of information.",
  ["What must the signal pass through to reach a satellite?", "Can microwaves do that?", "What else makes them suitable?"],
  "pass through atmosphere; narrow beams to dishes",
  ["Microwaves pass through the atmosphere to the satellite and can be sent in a narrow beam to a dish", "they travel through the atmosphere and clouds"],
  ["Microwaves cannot pass through air", "Satellites cook the signal"], min_points=1)

Q("w10b_light_vs_sound_speed", 2, "10a", "Compare the speed of light in air with the speed of sound in air, and give one everyday observation that shows the difference.",
  [P("light is much faster (about 3 × 10^8 m/s) than sound (about 340 m/s)", ["light is much faster", "light is faster", "3 × 10", "340", "much faster than sound"]),
   P("observation: lightning seen before thunder heard, or a firework seen before the bang", ["lightning", "thunder", "firework", "see before", "bang", "starting pistol"])],
  "Light travels at about 3 × 10⁸ m/s, almost a million times faster than sound (about 340 m/s). That is why we see lightning before we hear the thunder.",
  ["Which arrives first in a storm?", "Compare the two speeds.", "Give an example."],
  "light ≫ sound; lightning before thunder",
  ["Light is much faster than sound, so we see lightning before we hear thunder", "3 × 10⁸ m/s compared with 340 m/s; you see a firework before you hear it"],
  ["Sound is faster than light", "They travel at the same speed"], min_points=2,
  pitfalls=[PF(["sound is faster", "same speed as sound"], "Light is far faster than sound.")])

Q("w10b_sun_cream", 2, "10d", "Explain how sun cream helps to protect the skin.",
  [P("it absorbs (or reflects) ultraviolet radiation", ["absorbs ultraviolet", "absorbs uv", "blocks uv", "reflects uv", "ultraviolet", "uv"]),
   P("so less UV reaches the skin, reducing sunburn and the risk of skin cancer", ["less uv reaches", "sunburn", "skin cancer", "reduces damage", "protects"])],
  "Sun cream absorbs or reflects much of the Sun's ultraviolet radiation, so less UV reaches the skin cells. This reduces sunburn and the risk of skin cancer.",
  ["Which part of sunlight damages skin?", "What does sun cream do to it?", "What is the benefit?"],
  "absorbs/blocks UV → less sunburn and cancer risk",
  ["It absorbs ultraviolet so less reaches the skin, reducing sunburn and skin cancer", "sun cream blocks UV radiation, protecting the skin"],
  ["It cools the skin down", "It blocks radio waves"], min_points=2)

Q("w10b_gamma_hazard", 2, "10d", "Explain why over-exposure to gamma rays is dangerous.",
  [P("gamma rays are ionising", ["ionising", "ionise", "ionization", "ionisation"]),
   P("they damage or kill living cells / damage DNA, causing mutations or cancer", ["damage cells", "kill cells", "dna", "cancer", "mutation", "damage living"])],
  "Gamma rays are ionising radiation. They can damage or kill living cells and damage DNA, which can lead to mutations and cancer.",
  ["What can high-frequency radiation do to atoms?", "What happens to cells?", "State the consequences."],
  "ionising → cell/DNA damage, cancer",
  ["Gamma rays are ionising, so they damage cells and DNA and can cause cancer", "they ionise atoms in cells, killing them or causing mutations"],
  ["They make you too hot", "They are harmless"], min_points=2)

Q("w10b_f_lambda_relation", 2, "10a", "All electromagnetic waves travel at the same speed in a vacuum. Explain how the wavelength of a wave depends on its frequency.",
  [P("speed = frequency × wavelength (v = f λ) with v fixed", ["v = f λ", "speed = frequency × wavelength", "frequency × wavelength", "speed is the same", "constant speed"]),
   P("so a higher frequency means a shorter wavelength (inversely proportional)", ["higher frequency", "shorter wavelength", "inversely proportional", "inversely"])],
  "Since v = f λ and the speed v is the same for all electromagnetic waves, frequency and wavelength are inversely proportional: a higher frequency means a shorter wavelength.",
  ["Write the wave equation.", "Which quantity is fixed?", "What happens to λ if f increases?"],
  "v = f λ, v fixed → higher f, shorter λ",
  ["Since v = f λ and v is the same, a higher frequency means a shorter wavelength", "the wavelength is inversely proportional to the frequency"],
  ["Higher frequency means longer wavelength", "They are not related"], min_points=1,
  pitfalls=[PF(["higher frequency means longer", "longer wavelength", "not related"], "With the speed fixed, a HIGHER frequency means a SHORTER wavelength.")])

# ---------------------------------------------------------------- L3
Q("w10b_thermal_camera", 3, "10c", "Explain how a thermal imaging camera can show a person in complete darkness.",
  [P("the warm person emits infrared radiation", ["emits infrared", "gives out infrared", "infrared radiation", "warm body emits"]),
   P("the camera detects infrared (not visible light)", ["detects infrared", "senses infrared", "infrared camera"]),
   P("warmer objects emit more infrared and show up brighter / different colours", ["warmer", "emit more", "brighter", "different colour", "hotter"])],
  "All warm objects emit infrared radiation, even in the dark. The thermal imaging camera detects infrared rather than visible light. The person is warmer than their surroundings, so they emit more infrared and show up clearly on the image.",
  ["Does a person give out any radiation in the dark?", "What does the camera detect?", "Why does the person stand out?"],
  "warm bodies emit IR; camera detects IR; warmer shows brighter",
  ["The person emits infrared radiation, which the camera detects; being warmer, they show up brighter", "warm bodies give out infrared even in the dark, and the camera senses it"],
  ["The camera uses X-rays", "The person reflects light in the dark"], min_points=2)

Q("w10b_optical_fibre_comms", 3, "10c", "Optical fibres carry internet signals across the world. State which radiation they use and give one advantage over sending signals as electric currents in copper wires.",
  [P("visible light or infrared", ["light", "infrared", "visible"]),
   P("advantage: carry much more information / less signal loss / no electrical interference", ["more information", "more data", "less loss", "interference", "faster", "lighter"])],
  "Optical fibres carry signals as pulses of visible light or infrared. They can carry much more information than copper wires, with less loss of signal and no electrical interference.",
  ["What travels along a glass fibre?", "Which region is used?", "Why is this better than copper?"],
  "light/IR pulses; more information, less loss",
  ["They use infrared or light, which carries more information than copper wires", "pulses of light, with less signal loss and no interference"],
  ["They use gamma rays", "They use sound"], min_points=2)

Q("w10b_lead_apron", 3, "10d", "Explain why a radiographer wears a lead apron or stands behind a lead screen when taking X-ray images.",
  [P("X-rays are ionising and can damage cells / cause cancer", ["ionising", "damage cells", "cancer", "harmful"]),
   P("lead absorbs X-rays", ["lead absorbs", "absorbs x-rays", "blocks x-rays", "stops x-rays"]),
   P("the radiographer works with X-rays every day, so their total exposure must be kept low", ["every day", "many times", "repeated", "total exposure", "kept low", "cumulative"])],
  "X-rays are ionising and can damage cells and cause cancer. Lead absorbs X-rays, so the apron or screen protects the radiographer, who works with X-rays many times every day and must keep their total exposure low.",
  ["Why are X-rays harmful?", "What does lead do to X-rays?", "Why does the radiographer need more protection than the patient?"],
  "X-rays ionising; lead absorbs; repeated exposure",
  ["X-rays are ionising and lead absorbs them, protecting the radiographer who is exposed every day", "lead blocks the X-rays so the radiographer's total exposure stays low"],
  ["Lead makes the X-rays stronger", "The apron keeps the radiographer warm"], min_points=2)

Q("w10b_water_absorbs_microwaves", 3, "10c", "Explain why food containing water heats up in a microwave oven while a dry paper plate stays fairly cool.",
  [P("water molecules absorb microwaves strongly", ["water absorbs", "water molecules absorb", "absorbed by water", "absorbs microwaves"]),
   P("the absorbed energy increases the food's internal store, heating it", ["heats", "heated", "internal energy", "internal store", "vibrate"]),
   P("dry paper contains little water, so absorbs little and is heated only by contact with the hot food", ["little water", "dry", "absorbs little", "does not absorb much", "contact with the food"])],
  "Water molecules absorb microwaves strongly, so the energy goes into the internal store of the food and it heats up. The dry paper plate contains little water, so it absorbs very little microwave energy and only gets warm where it touches the hot food.",
  ["Which substance absorbs microwaves strongly?", "What happens to the absorbed energy?", "Why does the plate stay cool?"],
  "water absorbs microwaves; dry paper absorbs little",
  ["Water in the food absorbs the microwaves and heats up, but the dry plate has little water so it absorbs little", "microwaves are absorbed by water molecules, heating the food; the paper has no water"],
  ["The plate reflects all heat", "Microwaves only heat metal"], min_points=2)

Q("w10b_radio_telescope", 3, "10c", "Astronomers use radio telescopes as well as ordinary light telescopes. Explain why.",
  [P("stars and galaxies emit radio waves as well as light", ["emit radio", "give out radio", "radio waves from space", "radio waves"]),
   P("radio telescopes detect these, giving information that light telescopes cannot", ["detect", "different information", "cannot be seen", "information"]),
   P("radio waves pass through clouds/dust, so can be observed in cloudy weather or through dust clouds", ["through clouds", "through dust", "cloudy", "day and night"])],
  "Stars, galaxies and other objects emit radio waves as well as light. Radio telescopes detect these, revealing objects and information that light telescopes cannot. Radio waves also pass through clouds and dust, so observations can be made in cloudy weather.",
  ["Do objects in space emit only light?", "What extra information do radio waves give?", "What can radio waves pass through?"],
  "objects emit radio waves; extra information; pass through clouds/dust",
  ["Objects in space give out radio waves that radio telescopes can detect, giving different information, and radio waves pass through clouds", "radio telescopes detect radio waves from galaxies that cannot be seen with light"],
  ["Radio telescopes play music from space", "Light cannot travel through space"], min_points=2)

Q("w10b_cloudy_sunburn", 3, "10d", "Explain why you can still get sunburnt on a cloudy day.",
  [P("much of the Sun's ultraviolet radiation passes through clouds", ["passes through clouds", "through the clouds", "uv passes through", "clouds do not block"]),
   P("UV damages skin cells, causing sunburn, even if it does not feel hot", ["damages skin", "sunburn", "does not feel hot", "even if", "not the heat"])],
  "Much of the Sun's ultraviolet radiation passes through clouds, even though clouds block some visible light and make it feel cooler. The UV still reaches the skin and damages skin cells, causing sunburn.",
  ["Does UV pass through clouds?", "Is sunburn caused by heat or by UV?", "Explain."],
  "UV passes through clouds and damages skin",
  ["Ultraviolet radiation passes through clouds and still damages the skin, even if it does not feel hot", "the clouds do not block the UV, which causes sunburn"],
  ["Clouds focus the infrared", "You cannot get sunburnt on cloudy days"], min_points=2)

Q("w10b_gamma_radiotherapy", 3, "10c", "Explain how gamma rays are used to treat cancer, and how damage to healthy tissue is reduced.",
  [P("gamma rays are ionising and kill cells, including cancer cells", ["kill cells", "kill cancer cells", "ionising", "destroy cancer cells"]),
   P("the beam is focused/aimed at the tumour", ["aimed at the tumour", "focused", "directed", "targeted", "aimed"]),
   P("it is rotated / given from several directions so healthy tissue receives a smaller dose", ["several directions", "rotated", "different angles", "smaller dose", "healthy tissue"])],
  "Gamma rays are ionising and kill cells, including cancer cells. The beam is carefully aimed at the tumour and directed from several angles (rotated around the patient), so the tumour receives a large dose while the surrounding healthy tissue receives a much smaller dose.",
  ["What do gamma rays do to cells?", "How is the beam directed?", "How is healthy tissue protected?"],
  "kills cells; aimed at tumour; several angles reduce dose to healthy tissue",
  ["Gamma rays kill cancer cells; the beam is aimed at the tumour from several directions so healthy tissue gets a smaller dose", "the focused gamma beam destroys the tumour while rotating to spare healthy cells"],
  ["Gamma rays heat the tumour until it melts", "Microwaves are used to treat cancer"], min_points=2)

Q("w10b_camera_visible", 3, "10c", "Explain how a digital camera uses visible light to form a picture.",
  [P("light from (or reflected by) the object enters the camera through a lens", ["lens", "enters the camera", "reflected by the object", "light from the object"]),
   P("the lens focuses the light onto a sensor", ["focuses", "onto a sensor", "sensor", "image"]),
   P("the sensor detects the light and records the image", ["detects", "records", "converts", "electrical signal"])],
  "Visible light reflected by (or emitted from) the object enters the camera through a lens. The lens focuses the light to form an image on a light-sensitive sensor, which detects the light and records the picture.",
  ["Where does the light come from?", "What does the lens do?", "What detects the light?"],
  "light from object → lens focuses → sensor records",
  ["Light from the object passes through the lens, which focuses it onto a sensor that records the image", "the lens focuses visible light onto the sensor"],
  ["The camera sends out X-rays", "The camera detects sound"], min_points=2)

Q("w10b_uv_vs_visible_danger", 3, "10d", "Explain why ultraviolet is more harmful to the skin than visible light.",
  [P("ultraviolet has a higher frequency (shorter wavelength) than visible light", ["higher frequency", "shorter wavelength"]),
   P("so it carries more energy and can damage (ionise) skin cells / DNA", ["more energy", "damage", "ionise", "dna", "skin cells"]),
   P("causing sunburn and possibly skin cancer", ["sunburn", "skin cancer", "cancer", "eye damage"])],
  "Ultraviolet has a higher frequency than visible light, so it carries more energy. It can damage skin cells and their DNA, causing sunburn and possibly skin cancer; visible light does not have enough energy to do this.",
  ["Compare the frequencies.", "How is frequency linked to the damage radiation can do?", "What harm does UV cause?"],
  "UV higher frequency → more energy → cell damage",
  ["UV has a higher frequency and more energy than visible light, so it damages skin cells and can cause skin cancer", "the higher frequency of UV means it can damage DNA, causing sunburn"],
  ["Visible light has a higher frequency", "UV is louder"], min_points=2)

Q("w10b_continuous_spectrum", 3, "10b", "Fig. 1 shows the electromagnetic spectrum divided into regions. Explain why the boundaries between regions are not sharp.",
  [P("the spectrum is continuous: wavelength changes gradually", ["continuous", "gradually", "no gaps", "smoothly"]),
   P("the regions are named by their sources/uses, and neighbouring regions overlap", ["overlap", "named", "sources", "uses", "same wavelengths"])],
  "The electromagnetic spectrum is continuous: the wavelength changes gradually from one end to the other with no gaps. The regions are named mainly by how the waves are produced or used, so neighbouring regions overlap and there is no sharp boundary.",
  ["Is there a jump in wavelength between regions?", "How are the regions named?", "Explain."],
  "continuous spectrum; regions overlap",
  ["The spectrum is continuous, so the wavelength changes gradually and neighbouring regions overlap", "there are no gaps; the regions are just named by their uses and overlap"],
  ["There are gaps between the regions", "Each region has exactly one wavelength"], min_points=1, figure=SPEC)

# ---------------------------------------------------------------- L4
Q("w10b_long_lambda_comms", 4, "10c", "Explain why radio waves and microwaves, rather than X-rays or gamma rays, are used for communication.",
  [P("radio waves and microwaves are not ionising, so they are safe at normal intensities", ["not ionising", "safe", "harmless", "do not damage cells"]),
   P("they travel long distances / pass through the atmosphere", ["long distances", "through the atmosphere", "travel far", "through clouds"]),
   P("X-rays and gamma rays are ionising and dangerous (and would be absorbed)", ["x-rays and gamma rays are ionising", "dangerous", "ionising", "harmful", "absorbed"])],
  "Radio waves and microwaves are not ionising, so they are safe at the intensities used. They travel long distances and pass through the atmosphere. X-rays and gamma rays are ionising and would be dangerous to everyone they passed through.",
  ["Which regions are ionising?", "Which regions travel well through the atmosphere?", "Compare their suitability."],
  "radio/microwaves safe, travel far; X/gamma ionising",
  ["Radio waves and microwaves are not ionising and travel long distances, while X-rays and gamma rays are ionising and dangerous", "they are safe and pass through the atmosphere; gamma rays would harm people"],
  ["X-rays are too slow", "Gamma rays cannot carry signals because they are sound"], min_points=2, pitfalls=[NOT_IONISING])

Q("w10b_oven_metal_walls", 4, "10c", "Explain why a microwave oven has metal walls and a metal mesh in its door.",
  [P("metal reflects microwaves", ["reflects microwaves", "metal reflects", "reflect", "bounce off"]),
   P("so the microwaves stay inside the oven (heating the food)", ["stay inside", "kept inside", "do not escape", "trapped inside", "stay in the oven", "stops microwaves escaping", "stops the microwaves escaping"]),
   P("protecting people outside from being heated by them", ["protect", "people outside", "harm", "heating the body", "safe", "do not heat the user", "heat the user"])],
  "Metal reflects microwaves, so the metal walls and the metal mesh in the door keep the microwaves inside the oven, where they heat the food. This protects people outside from internal heating of their body tissue.",
  ["What does metal do to microwaves?", "Where should the microwaves stay?", "Why does this matter for safety?"],
  "metal reflects microwaves → kept inside → protects people",
  ["Metal reflects microwaves, keeping them inside the oven and protecting people outside", "the metal mesh stops microwaves escaping, so they do not heat the user"],
  ["Metal absorbs microwaves to make them stronger", "Metal lets microwaves out"], min_points=2)

Q("w10b_satellite_delay", 4, "10a", "During a live TV interview via satellite, there is a short delay before a reply is heard. Explain why.",
  [P("the signal travels a very long distance to the satellite and back (tens of thousands of km)", ["long distance", "to the satellite and back", "36 000", "thousands of km", "far away"]),
   P("even at the speed of light it takes a noticeable time (time = distance ÷ speed)", ["takes time", "distance ÷ speed", "speed of light", "noticeable time", "fraction of a second"])],
  "The signal travels tens of thousands of kilometres up to the satellite and back down. Even at the speed of light, 3 × 10⁸ m/s, this takes a noticeable fraction of a second (time = distance ÷ speed), causing the delay.",
  ["How far does the signal travel?", "How fast does it travel?", "Use time = distance ÷ speed."],
  "very long path; time = distance ÷ speed is noticeable",
  ["The signal travels a very long distance to the satellite and back, so even at the speed of light it takes a noticeable time", "time = distance ÷ speed, and the distance is tens of thousands of km"],
  ["The satellite is slow", "Microwaves travel at the speed of sound"], min_points=2)

Q("w10b_xray_short_exposure", 4, "10d", "Hospitals keep each X-ray exposure as short as possible and avoid unnecessary X-rays. Explain why.",
  [P("X-rays are ionising and can damage cells/DNA", ["ionising", "damage cells", "dna", "harmful"]),
   P("the risk of harm (e.g. cancer) increases with the total dose received", ["dose", "total exposure", "risk increases", "cumulative", "more exposure"]),
   P("so the benefit of each image must outweigh the risk; short exposures keep the dose low", ["benefit", "outweigh", "keep the dose low", "minimise", "as low as possible"])],
  "X-rays are ionising and can damage cells and DNA. The risk of harm, such as cancer, increases with the total dose received, so each exposure is kept short to keep the dose low, and X-rays are only taken when the benefit outweighs the risk.",
  ["What can X-rays do to cells?", "How does the risk depend on the dose?", "Why avoid unnecessary images?"],
  "ionising; risk rises with dose; keep dose low",
  ["X-rays are ionising, and the risk of cancer increases with the total dose, so exposures are kept short", "short exposures keep the dose low because X-rays damage cells"],
  ["X-rays use too much electricity", "Long exposures give clearer pictures with no risk"], min_points=2)

Q("w10b_uv_sterilise_water", 4, "10c", "Ultraviolet lamps are used to sterilise drinking water. Explain how this works and why the lamps are enclosed.",
  [P("ultraviolet damages/kills bacteria and viruses (damages their DNA)", ["kills bacteria", "kills germs", "kills microbes", "damages dna", "destroys bacteria"]),
   P("the water flows past the lamp so the microorganisms receive the UV", ["flows past", "passes the lamp", "exposed", "receive the uv"]),
   P("the lamps are enclosed because UV would also harm people's skin and eyes", ["harm people", "eyes", "skin", "protect people", "dangerous to people", "shielded", "must be shielded"])],
  "Ultraviolet radiation damages the DNA of bacteria and viruses, killing them. Water flows past the UV lamp so that any microorganisms receive a strong dose. The lamps are enclosed because UV would also damage people's skin and eyes.",
  ["What does UV do to microorganisms?", "How is the water exposed?", "Why must people be shielded?"],
  "UV kills microbes; water flows past; enclosed to protect people",
  ["UV kills bacteria in the water as it flows past, and the lamps are enclosed because UV harms skin and eyes", "ultraviolet damages the DNA of microbes; people must be shielded from it"],
  ["UV heats the water to boiling", "UV adds chlorine"], min_points=2)

Q("w10b_pir_alarm", 4, "10c", "Explain how an infrared intruder alarm (PIR sensor) detects a person entering a room.",
  [P("a person's warm body emits infrared radiation", ["emits infrared", "gives out infrared", "warm body", "body heat"]),
   P("the sensor detects the change in infrared when the person moves into view", ["detects", "change in infrared", "moves", "sensor"]),
   P("which triggers the alarm", ["triggers", "sets off", "alarm sounds", "switches on"])],
  "A person's warm body emits infrared radiation. When they move into the room, the sensor detects the change in the infrared reaching it and triggers the alarm.",
  ["What does a warm body give out?", "What does the sensor respond to?", "What happens then?"],
  "body emits IR; sensor detects change; alarm",
  ["The person's body emits infrared and the sensor detects the change when they move, triggering the alarm", "the PIR sensor picks up infrared from a warm body and sets off the alarm"],
  ["The sensor detects X-rays from the intruder", "It detects the sound of footsteps only"], min_points=2)

Q("w10b_gamma_vs_xray", 4, "10d", "Gamma rays and X-rays overlap in wavelength. State two ways in which they are similar and one way in which they differ.",
  [P("both are ionising / harmful to cells", ["both are ionising", "ionising", "harmful", "damage cells"]),
   P("both are highly penetrating electromagnetic waves (same speed)", ["penetrating", "electromagnetic", "same speed", "pass through the body"]),
   P("they differ in source: gamma rays come from nuclei; X-rays from X-ray tubes (electrons)", ["nucleus", "nuclei", "radioactive", "x-ray tube", "source", "electrons"])],
  "Both are ionising and harmful to living cells, and both are highly penetrating electromagnetic waves that travel at the same speed. They differ in their source: gamma rays come from unstable nuclei (radioactive decay), whereas X-rays are produced in X-ray tubes by fast electrons.",
  ["What do they have in common in terms of danger?", "And in terms of penetration?", "Where does each come from?"],
  "both ionising and penetrating; gamma from nuclei, X-rays from tubes",
  ["Both are ionising and penetrating, but gamma rays come from radioactive nuclei while X-rays come from X-ray tubes", "they are both harmful EM waves that pass through the body; their sources differ"],
  ["They are completely different types of wave", "X-rays are sound waves"], min_points=2)

Q("w10b_wifi_safety", 4, "10d", "Wi-Fi routers emit microwaves. Explain why they are considered safe in homes.",
  [P("microwaves are not ionising (low frequency)", ["not ionising", "non-ionising", "low frequency"]),
   P("their main effect is heating, and Wi-Fi routers emit very low power", ["low power", "low intensity", "very weak", "heating"]),
   P("so any heating of body tissue is negligible", ["negligible", "very small", "tiny", "not enough to heat"])],
  "Microwaves are not ionising, so they cannot damage DNA in the way that UV, X-rays or gamma rays can. Their main effect on the body is heating, and a Wi-Fi router emits very low power, so any heating of body tissue is negligible.",
  ["Are microwaves ionising?", "What is their main effect on tissue?", "How powerful is a router?"],
  "not ionising; low power → negligible heating",
  ["Microwaves are not ionising and the router's power is very low, so the heating is negligible", "Wi-Fi is low intensity microwaves, which only cause tiny heating"],
  ["Wi-Fi uses gamma rays", "Microwaves are ionising but blocked by walls"], min_points=2, pitfalls=[NOT_IONISING])

Q("w10b_light_vs_radio_same_speed", 4, "10a", "A radio station broadcasts at 100 MHz and a red light has a frequency of about 4.5 × 10^14 Hz. Explain how their speeds and wavelengths compare in a vacuum.",
  [P("they travel at the same speed (3 × 10^8 m/s)", ["same speed", "3 × 10", "speed of light", "both travel"]),
   P("the radio wave has a much longer wavelength because its frequency is much lower (v = f λ)", ["longer wavelength", "radio wave has a longer", "lower frequency", "v = f λ", "much longer"])],
  "Both are electromagnetic waves, so they travel at the same speed in a vacuum, 3 × 10⁸ m/s. Since v = f λ, the radio wave, with a much lower frequency, has a much longer wavelength (about 3 m, compared with about 670 nm for red light).",
  ["What is the speed of all EM waves in a vacuum?", "Use v = f λ.", "Which has the longer wavelength?"],
  "same speed; radio: lower f → longer λ",
  ["They travel at the same speed, so the radio wave has a much longer wavelength because its frequency is lower", "same speed of light; v = fλ means the radio wave's wavelength is much longer"],
  ["Light is faster because it has a higher frequency", "The radio wave has the shorter wavelength"], min_points=2)

Q("w10b_dose_distance", 4, "10d", "Explain two ways in which hospital staff reduce their exposure to ionising radiation such as X-rays.",
  [P("shielding: lead screens or aprons absorb the radiation", ["lead", "shield", "screen", "apron", "absorbs"]),
   P("distance: standing further away (or leaving the room)", ["distance", "further away", "leave the room", "stand away"]),
   P("time: keeping exposure time short / monitoring with badges", ["short time", "time", "badge", "monitor", "dosimeter"])],
  "Staff reduce their exposure by shielding (standing behind lead screens or wearing lead aprons, which absorb the radiation), by distance (standing well away or leaving the room during exposure), and by time (keeping exposures short and wearing badges to monitor their dose).",
  ["What material absorbs X-rays?", "How does distance help?", "How does time help?"],
  "shielding, distance, time",
  ["They stand behind lead screens that absorb X-rays and keep their distance from the machine", "lead aprons, standing further away and keeping exposure times short"],
  ["They wear sunglasses", "They drink water"], min_points=2)

# ---------------------------------------------------------------- L5
Q("w10b_phone_mast_claim", 5, "10d", "A resident says: 'The microwaves from the new mobile phone mast will cause cancer, just like X-rays.' Evaluate this claim.",
  [P("microwaves are not ionising, unlike X-rays", ["not ionising", "unlike x-rays", "x-rays are ionising", "non-ionising"]),
   P("so they cannot damage DNA directly in the way X-rays do; their effect is heating", ["heating", "cannot damage dna", "do not damage dna", "only heat"]),
   P("the intensity from a mast at a distance is very low, so heating is negligible", ["low intensity", "very low", "far away", "negligible", "weak"])],
  "The claim is not justified. Unlike X-rays, microwaves are not ionising, so they cannot damage DNA directly; their main effect on the body is heating. The intensity of microwaves from a mast, at the distance of a home, is very low, so any heating is negligible.",
  ["Are microwaves ionising like X-rays?", "What is their effect on tissue?", "How strong is the radiation at a distance?"],
  "microwaves not ionising; heating only; very low intensity",
  ["Not justified: microwaves are not ionising like X-rays, so they only cause heating, and the intensity from a mast is very low", "unlike X-rays, microwaves cannot damage DNA; the mast's signal is weak at a distance"],
  ["Correct, all EM waves cause cancer", "Correct, microwaves are ionising"], min_points=2, pitfalls=[NOT_IONISING])

Q("w10b_sunscreen_claim", 5, "10d", "A student says: 'Sunscreen blocks all of the Sun's radiation.' Evaluate this claim.",
  [P("wrong: sunscreen mainly absorbs/blocks ultraviolet", ["wrong", "mainly ultraviolet", "only ultraviolet", "blocks uv", "absorbs uv"]),
   P("visible light and infrared still reach the skin (you still see and feel warm)", ["visible light", "infrared", "still feel warm", "still see", "still reaches"]),
   P("and no sunscreen blocks all UV, so exposure should still be limited", ["not all", "some uv", "still limit", "reduce exposure", "not complete"])],
  "The claim is wrong. Sunscreen mainly absorbs or blocks ultraviolet radiation; visible light and infrared still reach the skin, which is why you can still see and feel warm. Even for UV it does not block everything, so exposure should still be limited.",
  ["Which part of sunlight is sunscreen designed for?", "Do you still feel warm with sunscreen on?", "Does it block all UV?"],
  "wrong; mainly UV; visible and IR pass; not all UV blocked",
  ["Wrong: sunscreen mainly blocks ultraviolet; visible light and infrared still reach the skin, and some UV still gets through", "it only blocks UV, and not all of it, so infrared and light still reach you"],
  ["Correct, sunscreen blocks everything", "Correct, it blocks radio waves too"], min_points=2)

Q("w10b_uv_beads_test", 5, "10d", "UV-sensitive beads change colour in ultraviolet light. Design an experiment using them to compare how well two brands of sunglasses block UV.",
  [P("place beads under each pair of sunglasses (and some uncovered as a control) in the same UV source / sunlight", ["beads under", "cover the beads", "control", "uncovered", "same uv source", "same sunlight"]),
   P("same exposure time and distance for each", ["same time", "same distance", "same exposure", "fair test", "same conditions"]),
   P("compare the colour change: less change means better UV blocking", ["compare the colour", "less colour change", "colour change", "better blocking", "less change"])],
  "Put some beads under each pair of sunglasses and leave some uncovered as a control. Expose them all to the same UV source (or sunlight) for the same time and at the same distance. Compare the colour change: beads that change least are behind the sunglasses that block UV best.",
  ["How can the beads show how much UV gets through?", "What must be kept the same?", "How do you compare the results?"],
  "beads behind each lens + control; same exposure; compare colour change",
  ["Put beads under each pair of sunglasses and some uncovered, expose them to the same UV for the same time, and compare the colour change; the least change is the best", "use the beads as detectors under each lens with a control and compare how much they change colour"],
  ["Weigh the sunglasses", "Look at the price of each brand"], min_points=2)

Q("w10b_choose_region_jobs", 5, "10c", "Choose a suitable region of the electromagnetic spectrum for each job and justify it: (a) sterilising sealed packs of syringes, (b) detecting a person in smoke, (c) sending signals to a satellite.",
  [P("(a) gamma rays: penetrate the sealed packaging and kill bacteria", ["gamma"]),
   P("(b) infrared: warm bodies emit infrared that passes through smoke (thermal imaging)", ["infrared", "thermal imaging"]),
   P("(c) microwaves: pass through the atmosphere", ["microwave"])],
  "(a) Gamma rays, because they penetrate the sealed packaging and kill any bacteria. (b) Infrared, because a warm body emits infrared, which passes through smoke and can be detected by a thermal imaging camera. (c) Microwaves, because they pass through the atmosphere to and from the satellite.",
  ["Which radiation kills bacteria through packaging?", "What do warm bodies emit?", "Which region is used for satellite links?"],
  "gamma; infrared; microwaves",
  ["Gamma rays for sterilising, infrared for finding people in smoke, microwaves for satellites", "(a) gamma, (b) thermal imaging with infrared, (c) microwaves through the atmosphere"],
  ["Radio waves for all three", "Visible light for sterilising"], min_points=3)

Q("w10b_patient_vs_staff", 5, "10d", "A patient has a single X-ray, while the radiographer is shielded every time. Evaluate why the precautions differ.",
  [P("for the patient, one short exposure gives a small dose, and the medical benefit outweighs the small risk", ["one exposure", "small dose", "benefit", "outweighs", "single"]),
   P("the radiographer would be exposed many times every day, so their total dose would build up", ["many times", "every day", "build up", "total dose", "repeated"]),
   P("so staff use shielding (lead), distance and time limits to keep their cumulative dose low", ["shielding", "lead", "distance", "keep the dose low", "cumulative"])],
  "For the patient, one short X-ray gives a small dose, and the medical benefit of the image outweighs the small risk. The radiographer would be exposed many times a day, every working day, so the total dose would build up; therefore staff use lead shielding, distance and short exposure times to keep their cumulative dose low.",
  ["How often is each person exposed?", "How does the total dose build up?", "What is the benefit to each?"],
  "patient: one small dose with benefit; staff: repeated exposure → cumulative dose",
  ["The patient has one small dose with a medical benefit, but the radiographer would be exposed many times a day so their total dose would build up; so they use lead shielding", "repeated exposure for staff adds up, so they shield themselves; the patient's single dose is small"],
  ["Patients are not affected by X-rays", "Radiographers are immune to X-rays"], min_points=2)

Q("w10b_xray_telescopes_space", 5, "10b", "X-ray telescopes are placed on satellites in space rather than on the ground. Evaluate why.",
  [P("the Earth's atmosphere absorbs X-rays from space", ["atmosphere absorbs", "absorbed by the atmosphere", "do not reach the ground", "blocked by the atmosphere"]),
   P("so X-rays from stars and galaxies cannot be detected on the ground", ["cannot be detected", "would not reach", "cannot reach", "not detected on the ground"]),
   P("above the atmosphere, the telescope can detect them (this also protects us on the ground)", ["above the atmosphere", "in space", "protects us", "can detect"])],
  "The Earth's atmosphere absorbs X-rays coming from space, so they never reach the ground and could not be detected there. A telescope on a satellite above the atmosphere can detect them. The same absorption protects life on Earth from these ionising rays.",
  ["Do X-rays from space reach the ground?", "What absorbs them?", "Where must the telescope be?"],
  "atmosphere absorbs X-rays → telescopes above it",
  ["The atmosphere absorbs X-rays, so they cannot reach the ground; telescopes in space above the atmosphere can detect them", "X-rays from space are blocked by the atmosphere, so the telescope must be in orbit"],
  ["Space is closer to the stars", "X-rays travel faster in space"], min_points=2)

Q("w10b_rank_hazard", 5, "10d", "Rank radio waves, ultraviolet and gamma rays from least to most hazardous to the human body, and justify your ranking.",
  [P("radio waves least hazardous: low frequency, not ionising", ["radio waves least", "radio", "not ionising", "low frequency"]),
   P("ultraviolet more hazardous: damages skin cells (sunburn, skin cancer)", ["ultraviolet", "skin", "sunburn"]),
   P("gamma most hazardous: highest frequency, very penetrating and ionising, damages cells throughout the body", ["gamma most", "gamma", "most hazardous", "penetrating", "highest frequency"])],
  "Least to most hazardous: radio waves, ultraviolet, gamma rays. Radio waves have a low frequency and are not ionising. Ultraviolet has a higher frequency and can damage skin cells, causing sunburn and skin cancer, but it is absorbed by the skin. Gamma rays have the highest frequency, are ionising and very penetrating, so they damage cells throughout the body.",
  ["How does hazard relate to frequency?", "Which can penetrate deep into the body?", "Rank and justify."],
  "radio < UV < gamma; frequency, ionisation, penetration",
  ["Radio waves are least hazardous as they are not ionising, ultraviolet damages the skin, and gamma rays are most hazardous because they are ionising and penetrating", "radio, then UV, then gamma, in order of increasing frequency and damage"],
  ["Radio waves are the most dangerous", "All three are equally hazardous"], min_points=2)

Q("w10b_infrared_is_heat_claim", 5, "10a", "A student says: 'Infrared radiation IS heat.' Evaluate this statement.",
  [P("not quite: infrared is electromagnetic radiation (a transverse wave travelling at 3 × 10^8 m/s)", ["electromagnetic", "em radiation", "wave", "not quite", "not exactly"]),
   P("it transfers energy by radiation; when absorbed it increases the internal energy of the absorber, which we feel as warmth", ["transfers energy", "absorbed", "internal energy", "heating", "warms"]),
   P("hot objects emit a lot of infrared, which is why the two are linked", ["hot objects emit", "emitted by hot", "warm objects", "linked"])],
  "The statement is not quite right. Infrared is electromagnetic radiation, a transverse wave travelling at 3 × 10⁸ m/s. It transfers energy by radiation; when it is absorbed it increases the internal energy of the absorber, which we feel as warmth. They are linked because hot objects emit a lot of infrared.",
  ["What kind of wave is infrared?", "What happens when it is absorbed?", "Why are infrared and heat often confused?"],
  "IR is EM radiation transferring energy; absorption causes heating",
  ["Not quite: infrared is electromagnetic radiation that transfers energy, and when it is absorbed it heats the object, which is why hot objects and infrared are linked", "infrared is an EM wave; it causes heating when absorbed"],
  ["Correct, infrared is a type of heat particle", "Infrared is a sound wave"], min_points=2, pitfalls=[LONGITUDINAL])

Q("w10b_radio_through_walls", 5, "10c", "Radio signals can be received inside a house, but you cannot see through the walls. Evaluate what this shows about how different EM waves interact with materials.",
  [P("radio waves pass through walls (are not absorbed much)", ["radio waves pass through", "pass through walls", "go through walls", "not absorbed"]),
   P("visible light is absorbed or reflected by walls", ["light is absorbed", "light is reflected", "absorbed or reflected", "blocked"]),
   P("different regions interact differently with the same material (depends on wavelength/frequency)", ["different regions", "depends on wavelength", "depends on frequency", "interact differently", "different wavelengths"])],
  "It shows that different regions of the spectrum interact with materials differently. Radio waves, with long wavelengths, pass through brick walls without much absorption, whereas visible light is absorbed or reflected by the wall. How a material affects an EM wave depends on the wave's wavelength (frequency).",
  ["What happens to radio waves at the wall?", "What happens to visible light?", "What general idea does this show?"],
  "radio passes through, light absorbed/reflected; depends on wavelength",
  ["Radio waves pass through the walls but visible light is absorbed or reflected, so different wavelengths interact differently with materials", "walls block light but not radio, showing it depends on the frequency"],
  ["Radio waves are faster than light", "Walls are transparent to everything"], min_points=2)

Q("w10b_rescue_thermal_camera", 5, "10c", "Explain how rescue teams could use a thermal imaging camera to find survivors in collapsed buildings at night, and one limitation.",
  [P("survivors' warm bodies emit infrared radiation", ["emit infrared", "give out infrared", "warm bodies", "body heat", "infrared from survivors"]),
   P("the camera detects infrared, so it works in darkness and through smoke/dust", ["detects infrared", "picks up infrared", "darkness", "in the dark", "smoke", "dust", "at night"]),
   P("limitation: infrared cannot pass through thick rubble/walls; a warm object may be mistaken for a person", ["cannot pass through", "rubble", "walls", "mistaken", "other warm objects", "limitation"])],
  "Survivors' warm bodies emit infrared radiation. A thermal imaging camera detects infrared, not visible light, so it works in darkness and through smoke and dust, showing people as warmer areas. A limitation is that infrared cannot pass through thick rubble or walls, so buried people may not be seen, and other warm objects can be mistaken for people.",
  ["What do survivors emit?", "Why does the camera work at night?", "What can block infrared?"],
  "bodies emit IR; camera detects in dark/smoke; cannot see through rubble",
  ["Warm bodies emit infrared, which the camera detects even at night and through smoke, but it cannot see through thick rubble", "the camera picks up infrared from survivors in the dark; a limitation is that walls block infrared"],
  ["The camera uses X-rays to see through rubble", "It listens for voices"], min_points=2)
