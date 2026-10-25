"""Chapter 9 General Wave Properties: 50 more written-answer questions (10 per level), marked by keywords/phrases."""
from .. import sketches
from ..marker import Pitfall, Point
from .base import written

P = Point
PF = Pitfall
CH = 9


def Q(id, lv, lo, stem, points, model, hints, keywords, passes, fails, pitfalls=(), min_points=None, figure=None):
    written(id, CH, lv, lo, stem=stem, points=points, model_answer=model, hints=hints, keywords=keywords,
            pitfalls=pitfalls, min_points=min_points, figure=figure, sample_pass=passes, sample_fail=fails)


MATTER = PF(["carries the water along", "transfers matter", "carries the rope along", "water moves along with", "moves the matter"],
            "Waves transfer energy, not matter; the particles only vibrate about fixed positions.")
LOUD_PITCH = PF(["louder means higher pitch", "higher pitch means louder", "amplitude decides the pitch", "frequency decides the loudness"],
                "Loudness depends on amplitude; pitch depends on frequency.")

# ---------------------------------------------------------------- L1
Q("w9b_define_period", 1, "9c", "Fig. 1 shows the displacement–time graph of a particle in a wave. Define the period of a wave and state its unit.",
  [P("the time taken for one complete oscillation (or for one wave to pass a point)", ["time for one complete", "time taken for one", "one complete oscillation", "one complete wave", "one oscillation", "one cycle"]),
   P("unit: second (s)", ["second", "seconds"])],
  "The period is the time taken for one complete oscillation of a particle (or for one complete wave to pass a point). It is measured in seconds.",
  ["Period is a time.", "How much of the motion does it cover?", "Give the unit."],
  "time for one complete oscillation; seconds",
  ["The time taken for one complete oscillation, in seconds", "the time for one complete wave to pass, measured in seconds"],
  ["The number of waves per second, in hertz", "The distance between two crests"], min_points=2,
  figure=lambda: sketches.wave_graph(2, 0.5, kind="time", cycles=2))

Q("w9b_define_wave_speed", 1, "9c", "State what is meant by the speed of a wave.",
  [P("the distance travelled by a wavefront (crest) per unit time", ["distance travelled per second", "distance per unit time", "distance a wavefront travels", "distance moved by a crest", "how far the wave travels per second", "distance per second", "how far a crest moves", "per unit time"])],
  "The speed of a wave is the distance travelled by a wavefront (for example a crest) per unit time.",
  ["Speed is distance ÷ time.", "What part of the wave do you follow?", "Define it."],
  "distance travelled by a wavefront per second",
  ["The distance travelled by a wavefront per second", "how far a crest moves per unit time"],
  ["The number of waves per second", "The height of the wave"],
  pitfalls=[PF(["number of waves per second", "waves per second"], "That is the frequency, not the speed.")])

Q("w9b_wave_equation_state", 1, "9d", "State the equation linking wave speed, frequency and wavelength, with the unit of each.",
  [P("v = f λ (wave speed = frequency × wavelength)", ["v = f λ", "v = fλ", "speed = frequency × wavelength", "frequency × wavelength", "frequency times wavelength", "v = f × λ"]),
   P("v in m/s, f in Hz, λ in m", ["m/s", "hz", "hertz", "metres"])],
  "Wave speed = frequency × wavelength, v = f λ, where v is in m/s, f in Hz and λ in m.",
  ["Three quantities are linked by multiplication.", "Check the units: Hz × m = m/s.", "State the equation and units."],
  "v = f λ; m/s, Hz, m",
  ["v = f λ, with speed in m/s, frequency in Hz and wavelength in m", "speed = frequency × wavelength"],
  ["v = f ÷ λ", "v = λ ÷ f"], min_points=1,
  pitfalls=[PF(["v = f / λ", "f ÷ λ", "λ ÷ f"], "The wave equation is v = f × λ.")])

Q("w9b_transverse_examples", 1, "9e", "Give two examples of transverse waves.",
  [P("light / electromagnetic waves", ["light", "electromagnetic", "radio", "microwave", "x-ray", "em wave"]),
   P("water (surface) waves / waves on a rope or string", ["water wave", "ripples", "rope", "string", "water waves", "surface waves"])],
  "Light (and all electromagnetic waves) and water ripples are transverse waves; so is a wave sent along a rope by moving its end up and down.",
  ["In a transverse wave the vibrations are at right angles to the direction of travel.", "Think of light and of waves on water.", "Give two."],
  "light/EM waves; water waves; waves on a rope",
  ["Light and water waves", "radio waves and a wave on a rope"],
  ["Sound and ultrasound", "Compression waves on a slinky"], min_points=2,
  pitfalls=[PF(["sound is transverse", "sound and"], "Sound is a LONGITUDINAL wave.")])

Q("w9b_longitudinal_example", 1, "9e", "Give an example of a longitudinal wave and state how its particles vibrate.",
  [P("sound (or a push–pull wave on a slinky)", ["sound", "slinky", "push and pull", "compression wave"]),
   P("particles vibrate parallel to (back and forth along) the direction of travel", ["parallel", "back and forth", "same direction", "along the direction", "backwards and forwards"])],
  "Sound is a longitudinal wave (as is a push–pull wave on a slinky spring). Its particles vibrate back and forth, parallel to the direction in which the wave travels.",
  ["Which everyday wave has compressions and rarefactions?", "Which way do its particles move?", "Give both."],
  "sound; vibrations parallel to direction of travel",
  ["Sound, where particles vibrate parallel to the direction of travel", "a slinky pushed and pulled; the coils move back and forth along the wave"],
  ["Light, vibrating up and down", "Water waves"], min_points=2)

Q("w9b_echo_def", 1, "9i", "State what an echo is.",
  [P("a sound that has been reflected (from a hard surface)", ["reflected", "reflection", "bounces off", "bounced back", "reflected sound"])],
  "An echo is a sound that has been reflected from a hard surface, such as a wall or cliff, and heard after the original sound.",
  ["You shout towards a cliff and hear your voice again.", "What happened to the sound at the cliff?", "Define it."],
  "reflected sound",
  ["A sound that has been reflected", "sound that bounces back off a wall"],
  ["A louder version of the sound", "Sound that is absorbed"])

Q("w9b_crest_trough", 1, "9c", "Fig. 1 shows a transverse wave. State what is meant by a crest and a trough.",
  [P("a crest is a highest point of the wave (maximum displacement upwards)", ["crest is the highest", "highest point", "top of the wave", "peak", "maximum displacement upwards"]),
   P("a trough is a lowest point (maximum displacement downwards)", ["trough is the lowest", "lowest point", "bottom of the wave", "maximum displacement downwards"])],
  "A crest is a highest point of a transverse wave (maximum upward displacement); a trough is a lowest point (maximum downward displacement).",
  ["Look at the top and bottom of the wave.", "Which is the crest, which the trough?", "Define both."],
  "crest = highest point; trough = lowest point",
  ["A crest is a highest point and a trough is a lowest point of the wave", "the peak of the wave and the bottom of the wave"],
  ["A crest is the middle of the wave", "A trough is the start of the wave"], min_points=2,
  figure=lambda: sketches.wave_graph(2, 4, kind="distance", cycles=2))

