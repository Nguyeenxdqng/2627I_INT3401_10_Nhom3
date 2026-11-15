# SO_LIEU (Nhóm 3)

Nguồn: log Autograder chạy lúc 08:34 ngày 13/11/2026 (`logs/project1.log`, `logs/project2.log`). Các ô trống chưa có số đo, AI không được tự điền.
Python: __ | Hệ điều hành: __ | CPU: __ | Seed Autograder: 0 (`random.seed(0)` trong `autograder.py`)

## 1. Điểm Autograder (13/11/2026)

| Project | q1 | q2 | q3 | q4 | q5 | q6 | q7 | q8 | Tổng |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P1 (tối đa 3,3,3,3,3,3,4,3 = 25) | 3/3 | 3/3 | 3/3 | 3/3 | 3/3 | 3/3 | 5/4 | 3/3 | 26/25 |
| P2 (tối đa 4,5,5,5,6 = 25) | 4/4 | 5/5 | 5/5 | 5/5 | 6/6 | n/a | n/a | n/a | 25/25 |

Ghi chú q7: test `food_heuristic_grade_tricky` cấp 1 điểm cơ bản và 1 điểm cho mỗi ngưỡng (15000, 12000, 9000, 7000); heuristic mở 4137 nút nên đạt cả 4 ngưỡng, tổng 5 điểm vượt trần 4 điểm của `CONFIG`. Báo cáo ghi 26/25 theo Autograder kèm chú thích này.

## 2. Bảng tab:p1: `mediumMaze` (số nút mở rộng / độ dài đường đi, đơn vị chi phí 1 mỗi bước)

| Layout | DFS | BFS | UCS | A* Manhattan |
| --- | --- | --- | --- | --- |
| mediumMaze | 146 / 130 | 269 / 68 | 269 / 68 | 221 / 68 |
| bigMaze | 390 / 210 | 620 / 210 | 620 / 210 | 549 / 210 |

Nguồn: test `pacman_1` (q1, q2), `ucs_1_problemC` (q3), `astar_2_manhattan` (q4). A* giảm 48 nút so với UCS, tương ứng 17,8% (= (269 − 221)/269).

UCS với hàm chi phí khác nhau trên `mediumMaze`:

| Hàm chi phí | Nút mở rộng | Độ dài đường đi |
| --- | --- | --- |
| 1 (mặc định) | 269 | 68 |
| `0.5 ** x` (StayEast) | 260 | 74 |
| `2 ** x` (StayWest) | 173 | 152 |

## 3. Bảng tab:heur

| Bài toán | Heuristic rỗng | Heuristic của nhóm | % giảm |
| --- | --- | --- | --- |
| mediumCorners (A\*, chi phí tối ưu 106) | 1966 nút| 692 nút | 64,80%|
| trickySearch (A\*) | 16688 nút| 4137 nút | 75,21%|

Ngưỡng của bộ chấm: q6 là 2000, 1600, 1200 nút; q7 là 15000, 12000, 9000, 7000 nút. Còn thiếu: số nút khi dùng `nullHeuristic` (lệnh ở mục B3 của file nhiệm vụ).

## 4. q8 ClosestDot

13/13 test đạt (độ dài đường đi 1, 1, 2, 3, 1, 1, 1, 3, 1, 2, 1, 3, 1 theo từng test). Trên bigSearch, ClosestDotSearchAgent tìm được đường đi có chi phí 350 bước.


Lệnh: python pacman.py -l bigSearch -p ClosestDotSearchAgent -q
## 5. Project 2: kết quả từ Autograder (chỉ dùng như số liệu của chính hai test này)

| Test | Tác tử | Layout | Ma | Số ván | Thắng | Điểm TB | Min | Max |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| q1 `grade-agent` | ReflexAgent | openClassic | 1 RandomGhost | 10 | 10/10 | 1225.3 | 1195 | 1251 |
| q5 `grade-agent` | ExpectimaxAgent, `evalFn=better`, depth 2 (mặc định) | smallClassic | 1 RandomGhost | 10 | 10/10 | 1190.6 | 866 | 1346 |

