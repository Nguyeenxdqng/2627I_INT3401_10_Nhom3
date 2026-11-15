# DANH SÁCH CÔNG VIỆC CÒN LẠI VÀ CÁCH THỰC HIỆN

Nhóm 3 · Pac-Man AI (Project 1 + Project 2) · Lập ngày 13/11/2026 (thứ Sáu) · Hạn nộp 22/11/2026 (Chủ nhật)

Mỗi công việc có ba phần: **làm gì**, **làm thế nào** (các bước ngắn), **thu gì cho báo cáo** (bằng chứng cần ghi lại). Tick `[x]` khi xong. Các lệnh chạy từ thư mục tương ứng (`Project1/` hoặc `Project2/`).

> Tôi không biết hiện nhóm đã xong những câu nào, vì các file `search.py`, `searchAgents.py`, `multiAgents.py` trong bản tôi nhận được còn là khung gốc. Việc đầu tiên là chạy Autograder để biết trạng thái thật (mục A0).

---

## 1. Mốc thời gian đề xuất (9 ngày)

| Ngày | Mục tiêu | Người chịu trách nhiệm chính |
| --- | --- | --- |
| Thứ Sáu 13/11 – Thứ Bảy 14/11 | Hoàn tất mã P1 và P2, Autograder đạt tối đa; gộp `dev` vào `main` | TV1, TV2, TV3, TV4 (gộp) |
| Chủ nhật 15/11 – Thứ Ba 17/11 | Chạy thực nghiệm, điền `SO_LIEU.md` | TV1, TV3 (chạy), TV4 (tổng hợp) |
| Thứ Ba 17/11 – Thứ Năm 19/11 | Viết báo cáo LaTeX (giao `HUONG_DAN_AI_VIET_BAO_CAO.md` + `SO_LIEU.md` + mã cho AI, sau đó cả nhóm sửa) | TV4, cả nhóm |
| Thứ Năm 19/11 – Thứ Sáu 20/11 | Hoàn thiện README, GitHub, CoReach; rà soát PDF (≤ 7 trang) | TV4 |
| Thứ Bảy 21/11 | Đóng gói zip, nộp sớm một ngày; ôn vấn đáp | Nhóm trưởng |
| Chủ nhật 22/11 | Dự phòng, không thêm tính năng mới | |

---

## 2. Quy trình chung cho mọi câu mã

1. `git pull origin dev`, rồi tạo nhánh theo quy ước `feature/<tv>/<project>-<câu>-<tên>`.
2. Viết mã, chạy `python autograder.py -q qN --no-graphics` cho câu đó.
3. Chạy `python autograder.py --no-graphics` toàn bộ để chắc các câu cũ không bị giảm điểm.
4. Xóa `print` gỡ lỗi, tạo PR vào `dev` (tên PR: `[P1-Q1] DFS`), dán kết quả Autograder, nhờ người review chạy lại.
5. Chụp hoặc lưu đoạn log "PASS/FAIL" và "Question qN: x/y" để đưa vào phụ lục báo cáo.

---

## 3. PHẦN A: Hoàn thiện mã và kiểm chứng

### A0. Biết trạng thái thật (làm ngay, 15 phút)

- **Làm gì:** xác định câu nào đã đạt điểm tối đa.
- **Làm thế nào:**
  ```
  cd Project1 && python autograder.py --no-graphics > log_p1.txt
  cd ../Project2 && python autograder.py --no-graphics > log_p2.txt
  ```
  Mở hai file log, ghi điểm từng câu vào bảng ở mục B1. Câu nào chưa tối đa thì xếp vào danh sách A1–A13 dưới đây.
- **Thu gì:** `log_p1.txt`, `log_p2.txt` (lưu vào thư mục `bao_cao/logs/`).

### Project 1: Search (file `search.py`, `searchAgents.py`)

**Ý tưởng chung q1–q4.** Một vòng lặp duy nhất; chỉ đổi loại hàng đợi. Mỗi phần tử trong hàng đợi gồm (trạng thái, danh sách hành động đã đi, tổng chi phí).
Vòng lặp: lấy một phần tử ra → nếu trạng thái đã mở thì bỏ qua → nếu là đích thì trả về danh sách hành động → đánh dấu đã mở → với mỗi trạng thái kế tiếp chưa mở, đẩy vào hàng đợi (danh sách hành động mới là `actions + [action]`, không dùng `append`).

