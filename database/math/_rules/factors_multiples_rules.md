# Rules: factors_multiples.json

## Mục tiêu
Tìm **ước số** và **bội số**. Mỗi đáp án là **một dãy số** (vd `"1, 2, 3, 6, 9, 18"`), học sinh chọn dãy đúng. Có 5 kiểu:
- **Kiểu 1**: Tìm tất cả các ước của N.
- **Kiểu 2**: Viết k bội nhỏ nhất (khác 0) của n.
- **Kiểu 3**: Viết tất cả các bội (khác 0) của n mà nhỏ hơn M.
- **Kiểu 4**: Dãy nào gồm toàn các ước của N?
- **Kiểu 5**: Dãy nào gồm toàn các bội của n?

## Ghi chú khi thêm/sửa câu hỏi
- **Mọi số** trong câu hỏi, đáp án đúng và `wrong_pool` đều **≤ 100**. Giới hạn này chỉ áp dụng cho dạng này.
- `correct`/`wrong_pool` là **string**: các số xếp tăng dần, cách nhau bằng `", "`.
- `wrong_pool` có **5** phần tử, không trùng nhau, không trùng đáp án.
- **Đổi số đa dạng**: mỗi câu dùng một N hoặc n khác nhau, không lặp lại trong cùng một kiểu.
- Có `hint` chỉ nêu cách làm, không cho đáp số.
- File được sinh bằng `scripts/gen_factors_multiples.py` (random với seed cố định, nên chạy lại ra đúng kết quả cũ). Muốn đổi số thì sửa danh sách số trong script rồi chạy lại.

## Phân bố (40 câu)
| Kiểu | Số câu | ID | Các số dùng |
|---|---|---|---|
| 1. Tất cả các ước | 12 | 1–12 | 12, 16, 20, 28, 30, 36, 42, 45, 50, 60, 75, 100 |
| 2. k bội nhỏ nhất | 10 | 13–22 | 3, 4, 6, 8, 9, 11, 12, 15, 5, 13 (k = 4–6) |
| 3. Bội nhỏ hơn M | 8 | 23–30 | 9 (<54), 8 (<48), 14 (<70), 16 (<80), 11 (<66), 12 (<60), 25 (<100), 6 (<42) |
| 4. Dãy toàn ước | 5 | 31–35 | 24, 40, 48, 72, 90 |
| 5. Dãy toàn bội | 5 | 36–40 | 4, 6, 8, 9, 15 |

Kiểu 1 có 3 cách hỏi xoay vòng: "Tìm tất cả các ước của N." / "Viết tất cả các ước của N." / "Số N chia hết cho những số nào? (viết tất cả)".

---

## Kiểu 1: Tất cả các ước
Ví dụ: ước của 12 là **1, 2, 3, 4, 6, 12**

| Bẫy | Ví dụ |
|---|---|
| Quên 1 và chính N | 2, 3, 4, 6 |
| Quên chính N | 1, 2, 3, 4, 6 |
| Bỏ sót cặp ước ở giữa (lớn nhất) | 1, 2, 6, 12 (thiếu 3 × 4) |
| Thêm một số không phải ước | 1, 2, 3, 4, 5, 6, 12 |
| Bỏ sót cặp ước ở giữa (nhỏ nhất) | 1, 3, 4, 12 (thiếu 2 × 6) |
| (dự phòng) Quên 1 | |

## Kiểu 2: k bội nhỏ nhất (khác 0)
Ví dụ: 5 bội nhỏ nhất của 3 là **3, 6, 9, 12, 15**

| Bẫy | Ví dụ |
|---|---|
| Tính cả số 0 | 0, 3, 6, 9, 12 |
| Bỏ qua chính số n | 6, 9, 12, 15, 18 |
| Đếm sai một bước (−1) | 3, 6, 9, 11, 15 |
| Nhầm bội thành ước | 1, 3 |
| Đếm cách quãng (chỉ lấy bội lẻ); nếu vượt 100 thì dùng "thiếu một bội" | 3, 9, 15, 21, 27 |

## Kiểu 3: Bội nhỏ hơn M
M luôn là bội của n, để bẫy "lấy cả M" có tác dụng. Ví dụ: bội của 9 nhỏ hơn 54 là **9, 18, 27, 36, 45**

| Bẫy | Ví dụ |
|---|---|
| Lấy cả M (nhầm "nhỏ hơn" thành "không quá") | 9, …, 45, 54 |
| Thiếu bội cuối | 9, 18, 27, 36 |
| Tính cả số 0 | 0, 9, …, 45 |
| Nhầm bội thành ước | 1, 3, 9 |
| Đếm sai một bước (+1) | 9, 18, 28, 36, 45 |

## Kiểu 4 và 5: Dãy nào gồm toàn ước / toàn bội
- Đáp án đúng gồm 4 số bốc ngẫu nhiên: với kiểu 4 là ước của N (khác 1 và N), với kiểu 5 là bội của n (khác n, ≤ 100).
- Mỗi đáp án sai là **một dãy bốc riêng**, gồm 3 số đúng và **1 số bẫy**:
  - Số bẫy **có chung thừa số** với N (hoặc n) nhưng **không chia hết**. Vd ước của 24 thì bẫy là 9, 10, 14, 16. Bội của 4 thì bẫy là các số chẵn không chia hết cho 4, như 38, 70, 86.
  - Mỗi đáp án sai dùng **một số bẫy khác nhau**.
- Lý do: nếu mọi đáp án sai đều sinh ra từ đáp án đúng bằng cách thay 1 số, học sinh chỉ cần chọn dãy có các số xuất hiện nhiều nhất, hoặc dãy duy nhất không chứa số bẫy lặp lại.
- Chọn N có ít nhất 6 ước ở giữa (không tính 1 và N), để các dãy bốc ra đủ khác nhau.