Lưu ý: ba test `8-pacman-game` (q2), `8-pacman-game` (q3), `7-pacman-game` (q4) đều in "Pacman died! Score: 84", vì trong các test đó tác tử của nhóm chỉ được so sánh hành động với tác tử chuẩn còn ván chơi do tác tử chuẩn điều khiển. Không dùng các con số này làm tỉ lệ thắng.

## 6. Bảng tab:p2 (smallClassic, cần chạy mục B5 để điền; mô hình ma: 2 RandomGhost; seed = 0.)

| Tác tử | n ván | Thắng | Điểm TB | Min | Max | s/ván |
| --- | --- | --- | --- | --- | --- | --- |
| Reflex | 10 | 9 | 1006.4 | -336.0 | 1551.0 |0.797735 |
| Minimax d3 | 10 | 5 | 430.3 | -397.0 | 1287.0|90.972287|
| Alpha-Beta d3 | 10 | 4 | 313.4| -319.0 | 1133.0 |93.5216427 |
| Expectimax d3 | 10 | 4| 140.7| -1180.0| 1455.0|331.7818554 |
| Expectimax + better d2 | 10|10 | 1405.9| 1147.0| 1741.0| 6.9191202|

Expectimax kết hợp hàm đánh giá better ở độ sâu 2 đạt kết quả cao nhất trong bảng: thắng 10/10 ván, điểm trung bình 1405,9 và thời gian khoảng 6,92 giây/ván. Reflex đạt 9/10 ván thắng và chạy nhanh nhất, khoảng 0,80 giây/ván. Kết quả gợi ý rằng chất lượng hàm đánh giá có vai trò lớn; tăng độ sâu tìm kiếm chưa chắc cải thiện hiệu quả. Tuy nhiên, so sánh Expectimax mặc định độ sâu 3 với better độ sâu 2 đồng thời thay đổi cả hàm đánh giá lẫn độ sâu, nên chưa thể tách riêng tác dụng của từng yếu tố.
## 7. Minimax và Alpha-Beta (mục B4)

| Layout, depth | Hành động Minimax | Hành động Alpha-Beta | Trạng thái Minimax | Trạng thái Alpha-Beta | s Minimax | s Alpha-Beta |
| --- | --- | --- | --- | --- | --- | --- |
| minimaxClassic, 3  |Stop  |Stop |607 |482 |0.0455 |0.0318 |
| smallClassic, 3 | West|West |423 |164 |0.0350 |0.0107 |

Minimax và Alpha-Beta trả về cùng hành động ở hai trạng thái được kiểm tra. Alpha-Beta giảm số trạng thái được ghi nhận từ 607 xuống 482 trên minimaxClassic, tương đương 20,59%; và từ 423 xuống 164 trên smallClassic, tương đương 61,23%. Đây là bằng chứng trực tiếp về lợi ích cắt tỉa. Chênh lệch số ván thắng giữa hai thuật toán ở mục 6 cần được kiểm tra lại trước khi dùng để kết luận về chất lượng quyết định.
## 8. trappedClassic (độ sâu 3, n = 10)

| Tác tử | Thắng | Điểm TB |
| --- | --- | --- |
| Alpha-Beta | 0/10 (0.0)|-501 điểm  |
| Expectimax | 5/10|15.0 điểm |

Với cùng độ sâu 3 và hai RandomGhost, Alpha-Beta thua cả 10 ván, đạt điểm trung bình −501; Expectimax thắng 5/10 ván, đạt điểm trung bình 15. Alpha-Beta sử dụng giả định Minimax rằng ma luôn chọn hành động bất lợi nhất cho Pac-Man. Khi các nhánh đều dẫn đến thua theo giả định này, Pac-Man chọn chết sớm để giảm điểm phạt thời gian. Expectimax tính giá trị kỳ vọng theo các hành động ngẫu nhiên của ma, nên vẫn chọn những hướng có cơ hội thoát. Kết quả cho thấy Expectimax phù hợp hơn với mô hình RandomGhost trong cấu hình thử nghiệm này.
## 9. Các phiên bản hàm đánh giá (mục B6)

