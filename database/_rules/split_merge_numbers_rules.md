# Rules: split_merge_numbers.json

## Mục tiêu
Bộ câu hỏi gồm 5 dạng:
- **Dạng 1**: Đọc mô tả từng hàng số → ghép thành số 5 chữ số.
- **Dạng 2**: Đọc mô tả từng hàng số → ghép thành số 6 chữ số.
- **Dạng 3**: Cho 4 cách tách một số, tìm ra cách tách sai.
- **Dạng 4**: Đọc mô tả giá trị của từng chữ số → ghép thành số 5 chữ số.
- **Dạng 5**: Hoàn thành phép tính có một ô trống (`....`), dùng phép nhân hoặc chia.

Phạm vi số: **chỉ số dương nguyên**, **mọi số trong phép tính < 999,999**.

## Ghi chú khi thêm/sửa câu hỏi
- `correct` và tất cả `wrong_pool` đều là **string** (kể cả khi là số thuần).
- `wrong_pool` phải có **ít nhất 5** phần tử (khuyến nghị 5, app chọn ngẫu nhiên 3).
- Không để `wrong_pool` chứa đúng đáp án đúng.

## Phân bố (40 câu)
| Dạng | Số câu | ID |
|---|---|---|
| Ghép số 5 chữ số (mô tả theo hàng) | 5 | 1–5 |
| Ghép số 6 chữ số (mô tả theo hàng) | 5 | 6–10 |
| Tìm cách tách sai | 10 | 11–20 |
| Ghép số 5 chữ số (mô tả theo giá trị chữ số) | 10 | 21–30 |
| Hoàn thành phép tính (× hoặc ÷) | 10 | 31–40 |

## Nếu muốn thêm dạng mới
Thêm một section mới vào file này, cập nhật bảng phân bố, và thêm câu hỏi vào JSON với id tiếp theo.

---

## Dạng 1: Ghép số 5 chữ số

### Mô tả
Cho mô tả bằng lời của từng chữ số ở từng hàng. Học sinh ghép lại thành số hoàn chỉnh.

### Hàng vị trí (5 chữ số)
```
[chục nghìn] [nghìn] [trăm] [chục] [đơn vị]
     X           X      X      X       X
```

### Format câu hỏi
```
"[Tên] nghĩ tới một số có 5 chữ số. Số đó có chữ số [A] ở hàng [h1] và hàng [h2], có chữ số [B] ở hàng [h3] và hàng [h4], có chữ số [C] ở hàng [h5]. Vậy [Tên] đang nghĩ tới số nào?"
```
- Nhóm các hàng có **cùng chữ số** vào một mệnh đề.
- Nếu chữ số chỉ xuất hiện ở một hàng: bỏ "và hàng ...".
- Liệt kê mệnh đề từ hàng **cao đến thấp** (chục nghìn → đơn vị).

### Chiến lược số
- Ưu tiên dùng **số đối xứng (palindrome-like)**: chục nghìn = đơn vị, nghìn = chục, trăm là hàng giữa.
  - Ví dụ: 36036 → "chữ số 3 ở chục nghìn và chục, chữ số 6 ở nghìn và đơn vị, chữ số 0 ở trăm"
- Hoặc: chục nghìn = đơn vị, nghìn và chục khác nhau, trăm khác.
  - Ví dụ: 52815 → "chữ số 5 ở chục nghìn và đơn vị, chữ số 2 ở nghìn, chữ số 8 ở trăm, chữ số 1 ở chục"

### Chiến lược wrong_pool (5 phần tử — số khác nhau dùng đúng các chữ số của đáp án, chỉ đổi chỗ)
| Bẫy | Mô tả | Ví dụ (đúng: 36036) |
|---|---|---|
| Hoán vị chục nghìn ↔ nghìn | Đổi chỗ hai chữ số đầu | 63036 |
| Hoán vị trăm ↔ chục | Đổi chỗ hai chữ số giữa | 36306 |
| Hoán vị chục ↔ đơn vị | Đổi chỗ hai chữ số cuối | 36063 |
| Đặt sai hàng chữ số 0 | Chuyển 0 sang nghìn thay vì trăm | 30636 |
| Hoán vị khác | Sắp xếp lại các chữ số theo cách khác | 60363 |

