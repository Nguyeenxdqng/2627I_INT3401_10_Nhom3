"""Record Pac-Man decisions without changing the search or evaluation code."""

import argparse
import contextlib
import hashlib
import json
from pathlib import Path
import random
import statistics
import sys
import time

PROJECT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT))

import layout
import multiAgents
import pacman
import textDisplay
from ghostAgents import RandomGhost
from util import manhattanDistance


def snapshot(state):
    position = state.getPacmanPosition()
    return {
        "pacman": position,
        "score": state.getScore(),
        "food": state.getNumFood(),
        "ghosts": [
            {
                "position": ghost.getPosition(),
                "scared": ghost.scaredTimer,
                "distance": manhattanDistance(position, ghost.getPosition()),
            }
            for ghost in state.getGhostStates()
        ],
    }


class TracedExpectimax(multiAgents.ExpectimaxAgent):
    def __init__(self, depth):
        super().__init__(evalFn="better", depth=str(depth))
        self.traces = []

    def registerInitialState(self, state):
        self.traces.append([])

    def getAction(self, state):
        entry = snapshot(state)
        pacman.GameState.getAndResetExplored()
        started = time.perf_counter()
        action = super().getAction(state)
        entry.update(
            turn=len(self.traces[-1]) + 1,
            action=action,
            seconds=time.perf_counter() - started,
            explored=len(pacman.GameState.getAndResetExplored()),
        )
        self.traces[-1].append(entry)
        return action


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--games", type=int, default=5)
    parser.add_argument("--seed", default="cs188")
    parser.add_argument("--depth", type=int, default=2)
    parser.add_argument("--layout", default="smallClassic")
    parser.add_argument("--output", default="ket_qua/quan_sat_hanh_vi.json")
    args = parser.parse_args()
    destination = Path(args.output)
    destination.parent.mkdir(parents=True, exist_ok=True)
    random.seed(args.seed)
    agent = TracedExpectimax(args.depth)
    maze = layout.getLayout(args.layout)
    if maze is None:
        parser.error("Unknown layout: " + args.layout)
    with destination.with_suffix(".log").open("w", encoding="utf-8") as log:
        with contextlib.redirect_stdout(log):
            games = pacman.runGames(
                maze, agent, [RandomGhost(1), RandomGhost(2)],
                textDisplay.NullGraphics(), args.games, False,
            )
    results = []
    for number, (game, trace) in enumerate(zip(games, agent.traces), 1):
        elapsed = [entry["seconds"] for entry in trace]
        stops = [entry for entry in trace if entry["action"] == "Stop"]
        ordered = sorted(elapsed)
        row = {
            "game": number,
            "win": game.state.isWin(),
            "score": game.state.getScore(),
            "turns": len(trace),
            "stops": len(stops),
            "mean_decision_seconds": statistics.mean(elapsed),
            "median_decision_seconds": statistics.median(elapsed),
            "p95_decision_seconds": ordered[min(int(len(ordered) * .95), len(ordered) - 1)],
            "max_decision_seconds": max(elapsed),
            "trace": trace,
            "moves": game.moveHistory,
            "final": snapshot(game.state),
        }
        results.append(row)
        print(json.dumps({key: value for key, value in row.items()
                          if key not in ("trace", "moves", "final")}))
    report = {
        "config": {
            "layout": args.layout, "agent": "ExpectimaxAgent", "evalFn": "better",
            "depth": args.depth, "ghosts": "2 RandomGhost", "games": args.games,
            "seed": args.seed, "graphics": False,
            "python": sys.version,
            "source_sha256": hashlib.sha256((PROJECT / "multiAgents.py").read_bytes()).hexdigest(),
        },
        "results": results,
    }
    destination.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print("TRACE:", destination.resolve())


if __name__ == "__main__":
    main()
