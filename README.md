# G3 Physics Trainer

Adaptive self-study MCQ trainer for Sec 3 / Sec 4 G3 Science (Physics), SEAB 5086, all 16 chapters
(Measurement, Kinematics, Force and Pressure, Dynamics, Turning Effects, Energy, Kinetic Particle Model, Thermal Processes,
Waves, Electromagnetic Spectrum, Light, Electric Charge and Current, D.C. Circuits, Practical Electricity, Magnetism and
Electromagnetism, Radioactivity). Streamlit app, no database.

## How it works

- Students log in with **name + class** (no password). Teacher view is password protected.
- Three categories: **Calculation** (411 parametrised templates, L1–L5, numbers change every time, every one with a diagram or data
  table drawn to match), **Explanation** (417 recall / identify / apply / evaluate MCQs at L1–L5, many with diagrams) and **Written
  answer** (1200 questions: 75 per chapter for all 16 chapters, 15 per level). Every chapter and level has at least 3 calculation and
  3 explanation questions (tested). Chapters 7, 8 and 15 have no calculation outcomes in the syllabus, so they appear under
  Explanation and Written answer only.
- **Written answers are marked by meaning, not word for word** (`trainer/marker.py`, no LLM): each question has marking points with
  many alternative phrasings; words match after light stemming with one spelling slip allowed, phrase words may appear in any order
  within a short window, and common wrong ideas ("cold flows in") are caught as pitfalls. Superscript and subscript digits read as
  digits (R₁ = R1, 10⁶ = 10^6), hyphenated words split ("high-resistance"), and "into the page" never matches "out of the page". The student sees how many points they
  have, which ones, and any pitfall message; hints and key words come from the same tutor panel; one edit-and-resubmit retry.
- **5 correct in a row → level up. 3 wrong in a row → level down.** Everyone starts at L1.
- Questions are dealt like a shuffled deck: no question comes back until the student has seen every question in that pool
  (chapter, level, category); after that only the least recently seen half can come up, never the one just answered.
- A wrong answer opens the scripted **tutor**: a message about the chosen option, up to 3 hints, the formula on request, then one retry
  (correct retries never count towards the streak). Explanation L1 questions come back until answered correctly.
- **Teacher dashboard** (sidebar → Teacher, or `?teacher=1`): who is online, levels, streaks, accuracy, last 20 attempts,
  reset / clear / CSV. Refreshes every 5 s. Data lives in memory only and disappears when the app restarts.

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

Default local teacher password is `physics`. Set `TEACHER_PASSWORD` as an environment variable or in `.streamlit/secrets.toml` to change it.

## Deploy on Streamlit Community Cloud

1. Push this folder to a GitHub repo (private is fine).
2. share.streamlit.io → **Create app** → pick the repo, branch `main`, main file `app.py`.
3. Advanced settings → **Secrets**:
   ```toml
   TEACHER_PASSWORD = "choose-something"
   ```
4. Deploy. Share the `*.streamlit.app` URL (or a QR code) with students.

Every push to `main` redeploys automatically. Live data is cleared on each redeploy.

## Tests

```bash
python -m pytest -q
```

`tests/test_engine.py` covers the level rules; `tests/test_content.py` builds every template with 20 seeds
(four distinct options, key present, a misconception message for every wrong option, three hints, a PNG figure whenever the stem says "Fig. 1").

## Adding a question

Calculation templates live in `trainer/content/calc_ch*.py`. Copy any existing one:

```python
@template("c3_my_question", chapter=3, level=2, lo="3i")
def my_question(rng):
    F = nice(rng, 20, 50, 80)
    ...
    opts, key, mis = numeric_options(rng, answer, [(wrong1, "why a student gets this"), ...], unit="Pa")
    return dict(stem=..., options=opts, key=key, misconceptions=mis, formula=..., working=[...], hints=[h1, h2, h3], figure=figs.graph(...))
```

Recall MCQs are dicts in `trainer/content/recall.py`. Run the tests afterwards.

## Layout

```
app.py                      entry point: login, routing
trainer/config.py           classes, chapters, rules (5 up / 3 down), refresh interval
trainer/engine.py           adaptive rules (pure Python)
trainer/store.py            in-memory live store shared by all sessions
trainer/figs.py             instrument and graph drawers (micrometer, vernier, stopwatch, cylinders, force diagrams, graphs, blocks)
trainer/sketches.py         scene sketches (motion, journeys, beams, slopes, lifts, waves, echo, wavefronts, EM spectrum, particles, thermal)
trainer/sketches2.py        Ch 11–16 drawers (reflection/refraction/lens rays, circuits, V–I graphs, plugs, magnetic fields, LHR, motor coil, atoms, decay curves, penetration)
trainer/marker.py           meaning-based marker for written answers (marking points, synonyms, spelling tolerance, pitfalls)
trainer/content/            question templates (base helpers, calc_ch*, calc_ch*_more, calc_ch*_x, explain_ch*, explain_x_*, recall*, written_ch1..16, written_ch*_b)
trainer/ui_student.py       student screen + tutor panel
trainer/ui_teacher.py       live dashboard
tests/                      pytest
```
