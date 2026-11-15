# HƯỚNG DẪN CHO AI: ĐỌC HIỂU DỰ ÁN PAC-MAN AI (NHÓM 3) VÀ VIẾT BÁO CÁO

> Đối tượng đọc: một mô hình AI được giao viết, hoàn thiện hoặc rà soát báo cáo LaTeX của dự án.
> Ngôn ngữ đầu ra: tiếng Việt học thuật. Định dạng đầu ra: LaTeX theo mẫu `IEEEtran` (conference), tối đa 7 trang.
> Ngày lập: 13/11/2026. Hạn nộp: 22/11/2026.

---

## 0. Vai trò, đầu ra và nguyên tắc bắt buộc

**Nhiệm vụ.** Điền toàn bộ các vị trí `\todo{...}` trong file `Nhom3.tex` bằng nội dung học thuật hoàn chỉnh, dựa trên (a) mã nguồn thực tế của nhóm, (b) kết quả Autograder và thực nghiệm do nhóm cung cấp, (c) các sự kiện về môi trường nêu trong file này.

**Nguyên tắc bắt buộc (xếp theo mức ưu tiên):**

1. **Không bịa số liệu.** Mọi con số về số nút mở rộng, chi phí đường đi, tỉ lệ thắng, điểm trung bình, thời gian, điểm Autograder chỉ được lấy từ file `SO_LIEU.md` (hoặc log mà người dùng dán). Nếu chưa có số liệu, để nguyên `\todo{cần số liệu: ...}` và liệt kê ở cuối câu trả lời. Các "giá trị tham chiếu" ở mục 5.4 và 6.4 là giá trị lấy từ file `.solution` của bộ chấm, chỉ dùng để đối chiếu, không dùng thay cho số đo của nhóm.
2. **Mô tả đúng mã thực tế.** Trước khi viết mục phương pháp cho một câu, đọc hàm tương ứng trong `search.py`, `searchAgents.py`, `multiAgents.py` của nhóm. Công thức, trọng số, tên đặc trưng trong báo cáo phải trùng với mã. Khi mã và tài liệu ôn tập (mục 10) khác nhau, mã là nguồn đúng.
3. **Giữ nguyên ràng buộc hình thức:** tối đa 7 trang, tiếng Việt, tối thiểu 5 tài liệu tham khảo định dạng IEEE, đường dẫn GitHub nằm trong phần Tóm tắt, bảng phân công có đủ Họ tên, MSSV, vai trò, công việc, % hoàn thành.
4. **Không tự thêm thư viện LaTeX nặng.** Biểu đồ vẽ bằng `pgfplots` hoặc chèn ảnh; mã nguồn dự án chỉ dùng thư viện chuẩn Python.
5. **Báo cáo thiếu thông tin thì hỏi, không đoán.** Các mục chưa rõ được liệt kê ở mục 9.

**Quy trình đề nghị:** đọc mục 1 đến 6 → đọc `Nhom3.tex` → đọc mã nguồn và `SO_LIEU.md` → viết từng mục theo mục 7 → tự rà soát bằng danh sách ở mục 11.

---

## 1. Thông tin dự án và yêu cầu hành chính

| Mục | Nội dung |
| --- | --- |
| Môn học | Trí tuệ nhân tạo, INT3401 (lớp 2627I_INT3401_10) |
| Đề bài | Bộ bài tập Pac-Man của UC Berkeley CS188: Project 1 (Search) và Project 2 (Multiagent Search). Project 0 (môi trường, Autograder) chỉ nhắc ngắn |
| Nhóm | Nhóm 3. Nhóm trưởng: Nguyễn Hồng Đăng (MSSV 24022956) |
| Thành viên | TV1 Trường Ngọc Anh (Lead Search); TV2 Giáp Vũ Diệu Kỳ (Lead Heuristic); TV3 Nguyễn Mai Phương Thúy (Lead Multiagent); TV4 Nguyễn Hồng Đăng (Lead Integration & Testing). MSSV của TV1 đến TV3 chưa có trong tài liệu |
| Kho mã | GitHub công khai, README.md đầy đủ. Tên repo trong hồ sơ: `2627I_INT3401_10_Nhom3`. URL đầy đủ phải đặt trong Tóm tắt |
| Bài nộp | 01 file `INT3401_10_Nhom3.zip` do nhóm trưởng nộp: báo cáo PDF, toàn bộ mã nguồn, tài liệu bổ sung (không kèm dữ liệu) |
| CoReach | Tạo Reach `2627I_INT3401_10_Nhom 3`, thêm giảng viên (duyld@vnu.edu.vn) vai trò Supervisor |
| Báo cáo | LaTeX, mẫu IEEE conference, tiếng Việt, tối đa 7 trang, tối thiểu 5 tài liệu tham khảo IEEE |
| Hạn nộp | 22/11/2026 |

**Phân công thực tế theo tài liệu nhóm:**