- [ ] **A1. q1 DFS (3 điểm).** Hàng đợi là `util.Stack()`. Kiểm tra: `python autograder.py -q q1`. Chạy thử: `python pacman.py -l mediumMaze -p SearchAgent -a fn=dfs`. Thu: chi phí đường đi và số nút mở rộng in ra trên terminal; nhận xét "không tối ưu" kèm test `graph_bfs_vs_dfs`.
- [ ] **A2. q2 BFS (3 điểm).** Hàng đợi là `util.Queue()`. Kiểm tra `-q q2`. Thu: số nút mở rộng trên `mediumMaze` và `bigMaze`.
- [ ] **A3. q3 UCS (3 điểm).** Hàng đợi là `util.PriorityQueue()`; độ ưu tiên là tổng chi phí $g$. Kiểm tra `-q q3`. Thử hàm chi phí: `python pacman.py -l mediumMaze -p StayEastSearchAgent` và `-p StayWestSearchAgent`. Thu: chi phí đường đi của UCS so với BFS khi có hàm chi phí khác nhau.
- [ ] **A4. q4 A\* (3 điểm).** Giống UCS nhưng độ ưu tiên là $g + h$, với $h$ là heuristic truyền vào. Kiểm tra `-q q4`. Chạy thử: `python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic`. Thu: số nút mở rộng so với UCS.
- [ ] **A5. q5 CornersProblem (3 điểm).**
  - Trạng thái = (vị trí, tuple bốn giá trị đúng/sai cho từng góc đã thăm). Dùng tuple (hoặc frozenset), không dùng list vì phải băm được.
  - `getStartState`: nếu ô xuất phát trùng một góc thì đánh dấu góc đó là đã thăm.
  - `isGoalState`: cả bốn góc đã thăm.
  - `getSuccessors`: với bốn hướng, nếu không có tường thì tạo trạng thái mới; nếu ô mới là góc thì cập nhật tuple góc; chi phí bước 1.
  - Kiểm tra `-q q5` (lời giải tối ưu `tinyCorner` dài 28). Chạy thử: `python pacman.py -l mediumCorners -p SearchAgent -a fn=bfs,prob=CornersProblem`.
  - Thu: khái niệm trạng thái, vì sao phải lưu góc đã thăm, kích thước không gian trạng thái $\le 16\cdot W\cdot H$.
- [ ] **A6. q6 cornersHeuristic (3 điểm).**
  - Phiên bản đơn giản: Manhattan lớn nhất từ vị trí hiện tại tới một góc chưa thăm.
  - Phiên bản mạnh hơn: với các góc chưa thăm, thử mọi thứ tự đi (tối đa 24), lấy tổng Manhattan nhỏ nhất của chuỗi vị trí → góc1 → góc2 …
  - Không có góc chưa thăm thì trả về 0.
  - Kiểm tra `-q q6`. Điểm tối đa cần ≤ 1200 nút mở trên `mediumCorners` (ba ngưỡng 2000, 1600, 1200).
  - Thu: công thức, lập luận chấp nhận được và nhất quán, số nút mở rộng so với `nullHeuristic` (mục B3).
- [ ] **A7. q7 foodHeuristic (4 điểm).**
  - Lấy danh sách thức ăn `foodGrid.asList()`; rỗng thì trả về 0.
  - $h$ = khoảng cách mê cung lớn nhất từ vị trí hiện tại tới một viên thức ăn, dùng `mazeDistance(position, food, problem.startingGameState)`.
  - Lưu kết quả vào `problem.heuristicInfo` theo khóa (position, food) để không chạy lại BFS.
  - Kiểm tra `-q q7`. Các ngưỡng nút mở trên `trickySearch`: 15000, 12000, 9000, 7000.
  - Muốn giảm số nút hơn nữa: lấy khoảng cách giữa hai viên xa nhau nhất cộng khoảng cách từ vị trí tới viên gần hơn trong hai viên đó (vẫn chấp nhận được).
  - Thu: lý do chọn max thay vì tổng, vì sao Manhattan yếu trên `trickySearch`, tác dụng của bộ nhớ đệm (so thời gian có và không có đệm nếu có điều kiện), số nút mở rộng.
