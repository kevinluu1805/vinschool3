"""Sinh database/math/multiply_divide_word_problem.json (Toán lời văn: nhân / chia có dư).

Chạy từ thư mục gốc repo:  python3 scripts/gen_multiply_divide_word_problem.py
Rules: database/math/_rules/multiply_divide_word_problem_rules.md
"""
import json, sys

# Kiểu 1 — nhân: (N, k, câu đề)
MUL = [
 (165,9,"Có {N} học sinh làm tranh khảm. Mỗi bạn làm một bức tranh bằng {k} viên đá khảm. Tính chính xác số viên đá cả nhóm cần dùng."),
 (128,6,"Mỗi hộp bút có {k} chiếc bút. Trường mua {N} hộp bút. Tính chính xác số chiếc bút trường đã mua."),
 (247,4,"Một con robot đồ chơi cần {k} cục pin. Cửa hàng lắp pin cho {N} con robot. Tính chính xác số cục pin cửa hàng cần dùng."),
 (136,7,"Mỗi tuần có {k} ngày. Hỏi {N} tuần có tất cả bao nhiêu ngày? Tính chính xác."),
 (215,8,"Mỗi chiếc bàn có {k} chiếc ốc vít. Xưởng đóng {N} chiếc bàn. Tính chính xác số ốc vít xưởng cần dùng."),
 (184,5,"Mỗi túi gạo nặng {k} kg. Một cửa hàng có {N} túi gạo như thế. Tính chính xác số ki-lô-gam gạo cửa hàng có."),
 (326,3,"Mỗi bạn được phát {k} quyển vở. Khối lớp 3 có {N} bạn. Tính chính xác số quyển vở cần phát."),
 (159,6,"Mỗi lốc sữa chua có {k} hộp. Siêu thị nhập về {N} lốc sữa chua. Tính chính xác số hộp sữa chua siêu thị nhập về."),
 (275,4,"Mỗi chiếc ghế có {k} chân. Hội trường có {N} chiếc ghế. Tính chính xác số chân ghế trong hội trường."),
 (148,9,"Mỗi bông hoa giấy cần {k} cánh hoa. Lớp em làm {N} bông hoa giấy. Tính chính xác số cánh hoa cần cắt."),
]

# Kiểu 2 & 3 — chia có dư: (N, k, câu dẫn, đơn vị nhóm, đơn vị vật)
DIV_REM = [
 (89,6,"Petra có {N} tấm ảnh. Mỗi trang album xếp đầy được {k} tấm.","Hỏi Petra xếp được nhiều nhất bao nhiêu trang đầy và còn thừa bao nhiêu tấm ảnh?","trang","tấm ảnh"),
 (58,4,"Có {N} quả cam, xếp vào các túi, mỗi túi {k} quả.","Hỏi xếp được nhiều nhất bao nhiêu túi đầy và còn thừa bao nhiêu quả cam?","túi","quả cam"),
 (75,7,"Có {N} chiếc bánh, xếp vào các hộp, mỗi hộp {k} chiếc.","Hỏi xếp được nhiều nhất bao nhiêu hộp đầy và còn thừa bao nhiêu chiếc bánh?","hộp","chiếc bánh"),
 (67,5,"Có {N} m vải, mỗi bộ quần áo may hết {k} m vải.","Hỏi may được nhiều nhất bao nhiêu bộ quần áo và còn thừa bao nhiêu mét vải?","bộ","m vải"),
 (94,8,"Có {N} quyển sách, xếp lên các ngăn tủ, mỗi ngăn {k} quyển.","Hỏi xếp được nhiều nhất bao nhiêu ngăn đầy và còn thừa bao nhiêu quyển sách?","ngăn","quyển sách"),
 (53,3,"Có {N} bông hoa, cắm vào các lọ, mỗi lọ {k} bông.","Hỏi cắm được nhiều nhất bao nhiêu lọ đầy và còn thừa bao nhiêu bông hoa?","lọ","bông hoa"),
 (85,9,"Có {N} cái bút, buộc thành các bó, mỗi bó {k} cái.","Hỏi buộc được nhiều nhất bao nhiêu bó và còn thừa bao nhiêu cái bút?","bó","cái bút"),
 (79,6,"Có {N} quả trứng, xếp vào các khay, mỗi khay {k} quả.","Hỏi xếp được nhiều nhất bao nhiêu khay đầy và còn thừa bao nhiêu quả trứng?","khay","quả trứng"),
 (46,4,"Có {N} chiếc bánh quy, chia đều vào các đĩa, mỗi đĩa {k} chiếc.","Hỏi được nhiều nhất bao nhiêu đĩa đầy và còn thừa bao nhiêu chiếc bánh quy?","đĩa","chiếc bánh quy"),
 (62,7,"Có {N} viên bi, bỏ vào các túi, mỗi túi {k} viên.","Hỏi được nhiều nhất bao nhiêu túi đầy và còn thừa bao nhiêu viên bi?","túi","viên bi"),
]
DIV_UP = [
 (89,6,"Petra có {N} tấm ảnh. Mỗi trang album xếp đầy được {k} tấm.","Hỏi Petra cần ít nhất bao nhiêu trang để xếp hết số tấm ảnh đó?","trang"),
 (45,6,"Lớp 3B có {N} học sinh đi chơi thuyền. Mỗi thuyền chở được {k} bạn.","Hỏi cần ít nhất bao nhiêu chiếc thuyền để chở hết các bạn?","thuyền"),
 (38,4,"Có {N} quả bóng, mỗi rổ đựng được {k} quả.","Hỏi cần ít nhất bao nhiêu cái rổ để đựng hết số bóng?","rổ"),
 (52,5,"Có {N} khách đi du lịch, mỗi xe chở được {k} người.","Hỏi cần ít nhất bao nhiêu chiếc xe để chở hết số khách?","xe"),
 (71,8,"Có {N} chiếc cốc, mỗi hộp đựng được {k} chiếc.","Hỏi cần ít nhất bao nhiêu cái hộp để đựng hết số cốc?","hộp"),
 (65,7,"Có {N} lít nước mắm, mỗi can chứa được {k} lít.","Hỏi cần ít nhất bao nhiêu cái can để chứa hết số nước mắm?","can"),
 (40,3,"Có {N} học sinh ngồi vào các bàn, mỗi bàn ngồi được {k} bạn.","Hỏi cần ít nhất bao nhiêu cái bàn để tất cả học sinh đều có chỗ ngồi?","bàn"),
 (83,9,"Có {N} quả xoài, mỗi thùng đựng được {k} quả.","Hỏi cần ít nhất bao nhiêu thùng để đựng hết số xoài?","thùng"),
 (57,4,"Có {N} chiếc bánh, mỗi hộp đựng được {k} chiếc.","Hỏi cần ít nhất bao nhiêu hộp để đựng hết số bánh?","hộp"),
 (61,6,"Có {N} người đi thang máy, mỗi lượt thang máy chở được {k} người.","Hỏi thang máy phải chở ít nhất bao nhiêu lượt để chở hết mọi người?","lượt"),
]