| TV | Project 1 | Project 2 | Khác |
| --- | --- | --- | --- |
| TV1 | q1 DFS, q2 BFS, q3 UCS, q4 A\*, q8 ClosestDot | Testcase so sánh Minimax và Alpha-Beta | Hỗ trợ kiểm tra heuristic |
| TV2 | q5 CornersProblem, q6 cornersHeuristic, q7 foodHeuristic | q5 betterEvaluationFunction (cặp với TV4) | |
| TV3 | | q1 Reflex, q2 Minimax, q3 Alpha-Beta, q4 Expectimax | Chạy nhiều ván so sánh hàm đánh giá |
| TV4 | | q5 betterEvaluationFunction (cặp với TV2) | Project 0, repo, `run_all.sh`, review PR, tổng hợp báo cáo |

Tỉ lệ đóng góp ghi trong `Nhom3.tex` hiện là 25% mỗi người; xác nhận lại với nhóm trước khi nộp.

---

## 2. Trạng thái tài nguyên và giới hạn của AI

- Các file `search.py`, `searchAgents.py`, `multiAgents.py` trong bản AI nhận được **vẫn là khung gốc** (còn `util.raiseNotDefined()`). Mã đã cài của nhóm nằm trên các nhánh/PR và phải được người dùng cung cấp. Do đó AI **chưa có** số liệu, chưa biết heuristic và hàm đánh giá cuối cùng của nhóm.
- Các tài liệu có sẵn: hai file phân công và quy ước Git, `Khung báo cáo` (đề cương nội bộ), `Nhom3.tex` (khung LaTeX có `\todo`), tài liệu ôn vấn đáp (PDF), hướng dẫn báo cáo của giảng viên, bộ `test_cases` và `layouts` của hai project.
- Tài liệu ôn vấn đáp chứa mã mẫu và một số con số minh họa. Chúng là tài liệu học tập, không phải kết quả đo của nhóm; xem mục 10 để biết những chỗ cần thận trọng.

---

## 3. Cấu trúc kho mã

```
2627I_INT3401_10_Nhom3/
├── README.md                 (hiện chỉ có tiêu đề, cần bổ sung)
├── .gitignore                (__pycache__/, *.pyc)
├── Project1/   search.py, searchAgents.py, util.py, game.py, pacman.py,
│               autograder.py, searchTestClasses.py, layouts/, test_cases/q1..q8
└── Project2/   multiAgents.py, util.py, game.py, pacman.py, ghostAgents.py,
                autograder.py, multiagentTestClasses.py, layouts/, test_cases/q1..q5 (+extra)
```

Chỉ được sửa: `search.py`, `searchAgents.py` (Project 1) và `multiAgents.py` (Project 2). Các file còn lại, gồm `test_cases/`, thuộc môi trường và bộ chấm.

---

## 4. Môi trường Pac-Man (sự kiện đã kiểm chứng từ mã nguồn)

- **Tọa độ:** gốc (0,0) ở góc dưới trái; x tăng sang phải, y tăng lên trên; North = (0,+1). File layout `.lay` được đọc từ trên xuống nên dòng đầu là hàng có y lớn nhất. Ký hiệu: `%` tường, `.` thức ăn, `o` capsule, `P` Pac-Man, `G` ma.
- **Tác tử:** `agentIndex = 0` là Pac-Man; 1, 2, … là các ma. Pac-Man có thể đứng yên (`Stop`). Ma không được `Stop` và không được quay đầu trừ khi cụt đường.
- **Điểm số:** ăn thức ăn +10; mỗi bước của Pac-Man −1; ăn hết thức ăn (thắng) +500; bị ma bắt (thua) −500; ăn ma đang sợ +200.
- **Hằng số:** `SCARED_TIME = 40` bước; `COLLISION_TOLERANCE = 0.7`; `TIME_PENALTY = 1`. Ma đang sợ di chuyển với tốc độ 0,5.
- **Mô hình ma có sẵn:** `RandomGhost` chọn đều ngẫu nhiên trong các hành động hợp lệ; `DirectionalGhost` tiến về Pac-Man với xác suất 0,8 (chạy xa khi đang sợ với xác suất 0,8), phần còn lại phân bố đều.
- **Luồng chạy khác nhau giữa hai project:** Project 1: toàn bộ đường đi được tính một lần trong `registerInitialState`, sau đó `getAction` trả lần lượt từng hành động. Project 2: mỗi lượt `getAction` dựng lại cây trò chơi từ trạng thái hiện tại vì ma di chuyển.
- **Giới hạn thời gian khi chấm:** trong Project 2 q5, tham số `maxTime = 120` được truyền làm `timeout`; tổng thời gian tính toán của tác tử trong một ván không được vượt 120 giây. Hàm đánh giá phải đủ nhanh (độ sâu mặc định của tác tử là 2).

---

## 5. Project 1: Tìm kiếm