- [ ] **A8. q8 ClosestDotSearchAgent (3 điểm).**
  - `AnyFoodSearchProblem.isGoalState(state)`: trả về `self.food[x][y]`.
  - `findPathToClosestDot(gameState)`: tạo `AnyFoodSearchProblem(gameState)` rồi `return search.bfs(problem)`.
  - Kiểm tra `-q q8`. Chạy thử: `python pacman.py -l bigSearch -p ClosestDotSearchAgent -z .5`.
  - Thu: chi phí đường đi trên `bigSearch`; nhận xét tham lam chưa chắc tối ưu toàn cục.

### Project 2: Multiagent (file `multiAgents.py`)

**Ý tưởng chung q2–q4.** Viết một hàm đệ quy nhận (trạng thái, chỉ số tác tử, độ sâu hiện tại) và trả về một con số. Tác tử kế tiếp là `(i + 1) % số tác tử`; độ sâu tăng thêm 1 khi tác tử kế tiếp là Pac-Man (chỉ số 0). Dừng và gọi `self.evaluationFunction(state)` khi thắng, thua hoặc `độ sâu == self.depth`. Hàm `getAction` ở gốc duyệt các hành động của Pac-Man, gọi hàm đệ quy cho từng hành động và trả về hành động có giá trị cao nhất (hòa thì giữ hành động đầu tiên).

- [ ] **A9. q1 ReflexAgent (4 điểm).** Sửa `evaluationFunction(currentGameState, action)`: lấy điểm của trạng thái kế tiếp, cộng thưởng nghịch đảo khoảng cách Manhattan tới thức ăn gần nhất, phạt nặng nếu có ma không sợ ở khoảng cách ≤ 1, phạt nhẹ hành động `Stop`. Kiểm tra `-q q1`; chạy thử `python pacman.py -p ReflexAgent -l testClassic`. Thu: các đặc trưng, trọng số, điểm Autograder (4 điểm: 10 ván, điểm TB ≥ 500 và ≥ 1000, thắng ≥ 5 và = 10).
- [ ] **A10. q2 MinimaxAgent (5 điểm).** Tầng Pac-Man lấy `max`, tầng ma lấy `min`. Phải kiểm tra trạng thái kết thúc trước khi duyệt hành động. Kiểm tra `-q q2`; chạy thử `python pacman.py -p MinimaxAgent -l minimaxClassic -a depth=4`. Thu: định nghĩa độ sâu (một lượt đủ mọi tác tử), hiện tượng Pac-Man lao vào ma khi chắc chắn bị bắt.
- [ ] **A11. q3 AlphaBetaAgent (5 điểm).** Thêm hai cận $\alpha, \beta$. Nút MAX: sau mỗi nhánh cập nhật $v$; nếu $v > \beta$ thì trả về ngay; rồi cập nhật $\alpha$. Nút MIN: nếu $v < \alpha$ thì trả về ngay; rồi cập nhật $\beta$. Ba lưu ý: dùng bất đẳng thức chặt (không cắt khi bằng); cập nhật $\alpha$ ngay tại gốc sau mỗi hành động của Pac-Man; không đổi thứ tự duyệt các con. Kiểm tra `-q q3`. Thu: điều kiện cắt, số nút sinh ra so với Minimax (mục B4).
- [ ] **A12. q4 ExpectimaxAgent (5 điểm).** Giống Minimax, nhưng tầng ma trả về trung bình cộng giá trị các nhánh (xác suất đều). Kiểm tra `-q q4`; chạy thử `python pacman.py -p ExpectimaxAgent -l trappedClassic -a depth=3 -q -n 10`. Thu: tỉ lệ thắng của Minimax/Alpha-Beta và Expectimax trên `trappedClassic` (mục B5).
- [ ] **A13. q5 betterEvaluationFunction (6 điểm).**
  - Hàm chỉ nhận `currentGameState` (không có `action`).
  - Gợi ý đặc trưng: điểm hiện tại, nghịch đảo khoảng cách tới thức ăn gần nhất, số thức ăn còn lại, số capsule còn lại, ma đang sợ (thưởng khi gần), ma không sợ (phạt khi rất gần).
  - Tránh gọi BFS hoặc `mazeDistance` ở đây: hàm được gọi ở mọi nút lá và tổng thời gian cả ván giới hạn 120 s.
  - Nên trả về giá trị hữu hạn cho trạng thái thắng/thua, vì trung bình giữa `+inf` và `-inf` ra `nan`.
  - Tinh chỉnh: sửa trọng số, chạy `python autograder.py -q q5 --no-graphics` và/hoặc script ở mục B5; ghi lại mỗi phiên bản v1, v2, … cùng tỉ lệ thắng và điểm TB.
  - Thu: công thức, ý nghĩa từng trọng số, bảng so sánh các phiên bản.

