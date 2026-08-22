# VinSchool Quiz — Design

## Overview

Static HTML + JS quiz website. No backend. Data stored as JSON files in `database/`.

## Flow

```
Selection Screen
  → user checks question type checkboxes
  → clicks Start
Quiz Screen
  → one random question per selected type, all shown at once
  → user picks one answer per question
  → clicks Verify
Results Screen
  → shows score (X/Y) and per-question detail
  → Try Again returns to Selection Screen
```

## File Structure

```
vinschool/
├── index.html                    # App shell
├── css/style.css                 # Custom styles (answer-btn states)
├── js/app.js                     # All app logic
├── database/
│   ├── question_types.json       # Index of all question types
│   ├── number_sequence.json      # Questions for "Number Sequence"
│   └── sort_numbers.json         # Questions for "Sort Numbers"
└── package.json                  # npm start → npx serve .
```

## Data Format

### `database/question_types.json`

Array of `{ id, label }`. The `id` must match the filename in `database/`.

```json
[
  { "id": "number_sequence", "label": "Number Sequence" },
  { "id": "sort_numbers",    "label": "Sort Numbers" }
]
```

### `database/<type_id>.json`

Array of questions. Each question has:

| Field        | Type       | Description                                              |
|-------------|------------|----------------------------------------------------------|
| `id`         | number     | Unique within the file                                   |
| `question`   | string     | Question text shown to user                              |
| `correct`    | string     | The one correct answer                                   |
| `wrong_pool` | string[]   | Pool of wrong answers — **must have at least 3** entries |
| `figure`     | string     | *(optional, future)* Path to an HTML fragment file for visual content — see [Figure Support](#figure-support-future) |

The quiz picks 3 random entries from `wrong_pool` each time, so having 5+ makes repetition less likely.

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

## Adding a New Question Type

1. Add an entry to `database/question_types.json`:
   ```json
   { "id": "odd_one_out", "label": "Odd One Out" }
   ```
2. Create `database/odd_one_out.json` with questions in the format above.

## Running Locally

Fetch requests require an HTTP server (not `file://`):

```bash
npm start          # npx serve .
# or
python3 -m http.server
```

Then open `http://localhost:3000` (or the port shown).

## Quiz Logic

- **Selection**: one checkbox per question type. Checked count = question count.
- **Question picking**: one random question drawn from each selected type's pool each time Start is clicked.
- **Answer display**: 4 options shown in random order — 1 correct + 3 randomly chosen from `wrong_pool`. Order shuffled every run.
- **Scoring**: correct = `userAnswer === correct` (string equality).
- **Results**: score card + per-question breakdown showing user's answer and correct answer for wrong ones.

## Figure Support (Future)

Questions can optionally reference a separate HTML fragment file for visual content (shapes, diagrams, images) instead of embedding raw HTML in the JSON.

**JSON field:** `"figure": "database/figures/<type_id>_q1.html"`

**File structure:**
```
database/
  figures/
    linear_nonlinear_q1.html
    linear_nonlinear_q2.html
```

**Figure file format:** plain HTML fragment, no `<html>`/`<body>` wrapper. Tailwind classes work since they're loaded globally.

```html
<div class="flex gap-4 items-center justify-center py-2">
  <div class="w-8 h-8 rounded-full bg-blue-500"></div>
  <div class="w-8 h-8 bg-blue-500"></div>
  <span class="text-2xl text-slate-400">?</span>
</div>
```

**How it works (when implemented):**
- `startQuiz()` fetches the figure file content alongside the question JSON (in parallel)
- Stores the raw HTML as `figureHtml` in the quiz state item
- `tmplQuiz()` and `tmplResults()` render it below the question text if present
- Questions without a `figure` field are unaffected

## State Machine

```
state.view: 'selection' → 'quiz' → 'results' → 'selection'
```

State is in-memory only; refreshing the page resets everything.
