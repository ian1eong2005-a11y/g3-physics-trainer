"""Chapter 9 General Wave Properties: extra calculation templates."""
from .. import sketches
from .base import calc_q, fmt, md_table, nice, template


# ---------------------------------------------------------------- L1
@template("c9_freq_from_period_table", chapter=9, level=1, lo="9c")
def freq_from_period_table(rng):
    T = nice(rng, 0.02, 0.05, 0.1, 0.25, 0.5)
    f = 1 / T
    table = md_table(["wave", "period / s"], [["water wave", fmt(T)]])
    return calc_q(rng, f"The table gives the period of a wave.\n\n{table}\n\nWhat is its frequency?", f, [
        (T, "Frequency is 1 ÷ period, not equal to it."),
        (T * 100, "f = 1 ÷ T."),
        (f / 2, "f = 1 ÷ T; there is no factor of 2."),
    ], "Hz", "f = 1 ÷ T", [f"f = 1 ÷ {fmt(T)}", f"= **{fmt(f)} Hz**"],
        ["Frequency and period are reciprocals.", "f = 1 ÷ T.", f"1 ÷ {fmt(T)}."])


@template("c9_wavelength_v_f", chapter=9, level=1, lo="9d")
def wavelength_v_f(rng):
    v = nice(rng, 2, 3, 4, 6, 12)
    lam = nice(rng, 0.5, 1, 1.5, 2, 3)
    f = v / lam
    return calc_q(rng, f"Fig. 1 shows a wave on a rope travelling at **{fmt(v)} m/s** with a frequency of **{fmt(f)} Hz**. What is its wavelength?", lam, [
        (v * f, "λ = v ÷ f, not v × f."),
        (f / v, "λ = v ÷ f."),
        (v - f, "Divide speed by frequency."),
    ], "m", "v = f λ, so λ = v ÷ f", ["λ = v ÷ f", f"= {fmt(v)} ÷ {fmt(f)}", f"= **{fmt(lam)} m**"],
        ["Use wave speed = frequency × wavelength.", "Rearrange for λ.", f"{fmt(v)} ÷ {fmt(f)}."],
        figure=sketches.wave_graph(1, lam, kind="distance_m", cycles=2))


@template("c9_freq_count_waves", chapter=9, level=1, lo="9c")
def freq_count_waves(rng):
    n = nice(rng, 20, 30, 40, 60)
    t = nice(rng, 5, 10, 20)
    f = n / t
    table = md_table(["number of waves passing a point", "time / s"], [[n, t]])
    return calc_q(rng, f"A student counts the water waves passing a post.\n\n{table}\n\nWhat is the frequency of the waves?", f, [
        (t / n, "That is the period. Frequency = number of waves ÷ time."),
        (n * t, "Frequency = number of waves per SECOND: divide."),
        (n, "That is the total number of waves, not the number per second."),
    ], "Hz", "frequency = number of waves ÷ time", [f"f = {n} ÷ {t}", f"= **{fmt(f)} Hz**"],
        ["Frequency is the number of waves per second.", "Divide the count by the time.", f"{n} ÷ {t}."])


@template("c9_wave_speed_d_t", chapter=9, level=1, lo="9c")
def wave_speed_d_t(rng):
    d = nice(rng, 30, 45, 60, 90)
    t = nice(rng, 3, 5, 6, 10)
    v = d / t
    return calc_q(rng, f"Fig. 1 shows ripples in a tank. A ripple travels **{d} cm** across the tank in **{t} s**. What is the speed of the ripples?", v, [
        (t / d, "Speed = distance ÷ time."),
        (d * t, "Divide, do not multiply."),
        (v / 100, "That is in m/s; the question uses cm and the answer is in cm/s."),
    ], "cm/s", "speed = distance ÷ time", [f"v = {d} ÷ {t}", f"= **{fmt(v)} cm/s**"],
        ["Wave speed is how far a wavefront travels per second.", "speed = distance ÷ time.", f"{d} ÷ {t}."],
        figure=sketches.wavefronts_sketch(5, f"{d} cm in {t} s"))