### Hoàn thiện kho mã

- [ ] **A14.** TV4 gộp `dev` vào `main` khi Autograder đạt điểm tối đa ở cả hai project; không `push` thẳng lên `main`.
- [ ] **A15.** Dọn `print` debug, file tạm; kiểm tra `.gitignore` có `__pycache__/` và `*.pyc`.
- [ ] **A16.** Không sửa `autograder.py`, `game.py`, `pacman.py`, `util.py`, `test_cases/`. Chạy `git diff main --stat` để xác nhận.

---

## 4. PHẦN B: Thực nghiệm và thu thập số liệu

Quy ước: ghi lại mọi lệnh đã chạy và seed; chạy trên cùng một máy cho các so sánh về thời gian. Tất cả điền vào file `SO_LIEU.md` (mẫu ở Phụ lục).

### B1. Điểm Autograder

- **Làm thế nào:** lấy từ phần "Provisional grades" ở cuối `log_p1.txt` và `log_p2.txt` (mục A0, chạy lại sau khi hoàn tất mã).
- **Thu:** bảng điểm từng câu; dán nguyên phần log "Provisional grades" vào phụ lục. Điền bảng `tab:grader`.

### B2. So sánh DFS, BFS, UCS, A\* (bảng `tab:p1`)

- **Lệnh** (chạy trong `Project1/`, thêm `-q` để tắt đồ họa):
  ```
  python pacman.py -l mediumMaze -p SearchAgent -a fn=dfs -q
  python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs -q
  python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs -q
  python pacman.py -l mediumMaze -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic -q
  ```
  Lặp lại với `-l bigMaze`.
- **Đọc kết quả:** terminal in `Path found with total cost of X in Y seconds` và `Search nodes expanded: N`. Ghi (N, X) cho mỗi ô của bảng.
- **Đối chiếu:** số nút của q1–q4 trên `mediumMaze` phải gần giá trị chuẩn trong `test_cases` (mục 5.4 của file hướng dẫn AI).

### B3. Hiệu quả heuristic (bảng `tab:heur`)

- **Corners:**
  ```
  python pacman.py -l mediumCorners -p SearchAgent -a fn=aStarSearch,prob=CornersProblem,heuristic=nullHeuristic -q
  python pacman.py -l mediumCorners -p AStarCornersAgent -q
  ```
- **Food:**
  ```
  python pacman.py -l trickySearch -p SearchAgent -a fn=aStarSearch,prob=FoodSearchProblem,heuristic=nullHeuristic -q
  python pacman.py -l trickySearch -p AStarFoodSearchAgent -q
  ```
- **Thu:** số nút mở rộng và chi phí đường đi; tính phần trăm giảm = (null − nhóm)/null × 100%. Chi phí đường đi của hai lần chạy phải bằng nhau (cùng tối ưu); nếu khác, heuristic có lỗi.
- **Ghi thêm (nếu có thời gian):** chạy `bfs` trên `mediumCorners` để làm mốc (chi phí tối ưu 106).

### B4. Minimax và Alpha-Beta: hành động, số trạng thái, thời gian (mục 6.3 của báo cáo)

Mục đích: chứng tỏ cùng hành động nhưng Alpha-Beta sinh ít trạng thái hơn.

- **Làm thế nào:** tạo file `Project2/tests/so_sanh_minimax_alphabeta.py` (TV1 phụ trách theo phân công). Chạy từ thư mục `Project2/`.
  ```python
  import os, sys, time
  sys.path.insert(0, os.getcwd())
  import layout, pacman, multiAgents
  from pacman import GameState

  def do(tac_tu, ten_layout, so_ma):
      lay = layout.getLayout(ten_layout)
      s = GameState(); s.initialize(lay, so_ma)
      GameState.getAndResetExplored()
      t0 = time.time()
      hanh_dong = tac_tu.getAction(s)
      dt = time.time() - t0
      so_trang_thai = len(GameState.getAndResetExplored())
      return hanh_dong, so_trang_thai, dt

  for ten_layout, so_ma in [("minimaxClassic", 3), ("smallClassic", 2)]:
      for depth in ("2", "3"):
          for ten, lop in [("Minimax", multiAgents.MinimaxAgent),
                           ("AlphaBeta", multiAgents.AlphaBetaAgent)]:
              print(ten_layout, "depth", depth, ten, do(lop(depth=depth), ten_layout, so_ma))
  ```
  Giá trị tham số: `minimaxClassic` có 3 ma và `smallClassic` có 2 ma (đếm ký tự `G` trong file layout); `getAndResetExplored` đếm số trạng thái được tạo ra, là cách bộ chấm đếm.
