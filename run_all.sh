#!/usr/bin/env bash
# run_all.sh - chay autograder cho Pac-Man AI Projects (Nhom 3)
#
# Cach dung (chay tu thu muc goc cua repo):
#   ./run_all.sh              chay tat ca: Project1 roi Project2
#   ./run_all.sh 1            chay toan bo Project1
#   ./run_all.sh 2            chay toan bo Project2
#   ./run_all.sh 1 q1         chay Project1, rieng cau q1
#   ./run_all.sh 2 q3         chay Project2, rieng cau q3
#
# Script chi goi autograder.py, khong sua autograder.py hay test_cases/.
# Log day du duoc luu o logs/ (da them vao .gitignore neu can).

set -u

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LOG_DIR="$ROOT_DIR/logs"
mkdir -p "$LOG_DIR"

# Chon lenh python
if command -v python3 >/dev/null 2>&1; then
    PY=python3
elif command -v python >/dev/null 2>&1; then
    PY=python
else
    echo "Khong tim thay python. Hay cai Python 3.6+." >&2
    exit 1
fi

PROJECT="${1:-all}"
QUESTION="${2:-}"

run_project() {
    local num="$1"
    local dir="$ROOT_DIR/Project$num"
    local log="$LOG_DIR/project${num}${QUESTION:+_$QUESTION}.log"

    if [ ! -d "$dir" ]; then
        echo "Khong thay thu muc $dir" >&2
        return 1
    fi

    echo "=============================================="
    echo " PROJECT $num ${QUESTION:+- cau $QUESTION}"
    echo "=============================================="

    cd "$dir" || return 1

    local args=(--no-graphics)
    if [ -n "$QUESTION" ]; then
        args+=(-q "$QUESTION")
    fi

    "$PY" autograder.py "${args[@]}" 2>&1 | tee "$log"

    echo
    echo "--- Tom tat Project $num ---"
    # In phan tong ket diem cua autograder
    sed -n '/Provisional grades/,/^Total:/p' "$log"
    echo "(Log day du: $log)"
    echo

    cd "$ROOT_DIR" || return 1
}

case "$PROJECT" in
    1|2)
        run_project "$PROJECT"
        ;;
    all)
        if [ -n "$QUESTION" ]; then
            echo "Muon chay mot cau thi hay chi ro project, vi du: ./run_all.sh 1 q1" >&2
            exit 1
        fi
        run_project 1
        run_project 2
        ;;
    *)
        echo "Tham so khong hop le: $PROJECT" >&2
        echo "Dung: ./run_all.sh [1|2] [qN]" >&2
        exit 1
        ;;
esac
