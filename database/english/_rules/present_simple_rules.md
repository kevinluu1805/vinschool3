# Rules: present_simple.json

## Mục tiêu
Học sinh nhận dạng và dùng đúng **thì Hiện Tại Đơn (Present Simple)** thông qua các từ/cụm nhận dạng (signal words). Câu hỏi dạng điền vào chỗ trống: chọn dạng động từ hoặc trợ động từ đúng.

Đối tượng: học sinh cấp 1 (lớp 1–5) — dùng từ vựng đơn giản, câu ngắn.

---

## Signal words (từ nhận dạng)

| Nhóm | Ví dụ |
|---|---|
| Every + time | every day, every night, every morning, every afternoon, every evening |
| Every + period | every week, every month, every year |
| Every + weekday | every Monday, every Tuesday, ... every Sunday |
| Tần suất có số | once a day/week/month/year, twice a week/month, three times a year |
| Frequency adverbs | always, usually, often, sometimes, rarely, never |
| Other time phrases | on weekdays, on weekends, on Saturdays, in the morning, at night, before meals, after school |

Mỗi câu hỏi PHẢI chứa ít nhất 1 signal word.

---

## Quy tắc chia động từ (cần nắm để ra câu)

| Chủ ngữ | Dạng động từ |
|---|---|
| I / You / We / They | base form (play, go, eat...) |
| He / She / It / danh từ số ít | base form + **s/es** (plays, goes, eats...) |

Lưu ý thêm **-es** cho: go→goes, do→does, watch→watches, brush→brushes, wash→washes, teach→teaches, fly→flies, study→studies.

**Sau Does/Do → luôn dùng base form:** "Does she go?" (KHÔNG phải "Does she goes?")

---

## Ghi chú khi thêm/sửa câu hỏi

- `correct` và tất cả `wrong_pool` đều là **chuỗi** (string).
- `wrong_pool` phải có **ít nhất 4** phần tử (app chọn 3 hiển thị).
- Câu hỏi viết bằng tiếng Anh, chỗ trống dùng `___`.
- Dùng từ vựng đơn giản: go, eat, play, watch, drink, sleep, study, brush, wash, cook, have, do, run, ride, take, give, meet, help, visit, leave, write, listen, fly, say, get.
- Không dùng cấu trúc phức tạp (relative clause, passive...).

---

## Wrong pool strategy

| Bẫy | Ví dụ (đáp án đúng = "watches") | Ví dụ (đáp án đúng = "Does") |
|---|---|---|
| Quên -s/-es (base form) | "watch" | — |
| Thêm -s/-es sai chủ ngữ | "plays" khi chủ ngữ là "we" | — |
| Nhầm thì hiện tại tiếp diễn (-ing) | "watching" | — |
| Nhầm thì quá khứ | "watched" / "went" | "Did" |
| Nhầm cấu trúc (is/am/are + V) | "is watching" | "Is" / "Are" |
| Nhầm Does ↔ Do | — | "Do" |

Không dùng wrong_pool chỉ là ±1 ký tự hoặc lỗi chính tả ngẫu nhiên.

---

## Dạng câu hỏi

### Dạng 1: Điền động từ — He / She / It / danh từ số ít (khẳng định)
- Đáp án: verb + s/es
- Bẫy chính: base form (quên -s/-es), -ing, past, is + V-ing
- Ví dụ: "She ___ TV every night." → "watches"

### Dạng 2: Điền động từ — I / You / We / They (khẳng định)
- Đáp án: base form
- Bẫy chính: verb + s/es (nhầm quy tắc), -ing, past, are/am + V-ing
- Ví dụ: "We ___ football every week." → "play"

### Dạng 3: Signal word "once/twice/three times a [period]"
- Cùng quy tắc Dạng 1 & 2, chỉ khác signal word
- Ví dụ: "He ___ to the dentist twice a year." → "goes"

### Dạng 4: Frequency adverbs (always / usually / often / sometimes / rarely / never)
- Adverb đứng trước động từ chính (sau subject)
- Ví dụ: "She often ___ to music after school." → "listens"

### Dạng 5: Câu hỏi — điền động từ sau Does/Do
- Sau Does/Do → bắt buộc dùng **base form** (không thêm -s/-es)
- Bẫy chính: verb+s/es (nhầm quy tắc), -ing, past, is + V-ing
- Ví dụ: "Does your brother ___ to school every day?" → "go" (KHÔNG phải "goes")

### Dạng 6: Câu hỏi — điền Does hoặc Do
- He/She/It/danh từ số ít → Does; I/You/We/They → Do
- Bẫy chính: Does ↔ Do nhầm nhau, "Is/Are" (nhầm sang hiện tại tiếp diễn), "Did" (nhầm sang quá khứ)
- Ví dụ: "___ she always wake up early?" → "Does"

---

## Dạng 7: Phủ định — doesn't/don't + động từ
- Sau doesn't/don't → base form (không thêm -s/-es)
- Bẫy chính: verb+s/es, -ing, past, is/am/are + V-ing
- Ví dụ: "She doesn't ___ meat." → "eat" (KHÔNG phải "eats")

## Dạng 8: Điền does/do vào phủ định
- "She ___ not like rainy days." → "does"; "They ___ not go..." → "do"
- Bẫy chính: does ↔ do nhầm nhau, "is/are" (nhầm tense), "did" (past)

---

## Phân bố (100 câu)

| Dạng | Số câu | ID |
|---|---|---|
| He/She/It/danh từ số ít — every [time] | 6 | 1, 3, 5, 7, 8, 9 |
| I/You/We/They — every [time] | 4 | 2, 4, 6, 10 |
| Once/twice/... a [period] | 8 | 11–18 |
| Frequency adverbs | 8 | 19–26 |
| Câu hỏi — điền động từ sau Does/Do | 6 | 27, 29, 31, 32, 34, 36 |
| Câu hỏi — điền Does hoặc Do | 4 | 28, 30, 33, 35 |
| Mixed signal words | 14 | 37–50 |
| Phủ định — doesn't/don't + V | 7 | 51–57 |
| Điền does/do vào phủ định | 2 | 58, 91, 92 |
| Câu hỏi Does/Do (mở rộng) | 8 | 59–66 |
| Chủ ngữ mới, động từ mới | 10 | 67–76 |
| Động từ đa dạng — mixed | 24 | 77–100 |

---

## Nếu muốn thêm dạng mới
Thêm section mới vào file này, cập nhật bảng phân bố, và thêm câu vào JSON với id tiếp theo.
