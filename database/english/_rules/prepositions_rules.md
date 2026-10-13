# Rules: prepositions.json

## Mục tiêu
Học sinh chọn đúng giới từ **on / in / from** trong các ngữ cảnh thời gian và xuất xứ.

Đối tượng: học sinh cấp 1 (lớp 1–5) — từ vựng đơn giản, câu ngắn.

---

## Quy tắc sử dụng

| Giới từ | Dùng với | Ví dụ |
|---|---|---|
| **on** | Ngày trong tuần | on Monday, on Saturday |
| **on** | Ngày cụ thể (có số) | on 3rd May, on 25th December |
| **on** | Ngày lễ cụ thể | on New Year's Day, on Christmas Day |
| **in** | Tháng | in May, in December |
| **in** | Năm | in 2020, in 2018 |
| **in** | Mùa | in summer, in winter, in spring, in autumn |
| **from** | Quốc gia / địa điểm xuất xứ | from Japan, from Vietnam |
| **from** | Trong "come from / be from" | She is from France. / Where do you come from? |

### Điểm dễ nhầm

| Tình huống | Đúng | Sai |
|---|---|---|
| Chỉ tháng (không có ngày) | in May | ~~on May~~ |
| Ngày cụ thể trong tháng | on 3rd May | ~~in 3rd May~~ |
| Ngày trong tuần | on Monday | ~~in Monday~~ |
| Năm | in 2020 | ~~on 2020~~ |
| Mùa | in summer | ~~on summer~~ |
| Xuất xứ | from Japan | ~~in Japan~~ (khi hỏi quốc tịch) |

---

## Ghi chú khi thêm/sửa câu hỏi

- `correct` và `wrong_pool` đều là **chuỗi** (string).
- `wrong_pool` phải có **ít nhất 4** phần tử.
- Câu hỏi viết bằng tiếng Anh, chỗ trống dùng `___`.
- Câu ngắn, ngữ cảnh quen thuộc: sinh nhật, trường học, tiệc, kỳ nghỉ, thời tiết, thể thao.

---

## Wrong pool strategy

| Blank | Bẫy chính | Wrong pool gợi ý |
|---|---|---|
| **on** (ngày) | "in" (nhầm dùng in cho ngày) | in, at, for, from |
| **in** (tháng) | "on" (nhầm dùng on cho tháng) | on, at, for, from |
| **in** (năm/mùa) | "on" (nhầm) | on, at, for, from |
| **from** (xuất xứ) | "in" (nhầm với vị trí) | in, on, at, for |

**Bẫy quan trọng nhất**: Học sinh hay nhầm "on May" (sai) thay vì "in May" (đúng), và ngược lại nhầm "in 3rd May" thay vì "on 3rd May". Câu hỏi nên khai thác cả hai hướng nhầm này.

---

## Dạng câu hỏi

### Dạng 1: on + ngày trong tuần
- "School starts ___ Monday." → "on"

### Dạng 2: in + tháng
- "My birthday is ___ May." → "in"

### Dạng 3: on + ngày cụ thể (có số)
- "Christmas is ___ 25th December." → "on"
- Chú ý hint: nhắc học sinh "in December" (tháng) khác "on 25th December" (ngày cụ thể)

### Dạng 4: in + năm / mùa
- "I was born ___ 2016." → "in"
- "We go to the beach ___ summer." → "in"

### Dạng 5: from + quốc gia
- "She is ___ Japan." → "from"
- "Where do you come ___?" → "from"

---

## Phân bố (50 câu)

| Dạng | Số câu | ID |
|---|---|---|
| on + ngày trong tuần | 10 | 1–10 |
| in + tháng | 10 | 11–20 |
| on + ngày cụ thể | 10 | 21–30 |
| in + năm / mùa | 8 | 31–38 |
| from + quốc gia / địa điểm | 12 | 39–50 |

---

## Nếu muốn thêm dạng mới
Thêm section mới vào file này, cập nhật bảng phân bố, và thêm câu vào JSON với id tiếp theo.
