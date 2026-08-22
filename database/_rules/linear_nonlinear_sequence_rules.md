# Rules: linear_nonlinear_sequence.json

## Mục tiêu
Bộ câu hỏi gồm 2 loại:
- **Tìm số tiếp theo**: cho 4 số, học sinh tìm số thứ 5.
- **Phân loại dãy số**: cho 5 số, học sinh chọn "Tuyến tính" hoặc "Phi tuyến tính".

Phạm vi số: **-100 đến 100** (áp dụng cho tất cả các số trong dãy).

## Ghi chú khi thêm/sửa câu hỏi
- Dạng 1–7: kiểm tra tất cả số trong [-100, 100].
- Dạng 8–9: kiểm tra start và đáp án trong [0, 1000].
- wrong_pool phải có **ít nhất 3** phần tử (khuyến nghị 5).
- Không để wrong_pool chứa đáp án đúng.
- Với dãy tăng/giảm đều: wrong_pool nên nằm trong khoảng ±5 so với đáp án để tăng độ khó vừa phải.
- Với số chính phương: wrong_pool nên là số lẻ hoặc số chắn không phải chính phương, gần đáp án.


## Dạng 12: Nhận diện dãy số từ mô tả
- Cho tên nhân vật mô tả dãy số bằng lời: số bắt đầu và quy luật "cộng đều X" hoặc "trừ đều X". Học sinh chọn đúng dãy 4 số hạng.
- **Đáp án và wrong_pool** đều là chuỗi 4 số, ví dụ: `"11, 9, 7, 5"`.
- Công thức đáp án đúng:
  - Cộng đều X: `start, start+X, start+2X, start+3X`
  - Trừ đều X: `start, start-X, start-2X, start-3X`
- **Phạm vi**: tất cả số hạng trong [0, 1000].
- **Bước nhảy**: cùng quy tắc Dạng 8/9 — step ≤ 10 nếu tất cả hạng ≤ 100; step là bội số của 10 nếu có hạng > 100.
- Câu hỏi: `"[Tên] tạo ra một dãy số và mô tả cho bạn của mình như sau: 'Tôi bắt đầu với số [start] và tôi tiếp tục [cộng/trừ] đều [X]'. Vậy dãy số của [Tên] là:"`
- **wrong_pool** (4 phần tử — mỗi phần tử là 1 dãy 4 số):
  - Sai chiều: dùng quy luật ngược lại (cộng thay vì trừ hoặc ngược lại)
  - Dịch dãy: bỏ số đầu, thêm số tiếp theo (shifted by 1)
  - Sai bước: dùng step ± 1 (hoặc step khác hợp lý)
  - Sai start: dùng start ± 1 với cùng step

## Dạng 13: Số đầu tiên vượt ngưỡng
- Cho tên nhân vật, số bắt đầu, bước đếm (thêm hoặc giảm). Học sinh tìm số đầu tiên trong dãy vượt qua một ngưỡng cho trước.
- **Hai kiểu câu hỏi**:
  - Đếm thêm: `"[Tên] đếm thêm [step] bắt đầu từ [start], số đầu tiên lớn hơn [T] là bao nhiêu?"`
  - Đếm giảm: `"[Tên] đếm giảm [step] bắt đầu từ [start], số đầu tiên nhỏ hơn [T] là bao nhiêu?"`
- **Ngưỡng T**: luôn là bội số của 10, thường là 10, 20, 30, ..., 100.
- **Độ dài dãy**: thiết kế sao cho dãy dài khoảng 5 số (đáp án ở bước thứ 4):
  - Đếm thêm: `start + 3*step ≤ T < start + 4*step` → đáp án = `start + 4*step`
  - Đếm giảm: `start - 3*step ≥ T > start - 4*step` → đáp án = `start - 4*step`
- **Phạm vi**: tất cả số hạng TRƯỚC đáp án nằm trong [0, 100]. Đáp án có thể nằm ngoài (ví dụ 103 hoặc 8 khi T=10).
- **Bước nhảy**: từ 2 đến 10.
- **Ràng buộc wrong_pool quan trọng**: tất cả đáp án sai phải nằm **cùng phía ngưỡng T với đáp án đúng**:
  - "Lớn hơn T": mọi wrong_pool phải > T
  - "Nhỏ hơn T": mọi wrong_pool phải < T
