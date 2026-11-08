import argparse
import random
import sys
import time
 
import ghostAgents
import layout
import multiAgents
import pacman
 
 
class Counter:
    calls = 0
 
 
_original_generate = pacman.GameState.generateSuccessor
 
 
def _counting_generate(self, agentIndex, action):
    Counter.calls += 1
    return _original_generate(self, agentIndex, action)
 
 
pacman.GameState.generateSuccessor = _counting_generate
 
 
def ask(agent, state, name):
    """Hoi agent chon hanh dong, tra ve (hanh dong, so lan generateSuccessor, giay)."""
    Counter.calls = 0
    start = time.time()
    try:
        action = agent.getAction(state)
    except (Exception, SystemExit) as error:
        print("Loi khi chay %s: %r" % (name, error))
        print("Kiem tra %s da duoc cai dat (khong con util.raiseNotDefined)." % name)
        sys.exit(2)
    return action, Counter.calls, time.time() - start
 
 
def compare_on_layout(layout_name, depth, max_moves, seed):
    random.seed(seed)
    lay = layout.getLayout(layout_name)
    if lay is None:
        print("Khong tim thay layout:", layout_name)
        sys.exit(2)
 
    num_ghosts = lay.getNumGhosts()
    state = pacman.GameState()
    state.initialize(lay, num_ghosts)
    ghosts = [ghostAgents.RandomGhost(i + 1) for i in range(num_ghosts)]
 
    minimax = multiAgents.MinimaxAgent(depth=str(depth))
    alphabeta = multiAgents.AlphaBetaAgent(depth=str(depth))
 
    result = {
        "positions": 0,
        "mismatches": [],
        "calls_minimax": 0,
        "calls_alphabeta": 0,
        "time_minimax": 0.0,
        "time_alphabeta": 0.0,
        "ended": "chua ket thuc",
    }
 
    for move in range(max_moves):
        if state.isWin():
            result["ended"] = "thang"
            break
        if state.isLose():
            result["ended"] = "thua"
            break
 
        a_mm, c_mm, t_mm = ask(minimax, state, "MinimaxAgent")
        a_ab, c_ab, t_ab = ask(alphabeta, state, "AlphaBetaAgent")
 
        result["positions"] += 1
        result["calls_minimax"] += c_mm
        result["calls_alphabeta"] += c_ab
        result["time_minimax"] += t_mm
        result["time_alphabeta"] += t_ab
        if a_mm != a_ab:
            result["mismatches"].append((move, a_mm, a_ab))
 
        state = state.generateSuccessor(0, a_mm)
        for i, ghost in enumerate(ghosts):
            if state.isWin() or state.isLose():
                break
            state = state.generateSuccessor(i + 1, ghost.getAction(state))
 
    return result
 
 
def main():
    parser = argparse.ArgumentParser(description="So sanh Minimax va Alpha-Beta")
    parser.add_argument("--layouts", default="minimaxClassic,smallClassic,trappedClassic")
    parser.add_argument("--depths", default="1,2,3")
    parser.add_argument("--moves", type=int, default=25, help="so buoc toi da moi van")
    parser.add_argument("--seed", type=int, default=188)
    args = parser.parse_args()
 
    layouts = [name.strip() for name in args.layouts.split(",") if name.strip()]
    depths = [int(d) for d in args.depths.split(",") if d.strip()]
 
    header = "%-16s %5s %8s %9s %12s %12s %9s %9s" % (
        "layout", "depth", "vi tri", "khac nhau",
        "calls MM", "calls AB", "giay MM", "giay AB")
    print(header)
    print("-" * len(header))
 
    total_mismatches = 0
    for layout_name in layouts:
        for depth in depths:
            r = compare_on_layout(layout_name, depth, args.moves, args.seed)
            total_mismatches += len(r["mismatches"])
            print("%-16s %5d %8d %9d %12d %12d %9.2f %9.2f  (%s)" % (
                layout_name, depth, r["positions"], len(r["mismatches"]),
                r["calls_minimax"], r["calls_alphabeta"],
                r["time_minimax"], r["time_alphabeta"], r["ended"]))
            for move, a_mm, a_ab in r["mismatches"]:
                print("    buoc %d: Minimax chon %s, AlphaBeta chon %s" % (move, a_mm, a_ab))
            if r["calls_alphabeta"] > r["calls_minimax"]:
                print("    Canh bao: Alpha-Beta goi generateSuccessor nhieu hon Minimax")
 
    print()
    if total_mismatches == 0:
        print("KET QUA: Minimax va Alpha-Beta trung nhau tren moi vi tri da thu.")
        return 0
    print("KET QUA: co %d vi tri khac nhau, xem danh sach o tren." % total_mismatches)
    return 1
 
 
if __name__ == "__main__":
    sys.exit(main())