"""Sinh database/math/secret_code.json + database/math/figures/secret_code_<id>.html (Mật mã con vật).

Chạy từ thư mục gốc repo:  python3 scripts/gen_secret_code.py
Rules: database/math/_rules/secret_code_rules.md

Mỗi câu có 4 con vật A, B, C, D (mỗi con là một chữ số 1–9, khác nhau) và 4 phép tính:
  dòng 1 tìm A (chỉ dùng số), dòng 2 tìm B từ A và một số,
  dòng 3 tìm C từ A và B, dòng 4 tìm D từ C và một số.
Mật mã = A B C D ghép lại theo thứ tự đó.
"""
import json, os, random, sys
rng = random.Random(2026)

OUT = sys.argv[1] if len(sys.argv) > 1 else "database/math/secret_code.json"
FIG_DIR = os.path.join(os.path.dirname(OUT), "figures")
N_QUESTIONS = 30
MAX_SHOWN = 20          # mọi số hiện trong phép tính ≤ 20

ANIMALS = [
    ["🐦", "🐰", "🐔", "🐿️"],
    ["🐶", "🐱", "🐟", "🐢"],
    ["🐮", "🐷", "🐑", "🐴"],
    ["🦆", "🐹", "🦜", "🐇"],
    ["🐐", "🐠", "🐥", "🐈"],
]
STORIES = [
    'Một nhóm bạn đang chơi trò "Cánh cổng bí ẩn". Mật mã mở cổng khu vườn là một số có 4 chữ số, được tạo từ số lượng vật nuôi.',
    'Bạn Nam tìm thấy một chiếc rương kho báu. Mật mã mở rương là một số có 4 chữ số, được tạo từ số lượng các con vật.',
    'Cô giáo khoá tủ đồ chơi bằng một mật mã có 4 chữ số, được tạo từ số lượng các con vật trong trang trại.',
]
ASK = "Ghép số lượng các con vật theo thứ tự {order} để được mật mã. Mật mã là số nào?"

# Dạng phương trình, U là ẩn. Mỗi dạng: (mẫu, giải đúng, giải sai — dùng nhầm phép tính)
FORMS = {
    "p+U=r": ("{p} + {U} = {r}", lambda p, r: r - p, lambda p, r: r + p),
    "U+p=r": ("{U} + {p} = {r}", lambda p, r: r - p, lambda p, r: r + p),
    "U-p=r": ("{U} − {p} = {r}", lambda p, r: r + p, lambda p, r: r - p),
    "p-U=r": ("{p} − {U} = {r}", lambda p, r: p - r, lambda p, r: p + r),
    "p+r=U": ("{p} + {r} = {U}", lambda p, r: p + r, lambda p, r: abs(p - r)),
    "p-r=U": ("{p} − {r} = {U}", lambda p, r: p - r, lambda p, r: p + r),
}
# Tính r (hoặc toán hạng thứ hai) từ giá trị đúng của U và p để dựng đề
def build_r(form, p, U):
    return {"p+U=r": p + U, "U+p=r": p + U, "U-p=r": U - p, "p-U=r": p - U,
            "p+r=U": U - p, "p-r=U": p - U}[form]

def digit(x): return 1 <= x <= 9

class Eq:
    """Một dòng: ẩn `unk`; p, r là số (int) hoặc tên con vật (str: 'A','B','C')."""
    def __init__(self, form, unk, p, r):
        self.form, self.unk, self.p, self.r = form, unk, p, r
    def val(self, x, env): return env[x] if isinstance(x, str) else x
    def solve(self, env, wrong=False):
        f = FORMS[self.form][2 if wrong else 1]
        return f(self.val(self.p, env), self.val(self.r, env))
    def shown(self):
        return [x for x in (self.p, self.r) if isinstance(x, int)]

def make_eq(form, unk, U, p, env):
    """Dựng phương trình cho ẩn có giá trị U; p là số hoặc tên con vật đã biết."""
    pv = env[p] if isinstance(p, str) else p
    rv = build_r(form, pv, U)
    return None if rv < 1 else Eq(form, unk, p, rv)

def chain(eqs, wrong_at=None):
    env = {}
    for i, e in enumerate(eqs):
        v = e.solve(env, wrong=(i == wrong_at))
        if not (0 <= v <= 9): return None
        env[e.unk] = v
    return env

def code(env): return "".join(str(env[k]) for k in "ABCD")

def traps(eqs, correct):
    out = []
    def add(c):
        if c and len(c) == 4 and c[0] != "0" and c != correct and c not in out: out.append(c)
    for i in range(4):                       # nhầm phép tính ở một dòng, sai lan sang các dòng sau
        env = chain(eqs, wrong_at=i)
        if env: add(code(env))
    add(correct[::-1])                       # ghép ngược thứ tự
    add(correct[1] + correct[0] + correct[2:])   # đổi chỗ 2 con đầu
    add(correct[:2] + correct[3] + correct[2])   # đổi chỗ 2 con cuối
    add(correct[0] + correct[2] + correct[1] + correct[3])
    return out[:5]

