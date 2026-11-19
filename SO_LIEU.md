# TỔNG HỢP SỐ LIỆU THỰC NGHIỆM — NHÓM 3

* **Môi trường:** Python 3.14.7 | Windows 11 Home | CPU 12th Gen Intel(R) Core(TM) i5-12450H
* **Nguồn dữ liệu:** Log Autograder (08:34 ngày 13/11/2026, `random.seed(0)`) và log thực nghiệm của nhóm.
* **Mã nguồn:** `https://github.com/Nguyeenxdqng/2627I_INT3401_10_Nhom3`

---

## 1. Điểm Autograder (13/11/2026)

| Phần | q1 | q2 | q3 | q4 | q5 | q6 | q7 | q8 | Tổng |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Project 1** *(Tối đa: 3,3,3,3,3,3,4,3)* | 3/3 | 3/3 | 3/3 | 3/3 | 3/3 | 3/3 | **5/4** | 3/3 | **26/25** |
| **Project 2** *(Tối đa: 4,5,5,5,6)* | 4/4 | 5/5 | 5/5 | 5/5 | 6/6 | — | — | — | **25/25** |

*Ghi chú q7:* Đạt cả 4 ngưỡng mở rộng nút (15000, 12000, 9000, 7000) nên nhận 5 điểm (vượt trần 4 điểm trong cấu hình).

---

## 2. Project 1: Thuật toán tìm kiếm cơ bản (q1–q4)

**Số nút mở rộng / Độ dài đường đi (bước, chi phí đơn vị 1):**

| Layout | DFS | BFS | UCS | A* (Manhattan) | Giảm nút (A* vs UCS) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `mediumMaze` | 146 / 130 | 269 / 68 | 269 / 68 | **221 / 68** | **17,8%** (48 nút) |
| `bigMaze` | 390 / 210 | 620 / 210 | 620 / 210 | **549 / 210** | **11,5%** (71 nút) |

**UCS với các hàm chi phí khác nhau trên `mediumMaze`:**

| Hàm chi phí | Số nút mở rộng | Độ dài đường đi (bước) |
| :--- | :---: | :---: |
| $1$ (mặc định) | 269 | 68 |
| $0{,}5^x$ (`StayEast`) | 260 | 74 |
| $2^x$ (`StayWest`) | 173 | 152 |

---

## 3. Project 1: Heuristic (q6, q7) & ClosestDot (q8)

| Bài toán (Layout) | Heuristic rỗng | Heuristic nhóm | Tỉ lệ giảm | Chi phí tối ưu |
| :--- | :---: | :---: | :---: | :---: |
| Corners (`mediumCorners` — q6) | 1966 | **692** | **64,80%** | 106 bước |
| Food (`trickySearch` — q7) | 16688 | **4137** | **75,21%** | Tối ưu |

* **Câu q8 (`ClosestDotSearchAgent`):** Đạt 13/13 test case; đường đi trên `bigSearch` dài **350 bước**.

---

## 4. Project 2: Kết quả từ Autograder (`grade-agent`, 1 `RandomGhost`, 10 ván)

| Test | Tác tử | Layout | Thắng | Điểm TB | Min | Max |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: |
| q1 | `ReflexAgent` | `openClassic` | 10/10 | 1225,3 | 1195 | 1251 |
| q5 | `ExpectimaxAgent` (`evalFn=better`, depth 2) | `smallClassic` | 10/10 | 1190,6 | 866 | 1346 |

---

## 5. Project 2: Thực nghiệm trên `smallClassic` (2 `RandomGhost`, 10 ván, seed 0)

| Tác tử | Số ván | Thắng | Điểm TB | Min | Max | Thời gian (s/ván) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `Reflex` | 10 | 9/10 | 1006,4 | $-336$ | 1551 | **0,80** |
| `Minimax` (depth 3) | 10 | 5/10 | 430,3 | $-397$ | 1287 | 90,97 |
| `Alpha-Beta` (depth 3) | 10 | 4/10 | 313,4 | $-319$ | 1133 | 93,52 |
| `Expectimax` (depth 3) | 10 | 4/10 | 140,7 | $-1180$ | 1455 | 331,78 |
| **`Expectimax + better` (depth 2)** | **10** | **10/10** | **1405,9** | **1147** | **1741** | **6,92** |