### 5.1 Hình thức hóa (dùng cho mục Giới thiệu)

Mỗi bài toán là một `SearchProblem` với ba phương thức `getStartState`, `isGoalState`, `getSuccessors` (trả về bộ ba `(trạng thái kế tiếp, hành động, chi phí bước)`). Thuật toán trong `search.py` không chứa thông tin riêng của Pac-Man.

| Bài toán | Không gian trạng thái | Hành động | Đích | Chi phí |
| --- | --- | --- | --- | --- |
| `PositionSearchProblem` (q1–q4) | Vị trí $(x,y)$ không phải tường | N, S, E, W | Tới ô đích | 1 hoặc `costFn` |
| `CornersProblem` (q5) | (vị trí, tập 4 góc đã thăm); tối đa $W\cdot H\cdot 2^4$ trạng thái | N, S, E, W | Đã thăm đủ 4 góc | 1 |
| `FoodSearchProblem` (q7) | (vị trí, lưới thức ăn); tối đa $W\cdot H\cdot 2^{N}$ | N, S, E, W | Hết thức ăn | 1 |
| `AnyFoodSearchProblem` (q8) | Vị trí $(x,y)$ | N, S, E, W | Ô có thức ăn bất kỳ | 1 |

Trạng thái phải băm được (tuple hoặc frozenset) vì được đưa vào tập `closed`. Trạng thái của `CornersProblem` cần ghi nhớ góc đã thăm; nếu chỉ lưu vị trí thì tập `closed` sẽ chặn việc quay lại một ngã tư cũ để đi tới góc còn lại.

### 5.2 Khung tìm kiếm đồ thị chung cho q1–q4

Cả bốn thuật toán dùng cùng một khung; điểm khác duy nhất là cấu trúc dữ liệu của biên (fringe) và độ ưu tiên.

```
fringe.push((start, [], 0))        ; closed = {}
while fringe không rỗng:
    (s, actions, g) = fringe.pop()
    if s in closed: continue
    if isGoalState(s): return actions        # kiểm tra đích khi lấy ra
    closed.add(s)                            # đánh dấu trước khi mở
    for (s', a, c) in getSuccessors(s):
        if s' not in closed: fringe.push((s', actions + [a], g + c))
```

| Thuật toán | Biên (`util.py`) | Tiêu chí lấy ra | Tối ưu? |
| --- | --- | --- | --- |
| DFS (q1) | `Stack` (LIFO) | Nút mới đẩy vào gần nhất | Không |
| BFS (q2) | `Queue` (FIFO) | Nút đẩy vào sớm nhất | Có, khi mọi bước có cùng chi phí dương |
| UCS (q3) | `PriorityQueue`, độ ưu tiên $g(n)$ | Chi phí tích lũy nhỏ nhất | Có |
| A\* (q4) | `PriorityQueue`, độ ưu tiên $f(n)=g(n)+h(n)$ | $f$ nhỏ nhất | Có, nếu $h$ nhất quán (tìm kiếm đồ thị) |

Điểm lập luận cần nêu trong báo cáo: (i) kiểm tra đích khi lấy nút ra khỏi biên, không phải khi đẩy vào, vì với UCS/A\* đường nhìn thấy đích đầu tiên có thể đắt hơn (test `ucs_5_goalAtDequeue`: cạnh A→G chi phí 10, đường vòng A→B→C→G chi phí 3); (ii) tập `closed` ngăn lặp vô hạn trên đồ thị có chu trình (test `graph_infinite`) và ngăn mở một trạng thái hai lần (bộ chấm đếm số lần gọi `getSuccessors`); (iii) tạo danh sách hành động mới bằng `actions + [a]` để các nhánh con không dùng chung một danh sách; (iv) với `nullHeuristic` A\* suy biến thành UCS.

Định nghĩa heuristic (dùng cho mục q4, q6, q7):

$$ f(n)=g(n)+h(n) $$
$$ \text{Chấp nhận được: } 0\le h(n)\le h^{*}(n) \qquad \text{Nhất quán: } h(n)\le c(n,a,n')+h(n') $$

Heuristic nhất quán và $h(\text{đích})=0$ thì chấp nhận được; chiều ngược lại không đúng.

### 5.3 Từng câu và cách bộ chấm kiểm tra

