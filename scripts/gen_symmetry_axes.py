"""Sinh database/math/symmetry_axes.json và các hình database/math/figures/symmetry_*.svg.

Số trục đối xứng (`correct`) được tính bằng hình học, không nhập tay.
Chạy từ thư mục gốc repo:  python3 scripts/gen_symmetry_axes.py
Rules: database/math/_rules/symmetry_axes_rules.md
"""
import json, math, os, sys
OUT = sys.argv[1] if len(sys.argv) > 1 else "database/math"
FIG = os.path.join(OUT, "figures")

def reg(n, r=75, cx=100, cy=100, start=-90):
    return [(cx + r*math.cos(math.radians(start + 360*i/n)), cy + r*math.sin(math.radians(start + 360*i/n))) for i in range(n)]

SQ = [(35,35),(165,35),(165,165),(35,165)]
RECT_H = [(20,55),(180,55),(180,145),(20,145)]
RECT_V = [(55,20),(145,20),(145,180),(55,180)]
TRI_EQ = reg(3, 85, 100, 115)

# primitive: (kind, data)  kind ∈ shape | fill | fill2 (màu cam, khác màu fill) | dot | line | ring
def shape(pts): return ("shape", pts)
def fill(pts): return ("fill", pts)
def fill2(pts): return ("fill2", pts)
def dot(x, y): return ("dot", (x, y, 8))
def line(a, b): return ("line", (a, b))
def ring(x, y, r): return ("ring", (x, y, r))

