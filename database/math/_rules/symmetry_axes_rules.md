# Rules: symmetry_axes.json

## Mục tiêu
Cho một hình hoặc hoạ tiết, học sinh chọn **số trục đối xứng** (lấy từ Phiếu 8, Phần B – Câu 10). Có 3 nhóm:
- **Hình học cơ bản**: vuông, chữ nhật, tam giác đều, tam giác cân, tam giác vuông cân, thoi, ngũ/lục/thất/bát giác đều, thang cân, ngôi sao 5 cánh, chữ thập, ngôi nhà.
- **Hình 0 trục**: bình hành, tam giác thường/tù, thang vuông, chữ L (hai nhánh dài khác nhau), chong chóng 3 cánh, chữ S, hình vuông chia 2 màu bởi đường lệch. Chong chóng và chữ S chỉ đối xứng qua phép **xoay**, không có trục, nên dễ gây nhầm.
- **Hình có hoạ tiết**: hình gốc có thêm chấm, đường kẻ hoặc phần tô màu, làm giữ nguyên hoặc **giảm** số trục so với hình gốc.

Không dùng hình tròn (có vô số trục).

## Ghi chú khi thêm/sửa câu hỏi
- `correct`/`wrong_pool` là **string** chỉ chứa số: `"0"`, `"1"`, `"2"`…
- `wrong_pool` có **5** phần tử, không trùng đáp án.
- Câu hỏi:
  - Nhóm cơ bản và nhóm 0 trục: `"Hình dưới đây có bao nhiêu trục đối xứng?"`
  - Nhóm hoạ tiết: `"Hoạ tiết dưới đây có bao nhiêu trục đối xứng? (tính cả chấm, đường kẻ và phần tô màu bên trong)"`
  - Hình 0 trục có tô 2 màu (group `zero_color` trong script): `"Hình dưới đây có bao nhiêu trục đối xứng? (tính cả phần tô màu bên trong)"`
- `figure` = `figures/symmetry_<tên>.svg` (tương đối với `database/math/`), viết dạng HTML fragment, `viewBox="0 0 200 200"`, cùng style với `polygon_*.svg`.
  - Thứ tự vẽ: nền hình → phần tô màu (`#60a5fa`; `fill2` là màu cam `#fdba74`, dùng khi cần hình có 2 màu khác hẳn nhau, script coi 2 màu là khác nhau khi đếm trục) → chấm (`#1e3a8a`) và đường kẻ → viền hình (luôn nằm trên cùng).
- File JSON và SVG được sinh bằng `scripts/gen_symmetry_axes.py`. Muốn thêm hình thì thêm vào `ITEMS` rồi chạy `python3 scripts/gen_symmetry_axes.py`. Script **tự đếm số trục bằng hình học**: thử mọi trục đi qua trọng tâm (theo lưới 0,5°, cộng thêm các trục đi qua từng đỉnh và các trục là trung trực của từng cặp đỉnh, để bắt được trục ở góc lẻ như của thất giác đều), rồi kiểm tra ảnh của từng chấm, cạnh, đường kẻ và vùng tô có trùng với hình ban đầu không. Vì vậy `correct` luôn khớp với hình vẽ. Khi thêm hình mới, hãy chạy lại kiểm tra này, không tự đếm bằng tay.

## Phân bố (50 câu)
| Nhóm | Số câu | ID |
|---|---|---|
| Hình học cơ bản | 15 | 1–10, 31–35 |
| Hình 0 trục | 9 | 11–15, 36–39 |
| Hình có hoạ tiết | 26 | 16–30, 40–50 |

