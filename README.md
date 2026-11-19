# Bài tập lớn Nhập môn Trí tuệ Nhân tạo (`INT3401 10`) — Nhóm 3

**Đề tài:** Cài đặt các thuật toán tìm kiếm và tìm kiếm đối kháng cho Pac-Man ([UC Berkeley CS188](https://inst.eecs.berkeley.edu/~cs188/): Project 1 — Search & Project 2 — Multiagent Search).

* **Kho mã nguồn:** [https://github.com/Nguyeenxdqng/2627I_INT3401_10_Nhom3](https://github.com/Nguyeenxdqng/2627I_INT3401_10_Nhom3)
* **Môi trường phát triển:** Python 3.14.7 (tương thích Python 3.x, không yêu cầu thư viện bên thứ ba)

---

## 1. Thành viên & Phân công công việc

| Thành viên | Mã sinh viên | Đóng góp | Nhiệm vụ chính |
| :--- | :---: | :---: | :--- |
| **Trương Ngọc Anh** | `24022944` | 25% | Project 1: q1–q4 (DFS, BFS, UCS, A*), q8 (ClosestDot); testcase so sánh Minimax và Alpha-Beta |
| **Giáp Vũ Diệu Kỳ** | `24023008` | 25% | Project 1: q5 (`CornersProblem`), q6, q7 (heuristic); Project 2: q5 (`betterEvaluationFunction`) |
| **Nguyễn Mai Phương Thúy** | `24023072` | 25% | Project 2: q1 (`ReflexAgent`), q2 (`MinimaxAgent`), q3 (`AlphaBetaAgent`), q4 (`ExpectimaxAgent`) |
| **Nguyễn Hồng Đăng** | `24022956` | 25% | Thiết lập môi trường, repo Git, Autograder; script kiểm thử; Project 2: q5; tổng hợp báo cáo |

---

## 2. Cấu trúc kho mã nguồn

```text
2627I_INT3401_10_Nhom3/
├── project1/ (hoặc search/)       # CS188 Project 1: Search
│   ├── search.py                  # Cài đặt DFS, BFS, UCS, A* (q1–q4)
│   ├── searchAgents.py            # Cài đặt CornersProblem, Heuristics & ClosestDot (q5–q8)
│   ├── autograder.py              # Bộ chấm tự động Project 1
│   └── ...                        # Các tệp môi trường Pac-Man và layouts
├── project2/ (hoặc multiagent/)   # CS188 Project 2: Multiagent Search
│   ├── multiAgents.py             # Cài đặt Reflex, Minimax, Alpha-Beta, Expectimax & EvalFn (q1–q5)
│   ├── autograder.py              # Bộ chấm tự động Project 2
│   └── ...                        # Các tệp môi trường Pac-Man và layouts
├── logs/                          # Log kết quả chạy Autograder & thực nghiệm
└── report/                        # Mã nguồn LaTeX và tài liệu báo cáo của nhóm
```

*(Lưu ý: Chỉ các tệp `search.py`, `searchAgents.py` và `multiAgents.py` được chỉnh sửa theo đúng quy định của bộ bài tập CS188).*

---

## 3. Hướng dẫn cài đặt và chạy chương trình

### 3.1. Yêu cầu hệ thống
* **Python 3.x** (Nhóm thực nghiệm trên Python `3.14.7`, Windows 11).
* Gói giao diện `tkinter` (đi kèm mặc định với Python) nếu chạy ở chế độ hiển thị đồ họa.

Clone kho mã nguồn về máy:
```bash
git clone https://github.com/Nguyeenxdqng/2627I_INT3401_10_Nhom3.git
cd 2627I_INT3401_10_Nhom3
```

### 3.2. Project 1: Tìm kiếm (Search)

Di chuyển vào thư mục chứa mã nguồn Project 1 và chạy các lệnh sau:

* **Chạy Autograder toàn bộ Project 1:**
  ```bash
  python autograder.py
  ```
* **Chạy kiểm thử từng câu (`q1` đến `q8`):**
  ```bash
  python autograder.py -q q7
  ```
* **Chạy trực quan với Pac-Man:**
  ```bash
  # Tìm đường bằng A* với Manhattan heuristic (q4)
  python pacman.py -l mediumMaze -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic

  # Bài toán đi qua 4 góc bằng A* (q5, q6)
  python pacman.py -l mediumCorners -p AStarCornersAgent

  # Bài toán ăn hết thức ăn bằng A* với foodHeuristic (q7)
  python pacman.py -l trickySearch -p AStarFoodSearchAgent

  # Tìm thức ăn gần nhất bằng thuật toán tham lam BFS (q8)
  python pacman.py -l bigSearch -p ClosestDotSearchAgent -z .5
  ```

### 3.3. Project 2: Tìm kiếm đối kháng (Multiagent Search)

Di chuyển vào thư mục chứa mã nguồn Project 2 và chạy các lệnh sau:

* **Chạy Autograder toàn bộ Project 2:**
  ```bash
  python autograder.py
  ```
* **Chạy kiểm thử từng câu (`q1` đến `q5`):**
  ```bash
  python autograder.py -q q5
  ```
* **Chạy trực quan với Pac-Man:**
  ```bash
  # ReflexAgent trên openClassic (q1)
  python pacman.py -p ReflexAgent -l openClassic

  # MinimaxAgent độ sâu 3 (q2)
  python pacman.py -p MinimaxAgent -l minimaxClassic -a depth=3

  # AlphaBetaAgent độ sâu 3 (q3)
  python pacman.py -p AlphaBetaAgent -a depth=3 -l smallClassic

  # ExpectimaxAgent kết hợp betterEvaluationFunction, độ sâu 2 (q4, q5)
  python pacman.py -p ExpectimaxAgent -l smallClassic -a evalFn=better,depth=2
  ```

---

## 4. Tóm tắt kết quả thực nghiệm

### 4.1. Điểm Autograder (Chạy ngày 13/11/2026, `random.seed(0)`)

| Phần | q1 | q2 | q3 | q4 | q5 | q6 | q7 | q8 | Tổng điểm |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Project 1** | 3/3 | 3/3 | 3/3 | 3/3 | 3/3 | 3/3 | **5/4*** | 3/3 | **26/25** |
| **Project 2** | 4/4 | 5/5 | 5/5 | 5/5 | 6/6 | — | — | — | **25/25** |

*\*Ghi chú câu q7: `foodHeuristic` mở 4.137 nút trên `trickySearch`, vượt qua cả 4 ngưỡng mở rộng (15.000, 12.000, 9.000, 7.000) nên đạt điểm thưởng tối đa 5/4.*

### 4.2. Hiệu năng nổi bật
* **Giảm không gian tìm kiếm (Project 1):**
  * `cornersHeuristic` (q6) giảm **64,80%** số nút mở rộng trên `mediumCorners` (từ $1966 \to 692$ nút, đường đi tối ưu 106 bước).
  * `foodHeuristic` (q7) giảm **75,21%** số nút mở rộng trên `trickySearch` (từ $16688 \to 4137$ nút).
* **Hiệu quả cắt tỉa & tác tử đối kháng (Project 2):**
  * `AlphaBetaAgent` giữ nguyên hành động tối ưu của `MinimaxAgent` tại trạng thái gốc (độ sâu 3) và giảm **20,59%** số trạng thái sinh ra trên `minimaxClassic` ($607 \to 482$) và **61,23%** trên `smallClassic` ($423 \to 164$).
  * `ExpectimaxAgent` (độ sâu 2) kết hợp `betterEvaluationFunction` đạt tỉ lệ thắng **10/10 ván** trên `smallClassic` (2 `RandomGhost`, seed 0) với điểm trung bình **1405,9** và thời gian trung bình **6,92 giây/ván**.

---

## 5. Tài liệu tham khảo & Tuyên bố minh bạch

1. S. Russell & P. Norvig, *Artificial Intelligence: A Modern Approach*, 4th ed., Pearson, 2021.
2. UC Berkeley CS188: *Introduction to Artificial Intelligence* — Pac-Man Projects.
3. **Tuyên bố sử dụng AI:** Nhóm sử dụng công cụ AI hỗ trợ gỡ lỗi cài đặt và định dạng văn bản LaTeX/Markdown. Toàn bộ mã nguồn nộp bài đều được các thành viên trực tiếp đọc hiểu, kiểm thử qua Autograder và chịu trách nhiệm; mọi số liệu thực nghiệm đều trích xuất trung thực từ log chạy thực tế của nhóm.