| Phiên bản | Thay đổi | Thắng | Điểm TB |
|---|---|---|---|
| Hàm mặc định (Berkeley) | không dùng hàm better | 7/10 | 912.3 |
| Gốc | không | 10/10 | 1378.8 |
| v1 | bản sao của gốc | 10/10 | 1378.8 |
| v2 | wGhost 12 -> 24 | 9/10 | 1269.9 |
| v3 | wNearestFood 10 -> 20 | 10/10 | 1523.4 |
| v4 | wFoodCount 4 -> 8 | 9/10 | 1145.7 |
| v5 | thêm capsule | 10/10 | 1391.9 |

Cấu hình: 2 RandomGhost, depth=3, scoreEvaluationFunction,
10 ván/tác tử, seed='cs188' qua cờ -f.
## 10. Công thức cần dán từ mã

Mỗi mục gồm mã nguồn đang dùng, công thức tương ứng và giải thích. Mã trích từ các file hiện tại; lược bỏ docstring và các dòng comment riêng để dễ đọc.

Quy ước chung: $S(s)$ là điểm của trạng thái $s$; $F(s)$ là tập thức ăn còn lại; $D_M(p,q)=|p_x-q_x|+|p_y-q_y|$ là khoảng cách Manhattan. Với ma thứ $i$, $d_i$ là khoảng cách Manhattan từ Pac-Man tới ma và $t_i$ là `scaredTimer`. Ký hiệu $\mathbf{1}[C]$ bằng 1 nếu điều kiện $C$ đúng, bằng 0 nếu sai.

### 10.1. Hàm đánh giá cuối (`betterEvaluationFunction`)

Nguồn: `Project2/multiAgents.py`.

**Mã nguồn:**

```python
def betterEvaluationFunction(currentGameState: GameState):
    score = float(currentGameState.getScore())
    if currentGameState.isWin():
        return score + 1_000_000.0
    if currentGameState.isLose():
        return score - 1_000_000.0

    position = currentGameState.getPacmanPosition()
    foods = currentGameState.getFood().asList()
    score -= 4.0 * len(foods)

    if foods:
        nearest_food = min(manhattanDistance(position, food) for food in foods)
        score += 10.0 / (nearest_food + 1.0)

    for ghost in currentGameState.getGhostStates():
        distance = manhattanDistance(position, ghost.getPosition())
        if ghost.scaredTimer > 0:
            if distance < ghost.scaredTimer:
                score += 20.0 / (distance + 1.0)
        else:
            score -= 12.0 / (distance + 1.0)
            if distance <= 1:
                score -= 200.0

    return score
```

**Công thức:**

Với trạng thái chưa thắng hoặc thua:

$$
E(s)=S(s)-4|F(s)|+B_F(s)+\sum_i G_i(s).
$$

Trong đó:

$$
B_F(s)=
\begin{cases}
\dfrac{10}{d_{\min}+1}, & F(s)\ne\varnothing,\\
0, & F(s)=\varnothing,
\end{cases}
$$

với $d_{\min}$ là khoảng cách Manhattan tới thức ăn gần nhất, và:

$$
G_i(s)=
\begin{cases}
\dfrac{20}{d_i+1}, & t_i>0 \text{ và } d_i<t_i,\\
0, & t_i>0 \text{ và } d_i\ge t_i,\\
-\dfrac{12}{d_i+1}-200\mathbf{1}[d_i\le1], & t_i=0.
\end{cases}
$$

Trạng thái thắng trả về $S(s)+1\,000\,000$; trạng thái thua trả về $S(s)-1\,000\,000$.

**Giải thích:**

