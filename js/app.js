'use strict';

const DB = './database';
const QUESTION_COUNTS = [1, 3, 5, 10];

const state = {
  view: 'selection',   // 'selection' | 'quiz' | 'results'
  types: [],           // [{ id, label }]
  selected: new Set(), // selected type IDs
  counts: {},          // { [typeId]: number } — questions per type, default 1
  quiz: [],            // [{ typeId, typeLabel, question, correct, answers, userAnswer }]
};

// ── Utilities ─────────────────────────────────────────────────────────────────

async function fetchJSON(url) {
  const res = await fetch(url);
  if (!res.ok) throw new Error(`Cannot load ${url}`);
  return res.json();
}

function shuffle(arr) {
  const a = [...arr];
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}

function pickN(arr, n) {
  return shuffle(arr).slice(0, n);
}

function randomItem(arr) {
  return arr[Math.floor(Math.random() * arr.length)];
}

// ── Actions ───────────────────────────────────────────────────────────────────

async function startQuiz() {
  const btn = document.getElementById('btn-start');
  btn.textContent = 'Loading…';
  btn.disabled = true;

  try {
    state.quiz = [];
    for (const typeId of state.selected) {
      const type = state.types.find(t => t.id === typeId);
      const pool = await fetchJSON(`${DB}/${typeId}.json`);
      const count = state.counts[typeId] || 1;
      const questions = pickN(pool, Math.min(count, pool.length));
      for (const q of questions) {
        state.quiz.push({
          typeId,
          typeLabel: type.label,
          question: q.question,
          correct: q.correct,
          answers: shuffle([q.correct, ...pickN(q.wrong_pool, Math.min(3, q.wrong_pool.length))]),
          userAnswer: null,
        });
      }
    }
    state.view = 'quiz';
    render();
  } catch (err) {
    alert(err.message);
    btn.textContent = 'Bắt Đầu';
    btn.disabled = false;
  }
}

function selectAnswer(qi, answer) {
  state.quiz[qi].userAnswer = answer;
  document.querySelectorAll(`[data-question="${qi}"] .answer-btn`).forEach(b => {
    b.classList.toggle('selected', b.dataset.answer === answer);
  });
}

// ── Templates ─────────────────────────────────────────────────────────────────

function tmplSelection() {
  const n = state.selected.size;
  return `
    <div class="space-y-6">
      <div class="text-center pt-4">
        <h1 class="text-3xl font-bold text-slate-800">VinSchool Math Quiz</h1>
      </div>

      <div class="bg-white rounded-2xl shadow-sm border border-slate-200 overflow-hidden">
        <div class="flex items-center px-5 py-2 border-b border-slate-100 bg-slate-50">
          <span class="flex-1"></span>
          <span class="text-xs font-semibold text-slate-400 uppercase tracking-wider">Số lượng câu hỏi</span>
        </div>
        ${state.types.map(t => `
          <label class="flex items-center gap-3 px-5 py-4 cursor-pointer hover:bg-slate-50 transition-colors border-b border-slate-100 last:border-0">
            <input type="checkbox" class="w-5 h-5 accent-blue-600 cursor-pointer flex-shrink-0"
              data-type="${t.id}" ${state.selected.has(t.id) ? 'checked' : ''}>
            <span class="text-slate-700 font-medium flex-1">${t.label}</span>
            <div class="flex items-center gap-1">
              ${QUESTION_COUNTS.map(c => {
                const isChecked = state.selected.has(t.id);
                const active = isChecked && (state.counts[t.id] || 1) === c;
                const cls = !isChecked ? 'bg-slate-100 text-slate-300'
                  : active ? 'bg-blue-600 text-white'
                  : 'bg-slate-100 text-slate-500 hover:bg-slate-200';
                return `<button class="count-btn text-xs font-semibold px-2 py-1 rounded transition-colors ${cls}"
                  data-type="${t.id}" data-count="${c}">${c}</button>`;
              }).join('')}
            </div>
          </label>
        `).join('')}
      </div>

      <div class="text-center">
        <button id="btn-start"
          class="px-10 py-3 rounded-xl font-semibold text-white transition-colors
            ${n > 0 ? 'bg-blue-600 hover:bg-blue-700 cursor-pointer' : 'bg-slate-300 cursor-not-allowed'}"
          ${n === 0 ? 'disabled' : ''}>
          Bắt Đầu
        </button>
      </div>
    </div>`;
}