---

## Dạng 2: Ghép số 6 chữ số

### Mô tả
Tương tự Dạng 1 nhưng với số 6 chữ số.

### Hàng vị trí (6 chữ số)
```
[trăm nghìn] [chục nghìn] [nghìn] [trăm] [chục] [đơn vị]
      X             X         X      X      X       X
```

### Format câu hỏi
```
"[Tên] nghĩ tới một số có 6 chữ số. Số đó có chữ số [A] ở hàng [h1] và hàng [h2], có chữ số [B] ở hàng [h3] và hàng [h4], có chữ số [C] ở hàng [h5] và hàng [h6]. Vậy [Tên] đang nghĩ tới số nào?"
```

### Chiến lược số
- Dùng số đối xứng 6 chữ số: trăm nghìn = đơn vị, chục nghìn = chục, nghìn = trăm.
  - Ví dụ: 362263 → "chữ số 3 ở trăm nghìn và đơn vị, chữ số 6 ở chục nghìn và chục, chữ số 2 ở nghìn và trăm"

### Chiến lược wrong_pool (5 phần tử — tương tự Dạng 1, áp dụng cho 6 hàng)
| Bẫy | Mô tả | Ví dụ (đúng: 362263) |
|---|---|---|
| Hoán vị trăm nghìn ↔ chục nghìn | Đổi hai chữ số đầu | 632263 |
| Hoán vị chục nghìn ↔ nghìn | Đổi cặp thứ hai | 326263 |
| Hoán vị nghìn ↔ trăm | Đổi hai hàng giữa | 362632 |
| Hoán vị chục ↔ đơn vị | Đổi hai chữ số cuối | 362236 |
| Hoán vị khác | Sắp xếp lại theo cách khác | 263362 |

---

## Dạng 3: Tìm cách tách sai

### Mô tả
Cho 4 cách tách một số 5 chữ số. Trong đó 3 cách đúng và 1 cách sai. Học sinh chọn cách sai.

### Format câu hỏi
```
"Bốn bạn cùng thực hiện tách số [X], có một đáp án sai, đó là đáp án nào?"
```
- Mỗi đáp án là chuỗi: `"[X] = [thành phần 1] + [thành phần 2] + ..."`

### Cấu trúc JSON
- **`correct`** = chuỗi biểu thức tách **SAI** (tổng ≠ X). Đây là đáp án học sinh cần chọn.
- **`wrong_pool`** = 5 chuỗi biểu thức tách **ĐÚNG** (tổng = X). App chọn 3 ngẫu nhiên làm đáp án nhiễu.

### Chiến lược wrong_pool (5 cách tách ĐÚNG, đa dạng cách nhóm)
| Nhóm | Ví dụ (số 75903) |
|---|---|
| Full breakdown (từng hàng riêng, bỏ hàng = 0) | `75903 = 70000 + 5000 + 900 + 3` |
| Nhóm 2 hàng đầu | `75903 = 75000 + 900 + 3` |
| Nhóm 2 hàng cuối hoặc 3 hàng cuối | `75903 = 75900 + 3` hoặc `75903 = 903 + 75000` |
| Nhóm chục nghìn + phần còn lại | `75903 = 70000 + 5903` |
| Đảo thứ tự | `75903 = 903 + 75000` |

### 3 kiểu lỗi cho cách tách SAI
#### Kiểu 1: Hoán đổi 2 hàng liền nhau
Đổi chỗ giá trị của 2 chữ số ở 2 hàng kề nhau.

