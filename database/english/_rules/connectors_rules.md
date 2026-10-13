# Rules: connectors.json

## Mục tiêu
Học sinh luyện tập 2 kỹ năng gộp trong 1 file:
1. **Like + V-ing**: Chia đúng động từ sang dạng -ing sau "like / likes / don't like / doesn't like"; chọn đúng "and / or / but" để nối ý.
2. **Từ nối thứ tự**: Chọn đúng từ nối (First, Then, Finally, After, Before, And) để diễn đạt thứ tự hành động.

Đối tượng: học sinh cấp 1 (lớp 1–5) — từ vựng đơn giản, ngữ cảnh gần gũi (trường học, sinh hoạt hàng ngày).

---

## Phần A: Like + V-ing

### Quy tắc

| Cấu trúc | Ví dụ |
|---|---|
| like / likes + V-ing | I like swimming. / She likes dancing. |
| don't / doesn't like + V-ing | He doesn't like eating vegetables. |
| like A **and** B | I like reading and drawing. (thích cả hai) |
| doesn't like A **or** B | She doesn't like singing or dancing. (không thích cả hai) |
| like A **but** not B | I like swimming but I don't like running. (tương phản) |

### V-ing spelling rules

| Trường hợp | Quy tắc | Ví dụ |
|---|---|---|
| Hầu hết | + ing | read → reading, play → playing |
| Kết thúc -e | bỏ e + ing | dance → dancing, make → making, write → writing |
| CVC ngắn (nhấn âm cuối) | nhân đôi phụ âm + ing | swim → swimming, run → running |

### Wrong pool strategy (Part A)

| Blank | Bẫy 1 | Bẫy 2 | Bẫy 3 | Bẫy 4 |
|---|---|---|---|---|
| **V-ing** | base form (swim) | third-person -s (swims) | past tense (swam) | to + V (to swim) |
| **and** | or (nhầm nghĩa "cả hai") | but | so | then |
| **or** | and (nhầm: "không thích cả hai") | but | so | then |
| **but** | and | or | so | then |

---

## Phần B: Từ nối thứ tự

### Quy tắc

| Từ nối | Nghĩa | Dùng khi |
|---|---|---|
| First / First of all | Đầu tiên | Bước đầu tiên trong chuỗi |
| Then | Sau đó (tiếp theo) | Bước giữa, ngay sau First |
| Finally | Cuối cùng | Bước kết thúc chuỗi |
| After (+ N/V-ing) | Sau khi | Hành động xảy ra SAU |
| Before (+ N/V-ing) | Trước khi | Hành động xảy ra TRƯỚC |
| And | Và | Nối 2 hành động liên tiếp hoặc đồng thời |

**Lưu ý**: "Then" và "Next" đều có thể chỉ "bước tiếp theo" — tránh ra câu hỏi mà cả hai đều đúng. Thiết kế câu hỏi rõ ràng bằng cách:
- Dùng "Then" khi bước trước là "First" và bước sau chưa xác định
- Dùng "Finally" khi đây rõ ràng là bước cuối (có First + Then trước đó)

### Wrong pool strategy (Part B)

| Blank | Bẫy chính |
|---|---|
| **First** | Then, Finally, After, Next |
| **Then** | First, Finally, Before, After |
| **Finally** | First, Next, Before, Then |
| **After** | Before (đối lập nghĩa), Then, Next, First |
| **Before** | After (đối lập nghĩa), Then, Next, Finally |
| **and** | or, but, then, so |

---

## Ghi chú khi thêm/sửa câu hỏi

- `correct` và tất cả `wrong_pool` đều là **chuỗi** (string).
- `wrong_pool` phải có **ít nhất 4** phần tử.
- Câu hỏi viết bằng tiếng Anh, chỗ trống dùng `___`.
- Với V-ing: ghi động từ gốc trong ngoặc sau câu hỏi, ví dụ: "I like ___ in the park. (run)"
- Với từ nối: đảm bảo chỉ có **một** đáp án đúng rõ ràng (tránh Then/Next mơ hồ).

---

## Dạng câu hỏi

### Dạng 1: Điền V-ing sau like/likes
- "She likes ___ (dance)." → "dancing"

### Dạng 2: Điền V-ing sau don't/doesn't like
- "He doesn't like ___ (eat) vegetables." → "eating"

### Dạng 3: Chọn and / or / but
- "I like reading ___ drawing." → "and"
- "She doesn't like singing ___ dancing." → "or"
- "I like swimming ___ I don't like running." → "but"

### Dạng 4: Chọn First / Then / Finally
- "___of all, open your book." → "First"
- "First, wash your hands. ___, eat your food." → "Then"
- "First, read. Then, think. ___, write." → "Finally"

### Dạng 5: Chọn After / Before
- "___ breakfast, I brush my teeth." → "After"
- "Wash your hands ___ eating." → "before"

### Dạng 6: Chọn And (nối hành động)
- "We sang songs ___ danced at the party." → "and"

---

## Phân bố (30 câu)

| Dạng | Số câu | ID |
|---|---|---|
| V-ing sau like/likes/don't like/doesn't like | 10 | 1–10 |
| and / or | 3 | 11–13 |
| but (tương phản) | 2 | 14–15 |
| First | 3 | 16–18 |
| Then | 3 | 19–21 |
| Finally | 3 | 22–24 |
| After | 2 | 25–26 |
| Before | 2 | 27–28 |
| And (nối hành động) | 2 | 29–30 |

---

## Nếu muốn thêm dạng mới
Thêm section mới vào file này, cập nhật bảng phân bố, và thêm câu vào JSON với id tiếp theo.