# ---------------------------------------------------------------- L2
@template("c9_period_ms_graph", chapter=9, level=2, lo="9c")
def period_ms_graph(rng):
    T = nice(rng, 2, 4, 5, 8, 10)
    return calc_q(rng, "Fig. 1 shows the displacement–time graph of an air particle as a sound wave passes. What is the period of the wave?", T, [
        (T / 2, "One period is a FULL cycle, crest to crest, not half a cycle."),
        (2 * T, "That is two cycles."),
        (1000 / T, "That is the frequency in Hz, not the period."),
    ], "ms", "period = time for one complete oscillation (read from the graph)", [f"one complete cycle takes **{fmt(T)} ms**"],
        ["Find two neighbouring crests.", "The time between them is one period.", "Read it off the time axis."],
        figure=sketches.wave_graph(2, T, kind="time_ms", cycles=2), sf=None)


@template("c9_amplitude_peak_trough", chapter=9, level=2, lo="9c")
def amplitude_peak_trough(rng):
    pt = nice(rng, 4, 6, 8, 10, 12)
    A = pt / 2
    table = md_table(["measurement", "value"], [["vertical distance from a crest to a trough", f"{pt} cm"]])
    return calc_q(rng, f"A student measures a wave on a rope.\n\n{table}\n\nWhat is the amplitude of the wave?", A, [
        (pt, "The amplitude is measured from the REST position to a crest, which is half of crest-to-trough."),
        (pt * 2, "Amplitude is half the crest-to-trough distance."),
        (pt / 4, "Halve once only."),
    ], "cm", "amplitude = ½ × crest-to-trough distance", [f"A = {pt} ÷ 2", f"= **{fmt(A)} cm**"],
        ["Amplitude is measured from the rest position.", "Crest to trough is twice the amplitude.", f"{pt} ÷ 2."])


@template("c9_wavelength_from_wavefronts", chapter=9, level=2, lo="9a")
def wavelength_from_wavefronts(rng):
    n = nice(rng, 5, 6, 7, 9)
    lam = nice(rng, 1.5, 2, 2.5, 3)
    span = (n - 1) * lam
    return calc_q(rng, f"Fig. 1 shows **{n}** straight wavefronts in a ripple tank. The distance from the first to the last is **{fmt(span)} cm**. What is the wavelength?", lam, [
        (span / n, f"{n} wavefronts have only {n - 1} gaps between them."),
        (span, "That is the distance across all the wavefronts."),
        (span / (n + 1), f"Count the gaps: {n} wavefronts → {n - 1} wavelengths."),
    ], "cm", "wavelength = span ÷ number of gaps (wavefronts − 1)", [f"gaps = {n} − 1 = {n - 1}", f"λ = {fmt(span)} ÷ {n - 1}", f"= **{fmt(lam)} cm**"],
        ["Neighbouring wavefronts are one wavelength apart.", "Count the GAPS, not the wavefronts.", f"{fmt(span)} ÷ {n - 1}."],
        figure=sketches.wavefronts_sketch(n, f"{fmt(span)} cm"))


@template("c9_sound_speed_d_t", chapter=9, level=2, lo="9c")
def sound_speed_d_t(rng):
    v = nice(rng, 330, 340, 345)
    t = nice(rng, 0.5, 1.0, 1.5, 2.0)
    d = v * t
    return calc_q(rng, f"Fig. 1 shows a starter's pistol fired **{fmt(d)} m** from a timekeeper. The sound arrives **{fmt(t)} s** after the flash is seen. What is the speed of sound?", v, [
        (d * t, "Speed = distance ÷ time."),
        (t / d, "Speed = distance ÷ time."),
        (v * 2, "The sound travels the distance only once here (no echo)."),
    ], "m/s", "speed = distance ÷ time", [f"v = {fmt(d)} ÷ {fmt(t)}", f"= **{fmt(v)} m/s**"],
        ["Light arrives almost instantly, so the delay is the sound's travel time.", "speed = distance ÷ time.", "There is no echo, so no halving."],
        figure=sketches.echo_sketch(f"{fmt(d)} m", f"sound arrives {fmt(t)} s after the flash", left="timekeeper", right="pistol", back=None))