| Câu | Nội dung | Điểm tối đa (CONFIG) | Bộ chấm kiểm tra |
| --- | --- | --- | --- |
| q1 | DFS | 3 | Đồ thị mẫu (backtrack, bfs_vs_dfs, infinite, manypaths) và `mediumMaze`; đúng đường đi và đúng thứ tự mở nút |
| q2 | BFS | 3 | Cùng nhóm test như q1 |
| q3 | UCS | 3 | `ucs_0..5`; hai hàm chi phí `0.5**x` (StayEast) và `2**x` (StayWest) trên `mediumMaze`; số nút mở trong ngưỡng 1,1 lần giá trị chuẩn |
| q4 | A\* | 3 | `astar_0..3`; `mediumMaze` với `manhattanHeuristic` (221 nút, hệ số 1,1) |
| q5 | CornersProblem | 3 | `tinyCorner`: lời giải tối ưu dài 28 bước, phải thăm đủ 4 góc |
| q6 | Heuristic cho Corners | 3 | `corner_sanity_1..3` (không âm, không tầm thường, chấp nhận được, nhất quán, bằng 0 tại đích); `medium_corners`: chi phí tối ưu 106, ngưỡng số nút mở 2000, 1600, 1200 (mỗi ngưỡng đạt được 1 điểm) |
| q7 | foodHeuristic | 4 | `food_heuristic_1..17` (chấp nhận được, nhất quán); `trickySearch`: 1 điểm cơ bản + 1 điểm cho mỗi ngưỡng 15000, 12000, 9000, 7000 nút mở |
| q8 | ClosestDotSearchAgent, AnyFoodSearchProblem | 3 | `closest_dot_1..13`: độ dài đường tới viên thức ăn gần nhất |

Tổng Project 1 là 25 điểm. Nếu Autograder in điểm khác bảng này (ví dụ q7), lấy theo Autograder (xem mục 10).

### 5.4 Giá trị tham chiếu từ file `.solution` (chỉ để đối chiếu)

| Test | Số nút mở trong file chuẩn |
| --- | --- |
| `mediumMaze`, DFS (q1) | 146 (thứ tự đảo: 269) |
| `mediumMaze`, BFS (q2) | 269 |
| `mediumMaze`, UCS chi phí 1 (q3) | 269 |
| `mediumMaze`, UCS `2**x` (StayWest) | 173 |
| `mediumMaze`, UCS `0.5**x` (StayEast) | 260 |
| `mediumMaze`, A\* + Manhattan (q4) | 221 |
| `mediumCorners`, chi phí tối ưu (q6) | 106 |

### 5.5 Ý chính cho từng thuật toán (để viết mục Phương pháp)

- **q5.** Trạng thái là cặp (vị trí, tuple/frozenset các góc đã thăm). Nếu vị trí xuất phát trùng một góc thì góc đó được đánh dấu đã thăm ngay từ đầu. Hàm kế tiếp cập nhật tập góc khi bước vào một góc; đích là đủ cả bốn góc. Tường là dữ liệu tĩnh nên không đưa vào trạng thái.
- **q6.** Heuristic dựa trên khoảng cách Manhattan, bỏ qua tường nên không vượt chi phí thực. Hai mức: khoảng cách Manhattan lớn nhất tới một góc chưa thăm; hoặc tổng Manhattan nhỏ nhất theo mọi thứ tự duyệt các góc còn lại (tối đa 4! = 24 hoán vị). Báo cáo cần có lập luận chứng minh chấp nhận được (mỗi chặng đi thực ≥ Manhattan của chặng đó, lấy min trên mọi thứ tự) và nhất quán (một bước đi làm thay đổi khoảng cách tới điểm đầu của chặng tối đa 1).
- **q7.** Heuristic lấy khoảng cách mê cung lớn nhất từ vị trí hiện tại tới một viên thức ăn còn lại (`mazeDistance`, chạy BFS), có bộ nhớ đệm trong `problem.heuristicInfo` theo khóa (vị trí, viên thức ăn). Lấy max (không lấy tổng) vì Pac-Man bắt buộc phải tới được viên xa nhất, còn tổng khoảng cách tính trùng các viên nằm trên đường. Cần giải thích vì sao Manhattan yếu trên `trickySearch` (tường chữ U làm đường thực dài hơn nhiều so với đường chim bay).
- **q8.** `AnyFoodSearchProblem.isGoalState` trả về `self.food[x][y]`; `findPathToClosestDot` gọi `search.bfs` trên bài toán này. DFS không phù hợp vì không đảm bảo viên gần nhất. Cần nêu rõ hạn chế: chiến lược tham lam theo từng đoạn không đảm bảo đường đi tối ưu toàn cục.

---

## 6. Project 2: Tìm kiếm đối kháng

### 6.1 Hình thức hóa

- **Tác tử:** $n = 1 + m$ (1 Pac-Man và $m$ ma), chơi luân phiên theo chỉ số.
- **Trạng thái:** `GameState` gồm vị trí các tác tử, lưới thức ăn, danh sách capsule, bộ đếm sợ của từng ma, điểm hiện tại.
- **Hành động:** `getLegalActions(agentIndex)`; hàm chuyển: `generateSuccessor(agentIndex, action)`.
- **Hàm tiện ích:** điểm trò chơi `getScore()` (hoặc hàm đánh giá tự thiết kế); nút thắng/thua là nút lá.
- **Độ sâu:** một đơn vị độ sâu gồm một lượt của Pac-Man và một lượt của tất cả các ma. Với $m$ ma và độ sâu $D$, cây có $D\cdot(m+1)$ tầng. Nút lá khi thắng, thua hoặc đạt độ sâu $D$.

