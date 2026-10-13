'use strict';

const APP_CONFIG = window.APP_CONFIG || {};
const DB = APP_CONFIG.db || window.DB_PATH || './database';
const QUESTION_COUNTS = [1, 3, 5, 10];

let _settingsOutsideListener = null;

const state = {
  view: 'selection',   // 'selection' | 'quiz' | 'results'
  types: [],           // [{ id, label }]
  selected: new Set(), // selected type IDs
  counts: {},          // { [typeId]: number } — questions per type, default 1
  quiz: [],            // [{ typeId, typeLabel, question, correct, answers, userAnswer }]
  settings: {
    help: APP_CONFIG.showSettings !== false,
  },
  theories: [],
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

function normalize(str) {
  return str.normalize('NFD').replace(/[̀-ͯ]/g, '').toLowerCase();
}

function renderTheoryList(query) {
  const body = document.getElementById('theory-body');
  if (!body) return;
  const q = normalize(query || '');
  const results = q
    ? state.theories.filter(t => normalize(t.title).includes(q) || normalize(t.content).includes(q))
    : state.theories;
  if (results.length === 0) {
    body.innerHTML = '<p class="text-slate-400 text-sm text-center py-4">Không tìm thấy kết quả.</p>';
    return;
  }
  body.innerHTML = results.map(t => `
    <div class="border border-slate-100 rounded-xl p-4 space-y-1">
      <p class="font-semibold text-slate-800 text-sm">${t.title}</p>
      <p class="text-slate-600 text-sm leading-relaxed">${t.content}</p>
    </div>
  `).join('');
}

// ── Actions ───────────────────────────────────────────────────────────────────

async function startRandom() {
  const btn = document.getElementById('btn-start');
  btn.textContent = 'Loading…';
  btn.disabled = true;

  try {
    const allQuestions = [];
    for (const type of state.types) {
      const pool = await fetchJSON(`${DB}/${type.id}.json`);
      for (const q of pool) allQuestions.push({ type, q });
    }
    const picked = pickN(allQuestions, 20);
    state.quiz = shuffle(picked.map(({ type, q }) => ({
      typeId: type.id,
      typeLabel: type.label,
      question: q.question,
      correct: q.correct,
      answers: shuffle([q.correct, ...pickN(q.wrong_pool, Math.min(3, q.wrong_pool.length))]),
      userAnswer: null,
      hint: q.hint || null,
    })));
    state.view = 'quiz';
    render();
  } catch (err) {
    alert(err.message);
    btn.textContent = 'Làm ngẫu nhiên';
    btn.disabled = false;
  }
}

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
          hint: q.hint || null,
        });
      }
    }
    state.quiz = shuffle(state.quiz);
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
  const totalQ = [...state.selected].reduce((sum, id) => sum + (state.counts[id] || 1), 0);
  return `
    <div class="space-y-6">
      <div class="flex items-center pt-4">
        <a href="../" class="flex items-center gap-1.5 text-sm text-slate-400 hover:text-blue-600 transition-colors">
          <i class="fa-solid fa-arrow-left text-xs"></i>
          Chọn môn
        </a>
        <h1 class="flex-1 text-center text-3xl font-bold text-slate-800 ${APP_CONFIG.showSettings !== false ? 'pr-16' : ''}">${APP_CONFIG.subject || 'Toán'}</h1>
      </div>

      ${APP_CONFIG.showSettings !== false ? `
      <div class="relative flex justify-end" id="settings-wrapper">
        <button id="btn-settings"
          class="flex items-center gap-2 text-sm font-medium text-slate-600 hover:text-slate-900 bg-white border border-slate-200 rounded-lg px-3 py-1.5 transition-colors shadow-sm">
          <i class="fa-solid fa-gear"></i>
          Cài Đặt
        </button>
        <div id="settings-dropdown"
          class="hidden absolute right-0 top-10 bg-white rounded-xl shadow-lg border border-slate-200 w-52 z-10 py-1">
          <label class="flex items-center gap-3 px-4 py-3 cursor-pointer hover:bg-slate-50 transition-colors rounded-xl">
            <input type="checkbox" id="setting-help" class="w-4 h-4 accent-blue-600 cursor-pointer"
              ${state.settings.help ? 'checked' : ''}>
            <span class="text-slate-700 text-sm">${APP_CONFIG.settingsLabel || 'Cho xem lý thuyết'}</span>
          </label>
        </div>
      </div>
      ` : ''}

      <div class="bg-white rounded-2xl shadow-sm border border-slate-200 overflow-hidden">
        <label class="flex items-center gap-3 px-5 py-3 cursor-pointer hover:bg-slate-100 transition-colors border-b border-slate-200 bg-slate-50">
          <input type="checkbox" id="cb-select-all" class="w-5 h-5 accent-blue-600 cursor-pointer flex-shrink-0"
            ${state.selected.size === state.types.length ? 'checked' : ''}>
          <span class="text-slate-600 font-semibold flex-1 text-sm">Chọn tất cả</span>
          <span class="text-xs font-semibold text-slate-400 uppercase tracking-wider">Số lượng câu hỏi</span>
        </label>
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
          class="px-10 py-3 rounded-xl font-semibold text-white transition-colors cursor-pointer
            ${n > 0 ? 'bg-blue-600 hover:bg-blue-700' : 'bg-emerald-600 hover:bg-emerald-700'}">
          ${n === 0 ? 'Làm ngẫu nhiên' : `Bắt đầu làm ${totalQ} câu hỏi`}
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
            ${q.hint && state.settings.help ? `
            <div>
              <button class="hint-btn text-xs text-slate-400 hover:text-blue-600 underline mt-1 transition-colors" data-q="${i}">Xem gợi ý</button>
              <p class="hint-text hidden text-xs text-amber-600 bg-amber-50 rounded-lg px-3 py-2 mt-1" data-q="${i}">${q.hint}</p>
            </div>
            ` : ''}
          </div>
        `).join('')}
      </div>

      <div class="text-center pb-6">
        <button id="btn-verify"
          class="px-10 py-3 rounded-xl font-semibold text-white bg-emerald-600 hover:bg-emerald-700 transition-colors cursor-pointer">
          Kiểm tra
        </button>
      </div>
    </div>

    ${state.settings.help && APP_CONFIG.hasTheory ? `
    <button id="btn-help"
      class="fixed bottom-6 right-6 w-14 h-14 rounded-full bg-blue-600 hover:bg-blue-700 text-white shadow-lg flex items-center justify-center text-xl transition-colors z-40">
      <i class="fa-solid fa-book-open"></i>
    </button>

    <div id="help-modal-overlay" class="hidden fixed inset-0 bg-black/40 z-50 flex items-start justify-center p-4 pt-6">
      <div class="bg-white rounded-2xl shadow-xl w-full max-w-lg flex flex-col" style="max-height:80vh">
        <div class="flex items-center justify-between px-5 py-4 border-b border-slate-100">
          <h3 class="text-lg font-bold text-slate-800">Lý thuyết</h3>
          <button id="btn-help-close" class="w-8 h-8 flex items-center justify-center rounded-lg text-slate-400 hover:text-slate-700 hover:bg-slate-100 transition-colors">
            <i class="fa-solid fa-xmark text-lg"></i>
          </button>
        </div>
        <div class="px-5 py-3 border-b border-slate-100">
          <div class="relative">
            <i class="fa-solid fa-magnifying-glass absolute left-3 top-1/2 -translate-y-1/2 text-slate-400 text-sm"></i>
            <input id="help-search" type="text" placeholder="Tìm kiếm..."
              class="w-full pl-9 pr-4 py-2 rounded-lg border border-slate-200 text-base text-slate-700 placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-blue-400">
          </div>
        </div>
        <div id="theory-body" class="overflow-y-auto flex-1 px-5 py-4 space-y-3">
          <p class="text-slate-400 text-sm text-center">Đang tải...</p>
        </div>
      </div>
    </div>
    ` : ''}`;
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
        <p class="text-slate-400 mt-2 text-sm">${pct}% chính xác${state.settings.help && state.quiz.some(q => q.hint) ? ' (có sử dụng gợi ý)' : ''}</p>
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
                    ${!ok && q.hint ? `<p class="text-amber-600 text-xs mt-1">Gợi ý: ${q.hint}</p>` : ''}
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
    document.querySelectorAll('input[data-type]').forEach(cb => {
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
        const startBtn = document.getElementById('btn-start');
        if (startBtn && state.selected.size > 0) {
          const totalQ = [...state.selected].reduce((sum, id) => sum + (state.counts[id] || 1), 0);
          startBtn.textContent = `Bắt đầu làm ${totalQ} câu hỏi`;
        }
      });
    });
    const cbSelectAll = document.getElementById('cb-select-all');
    if (cbSelectAll) {
      cbSelectAll.indeterminate = state.selected.size > 0 && state.selected.size < state.types.length;
      cbSelectAll.addEventListener('change', () => {
        if (cbSelectAll.checked) {
          state.types.forEach(t => state.selected.add(t.id));
        } else {
          state.selected.clear();
        }
        localStorage.setItem('selected_types', JSON.stringify([...state.selected]));
        render();
      });
    }

    const btn = document.getElementById('btn-start');
    if (btn) btn.addEventListener('click', state.selected.size === 0 ? startRandom : startQuiz);

    const settingsBtn = document.getElementById('btn-settings');
    const settingsDropdown = document.getElementById('settings-dropdown');
    if (settingsBtn) {
      if (_settingsOutsideListener) {
        document.removeEventListener('click', _settingsOutsideListener);
      }
      _settingsOutsideListener = () => {
        settingsDropdown.classList.add('hidden');
      };
      document.addEventListener('click', _settingsOutsideListener);

      settingsBtn.addEventListener('click', e => {
        e.stopPropagation();
        settingsDropdown.classList.toggle('hidden');
      });

      settingsDropdown.addEventListener('click', e => {
        e.stopPropagation();
      });

      document.getElementById('setting-help').addEventListener('change', e => {
        state.settings.help = e.target.checked;
        localStorage.setItem('settings', JSON.stringify(state.settings));
      });
    }
  }

  if (state.view === 'quiz') {
    document.getElementById('quiz-list').addEventListener('click', e => {
      const btn = e.target.closest('.answer-btn');
      if (btn) selectAnswer(parseInt(btn.dataset.q), btn.dataset.answer);
      const hintBtn = e.target.closest('.hint-btn');
      if (hintBtn) {
        const qi = hintBtn.dataset.q;
        const hintText = document.querySelector(`.hint-text[data-q="${qi}"]`);
        if (hintText) hintText.classList.toggle('hidden');
        hintBtn.textContent = hintText && !hintText.classList.contains('hidden') ? 'Ẩn gợi ý' : 'Xem gợi ý';
      }
    });
    document.getElementById('btn-verify').addEventListener('click', () => {
      state.view = 'results';
      render();
    });

    if (state.settings.help && APP_CONFIG.hasTheory) {
      const overlay = document.getElementById('help-modal-overlay');
      const searchInput = document.getElementById('help-search');

      async function openHelpModal() {
        overlay.classList.remove('hidden');
        searchInput.focus();
        if (state.theories.length === 0) {
          state.theories = await fetchJSON(`${DB}/theories.json`);
        }
        renderTheoryList(searchInput.value);
      }

      document.getElementById('btn-help').addEventListener('click', openHelpModal);
      document.getElementById('btn-help-close').addEventListener('click', () => {
        overlay.classList.add('hidden');
      });
      overlay.addEventListener('click', e => {
        if (e.target === overlay) overlay.classList.add('hidden');
      });
      searchInput.addEventListener('input', e => {
        renderTheoryList(e.target.value);
      });
    }
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
    if (APP_CONFIG.showSettings !== false) {
      Object.assign(state.settings, JSON.parse(localStorage.getItem('settings') || '{}'));
    }
    render();
  } catch (err) {
    document.getElementById('app').innerHTML = `
      <div class="text-center py-20 space-y-2">
        <p class="text-red-500 font-medium">Failed to load: ${err.message}</p>
        <p class="text-slate-400 text-sm">Run a local server: <code class="bg-slate-100 px-2 py-0.5 rounded">npm start</code></p>
      </div>`;
  }
})();