function tmplQuiz() {
  return `
    <div class="space-y-6">
      <div class="flex items-center justify-between">
        <h2 class="text-2xl font-bold text-slate-800">Quiz</h2>
        <span class="text-sm text-slate-500 bg-white border border-slate-200 rounded-lg px-3 py-1">
          ${state.quiz.length} question${state.quiz.length > 1 ? 's' : ''}
        </span>
      </div>

      <div id="quiz-list" class="space-y-4">
        ${state.quiz.map((q, i) => `
          <div class="bg-white rounded-2xl shadow-sm border border-slate-200 p-5 space-y-4">
            <div class="flex items-center gap-3">
              <span class="flex-shrink-0 w-7 h-7 rounded-full bg-blue-100 text-blue-700 font-bold text-sm flex items-center justify-center">
                ${i + 1}
              </span>
              <p class="text-blue-500 font-semibold">${q.question}</p>
            </div>
            <div class="grid grid-cols-2 gap-2" data-question="${i}">
              ${q.answers.map(ans => `
                <button class="answer-btn" data-q="${i}" data-answer="${ans}">${ans}</button>
              `).join('')}
            </div>
          </div>
        `).join('')}
      </div>

      <div class="text-center pb-6">
        <button id="btn-verify"
          class="px-10 py-3 rounded-xl font-semibold text-white bg-emerald-600 hover:bg-emerald-700 transition-colors cursor-pointer">
          Kiểm tra
        </button>
      </div>
    </div>`;
}

function tmplResults() {
  const correct = state.quiz.filter(q => q.userAnswer === q.correct).length;
  const total = state.quiz.length;
  const pct = Math.round((correct / total) * 100);
  const scoreColor = pct >= 80 ? 'text-emerald-600' : pct >= 50 ? 'text-amber-500' : 'text-red-500';

  return `
    <div class="space-y-6 pb-10">
      <div class="text-center bg-white rounded-2xl shadow-sm border border-slate-200 py-8 px-6">
        <p class="text-xs font-semibold text-slate-400 uppercase tracking-widest">Kết quả</p>
        <p class="text-6xl font-bold ${scoreColor} mt-3">
          ${correct}<span class="text-3xl text-slate-300">/${total}</span>
        </p>
        <p class="text-slate-400 mt-2 text-sm">${pct}% chính xác</p>
      </div>

      <div class="space-y-3">
        ${state.quiz.map((q) => {
          const ok = q.userAnswer === q.correct;
          return `
            <div class="bg-white rounded-2xl shadow-sm border ${ok ? 'border-emerald-200' : 'border-red-200'} p-5">
              <div class="flex items-start gap-3">
                <span class="flex-shrink-0 w-7 h-7 rounded-full
                  ${ok ? 'bg-emerald-100 text-emerald-700' : 'bg-red-100 text-red-500'}
                  font-bold text-sm flex items-center justify-center">
                  ${ok ? '✓' : '✗'}
                </span>
                <div class="flex-1 space-y-2">
                  <div>
                    <p class="text-xs font-semibold text-blue-500 uppercase tracking-wider">${q.typeLabel}</p>
                    <p class="text-slate-700 font-medium mt-0.5">${q.question}</p>
                  </div>
                  <div class="text-sm">
                    <p class="${ok ? 'text-emerald-600' : 'text-red-500'} font-medium">
                      Đáp án của bạn:
                      ${q.userAnswer
                        ? `${q.userAnswer} ${ok ? '✓' : '✗'}`
                        : '<span class="text-slate-400 font-normal italic">Chưa chọn</span>'}
                    </p>
                    ${!ok ? `<p class="text-emerald-600 font-medium mt-0.5">Đáp án đúng: ${q.correct}</p>` : ''}
                  </div>
                </div>
              </div>
            </div>`;
        }).join('')}
      </div>

      <div class="text-center">
        <button id="btn-retry"
          class="px-10 py-3 rounded-xl font-semibold text-white bg-blue-600 hover:bg-blue-700 transition-colors cursor-pointer">
          Làm bài mới
        </button>
      </div>
    </div>`;
}

