# Rules: secret_code.json

## Mục tiêu
Bài "Mật mã con vật" (tìm số chưa biết trong phép cộng/trừ). Mỗi con vật là một chữ số; học sinh giải 4 phép tính để tìm số lượng từng con, rồi ghép theo thứ tự thành mật mã 4 chữ số.

Ví dụ (câu 1, đúng đề gốc):
```
7 + 🐦 = 12        → 🐦 = 5
🐰 + 8 = 15        → 🐰 = 7
🐰 − 🐦 = 🐔       → 🐔 = 2
🐿️ − 🐔 = 6        → 🐿️ = 8
Mật mã: 🐦 🐰 🐔 🐿️ → 5728
```

## Ghi chú khi thêm/sửa câu hỏi
- File được sinh bằng `scripts/gen_secret_code.py` (seed cố định). **Sửa script rồi chạy lại, không sửa JSON hay file hình bằng tay.**
- Mỗi câu có `figure` = `figures/secret_code_<id>.html` (HTML fragment: 4 dòng phép tính + hàng ô "Mật mã" theo thứ tự).
- Câu hỏi luôn nêu rõ **thứ tự ghép** các con vật (để đáp án không mơ hồ).
- `correct`/`wrong_pool` là string 4 chữ số, không bắt đầu bằng 0; `wrong_pool` có **5** phần tử khác nhau.
- Có `hint` chỉ nêu cách làm (giải từng dòng từ trên xuống), không cho đáp số.

## Cấu trúc đề
- Giá trị mỗi con vật: **1–9**, 4 con khác nhau.
- Mọi số hiện trong phép tính: **1–20** (chỉ cộng/trừ).
- Dòng 1: tìm con thứ 1 chỉ từ số (`a + 🐦 = b`, `🐦 + a = b`, `🐦 − a = b`, `a − 🐦 = b`).
- Dòng 2: tìm con thứ 2 **từ con thứ 1 và một số** (`🐦 + 🐰 = n`, `🐰 + 🐦 = n`, `🐰 − 🐦 = n`, `🐦 − 🐰 = n`) — mỗi dòng phải dùng con vừa tìm ở dòng trước.
- Dòng 3: tìm con thứ 3 từ con 1 và con 2 (`🐦 + 🐰 = 🐔`, `🐰 − 🐦 = 🐔`, …). Dòng 3 phải **khác phép tính** với dòng 2 (dòng 2 cộng thì dòng 3 trừ và ngược lại), để dòng 3 không lặp lại vế trái của dòng 2.
- Dòng 4: tìm con thứ 4 từ con 3 và một số (`🐿️ − 🐔 = a`, `🐔 + 🐿️ = a`, `a − 🐿️ = 🐔`, …).
- Bộ con vật xoay vòng: 🐦🐰🐔🐿️ / 🐶🐱🐟🐢 / 🐮🐷🐑🐴 / 🦆🐹🦜🐇 / 🐐🐠🐥🐈. Lời dẫn xoay vòng 3 câu chuyện (cánh cổng, rương kho báu, tủ đồ chơi).

## Chiến lược wrong_pool (ưu tiên theo thứ tự)
| Bẫy | Ví dụ (đáp án 5728) |
|---|---|
| Dùng nhầm phép tính ở một dòng (cộng thay vì trừ), **sai lan sang các dòng sau** — chỉ lấy khi mọi giá trị vẫn là chữ số | 5724 (dòng 4: 6 − 2) |
| Ghép ngược thứ tự | 8275 |
| Đổi chỗ 2 con đầu | 7528 |
| Đổi chỗ 2 con cuối | 5782 |
| Đổi chỗ 2 con giữa | 5278 |

## Phân bố (30 câu)
| ID | Nội dung |
|---|---|
| 1 | Đề gốc (5728) — ngoại lệ: dòng 2 không dùng 🐦 |
| 2–30 | Sinh ngẫu nhiên theo cấu trúc trên, mật mã không trùng nhau |
