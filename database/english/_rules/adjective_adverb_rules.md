# Rules: adjective_adverb.json

## Mục tiêu
Học sinh phân biệt và dùng đúng **tính từ (adjective)** và **trạng từ (adverb)** trong câu:
- **Tính từ**: đứng sau động từ "to be" hoặc linking verb → mô tả danh từ (chủ ngữ)
- **Trạng từ**: đứng sau động từ thường → mô tả cách thực hiện hành động (thường = tính từ + -ly)

Đối tượng: học sinh cấp 1 (lớp 1–5) — từ vựng đơn giản.

---

## Quy tắc cơ bản

| Vị trí trong câu | Dùng | Ví dụ |
|---|---|---|
| Sau "is/am/are/was/were" | Tính từ (adjective) | The music is **loud**. |
| Sau linking verb (looks, sounds, smells, tastes, feels) | Tính từ (adjective) | The cake tastes **sweet**. |
| Sau động từ thường (action verb) | Trạng từ (adverb) | She speaks **softly**. |

**Cách nhận biết linking verb**: thay bằng "is/are" vẫn có nghĩa → đó là linking verb.
Ví dụ: "The soup smells good" = "The soup is good" ✓ → linking verb → dùng tính từ.

---

## Cách tạo trạng từ

| Trường hợp | Quy tắc | Ví dụ |
|---|---|---|
| Hầu hết | + -ly | slow → slowly, loud → loudly |
| Kết thúc -y | đổi y → i + -ly | happy → happily, noisy → noisily |
| Kết thúc -le | đổi -le → -ly | gentle → gently |

---

## Trường hợp đặc biệt (bất quy tắc)

| Tính từ | Trạng từ | Lưu ý |
|---|---|---|
| good | well | "He plays **well**." (KHÔNG phải "goodly") |
| fast | fast | "She runs **fast**." (KHÔNG thêm -ly) |
| hard | hard | "He works **hard**." (KHÔNG phải "hardly") |

**Lưu ý quan trọng**: "hardly" là trạng từ có nghĩa khác — "hầu như không" (barely).
Ví dụ: "She hardly eats." = "Cô ấy hầu như không ăn." ← khác hoàn toàn với "hard".

---

## Ghi chú khi thêm/sửa câu hỏi

- Mỗi câu phải cung cấp 2 lựa chọn rõ ràng trong ngoặc, ví dụ: "(loud / loudly)".
- `wrong_pool` phải có **ít nhất 4** phần tử.
- Bẫy chính luôn là dạng đối lập: tính từ ↔ trạng từ.
- Tránh dùng cặp "funny / funnily" (funny là tính từ khác nghĩa với fun).
- Với linking verbs: ưu tiên dùng looks, sounds, smells, tastes, feels.

---

## Wrong pool strategy

| Blank | Bẫy chính | Bẫy phụ |
|---|---|---|
| Tính từ (sau be) | Dạng trạng từ (-ly) | Comparative (-er), noun form |
| Trạng từ (sau action verb) | Dạng tính từ gốc | Comparative (-er), noun form |
| well | good — bẫy chính | goodly (không tồn tại), goods |
| hard (adv) | hardly — bẫy chính (nhầm nghĩa) | harder, harden |
| fast (adv) | fastly — bẫy chính (không tồn tại) | faster, fasted |

---

## Dạng câu hỏi

### Dạng 1: Điền tính từ (sau be/linking verb) — IDs 1–12
- Nhận dạng: động từ là is/am/are/was/were hoặc looks/sounds/smells/tastes/feels
- Đáp án là dạng tính từ gốc
- Ví dụ: "The music is ___. (loud / loudly)" → loud

### Dạng 2: Điền trạng từ (sau action verb) — IDs 13–24
- Nhận dạng: động từ là action verb (runs, speaks, walks, dances, writes...)
- Đáp án là dạng trạng từ (-ly)
- Ví dụ: "She speaks ___. (soft / softly)" → softly

### Dạng 3: Trường hợp bất quy tắc — IDs 25–30
- good → well: "He sings ___. (good / well)" → well
- hard (giữ nguyên): "She works ___. (hard / hardly)" → hard
- fast (giữ nguyên): "He runs ___. (fast / fastly)" → fast

---

## Phân bố (30 câu)

| Dạng | Số câu | ID |
|---|---|---|
| Điền tính từ sau be/linking verb | 12 | 1–12 |
| Điền trạng từ sau action verb | 12 | 13–24 |
| Trường hợp bất quy tắc (good/well, hard, fast) | 6 | 25–30 |

---

## Nếu muốn thêm dạng mới
Thêm section mới vào file này, cập nhật bảng phân bố, và thêm câu vào JSON với id tiếp theo.