| Hàng hoán đổi | Ví dụ (số 75903, đúng: 70000+5000+900+3) | Cách tách sai |
|---|---|---|
| chục nghìn ↔ nghìn | 7↔5 | `50000 + 70000 + 900 + 3` |
| nghìn ↔ trăm | 5↔9 (5000→500, 9000→9) | `79000 + 500 + 3` |
| trăm ↔ chục | (bỏ qua nếu một hàng = 0) | — |
| chục ↔ đơn vị | (bỏ qua nếu một hàng = 0) | — |

**Lưu ý**: Nếu một trong hai hàng bằng 0, chọn cặp hàng khác để hoán đổi.

#### Kiểu 2: Bỏ sót một hàng
Thiếu một thành phần có giá trị ≠ 0 trong phân tích.

| Hàng bỏ sót | Ví dụ (số 46218, đúng: 46000+200+18) | Cách tách sai |
|---|---|---|
| Bỏ trăm | thiếu 200 | `46000 + 10 + 8` |
| Bỏ chục | thiếu 30 | `57000 + 400 + 8` (số 57438) |
| Bỏ nghìn | thiếu 1000 | `70000 + 400 + 30 + 9` (số 71439) |

**Lưu ý**: Chỉ bỏ sót hàng có chữ số ≠ 0; không bỏ chục nghìn (quá dễ nhận ra).

#### Kiểu 3: Nhân đôi một hàng
Một chữ số xuất hiện ở đúng hàng của nó **và** ở thêm một hàng cao hơn sai.

- Pattern: lấy digit D ở hàng thấp (đúng), nhét thêm D × 10 vào hàng liền trên (sai).
- Ví dụ (số 83754): digit 7 ở trăm (700). Thêm 7 ở nghìn (7000) → sai.
  - Cách tách sai: `80000 + 3000 + 7000 + 700 + 50 + 4`
- Ví dụ (số 94125): digit 1 ở trăm (100). Thêm 1 ở nghìn (1000) → sai.
  - Cách tách sai: `90000 + 4000 + 1000 + 100 + 20 + 5`

**Lưu ý**: Chọn digit nhân đôi ≠ 0. Hàng sai thêm vào phải là hàng NGAY TRÊN hàng đúng.

### Phân bố kiểu lỗi (10 câu)
| Kiểu lỗi | Số câu | ID | Hàng lỗi |
|---|---|---|---|
| Hoán đổi 2 hàng liền nhau | 4 | 11, 14, 17, 18 | nghìn↔trăm / trăm↔chục / chục nghìn↔nghìn |
| Bỏ sót một hàng | 3 | 12, 15, 19 | trăm / chục / nghìn |
| Nhân đôi một hàng | 3 | 13, 16, 20 | trăm→nghìn |

### Ràng buộc cách tách sai
- Tổng các thành phần ≠ số gốc X.
- Dùng đúng các chữ số có trong X, chỉ đặt sai vị trí (không thêm chữ số lạ).
- Cách tách sai phải **trông hợp lý** — học sinh phải tính mới phát hiện sai.

---

## Dạng 5: Hoàn thành phép tính

### Mô tả
Một phép tính nhân hoặc chia có **một ô trống** (`....`). Học sinh tìm số còn thiếu.

### Format câu hỏi
```
"Hoàn thành phép tính sau: [A] × .... = [C]"
"Hoàn thành phép tính sau: .... ÷ [B] = [C]"
"Hoàn thành phép tính sau: [A] ÷ [B] = ...."
```
- Ô trống `....` có thể ở **bất kỳ vị trí nào** trong 3 số của phép tính.
- Dùng ký hiệu `×` (nhân) và `÷` (chia), không dùng `*` hay `/`.

