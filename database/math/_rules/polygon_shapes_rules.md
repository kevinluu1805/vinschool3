# Rules: polygon_shapes.json

## Mục tiêu
Cho một hình vẽ, học sinh chọn tên hình. Chỉ có **1 dạng bài**: nhận biết hình.

12 hình: tam giác, chữ nhật, vuông, thoi, bình hành, thang, ngũ giác, lục giác, thất giác, bát giác, cửu giác, thập giác.

## Ghi chú khi thêm/sửa câu hỏi
- `correct` và tất cả `wrong_pool` đều là **string**, có tiền tố "Hình " (vd: `"Hình thoi"`).
- `wrong_pool` có **5** phần tử (app chọn ngẫu nhiên 3).
- Câu hỏi luôn là `"Hình dưới đây là hình gì?"`.
- Hình nằm trong trường `figure` — đường dẫn **tương đối với `database/math/`**, trỏ tới file SVG trong `figures/`.
  - Tên file: `figures/polygon_<hình>_<biến thể 1-3>.svg`
  - File là HTML fragment (không có `<html>`/`<body>`), chứa `<svg viewBox="0 0 200 200">` với một `<polygon>`.
- Khi thêm hình mới: tạo file SVG trong `figures/`, thêm câu vào JSON với `figure` tương ứng.

## Phân bố (36 câu — mỗi hình 3 biến thể)
| Hình | ID | 3 biến thể |
|---|---|---|
| Tam giác | 1–3 | cân đều / cân cao / vuông |
| Chữ nhật | 4–6 | ngang / đứng / ngang dẹt |
| Thoi | 7–9 | đứng / dẹt / hẹp (luôn đặt theo hướng kim cương, không vẽ nghiêng) |
| Ngũ giác | 10–12 | đều, xoay 0° / ½ góc / ¼ góc |
| Lục giác | 13–15 | như trên |
| Thất giác | 16–18 | như trên |
| Bát giác | 19–21 | như trên |
| Cửu giác | 22–24 | như trên |
| Thập giác | 25–27 | như trên |
| Bình hành | 28–30 | nghiêng phải / nghiêng trái / đứng |
| Thang | 31–33 | cân / cân (rộng) / vuông |
| Vuông | 34–36 | 3 kích thước, **luôn đặt thẳng** (không xoay) |

## Ràng buộc hình vẽ (tránh đáp án mơ hồ)
- **Hình vuông không xoay**: xoay 45° sẽ giống hình thoi.
- **Chữ nhật**: chiều dài ≠ chiều rộng rõ rệt (không gần vuông).
- **Thoi**: 4 cạnh bằng nhau, **không có góc vuông**, luôn đặt theo hướng kim cương (đỉnh trên/dưới). **Không vẽ thoi nghiêng** vì trông y hệt hình bình hành.
- **Bình hành**: 2 cặp cạnh song song, cạnh dài ≥ ~1,7 lần cạnh ngắn (lệch rõ để không giống hình thoi), **không có góc vuông**.
- **Thang**: chỉ **1 cặp** cạnh song song (không vẽ thành bình hành).
- Đa giác ≥ 5 cạnh: đa giác **đều**.

## Chiến lược wrong_pool (5 phần tử)
Quy tắc cốt lõi: **không đưa vào `wrong_pool` tên hình cũng đúng về mặt toán học** (vì vuông ⊂ chữ nhật ⊂ bình hành ⊂ thang; vuông ⊂ thoi ⊂ bình hành).

| Đáp án đúng | wrong_pool | Lý do loại |
|---|---|---|
| Tam giác | chữ nhật, ngũ giác, vuông, thang, lục giác | — |
| Chữ nhật | vuông, thoi, tam giác, ngũ giác, lục giác | loại bình hành, thang (chữ nhật cũng là bình hành/thang) |
| Thoi | vuông, chữ nhật, tam giác, ngũ giác, lục giác | loại bình hành, thang |
| Bình hành | chữ nhật, thoi, vuông, tam giác, ngũ giác | loại thang |
| Thang | bình hành, chữ nhật, thoi, vuông, tam giác | — |
| Vuông | tam giác, ngũ giác, lục giác, thất giác, bát giác | loại chữ nhật, thoi, bình hành, thang |
| n-giác đều | các đa giác có số cạnh **gần** n (n±1, n±2) + 1 hình khác | bẫy đếm sai số cạnh |

Với đa giác đều (ngũ → thập giác), bẫy chính là **đếm nhầm số cạnh 1–2 cạnh** → ưu tiên n±1, n±2.