// ── Render ────────────────────────────────────────────────────────────────────

function render() {
  const app = document.getElementById('app');

  switch (state.view) {
    case 'selection': app.innerHTML = tmplSelection(); break;
    case 'quiz':      app.innerHTML = tmplQuiz();      break;
    case 'results':   app.innerHTML = tmplResults();   break;
  }

  if (state.view === 'selection') {
    document.querySelectorAll('input[type="checkbox"]').forEach(cb => {
      cb.addEventListener('change', () => {
        cb.checked ? state.selected.add(cb.dataset.type) : state.selected.delete(cb.dataset.type);
        localStorage.setItem('selected_types', JSON.stringify([...state.selected]));
        render();
      });
    });
    document.querySelectorAll('.count-btn').forEach(btn => {
      btn.addEventListener('click', e => {
        e.stopPropagation();
        const typeId = btn.dataset.type;
        const count = parseInt(btn.dataset.count);
        state.counts[typeId] = count;
        const saved = JSON.parse(localStorage.getItem('question_counts') || '{}');
        saved[typeId] = count;
        localStorage.setItem('question_counts', JSON.stringify(saved));
        const isChecked = state.selected.has(typeId);
        document.querySelectorAll(`.count-btn[data-type="${typeId}"]`).forEach(b => {
          const active = isChecked && parseInt(b.dataset.count) === count;
          const cls = !isChecked ? 'bg-slate-100 text-slate-300'
            : active ? 'bg-blue-600 text-white'
            : 'bg-slate-100 text-slate-500 hover:bg-slate-200';
          b.className = `count-btn text-xs font-semibold px-2 py-1 rounded transition-colors ${cls}`;
        });
      });
    });
    const btn = document.getElementById('btn-start');
    if (btn && !btn.disabled) btn.addEventListener('click', startQuiz);
  }

  if (state.view === 'quiz') {
    document.getElementById('quiz-list').addEventListener('click', e => {
      const btn = e.target.closest('.answer-btn');
      if (btn) selectAnswer(parseInt(btn.dataset.q), btn.dataset.answer);
    });
    document.getElementById('btn-verify').addEventListener('click', () => {
      state.view = 'results';
      render();
    });
  }

  if (state.view === 'results') {
    document.getElementById('btn-retry').addEventListener('click', () => {
      const saved = JSON.parse(localStorage.getItem('selected_types') || '[]');
      const validIds = new Set(state.types.map(t => t.id));
      state.selected = new Set(saved.filter(id => validIds.has(id)));
      state.quiz = [];
      state.view = 'selection';
      render();
    });
  }
}

// ── Init ──────────────────────────────────────────────────────────────────────

(async () => {
  try {
    state.types = await fetchJSON(`${DB}/question_types.json`);
    const saved = JSON.parse(localStorage.getItem('selected_types') || '[]');
    const validIds = new Set(state.types.map(t => t.id));
    state.selected = new Set(saved.filter(id => validIds.has(id)));
    state.counts = JSON.parse(localStorage.getItem('question_counts') || '{}');
    render();
  } catch (err) {
    document.getElementById('app').innerHTML = `
      <div class="text-center py-20 space-y-2">
        <p class="text-red-500 font-medium">Failed to load: ${err.message}</p>
        <p class="text-slate-400 text-sm">Run a local server: <code class="bg-slate-100 px-2 py-0.5 rounded">npm start</code></p>
      </div>`;
  }
})();