### Công thức tính đáp án theo vị trí ô trống
| Phép tính | Vị trí ô trống | Công thức đáp án |
|---|---|---|
| `.... × B = C` | Thừa số 1 | `C ÷ B` |
| `A × .... = C` | Thừa số 2 | `C ÷ A` |
| `A × B = ....` | Tích | `A × B` |
| `.... ÷ B = C` | Số bị chia | `B × C` |
| `A ÷ .... = C` | Số chia | `A ÷ C` |
| `A ÷ B = ....` | Thương | `A ÷ B` |

### Ràng buộc
- Tất cả 3 số trong phép tính phải là **số nguyên dương** và **< 999,999**.
- Với phép chia: đảm bảo A **chia hết** cho B (thương là số nguyên).
- **Số chia** (B trong `A ÷ B = C`) phải là **bội số của 10**.
- **Phần `....`** (đáp án mà học sinh phải điền) phải là **bội số của 10**.
- Đáp án không được trùng với bất kỳ số nào trong wrong_pool.

### Chiến lược wrong_pool (5 phần tử)
| Bẫy | Mô tả | Ví dụ (.... ÷ 10 = 74, đúng: 740) |
|---|---|---|
| Dùng một trong các số đã biết | Học sinh ghi lại số có sẵn trong đề | "74" hoặc "10" |
| Sai phép tính (cộng/trừ thay vì nhân/chia) | Cộng hoặc trừ thay vì nhân | "84" (74+10), "64" (74−10) |
| Sai hệ số (×10 vs ×100) | Nhân nhầm với bậc lũy thừa khác | "7400" (74×100) |
| Gần đúng nhưng sai | Kết quả gần đúng nhưng tính sai một bước | "700" (70×10) |
| Phép tính ngược | Chia thay vì nhân hoặc ngược lại | "7" (74÷10, làm tròn) |

### Phân bố (10 câu, ID 31–40)
| ID | Phép tính | Vị trí ô trống | Đáp án |
|---|---|---|---|
| 31 | .... ÷ 10 = 74 | Số bị chia | 740 |
| 32 | 360 ÷ .... = 12 | Số chia | 30 |
| 33 | 4500 ÷ 50 = .... | Thương | 90 |
| 34 | .... × 8 = 640 | Thừa số 1 | 80 |
| 35 | 9 × .... = 630 | Thừa số 2 | 70 |
| 36 | 12 × 15 = .... | Tích | 180 |
| 37 | .... ÷ 20 = 35 | Số bị chia | 700 |
| 38 | 840 ÷ .... = 42 | Số chia | 20 |
| 39 | .... × 50 = 2500 | Thừa số 1 | 50 |
| 40 | 7 × .... = 490 | Thừa số 2 | 70 |

---

## Dạng 4: Ghép số từ mô tả giá trị chữ số

### Mô tả
Học sinh đọc mô tả **giá trị** (value) của từng chữ số và ghép lại thành số hoàn chỉnh. Khác Dạng 1/2 (mô tả theo tên hàng), Dạng 4 dùng giá trị số cụ thể (ví dụ: "giá trị 50000", "giá trị 50").

### Đặc điểm quan trọng
- Cùng một **chữ số** có thể xuất hiện ở **nhiều hàng** với các giá trị khác nhau → được nhóm lại: "chữ số X có giá trị [v1] và [v2]".
- Chữ số **0** không được nhắc đến (giá trị 0 không đáng kể).
- Học sinh phải suy ngược từ giá trị → xác định hàng → ghép số.

### Hàng vị trí và giá trị tương ứng (5 chữ số)
```
Hàng:    chục nghìn   nghìn   trăm   chục   đơn vị
Giá trị:   X0000      X000    X00     X0      X
```

### Format câu hỏi
```
"[Tên] nghĩ tới một số có 5 chữ số. Chữ số [A] có giá trị [va1] và [va2], chữ số [B] có giá trị [vb], chữ số [C] có giá trị [vc]. Vậy [Tên] đang nghĩ tới số nào?"
```
- Nhóm tất cả giá trị của cùng một chữ số vào một mệnh đề.
- Nếu chữ số chỉ xuất hiện một lần: "chữ số [X] có giá trị [v]" (không có "và").
- Liệt kê theo thứ tự giá trị cao nhất của mỗi chữ số giảm dần.
- Chữ số 0 không được liệt kê.

