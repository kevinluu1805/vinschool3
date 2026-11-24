# Rules: multiply_divide_word_problem.json

## Mục tiêu
Toán có lời văn dùng **phép nhân** và **phép chia có dư** (lấy từ Phiếu 8, Phần A – Câu 10 và 11). Mỗi câu gồm một tình huống và **một** yêu cầu, thuộc 1 trong 3 kiểu:
- **Kiểu 1 – Tính chính xác (nhân)**: số có 3 chữ số × số có 1 chữ số. Không hỏi ước lượng.
- **Kiểu 2 – Nhiều nhất bao nhiêu nhóm đầy và còn thừa bao nhiêu**: lấy thương và số dư.
- **Kiểu 3 – Cần ít nhất bao nhiêu nhóm để chứa hết**: lấy thương + 1.

## Ghi chú khi thêm/sửa câu hỏi
- `correct`/`wrong_pool` là **string**. Kiểu 1 chỉ ghi số (`"1485"`). Kiểu 2 ghi `"14 trang, thừa 5 tấm ảnh"`. Kiểu 3 ghi `"15 trang"`.
- `wrong_pool` có **5** phần tử, không trùng nhau, không trùng đáp án.
- Kiểu 1: tích < 10000, có ít nhất một lần nhớ (để bẫy "quên nhớ" có tác dụng).
- Kiểu 2 và 3: số bị chia có 2 chữ số, số chia từ 3 đến 9, **số dư luôn khác 0**.
- Lời đề phải khớp với tình huống: "trang đầy", "túi đầy", "bó", "bộ quần áo"…
- Có `hint` chỉ nêu cách làm, không cho đáp số.
- File được sinh bằng `scripts/gen_multiply_divide_word_problem.py` (sửa `MUL` / `DIV_REM` / `DIV_UP` rồi chạy lại, không sửa JSON bằng tay); khi thêm câu, giữ đúng chiến lược wrong_pool bên dưới.

## Phân bố (30 câu)
| Kiểu | Số câu | ID |
|---|---|---|
| Tính chính xác (nhân) | 10 | 1–10 |
| Nhóm đầy + số thừa | 10 | 11–20 |
| Cần ít nhất bao nhiêu nhóm | 10 | 21–30 |

---

## Kiểu 1: Tính chính xác
Ví dụ: "Có 165 học sinh làm tranh khảm. Mỗi bạn làm một bức tranh bằng 9 viên đá khảm. Tính chính xác số viên đá cả nhóm cần dùng." → **1485**

| Bẫy | Công thức | Ví dụ (165 × 9) |
|---|---|---|
| Quên nhớ (mỗi hàng chỉ viết hàng đơn vị của tích) | — | 945 |
| Nhân thiếu 1 | N × (k − 1) | 1320 |
| Nhân thừa 1 | N × (k + 1) | 1650 |
| Nhớ sai ở hàng chục | P + 10 | 1495 |
| Nhớ sai ở hàng trăm | P − 100 (dự phòng P + 100) | 1385 |

## Kiểu 2: Nhóm đầy + số thừa
Ví dụ: "Petra có 89 tấm ảnh. Mỗi trang album xếp đầy được 6 tấm. Hỏi Petra xếp được nhiều nhất bao nhiêu trang đầy và còn thừa bao nhiêu tấm ảnh?" → **14 trang, thừa 5 tấm ảnh**

| Bẫy | Dạng (q = thương, r = dư) | Ví dụ |
|---|---|---|
| Số dư ≥ số chia | (q − 1, r + k) | 13 trang, thừa 11 |
| Thương thừa 1 | (q + 1, r) | 15 trang, thừa 5 |
| Nhầm số dư thành số còn thiếu | (q, k − r) | 14 trang, thừa 1 |
| Đảo thương và số dư | (r, q) | 5 trang, thừa 14 |
| Số dư lệch 1 | (q, r ± 1) | 14 trang, thừa 6 |

## Kiểu 3: Cần ít nhất bao nhiêu nhóm
Ví dụ: "Lớp 3B có 45 học sinh đi chơi thuyền. Mỗi thuyền chở được 6 bạn. Hỏi cần ít nhất bao nhiêu chiếc thuyền để chở hết các bạn?" → **8 thuyền**

| Bẫy | Công thức | Ví dụ (45 : 6 = 7 dư 3) |
|---|---|---|
| Quên phần dư (bẫy chính) | q | 7 |
| Cộng thừa | q + 2 | 9 |
| Lấy số dư | r | 3 |
| Cộng thương với số dư | q + r | 10 |
| Thiếu 1 | q − 1 (dự phòng k, q + 3) | 6 |