Công thức giá trị (tại độ sâu $d$, tác tử $i$):

$$ V(s,d,i)=\begin{cases}
\text{Eval}(s) & s\ \text{kết thúc hoặc}\ d=D\\
\max_{a} V(s_a,d',i') & i=0\ (\text{Pac-Man})\\
\min_{a} V(s_a,d',i') & i\ge 1\ (\text{Minimax})\\
\frac{1}{|A(s)|}\sum_{a} V(s_a,d',i') & i\ge 1\ (\text{Expectimax})
\end{cases} $$

với $i'=(i+1)\bmod n$ và $d'=d+1$ khi $i'=0$, ngược lại $d'=d$.

Alpha-Beta giữ hai cận $\alpha$ (giá trị tốt nhất MAX đã đảm bảo) và $\beta$ (giá trị tốt nhất MIN đã đảm bảo). Nút MAX cắt khi $v>\beta$, nút MIN cắt khi $v<\alpha$. Phải dùng bất đẳng thức chặt (không cắt khi bằng) để tập nút sinh ra khớp bộ chấm; tại gốc phải cập nhật $\alpha$ sau mỗi hành động của Pac-Man, nếu không các nhánh MIN phía dưới không cắt tỉa được. Alpha-Beta trả về cùng hành động và cùng giá trị gốc với Minimax nhưng sinh ít nút hơn.

### 6.2 Từng câu và cách bộ chấm kiểm tra

| Câu | Nội dung | Điểm tối đa | Bộ chấm kiểm tra |
| --- | --- | --- | --- |
| q1 | ReflexAgent | 4 | 10 ván trên `openClassic`, 1 `RandomGhost`, tối đa 120 s; điểm trung bình ≥ 500 và ≥ 1000 (mỗi ngưỡng 1 điểm); số ván thắng ≥ 5 và = 10 (mỗi ngưỡng 1 điểm); cần ít nhất 1 ván thắng |
| q2 | MinimaxAgent | 5 | Cây đồ thị (`GraphGameTreeTest`: hành động đúng và tập nút sinh ra đúng, gồm các test độ sâu, nhiều ma, nút thắng/thua, hòa tại gốc) và `8-pacman-game` (`smallClassic`, độ sâu 2, 2 `DirectionalGhost`) |
| q3 | AlphaBetaAgent | 5 | Cùng loại test; kiểm tra cả số nút được mở, nên không được sắp xếp lại thứ tự con hay cắt khi bằng |
| q4 | ExpectimaxAgent | 5 | Cây `expectimax1/2`, test nhiều ma và độ sâu, `7-pacman-game` |
| q5 | betterEvaluationFunction | 6 | `ExpectimaxAgent` với `evalFn=better`, `smallClassic`, 10 ván, 1 `RandomGhost`, tối đa 120 s: 1 điểm nếu không ván nào quá giờ; 2 điểm theo ngưỡng điểm trung bình 500 và 1000; 3 điểm theo số ván thắng ≥ 1, ≥ 5, = 10 |

Tổng Project 2 là 25 điểm. (File `extra`, `ContestAgent`, là phần thêm 0 điểm, bỏ qua trừ khi nhóm có làm.)

### 6.3 Ý chính cho từng tác tử

- **q1.** Tác tử xét từng hành động hợp lệ, sinh trạng thái kế tiếp rồi chấm bằng hàm đánh giá. Các đặc trưng điển hình: điểm nền của trạng thái kế tiếp, nghịch đảo khoảng cách Manhattan tới thức ăn gần nhất (thưởng khi gần), phạt nặng khi ma không sợ ở rất gần, phạt hành động `Stop`.
- **q2.** Một hàm đệ quy duyệt theo chỉ số tác tử và độ sâu; tại gốc chọn hành động có giá trị lớn nhất, giữ hành động đầu tiên khi hòa. Cần xử lý nút kết thúc trước khi đọc danh sách hành động (tránh `max()` trên danh sách rỗng). Hiện tượng đáng nêu: khi Minimax chắc chắn bị bắt, nó chọn chết sớm để giảm phạt thời gian (−501 tốt hơn −504).
- **q3.** Thêm $\alpha, \beta$ như mục 6.1. Nêu điều kiện không cắt khi bằng và lý do liên quan đến việc khớp tập nút của bộ chấm.
- **q4.** Thay tầng MIN bằng tầng kỳ vọng với xác suất đều $1/|A(s)|$, đúng mô hình `RandomGhost`. Không thể cắt tỉa kiểu Alpha-Beta vì trung bình phụ thuộc mọi nhánh con. Ở `trappedClassic`, Minimax tin ma chơi tối ưu nên lao vào ma; Expectimax còn xác suất thoát và thắng một số ván. Chỉ khẳng định tỉ lệ thắng bằng số đo của nhóm.
- **q5.** Hàm đánh giá tuyến tính trên trạng thái (không có tham số `action`):