def uniq(cands, correct, n=5):
    out = []
    for c in cands:
        if c is not None and c != correct and c not in out:
            out.append(c)
    assert len(out) >= n, (correct, out)
    return out[:n]

def no_carry(N, k):
    # lỗi quên nhớ: mỗi hàng chỉ viết hàng đơn vị của tích, hàng cao nhất viết cả tích
    ds = [int(d) for d in str(N)]
    s = str(ds[0]*k) + "".join(str(d*k % 10) for d in ds[1:])
    return int(s)

OUT = sys.argv[1] if len(sys.argv) > 1 else "database/math/multiply_divide_word_problem.json"

qs = []
for N,k,t in MUL:
    P = N*k
    assert P < 10000
    wp = uniq([no_carry(N,k), N*(k-1), N*(k+1), P+10, P-100, P+100, N+k], P)
    qs.append({"question": t.format(N=N,k=k), "correct": str(P), "wrong_pool": [str(x) for x in wp],
               "hint": f"Lấy {N} × {k}. Nhớ cộng phần nhớ sang hàng bên trái."})

for N,k,intro,ask,g,item in DIV_REM:
    q, r = divmod(N, k)
    assert r != 0 and N < 100
    fmt = lambda a,b: f"{a} {g}, thừa {b} {item}"
    cands = [(q-1, r+k), (q+1, r), (q, k-r), (r, q), (q, r+1), (q, r-1), (q+1, 0)]
    wp = uniq([c for c in cands if c[1] >= 0], (q, r))
    qs.append({"question": f"{intro.format(N=N,k=k)} {ask}", "correct": fmt(q,r),
               "wrong_pool": [fmt(*c) for c in wp],
               "hint": f"Thực hiện phép chia {N} : {k}. Thương là số {g} đầy, số dư là số {item} còn thừa. Số dư phải bé hơn {k}."})

for N,k,intro,ask,g in DIV_UP:
    q, r = divmod(N, k)
    assert r != 0 and N < 100
    wp = uniq([q, q+2, r, q+r, q-1, k, q+3], q+1)
    qs.append({"question": f"{intro.format(N=N,k=k)} {ask}", "correct": f"{q+1} {g}",
               "wrong_pool": [f"{x} {g}" for x in wp],
               "hint": f"Thực hiện phép chia {N} : {k}. Nếu còn dư thì cần thêm 1 {g} nữa cho phần dư."})

for i,q in enumerate(qs,1):
    q["id"] = i
qs = [{"id":q["id"], **{k:v for k,v in q.items() if k!="id"}} for q in qs]
json.dump(qs, open(OUT,"w"), ensure_ascii=False, indent=2)
