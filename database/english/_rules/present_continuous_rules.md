# Rules: present_continuous.json

## Mục tiêu
Học sinh nhận dạng và dùng đúng **thì Hiện Tại Tiếp Diễn (Present Continuous)** thông qua signal words. Câu hỏi dạng điền vào chỗ trống: chọn đúng dạng V-ing hoặc trợ động từ am/is/are.

Đối tượng: học sinh cấp 1 (lớp 1–5) — từ vựng đơn giản, câu ngắn.

---

## Signal words (từ nhận dạng)

| Nhóm | Ví dụ |
|---|---|
| Thời điểm hiện tại | now, right now, at the moment |
| Câu mệnh lệnh gây chú ý | Look!, Listen!, Be quiet!, Keep silent!, Watch out!, Look out! |
| Xu hướng hiện tại | currently, these days |

---

## Cấu trúc

| Loại câu | Cấu trúc |
|---|---|
| Khẳng định | S + **am/is/are** + **V-ing** |
| Phủ định | S + **am/is/are + not** + V-ing (hoặc isn't / aren't) |
| Câu hỏi | **Am/Is/Are** + S + V-ing? |

**Chọn am / is / are theo chủ ngữ:**

| Chủ ngữ | Dùng |
|---|---|
| I | am |
| He / She / It / danh từ số ít | is |
| You / We / They / danh từ số nhiều | are |

---

## Quy tắc thêm -ing

| Trường hợp | Quy tắc | Ví dụ |
|---|---|---|
| Hầu hết động từ | + ing | cook→cooking, talk→talking, rain→raining |
| Kết thúc bằng -e | bỏ e + ing | write→writing, dance→dancing, ride→riding, shine→shining |
| Ngắn — kết thúc CVC | nhân đôi phụ âm cuối + ing | run→running, swim→swimming, sit→sitting |
| Kết thúc bằng -ie | đổi ie→y + ing | lie→lying, die→dying |

---

## Ghi chú khi thêm/sửa câu hỏi

- `correct` và `wrong_pool` đều là **chuỗi**.
- `wrong_pool` phải có **ít nhất 4** phần tử.
- Câu hỏi viết bằng tiếng Anh, chỗ trống dùng `___`.
- Câu Look! / Listen! / Watch out! kết thúc bằng `!`.
- Từ vựng phù hợp cấp 1: watch, swim, play, read, listen, eat, cook, run, write, walk, sing, build, wash, dance, draw, sleep, ride, climb, fly, call, rain, shine, laugh, study, learn, feel, drink, paint, tell, cry, bark, drive, sit, make, wait, come, work.

---

## Wrong pool strategy

| Blank | Bẫy 1 | Bẫy 2 | Bẫy 3 | Bẫy 4 |
|---|---|---|---|---|
| **V-ing** | base form (cook) | verb+s/es (cooks) | past (cooked) | to + V (to cook) |
| **is** (he/she/it) | are | am | was | does |
| **are** (you/we/they) | is | am | were | do |
| **am** (I) | is | are | was | do |
| **Is** (câu hỏi) | Are | Am | Does | Was |
| **Are** (câu hỏi) | Is | Am | Do | Were |
| **Am** (câu hỏi, I) | Is | Are | Do | Was |

Bẫy chính cho V-ing: học sinh hay dùng base form (quên -ing) hoặc verb+s/es (nhầm sang Present Simple).
Bẫy chính cho is/are: học sinh hay nhầm is ↔ are, hoặc dùng was/were (nhầm sang quá khứ).

---

## Dạng câu hỏi

### Dạng 1: Khẳng định — điền V-ing (now / right now / at the moment)
- "She is ___ TV right now." → "watching"

### Dạng 2: Khẳng định — điền is/are/am (now / right now / at the moment)
- "She ___ watching TV right now." → "is"

### Dạng 3: Look! / Listen! / Be quiet! / Watch out! — điền V-ing
- "Look! The cat is ___ up the tree!" → "climbing"

### Dạng 4: Look! / Listen! / Be quiet! / Watch out! — điền is/are
- "Look! The birds ___ flying!" → "are"

### Dạng 5: Currently / These days — điền V-ing
- "She is ___ hard these days." → "studying"

### Dạng 6: Currently / These days — điền is/are/am
- "Currently, she ___ studying very hard." → "is"

### Dạng 7: Phủ định — điền V-ing sau isn't / aren't / am not
- "She isn't ___ right now." → "sleeping"

### Dạng 8: Phủ định — điền is/are/am trong "S ___ not V-ing"
- "She ___ not dancing right now." → "is"

### Dạng 9: Câu hỏi — điền Is / Are / Am ở đầu câu
- "___ she studying right now?" → "Is"

### Dạng 10: Câu hỏi — điền V-ing sau Is / Are
- "Are they ___ football at the moment?" → "playing"

---

## Phân bố (100 câu)

| Dạng | Số câu | ID |
|---|---|---|
| Khẳng định — V-ing (now/right now/at the moment) | 20 | 1–20 |
| Khẳng định — is/are/am (now/right now/at the moment) | 10 | 21–30 |
| Look!/Listen!/Be quiet!/Watch out! — V-ing | 12 | 31–42 |
| Look!/Listen!/Be quiet!/Watch out! — is/are | 8 | 43–50 |
| Currently/These days — V-ing | 10 | 51–60 |
| Currently/These days — is/are/am | 5 | 61–65 |
| Phủ định — isn't/aren't + V-ing | 7 | 66–72 |
| Phủ định — S ___ not V-ing | 5 | 73–77 |
| Câu hỏi — Is/Are/Am ở đầu câu | 10 | 78–87 |
| Câu hỏi — V-ing sau Is/Are | 8 | 88–95 |
| Mixed | 5 | 96–100 |

---

## Nếu muốn thêm dạng mới
Thêm section mới vào file này, cập nhật bảng phân bố, và thêm câu vào JSON với id tiếp theo.