Q("w9b_sound_source", 1, "9f", "State how sounds are produced, giving an example.",
  [P("by vibrating objects (sources)", ["vibrating", "vibration", "vibrates", "vibrate"]),
   P("example: guitar string, loudspeaker cone, drum skin, vocal cords, tuning fork", ["guitar string", "string", "loudspeaker", "drum", "vocal cords", "tuning fork", "speaker"])],
  "Sounds are produced by vibrating objects, for example a plucked guitar string, a loudspeaker cone or a drum skin.",
  ["What do all sound sources have in common?", "Think of a guitar or a drum.", "State and give an example."],
  "vibrating source; e.g. guitar string",
  ["By vibrating objects such as a guitar string", "a drum skin vibrates to make sound"],
  ["By light shining on objects", "By heating air"], min_points=2)

Q("w9b_sound_media", 1, "9f", "State whether sound can travel through (a) solids, (b) liquids, (c) gases and (d) a vacuum.",
  [P("it can travel through solids, liquids and gases (any medium)", ["solids, liquids and gases", "solids liquids and gases", "all three", "any medium", "through solids", "through liquids"]),
   P("it cannot travel through a vacuum", ["not through a vacuum", "cannot travel through a vacuum", "not a vacuum", "no sound in a vacuum", "cannot pass through a vacuum"])],
  "Sound can travel through solids, liquids and gases, because they all contain particles that can pass on vibrations, but it cannot travel through a vacuum.",
  ["Sound needs particles to pass on vibrations.", "Which of the four has no particles?", "Answer all four."],
  "yes: solids, liquids, gases; no: vacuum",
  ["It can travel through solids, liquids and gases but not through a vacuum", "sound cannot travel through a vacuum, but it travels through all three states"],
  ["Only through air", "Through a vacuum but not through solids"], min_points=2)

Q("w9b_units_lambda_amp", 1, "9c", "State the SI units of wavelength, amplitude and frequency.",
  [P("wavelength and amplitude: metres (m)", ["metre", "metres", "m"]),
   P("frequency: hertz (Hz)", ["hertz", "hz"])],
  "Wavelength and amplitude are both lengths, measured in metres (m); frequency is measured in hertz (Hz).",
  ["Wavelength and amplitude are both distances.", "Frequency counts waves per second.", "Give the units."],
  "m, m, Hz",
  ["Wavelength and amplitude in metres, frequency in hertz", "m for both lengths and Hz for frequency"],
  ["All in seconds", "Wavelength in Hz"], min_points=2)

# ---------------------------------------------------------------- L2
Q("w9b_slinky_two_ways", 2, "9e", "Describe how to send (a) a transverse wave and (b) a longitudinal wave along a stretched slinky spring.",
  [P("transverse: move the end from side to side (at right angles to the slinky)", ["side to side", "up and down", "at right angles", "perpendicular"]),
   P("longitudinal: push and pull the end back and forth along the slinky", ["push and pull", "back and forth", "along the slinky", "in and out", "backwards and forwards"])],
  "(a) Move the end of the slinky from side to side, at right angles to its length, to send a transverse wave. (b) Push and pull the end back and forth along the length of the slinky to send a longitudinal wave of compressions and rarefactions.",
  ["How should your hand move for each type of wave?", "Compare with the direction the wave travels.", "Describe both."],
  "transverse: side to side; longitudinal: push–pull along",
  ["Move the end side to side for a transverse wave, and push and pull it along the slinky for a longitudinal wave", "up and down gives transverse; back and forth gives longitudinal"],
  ["Shake it harder for longitudinal", "Both are made by twisting it"], min_points=2)

Q("w9b_rope_particles", 2, "9b", "A wave travels along a rope. Describe how a marked point on the rope moves, and what the wave transfers.",
  [P("the point moves up and down (vibrates about its rest position)", ["up and down", "vibrates", "oscillates", "about its rest position", "side to side"]),
   P("it does not move along with the wave", ["does not move along", "stays in the same place", "not carried along", "not move forward"]),
   P("the wave transfers energy along the rope", ["transfers energy", "energy", "carries energy"])],
  "The marked point moves up and down about its rest position; it does not travel along the rope with the wave. The wave transfers energy along the rope, not the rope itself.",
  ["Which way does the marked point move?", "Does it travel along the rope?", "What does the wave carry?"],
  "point vibrates up and down; no movement along; energy transferred",
  ["The point moves up and down but does not move along the rope; the wave transfers energy", "it vibrates about its rest position while energy travels along the rope"],
  ["The point travels along the rope with the wave", "The rope is carried to the other end"], min_points=2, pitfalls=[MATTER])

Q("w9b_read_period_graph", 2, "9c", "Fig. 1 shows a displacement–time graph for a particle in a wave. Explain how to find the period and the frequency from it.",
  [P("period = time for one complete cycle (e.g. crest to next crest) read from the time axis", ["time for one complete", "crest to crest", "one cycle", "one complete wave", "read the time"]),
   P("frequency = 1 ÷ period", ["1 ÷ period", "1 / t", "1/t", "1 ÷ t", "one over the period", "f = 1 / t", "reciprocal"])],
  "The period is the time for one complete cycle, for example from one crest to the next, read from the time axis. The frequency is then 1 ÷ period.",
  ["Find two neighbouring crests on the time axis.", "What is the time between them?", "How is frequency related to period?"],
  "period from crest-to-crest time; f = 1 ÷ T",
  ["Read the time from one crest to the next to get the period, then the frequency is 1 ÷ period", "find the time for one cycle; f = 1/T"],
  ["The period is the height of the crest", "The frequency is the distance between crests"], min_points=2,
  figure=lambda: sketches.wave_graph(2, 0.2, kind="time", cycles=3))

Q("w9b_dipper_faster", 2, "9d", "Fig. 1 shows wavefronts in a ripple tank. The dipper's frequency is increased. Explain what happens to the spacing of the wavefronts.",
  [P("the wavefronts become closer together (shorter wavelength)", ["closer together", "shorter wavelength", "wavelength decreases", "closer", "smaller wavelength"]),
   P("because the speed is unchanged (same water depth), and v = f λ", ["speed is unchanged", "same speed", "v = f λ", "v = fλ", "speed stays the same"])],
  "The wavefronts become closer together. The speed of the waves depends on the water and stays the same, so by v = f λ, a higher frequency gives a shorter wavelength.",
  ["Does the wave speed change if only the dipper changes?", "Use v = f λ.", "What happens to λ when f increases?"],
  "closer wavefronts (shorter λ); v unchanged",
  ["The wavefronts get closer together because the speed is the same, so a higher frequency gives a shorter wavelength", "wavelength decreases since v = fλ and v stays the same"],
  ["The wavefronts spread further apart", "The waves travel faster"], min_points=2,
  figure=lambda: sketches.wavefronts_sketch(6, ""))