---

## 6. Project 2: Minimax vs Alpha-Beta tại trạng thái gốc (depth 3)

| Layout | Hành động (MM / AB) | Số trạng thái (MM $\to$ AB) | Giảm trạng thái | Thời gian (MM $\to$ AB) |
| :--- | :---: | :---: | :---: | :---: |
| `minimaxClassic` | `Stop` / `Stop` | 607 $\to$ 482 | **20,59%** | 0,0455s $\to$ 0,0318s |
| `smallClassic` | `West` / `West` | 423 $\to$ 164 | **61,23%** | 0,0350s $\to$ 0,0107s |

---

## 7. Project 2: Thực nghiệm trên `trappedClassic` (depth 3, 10 ván)

| Tác tử | Thắng | Điểm TB |
| :--- | :---: | :---: |
| `Alpha-Beta` | 0/10 | $-501,0$ |
| `Expectimax` | **5/10** | **15,0** |

---

## 8. Project 2: Các phiên bản hàm đánh giá (Expectimax, `smallClassic`, depth 3, cờ `-f`)

| Phiên bản | Thay đổi trọng số | Thắng (10 ván) | Điểm TB (10 ván) | Thắng (30 ván) | Điểm TB (30 ván) |
| :--- | :--- | :---: | :---: | :---: | :---: |
| Mặc định (Berkeley) | Không dùng `better` | 7/10 | 912,3 | — | — |
| **Gốc (= v1)** | **`wFood=4, wNear=10, wGhost=12`** | **10/10** | **1378,8** | **30/30** | **1404,6** |
| v2 | `wGhost` $12 \to 24$ | 9/10 | 1269,9 | — | — |
| v3 | `wNearestFood` $10 \to 20$ | 10/10 | 1523,4 | 27/30 | 1312,5 |
| v4 | `wFoodCount` $4 \to 8$ | 9/10 | 1145,7 | — | — |
| v5 | Thêm capsule ($w=10$) | 10/10 | 1391,9 | 26/30 | 1284,4 |

---

## 9. Số liệu đo vết hành động `Stop` (`Expectimax + better`, depth 2, 2 `RandomGhost`, seed `cs188`)

* **Kết quả 5 ván:** Thắng 4/5 — Điểm từng ván: `1677`, `1360`, `1274`, `16` (thua), `1689` (TB: `1203,2`).
* **Tần suất chọn `Stop` / Tổng số lượt:** `40/173`, `7/90`, `38/176`, `138/274` (50,36%), `60/161`.
* **Thời gian gọi `getAction` (trên 874 lượt):** Trung bình `10,96 ms` | Trung vị `8,66 ms` | Lớn nhất `56,51 ms`.

---

## 10. Công thức cài đặt chính

* **Heuristic q6 (`cornersHeuristic`):**
  $$h_{\mathrm{corners}}(s) = \sum_{j=1}^{k} D_M(c_{j-1}, c_j)$$

* **Heuristic q7 (`foodHeuristic`):**
  $$h_{\mathrm{food}}(p, F) = \max_{f \in F} D_{\mathrm{maze}}(p, f), \quad h_{\mathrm{food}} = 0 \text{ khi } F = \varnothing$$

* **Hàm đánh giá `ReflexAgent` (q1):**
  $$R(s, a) = S(s') + B_R + \sum_i H_i - 10\cdot\mathbf{1}[a=\mathrm{Stop},\, F'\neq\varnothing]$$

* **Hàm đánh giá `betterEvaluationFunction` (q5):**
  $$E(s) = S(s) - 4|F(s)| + B_F(s) + \sum_i G_i(s)$$
  $$B_F = \frac{10}{d_{\min}+1}\ (F \neq \varnothing), \quad G_i = \begin{cases} \dfrac{20}{d_i+1}, & t_i > 0,\ d_i < t_i \\ 0, & t_i > 0,\ d_i \ge t_i \\ -\dfrac{12}{d_i+1} - 200\cdot\mathbf{1}[d_i \le 1], & t_i = 0 \end{cases}$$