- **wrong_pool** (4 phần tử, gọi A = đáp án đúng, s = step):
  - Lớn hơn T: `[A−1, A+1, A+s, A+2s]` — nhưng nếu A−1 = T (không > T), dùng `A+2` thay thế
  - Nhỏ hơn T: `[A+1, A−1, A−s, A−2s]` — nhưng nếu A+1 = T (không < T), dùng `A−2` thay thế; nếu A−2s < 0, dùng `A−2` thay thế

## Nếu muốn thêm dạng mới
Thêm một section mới vào file này, cập nhật bảng phân bố, và thêm câu hỏi vào JSON với id tiếp theo.

## Phân bố (101 câu)
| Dạng                        | Số câu | ID      |
|-----------------------------|--------|---------|
| Tăng đều (tìm số tiếp theo) | 7      | 1–7     |
| Giảm đều (tìm số tiếp theo) | 7      | 8–14    |
| Số chính phương (tìm số)    | 6      | 15–20   |
| Phân loại tuyến tính        | 5      | 21–25   |
| Nhân đôi (tìm số tiếp theo) | 6      | 26–31   |
| Tìm quy luật                | 5      | 33–37   |
| Số chính phương thứ 6       | 5      | 38–42   |
| Đếm xuôi                    | 10     | 43–52   |
| Đếm ngược                   | 10     | 53–62   |
| Tìm số hạng thứ N           | 10     | 63–72   |
| Tìm số hạng từ cuối dãy     | 10     | 73–82   |
| Nhận diện dãy số từ mô tả   | 10     | 83–92   |
| Số đầu tiên vượt ngưỡng     | 10     | 93–102  |

---

## Dạng 1: Tăng đều (Arithmetic Increase)
- Dãy cộng thêm cùng một số dương mỗi bước.
- **Bước tăng**: từ 1 đến 10 (≤ 10) đối với dãy <= 100, và bước tăng là bội số của 5 đối với dãy <= 1000
- **Vị trí dấu `...`**: có thể ở cuối hoặc ở đầu dãy.
  - Cuối: `a, b, c, d, ...` → đáp án = d + bước
  - Đầu: `..., b, c, d, e` → đáp án = b − bước (số đứng trước b)
- Ví dụ cuối: `-50, -47, -44, -41, ...` → bước +3 → đáp án `-38`
- Ví dụ đầu: `..., -47, -44, -41, -38` → bước +3 → đáp án `-50`
- **wrong_pool (dạng cuối)**: đảo dấu, số liền trước trong dãy, đi thêm 1 bước quá đà, sai chiều.
- **wrong_pool (dạng đầu)**: số đầu tiên nhìn thấy (b), đi 1 bước quá đà về trước (đáp án − bước), số cuối (e), mở rộng sai chiều (e + bước), số thứ 2 nhìn thấy (c).

## Dạng 2: Giảm đều (Arithmetic Decrease)
- Dãy trừ đi cùng một số dương mỗi bước.
- **Bước giảm**: từ 1 đến 10 (≤ 10) đối với dãy <= 100, và bước giảm là bội số âm của 5 đối với dãy >= -1000
- **Vị trí dấu `...`**: có thể ở cuối hoặc ở đầu dãy.
  - Cuối: `a, b, c, d, ...` → đáp án = d − bước
  - Đầu: `..., b, c, d, e` → đáp án = b + |bước| (số đứng trước b)
- Ví dụ cuối: `100, 92, 84, 76, ...` → bước -8 → đáp án `68`
- Ví dụ đầu: `..., 27, 24, 21, 18` → bước -3 → đáp án `30`
- **wrong_pool (dạng cuối)**: tương tự dạng 1 — đảo dấu, số liền trước, quá đà.
- **wrong_pool (dạng đầu)**: số đầu tiên nhìn thấy (b), đi 1 bước quá đà về trước (đáp án + |bước|), số cuối (e), mở rộng sai chiều (e − |bước|), số thứ 2 nhìn thấy (c).

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

## Dạng 8: Đếm xuôi (Count Up)
- Cho tên nhân vật, bước nhảy, số bắt đầu. Học sinh tìm số tiếp theo khi đếm **xuôi**.
- Công thức: đáp án = start + step
- **Phạm vi**: start và đáp án đều trong **[0, 1000]**
- **Bước nhảy**:
  - Nếu start và đáp án ≤ 100: step ≤ 10
  - Nếu start hoặc đáp án > 100: step là bội số của 10