Q("w9b_amplitude_energy", 2, "9c", "Two waves on the sea have the same wavelength, but one has a much larger amplitude. Explain which carries more energy.",
  [P("the wave with the larger amplitude", ["larger amplitude", "bigger amplitude", "higher amplitude", "taller wave"]),
   P("a larger amplitude means the particles vibrate with larger displacement, carrying more energy", ["more energy", "larger displacement", "vibrate more", "greater energy"])],
  "The wave with the larger amplitude carries more energy: its particles vibrate with a larger displacement, which requires and transfers more energy.",
  ["What does amplitude measure?", "How is it linked to energy?", "Which wave?"],
  "larger amplitude → more energy",
  ["The wave with the larger amplitude carries more energy because the water vibrates more", "the bigger amplitude wave transfers more energy"],
  ["The smaller wave, because it is faster", "They carry the same energy"], min_points=2)

Q("w9b_sound_through_table", 2, "9f", "A student puts her ear to a table while a friend taps the far end. She hears the tap clearly. Explain what this shows.",
  [P("sound can travel through solids", ["through solids", "through a solid", "through the table", "solids carry sound", "travels through the wood", "carries the sound"]),
   P("the vibrations are passed on from particle to particle in the table", ["vibrations", "passed on", "particle to particle", "particles vibrate", "close together"])],
  "It shows that sound can travel through solids: the tap makes the table's particles vibrate, and the vibrations are passed from particle to particle through the wood to her ear.",
  ["What carries the sound to her ear?", "How does sound travel through a material?", "Explain."],
  "sound travels through solids by vibrations passed between particles",
  ["It shows sound travels through solids; the vibrations are passed from particle to particle", "the table carries the sound because its particles pass on the vibrations"],
  ["Sound cannot travel through solids", "Light from the tap travels through the table"], min_points=2)

Q("w9b_dt_vs_dx_confusion", 2, "9c", "A student says the distance between two crests on a displacement–TIME graph is the wavelength. Explain why this is wrong.",
  [P("the horizontal axis is time, so the spacing between crests is a time", ["axis is time", "it is a time", "time axis", "measured in seconds"]),
   P("it is the period, not the wavelength", ["period", "not the wavelength"]),
   P("wavelength is read from a displacement–distance graph", ["displacement–distance", "displacement-distance", "distance graph", "distance axis"])],
  "On a displacement–time graph the horizontal axis is time, so the spacing between crests is a time: the period. The wavelength is a distance and must be read from a displacement–distance graph.",
  ["What is on the horizontal axis of this graph?", "What quantity is the gap between crests here?", "Which graph gives wavelength?"],
  "time axis → crest spacing is the period; wavelength from distance graph",
  ["The axis is time, so the gap between crests is the period, not the wavelength; wavelength comes from a displacement-distance graph", "it is a time, the period; you need a distance graph for the wavelength"],
  ["It is right, both graphs give wavelength", "It is the amplitude"], min_points=2)

Q("w9b_drum", 2, "9f", "Explain how a drum produces a sound that travels to a listener.",
  [P("the drum skin vibrates when hit", ["skin vibrates", "drum vibrates", "vibrates", "vibration"]),
   P("it pushes and pulls the air, making compressions and rarefactions", ["compressions", "rarefactions", "pushes the air", "pushes and pulls", "squashes the air"]),
   P("the longitudinal wave travels through the air to the listener's ear", ["travels through the air", "longitudinal", "to the ear", "through the air", "reaches the ear"])],
  "When the drum is hit, its skin vibrates. As it moves out and in, it pushes and pulls the air next to it, producing compressions and rarefactions. This longitudinal wave travels through the air to the listener's ear.",
  ["What does the drum skin do when hit?", "What does it do to the air?", "How does the sound reach the ear?"],
  "skin vibrates → compressions/rarefactions → longitudinal wave through air",
  ["The skin vibrates, pushing and pulling the air to make compressions and rarefactions, which travel through the air to the ear", "the drum vibrates and sends a longitudinal wave through the air"],
  ["The drum sends out light", "The air is carried from the drum to the ear"], min_points=2, pitfalls=[MATTER])

Q("w9b_echo_conditions", 2, "9i", "State two conditions needed for a clear echo to be heard.",
  [P("a large, hard (flat) reflecting surface", ["hard surface", "large surface", "flat surface", "hard wall", "cliff", "hard"]),
   P("the surface far enough away that the echo arrives separately from the original sound", ["far enough", "far away", "distance", "separately", "delay", "time gap"])],
  "A clear echo needs a large, hard, flat surface to reflect the sound well, and the surface must be far enough away that the echo arrives clearly after the original sound.",
  ["What kind of surface reflects sound well?", "Why might a very close wall not give a separate echo?", "State both conditions."],
  "hard large surface; far enough away",
  ["A large hard surface that is far enough away for the echo to be heard separately", "a flat hard wall at a good distance"],
  ["A soft curtain nearby", "A very loud sound only"], min_points=2)

Q("w9b_count_frequency", 2, "9c", "A student counts 15 ripples passing a post in 5 seconds. Explain how to find the frequency and the period.",
  [P("frequency = number of waves ÷ time = 15 ÷ 5 = 3 Hz", ["15 ÷ 5", "3 hz", "number of waves ÷ time", "waves per second"]),
   P("period = 1 ÷ frequency = 1/3 s (≈ 0.33 s)", ["1 ÷ 3", "0.33", "1/3", "1 ÷ frequency", "time for one wave"])],
  "Frequency = number of waves ÷ time = 15 ÷ 5 = 3 Hz. Period = 1 ÷ frequency = 1/3 s ≈ 0.33 s.",
  ["Frequency is waves per second.", "Period is the time for one wave.", "Calculate both."],
  "f = 15 ÷ 5 = 3 Hz; T = 1/3 s",
  ["Frequency is 15 ÷ 5 = 3 Hz and the period is 1 ÷ 3 = 0.33 s", "3 waves per second, so each takes 1/3 s"],
  ["Frequency = 5 ÷ 15", "Frequency = 75 Hz"], min_points=2)

# ---------------------------------------------------------------- L3
Q("w9b_why_halve_echo", 3, "9i", "When using an echo to find the distance to a cliff, a student uses d = (speed × time) ÷ 2. Explain the ÷ 2.",
  [P("the sound travels to the cliff and back again", ["to the cliff and back", "there and back", "goes and returns", "travels twice the distance", "round trip"]),
   P("so speed × time gives twice the distance to the cliff", ["twice the distance", "double the distance", "two times the distance", "2d", "half of speed"])],
  "The time measured is for the sound to travel to the cliff and back again, so speed × time is twice the distance to the cliff. Dividing by 2 gives the one-way distance.",
  ["How far does the sound travel before the echo is heard?", "What does speed × time give?", "Why halve it?"],
  "there and back; speed × time = 2d",
  ["The sound goes to the cliff and back, so speed × time is twice the distance", "it is a round trip, so the distance is half of speed × time"],
  ["Because sound slows down after reflecting", "Because only half the sound is reflected"], min_points=2)

