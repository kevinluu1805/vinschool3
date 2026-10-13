# Rules: question_words.json

## Mục tiêu
Học sinh nhận biết và chọn đúng **từ để hỏi (wh-word)** phù hợp với nội dung câu trả lời hoặc ngữ cảnh câu hỏi. Dạng bài điền vào chỗ trống đầu câu.

Đối tượng: học sinh cấp 1 (lớp 1–5) — chủ đề quen thuộc (trường học, gia đình, bạn bè, thời gian, địa điểm).

---

## Từ để hỏi và ý nghĩa

| Từ để hỏi | Hỏi về | Ví dụ câu trả lời |
|---|---|---|
| What | sự vật, hoạt động, môn học, nghề nghiệp, thức ăn | "Football." / "I eat rice." |
| Who | người | "My mum." / "My teacher." |
| Where | địa điểm | "At school." / "In the park." |
| When | thời gian | "On Monday." / "At 7 o'clock." |
| How | cách thức, tình trạng, sức khoẻ | "By bus." / "I am fine." |
| How old | tuổi | "I am 8 years old." |
| How tall | chiều cao | "I am 1.2 metres tall." |
| Which | lựa chọn giữa các phương án cụ thể | "The red one." / "Football." |
| How many | số lượng (đếm được) | "20 students." / "3 pets." |

---

## Ghi chú khi thêm/sửa câu hỏi

- `correct` và `wrong_pool` đều là **chuỗi**.
- `wrong_pool` phải có **ít nhất 4** phần tử.
- Câu hỏi phải đủ ngữ cảnh để CHỈ CÓ MỘT wh-word đúng.
- Với **Which**: phải có "or" hoặc liệt kê 2 lựa chọn cụ thể trong câu.
- Với **How many**: danh từ theo sau phải đếm được (số nhiều).
- Tránh câu mơ hồ có thể đúng cho nhiều wh-word.

---

## Wrong pool strategy

| Đáp án đúng | Không dùng những từ này trong wrong_pool |
|---|---|
| What | Who, Where, When, How (chọn 3–4 trong số này) |
| Who | What, Where, When, Which |
| Where | What, Who, When, How |
| When | What, Where, Who, Which |
| How | What, Where, Who, When |
| Which | What, Who, How, When |
| How many | How, What, Which, Who |

**Lưu ý:** "How many" và "How" dễ nhầm → luôn đưa "How" vào wrong_pool khi đáp án là "How many".

---

## Dạng câu hỏi

### Dạng 1: Hỏi về sự vật / hoạt động (What)
- "___ is your favourite colour?" → What

### Dạng 2: Hỏi về người (Who)
- "___ taught you to sing?" → Who

### Dạng 3: Hỏi về địa điểm (Where)
- "___ is the toilet?" → Where

### Dạng 4: Hỏi về thời gian (When)
- "___ does school start?" → When

### Dạng 5: Hỏi về cách thức / tình trạng / đặc điểm (How)
- "___ do you go to school?" → How
- "___ old are you?" → How
- "___ tall is your brother?" → How

### Dạng 6: Hỏi lựa chọn (Which)
- "___ bag is bigger — yours or mine?" → Which

### Dạng 7: Hỏi số lượng (How many)
- "___ students are in your class?" → How many

---

## Phân bố (30 câu)

| Wh-word | Số câu | ID |
|---|---|---|
| What | 6 | 1, 8, 15, 21, 26, 29 |
| Who | 5 | 2, 9, 13, 19, 28 |
| Where | 5 | 3, 10, 14, 20, 30 |
| When | 4 | 4, 11, 16, 23 |
| How | 5 | 5, 12, 17, 22, 25 |
| Which | 3 | 6, 18, 24 |
| How many | 2 | 7, 27 |
| **Tổng** | **30** | |

---

## Nếu muốn thêm dạng mới
Thêm section mới vào file này, cập nhật bảng phân bố, và thêm câu vào JSON với id tiếp theo.