- `-4 * len(foods)`: phạt thức ăn còn lại, khuyến khích hoàn thành màn chơi.
- `10 / (nearest_food + 1)`: thưởng khi ở gần thức ăn; cộng 1 ở mẫu để tránh chia cho 0.
- `20 / (distance + 1)`: thưởng tiếp cận ma đang sợ khi `distance < scaredTimer`. Điều kiện này dùng khoảng cách Manhattan, là tiêu chí ước lượng cơ hội bắt ma.
- `-12 / (distance + 1)` và phạt thêm 200 khi `distance <= 1`: tránh ma nguy hiểm, đặc biệt ở cự ly sát bên.
- Thưởng/phạt lớn ở trạng thái kết thúc giúp ưu tiên thắng và tránh thua.

### 10.2. Heuristic q6 (`cornersHeuristic`)

Nguồn: `Project1/searchAgents.py`.

**Mã nguồn:**

```python
def cornersHeuristic(state: Any, problem: CornersProblem):
    corners = problem.corners # These are the corner coordinates
    walls = problem.walls # These are the walls of the maze, as a Grid (game.py)

    position, visited_corners = state

    unvisited = [
        corner for corner, visited in zip(corners, visited_corners)
        if not visited
    ]

    if not unvisited:
        return 0  # Goal state

    current_pos = position
    total_cost  = 0
    remaining   = list(unvisited)

    while remaining:
        nearest_dist = min(
            util.manhattanDistance(current_pos, corner)
            for corner in remaining
        )
        total_cost += nearest_dist
        for corner in remaining:
            if util.manhattanDistance(current_pos, corner) == nearest_dist:
                current_pos = corner
                remaining.remove(corner)
                break

    return total_cost
```

**Công thức:**

Gọi $U$ là tập các góc chưa thăm, $k=|U|$, và $c_0=p$ là vị trí hiện tại. Mã chọn lần lượt góc gần nhất:

$$
c_j \in \operatorname*{arg\,min}_{c\in U\setminus\{c_1,\ldots,c_{j-1}\}}
D_M(c_{j-1},c),\qquad j=1,\ldots,k.
$$

Sau đó trả về:

$$
h_{\mathrm{corners}}(s)=\sum_{j=1}^{k}D_M(c_{j-1},c_j).
$$

Nếu $U$ rỗng thì $h_{\mathrm{corners}}(s)=0$.

**Giải thích:**

- `unvisited` lấy các góc chưa thăm từ trạng thái tìm kiếm.
- Mỗi vòng lặp chọn góc gần nhất theo Manhattan, cộng khoảng cách vào `total_cost`, rồi loại góc đó khỏi `remaining`.
- Khi có nhiều góc gần nhất bằng nhau, mã chọn góc xuất hiện đầu tiên trong `remaining`.
- Đây là tổng khoảng cách của chuỗi góc được chọn theo chiến lược tham lam. Tính chấp nhận được và nhất quán cần lập luận riêng; việc từng đoạn dùng Manhattan chưa đủ chứng minh hai tính chất cho cả chuỗi.

### 10.3. Heuristic q7 (`foodHeuristic`)

Nguồn: `Project1/searchAgents.py`.

**Mã nguồn:**

```python
def foodHeuristic(state: Tuple[Tuple, List[List]], problem: FoodSearchProblem):
    position, foodGrid = state

    foodList = foodGrid.asList()

    if not foodList:
        return 0  # Goal state — không còn food

    max_dist = 0
    for food in foodList:
        key = (position, food)
        if key not in problem.heuristicInfo:
            problem.heuristicInfo[key] = mazeDistance(
                position, food, problem.startingGameState
            )
        dist = problem.heuristicInfo[key]
        if dist > max_dist:
            max_dist = dist

    return max_dist
```

**Công thức:**

$$
h_{\mathrm{food}}(p,F)=
\begin{cases}
\max_{f\in F}D_{\mathrm{maze}}(p,f), & F\ne\varnothing,\\
0, & F=\varnothing.
\end{cases}
$$