Q("w9b_shallow_water", 3, "9d", "Fig. 1 shows wavefronts. Water waves move into shallower water, where they travel more slowly. Explain what happens to their frequency and wavelength.",
  [P("the frequency stays the same (set by the source)", ["frequency stays the same", "same frequency", "frequency does not change", "frequency is unchanged"]),
   P("the wavelength decreases (wavefronts closer together)", ["wavelength decreases", "shorter wavelength", "closer together", "wavelength gets smaller"]),
   P("because v = f λ: with f fixed, smaller v means smaller λ", ["v = f λ", "v = fλ", "lower speed", "slower", "smaller speed"])],
  "The frequency stays the same, because it is set by the source. Since v = f λ and the speed decreases, the wavelength must decrease, so the wavefronts get closer together.",
  ["What sets the frequency of a wave?", "Use v = f λ.", "What happens to λ when v falls?"],
  "f unchanged; λ decreases (v = f λ)",
  ["The frequency stays the same and the wavelength decreases, because v = fλ and the speed is lower", "same frequency, shorter wavelength since the waves slow down"],
  ["The frequency decreases", "The wavelength increases"], min_points=2,
  pitfalls=[PF(["frequency decreases", "frequency changes", "wavelength increases"], "Frequency is fixed by the source; slower waves have a SHORTER wavelength.")],
  figure=lambda: sketches.wavefronts_sketch(6, ""))

Q("w9b_double_f_speaker", 3, "9d", "A loudspeaker's frequency is doubled. Explain what happens to the wavelength of the sound in the air.",
  [P("the wavelength halves", ["halves", "half", "halved", "decreases by half"]),
   P("the speed of sound in air stays the same, and v = f λ", ["speed stays the same", "same speed", "speed is unchanged", "v = f λ", "v = fλ"])],
  "The speed of sound in air does not depend on frequency, so it stays the same. Since v = f λ, doubling the frequency halves the wavelength.",
  ["Does changing the frequency change the speed of sound in air?", "Use v = f λ.", "What happens to λ?"],
  "λ halves (v fixed)",
  ["The wavelength halves because the speed stays the same and v = fλ", "same speed, double frequency, so half the wavelength"],
  ["The wavelength doubles", "The sound travels twice as fast"], min_points=2)

Q("w9b_compression_spacing", 3, "9g", "Explain how the wavelength of a sound wave relates to its compressions and rarefactions.",
  [P("the wavelength is the distance between two neighbouring compressions", ["distance between two compressions", "between neighbouring compressions", "one compression to the next", "two compressions"]),
   P("(or) between two neighbouring rarefactions", ["two rarefactions", "rarefaction to rarefaction", "between rarefactions"])],
  "The wavelength of a sound wave is the distance between the centres of two neighbouring compressions (or between two neighbouring rarefactions).",
  ["A sound wave has a repeating pattern of compressions and rarefactions.", "What repeats once per wavelength?", "State it."],
  "distance between neighbouring compressions (or rarefactions)",
  ["The wavelength is the distance between two neighbouring compressions", "it is the distance from one rarefaction to the next"],
  ["The distance between a compression and the next rarefaction", "The size of a compression"], min_points=1,
  pitfalls=[PF(["compression and the next rarefaction", "compression to rarefaction"], "Compression to rarefaction is only HALF a wavelength.")])

Q("w9b_stadium_wave", 3, "9b", "In a 'Mexican wave' in a stadium, spectators stand up and sit down in turn. Explain why this is like a transverse wave and what travels around the stadium.",
  [P("each spectator moves up and down, at right angles to the direction the wave travels", ["up and down", "right angles", "perpendicular", "at 90"]),
   P("the spectators do not move around the stadium (they stay in their seats)", ["stay in their seats", "do not move around", "stay in place", "do not travel"]),
   P("the disturbance (pattern/energy) travels around the stadium", ["pattern travels", "disturbance travels", "energy travels", "wave travels", "the pattern moves"])],
  "Each spectator moves up and down, at right angles to the direction in which the wave moves around the stadium, as in a transverse wave. The spectators stay in their seats; it is the disturbance, the pattern of standing and sitting, that travels around the stadium, just as a wave transfers energy, not matter.",
  ["Which way does each person move?", "Do they move around the stadium?", "What does travel around?"],
  "people move up/down (perpendicular); pattern travels, not people",
  ["Each person moves up and down at right angles to the wave's direction, staying in their seat, while the pattern travels round", "the people do not move around; the disturbance travels, like a transverse wave"],
  ["The spectators run around the stadium", "It is longitudinal because people move forwards"], min_points=2)

Q("w9b_tuning_fork", 3, "9g", "Explain how a vibrating tuning fork produces compressions and rarefactions in the air.",
  [P("as a prong moves outwards it pushes air particles together, forming a compression", ["pushes air particles together", "squashes the air", "compression", "moves outwards"]),
   P("as it moves back, it leaves a region where particles are spread out, a rarefaction", ["spread out", "rarefaction", "moves back", "moves inwards", "further apart"]),
   P("these regions travel outwards as a longitudinal sound wave", ["travel outwards", "longitudinal", "sound wave", "spread out from"])],
  "As each prong moves outwards, it pushes the air particles next to it closer together, forming a compression. As it moves back, it leaves a region where the particles are more spread out, a rarefaction. The prongs keep vibrating, so a series of compressions and rarefactions travels outwards as a longitudinal sound wave.",
  ["What does a prong do to the air as it moves out?", "And as it moves back?", "What travels away?"],
  "prong out → compression; back → rarefaction; travel outwards",
  ["When a prong moves out it squashes the air into a compression, and when it moves back it leaves a rarefaction; these travel outwards as sound", "the prongs push and pull the air, making compressions and rarefactions"],
  ["The fork gives out light", "The fork blows air towards the listener"], min_points=2, pitfalls=[MATTER])

Q("w9b_louder_same_pitch", 3, "9h", "A note is played louder but at the same pitch. Explain how the sound wave changes, and what stays the same.",
  [P("the amplitude increases", ["amplitude increases", "larger amplitude", "bigger amplitude", "higher amplitude"]),
   P("the frequency (and so the period and wavelength) stays the same", ["frequency stays the same", "same frequency", "frequency does not change", "same period", "same wavelength"])],
  "Playing louder increases the amplitude of the wave. The pitch is the same, so the frequency (and therefore the period and wavelength) does not change.",
  ["Which property decides loudness?", "Which property decides pitch?", "Which changes, which stays the same?"],
  "amplitude up; frequency unchanged",
  ["The amplitude increases but the frequency stays the same", "bigger amplitude for loudness, same frequency because the pitch is unchanged"],
  ["The frequency increases", "The wave travels faster"], min_points=2, pitfalls=[LOUD_PITCH])

