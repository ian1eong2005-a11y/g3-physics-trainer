"""Chapter 10 Electromagnetic Spectrum: more calculations with c = 3 × 10⁸ m/s (v = f λ, distance = speed × time, radar echoes)."""
from .. import sketches
from .base import fmt, md_table, nice, numeric_options, template

C_KM = 300000  # km/s


# ---------------------------------------------------------------- L1
@template("c10_light_distance", chapter=10, level=1, lo="10a")
def light_distance(rng):
    t = nice(rng, 0.5, 1.2, 1.3, 2, 4, 8, 20)
    d = C_KM * t
    opts, key, mis = numeric_options(rng, d, [
        (C_KM / t, "You divided. distance = speed × time."),
        (d * 1000, "The speed is already in km/s, so the answer is already in km."),
        (d / 2, "There is no echo here; the signal travels the distance only once."),
    ], unit="km", sf=3)
    return dict(
        stem=f"Fig. 1 shows the electromagnetic spectrum. A light signal travels through space for **{fmt(t)} s**. Light travels at **300 000 km/s**. How far does it travel?",
        figure=sketches.em_spectrum(highlight="visible light"),
        options=opts, key=key, misconceptions=mis,
        formula="distance = speed × time",
        working=["distance = speed × time", f"= 300 000 × {fmt(t)}", f"= **{fmt(d)} km**"],
        hints=["All electromagnetic waves travel at the same speed in a vacuum.",
               "distance = speed × time.",
               f"300 000 × {fmt(t)}."],
    )


@template("c10_light_time", chapter=10, level=1, lo="10a")
def light_time(rng):
    t = nice(rng, 0.1, 0.2, 0.5, 1.5, 2, 3)
    d = C_KM * t
    opts, key, mis = numeric_options(rng, t, [
        (d * C_KM, "You multiplied. time = distance ÷ speed."),
        (C_KM / d, "You divided the wrong way round. time = distance ÷ speed."),
        (t * 2, "The signal makes the journey once, so do not double."),
    ], unit="s", sf=3)
    return dict(
        stem=f"Fig. 1 shows the electromagnetic spectrum. A radio signal travels **{fmt(d)} km** through space at **300 000 km/s**. How long does it take?",
        figure=sketches.em_spectrum(highlight="radio waves"),
        options=opts, key=key, misconceptions=mis,
        formula="time = distance ÷ speed",
        working=["time = distance ÷ speed", f"= {fmt(d)} ÷ 300 000", f"= **{fmt(t)} s**"],
        hints=["Radio waves are electromagnetic waves, so they travel at the speed of light.",
               "time = distance ÷ speed.",
               f"{fmt(d)} ÷ 300 000."],
    )


@template("c10_frequency_from_lambda_m", chapter=10, level=1, lo="10a")
def frequency_from_lambda_m(rng):
    lam = nice(rng, 1, 1.5, 2, 3, 5, 6, 10)
    f = 300 / lam
    opts, key, mis = numeric_options(rng, f, [
        (lam / 300, "You divided the wrong way round. f = c ÷ λ."),
        (300 * lam, "You multiplied. f = c ÷ λ."),
        (f * 1000, "Check the units: 3 × 10⁸ m/s ÷ λ gives Hz; ÷ 10⁶ for MHz."),
    ], unit="MHz", sf=3)
    return dict(
        stem=f"Fig. 1 shows the electromagnetic spectrum. A radio wave has a wavelength of **{fmt(lam)} m**. Taking the speed of radio waves as **3 × 10⁸ m/s**, what is its frequency in MHz (1 MHz = 10⁶ Hz)?",
        figure=sketches.em_spectrum(highlight="radio waves"),
        options=opts, key=key, misconceptions=mis,
        formula="c = f λ, so f = c ÷ λ",
        working=[f"f = 3 × 10⁸ ÷ {fmt(lam)} = {fmt(3e8 / lam, sf=4)} Hz", f"= **{fmt(f)} MHz**"],
        hints=["Use wave speed = frequency × wavelength.",
               "Rearrange for f: f = c ÷ λ.",
               f"3 × 10⁸ ÷ {fmt(lam)}, then divide by 10⁶."],
    )