@template("c9_freq_from_v_lambda", chapter=9, level=2, lo="9d")
def freq_from_v_lambda(rng):
    lam = nice(rng, 0.5, 0.68, 0.85, 1.7, 3.4)
    v = 340
    f = v / lam
    return calc_q(rng, f"Fig. 1 shows a sound wave in air of wavelength **{fmt(lam)} m**. The speed of sound in air is **340 m/s**. What is the frequency?", f, [
        (v * lam, "f = v ÷ λ, not v × λ."),
        (lam / v, "f = v ÷ λ."),
        (f / 2, "No factor of 2: f = v ÷ λ."),
    ], "Hz", "f = v ÷ λ", [f"f = 340 ÷ {fmt(lam)}", f"= **{fmt(f)} Hz**"],
        ["v = f λ.", "Rearrange for f.", f"340 ÷ {fmt(lam)}."],
        figure=sketches.wave_graph(1, lam, kind="distance_m", cycles=2))


@template("c9_speed_in_water", chapter=9, level=2, lo="9d")
def speed_in_water(rng):
    f_khz = nice(rng, 5, 10, 15, 20)
    lam_cm = 150 / f_khz
    v = f_khz * 1000 * lam_cm / 100
    table = md_table(["frequency / kHz", "wavelength in water / cm"], [[f_khz, fmt(lam_cm)]])
    return calc_q(rng, f"A dolphin's click travels through sea water.\n\n{table}\n\nWhat is the speed of the sound in water?", v, [
        (f_khz * lam_cm, "Convert kHz to Hz (× 1000) and cm to m (÷ 100) first."),
        (f_khz * 1000 * lam_cm, "Convert the wavelength from cm to m."),
        (f_khz * lam_cm / 100, "Convert the frequency from kHz to Hz."),
    ], "m/s", "v = f λ in SI units", [f"f = {f_khz} kHz = {f_khz * 1000} Hz; λ = {fmt(lam_cm)} cm = {fmt(lam_cm / 100)} m", f"v = {f_khz * 1000} × {fmt(lam_cm / 100)}", f"= **{fmt(v)} m/s**"],
        ["Use v = f λ.", "Change kHz to Hz and cm to m.", "Multiply."])


# ---------------------------------------------------------------- L3
@template("c9_lightning_distance", chapter=9, level=3, lo="9i")
def lightning_distance(rng):
    t = nice(rng, 3, 4, 5, 6, 8)
    d = 340 * t
    return calc_q(rng, f"During a storm, thunder is heard **{t} s** after the lightning flash is seen. The speed of sound is **340 m/s**, and light arrives almost instantly. How far away is the storm? The table summarises the data.\n\n" + md_table(["time between flash and thunder / s", "speed of sound / m/s"], [[t, 340]]), d, [
        (340 * t / 2, "This is not an echo: the sound travels the distance only ONCE."),
        (340 / t, "distance = speed × time."),
        (340 * t * 2, "The sound travels from the storm to you once."),
    ], "m", "distance = speed of sound × time delay", [f"d = 340 × {t}", f"= **{fmt(d)} m**"],
        ["The flash arrives almost at once; the delay is the sound's travel time.", "distance = speed × time.", "Do not halve: there is no reflection."])


@template("c9_ripple_wavelength_cm", chapter=9, level=3, lo="9d")
def ripple_wavelength_cm(rng):
    v = nice(rng, 12, 15, 18, 24, 30)
    f = nice(rng, 3, 4, 5, 6)
    lam = v / f
    return calc_q(rng, f"Fig. 1 shows ripples made by a dipper vibrating at **{f} Hz**. The ripples travel at **{v} cm/s**. What is the distance between neighbouring wavefronts?", lam, [
        (v * f, "λ = v ÷ f."),
        (f / v, "λ = v ÷ f."),
        (lam / 100, "Keep the answer in cm: the speed is in cm/s."),
    ], "cm", "λ = v ÷ f", [f"λ = {v} ÷ {f}", f"= **{fmt(lam)} cm**"],
        ["The distance between neighbouring wavefronts is one wavelength.", "v = f λ.", f"{v} ÷ {f}."],
        figure=sketches.wavefronts_sketch(5, "λ = ?"))