Q("w9b_pistol_smoke", 3, "9i", "At a race, timekeepers start their stopwatches when they see the smoke from the starting pistol, not when they hear the bang. Explain why.",
  [P("light travels much faster than sound (almost instantly over a stadium)", ["light travels faster", "much faster", "almost instantly", "light is faster"]),
   P("the sound takes a noticeable time to reach the finish line", ["sound takes time", "sound is slower", "delay", "takes time to arrive", "sound arrives later"]),
   P("so starting on the sound would start the watch late, giving times that are too short", ["start late", "too short", "less than the real time", "times too small"])],
  "Light travels much faster than sound, reaching the timekeepers almost instantly, whereas the sound takes a noticeable time to travel to the finish line. Starting on the sound would start the stopwatch late and make the recorded times too short.",
  ["Which arrives first, the light or the sound?", "What would happen if they waited for the sound?", "Explain."],
  "light much faster; sound delay makes times too short",
  ["Light travels much faster than sound, so the sound arrives late and the times would be too short", "seeing the smoke is almost instant, but the sound takes time to reach them"],
  ["The smoke is louder than the bang", "Sound travels faster than light"], min_points=2,
  pitfalls=[PF(["sound travels faster than light", "sound is faster"], "Light travels about a million times faster than sound.")])

Q("w9b_compare_vibration_directions", 3, "9e", "Compare the direction of vibration of the particles in a water ripple and in a sound wave, relative to the direction of travel.",
  [P("water ripple: particles vibrate at right angles (perpendicular) to the direction of travel (transverse)", ["right angles", "perpendicular", "transverse", "up and down"]),
   P("sound: particles vibrate parallel to the direction of travel (longitudinal)", ["parallel", "longitudinal", "back and forth", "same direction"])],
  "In a water ripple, the particles move up and down, at right angles to the direction of travel: a transverse wave. In a sound wave, the particles vibrate back and forth, parallel to the direction of travel: a longitudinal wave.",
  ["Which type of wave is a water ripple?", "Which type is sound?", "Compare the directions."],
  "ripple: perpendicular (transverse); sound: parallel (longitudinal)",
  ["In the ripple the particles move at right angles to the direction of travel, but in sound they vibrate parallel to it", "water ripples are transverse and sound is longitudinal"],
  ["Both vibrate parallel", "Both vibrate at right angles"], min_points=2)

Q("w9b_fish_finder", 3, "9i", "A fishing boat uses an echo sounder to detect shoals of fish. Explain how it works.",
  [P("it sends a pulse of sound (ultrasound) down into the water", ["sends a pulse", "sends sound", "pulse of sound", "sound pulse", "ultrasound"]),
   P("the pulse is reflected by the fish (and the sea bed) and the echo is detected", ["reflected", "echo", "bounces off", "detected"]),
   P("the time for the echo, with the speed of sound in water, gives the depth of the fish (d = v t ÷ 2)", ["time", "speed of sound in water", "d = vt", "÷ 2", "depth"])],
  "The echo sounder sends a pulse of sound down into the water. The pulse is reflected by a shoal of fish (and by the sea bed), and the echo is detected back at the boat. From the time taken and the speed of sound in water, the depth of the fish is found using d = v × t ÷ 2.",
  ["What does the device send out?", "What happens when the pulse hits the fish?", "How is the depth worked out?"],
  "sound pulse, reflected by fish, echo time → depth",
  ["It sends a sound pulse that is reflected by the fish; the echo time and the speed of sound in water give the depth", "the pulse bounces off the fish and the time taken gives how deep they are"],
  ["It uses light to see the fish", "The fish make the sound"], min_points=2)

# ---------------------------------------------------------------- L4
Q("w9b_ripple_speed_method", 4, "9d", "Describe how to find the speed of water waves in a ripple tank by measuring their frequency and wavelength.",
  [P("frequency: count the number of waves passing a point in a measured time (or use the dipper's frequency)", ["count", "number of waves", "measured time", "frequency of the dipper", "waves per second"]),
   P("wavelength: measure across several wavefronts on the shadow/screen and divide by the number of gaps", ["several wavefronts", "number of gaps", "measure the distance", "divide by", "ruler"]),
   P("speed = frequency × wavelength", ["frequency × wavelength", "v = f λ", "v = fλ", "multiply"])],
  "Find the frequency by counting the number of waves passing a fixed point in a measured time (frequency = waves ÷ time), or from the dipper's setting. Find the wavelength by measuring across several wavefronts on the shadow pattern with a ruler and dividing by the number of gaps. Then speed = frequency × wavelength.",
  ["How can you find the number of waves per second?", "How can you measure the wavelength accurately?", "Combine them."],
  "count waves per second; measure across several wavefronts; v = f λ",
  ["Count the waves passing in a measured time for the frequency, measure across several wavefronts and divide by the gaps for the wavelength, then multiply", "find f and λ and use v = f λ"],
  ["Time one ripple with a stopwatch only", "Measure the depth of the water"], min_points=1)

Q("w9b_soundproofing", 4, "9i", "A music practice room has soft foam panels on the walls. Explain how they improve the sound in the room.",
  [P("soft materials absorb sound instead of reflecting it", ["absorb", "absorbs sound", "soak up", "do not reflect"]),
   P("so there are fewer echoes / less reverberation", ["fewer echoes", "less echo", "reduce echoes", "no echoes", "reverberation"]),
   P("hard walls would reflect sound, making it muddled or too loud", ["hard walls reflect", "hard surfaces reflect", "reflect", "muddled", "too loud"])],
  "Soft foam absorbs much of the sound that hits it instead of reflecting it, so there are fewer echoes and the sound is clearer. Bare hard walls would reflect the sound, causing echoes that make the music muddled and louder.",
  ["What do hard surfaces do to sound?", "What do soft surfaces do?", "What problem does this solve?"],
  "foam absorbs sound → fewer echoes",
  ["The soft panels absorb sound so there are fewer echoes, whereas hard walls would reflect it", "foam soaks up the sound, reducing reflections and echoes"],
  ["Foam makes the room louder", "Foam reflects the sound back better"], min_points=2)

Q("w9b_two_mic_speed", 4, "9d", "Describe how two microphones a measured distance apart and an electronic timer can be used to measure the speed of sound.",
  [P("place the microphones in a line a measured distance apart (e.g. 1 m) and make a sharp sound at one end", ["measured distance", "distance apart", "1 m", "sharp sound", "in a line", "clap"]),
   P("the timer starts when the first microphone detects the sound and stops at the second", ["timer starts", "starts", "stops", "first microphone", "second microphone", "time on the timer"]),
   P("speed = distance ÷ time (repeat and average)", ["distance ÷ time", "distance divided by time", "speed =", "repeat", "average", "then divide"])],
  "Place two microphones in line with the sound source, a measured distance apart, and connect them to an electronic timer. Make a sharp sound beyond the first microphone; the timer starts when the sound reaches the first microphone and stops when it reaches the second. Speed of sound = distance between the microphones ÷ time. Repeat and average.",
  ["What two measurements are needed?", "How does the timer start and stop?", "How is the speed calculated?"],
  "distance between mics; timer between them; v = d ÷ t",
  ["Put the microphones a measured distance apart, the timer records the time for the sound to go from one to the other, and speed = distance ÷ time", "measure the distance between the microphones and the time on the timer, then divide"],
  ["Use one microphone and a ruler", "Measure how loud the sound is"], min_points=2)