- **Thu:** hành động hai tác tử trả về (phải giống nhau), số trạng thái sinh ra, thời gian; phần trăm giảm của Alpha-Beta. Điền bảng mục 6.3 của `SO_LIEU.md`.

### B5. Tỉ lệ thắng và điểm trung bình trên `smallClassic` (bảng `tab:p2`)

- **Làm thế nào:** tạo `Project2/tests/chay_thuc_nghiem.py` (chỉ dùng thư viện chuẩn), chạy từ `Project2/`:
  ```python
  import os, sys, time, random
  sys.path.insert(0, os.getcwd())
  import layout, pacman, textDisplay, multiAgents
  from ghostAgents import RandomGhost, DirectionalGhost

  def chay(ten, tac_tu, ten_layout, so_van, ghosts, seed=0):
      random.seed(seed)
      lay = layout.getLayout(ten_layout)
      t0 = time.time()
      games = pacman.runGames(lay, tac_tu, ghosts, textDisplay.NullGraphics(),
                              so_van, False, catchExceptions=True, timeout=120)
      dt = time.time() - t0
      diem = [g.state.getScore() for g in games]
      thang = sum(1 for g in games if g.state.isWin())
      print("%s | %s | thang %d/%d | diem TB %.1f | min %.0f | max %.0f | %.1f s/van" % (
          ten, ten_layout, thang, len(games), sum(diem)/len(diem), min(diem), max(diem), dt/len(games)))

  ma = lambda: [RandomGhost(i + 1) for i in range(2)]
  chay("Reflex", multiAgents.ReflexAgent(), "smallClassic", 50, ma())
  chay("Minimax d3", multiAgents.MinimaxAgent(depth="3"), "smallClassic", 10, ma())
  chay("AlphaBeta d3", multiAgents.AlphaBetaAgent(depth="3"), "smallClassic", 10, ma())
  chay("Expectimax d3", multiAgents.ExpectimaxAgent(depth="3"), "smallClassic", 10, ma())
  chay("Expectimax better d2", multiAgents.ExpectimaxAgent(evalFn="better", depth="2"), "smallClassic", 50, ma())
  ```
- **Cỡ mẫu:** giảng viên khuyến nghị 50 hoặc 100 ván. Minimax và Alpha-Beta độ sâu 3 chạy lâu; đo thời gian với `so_van = 2` trước rồi suy ra cỡ mẫu phù hợp (10 ván là mức tối thiểu để có số liệu); ghi rõ cỡ mẫu từng hàng trong bảng.
- **Thu:** tỉ lệ thắng, điểm trung bình, điểm cao nhất/thấp nhất, thời gian mỗi ván, seed. Chạy thêm `trappedClassic` (Minimax/Alpha-Beta so với Expectimax, độ sâu 3, 10 ván) để minh họa khác biệt về giả định ma.
- **Kiểm tra chéo bằng dòng lệnh:** `python pacman.py -p ExpectimaxAgent -a evalFn=better -l smallClassic -n 50 -q` (in `Win Rate` và `Average Score`).

### B6. Các phiên bản hàm đánh giá (bảng ở mục 6.4)

- **Làm thế nào:** mỗi lần đổi đặc trưng hoặc trọng số, lưu lại phiên bản (commit hoặc đoạn mã ngắn), chạy B5 cho `ExpectimaxAgent(evalFn="better")` với cùng seed và cỡ mẫu.
- **Thu:** bảng (phiên bản, đặc trưng, tỉ lệ thắng, điểm TB); lý do giữ hoặc bỏ từng thay đổi.

### B7. Phân tích định tính (cho phần Thảo luận)

- **Làm thế nào:** chạy có đồ họa vài ván (`python pacman.py -p ExpectimaxAgent -a evalFn=better -l smallClassic`), quan sát các tình huống thua.
- **Thu:** 2–3 tình huống cụ thể (ví dụ Pac-Man dừng lại gần ma, mắc kẹt ở góc, bỏ lỡ thức ăn xa) và nguyên nhân gắn với đặc trưng của hàm đánh giá; đây là nội dung cho phần "Thảo luận" mà giảng viên yêu cầu.