$$ \text{Eval}(s)=\text{Score}(s)+\frac{w_1}{d_{\text{food}}+1}-w_2\,N_{\text{food}}-w_3\,N_{\text{capsule}}+\sum_{g\ \text{sợ}}\frac{w_4}{d_g+1}-\sum_{g\ \text{thường}}\Phi(d_g) $$

Công thức trên là **mẫu**; phải thay bằng công thức thật của nhóm. Cần giải thích: dùng nghịch đảo khoảng cách để biến giá trị nhỏ thành điểm thưởng lớn và tránh chia cho 0 (cộng 1 ở mẫu); vì sao dùng Manhattan thay cho `mazeDistance` (hàm được gọi ở mọi nút lá, giới hạn 120 s/ván); xử lý riêng ma đang sợ (`scaredTimer > 0`); cách chọn trọng số (các phiên bản đã thử, kết quả từng phiên bản).

### 6.4 Giá trị tham chiếu

Bộ chấm không cung cấp số liệu tham chiếu về tỉ lệ thắng; mọi số về thắng/thua, điểm trung bình, thời gian lấy từ thực nghiệm của nhóm.

---

## 7. Ánh xạ từng `\todo` trong `Nhom3.tex` sang nội dung cần viết

Ngân sách trang gợi ý (tổng ≤ 7): Tóm tắt 0,25; Giới thiệu 0,9; Phương pháp 2,4; Thực nghiệm 2,4; Kết luận 0,3; Tài liệu tham khảo 0,5; bảng phân công đã chiếm một phần Giới thiệu.

| Vị trí trong `Nhom3.tex` | Nội dung cần viết | Nguồn |
| --- | --- | --- |
| Tóm tắt: "Thêm 2–3 câu tóm tắt kết quả" | Bài toán, các thuật toán đã cài, 2–3 kết quả định lượng nổi bật (điểm Autograder, giảm số nút mở của A\* so với UCS, tỉ lệ thắng của tác tử tốt nhất, giảm số nút của Alpha-Beta so với Minimax) | `SO_LIEU.md` |
| Tóm tắt: URL GitHub | Thay `\url{https://github.com/\todo{...}/\todo{...}}` bằng URL thật; đừng đặt `\todo` bên trong `\url` | Người dùng |
| 1.1 "Nêu rõ vấn đề cần giải quyết" | Hai đoạn: (P1) bài toán tìm kiếm trên không gian trạng thái ở mục 5.1, tiêu chí là đường đi chi phí nhỏ nhất và số nút mở; (P2) bài toán ra quyết định đối kháng ở mục 6.1, tiêu chí là điểm số và xác suất thắng. Nêu được không gian trạng thái, tập hành động, hàm chuyển, hàm đích/tiện ích | Mục 5.1, 6.1 |
| 1.3 "Bố cục" | 1–2 câu dẫn các Mục II, III, IV | |
| 2.1.1 q1–q4 "Nêu thêm" | Cách lưu đường đi, xử lý nút trùng, tối ưu và độ phức tạp ($O(b^m)$ thời gian cho DFS, $O(b^{d})$ cho BFS/UCS/A\* trong trường hợp xấu nhất) | Mục 5.2 |
| 2.1.2 q5, q6 | Biểu diễn trạng thái, hàm kế tiếp, đích; heuristic và chứng minh chấp nhận được, nhất quán | Mục 5.5 và mã của TV2 |
| 2.1.3 q7 | foodHeuristic, chứng minh, bộ nhớ đệm | Mục 5.5 và mã của TV2 |
| 2.1.4 q8 | BFS trên `AnyFoodSearchProblem`, hạn chế tham lam | Mục 5.5 |
| 2.2.1 Reflex | Đặc trưng và trọng số thực tế | Mã của TV3 |
| 2.2.2 Minimax, Alpha-Beta | Công thức mục 6.1 hoặc giả mã (`algorithmic`); điều kiện cắt tỉa | Mục 6.1 |
| 2.2.3 Expectimax | Mô hình ma ngẫu nhiên đều; khác biệt so với Minimax | Mục 6.3 |
| 2.2.4 Hàm đánh giá tốt hơn | Đặc trưng, công thức, trọng số, các phiên bản đã thử | Mã của TV2, TV4 |
| 3.1 Thiết lập thực nghiệm | Python, hệ điều hành, CPU, layout, seed, số ván, tiêu chí đo | `SO_LIEU.md`, mục 8 của file nhiệm vụ |
| Bảng `tab:p1` | Số nút mở rộng và chi phí trên `mediumMaze`, `bigMaze` cho DFS/BFS/UCS/A\* | `SO_LIEU.md` |
| Bảng `tab:heur` | Số nút mở rộng của A\* với heuristic rỗng và heuristic của nhóm (`mediumCorners`, `trickySearch`) | `SO_LIEU.md` |
| Nhận xét sau `tab:heur` | Thuật toán nào mở ít nút nhất; heuristic cải thiện bao nhiêu phần trăm (tính từ số đo) | `SO_LIEU.md` |
| Bảng `tab:p2` | Tỉ lệ thắng, điểm trung bình, thời gian mỗi ván trên `smallClassic` cho Reflex, Minimax, Alpha-Beta, Expectimax, hàm đánh giá tốt hơn | `SO_LIEU.md` |
| Nhận xét sau `tab:p2` | Alpha-Beta giảm bao nhiêu thời gian/số nút so với Minimax khi hành động giống nhau; Expectimax so với Minimax khi ma ngẫu nhiên | `SO_LIEU.md` |
| Bảng `tab:grader` | Điểm Autograder P1 và P2 (tối đa 25 mỗi project) | Log Autograder |
| Kết luận | Kết quả, hạn chế, hướng phát triển (3–5 câu) | Toàn bộ báo cáo |
| Bảng phân công | MSSV TV1–TV3, % hoàn thành đã được nhóm xác nhận | Người dùng |