Q("w9b_frequency_up_same_medium", 4, "9d", "A signal generator increases the frequency of a sound from a loudspeaker. Explain what happens to the speed, wavelength and pitch.",
  [P("the speed stays the same (depends on the medium, air)", ["speed stays the same", "same speed", "speed does not change", "depends on the medium"]),
   P("the wavelength decreases (v = f λ)", ["wavelength decreases", "shorter wavelength", "wavelength gets smaller"]),
   P("the pitch becomes higher", ["higher pitch", "pitch increases", "pitch rises", "pitch gets higher"])],
  "The speed of sound depends on the medium, air, so it stays the same. Since v = f λ, increasing the frequency decreases the wavelength. A higher frequency is heard as a higher pitch.",
  ["What decides the speed of sound?", "Use v = f λ.", "How does frequency relate to pitch?"],
  "speed same; wavelength down; pitch up",
  ["The speed stays the same, the wavelength decreases and the pitch gets higher", "same speed in air, shorter wavelength, higher pitch"],
  ["The sound travels faster", "The pitch gets lower"], min_points=3)

Q("w9b_period_frequency_relation", 4, "9c", "Explain the relationship between the period and the frequency of a wave, using a wave of frequency 50 Hz as an example.",
  [P("period = 1 ÷ frequency (they are reciprocals)", ["1 ÷ frequency", "1 / f", "reciprocal", "t = 1 / f", "one over"]),
   P("50 Hz means 50 waves per second, so each takes 1/50 s = 0.02 s", ["0.02 s", "1/50", "50 waves per second", "0.02"]),
   P("a higher frequency means a shorter period", ["higher frequency", "shorter period", "inversely"])],
  "Period and frequency are reciprocals: T = 1 ÷ f. A frequency of 50 Hz means 50 waves per second, so each wave takes 1/50 s = 0.02 s. The higher the frequency, the shorter the period.",
  ["What does 50 Hz mean?", "How long is each wave, then?", "Generalise."],
  "T = 1/f; 50 Hz → 0.02 s",
  ["The period is 1 ÷ frequency, so 50 Hz gives a period of 0.02 s; higher frequency means shorter period", "50 waves per second means each takes 1/50 s"],
  ["Period = frequency × 50", "They are the same thing"], min_points=1)

Q("w9b_concert_hall", 4, "9i", "Explain why concert halls are designed with soft seats and curtains, and why some hard surfaces are still used.",
  [P("soft materials absorb sound, reducing unwanted echoes", ["absorb", "reduce echoes", "fewer echoes", "soak up"]),
   P("too many echoes would make music sound muddled / unclear", ["muddled", "unclear", "blurred", "overlap", "confusing"]),
   P("some reflection from hard surfaces helps sound reach the whole audience / sound fuller", ["some reflection", "reach the audience", "hard surfaces reflect", "fuller", "louder at the back"])],
  "Soft seats and curtains absorb sound, reducing echoes that would arrive at different times and make the music sound muddled. Some hard, reflecting surfaces are kept so that enough reflected sound reaches the whole audience, making the music sound full rather than dead.",
  ["What do soft materials do to sound?", "What problem do too many echoes cause?", "Why keep some reflection?"],
  "absorb to reduce echoes; some reflection to reach everyone",
  ["Soft materials absorb sound to reduce echoes that make music muddled, but some hard surfaces reflect sound so it reaches the whole audience", "fewer echoes from the absorbing seats, with some reflection for a fuller sound"],
  ["Soft seats make the music louder", "Curtains reflect the sound"], min_points=2)

Q("w9b_shallowing_sea", 4, "9i", "As a ship sails towards the shore, its echo sounder records shorter and shorter echo times. Explain what this shows.",
  [P("a shorter echo time means the pulse travels a shorter distance (there and back)", ["shorter distance", "less distance", "less time", "travels less far"]),
   P("so the sea bed is getting closer: the water is becoming shallower", ["shallower", "depth decreases", "sea bed is closer", "less deep"]),
   P("depth = speed × time ÷ 2, which decreases as time decreases", ["speed × time", "÷ 2", "proportional", "depth ="])],
  "The echo time is the time for the pulse to travel to the sea bed and back. Shorter echo times mean the pulse travels a shorter distance, so the sea bed is getting closer: the water becomes shallower as the ship nears the shore (depth = speed × time ÷ 2).",
  ["What does the echo time depend on?", "What does a shorter time mean?", "What is happening to the depth?"],
  "shorter echo time → shallower water",
  ["The shorter echo times mean the sound travels a shorter distance, so the water is getting shallower", "depth = speed × time ÷ 2, so less time means less depth"],
  ["The sound is travelling faster", "The sea is getting deeper"], min_points=2)

Q("w9b_slinky_energy", 4, "9b", "A pulse is sent along a slinky lying on a table; a light paper cup at the far end is knocked over. Explain what this shows about waves.",
  [P("the pulse transfers energy along the slinky", ["transfers energy", "carries energy", "energy is transferred", "energy"]),
   P("the coils of the slinky themselves do not travel to the end (they vibrate and return)", ["coils do not travel", "do not move along", "return to their positions", "stay in place", "vibrate"]),
   P("the energy arriving at the end does work on the cup", ["does work", "knocks over", "energy reaches the cup", "transferred to the cup"])],
  "The cup is knocked over because the pulse transfers energy along the slinky; when it arrives, the energy does work on the cup. The coils of the slinky only vibrate and return to their positions; they do not travel along to the end. Waves transfer energy without transferring matter.",
  ["Did the coils travel the length of the slinky?", "What reached the cup?", "What does this show?"],
  "energy transferred, not matter",
  ["The pulse transfers energy along the slinky, which knocks the cup over, while the coils only vibrate and stay in place", "energy travels along the slinky even though the coils do not move along it"],
  ["The slinky moves to the end and pushes the cup", "Air pushes the cup"], min_points=2, pitfalls=[MATTER])

Q("w9b_guitar_pitch", 4, "9h", "A guitarist presses a string against a fret, making the vibrating length shorter. Explain the effect on the note.",
  [P("a shorter string vibrates with a higher frequency", ["higher frequency", "vibrates faster", "frequency increases", "more vibrations per second"]),
   P("so the pitch of the note is higher", ["higher pitch", "pitch increases", "higher note", "pitch rises", "raising the pitch", "raises the pitch"])],
  "Shortening the vibrating length makes the string vibrate with a higher frequency. A higher frequency is heard as a higher-pitched note.",
  ["What happens to the vibration of a shorter string?", "How is pitch related to frequency?", "Explain."],
  "shorter → higher frequency → higher pitch",
  ["The shorter string vibrates at a higher frequency, so the note has a higher pitch", "it vibrates faster, raising the pitch"],
  ["The note gets louder", "The note gets lower"], min_points=2, pitfalls=[LOUD_PITCH])

