#!/usr/bin/python3
# 101-nqueens.py
# tonybnya
"""
The N queens puzzle is the challenge of placing N non-attacking queens on
an NxN chessboard.
Write a program that solves the N queens problem.
"""
import sys


def nqueens():
    """
    Solves the N queens puzzle
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    arg = sys.argv[1]
    if not arg.isdigit():
        print("N must be a number")
        sys.exit(1)

    N = int(arg)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)


if __name__ == '__main__':
    nqueens()
