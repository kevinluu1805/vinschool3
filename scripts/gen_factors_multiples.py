"""Sinh database/math/factors_multiples.json (Ước số và bội số, mọi số ≤ 100).

Chạy từ thư mục gốc repo:  python3 scripts/gen_factors_multiples.py
Rules: database/math/_rules/factors_multiples_rules.md
"""
import json, math, random, sys
rng = random.Random(2026)
MAX = 100

def divisors(n): return [d for d in range(1, n+1) if n % d == 0]
def s(xs): return ", ".join(str(x) for x in xs)

def finish(question, correct, traps, hint):
    out = []
    for t in traps:
        t = list(t)
        assert all(0 <= x <= MAX for x in t), (question, t)
        if t and t != correct and s(t) not in out: out.append(s(t))
    assert len(out) >= 5, (question, out)
    assert all(0 <= x <= MAX for x in correct)
    return {"question": question, "correct": s(correct), "wrong_pool": out[:5], "hint": hint}

def tricky_non(test, base, avoid, around, lo=2, hi=MAX):
    # số không thoả `test` nhưng có chung thừa số với `base` (khó loại bằng mắt), gần `around` nhất
    cands = [x for x in range(lo, hi+1) if not test(x) and math.gcd(x, base) > 1 and x not in avoid]
    return min(cands, key=lambda x: (abs(x - around), x))

OUT = sys.argv[1] if len(sys.argv) > 1 else "database/math/factors_multiples.json"

qs = []

# Kiểu 1 — tìm tất cả các ước
ASK1 = ["Tìm tất cả các ước của {N}.", "Viết tất cả các ước của {N}.", "Số {N} chia hết cho những số nào? (viết tất cả)"]
for i, N in enumerate([12, 16, 20, 28, 30, 36, 42, 45, 50, 60, 75, 100]):
    D = divisors(N)
    mids = [d for d in D if 1 < d < N and d * d <= N]           # nửa nhỏ của các cặp ước giữa
    pairs = [sorted({a, N // a}) for a in mids]
    extra = next(x for x in range(2, N) if N % x and D[1] < x < D[-2])  # số chen giữa nhưng không chia hết
    traps = [
        D[1:-1],                                           # quên 1 và chính nó
        D[:-1],                                            # quên chính nó
        [d for d in D if d not in pairs[-1]],              # bỏ sót cặp ước giữa lớn nhất
        sorted(D + [extra]),                               # thêm số không phải ước
        [d for d in D if d not in pairs[0]],               # bỏ sót cặp ước giữa nhỏ nhất
        D[1:],                                             # quên 1
    ]
    qs.append(finish(ASK1[i % 3].format(N=N), D, traps,
        f"Tìm từng cặp số nhân với nhau bằng {N}: 1 × {N}, 2 × …, cho đến khi hai số gặp nhau. Đừng quên 1 và chính số {N}."))

# Kiểu 2 — k bội nhỏ nhất khác 0
for n, k in [(3,5),(4,6),(6,5),(8,4),(9,5),(11,4),(12,5),(15,4),(5,6),(13,4)]:
    M = [n*i for i in range(1, k+1)]
    slip = M[:]; slip[k-2] -= 1                                # đếm sai một bước
    traps = [
        [0] + M[:-1],                                      # tính cả số 0
        [n*i for i in range(2, k+2)],                      # bỏ qua chính số n
        slip,
        divisors(n),                                       # nhầm bội thành ước
        [n*i for i in range(1, 2*k, 2)] if n*(2*k-1) <= MAX else [n*i for i in range(1, k)],  # đếm cách quãng / thiếu một bội
        [n*i for i in range(1, k)],
    ]
    qs.append(finish(f"Viết {k} bội nhỏ nhất (khác 0) của {n}.", M, traps,
        f"Đếm thêm {n}, bắt đầu từ {n}: {n}, {n} + {n}, … Bội khác 0 nhỏ nhất của {n} là chính số {n}."))

# Kiểu 3 — các bội khác 0 nhỏ hơn M
for n, lim in [(9,54),(8,48),(14,70),(16,80),(11,66),(12,60),(25,100),(6,42)]:
    assert lim % n == 0
    M = list(range(n, lim, n))
    slip = M[:]; slip[len(M)//2] += 1
    traps = [
        M + [lim],                                         # lấy cả số {lim} (nhầm "nhỏ hơn" thành "không quá")
        M[:-1],                                            # thiếu bội cuối
        [0] + M,                                           # tính cả số 0
        divisors(n),                                       # nhầm bội thành ước
        slip,
        M[1:],                                             # bỏ qua chính số n
    ]
    qs.append(finish(f"Viết tất cả các bội (khác 0) của {n} mà nhỏ hơn {lim}.", M, traps,
        f"Đếm thêm {n} bắt đầu từ {n} và dừng lại trước khi đến {lim}. Chú ý \"nhỏ hơn {lim}\" thì không lấy số {lim}."))

# Kiểu 4 & 5 — mỗi đáp án là một dãy 4 số bốc ngẫu nhiên riêng; đáp án sai có đúng 1 số bẫy
# (chung thừa số nhưng không chia hết), số bẫy không lặp giữa các đáp án → không loại trừ được bằng cách so dãy
def pick_sets(good, test, base, hi):
    correct = sorted(rng.sample(good, 4))
    used, traps = set(), []
    while len(traps) < 6:
        keep = rng.sample(good, 3)
        bad = tricky_non(test, base, set(keep) | used, rng.choice(keep), hi=hi)
        used.add(bad)
        t = sorted(keep + [bad])
        if t not in traps: traps.append(t)
    return correct, traps

for N in [24, 40, 48, 72, 90]:
    good = [d for d in divisors(N) if 1 < d < N]
    correct, traps = pick_sets(good, lambda x: N % x == 0, N, N - 1)
    qs.append(finish(f"Dãy số nào dưới đây gồm toàn các ước của {N}?", correct, traps,
        f"Thử chia {N} cho từng số trong dãy. Mỗi số phải chia hết, không có dư."))

for n in [4, 6, 8, 9, 15]:
    good = list(range(2 * n, MAX + 1, n))
    correct, traps = pick_sets(good, lambda x: x % n == 0, n, MAX)
    qs.append(finish(f"Dãy số nào dưới đây gồm toàn các bội của {n}?", correct, traps,
        f"Một số là bội của {n} khi số đó chia hết cho {n}. Thử chia từng số trong dãy cho {n}."))

qs = [{"id": i, **q} for i, q in enumerate(qs, 1)]
json.dump(qs, open(OUT, "w"), ensure_ascii=False, indent=2)
for q in qs: print(q["id"], "|", q["question"], "|", q["correct"], "|", q["wrong_pool"])
