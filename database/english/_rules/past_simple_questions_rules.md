# Rules: past_simple_questions.json

## Mục tiêu
Học sinh biết cách **đặt câu hỏi trong thì Quá Khứ Đơn (Past Simple)**:
- Chọn đúng **Was / Were / Did** để bắt đầu câu hỏi Yes/No
- Chọn đúng **từ để hỏi (Wh-word)** phù hợp với nội dung câu trả lời

Đối tượng: học sinh cấp 1 (lớp 1–5) — từ vựng đơn giản, câu ngắn.

---

## Cấu trúc câu hỏi quá khứ đơn

| Loại | Cấu trúc | Ví dụ |
|---|---|---|
| Yes/No — to be | Was/Were + S + ...? | Was she at home? |
| Yes/No — action verb | Did + S + base form + ...? | Did they play football? |
| Wh- — action verb | Wh-word + did + S + base form? | Where did you go? |
| Wh- — to be | Wh-word + was/were + S? | Where was the cat? |

---

## Was vs Were vs Did

| Trường hợp | Dùng |
|---|---|
| Chủ ngữ số ít (he, she, it, danh từ số ít) + to be | Was |
| Chủ ngữ số nhiều (you, we, they, "A and B", danh từ số nhiều) + to be | Were |
| Bất kỳ chủ ngữ nào + động từ thường (action verb) | Did |

**Lưu ý**: Sau `Did` → luôn dùng **base form** (không chia).

---

## Wh-words và ý nghĩa

| Wh-word | Hỏi về | Câu trả lời điển hình |
|---|---|---|
| Where | Địa điểm | at the park / in Hanoi / under the table |
| Who | Người | my teacher / her friend / his uncle |
| What | Vật / hoạt động | football / rice / a new book |
| When | Thời gian | at 9 o'clock / last Friday / last summer |
| How | Cách thức / phương tiện / cảm giác | by plane / very well / very tired |

---

## Ghi chú khi thêm/sửa câu hỏi

- `correct` và `wrong_pool` đều là **chuỗi**.
- `wrong_pool` phải có **ít nhất 4** phần tử.
- Câu hỏi Wh- nên có gợi ý câu trả lời trong ngoặc để học sinh xác định wh-word.
- Mỗi câu phải có signal word hoặc ngữ cảnh quá khứ rõ ràng.

---

## Wrong pool strategy

| Blank | Bẫy chính |
|---|---|
| Was | Were (nhầm số nhiều), Did (nhầm sang action verb), Is/Does (nhầm hiện tại) |
| Were | Was (nhầm số ít), Did (nhầm sang action verb), Are/Do (nhầm hiện tại) |
| Did | Was/Were (nhầm sang to be), Does/Do (nhầm hiện tại) |
| Wh-word | Các wh-word khác không phù hợp với loại thông tin trong câu trả lời |

---

## Dạng câu hỏi

### Dạng 1: Điền Was (to be — chủ ngữ số ít)
- "she / he / it / danh từ số ít" + trạng ngữ quá khứ
- Ví dụ: "___ she at home yesterday?" → Was

### Dạng 2: Điền Were (to be — chủ ngữ số nhiều)
- "they / you / we / danh từ số nhiều / A and B" + trạng ngữ quá khứ
- Ví dụ: "___ they at the park last weekend?" → Were

### Dạng 3: Điền Did (action verb)
- Bất kỳ chủ ngữ nào + động từ thường (không phải to be) + trạng ngữ quá khứ
- Ví dụ: "___ she go to school yesterday?" → Did

### Dạng 4: Điền Wh-word — địa điểm (Where)
- Câu trả lời là địa điểm / vị trí
- Ví dụ: "___ did you go? (Answer: the zoo)" → Where

### Dạng 5: Điền Wh-word — người (Who)
- Câu trả lời là người
- Ví dụ: "___ did she see? (Answer: her friend)" → Who

### Dạng 6: Điền Wh-word — vật / hoạt động (What)
- Câu trả lời là vật hoặc hoạt động
- Ví dụ: "___ did they do? (Answer: played football)" → What

### Dạng 7: Điền Wh-word — thời gian (When)
- Câu trả lời là mốc / khoảng thời gian
- Ví dụ: "___ did he go to bed? (Answer: at 9 o'clock)" → When

### Dạng 8: Điền Wh-word — cách thức / phương tiện / cảm giác (How)
- Câu trả lời là cách làm, phương tiện, hoặc trạng thái
- Ví dụ: "___ did you travel? (Answer: by plane)" → How

---

## Phân bố (50 câu)

| Dạng | Số câu | ID |
|---|---|---|
| Điền Was | 8 | 1–8 |
| Điền Were | 8 | 9–16 |
| Điền Did | 9 | 17–25 |
| Wh-word: Where | 5 | 26–30 |
| Wh-word: Who | 5 | 31–35 |
| Wh-word: What | 5 | 36–40 |
| Wh-word: When | 5 | 41–45 |
| Wh-word: How | 5 | 46–50 |

---

## Nếu muốn thêm dạng mới
Thêm section mới vào file này, cập nhật bảng phân bố, và thêm câu vào JSON với id tiếp theo.