@template("c9_ultrasound_wavelength", chapter=9, level=3, lo="9d")
def ultrasound_wavelength(rng):
    f_khz = nice(rng, 30, 50, 75, 150)
    lam_mm = 1500 / f_khz
    table = md_table(["speed of sound in water / m/s", "frequency / kHz"], [[1500, f_khz]])
    return calc_q(rng, f"A sonar device sends ultrasound into water.\n\n{table}\n\nWhat is the wavelength of the ultrasound, in mm?", lam_mm, [
        (lam_mm / 1000, "That is in metres; convert to mm (× 1000)."),
        (1500 / f_khz / 10, "Check the conversion: 1 m = 1000 mm."),
        (f_khz * 1500 / 1e6, "λ = v ÷ f."),
    ], "mm", "λ = v ÷ f (f in Hz), then m → mm", [f"λ = 1500 ÷ {f_khz * 1000} = {fmt(lam_mm / 1000)} m", f"= **{fmt(lam_mm)} mm**"],
        ["Convert kHz to Hz.", "λ = v ÷ f gives metres.", "Multiply by 1000 for mm."])


@template("c9_crests_per_second_speed", chapter=9, level=3, lo="9d")
def crests_per_second_speed(rng):
    n = nice(rng, 2, 3, 4, 5)
    lam = nice(rng, 1.5, 2, 2.5, 4)
    v = n * lam
    return calc_q(rng, f"Fig. 1 shows water waves passing a pier. **{n} crests** pass the pier each second and the crests are **{fmt(lam)} m** apart. What is the speed of the waves?", v, [
        (lam / n, "v = f λ: multiply."),
        (n / lam, "v = f λ."),
        (n + lam, "Multiply frequency by wavelength."),
    ], "m/s", "f = crests per second; v = f λ", [f"f = {n} Hz, λ = {fmt(lam)} m", f"v = {n} × {fmt(lam)}", f"= **{fmt(v)} m/s**"],
        ["The number of crests per second is the frequency.", "The distance between crests is the wavelength.", "v = f λ."],
        figure=sketches.wave_graph(1, lam, kind="distance_m", cycles=3))


# ---------------------------------------------------------------- L4
@template("c9_sonar_depth", chapter=9, level=4, lo="9i")
def sonar_depth(rng):
    t = nice(rng, 0.04, 0.08, 0.1, 0.2, 0.4)
    d = 1500 * t / 2
    return calc_q(rng, f"Fig. 1 shows a ship sending a sound pulse to the sea bed. The echo returns after **{fmt(t)} s**. Sound travels at **1500 m/s** in sea water. How deep is the sea?", d, [
        (1500 * t, "The pulse goes down AND back up: halve the total distance."),
        (340 * t / 2, "Use the speed of sound in WATER, not air."),
        (1500 / t / 2, "distance = speed × time."),
    ], "m", "depth = v × t ÷ 2", [f"total path = 1500 × {fmt(t)} = {fmt(1500 * t)} m", f"depth = {fmt(1500 * t)} ÷ 2", f"= **{fmt(d)} m**"],
        ["The pulse travels to the sea bed and back.", "Use 1500 m/s.", "Halve the total path."],
        figure=sketches.echo_sketch("depth = ?", f"echo after {fmt(t)} s", left="ship", right="sea bed", wave="sound pulse", person=False))


