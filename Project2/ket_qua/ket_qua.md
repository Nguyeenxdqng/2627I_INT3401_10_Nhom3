# So sánh evaluation function (tuần 4)

Cấu hình: ExpectimaxAgent, layout smallClassic, depth 3, cờ -f (cố định hạt giống).

## Kết quả 30 ván
| Phiên bản | Thay đổi | Thắng | Điểm TB |
|---|---|---|---|
| Gốc (betterEvaluationFunction) | không | 30/30 | 1404.6 |
| v3 | wNearestFood 10 -> 20 | 27/30 | 1312.5 |
| v5 | thêm capsule (wCapsule = 10) | 26/30 | 1284.4 |

## Kết quả 10 ván
| Phiên bản | Thay đổi | Thắng | Điểm TB |
|---|---|---|---|
| Hàm mặc định (Berkeley) | không dùng hàm better | 7/10 | 912.3 |
| Gốc | không | 10/10 | 1378.8 |
| v1 | bản sao của gốc | 10/10 | 1378.8 |
| v2 | wGhost 12 -> 24 | 9/10 | 1269.9 |
| v3 | wNearestFood 10 -> 20 | 10/10 | 1523.4 |
| v4 | wFoodCount 4 -> 8 | 9/10 | 1145.7 |
| v5 | thêm capsule | 10/10 | 1391.9 |

## Nhận xét
- Bản gốc thắng 30/30, điểm TB cao nhất, ván thấp nhất 959.
- v3 và v5 tốt ở 10 ván đầu nhưng thua 3-4 ván khi chạy 30 ván.
- v2, v4 chỉ chạy 10 ván, mỗi bản thua 1 ván.
- Kết luận: giữ nguyên betterEvaluationFunction hiện tại.