---

## 5. PHẦN C: Viết báo cáo LaTeX

- [ ] **C1. Chuẩn bị đầu vào cho AI.** Gồm: `HUONG_DAN_AI_VIET_BAO_CAO.md`, `Nhom3.tex`, mã bản cuối (`search.py`, `searchAgents.py`, `multiAgents.py`), `SO_LIEU.md` đã điền, log Autograder. Thiếu mục nào, AI sẽ để lại `\todo` thay vì bịa.
- [ ] **C2. Câu lệnh gợi ý giao cho AI:**
  > Đọc `HUONG_DAN_AI_VIET_BAO_CAO.md`, sau đó đọc `Nhom3.tex`, mã nguồn và `SO_LIEU.md`. Điền tất cả `\todo` theo bảng ánh xạ ở mục 7 của file hướng dẫn, tuân thủ văn phong ở mục 8 và giới hạn 7 trang. Không được dùng số liệu ngoài `SO_LIEU.md`. Cuối câu trả lời liệt kê các `\todo` còn lại và thông tin còn thiếu.
- [ ] **C3. Chèn biểu đồ.** Dùng `pgfplots` hoặc xuất hình từ Excel. Hai biểu đồ gợi ý: (i) cột so sánh số nút mở rộng của DFS/BFS/UCS/A\*; (ii) cột tỉ lệ thắng và điểm TB của các tác tử.
- [ ] **C4. Biên dịch trên Overleaf** với mẫu `IEEE-conference-template-062824`. Kiểm tra: không lỗi `\url`, không còn `[]` rỗng trong bảng, tổng ≤ 7 trang.
- [ ] **C5. Mỗi thành viên rà soát phần mình** (TV1: mục tìm kiếm q1–q4, q8; TV2: q5–q7 và hàm đánh giá; TV3: Reflex, Minimax, Alpha-Beta, Expectimax; TV4: tổng thể và thực nghiệm). Đối chiếu mọi công thức với mã.
- [ ] **C6. Rà soát văn phong** theo mục 8 của file hướng dẫn AI: không có "nhìn chung", "có thể thấy rằng", phó từ cảm xúc; mỗi nhận xét có số liệu hoặc lập luận.
- [ ] **C7. Điền MSSV TV1–TV3, tỉ lệ đóng góp, URL GitHub** trong tác giả, Tóm tắt, bảng phân công.
- [ ] **C8. Kiểm tra tài liệu tham khảo:** ít nhất 5 mục, định dạng IEEE, mỗi mục có `\cite` trong văn bản (hiện có b1–b6).

---

## 6. PHẦN D: Kho mã và nộp bài

- [ ] **D1. README.md** (hiện chỉ có tiêu đề). Nội dung tối thiểu: giới thiệu dự án; thành viên; yêu cầu (Python phiên bản nào, không cài thêm thư viện); cấu trúc thư mục; lệnh chạy Autograder; lệnh chạy lại từng thực nghiệm trong báo cáo (copy từ phần B); ghi chú nguồn UC Berkeley CS188.
- [ ] **D2. GitHub công khai.** Kiểm tra bằng cách mở repo trong cửa sổ ẩn danh; nhánh `main` chứa bản cuối.
- [ ] **D3. Giữ thông báo giấy phép** ở đầu mỗi file gốc và ghi nguồn CS188 trong README và báo cáo (thông báo gốc yêu cầu giữ ghi nguồn và không phân phối lời giải; nếu lo ngại về việc công khai, hỏi giảng viên trước, vì yêu cầu nộp bài là repo công khai).
- [ ] **D4. CoReach.** Nhóm trưởng tạo Reach `2627I_INT3401_10_Nhom 3`, thêm duyld@vnu.edu.vn với vai trò Supervisor; cập nhật tiến độ và phân công tác vụ.
- [ ] **D5. Đóng gói** `INT3401_10_Nhom3.zip` gồm: báo cáo PDF, thư mục `Project1/`, `Project2/` (kèm `tests/`), `README.md`, tài liệu bổ sung (bảng phân công, quy ước Git); không kèm dữ liệu, không kèm `__pycache__`.
- [ ] **D6. Nộp:** chỉ nhóm trưởng nộp, đúng một lần, đúng tên file. Giữ lại ảnh xác nhận.

