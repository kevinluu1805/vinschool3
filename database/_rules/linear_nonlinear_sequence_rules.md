# Rules: linear_nonlinear_sequence.json

## Mục tiêu
Bộ câu hỏi gồm 2 loại:
- **Tìm số tiếp theo**: cho 4 số, học sinh tìm số thứ 5.
- **Phân loại dãy số**: cho 5 số, học sinh chọn "Tuyến tính" hoặc "Phi tuyến tính".

Phạm vi số: **-100 đến 100** (áp dụng cho tất cả các số trong dãy).

## Phân bố (41 câu)
| Dạng                        | Số câu | ID      |
|-----------------------------|--------|---------|
| Tăng đều (tìm số tiếp theo) | 7      | 1–7     |
| Giảm đều (tìm số tiếp theo) | 7      | 8–14    |
| Số chính phương (tìm số)    | 6      | 15–20   |
| Phân loại tuyến tính        | 5      | 21–25   |
| Nhân đôi (tìm số tiếp theo) | 6      | 26–31   |
| Tìm quy luật                | 5      | 33–37   |
| Số chính phương thứ 6       | 5      | 38–42   |

---

## Dạng 1: Tăng đều (Arithmetic Increase)
- Dãy cộng thêm cùng một số dương mỗi bước.
- **Bước tăng**: từ 1 đến 10 (≤ 10).
- Ví dụ: `-50, -47, -44, -41` → bước +3 → đáp án `-38`
- **wrong_pool**: chọn 5 số gần đáp án đúng (±1 đến ±5), không trùng đáp án, không tạo thành dãy hợp lệ.

## Dạng 2: Giảm đều (Arithmetic Decrease)
- Dãy trừ đi cùng một số dương mỗi bước.
- **Bước giảm**: từ 1 đến 10 (≤ 10).
- Ví dụ: `100, 92, 84, 76` → bước -8 → đáp án `68`
- **wrong_pool**: tương tự dạng 1, chọn gần đáp án đúng.

## Dạng 3: Số chính phương (Perfect Squares)
- Dãy là các số chính phương liên tiếp: n², (n+1)², (n+2)², (n+3)² → đáp án: (n+4)²
- Phạm vi dùng: n từ 1 đến 10 (vì 10² = 100 ≤ phạm vi cho phép).
- Ví dụ: `1, 4, 9, 16` (1², 2², 3², 4²) → đáp án `25` (5²)
- Các câu dùng điểm bắt đầu khác nhau để tránh trùng lặp.
- Không sử dụng số âm cho các bài về số chính phương
- **wrong_pool**: chọn 5 số không phải số chính phương, nằm gần đáp án đúng nhưng không trùng.

## Dạng 4: Nhân đôi (Geometric x2)
- Mỗi số bằng số trước nhân 2 (tỉ lệ công bội = 2).
- Cho 4 số, học sinh tìm số thứ 5.
- **Chỉ dùng số dương** (không dùng số âm).
- Phạm vi: tất cả số trong dãy và đáp án nằm trong [1, 100].
- Điểm bắt đầu hợp lệ: 1, 2, 3, 4, 5, 6 (vì 6×2⁴=96 ≤ 100; 7×2⁴=112 > 100).
- **wrong_pool**: chọn 5 số gần đáp án đúng (±1 đến ±5), không trùng đáp án.

## Dạng 5: Tìm quy luật
- Cho 5 số trong một dãy (tăng đều, giảm đều, hoặc số chính phương).
- Câu hỏi: `"Quy luật của dãy số: a, b, c, d, e, ... là gì?"`
- Đáp án đúng: bước tăng/giảm dạng `"+n"` hoặc `"-n"`, hoặc `"Số chính phương"`.
- **wrong_pool**: 5 phần tử, gồm các bước sai gần đúng và/hoặc đáp án của dạng khác để đánh lừa.
  - Ví dụ tăng đều +3: wrong gồm ["+2", "+4", "+5", "-3", "Số chính phương"]
  - Ví dụ số chính phương: wrong gồm các bước số lẻ ["+3", "+5", "+7", "+9", "×2"]

## Dạng 6: Số chính phương thứ 6
- Hiển thị 4 số chính phương liên tiếp bắt đầu từ n², hỏi số chính phương thứ 6 = (n+5)².
- **Phạm vi**: (n+5)² ≤ 100 → n chỉ có thể từ 1 đến 5 (đúng 5 câu hợp lệ).
- Câu hỏi: `"Trong dãy số chính phương: a, b, c, d, ..., hãy tìm số chính phương thứ 6 trong dãy."`
- **wrong_pool**: 5 số không phải số chính phương, nằm gần đáp án đúng.

## Dạng 7: Phân loại tuyến tính / phi tuyến tính
- Cho 5 số trong một dãy (tăng đều, giảm đều, hoặc số chính phương).
- Câu hỏi: `"Đây là dãy số: a, b, c, d, e, ..."`
- **Chỉ có 2 đáp án**: `"Tuyến tính"` và `"Phi tuyến tính"`.
- Dãy tăng/giảm đều → Tuyến tính. Dãy số chính phương → Phi tuyến tính.
- **wrong_pool**: chỉ có 1 phần tử (đáp án còn lại).
- App tự động xử lý pool 1 phần tử → hiển thị 2 nút thay vì 4.
- Phân bố: khoảng 3 tuyến tính + 2 phi tuyến tính (hoặc cân bằng tùy ý).

---

## Ghi chú khi thêm/sửa câu hỏi
- Luôn kiểm tra: tất cả số trong dãy + đáp án đúng nằm trong [-100, 100].
- wrong_pool phải có **ít nhất 3** phần tử (khuyến nghị 5).
- Không để wrong_pool chứa đáp án đúng.
- Với dãy tăng/giảm đều: wrong_pool nên nằm trong khoảng ±5 so với đáp án để tăng độ khó vừa phải.
- Với số chính phương: wrong_pool nên là số lẻ hoặc số chắn không phải chính phương, gần đáp án.

## Nếu muốn thêm dạng mới
Thêm một section mới vào file này, cập nhật bảng phân bố, và thêm câu hỏi vào JSON với id tiếp theo.