Yêu cầu bổ sung của giảng viên: phần Thực nghiệm nên có ít nhất một biểu đồ (đường hoặc cột) và một đoạn thảo luận về trường hợp quyết định sai, góc chết, điểm yếu khi ma ngẫu nhiên. Phần tài liệu tham khảo đã có 6 mục; nên giữ đủ ít nhất 5 và thêm tài liệu CS188 nếu cần.

---

## 8. Văn phong học thuật

### 8.1 Quy tắc

1. Dùng ngôn ngữ khoa học, nghiêm túc, chính xác; không dùng văn nói, từ cảm tính hoặc diễn đạt tùy tiện.
2. Diễn giải tự nhiên, có lập luận và chiều sâu, phù hợp một bài nghiên cứu của sinh viên. Không cố viết quá hàn lâm làm câu văn nặng nề, thiếu tự nhiên.
3. Tránh các cụm sáo rỗng, lối dẫn dắt khuôn mẫu và câu kết chung chung như "nhìn chung", "có thể thấy rằng", "như chúng ta đã biết", "không thể phủ nhận" khi không thật sự cần.
4. Tránh phó từ cảm xúc ("rất", "cực kỳ", "tuyệt vời", "dễ dàng") và các lời khen cho phương pháp; thay bằng số liệu hoặc lập luận.
5. Mỗi nhận xét phải gắn với một bằng chứng: số liệu trong bảng, hoặc một lập luận lý thuyết nêu rõ tiền đề. Mỗi bảng, hình phải được dẫn chiếu trong văn bản (`Bảng~\ref{...}`).
6. Dùng ngôi vô nhân xưng hoặc "nhóm" ("nhóm cài đặt", "kết quả cho thấy"). Không dùng "chúng em", "tụi mình".
7. Phần phân tích viết thành đoạn văn liền mạch; chỉ dùng danh sách gạch đầu dòng cho các mục liệt kê ngắn.
8. Con số kèm đơn vị và điều kiện đo (layout, độ sâu, số ván, seed). Phần trăm cải thiện phải tính từ số đo và ghi rõ cách tính.
9. Không dùng emoji, không viết hoa nhấn mạnh, không để lại ký hiệu `\todo` trong bản cuối.
10. Thuật ngữ nhất quán suốt bài (bảng dưới). Lần đầu xuất hiện, ghi kèm thuật ngữ tiếng Anh trong ngoặc.

### 8.2 Bảng thuật ngữ

| Tiếng Anh | Dùng trong báo cáo |
| --- | --- |
| search problem / state space | bài toán tìm kiếm / không gian trạng thái |
| fringe, frontier | biên (tập nút chờ mở) |
| closed set / expanded | tập nút đã mở / mở rộng nút |
| graph search | tìm kiếm trên đồ thị |
| admissible / consistent heuristic | heuristic chấp nhận được / nhất quán |
| adversarial search | tìm kiếm đối kháng |
| pruning | cắt tỉa |
| evaluation function | hàm đánh giá |
| ply / depth | độ sâu (một lượt của mọi tác tử) |
| win rate | tỉ lệ thắng |
| scared ghost | ma đang sợ (bị dọa) |

### 8.3 Ví dụ viết lại

- Cần tránh: "Nhìn chung, có thể thấy rằng A\* rất hiệu quả và nhanh hơn hẳn các thuật toán còn lại."
- Nên viết: "Trên `mediumMaze`, A\* với heuristic Manhattan mở rộng 221 nút, ít hơn 48 nút so với UCS (269 nút), tương ứng giảm 17,8%; cả hai cùng cho đường đi tối ưu." (Chỉ dùng khi các số này trùng số đo của nhóm.)
- Cần tránh: "Alpha-Beta tốt hơn Minimax vì chạy nhanh."
- Nên viết: "Do không xét các nhánh không thể làm thay đổi giá trị tại gốc, Alpha-Beta cho cùng hành động với Minimax nhưng sinh ít trạng thái hơn; ở độ sâu 3 trên `smallClassic`, số trạng thái sinh ra giảm từ X xuống Y."