# (tên file, nhóm, mô tả, các primitive, trap theo hình gốc)
ITEMS = [
 ("vuong", "basic", "Hình vuông", [shape(SQ)], None),
 ("chu_nhat_ngang", "basic", "Hình chữ nhật nằm ngang", [shape(RECT_H)], None),
 ("chu_nhat_dung", "basic", "Hình chữ nhật đứng", [shape(RECT_V)], None),
 ("tam_giac_deu", "basic", "Tam giác đều", [shape(TRI_EQ)], None),
 ("tam_giac_can", "basic", "Tam giác cân", [shape([(100,20),(150,180),(50,180)])], None),
 ("thoi", "basic", "Hình thoi", [shape([(100,15),(160,100),(100,185),(40,100)])], None),
 ("ngu_giac_deu", "basic", "Ngũ giác đều", [shape(reg(5, 82, 100, 108))], None),
 ("luc_giac_deu", "basic", "Lục giác đều", [shape(reg(6, 82, 100, 100, 0))], None),
 ("thang_can", "basic", "Hình thang cân", [shape([(65,45),(135,45),(180,155),(20,155)])], None),
 ("bat_giac_deu", "basic", "Bát giác đều", [shape(reg(8, 82, 100, 100, -90+22.5))], None),

 ("binh_hanh", "zero", "Hình bình hành", [shape([(60,50),(185,50),(140,150),(15,150)])], None),
 ("tam_giac_thuong", "zero", "Tam giác thường", [shape([(40,170),(180,170),(75,40)])], None),
 ("thang_vuong", "zero", "Hình thang vuông", [shape([(30,40),(110,40),(175,160),(30,160)])], None),
 ("vuong_2_mau_lech", "zero_color", "Hình vuông chia 2 màu bởi đường lệch",
   [fill([(35,35),(75,35),(165,165),(35,165)]), fill2([(75,35),(165,35),(165,165)]), shape(SQ)], None),
 ("chu_s", "zero", "Hình chữ S ghép từ 4 ô vuông",
   [shape([(70,40),(170,40),(170,90),(120,90),(120,140),(20,140),(20,90),(70,90)])], None),

 ("vuong_4_cham", "pattern", "Hình vuông có 4 chấm đối xứng (như đề)",
   [shape(SQ), dot(75,75), dot(125,75), dot(125,125), dot(75,125)], "4"),
 ("vuong_cham_goc", "pattern", "Hình vuông có 1 chấm ở góc",
   [shape(SQ), dot(62,62)], "4"),
 ("vuong_cham_canh", "pattern", "Hình vuông có 1 chấm sát giữa cạnh trên",
   [shape(SQ), dot(100,62)], "4"),
 ("vuong_duong_cheo", "pattern", "Hình vuông có 1 đường chéo",
   [shape(SQ), line((35,35),(165,165))], "4"),
 ("vuong_to_nua", "pattern", "Hình vuông tô màu nửa bên trái",
   [fill([(35,35),(100,35),(100,165),(35,165)]), shape(SQ)], "4"),
 ("vuong_to_mot_o", "pattern", "Hình vuông tô màu 1 ô góc trên trái",
   [fill([(35,35),(100,35),(100,100),(35,100)]), shape(SQ)], "4"),
 ("vuong_to_hai_o_cheo", "pattern", "Hình vuông tô màu 2 ô chéo nhau",
   [fill([(35,35),(100,35),(100,100),(35,100)]), fill([(100,100),(165,100),(165,165),(100,165)]), shape(SQ)], "4"),
 ("vuong_dau_cong", "pattern", "Hình vuông có dấu cộng ở giữa",
   [shape(SQ), line((100,60),(100,140)), line((60,100),(140,100))], "2"),
 ("chu_nhat_cham_tam", "pattern", "Hình chữ nhật có 1 chấm ở tâm",
   [shape(RECT_H), dot(100,100)], "4"),
 ("chu_nhat_cham_goc", "pattern", "Hình chữ nhật có 1 chấm ở góc",
   [shape(RECT_H), dot(45,78)], "2"),
 ("tam_giac_cham_tam", "pattern", "Tam giác đều có 1 chấm ở tâm",
   [shape(TRI_EQ), dot(100,115)], "1"),
 ("tam_giac_cham_dinh", "pattern", "Tam giác đều có 1 chấm gần đỉnh trên",
   [shape(TRI_EQ), dot(100,70)], "3"),
 ("vuong_hinh_tron", "pattern", "Hình vuông có hình tròn ở giữa",
   [shape(SQ), ring(100,100,35)], "2"),
 ("vuong_2_cham_ngang", "pattern", "Hình vuông có 2 chấm ở giữa cạnh trái và phải",
   [shape(SQ), dot(62,100), dot(138,100)], "4"),
 ("vuong_soc_ngang", "pattern", "Hình vuông có một dải màu nằm ngang ở giữa",
   [fill([(35,80),(165,80),(165,120),(35,120)]), shape(SQ)], "4"),
 # ---- bổ sung (id 31–50) ----
 ("ngoi_sao_5_canh", "basic", "Ngôi sao 5 cánh",
   [shape([pt for i in range(5) for pt in (reg(5, 85, 100, 108)[i], reg(5, 34, 100, 108, -90+36)[i])])], None),
 ("chu_thap", "basic", "Hình chữ thập",
   [shape([(75,25),(125,25),(125,75),(175,75),(175,125),(125,125),(125,175),(75,175),(75,125),(25,125),(25,75),(75,75)])], None),
 ("ngoi_nha", "basic", "Hình ngôi nhà",
   [shape([(100,25),(165,85),(165,175),(35,175),(35,85)])], None),
 ("tam_giac_vuong_can", "basic", "Tam giác vuông cân",
   [shape([(40,30),(40,170),(180,170)])], None),
 ("that_giac_deu", "basic", "Thất giác đều", [shape(reg(7, 82, 100, 105))], None),

 ("binh_hanh_nghieng_trai", "zero", "Hình bình hành nghiêng trái", [shape([(15,50),(140,50),(185,150),(60,150)])], None),
 ("tam_giac_tu", "zero", "Tam giác tù", [shape([(20,140),(110,140),(180,50)])], None),
 ("chu_l", "zero", "Hình chữ L", [shape([(40,25),(90,25),(90,125),(140,125),(140,175),(40,175)])], None),
 ("chong_chong_3_canh", "zero", "Chong chóng 3 cánh",
   [shape([(100,100), reg(3, 85, 100, 100, -90+120*i)[0], reg(3, 70, 100, 100, -90+120*i+40)[0]]) for i in range(3)], None),

 ("luc_giac_cham_tam", "pattern", "Lục giác đều có 1 chấm ở tâm",
   [shape(reg(6, 82, 100, 100, 0)), dot(100,100)], "1"),
 ("luc_giac_cham_dinh", "pattern", "Lục giác đều có 1 chấm gần một đỉnh",
   [shape(reg(6, 82, 100, 100, 0)), dot(150,100)], "6"),
 ("chu_nhat_duong_cheo", "pattern", "Hình chữ nhật có 1 đường chéo",
   [shape(RECT_H), line((20,55),(180,145))], "2"),
 ("vuong_hai_duong_cheo", "pattern", "Hình vuông có 2 đường chéo",
   [shape(SQ), line((35,35),(165,165)), line((165,35),(35,165))], "2"),
 ("vuong_4_o_goc", "pattern", "Hình vuông tô màu 4 ô nhỏ ở 4 góc",
   [fill([(35,35),(75,35),(75,75),(35,75)]), fill([(125,35),(165,35),(165,75),(125,75)]),
    fill([(125,125),(165,125),(165,165),(125,165)]), fill([(35,125),(75,125),(75,165),(35,165)]), shape(SQ)], "2"),
 ("vuong_to_ba_o", "pattern", "Hình vuông tô màu 3 trong 4 ô",
   [fill([(35,35),(100,35),(100,100),(35,100)]), fill([(100,35),(165,35),(165,100),(100,100)]),
    fill([(35,100),(100,100),(100,165),(35,165)]), shape(SQ)], "4"),
 ("thoi_cham_dinh", "pattern", "Hình thoi có 1 chấm gần đỉnh trên",
   [shape([(100,15),(160,100),(100,185),(40,100)]), dot(100,55)], "2"),
 ("tam_giac_duong_cao", "pattern", "Tam giác đều có 1 đường kẻ từ đỉnh xuống giữa cạnh đáy",
   [shape(TRI_EQ), line(TRI_EQ[0], ((TRI_EQ[1][0]+TRI_EQ[2][0])/2, (TRI_EQ[1][1]+TRI_EQ[2][1])/2))], "3"),
 ("vuong_thoi_ben_trong", "pattern", "Hình vuông có hình thoi tô màu bên trong",
   [fill([(100,55),(145,100),(100,145),(55,100)]), shape(SQ)], "2"),
 ("chu_nhat_to_nua_tren", "pattern", "Hình chữ nhật tô màu nửa trên",
   [fill([(20,55),(180,55),(180,100),(20,100)]), shape(RECT_H)], "2"),
 ("vuong_3_cham_cheo", "pattern", "Hình vuông có 3 chấm nằm trên đường chéo",
   [shape(SQ), dot(65,65), dot(100,100), dot(135,135)], "4"),
]