@template("c9_echo_speed_of_sound", chapter=9, level=4, lo="9i")
def echo_speed_of_sound(rng):
    d = nice(rng, 85, 102, 136, 170)
    v = 340
    t = 2 * d / v
    return calc_q(rng, f"Fig. 1 shows a student **{d} m** from a wall. She claps and hears the echo **{fmt(t)} s** later. What is the speed of sound found from this?", v, [
        (d / t, "The sound travels to the wall and BACK: the distance is 2d."),
        (d * t, "speed = distance ÷ time."),
        (d / t / 2, "Double the distance, do not halve the speed."),
    ], "m/s", "v = 2d ÷ t", [f"distance travelled = 2 × {d} = {2 * d} m", f"v = {2 * d} ÷ {fmt(t)}", f"= **{fmt(v)} m/s**"],
        ["How far does the sound travel before she hears the echo?", "There and back = 2d.", "v = 2d ÷ t."],
        figure=sketches.echo_sketch(f"{d} m", f"echo heard after {fmt(t)} s"))


@template("c9_freq_from_ms_graph", chapter=9, level=4, lo="9c")
def freq_from_ms_graph(rng):
    T = nice(rng, 2, 4, 5, 8, 10)
    f = 1000 / T
    return calc_q(rng, "Fig. 1 shows the displacement–time graph of a vibrating loudspeaker cone. What is the frequency of the sound?", f, [
        (1 / T, "Convert the period from ms to s before finding 1 ÷ T."),
        (T, "That is the period in ms."),
        (1000 / (2 * T), "One period is a full cycle, crest to crest."),
    ], "Hz", "f = 1 ÷ T with T in s", [f"T = {T} ms = {fmt(T / 1000)} s", f"f = 1 ÷ {fmt(T / 1000)}", f"= **{fmt(f)} Hz**"],
        ["Read the period from the graph.", "Convert ms to s.", "f = 1 ÷ T."],
        figure=sketches.wave_graph(1, T, kind="time_ms", cycles=2))


@template("c9_wavelength_change_medium", chapter=9, level=4, lo="9d")
def wavelength_change_medium(rng):
    f = nice(rng, 500, 680, 850, 1000)
    lam_air = 340 / f
    lam_w = 1500 / f
    table = md_table(["medium", "speed of sound / m/s"], [["air", 340], ["water", 1500]])
    return calc_q(rng, f"A **{f} Hz** sound passes from air into water.\n\n{table}\n\nWhat is its wavelength in water?", lam_w, [
        (lam_air, "That is the wavelength in AIR."),
        (f / 1500, "λ = v ÷ f."),
        (lam_air * 1500 / 340 / 2, "The frequency stays the same; use λ = 1500 ÷ f."),
    ], "m", "frequency unchanged; λ = v_water ÷ f", [f"f stays {f} Hz", f"λ = 1500 ÷ {f}", f"= **{fmt(lam_w)} m**"],
        ["Which quantity does not change when a wave enters a new medium?", "The frequency is set by the source.", "λ = v ÷ f using the speed in water."])


# ---------------------------------------------------------------- L5
@template("c9_two_walls_echoes", chapter=9, level=5, lo="9i")
def two_walls_echoes(rng):
    t1, t2 = rng.choice([(0.5, 0.8), (0.4, 1.0), (0.6, 1.2), (1.0, 1.5)])
    D = 340 * (t1 + t2) / 2
    table = md_table(["echo", "time after the clap / s"], [["from wall A", fmt(t1)], ["from wall B", fmt(t2)]])
    return calc_q(rng, f"A student stands between two tall walls and claps once. She hears two echoes.\n\n{table}\n\nThe speed of sound is 340 m/s. How far apart are the walls?", D, [
        (340 * (t1 + t2), "Each echo time is there-and-back; halve each to get the distance to that wall."),
        (340 * (t2 - t1) / 2, "She is BETWEEN the walls: add the two distances."),
        (340 * t2 / 2, "That is only the distance to wall B."),
    ], "m", "distance to each wall = 340 × t ÷ 2; add them", [f"to A: 340 × {fmt(t1)} ÷ 2 = {fmt(170 * t1)} m", f"to B: 340 × {fmt(t2)} ÷ 2 = {fmt(170 * t2)} m", f"separation = **{fmt(D)} m**"],
        ["Find her distance to each wall from its echo time.", "Remember each echo is a round trip.", "She is between them, so add."])