# ---------------------------------------------------------------- L2
@template("c10_wavelength_cm_from_ghz", chapter=10, level=2, lo="10a")
def wavelength_cm_from_ghz(rng):
    f = nice(rng, 1, 1.5, 2, 2.5, 3, 5, 6, 10)
    lam_cm = 30 / f
    opts, key, mis = numeric_options(rng, lam_cm, [
        (lam_cm / 100, "That is the wavelength in metres; the question asks for cm."),
        (f / 30, "You divided the wrong way round. λ = c ÷ f."),
        (lam_cm * 10, "Check the conversion: 1 GHz = 10⁹ Hz."),
    ], unit="cm", sf=3)
    return dict(
        stem=f"Fig. 1 shows the electromagnetic spectrum. A Wi-Fi router emits microwaves of frequency **{fmt(f)} GHz** (1 GHz = 10⁹ Hz). Taking c = 3 × 10⁸ m/s, what is their wavelength in **cm**?",
        figure=sketches.em_spectrum(highlight="microwaves"),
        options=opts, key=key, misconceptions=mis,
        formula="λ = c ÷ f, then × 100 for cm",
        working=[f"λ = 3 × 10⁸ ÷ ({fmt(f)} × 10⁹) = {fmt(lam_cm / 100)} m", f"= **{fmt(lam_cm)} cm**"],
        hints=["Convert GHz to Hz first.",
               "λ = c ÷ f gives the wavelength in metres.",
               "Multiply metres by 100 to get cm."],
    )


@template("c10_radar_distance", chapter=10, level=2, lo="10a")
def radar_distance(rng):
    t_us = nice(rng, 20, 40, 60, 100, 120, 200)
    d = 300 * t_us / 2
    opts, key, mis = numeric_options(rng, d, [
        (300 * t_us, "The pulse goes there AND back. Halve the total distance."),
        (300 * t_us / 4, "Halve only once: the echo time covers the journey there and back."),
        (t_us / 300, "You divided. distance = speed × time."),
    ], unit="m", sf=3)
    return dict(
        stem=f"Fig. 1 shows a radar station sending a pulse of microwaves towards a ship. The echo returns after **{t_us} μs** (1 μs = 10⁻⁶ s). Microwaves travel at 3 × 10⁸ m/s. How far away is the ship?",
        figure=sketches.echo_sketch("d = ?", f"echo after {t_us} μs", left="radar", right="ship", wave="microwave pulse", back="reflected pulse", person=False),
        options=opts, key=key, misconceptions=mis,
        formula="distance = speed × time ÷ 2 (there and back)",
        working=[f"total path = 3 × 10⁸ × {t_us} × 10⁻⁶ = {fmt(300 * t_us)} m", f"distance = {fmt(300 * t_us)} ÷ 2", f"= **{fmt(d)} m**"],
        hints=["The pulse travels to the ship and back.",
               "In 1 μs light travels 300 m.",
               f"Total path = 300 × {t_us} m; halve it."],
    )


@template("c10_wavelength_ratio", chapter=10, level=2, lo="10a")
def wavelength_ratio(rng):
    lam1 = nice(rng, 2, 3, 4, 6, 12)
    k = nice(rng, 2, 3, 4)
    lam2 = lam1 / k
    table = md_table(["wave", "frequency", "wavelength / m"], [["P", "f", fmt(lam1)], ["Q", f"{k}f", "?"]])
    opts, key, mis = numeric_options(rng, lam2, [
        (lam1 * k, "All EM waves have the same speed, so a HIGHER frequency means a SHORTER wavelength."),
        (lam1, "The wavelength changes when the frequency changes, because c is fixed."),
        (lam1 - k, "Wavelength is inversely proportional to frequency: divide, do not subtract."),
    ], unit="m", sf=3)
    return dict(
        stem=f"The table gives data for two electromagnetic waves P and Q travelling in a vacuum.\n\n{table}\n\nWhat is the wavelength of Q?",
        options=opts, key=key, misconceptions=mis,
        formula="c = f λ is the same for both, so λ ∝ 1 / f",
        working=[f"f λ is constant; Q has {k} times the frequency", f"λ_Q = {fmt(lam1)} ÷ {k}", f"= **{fmt(lam2)} m**"],
        hints=["What is the same for all electromagnetic waves in a vacuum?",
               "If f λ is fixed and f is multiplied by a number, what happens to λ?",
               f"{fmt(lam1)} ÷ {k}."],
    )