def random_question(used):
    while True:
        A, B, C, D = rng.sample(range(1, 10), 4)
        env = {"A": A, "B": B, "C": C, "D": D}
        f1, f2 = rng.choice(["p+U=r", "U+p=r", "U-p=r", "p-U=r"]), rng.choice(["p+U=r", "U+p=r", "U-p=r", "p-U=r"])
        e1 = make_eq(f1, "A", A, rng.randint(2, 12), env)
        # dòng 2: B liên hệ với A (con vừa tìm ở dòng 1) và một số
        e2 = make_eq(f2, "B", B, "A", env)  # 🐦 + 🐰 = n, 🐰 + 🐦 = n, 🐰 − 🐦 = n, 🐦 − 🐰 = n
        # dòng 3: C liên hệ với A và B
        if A + B == C: e3 = Eq("p+r=U", "C", "A", "B")
        elif B - A == C: e3 = Eq("p-r=U", "C", "B", "A")
        elif A - B == C: e3 = Eq("p-r=U", "C", "A", "B")
        elif A + C == B: e3 = Eq("p+U=r", "C", "A", "B")
        elif C + B == A: e3 = Eq("U+p=r", "C", "B", "A")
        else: continue
        # dòng 4: D liên hệ với C và một số
        f4 = rng.choice(["U-p=r", "p+U=r", "U+p=r", "p-U=r"])
        if f4 == "p-U=r": e4 = Eq(f4, "D", C + D, "C")        # n − D = C
        else:             e4 = make_eq(f4, "D", D, "C", env)  # D − C = n, C + D = n, D + C = n
        eqs = [e1, e2, e3, e4]
        if None in eqs: continue
        # dòng 2 và dòng 3 đều chứa A, B → khác phép tính, kẻo dòng 3 lặp lại vế trái dòng 2
        if ("−" in FORMS[e2.form][0]) == ("−" in FORMS[e3.form][0]): continue
        if any(not 1 <= x <= MAX_SHOWN for e in eqs for x in e.shown()): continue
        if chain(eqs) != env: continue
        c = code(env)
        if c in used: continue
        tp = traps(eqs, c)
        if len(tp) >= 5: return eqs, c, tp

def render(eqs, icons):
    name = dict(zip("ABCD", icons))
    def tok(x):
        if isinstance(x, str): return f'<span class="text-3xl">{name[x]}</span>'
        return f"<span>{x}</span>"
    rows = []
    for e in eqs:
        slots = {"{U}": e.unk, "{p}": e.p, "{r}": e.r}
        html = "".join(tok(slots[t]) if t in slots else f"<span>{t}</span>" for t in FORMS[e.form][0].split())
        rows.append(f'<div class="flex items-center gap-2">{html}</div>')
    boxes = "".join(f'<span class="w-12 h-12 rounded-lg border-2 border-amber-400 bg-amber-50 flex items-center justify-center text-2xl">{i}</span>' for i in icons)
    return (
        '<div class="flex flex-col items-center gap-4 py-2">'
        f'<div class="space-y-2 text-2xl font-semibold text-slate-700">{"".join(rows)}</div>'
        f'<div class="flex items-center gap-2"><span class="text-sm font-semibold text-slate-500 mr-1">Mật mã:</span>{boxes}</div>'
        '</div>\n'
    )

def hint(icons):
    a, b, c, d = icons
    return (f"Giải từng dòng từ trên xuống: dòng 1 tìm {a}, dòng 2 dùng {a} để tìm {b}, dòng 3 dùng {a} và {b} để tìm {c}, "
            f"dòng 4 dùng {c} để tìm {d}. Thử lại bằng cách thay số vào phép tính, rồi ghép đúng thứ tự.")

# Câu 1: đúng ví dụ gốc  7 + 🐦 = 12, 🐰 + 8 = 15, 🐰 − 🐦 = 🐔, 🐿️ − 🐔 = 6  → 5728
example = [Eq("p+U=r", "A", 7, 12), Eq("U+p=r", "B", 8, 15), Eq("p-r=U", "C", "B", "A"), Eq("U-p=r", "D", "C", 6)]
assert code(chain(example)) == "5728"

qs = []
for i in range(N_QUESTIONS):
    if i == 0: eqs, c, tp = example, "5728", traps(example, "5728")
    else:      eqs, c, tp = random_question({q["correct"] for q in qs})
    assert len(tp) == 5, tp
    icons = ANIMALS[i % len(ANIMALS)]
    story = STORIES[0] if i == 0 else STORIES[i % len(STORIES)]
    qid = i + 1
    fig = f"figures/secret_code_{qid}.html"
    with open(os.path.join(FIG_DIR, f"secret_code_{qid}.html"), "w", encoding="utf-8") as f:
        f.write(render(eqs, icons))
    qs.append({"id": qid, "question": f"{story} {ASK.format(order=' '.join(icons))}",
               "figure": fig, "correct": c, "wrong_pool": tp, "hint": hint(icons)})

with open(OUT, "w", encoding="utf-8") as f:
    json.dump(qs, f, ensure_ascii=False, indent=2)
    f.write("\n")
print(f"Wrote {len(qs)} questions to {OUT}")
