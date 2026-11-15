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