Q("w9b_whale_sound", 4, "9f", "Whales communicate using sound over long distances in the ocean. Explain how sound travels through water.",
  [P("the whale's sound makes water particles vibrate", ["water particles vibrate", "vibrate", "vibration"]),
   P("the vibrations are passed from particle to particle as compressions and rarefactions (longitudinal)", ["passed on", "particle to particle", "compressions", "rarefactions", "longitudinal"]),
   P("water particles are close together, so vibrations pass on easily; the water itself does not travel", ["close together", "easily", "does not travel", "particles stay", "not carried"])],
  "The whale's sound makes the water particles near it vibrate. Each particle passes the vibration on to its neighbours, creating compressions and rarefactions that travel through the water as a longitudinal wave. The water particles are close together, so they pass the vibrations on easily; the water itself does not travel with the sound.",
  ["What does the sound do to the water particles?", "How is the vibration passed on?", "Does the water move along with the sound?"],
  "particles vibrate, pass on vibrations; compressions/rarefactions; no flow",
  ["The sound makes water particles vibrate, and the vibrations pass from particle to particle as compressions and rarefactions", "it is a longitudinal wave in the water; the particles are close so they pass the vibrations on"],
  ["The water carries the sound by flowing", "Sound cannot travel in water"], min_points=2, pitfalls=[MATTER])

# ---------------------------------------------------------------- L5
Q("w9b_long_wavelength_faster_claim", 5, "9d", "A student says: 'Waves with a longer wavelength travel faster.' Evaluate this claim for sound waves in air.",
  [P("wrong: all sound waves in air travel at the same speed", ["wrong", "same speed", "all travel at", "speed is the same", "incorrect"]),
   P("the speed depends on the medium, not the wavelength", ["depends on the medium", "medium", "not on the wavelength"]),
   P("a longer wavelength simply goes with a lower frequency (v = f λ)", ["lower frequency", "v = f λ", "v = fλ", "smaller frequency"])],
  "The claim is wrong for sound in air. All sound waves in air travel at the same speed, because the speed depends on the medium, not on the wavelength. Since v = f λ with v fixed, a longer wavelength simply goes with a lower frequency.",
  ["What decides the speed of sound?", "Is it the same for all frequencies in air?", "How are λ and f related when v is fixed?"],
  "wrong; same speed in same medium; longer λ ↔ lower f",
  ["Wrong: all sound in air travels at the same speed because it depends on the medium; a longer wavelength just means a lower frequency", "the speed depends on the medium, so a longer wavelength has a lower frequency, not a higher speed"],
  ["Correct, longer waves are faster", "Correct, wavelength decides the speed"], min_points=2)

Q("w9b_improve_echo_method", 5, "9i", "A student times one echo from a wall 50 m away with a stopwatch to find the speed of sound. Evaluate the method and suggest improvements.",
  [P("the echo time is only about 0.3 s, so reaction time (≈ 0.2 s) gives a very large error", ["reaction time", "0.3 s", "large error", "short time", "0.2 s"]),
   P("improve: clap repeatedly in time with the echoes and time many (e.g. 20) intervals, then divide", ["clap repeatedly", "many claps", "20 claps", "rhythm", "time many", "in time with the echoes"]),
   P("or use a greater distance / electronic timing / repeat and average", ["greater distance", "further away", "electronic", "microphones", "repeat", "average"])],
  "Timing a single echo from 50 m is unreliable: the echo arrives after only about 0.3 s, and human reaction time (about 0.2 s) is a large fraction of that. Better: clap repeatedly so that each clap coincides with the previous echo, time 20 such intervals and divide, or move further from the wall, or use microphones and an electronic timer, repeating and averaging.",
  ["How long does the echo take?", "How does that compare with reaction time?", "How can the measured time be made longer, or the timing automatic?"],
  "short time vs reaction time; time many echoes, electronic timing",
  ["The time is only 0.3 s so reaction time causes a large error; clap in rhythm with the echoes and time 20 claps, or use electronic timing", "reaction time is a big fraction of the time; time many echo intervals and average"],
  ["The method is accurate because stopwatches read to 0.01 s", "Shout louder"], min_points=2)

Q("w9b_space_explosion_claim", 5, "9f", "In a science-fiction film, a spaceship explodes with a loud bang heard by a nearby spacecraft. Evaluate whether this could happen.",
  [P("it could not happen: sound cannot travel through the vacuum of space", ["could not", "cannot", "vacuum", "no sound in space", "not possible"]),
   P("sound needs a medium (particles) to pass on vibrations", ["needs a medium", "needs particles", "no particles", "no air"]),
   P("the light from the explosion would be seen, because light can travel through a vacuum", ["light", "seen", "light can travel", "electromagnetic"])],
  "This could not happen. Sound needs a medium of particles to pass on its vibrations, and space is a vacuum, so no sound would reach the other spacecraft. The flash of light from the explosion would be seen, though, because light can travel through a vacuum.",
  ["What does sound need in order to travel?", "What is between the spacecraft?", "What would the crew detect?"],
  "no sound in a vacuum; light would be seen",
  ["It is impossible: space is a vacuum and sound needs a medium, but the light from the explosion would be seen", "sound cannot travel through the vacuum of space, though light can"],
  ["Possible, because explosions are very loud", "Possible, sound travels faster in space"], min_points=2)

Q("w9b_frequency_change_medium_claim", 5, "9d", "A student says: 'When sound passes from air into water its frequency changes because it speeds up.' Evaluate this claim.",
  [P("wrong: the frequency stays the same (set by the source)", ["wrong", "frequency stays the same", "same frequency", "set by the source", "frequency does not change"]),
   P("the speed does increase in water", ["speeds up", "faster in water", "speed increases"]),
   P("so it is the wavelength that increases (v = f λ)", ["wavelength increases", "longer wavelength", "wavelength gets longer", "v = f λ"])],
  "The claim is wrong. The frequency of a wave is set by the source, so it stays the same when the sound enters water. The sound does speed up in water, so by v = f λ it is the wavelength that increases.",
  ["What sets the frequency of a wave?", "Does the speed change in water?", "Which quantity must change?"],
  "wrong; frequency fixed by source; wavelength increases",
  ["Wrong: the frequency stays the same because it is set by the source; the speed increases, so the wavelength increases", "frequency does not change; the wavelength gets longer since v = fλ"],
  ["Correct, the frequency increases", "Correct, faster sound has a higher frequency"], min_points=2)

Q("w9b_rope_matter_claim", 5, "9b", "A student says: 'When I send a wave along a rope, the rope itself moves to the far end.' Evaluate this claim, suggesting how to test it.",
  [P("wrong: each part of the rope only vibrates about its rest position", ["wrong", "only vibrates", "rest position", "up and down", "does not move along"]),
   P("the wave transfers energy, not the rope (matter)", ["transfers energy", "energy", "not matter", "not the rope"]),
   P("test: tie a ribbon to the rope and watch it move up and down but stay in place", ["ribbon", "mark", "tie", "watch", "stays in place", "piece of tape"])],
  "The claim is wrong. Each part of the rope only vibrates about its rest position; the wave transfers energy along the rope, not the rope itself. To test it, tie a ribbon to the middle of the rope: as the wave passes, the ribbon moves up and down but stays at the same place along the rope.",
  ["What does a point on the rope actually do?", "What does the wave transfer?", "How could you track a point on the rope?"],
  "wrong; rope vibrates in place; energy transferred; ribbon test",
  ["Wrong: the rope only vibrates about its rest position and the wave transfers energy; tie a ribbon on it and it just moves up and down", "the rope does not travel; a marked point stays in place while energy moves along"],
  ["Correct, the rope moves along with the wave", "Correct, waves carry the rope"], min_points=2, pitfalls=[MATTER])

