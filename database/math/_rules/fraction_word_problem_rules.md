# Rules: fraction_word_problem.json

## Mục tiêu
Toán có lời văn về **phân số của một số** (lấy từ Phiếu 8, Phần A – Câu 4): có N đồ vật, cho/bán/dùng `một phần k` số đó.
- **Dạng 1 – Hỏi phần còn lại**: N − N : k (2 bước).
- **Dạng 2 – Hỏi phần đã cho**: N : k (1 bước).

## Ghi chú khi thêm/sửa câu hỏi
- `correct` và `wrong_pool` là **string** chỉ chứa số (không kèm đơn vị).
- `wrong_pool` có **5** phần tử, không trùng nhau, không trùng đáp án, đều > 0.
- Phân số viết bằng chữ như trong đề: "một phần ba", "một phần tư", … "một phần chín".
- **k từ 3 đến 9** (không dùng một phần hai, vì khi đó phần đã cho = phần còn lại nên bẫy không còn tác dụng).
- N chia hết cho k và N ≤ 90 (nằm trong bảng chia lớp 3).
- Tránh k = N : k (vd 49 và một phần bảy), vì khi đó các bẫy bị trùng nhau.
- Có `hint` chỉ nêu cách làm, không cho đáp số.
- File được sinh bằng `scripts/gen_fraction_word_problem.py` (sửa danh sách `DATA` rồi chạy `python3 scripts/gen_fraction_word_problem.py`, không sửa JSON bằng tay); khi thêm câu, giữ đúng chiến lược wrong_pool bên dưới.

## Phân bố (20 câu)
| Dạng | Số câu | ID |
|---|---|---|
| Hỏi phần còn lại | 12 | 1–12 |
| Hỏi phần đã cho | 8 | 13–20 |

---

## Dạng 1: Hỏi phần còn lại
Ví dụ: "Rajiv có 45 chiếc ô tô đồ chơi. Bạn tặng một phần năm số ô tô cho em trai. Hỏi Rajiv còn lại bao nhiêu chiếc ô tô đồ chơi?" → **36**

| Bẫy | Công thức | Ví dụ (45, 1/5) |
|---|---|---|
| Dừng ở bước 1 | N : k | 9 |
| Trừ thẳng mẫu số | N − k | 40 |
| Cộng thay vì trừ | N + N : k | 54 |
| Trừ hai lần | N − 2 × (N : k) | 27 |
| Quên trừ | N | 45 |
| (dự phòng) | đáp án + k, đáp án − 1 | |

## Dạng 2: Hỏi phần đã cho
Ví dụ: "Mai có 30 cái bút chì màu. Mai cho em một phần ba số bút chì màu. Hỏi Mai đã cho em bao nhiêu cái bút chì màu?" → **10**

| Bẫy | Công thức | Ví dụ (30, 1/3) |
|---|---|---|
| Nhầm thành phần còn lại | N − N : k | 20 |
| Trừ thẳng mẫu số | N − k | 27 |
| Chép mẫu số | k | 3 |
| Nhân đôi | 2 × (N : k) | 20 → bị loại vì trùng, dùng bẫy dự phòng |
| Cộng mẫu số | N : k + k | 13 |
| (dự phòng) | N + k | 33 |
