# G3 Physics Trainer

Adaptive self-study MCQ trainer for Sec 3 / Sec 4 G3 Science (Physics), SEAB 5086, Chapters 1–4
(Measurement, Kinematics, Force and Pressure, Dynamics). Streamlit app, no database.

## How it works

- Students log in with **name + class** (no password). Teacher view is password protected.
- Two categories: **Calculation** (40 parametrised templates, L1–L5, numbers change every time, diagrams drawn to match)
  and **Explanation** (20 recall MCQs at L1–L2 so far).
- **5 correct in a row → level up. 3 wrong in a row → level down.** Everyone starts at L1.
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
trainer/figs.py             diagram drawers (micrometer, vernier, stopwatch, cylinders, force diagrams, graphs, blocks)
trainer/content/            question templates (base helpers, calc_ch1..4, recall)
trainer/ui_student.py       student screen + tutor panel
trainer/ui_teacher.py       live dashboard
tests/                      pytest
```
