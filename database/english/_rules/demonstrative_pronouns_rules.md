# Rules: demonstrative_pronouns.json

## Mục tiêu
Học sinh nhận biết và chọn đúng **đại từ chỉ định** (this / that / these / those) dựa vào hai tiêu chí: **số lượng** (ít/nhiều) và **khoảng cách** (gần/xa).

Đối tượng: học sinh cấp 1 (lớp 1–5) — câu ngắn, danh từ quen thuộc.

---

## Quy tắc chọn đại từ chỉ định

|  | Gần (near) | Xa (far) |
|---|---|---|
| **Số ít (singular)** | this | that |
| **Số nhiều (plural)** | these | those |

**Cách nhận biết số ít/nhiều:**
- Số ít: "is", "a/an + noun", danh từ không có -s
- Số nhiều: "are", danh từ có -s (books, friends, shoes...)

**Cách nhận biết gần/xa:**
- Gần: ngữ cảnh trong ngoặc ghi "gần em", "trong tay em", "trên bàn em", "đang đeo"...
- Xa: "ở đằng xa", "over there", "far away", "trên trời", "ở phía kia"...

---

## Ghi chú khi thêm/sửa câu hỏi

- `correct` và `wrong_pool` đều là **chuỗi**.
- `wrong_pool` luôn là 3 đại từ còn lại: ví dụ correct = "This" → wrong_pool = ["That", "These", "Those"].
- **Bắt buộc** thêm ngữ cảnh trong ngoặc vào câu hỏi để học sinh xác định gần/xa và số ít/nhiều.
- Hoa/thường của đại từ phụ thuộc vị trí trong câu: đầu câu viết hoa (This/That/These/Those), trong câu viết thường (this/that/these/those).

---

## Wrong pool strategy

Vì chỉ có 4 đại từ, wrong_pool luôn là **3 cái còn lại**. Bẫy chính là:

| Bẫy | Mô tả |
|---|---|
| Nhầm số ít ↔ số nhiều | Dùng "this" thay "these" hoặc ngược lại |
| Nhầm gần ↔ xa | Dùng "this" thay "that" hoặc ngược lại |
| Nhầm cả hai | Dùng "those" thay "this" |

---

## Dạng câu hỏi

### Dạng 1: ___ is/are + danh từ + (ngữ cảnh)
- "___ is my book. (1 cuốn, gần em)" → This

### Dạng 2: Is/Are ___ your + danh từ? (ngữ cảnh)
- "Is ___ your pencil case? (hộp bút ngay trước mặt em)" → this

### Dạng 3: Look! ___ is/are + miêu tả (ngữ cảnh)
- "Look! ___ is a rainbow! (ở trên trời, rất xa)" → That

### Dạng 4: What is/are ___? (ngữ cảnh)
- "What is ___? (chỉ vào 1 vật đang cầm trên tay)" → this

### Dạng 5: ___ + danh từ + is/are + tính từ (ngữ cảnh)
- "___ cake is delicious! (miếng bánh em đang ăn)" → This

---

## Phân bố (30 câu)

| Đại từ | Số lượng | ID |
|---|---|---|
| This | 8 | 1, 5, 9, 11, 15, 21, 23, 27 |
| That | 7 | 3, 7, 12, 16, 20, 25, 28... |
| These | 8 | 4, 8, 13, 17, 18*, 22, 29, 31... |
| Those | 7 | 2, 6, 10, 14, 19, 24, 26, 28, 30 |

*Chú ý: ID 17 và 18 dùng chữ thường (these/this) vì đại từ nằm sau động từ "are/is".

---

## Nếu muốn thêm dạng mới
Thêm section mới vào file này, cập nhật bảng phân bố, và thêm câu vào JSON với id tiếp theo.