- Câu hỏi: `"Bạn [Tên] đếm xuôi các số cách đều [step] đơn vị, bắt đầu từ số [start], số tiếp theo bạn ấy đếm được là:"`
- **wrong_pool** (5 phần tử):
  - `start + 2*step` — đếm thêm 1 bước nữa (đi quá đà)
  - `start` — quên không cộng (số ban đầu)
  - `start - step` — trừ thay vì cộng (sai chiều)
  - `đáp án + 1` hoặc `± nhỏ` — sai nhỏ
  - `step` — nhầm bước với đáp án

## Dạng 9: Đếm ngược (Count Down)
- Giống Dạng 8 nhưng đếm **ngược**.
- Công thức: đáp án = start − step
- **Phạm vi**: start và đáp án đều trong **[0, 1000]**; start phải > step (đáp án ≥ 0)
- **Bước nhảy**: cùng quy tắc Dạng 8
- Câu hỏi: `"Bạn [Tên] đếm ngược các số cách đều [step] đơn vị, bắt đầu từ số [start], số tiếp theo bạn ấy đếm được là:"`
- **wrong_pool** (5 phần tử):
  - `start - 2*step` — đếm thêm 1 bước nữa (đi quá đà)
  - `start` — quên không trừ (số ban đầu)
  - `start + step` — cộng thay vì trừ (sai chiều)
  - `đáp án ± nhỏ` — sai nhỏ
  - `step` — nhầm bước với đáp án

## Dạng 10: Tìm số hạng thứ N
- Cho tên nhân vật, số hạng đầu tiên, và quy luật ("cộng X" hoặc "trừ X"). Học sinh tìm giá trị của số hạng thứ 3 hoặc thứ 4.
- Công thức: số hạng thứ N = start + (N−1) × step (step dương nếu "cộng", âm nếu "trừ")
- **Chỉ hỏi số hạng thứ 3 hoặc thứ 4** (không hỏi các vị trí khác).
- **Bước nhảy**: |step| từ 2 đến 10 (bước "cộng" hay "trừ" đều ≤ 10 về giá trị tuyệt đối).
- **Phạm vi**: tất cả số hạng được nhắc đến (từ hạng 1 đến hạng được hỏi) nằm trong [-100, 100].
- Câu hỏi: `"[Tên] viết 1 dãy số. Số hạng đầu tiên trong dãy số là [start], [Tên] sử dụng quy luật "[cộng/trừ X]" để tính số hạng tiếp theo. Vậy số hạng thứ [ba/tư] trong dãy số là số nào?"`
- **wrong_pool** (5 phần tử):
  - Số hạng liền trước đáp án (N−1): đếm thiếu 1 bước
  - Số hạng liền sau đáp án (N+1): đếm dư 1 bước
  - Áp dụng sai chiều: start + (N−1) × (−step) — cộng thay vì trừ hoặc ngược lại
  - Số hạng đầu tiên (start): nhầm vị trí hạng 1 với hạng được hỏi
  - Số hạng thứ 2 (start + step): chỉ áp dụng quy luật 1 lần

## Dạng 11: Tìm số hạng từ cuối dãy
- Cho tên nhân vật, số hạng cuối (hạng 5), và quy luật "trừ X" để tính các số hạng trước đó. Học sinh tìm số hạng thứ 1, 2, hoặc 3.
- Dãy số gồm **5 số hạng**. Từ hạng cuối trừ X liên tục để tìm hạng trước → dãy xuôi luôn **tăng dần**: `[last−4X, last−3X, last−2X, last−X, last]`
- Công thức: số hạng thứ N = last − (5−N) × X
- **Chỉ hỏi số hạng thứ nhất, thứ hai, hoặc thứ ba**.
- **Bước nhảy**: X từ 2 đến 10 (luôn là "trừ X").
- **Phạm vi**: tất cả 5 số hạng nằm trong [-100, 100].
- Câu hỏi: `"[Tên] viết 1 dãy số gồm 5 số hạng, số cuối cùng trong dãy số là [last]. [Tên] dùng quy luật "trừ [X]" để tính các số hạng trước đó. Vậy số hạng thứ [nhất/hai/ba] trong dãy số là số nào?"`
- **wrong_pool** (5 phần tử):
  - Số hạng liền sau đáp án (N+1): đếm dư 1 vị trí
  - Số hạng liền trước đáp án (N−1, nếu N>1): đếm thiếu 1 vị trí
  - `last − X` (hạng 4): nhầm hạng cuối là hạng 1 → chỉ lùi 1 bước
  - Số hạng cuối (last): nhầm hạng cuối với đáp án
  - `last + X`: áp dụng sai chiều (đi tới thay vì lùi)

---