# ---------------------------------------------------------------- L3
@template("c10_wavelength_nm", chapter=10, level=3, lo="10a")
def wavelength_nm(rng):
    f14 = nice(rng, 4, 5, 6, 7.5)
    lam_nm = 3000 / f14
    opts, key, mis = numeric_options(rng, lam_nm, [
        (lam_nm / 1000, "1 nm = 10⁻⁹ m, so multiply the wavelength in m by 10⁹, not 10⁶."),
        (f14 / 3, "You divided the wrong way round. λ = c ÷ f."),
        (lam_nm * 10, "Check the powers of ten: (3 × 10⁸) ÷ (f × 10¹⁴)."),
    ], unit="nm", sf=3)
    return dict(
        stem=f"Fig. 1 shows the electromagnetic spectrum. A beam of visible light has frequency **{fmt(f14)} × 10¹⁴ Hz**. Taking c = 3 × 10⁸ m/s, what is its wavelength in nanometres (1 nm = 10⁻⁹ m)?",
        figure=sketches.em_spectrum(highlight="visible light"),
        options=opts, key=key, misconceptions=mis,
        formula="λ = c ÷ f; 1 m = 10⁹ nm",
        working=[f"λ = 3 × 10⁸ ÷ ({fmt(f14)} × 10¹⁴) = {fmt(lam_nm)} × 10⁻⁹ m", f"= **{fmt(lam_nm)} nm**"],
        hints=["λ = c ÷ f.",
               "10⁸ ÷ 10¹⁴ = 10⁻⁶; then express the answer in units of 10⁻⁹ m.",
               f"3 ÷ {fmt(f14)} = {fmt(3 / f14)}, so λ = {fmt(3 / f14)} × 10⁻⁶ m."],
    )


@template("c10_satellite_delay_ms", chapter=10, level=3, lo="10a")
def satellite_delay_ms(rng):
    d_km = nice(rng, 20000, 24000, 30000, 36000, 42000)
    t_ms = d_km / C_KM * 1000
    opts, key, mis = numeric_options(rng, t_ms, [
        (t_ms / 1000, "That is the time in seconds; the question asks for milliseconds."),
        (t_ms * 2, "The signal travels from the satellite to the ground once, so do not double."),
        (d_km / 3e8 * 1000, "You used c in m/s with the distance in km. Use matching units."),
    ], unit="ms", sf=3)
    return dict(
        stem=f"Fig. 1 shows a navigation satellite **{d_km} km** above a receiver. Its radio signal travels at 3 × 10⁸ m/s. How long does the signal take to reach the receiver, in milliseconds?",
        figure=sketches.echo_sketch(f"{d_km} km", "t = ?", left="receiver", right="satellite", wave="radio signal", back=None, person=False),
        options=opts, key=key, misconceptions=mis,
        formula="time = distance ÷ speed; 1 s = 1000 ms",
        working=[f"t = {d_km} km ÷ 300 000 km/s = {fmt(t_ms / 1000)} s", f"= **{fmt(t_ms)} ms**"],
        hints=["Use the same distance unit in the distance and the speed (3 × 10⁸ m/s = 300 000 km/s).",
               "time = distance ÷ speed.",
               "Multiply seconds by 1000 to get ms."],
    )


# ---------------------------------------------------------------- L4
@template("c10_period_ns", chapter=10, level=4, lo="10a")
def period_ns(rng):
    f_mhz = nice(rng, 50, 100, 125, 200, 250, 500)
    T_ns = 1000 / f_mhz
    lam = 300 / f_mhz
    opts, key, mis = numeric_options(rng, T_ns, [
        (lam, "That is the wavelength in metres, not the period."),
        (f_mhz / 1000, "You inverted the wrong way: T = 1 ÷ f."),
        (T_ns * 1000, "Check the units: 1 ÷ (10⁶ Hz) = 10⁻⁶ s = 1000 ns."),
    ], unit="ns", sf=3)
    table = md_table(["signal", "frequency / MHz"], [["radio", f_mhz]])
    return dict(
        stem=f"The table gives the frequency of a radio signal.\n\n{table}\n\nWhat is the period of the wave in nanoseconds (1 ns = 10⁻⁹ s)?",
        options=opts, key=key, misconceptions=mis,
        formula="T = 1 ÷ f",
        working=[f"f = {f_mhz} × 10⁶ Hz", f"T = 1 ÷ ({f_mhz} × 10⁶) = {fmt(T_ns)} × 10⁻⁹ s", f"= **{fmt(T_ns)} ns**"],
        hints=["Period and frequency are reciprocals.",
               "Convert MHz to Hz first.",
               f"1 ÷ ({f_mhz} × 10⁶) s, then express in ns."],
    )