Q("w9b_two_traces", 5, "9h", "Two sound traces are shown on an oscilloscope with the same settings. Trace A has taller waves; trace B has more waves across the screen. Evaluate which sound is louder and which has the higher pitch.",
  [P("A is louder because it has the larger amplitude", ["a is louder", "a has the larger amplitude", "taller waves are louder", "larger amplitude"]),
   P("B has the higher pitch because it has the higher frequency (more waves in the same time)", ["b has the higher pitch", "higher frequency", "more waves", "b is higher"]),
   P("loudness depends on amplitude; pitch depends on frequency", ["loudness depends on amplitude", "pitch depends on frequency", "amplitude", "frequency"])],
  "Trace A is louder, because its waves are taller, showing a larger amplitude. Trace B has the higher pitch, because more waves fit across the screen in the same time, showing a higher frequency. Loudness depends on amplitude; pitch depends on frequency.",
  ["What does the height of a trace show?", "What does the number of waves across the screen show?", "Match each to loudness and pitch."],
  "A louder (amplitude); B higher pitch (frequency)",
  ["A is louder because it has a larger amplitude, and B has a higher pitch because it has a higher frequency", "taller waves mean louder; more waves in the same time mean a higher pitch, so B is higher"],
  ["A has the higher pitch because its waves are taller", "B is louder because it has more waves"], min_points=2, pitfalls=[LOUD_PITCH,
  PF(["a has the higher pitch", "b is louder"], "Taller waves (amplitude) mean louder; more waves in the same time (frequency) mean higher pitch.")])

Q("w9b_short_echo_timing", 5, "9i", "A student stands 17 m from a wall and tries to time a single echo with a stopwatch. Evaluate this, given the speed of sound is about 340 m/s.",
  [P("the echo time is only about 0.1 s (34 m ÷ 340 m/s)", ["0.1 s", "34 ÷ 340", "very short", "tenth of a second"]),
   P("this is less than human reaction time, so it cannot be timed reliably by hand", ["reaction time", "too short", "cannot be timed", "unreliable", "less than reaction"]),
   P("use a much greater distance, many repeated echoes, or electronic timing", ["greater distance", "further away", "many echoes", "electronic", "microphones", "repeated claps"])],
  "The sound travels 34 m there and back, taking only about 34 ÷ 340 = 0.1 s. That is shorter than human reaction time, so it cannot be timed reliably by hand. The student should stand much further away, time many echoes by clapping in rhythm, or use microphones with an electronic timer.",
  ["How far does the sound travel, and how long does that take?", "Compare with reaction time.", "Suggest improvements."],
  "echo time 0.1 s < reaction time; use bigger distance, many echoes, electronic timing",
  ["The echo takes only 0.1 s, less than reaction time, so hand timing is unreliable; move further away or use electronic timing", "34 m at 340 m/s is 0.1 s, too short to time by hand"],
  ["It is fine because the wall is close", "The echo would take 5 s"], min_points=2)

Q("w9b_tsunami", 5, "9b", "A tsunami can cross an ocean and cause destruction thousands of kilometres away, yet the water in mid-ocean only moves up and down slightly as it passes. Evaluate this using wave ideas.",
  [P("the tsunami transfers energy across the ocean", ["transfers energy", "energy", "carries energy"]),
   P("the water itself is not carried across the ocean; it only vibrates locally", ["not carried", "does not travel across", "only moves up and down", "vibrates", "stays in place"]),
   P("near the shore the energy is concentrated, producing huge, destructive waves", ["near the shore", "shallow", "concentrated", "huge waves", "destructive", "amplitude increases"])],
  "This is consistent with how waves work. The tsunami transfers a huge amount of energy across the ocean, but the water itself is not carried across: in deep water it only moves up and down slightly as the wave passes. Near the shore, in shallow water, the energy is concentrated into much taller waves, which cause the destruction.",
  ["What does a wave transfer?", "Does the water travel with the wave?", "Why is it destructive at the coast?"],
  "energy transferred, not water; concentrated at shore",
  ["The tsunami transfers energy across the ocean while the water only moves up and down; near the shore the energy makes huge waves", "waves carry energy not water, and in shallow water the energy builds up into tall destructive waves"],
  ["The water from one coast is carried to the other", "Tsunamis carry no energy"], min_points=2, pitfalls=[MATTER])

Q("w9b_wavefronts_closer_interpret", 5, "9d", "Fig. 1 shows wavefronts in a ripple tank. In one region the wavefronts are closer together. Evaluate what this shows about the waves in that region, given the dipper's frequency is constant.",
  [P("the wavelength is shorter in that region", ["shorter wavelength", "wavelength is shorter", "smaller wavelength", "wavelength decreases"]),
   P("the frequency is the same everywhere (set by the dipper)", ["same frequency", "frequency is the same", "frequency is constant", "set by the dipper"]),
   P("so the waves are travelling more slowly there (v = f λ), e.g. shallower water", ["more slowly", "slower", "lower speed", "shallower", "v = f λ"])],
  "Closer wavefronts mean the wavelength is shorter in that region. The frequency is fixed by the dipper, so it is the same everywhere; by v = f λ, a shorter wavelength means the waves are travelling more slowly there, for example because the water is shallower.",
  ["What does the spacing of wavefronts show?", "Does the frequency change from region to region?", "Use v = f λ."],
  "shorter λ, same f → slower waves (shallower water)",
  ["The wavelength is shorter there, and with the same frequency the waves must be slower, probably because the water is shallower", "same frequency but closer wavefronts means a lower speed by v = fλ"],
  ["The waves are faster there", "The frequency is higher there"], min_points=2,
  figure=lambda: sketches.wavefronts_sketch(7, ""))

Q("w9b_high_pitch_loud_claim", 5, "9h", "A student says: 'A high-pitched sound is always louder than a low-pitched one.' Evaluate this claim.",
  [P("wrong: pitch and loudness are independent", ["wrong", "independent", "not related", "different properties", "incorrect"]),
   P("pitch depends on frequency", ["pitch depends on frequency", "frequency"]),
   P("loudness depends on amplitude, so a high note can be quiet and a low note loud", ["loudness depends on amplitude", "amplitude", "quiet high note", "loud low note", "can be quiet"])],
  "The claim is wrong. Pitch depends on the frequency of the sound wave, while loudness depends on its amplitude. They are independent: a high-pitched note can be very quiet (small amplitude), and a low-pitched note can be very loud (large amplitude).",
  ["Which wave property decides pitch?", "Which decides loudness?", "Are they linked?"],
  "wrong; pitch = frequency, loudness = amplitude; independent",
  ["Wrong: pitch depends on frequency and loudness on amplitude, so a high note can be quiet", "they are independent properties; a low note with a large amplitude can be very loud"],
  ["Correct, higher pitch means louder", "Correct, frequency decides loudness"], min_points=2, pitfalls=[LOUD_PITCH])
