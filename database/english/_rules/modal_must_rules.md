# Rules: modal_must.json

## Mục tiêu
Học sinh nhận biết và dùng đúng **must** (bắt buộc phải) và **mustn't** (bị cấm, không được làm) trong các tình huống quy tắc, an toàn, và thói quen sức khoẻ. Câu hỏi dạng điền vào chỗ trống.

Đối tượng: học sinh cấp 1 (lớp 1–5) — ngữ cảnh quen thuộc, câu ngắn.

---

## Cấu trúc

| Cấu trúc | Nghĩa | Ví dụ |
|---|---|---|
| must + V (base) | phải làm (bắt buộc) | You must wear your uniform. |
| mustn't + V (base) | không được làm (bị cấm) | You mustn't run in the classroom. |

**Lưu ý:** Sau must/mustn't → luôn dùng **base form** (động từ nguyên thể, không chia).

---

## Ngữ cảnh câu hỏi

| Nhóm | Ví dụ tình huống |
|---|---|
| Nội quy trường học | be quiet, do homework, wear uniform, bring books |
| Quy tắc an toàn | cross red light, touch electric socket, swim alone |
| Sức khoẻ & vệ sinh | wash hands, brush teeth, sleep early, drink clean water |
| Nơi công cộng | talk loudly in hospital, throw rubbish, write on walls |

---

## Ghi chú khi thêm/sửa câu hỏi

- `correct` và tất cả `wrong_pool` đều là **chuỗi** (string).
- `wrong_pool` phải có **ít nhất 4** phần tử.
- Chỗ trống dùng `___`.
- Ngữ cảnh câu phải đủ rõ để học sinh hiểu đây là bắt buộc hay cấm đoán.
- Tránh câu có thể đúng cho cả must lẫn mustn't.

---

## Wrong pool strategy

| Đáp án đúng | Bẫy 1 (quan trọng nhất) | Bẫy 2 | Bẫy 3 | Bẫy 4 |
|---|---|---|---|---|
| **must** | mustn't (nghĩa ngược) | can (khả năng, không phải bắt buộc) | should (khuyên, không bắt buộc) | don't / may |
| **mustn't** | must (nghĩa ngược) | can (không liên quan) | should (khuyên, không phải cấm) | may / could |

**Bẫy quan trọng nhất:** must ↔ mustn't (nghĩa hoàn toàn ngược nhau). Học sinh hay nhầm vì hình thức chữ viết giống nhau, chỉ khác phần "n't".

---

## Dạng câu hỏi

### Dạng 1: Quy tắc bắt buộc → must
- Ngữ cảnh: an toàn, vệ sinh, nội quy rõ ràng
- Ví dụ: "You ___ wash your hands before eating." → must

### Dạng 2: Quy tắc cấm đoán → mustn't
- Ngữ cảnh: hành vi nguy hiểm hoặc vi phạm nội quy
- Ví dụ: "You ___ run in the classroom." → mustn't

---

## Phân bố (30 câu)

| Nhóm chủ đề | Số câu | must | mustn't |
|---|---|---|---|
| Nội quy trường học | 10 | 5 | 5 |
| Quy tắc an toàn | 8 | 2 | 6 |
| Sức khoẻ & vệ sinh | 7 | 6 | 1 |
| Nơi công cộng | 5 | 2 | 3 |
| **Tổng** | **30** | **15** | **15** |

---

## Nếu muốn thêm dạng mới
Thêm section mới vào file này, cập nhật bảng phân bố, và thêm câu vào JSON với id tiếp theo.