# ---------- kiểm tra số trục bằng hình học ----------
def key_pts(p):
    k, d = p
    if k in ("shape", "fill", "fill2"): return list(d)
    if k in ("dot", "ring"): return [(d[0], d[1])]
    return list(d)

def reflect(pt, c, ang):
    ux, uy = math.cos(ang), math.sin(ang)
    x, y = pt[0]-c[0], pt[1]-c[1]
    dp = x*ux + y*uy
    return (c[0] + 2*dp*ux - x, c[1] + 2*dp*uy - y)

def close(a, b, tol=0.6): return abs(a[0]-b[0]) < tol and abs(a[1]-b[1]) < tol

def same(p, q):
    if p[0] != q[0]: return False
    k = p[0]
    if k in ("shape", "fill", "fill2"):
        A, B = p[1], q[1]
        if len(A) != len(B): return False
        ea = [(A[i], A[(i+1) % len(A)]) for i in range(len(A))]
        eb = [(B[i], B[(i+1) % len(B)]) for i in range(len(B))]
        return all(any((close(a1,b1) and close(a2,b2)) or (close(a1,b2) and close(a2,b1)) for b1,b2 in eb) for a1,a2 in ea)
    if k in ("dot", "ring"):
        return close(p[1][:2], q[1][:2]) and p[1][2] == q[1][2]
    a1, a2 = p[1]; b1, b2 = q[1]
    return (close(a1,b1) and close(a2,b2)) or (close(a1,b2) and close(a2,b1))

def refl_prim(p, c, ang):
    k, d = p
    if k in ("shape", "fill", "fill2"): return (k, [reflect(v, c, ang) for v in d])
    if k in ("dot", "ring"): return (k, (*reflect(d[:2], c, ang), d[2]))
    return (k, tuple(reflect(v, c, ang) for v in d))

