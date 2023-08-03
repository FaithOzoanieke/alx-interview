#!/usr/bin/env python3
import sys

def is_safe(board, row, col):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i] == col:
            return False

        # Check diagonals
        if abs(board[i] - col) == abs(i - row):
            return False
    return True

def nqueens_util(board, row):
    N = len(board)

    # If all queens are placed, print the solution
    if row == N:
        print([[i, board[i]] for i in range(N)])
        return

    for col in range(N):
        if is_safe(board, row, col):
            board[row] = col
            nqueens_util(board, row + 1)

def nqueens(N):
    if not isinstance(N, int):
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * N
    nqueens_util(board, 0)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        nqueens(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
