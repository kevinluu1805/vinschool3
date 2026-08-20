# VinSchool Quiz — Claude Reference

## What is this project?

A static quiz website (no backend). The user picks question types on a selection screen, gets one random question per type, answers all of them, then verifies to see their score with a detailed breakdown.

Built with: plain HTML + vanilla JS + Tailwind CSS (CDN). Data stored as JSON files.

## How to run

```bash
npm start        # npx serve . → http://localhost:3000
# or
python3 -m http.server 3000
```

Must use a local server — `fetch()` is blocked on `file://`.

## App flow

```
Selection Screen
  → checkboxes, one per question type
  → checked count = number of questions in the quiz
  → click Start

Quiz Screen
  → all questions shown at once (scroll to answer)
  → one random question drawn from each selected type
  → 4 answers: 1 correct + 3 random from wrong_pool, shuffled each time
  → click Verify

Results Screen
  → score card: X/Y and percentage
  → per-question detail: user's answer, correct answer for wrong ones
  → click Try Again → back to Selection
```

## File structure

```
vinschool/
├── index.html                     # App shell — just loads Tailwind + app.js
├── css/style.css                  # Only for .answer-btn and .answer-btn.selected
├── js/app.js                      # All logic (state, templates, events, init)
├── database/
│   ├── question_types.json        # Index — list of all available question types
│   ├── number_sequence.json       # Questions for "Number Sequence"
│   └── sort_numbers.json          # Questions for "Sort Numbers"
├── package.json                   # { "start": "npx serve ." }
├── DESIGN.md                      # Detailed design doc
└── CLAUDE.md                      # This file
```

## js/app.js architecture

Single file, no framework. State machine with three views.

```
state = {
  view: 'selection' | 'quiz' | 'results'
  types: []         ← loaded from question_types.json on init
  selected: Set     ← IDs of checked question types
  quiz: []          ← built when Start is clicked
}
```

Each `quiz` item:
```js
{
  typeId,       // matches the JSON filename
  typeLabel,    // display name
  question,     // question text
  correct,      // correct answer string
  answers,      // shuffled [correct, ...3 wrong] — shown as buttons
  userAnswer,   // null until user clicks an answer
}
```

Key functions:
- `render()` — switches the full `#app` innerHTML based on `state.view`, then calls `attachEvents()`
- `tmplSelection()` / `tmplQuiz()` / `tmplResults()` — return HTML strings
- `startQuiz()` — fetches each selected type's JSON, picks 1 random question, builds `state.quiz`, switches to quiz view
- `selectAnswer(qi, answer)` — updates `state.quiz[qi].userAnswer` and toggles `.selected` class on answer buttons (no re-render)
- `attachEvents()` — wires up event listeners after each render; quiz answers use event delegation on `#quiz-list`

Answer selection avoids full re-render — it only toggles the `.selected` CSS class on the clicked button and removes it from siblings.

## Data format

### `database/question_types.json`

```json
[
  { "id": "number_sequence", "label": "Number Sequence" },
  { "id": "sort_numbers",    "label": "Sort Numbers" }
]
```

`id` must match the filename: `database/<id>.json`.

### `database/<type_id>.json`

```json
[
  {
    "id": 1,
    "question": "Find the next number: 1, 3, 5, 7, ...",
    "correct": "9",
    "wrong_pool": ["8", "10", "11", "12", "13"]
  }
]
```

Rules:
- `correct` and all `wrong_pool` entries are **strings** (keeps the model uniform across all question types)
- `wrong_pool` must have **at least 3** entries (quiz picks exactly 3)
- Having 5+ in `wrong_pool` reduces repetition across quiz runs

## Adding a new question type

1. Add to `database/question_types.json`:
   ```json
   { "id": "odd_one_out", "label": "Odd One Out" }
   ```
2. Create `database/odd_one_out.json` with questions in the format above.
3. No code changes needed — the app loads all types dynamically.

## Hosting

Deployed on GitHub Pages (free). Push to `main`, enable Pages in repo Settings → Pages → Branch: main / root. Live at `https://<username>.github.io/vinschool/`.