$D_{\mathrm{maze}}(p,f)$ là độ dài đường đi ngắn nhất có xét tường, được tính bằng BFS trong `mazeDistance`.

**Giải thích:**

- Với từng viên thức ăn còn lại, tính khoảng cách mê cung từ vị trí hiện tại.
- Trả về khoảng cách lớn nhất: Pac-Man phải tới viên thức ăn đó để hoàn tất bài toán, nên đây là cận dưới của tổng chi phí còn lại.
- `problem.heuristicInfo[(position, food)]` lưu khoảng cách đã tính để tránh chạy lại BFS cho cùng cặp vị trí.
- Khi không còn thức ăn, chi phí ước lượng còn lại bằng 0.

### 10.4. Hàm đánh giá của `ReflexAgent`

Nguồn: phương thức `ReflexAgent.evaluationFunction` trong `Project2/multiAgents.py`.

**Mã nguồn:**

```python
def evaluationFunction(self, currentGameState: GameState, action):
    successorGameState = currentGameState.generatePacmanSuccessor(action)
    newPos = successorGameState.getPacmanPosition()
    newFood = successorGameState.getFood()
    newGhostStates = successorGameState.getGhostStates()
    newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

    score = successorGameState.getScore()

    foodList = newFood.asList()

    if foodList:
        foodDistances = [
            manhattanDistance(newPos, food)
            for food in foodList
        ]
        minFoodDistance = min(foodDistances)

        score += 10.0 / (minFoodDistance + 1)

        oldFoodCount = len(currentGameState.getFood().asList())
        newFoodCount = len(foodList)
        score += 10 * (oldFoodCount - newFoodCount)

    for ghostState in newGhostStates:
        ghostPos = ghostState.getPosition()

        ghostDistance = manhattanDistance(newPos, ghostPos)
        scaredTimer = ghostState.scaredTimer

        if scaredTimer > 0:
            if ghostDistance < scaredTimer:
                score += 8.0 / (ghostDistance + 1)
        else:
            if ghostDistance == 0:
                score -= 1000
            elif ghostDistance == 1:
                score -= 200
            elif ghostDistance == 2:
                score -= 50
            elif ghostDistance == 3:
                score -= 10

    if action == Directions.STOP and foodList:
        score -= 10

    return score
```

**Công thức:**