@template("c10_radar_echo_time", chapter=10, level=4, lo="10a")
def radar_echo_time(rng):
    d_km = nice(rng, 15, 30, 45, 60, 90, 120)
    t_us = 2 * d_km * 1000 / 300
    opts, key, mis = numeric_options(rng, t_us, [
        (t_us / 2, "That is the time to reach the aircraft. The echo must travel back too."),
        (t_us / 1000, "Check your units: the answer should be in μs."),
        (t_us * 2, "Double only once: there and back."),
    ], unit="μs", sf=3)
    return dict(
        stem=f"Fig. 1 shows a radar pulse sent towards an aircraft **{d_km} km** away. Radar waves travel at 3 × 10⁸ m/s. After how many microseconds does the echo return?",
        figure=sketches.echo_sketch(f"{d_km} km", "echo time = ?", left="radar", right="aircraft", wave="radar pulse", back="echo", person=False),
        options=opts, key=key, misconceptions=mis,
        formula="time = 2 × distance ÷ speed",
        working=[f"path = 2 × {d_km} km = {2 * d_km * 1000} m", f"t = {2 * d_km * 1000} ÷ 3 × 10⁸ = {fmt(t_us)} × 10⁻⁶ s", f"= **{fmt(t_us)} μs**"],
        hints=["The pulse goes to the aircraft and back.",
               "Convert km to m, then t = distance ÷ speed.",
               "1 μs = 10⁻⁶ s."],
    )


# ---------------------------------------------------------------- L5
@template("c10_wavelength_change", chapter=10, level=5, lo="10a")
def wavelength_change(rng):
    f1, f2 = rng.choice([(100, 150), (75, 100), (60, 100), (120, 200), (150, 300)])
    l1, l2 = 300 / f1, 300 / f2
    change = l1 - l2
    opts, key, mis = numeric_options(rng, change, [
        (300 / (f2 - f1), "You found the wavelength for the CHANGE in frequency. Work out each wavelength, then subtract."),
        (l1 + l2, "You added the wavelengths. The change is the difference."),
        (l2, "That is the new wavelength, not the change."),
    ], unit="m", sf=3)
    table = md_table(["station", "frequency / MHz"], [["first", f1], ["second", f2]])
    return dict(
        stem=f"A radio is retuned from one station to another.\n\n{table}\n\nTaking c = 3 × 10⁸ m/s, by how much does the wavelength received change?",
        options=opts, key=key, misconceptions=mis,
        formula="λ = c ÷ f for each station; change = λ₁ − λ₂",
        working=[f"λ₁ = 300 ÷ {f1} = {fmt(l1)} m", f"λ₂ = 300 ÷ {f2} = {fmt(l2)} m", f"change = **{fmt(change)} m** (shorter)"],
        hints=["Find each wavelength separately using λ = c ÷ f.",
               "With f in MHz, λ in metres = 300 ÷ f.",
               "Subtract the two wavelengths."],
    )


@template("c10_laser_moon", chapter=10, level=5, lo="10a")
def laser_moon(rng):
    t = nice(rng, 2.50, 2.52, 2.56, 2.60, 2.64)
    d = C_KM * t / 2
    opts, key, mis = numeric_options(rng, d, [
        (C_KM * t, "The pulse goes to the Moon AND back. Halve the total path."),
        (C_KM * t / 4, "Halve once only."),
        (C_KM / t, "You divided. distance = speed × time."),
    ], unit="km", sf=3)
    return dict(
        stem=f"Fig. 1 shows a laser pulse fired at a reflector on the Moon. The reflected pulse is detected **{fmt(t)} s** later. Light travels at 300 000 km/s. How far away is the Moon?",
        figure=sketches.echo_sketch("d = ?", f"pulse returns after {fmt(t)} s", left="laser", right="Moon", wave="laser pulse", back="reflected pulse", person=False),
        options=opts, key=key, misconceptions=mis,
        formula="distance = speed × time ÷ 2",
        working=[f"total path = 300 000 × {fmt(t)} = {fmt(C_KM * t)} km", f"distance = {fmt(C_KM * t)} ÷ 2", f"= **{fmt(d)} km**"],
        hints=["The light travels to the Moon and back in that time.",
               "Total path = speed × time.",
               "Halve the total path."],
    )