@template("c9_clap_echo_method", chapter=9, level=5, lo="9i")
def clap_echo_method(rng):
    d = nice(rng, 50, 60, 80, 85)
    n = 20
    v = nice(rng, 320, 340, 350)
    t_total = n * 2 * d / v
    table = md_table(["distance to wall / m", "number of claps (each in time with the echo of the last)", "time for the claps / s"], [[d, n, fmt(t_total, sf=3)]])
    return calc_q(rng, f"A student claps so that each clap coincides with the echo of the one before.\n\n{table}\n\nWhat value for the speed of sound do these results give?", 2 * d * n / t_total, [
        (d * n / t_total, "Between claps the sound travels to the wall AND back: 2d."),
        (2 * d / t_total, "Divide the total time by the number of claps to get the time for ONE echo."),
        (2 * d * t_total / n, "v = 2d ÷ (time between claps)."),
    ], "m/s", "time between claps = total ÷ n; v = 2d ÷ that time",
        [f"time between claps = {fmt(t_total, sf=3)} ÷ {n} = {fmt(t_total / n, sf=3)} s", f"v = 2 × {d} ÷ {fmt(t_total / n, sf=3)}", f"= **{fmt(2 * d * n / t_total)} m/s**"],
        ["Each gap between claps is the time for sound to go to the wall and back.", "Find the time for one gap.", "v = 2d ÷ t."])


@template("c9_depth_change", chapter=9, level=5, lo="9i")
def depth_change(rng):
    t1, t2 = rng.choice([(0.2, 0.12), (0.4, 0.3), (0.1, 0.06), (0.5, 0.36)])
    change = 1500 * (t1 - t2) / 2
    table = md_table(["position", "echo time / s"], [["P", fmt(t1)], ["Q", fmt(t2)]])
    return calc_q(rng, f"A ship measures the echo time of sonar pulses at two places. Sound travels at 1500 m/s in sea water.\n\n{table}\n\nHow much shallower is the sea at Q than at P?", change, [
        (1500 * (t1 - t2), "Each echo time covers the journey down AND up: halve."),
        (1500 * t2 / 2, "That is the depth at Q, not the difference."),
        (340 * (t1 - t2) / 2, "Use the speed of sound in water."),
    ], "m", "depth = 1500 × t ÷ 2 at each place; subtract", [f"depth at P = 1500 × {fmt(t1)} ÷ 2 = {fmt(750 * t1)} m", f"depth at Q = {fmt(750 * t2)} m", f"difference = **{fmt(change)} m**"],
        ["Find each depth from its echo time.", "Halve each round trip.", "Subtract."])


@template("c9_dipper_frequency", chapter=9, level=5, lo="9d")
def dipper_frequency(rng):
    d, t = rng.choice([(30, 2), (45, 3), (60, 4), (36, 2)])
    lam = nice(rng, 1.5, 2, 2.5, 3)
    v = d / t
    f = v / lam
    table = md_table(["distance a wavefront travels / cm", "time / s", "required wavelength / cm"], [[d, t, fmt(lam)]])
    return calc_q(rng, f"In a ripple tank, a student wants waves of a particular wavelength.\n\n{table}\n\nAt what frequency must the dipper vibrate?", f, [
        (d / lam, "First find the wave SPEED (distance ÷ time)."),
        (v * lam, "f = v ÷ λ."),
        (v, "That is the speed in cm/s; divide by the wavelength."),
    ], "Hz", "v = distance ÷ time; f = v ÷ λ", [f"v = {d} ÷ {t} = {fmt(v)} cm/s", f"f = {fmt(v)} ÷ {fmt(lam)}", f"= **{fmt(f)} Hz**"],
        ["The wave speed depends on the water depth, so find it from the measurement.", "v = distance ÷ time.", "Then f = v ÷ λ."])
