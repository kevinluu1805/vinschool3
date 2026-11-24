"""Sinh database/math/fraction_word_problem.json (Toán lời văn: phân số của một số).

Chạy từ thư mục gốc repo:  python3 scripts/gen_fraction_word_problem.py
Rules: database/math/_rules/fraction_word_problem_rules.md
"""
import json, sys
FR = {3:"một phần ba",4:"một phần tư",5:"một phần năm",6:"một phần sáu",7:"một phần bảy",8:"một phần tám",9:"một phần chín"}

# (kind, name, N, k, intro, give_verb, item, ask_unit)
# kind: "left" = hỏi còn lại, "part" = hỏi phần đã cho
DATA = [
 ("left","Rajiv",45,5,"Rajiv có {N} chiếc ô tô đồ chơi. Bạn tặng {f} số ô tô cho em trai.","Hỏi Rajiv còn lại bao nhiêu chiếc ô tô đồ chơi?","chiếc ô tô"),
 ("left","Lan",24,3,"Lan có {N} cái kẹo. Lan cho bạn {f} số kẹo đó.","Hỏi Lan còn lại bao nhiêu cái kẹo?","cái kẹo"),
 ("left","Minh",32,4,"Minh có {N} viên bi. Minh cho em {f} số viên bi.","Hỏi Minh còn lại bao nhiêu viên bi?","viên bi"),
 ("left","Mẹ",42,6,"Mẹ mua {N} quả trứng. Mẹ đã dùng {f} số trứng để làm bánh.","Hỏi mẹ còn lại bao nhiêu quả trứng?","quả trứng"),
 ("left","Cửa hàng",56,7,"Một cửa hàng có {N} chiếc áo. Cửa hàng đã bán {f} số áo.","Hỏi cửa hàng còn lại bao nhiêu chiếc áo?","chiếc áo"),
 ("left","Hoa",72,8,"Hoa có {N} bông hoa. Hoa tặng cô giáo {f} số bông hoa.","Hỏi Hoa còn lại bao nhiêu bông hoa?","bông hoa"),
 ("left","Thư viện",63,9,"Thư viện lớp có {N} quyển truyện. Các bạn đã mượn {f} số quyển truyện.","Hỏi thư viện lớp còn lại bao nhiêu quyển truyện?","quyển truyện"),
 ("left","Nam",35,5,"Nam có {N} nhãn vở. Nam dán {f} số nhãn vở lên sách.","Hỏi Nam còn lại bao nhiêu nhãn vở chưa dán?","nhãn vở"),
 ("left","Bác nông dân",48,6,"Bác nông dân có {N} con gà. Bác bán {f} số gà.","Hỏi bác nông dân còn lại bao nhiêu con gà?","con gà"),
 ("left","Petra",81,9,"Petra có {N} tấm ảnh. Petra tặng bạn {f} số tấm ảnh.","Hỏi Petra còn lại bao nhiêu tấm ảnh?","tấm ảnh"),
 ("left","Lớp 3A",36,4,"Lớp 3A có {N} học sinh. Có {f} số học sinh đi học bơi.","Hỏi lớp 3A còn bao nhiêu học sinh không đi học bơi?","học sinh"),
 ("left","An",64,8,"An có một sợi dây dài {N} cm. An cắt đi {f} sợi dây.","Hỏi sợi dây còn lại dài bao nhiêu xăng-ti-mét?","cm"),
 ("part","Mai",30,3,"Mai có {N} cái bút chì màu. Mai cho em {f} số bút chì màu.","Hỏi Mai đã cho em bao nhiêu cái bút chì màu?","cái bút chì"),
 ("part","Bình",28,4,"Bình có {N} quả táo. Bình biếu bà {f} số táo.","Hỏi Bình đã biếu bà bao nhiêu quả táo?","quả táo"),
 ("part","Trường",54,6,"Một vườn trường có {N} cây. {F} số cây là cây bàng.","Hỏi vườn trường có bao nhiêu cây bàng?","cây"),
 ("part","Linh",42,7,"Linh có {N} viên kẹo. Linh chia cho bạn {f} số viên kẹo.","Hỏi Linh đã chia cho bạn bao nhiêu viên kẹo?","viên kẹo"),
 ("part","Hà",40,5,"Hà có {N} nghìn đồng. Hà dùng {f} số tiền để mua bút.","Hỏi Hà đã dùng bao nhiêu nghìn đồng để mua bút?","nghìn đồng"),
 ("part","Quân",56,8,"Quân có {N} tấm thẻ. Quân tặng bạn {f} số thẻ.","Hỏi Quân đã tặng bạn bao nhiêu tấm thẻ?","tấm thẻ"),
 ("part","Bể cá",27,9,"Một bể có {N} con cá. {F} số cá là cá vàng.","Hỏi bể có bao nhiêu con cá vàng?","con cá"),
 ("part","Đội",60,6,"Một đội có {N} vận động viên. {F} số vận động viên là nữ.","Hỏi đội có bao nhiêu vận động viên nữ?","vận động viên"),
]

def pool(cands, correct):
    out = []
    for c in cands:
        if c > 0 and c != correct and c not in out:
            out.append(c)
    return out

OUT = sys.argv[1] if len(sys.argv) > 1 else "database/math/fraction_word_problem.json"

qs = []
for i,(kind,name,N,k,intro,ask,unit) in enumerate(DATA,1):
    assert N % k == 0 and k in FR
    part, rem = N//k, N - N//k
    f = FR[k]
    text = intro.format(N=N, f=f, F=f[0].upper()+f[1:]) + " " + ask
    if kind == "left":
        correct = rem
        cands = [part, N-k, N+part, N-2*part, N, rem+k, rem-1]
        hint = f"Bước 1: tìm {f} của {N} (lấy {N} chia cho {k}). Bước 2: lấy {N} trừ đi kết quả vừa tìm."
    else:
        correct = part
        cands = [rem, N-k, k, 2*part, part+k, N+k]
        hint = f"Tìm {f} của {N} bằng cách lấy {N} chia cho {k}."
    wp = pool(cands, correct)[:5]
    assert len(wp) == 5, (i, wp)
    qs.append({"id": i, "question": text, "correct": str(correct),
               "wrong_pool": [str(x) for x in wp], "hint": hint})
json.dump(qs, open(OUT,"w"), ensure_ascii=False, indent=2)
print(len(qs))