Gọi $s'$ là trạng thái sau hành động $a$, $F=F(s)$, $F'=F(s')$. Các khoảng cách tới thức ăn và ma được tính trong $s'$.

$$
R(s,a)=S(s')+B_R(s,a)+\sum_i H_i(s')
-10\mathbf{1}[a=\mathrm{Stop}\ \text{và}\ |F'|>0].
$$

Thành phần thức ăn:

$$
B_R(s,a)=
\begin{cases}
\dfrac{10}{d'_{\min}+1}+10(|F|-|F'|), & |F'|>0,\\
0, & |F'|=0.
\end{cases}
$$

$d'_{\min}$ là khoảng cách Manhattan tới thức ăn gần nhất trong trạng thái kế tiếp. Thành phần của từng ma:

$$
H_i(s')=
\begin{cases}
\dfrac{8}{d_i+1}, & t_i>0 \text{ và } d_i<t_i,\\
0, & t_i>0 \text{ và } d_i\ge t_i,\\
-1000, & t_i=0 \text{ và } d_i=0,\\
-200, & t_i=0 \text{ và } d_i=1,\\
-50, & t_i=0 \text{ và } d_i=2,\\
-10, & t_i=0 \text{ và } d_i=3,\\
0, & \text{các trường hợp còn lại}.
\end{cases}
$$

**Giải thích:**

- `successorGameState.getScore()` lấy điểm sau khi thực hiện hành động đang xét.
- Thành phần thức ăn thưởng tiến gần thức ăn và thưởng thêm 10 điểm cho mỗi viên vừa ăn. Trong mã hiện tại, cả hai khoản thưởng thêm này chỉ được tính nếu trạng thái kế tiếp vẫn còn thức ăn.
- Ma đang sợ có thể mang lại điểm thưởng tiếp cận; ma thường càng gần thì mức phạt càng lớn theo các mốc 0, 1, 2, 3.
- `Stop` bị phạt thêm 10 điểm nếu vẫn còn thức ăn, giúp hạn chế đứng yên.
- `getAction` chọn hành động có điểm đánh giá cao nhất; nếu hòa thì chọn ngẫu nhiên trong các hành động cùng điểm.

## 11. Tình huống thất bại quan sát được (mục B7)

### 11.1. Cấu hình và kết quả kiểm chứng

Nhóm quan sát chơi có đồ họa và báo cáo Pac-Man thắng 4/5 ván, có lúc đứng chờ ma tới gần rồi mới chạy. Chạy kiểm chứng ngày 16/11/2026 với `smallClassic`, `ExpectimaxAgent`, `evalFn=better`, `depth=2`, 2 `RandomGhost`, 5 ván và seed chuỗi `'cs188'` cho đúng kết quả 4/5 ván thắng. Lần kiểm chứng tắt đồ họa để ghi hành động và thời gian tính toán; không đo độ trễ hiển thị của cửa sổ game.

Lệnh chạy từ `Project2/`:

```powershell
python pacman.py -l smallClassic -p ExpectimaxAgent -a "evalFn=better,depth=2" -g RandomGhost -k 2 -n 5 -q -f
```

| Ván | Kết quả | Điểm cuối | Số lượt Pac-Man | Số hành động Stop |
| --- | --- | --- | --- | --- |
| 1 | Thắng | 1677 | 173 | 40 |
| 2 | Thắng | 1360 | 90 | 7 |
| 3 | Thắng | 1274 | 176 | 38 |
| 4 | Thua | 16 | 274 | 138 |
| 5 | Thắng | 1689 | 161 | 60 |

Tỉ lệ thắng: 80%; điểm trung bình: 1203,2. Đây là đợt 5 ván riêng, không thay thế số liệu 10 ván với seed 0 ở mục 6. Lệnh game gốc và lần chạy có ghi vết cho cùng thứ tự thắng/thua và cùng điểm từng ván.

### 11.2. Đứng chờ ma tiến gần rồi mới chạy

Trong ván 4, log xác nhận Pac-Man chọn hành động `Stop` thật, không chỉ dừng hình để tính toán. Một đoạn cụ thể, với khoảng cách Manhattan được ghi trước mỗi hành động:

| Lượt Pac-Man (đếm từ 1) | Vị trí Pac-Man | Khoảng cách tới ma thường gần nhất | Hành động |
| --- | --- | --- | --- |
| 260 | (10, 5) | 5 | Stop |
| 261 | (10, 5) | 4 | Stop |
| 262 | (10, 5) | 3 | Stop |
| 263 | (10, 5) | 2 | Stop |
| 264 | (10, 5) | 1 | South |

Pac-Man thoát được đoạn trên nhưng tiếp tục gặp nguy hiểm về sau. Ở lượt 273–274, nó đứng tại (13, 5) và chọn `Stop` hai lần; sau lượt 274, ma đi vào cùng ô và Pac-Man thua, còn 16 viên thức ăn. Việc đứng chờ ở lượt 260–263 không gây chết ngay, nên chưa thể coi đó là nguyên nhân duy nhất của thất bại cuối ván.

### 11.3. Hòa giá trị hành động và trì hoãn tiến tới thức ăn

Phát lại lịch sử ván 4 và tính riêng giá trị kỳ vọng của các hành động ở gốc cho thấy:

| Lượt | Giá trị Stop | Giá trị East | Hành động mã chọn |
| --- | --- | --- | --- |
| 260 | 422,583333 | 422,583333 | Stop |
| 261 | 420,930736 | 420,930736 | Stop |
| 262 | 419,333333 | 419,333333 | Stop |
| 263 | 317,742424 | 317,742424 | Stop |

Các cặp giá trị trên bằng nhau cả trước khi làm tròn. Trong những trạng thái này, `Stop` xuất hiện trước `East` trong danh sách hành động hợp lệ. `ExpectimaxAgent` chỉ cập nhật hành động tốt nhất khi `value > bestValue`, nên giữ `Stop` khi hòa. Đây là cơ chế trực tiếp giải thích chuỗi đứng chờ được ghi nhận.

`betterEvaluationFunction` không có khoản phạt riêng cho `Stop`; phạt thời gian trong điểm game áp dụng cho mọi lượt Pac-Man. Hàm dùng khoảng cách Manhattan tới thức ăn gần nhất, phạt khoảng cách tới ma và tìm kiếm độ sâu hữu hạn, nên có thể đánh giá đứng chờ ngang bằng hoặc cao hơn một bước di chuyển. Ví dụ, ở lượt 73, giá trị `Stop` là 609,130987, cao hơn `North` (609,107418) và `South` (609,096235): không phải mọi lần đứng chờ đều do hòa điểm.

Trong ván thua, `Stop` chiếm 138/274 lượt (50,36%). Từ đầu lượt 62 đến đầu lượt 268, số thức ăn còn lại luôn là 19, cho thấy tiến độ ăn bị đình trệ qua 207 lượt liên tiếp. Tuy nhiên, đứng chờ không luôn dẫn tới thua: ván 5 có chuỗi 56 hành động `Stop` liên tiếp ở lượt 81–136 nhưng cuối cùng vẫn thắng.

Tại lượt cuối (274), giá trị `Stop` là -499811, cao hơn `South` (-499817,45) và `East` (-999974). Tác tử chọn hành động có kỳ vọng cao nhất nhưng vẫn thua trong diễn biến ma thực tế. Kết quả này cho thấy cần phân biệt lựa chọn tốt nhất theo mô hình tìm kiếm với bảo đảm sống sót trong từng ván.

### 11.4. Thời gian tính toán và hiện tượng khựng hình

Trong lần chạy có ghi vết trên máy kiểm chứng, thời gian chọn hành động trung bình khoảng 10,96 ms, trung vị 8,66 ms và lớn nhất 56,51 ms trên tổng 874 lượt Pac-Man. Các số này chỉ đo `getAction`, không bao gồm hiệu ứng đồ họa và không đại diện cho tốc độ trên máy khác.

Vòng lặp trong `Project2/game.py` chờ `getAction` trả về rồi mới thực hiện hành động và chuyển sang lượt kế tiếp; ma không tự chạy tiếp trong lúc Pac-Man đang tính. Vì vậy, chuỗi ma di chuyển trong khi Pac-Man giữ nguyên vị trí ở mục 11.2 là hành vi chọn `Stop`, không thể giải thích bằng việc tính toán chậm. Độ khựng khi bật đồ họa cần phép đo riêng để tách thời gian tính toán và thời gian hiển thị.

### 11.5. Bằng chứng và hướng cải thiện

- Script ghi vết: `Project2/tests/quan_sat_hanh_vi.py`; chạy từ `Project2/` bằng `python -B tests/quan_sat_hanh_vi.py`.
- Log điểm và thắng/thua: `Project2/ket_qua/quan_sat_hanh_vi.log`.
- Hành động, vị trí, khoảng cách ma và thời gian từng lượt: `Project2/ket_qua/quan_sat_hanh_vi.json`.
- Giá trị các hành động ở những lượt được phân tích: `Project2/ket_qua/quan_sat_phan_tich.json`.

Hướng thử nghiệm tiếp theo: ưu tiên hành động di chuyển khi hòa với `Stop`, hoặc bổ sung cơ chế khuyến khích tiến tới thức ăn có xét tường. Có thể thử phạt `Stop` hoặc điều chỉnh phạt ma, nhưng cần đo lại vì một số tình huống đứng chờ giúp tránh ma. Những thay đổi này chưa được triển khai hay đánh giá; kết quả trên phản ánh mã hiện tại.