---

## 9. Thông tin AI cần hỏi người dùng nếu chưa có

1. URL GitHub chính xác và nhánh nộp bài.
2. MSSV của TV1, TV2, TV3; tỉ lệ đóng góp cuối cùng của từng thành viên.
3. Mã `search.py`, `searchAgents.py` (CornersProblem, cornersHeuristic, foodHeuristic, ClosestDot) và `multiAgents.py` bản cuối.
4. File `SO_LIEU.md` đã điền (mẫu ở cuối file `DANH_SACH_CONG_VIEC.md`) và log Autograder của hai project.
5. Môi trường chạy thực tế: phiên bản Python, hệ điều hành, CPU.
6. Công thức, trọng số và các phiên bản hàm đánh giá đã thử ở q5.

---

## 10. Các điểm mâu thuẫn hoặc cần thận trọng trong tài liệu nguồn

1. **Điểm tối đa:** tài liệu ôn vấn đáp nêu q6 "4/4" và q7 "5/5"; file `CONFIG` ghi q6 = 3 điểm, q7 = 4 điểm (riêng test `trickySearch` có điểm cơ bản 1 và 4 ngưỡng, nên điểm hiển thị có thể khác trần CONFIG). Báo cáo lấy theo **đầu ra thực của Autograder**.
2. **Phiên bản Python:** file phân công và khung báo cáo ghi "3.6+"; hướng dẫn của giảng viên ghi 3.9–3.12. Ghi đúng phiên bản nhóm thực sự dùng, khuyến nghị 3.9 trở lên.
3. **Số liệu minh họa trong tài liệu ôn tập** (ví dụ khoảng 4137 nút cho q7, 700–900 nút cho q6) chưa được kiểm chứng trên mã của nhóm; không đưa vào báo cáo.
4. **Hàm đánh giá mẫu trong tài liệu ôn tập** trả về `+inf` khi thắng và `-inf` khi thua. Trong Expectimax, trung bình có cả hai giá trị này cho kết quả `nan`. Nếu mã của nhóm dùng cách đó, nên nêu rõ trong mục hạn chế hoặc dùng giá trị hữu hạn lớn.
5. **Công thức hàm đánh giá:** công thức trong hướng dẫn của giảng viên (5 trọng số, không có capsule) khác công thức trong tài liệu ôn tập (có capsule). Công thức trong báo cáo phải khớp mã.
6. **Tên thành viên:** một số chỗ ghi "Trường NGọc Anh", "Hồng Đăng"; dùng tên đầy đủ như trong `Nhom3.tex`.
7. **`Nhom3.tex`:** (a) `\url` chứa `\todo` sẽ lỗi biên dịch; (b) chưa nạp gói `url` hoặc `hyperref` nên cần kiểm tra khi biên dịch; (c) lệnh `\todo{}` rỗng trong bảng in ra `[]`; (d) nếu thêm `pgfplots`, nạp trong phần tiền đề.
8. **Project 0:** không có trong bản mã AI nhận được; chỉ nhắc ngắn (môi trường, Autograder) trong báo cáo, không mô tả chi tiết nếu thiếu dữ liệu.
9. **Giấy phép:** các file gốc mang thông báo của UC Berkeley (không phân phối lời giải, giữ nguyên thông báo bản quyền và ghi nguồn). Yêu cầu của giảng viên là GitHub công khai; giữ nguyên phần tiêu đề giấy phép trong mọi file và ghi nguồn CS188 trong README và báo cáo.

---

## 11. Danh sách tự rà soát trước khi trả bài

- [ ] Không còn `\todo` (trừ khi thiếu số liệu thật, và đã liệt kê riêng).
- [ ] Mỗi con số trong báo cáo có trong `SO_LIEU.md` hoặc log do người dùng cung cấp.
- [ ] Công thức hàm đánh giá, heuristic khớp mã.
- [ ] Mỗi bảng và hình có chú thích, có nhãn và được dẫn chiếu trong văn bản.
- [ ] URL GitHub nằm trong Tóm tắt.
- [ ] Bảng phân công đủ Họ tên, MSSV, vai trò, công việc, %.
- [ ] Có ít nhất 5 tài liệu tham khảo IEEE và mỗi mục đều được trích dẫn trong văn bản.
- [ ] Tổng độ dài ≤ 7 trang (biên dịch trên Overleaf).
- [ ] Văn phong đúng mục 8: không có cụm sáo rỗng, không phó từ cảm xúc, mỗi nhận xét có bằng chứng.
- [ ] Các điểm ở mục 10 đã được xử lý hoặc nêu rõ.