### Danh sách hình
| ID | Hình | Số trục |
|---|---|---|
| 1 | Vuông | 4 |
| 2–3 | Chữ nhật ngang / đứng | 2 |
| 4 | Tam giác đều | 3 |
| 5 | Tam giác cân | 1 |
| 6 | Thoi | 2 |
| 7 | Ngũ giác đều | 5 |
| 8 | Lục giác đều | 6 |
| 9 | Thang cân | 1 |
| 10 | Bát giác đều | 8 |
| 11–15 | Bình hành, tam giác thường, thang vuông, hình vuông chia 2 màu bởi đường lệch (xanh/cam), chữ S | 0 |
| 16 | Vuông + 4 chấm đối xứng (như đề) | 4 |
| 17 | Vuông + 1 chấm ở góc | 1 (đường chéo) |
| 18 | Vuông + 1 chấm giữa cạnh trên | 1 (trục dọc) |
| 19 | Vuông + 1 đường chéo | 2 (hai đường chéo) |
| 20 | Vuông tô nửa trái | 1 (trục ngang) |
| 21 | Vuông tô 1 ô góc | 1 (đường chéo) |
| 22 | Vuông tô 2 ô chéo nhau | 2 (hai đường chéo) |
| 23 | Vuông + dấu cộng | 4 |
| 24 | Chữ nhật + chấm ở tâm | 2 |
| 25 | Chữ nhật + chấm ở góc | 0 |
| 26 | Tam giác đều + chấm ở tâm | 3 |
| 27 | Tam giác đều + chấm gần đỉnh | 1 |
| 28 | Vuông + hình tròn ở giữa | 4 |
| 29 | Vuông + 2 chấm giữa cạnh trái/phải | 2 |
| 30 | Vuông + dải màu ngang ở giữa | 2 |
| 31 | Ngôi sao 5 cánh | 5 |
| 32 | Chữ thập | 4 |
| 33 | Ngôi nhà | 1 |
| 34 | Tam giác vuông cân | 1 |
| 35 | Thất giác đều | 7 |
| 36–39 | Bình hành nghiêng trái, tam giác tù, chữ L, chong chóng 3 cánh | 0 |
| 40 | Lục giác đều + chấm ở tâm | 6 |
| 41 | Lục giác đều + chấm gần 1 đỉnh | 1 |
| 42 | Chữ nhật + 1 đường chéo | 0 (bẫy: chữ nhật có 2 trục) |
| 43 | Vuông + 2 đường chéo | 4 |
| 44 | Vuông tô 4 ô nhỏ ở 4 góc | 4 |
| 45 | Vuông tô 3 trong 4 ô | 1 (đường chéo) |
| 46 | Thoi + chấm gần đỉnh trên | 1 |
| 47 | Tam giác đều + đường kẻ từ đỉnh xuống giữa đáy | 1 |
| 48 | Vuông + thoi tô màu bên trong | 4 |
| 49 | Chữ nhật tô nửa trên | 1 (trục dọc) |
| 50 | Vuông + 3 chấm trên đường chéo | 2 |

## Chiến lược wrong_pool (5 phần tử)
- **Nhóm hoạ tiết**: trap đầu tiên luôn là **số trục của hình gốc** (vd vuông có chấm ở góc → `"4"`), vì học sinh hay quên tính phần hoạ tiết.
- Các bẫy còn lại dựa trên đáp án đúng:

| Đúng | wrong_pool | Lý do |
|---|---|---|
| 0 | 1, 2, 4, 3, 6 | nhầm đối xứng xoay thành có trục (chong chóng → 4) |
| 1 | 2, 0, 3, 4, 6 | |
| 2 | 4, 1, 0, 3, 6 | nghĩ đường chéo chữ nhật/thoi cũng là trục → 4 |
| 3 | 1, 6, 2, 0, 4 | đếm mỗi nửa trục riêng → 6 |
| 4 | 2, 8, 1, 0, 3 | quên hai đường chéo → 2; đếm nửa trục → 8 |
| 5 | 4, 6, 10, 3, 1 | |
| 6 | 3, 4, 5, 12, 8 | chỉ đếm trục qua đỉnh → 3 |
| 7 | 6, 8, 14, 5, 1 | |
| 8 | 4, 6, 16, 7, 2 | |