---

## 7. PHẦN E: Chuẩn bị vấn đáp (tuần cuối)

Giảng viên có thể hỏi bất kỳ thành viên về bất kỳ câu nào. Mỗi người tự kiểm tra khả năng giải thích (không nhìn màn hình, 3 phút mỗi chủ đề):

- [ ] Khung tìm kiếm đồ thị: vì sao cần tập `closed`, vì sao kiểm tra đích khi lấy ra, vì sao dùng `actions + [action]`.
- [ ] Khác biệt DFS/BFS/UCS/A\*, A\* với `nullHeuristic`, chấp nhận được và nhất quán.
- [ ] Trạng thái của `CornersProblem`; chứng minh heuristic q6 và q7.
- [ ] Cách tính độ sâu trong Minimax; điều kiện cắt tỉa của Alpha-Beta và lý do dùng bất đẳng thức chặt; Expectimax khác Minimax ở đâu.
- [ ] Từng đặc trưng và dấu của trọng số trong `betterEvaluationFunction`.

Hỏi chéo nhau theo bộ 20 câu trong tài liệu ôn vấn đáp, đồng thời thử sửa một dòng mã và dự đoán kết quả Autograder.

---

## 8. Ghi lại môi trường thực nghiệm (điền vào mục 3.1 của báo cáo)

| Hạng mục | Cách lấy | Giá trị |
| --- | --- | --- |
| Phiên bản Python | `python --version` | |
| Hệ điều hành | Cài đặt hệ thống | |
| CPU, RAM | Cài đặt hệ thống | |
| Seed | `random.seed(0)` trong script B5 | |
| Layout | `mediumMaze`, `bigMaze`, `mediumCorners`, `trickySearch`, `bigSearch`, `minimaxClassic`, `smallClassic`, `trappedClassic`, `openClassic`, `testClassic` | |
| Số ván mỗi cấu hình | Theo B5 | |
| Mô hình ma | `RandomGhost` (Expectimax, Reflex), `DirectionalGhost` (test `8-pacman-game`) | |
| Tiêu chí đo | số nút mở rộng, chi phí đường đi, số trạng thái sinh ra, tỉ lệ thắng, điểm TB, thời gian | |

---

## Phụ lục: Mẫu file `SO_LIEU.md` (nhóm điền, rồi đưa cho AI)

```markdown
# SO_LIEU (nhóm 3)
Ngày chạy: __ | Python: __ | Hệ điều hành: __ | CPU: __ | Seed: 0

## Autograder (từ log)
| Project | q1 | q2 | q3 | q4 | q5 | q6 | q7 | q8 | Tổng /25 |
| P1 | | | | | | | | | |
| P2 | | | | | | | | n/a | |

## Bảng tab:p1 (nút mở rộng / chi phí đường đi)
| Layout | DFS | BFS | UCS | A* Manhattan |
| mediumMaze | | | | |
| bigMaze | | | | |

## Bảng tab:heur (nút mở rộng, chi phí đường đi)
| Bài toán | Heuristic rỗng | Heuristic của nhóm | % giảm |
| mediumCorners | | | |
| trickySearch | | | |

## Minimax và Alpha-Beta (cùng hành động? số trạng thái sinh ra, thời gian)
| Layout, depth | Hành động Minimax | Hành động Alpha-Beta | TT Minimax | TT Alpha-Beta | s Minimax | s Alpha-Beta |
| minimaxClassic, 3 | | | | | | |
| smallClassic, 3 | | | | | | |

## Bảng tab:p2 (smallClassic, mô hình ma: __)
| Tác tử | n ván | Thắng | Điểm TB | Min | Max | s/ván |
| Reflex | | | | | | |
| Minimax d3 | | | | | | |
| Alpha-Beta d3 | | | | | | |
| Expectimax d3 | | | | | | |
| Expectimax + better d2 | | | | | | |

## trappedClassic (độ sâu 3, n=10)
| Tác tử | Thắng | Điểm TB |
| Alpha-Beta | | |
| Expectimax | | |

## Các phiên bản hàm đánh giá
| Phiên bản | Đặc trưng/trọng số | Thắng | Điểm TB |
| v1 | | | |
| Bản cuối | | | |

## Công thức hàm đánh giá cuối (dán từ mã)
## Công thức heuristic q6 và q7 (dán từ mã)
## Tình huống thất bại quan sát được (B7)
```