def count_axes(prims):
    pts = [pt for p in prims for pt in key_pts(p)]
    c = (sum(x for x,_ in pts)/len(pts), sum(y for _,y in pts)/len(pts))
    # trục ứng viên: lưới 0.5°, trục qua từng điểm đặc trưng, trung trực của từng cặp điểm
    cands = [math.radians(i/2) for i in range(360)]
    for a in pts:
        if math.dist(a, c) > 1e-6: cands.append(math.atan2(a[1]-c[1], a[0]-c[0]))
        for b in pts:
            if a != b: cands.append(math.atan2(b[1]-a[1], b[0]-a[0]) + math.pi/2)
    found = []
    for ang in cands:
        ang %= math.pi
        if any(min(abs(ang-f), math.pi-abs(ang-f)) < math.radians(0.2) for f in found): continue
        if all(any(same(refl_prim(p, c, ang), q) for q in prims) for p in prims):
            found.append(ang)
    return len(found)

# ---------- SVG ----------
def fmt(pts): return " ".join(f"{x:.1f},{y:.1f}" for x,y in pts)
def svg(prims, label):
    # thứ tự vẽ: nền hình → phần tô màu → chấm/đường kẻ → viền hình (viền luôn nằm trên cùng)
    bg, fills, marks, outlines = [], [], [], []
    for k, d in prims:
        if k == "shape":
            bg.append(f'<polygon points="{fmt(d)}" fill="#dbeafe"/>')
            outlines.append(f'<polygon points="{fmt(d)}" fill="none" stroke="#2563eb" stroke-width="4" stroke-linejoin="round"/>')
        elif k == "fill": fills.append(f'<polygon points="{fmt(d)}" fill="#60a5fa"/>')
        elif k == "fill2": fills.append(f'<polygon points="{fmt(d)}" fill="#fdba74"/>')
        elif k == "dot": marks.append(f'<circle cx="{d[0]}" cy="{d[1]}" r="{d[2]}" fill="#1e3a8a"/>')
        elif k == "ring": marks.append(f'<circle cx="{d[0]}" cy="{d[1]}" r="{d[2]}" fill="none" stroke="#2563eb" stroke-width="4"/>')
        else: marks.append(f'<line x1="{d[0][0]}" y1="{d[0][1]}" x2="{d[1][0]}" y2="{d[1][1]}" stroke="#2563eb" stroke-width="4" stroke-linecap="round"/>')
    return (f'<div class="flex justify-center py-2"><svg viewBox="0 0 200 200" width="160" height="160" role="img" aria-label="{label}">'
            + "".join(bg + fills + marks + outlines) + "</svg></div>\n")

TRAPS = {
    0: ["1", "2", "4", "3", "6"],
    1: ["2", "0", "3", "4", "6"],
    2: ["4", "1", "0", "3", "6"],
    3: ["1", "6", "2", "0", "4"],
    4: ["2", "8", "1", "0", "3"],
    5: ["4", "6", "10", "3", "1"],
    6: ["3", "4", "5", "12", "8"],
    7: ["6", "8", "14", "5", "1"],
    8: ["4", "6", "16", "7", "2"],
}

qs = []
for i, (name, group, label, prims, base) in enumerate(ITEMS, 1):
    n = count_axes(prims)
    path = f"figures/symmetry_{name}.svg"
    open(os.path.join(OUT, path), "w").write(svg(prims, label))
    wp = []
    for t in ([base] if base else []) + TRAPS[n]:
        if t != str(n) and t not in wp: wp.append(t)
    q = {"pattern": "Hoạ tiết dưới đây có bao nhiêu trục đối xứng? (tính cả chấm, đường kẻ và phần tô màu bên trong)",
         "zero_color": "Hình dưới đây có bao nhiêu trục đối xứng? (tính cả phần tô màu bên trong)",
         }.get(group, "Hình dưới đây có bao nhiêu trục đối xứng?")
    qs.append({"id": i, "question": q, "figure": path, "correct": str(n), "wrong_pool": wp[:5]})
    print(f"{i:2} {group:7} {n}  {label}  {wp[:5]}")
json.dump(qs, open(os.path.join(OUT, "symmetry_axes.json"), "w"), ensure_ascii=False, indent=2)
