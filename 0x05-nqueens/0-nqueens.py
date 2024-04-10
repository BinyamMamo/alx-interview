#!/usr/bin/python3
"""
Task 0. N queens -> # Interview Problem
Mission: Solve the N Queens problem of placing N queens on
an NxN chessboard such that no two queens attack each other

USAGE: ./0-nqueens.py N
"""
import sys


def solveNQueens(n):
    """
    Uses a backtracking algorithm to test
    each possible placement of queens.

    Args:
        n: The number of queens (or size of the board).

    Returns:
        A list of lists of integers representing
        valid placements of N queens on an NxN board
    """

    col = set()
    posDiag = set()
    negDiag = set()

    res = []
    board = [[". "] * n for _ in range(n)]

    def backtrack(r):
        """
        Recursive backtracking function to test each placement.
        """
        if r == n:
            pos = []
            for x in range(4):
                for y in range(n):
                    if board[x][y] == "Q":
                        pos.append([x, y])
            res.append(pos)
            return

        for c in range(n):
            if c in col or (r + c) in posDiag or (r - c) in negDiag:
                continue

            col.add(c)
            posDiag.add(r + c)
            negDiag.add(r - c)
            board[r][c] = "Q"

            backtrack(r + 1)

            col.remove(c)
            posDiag.remove(r + c)
            negDiag.remove(r - c)
            board[r][c] = "."

    backtrack(0)
    return res


if len(sys.argv) < 2:
    print("Usage: nqueens N")
    exit(1)
if not sys.argv[1].isnumeric():
    print("N must be a number")
    exit(1)

n = int(sys.argv[1])
if n < 4:
    print("N must be at least 4")
    exit(1)

for solution in solveNQueens(n):
    print(solution)