### Chiến lược chọn số
- Phải có **ít nhất một chữ số xuất hiện ở hai hàng khác nhau** — đây là điểm mấu chốt của dạng bài.
- Phổ biến nhất: chữ số X ở chục nghìn (X0000) và chục (X0), hoặc ở nghìn (X000) và đơn vị (X).
- Các pattern phổ biến:
  | Pattern | Ví dụ số | Mô tả |
  |---|---|---|
  | A ở chục nghìn + chục; B ở nghìn; C ở trăm; D ở đơn vị | 50654 | 5→50000+50, 6→600, 4→4 |
  | A ở chục nghìn + đơn vị; B ở nghìn + chục | 73037 | 7→70000+7, 3→3000+30 |
  | A ở chục nghìn + đơn vị; B ở nghìn + chục; C ở trăm | 41814 | 4→40000+4, 1→1000+10, 8→800 |
  | A ở chục nghìn + chục; B ở nghìn + đơn vị; C ở trăm | 32132 | 3→30000+30, 2→2000+2, 1→100 |
  | Một chữ số không lặp (không có đôi) | 64368 | 6→60000+60, 4→4000, 3→300, 8→8 |

### Chiến lược wrong_pool (5 phần tử — dùng đúng tập chữ số, chỉ đổi vị trí)
Mỗi wrong answer là một số dùng đúng **multiset chữ số** của đáp án nhưng sắp xếp sai. Bao gồm 5 bẫy nhận thức:

| Bẫy | Mô tả | Ví dụ (đúng: 50654) |
|---|---|---|
| Chữ số lặp ở hàng cao hơn so với đúng | 5 ở nghìn (5000) thay vì chục (50) | 55064 |
| Chữ số lặp ở hàng thấp hơn so với đúng | 5 ở trăm (500) thay vì chục (50) | 50564 |
| Chữ số đơn ở hàng sai | 6 ở nghìn (6000) thay vì trăm (600) | 56054 |
| Hoán vị hai chữ số cuối | đổi chỗ chục ↔ đơn vị | 50645 |
| Đặt chữ số đơn ở hàng cao nhất | 6 ở chục nghìn (60000) | 60554 |

**Quy tắc**: Mỗi wrong answer phải dùng **đúng multiset chữ số** của đáp án (cùng số lần xuất hiện của mỗi chữ số) và phải là số 5 chữ số hợp lệ (không bắt đầu bằng 0).

### Phân bố (10 câu, ID 21–30)
| Số | Chữ số lặp | Chữ số không lặp | Có số 0 ẩn? |
|---|---|---|---|
| 50654 | 5 (chục nghìn + chục) | 6, 4 | Có (nghìn) |
| 73037 | 7 (chục nghìn + đơn vị), 3 (nghìn + chục) | — | Có (trăm) |
| 41814 | 4 (chục nghìn + đơn vị), 1 (nghìn + chục) | 8 | Không |
| 32132 | 3 (chục nghìn + chục), 2 (nghìn + đơn vị) | 1 | Không |
| 28920 | 2 (chục nghìn + chục) | 8, 9 | Có (đơn vị) |
| 64368 | 6 (chục nghìn + chục) | 4, 3, 8 | Không |
| 85258 | 8 (chục nghìn + đơn vị), 5 (nghìn + chục) | 2 | Không |
| 91719 | 9 (chục nghìn + đơn vị), 1 (nghìn + chục) | 7 | Không |
| 46064 | 4 (chục nghìn + đơn vị), 6 (nghìn + chục) | — | Có (trăm) |
| 17571 | 1 (chục nghìn + đơn vị), 7 (nghìn + chục) | 5 | Không |

---
