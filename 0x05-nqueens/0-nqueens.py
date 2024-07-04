#!/usr/bin/python3
"""N Queens problem"""
import sys


def print_usage():
    """
    Prints the usage message and exits
    the program with status 1.
    """
    print("Usage: nqueens N")
    sys.exit(1)


def validate_input(args):
    """
    Validates the command line arguments.
    Args:
        args: List of command line arguments.
    Returns:
        N: The integer value of the argument if valid.
    Exits:
        If the number of arguments is incorrect.
        If N is not a valid integer.
        If N is less than 4.
    """
    if len(args) != 2:
        print_usage()
    try:
        N = int(args[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    return N


def is_safe(board, row, col):
    """
    Checks if a queen can be placed on board at (row, col).
    Args:
        board: The current state of the chessboard.
        row: The row index to check.
        col: The column index to check.
    Returns:
        True if it's safe to place the queen,
        False otherwise.
    """
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False
    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    # Check lower diagonal on left side
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True


def solve_nqueens_util(board, col, solutions):
    """
    Recursively solves the N queens problem using backtracking.
    Args:
        board: The current state of the chessboard.
        col: The current column index to place a queen.
        solutions: A list to store the valid solutions.
    Returns:
        True if a solution is found, False otherwise.
    """
    if col >= len(board):
        solution = []
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return True
    res = False
    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            res = solve_nqueens_util(board, col + 1, solutions) or res
            board[i][col] = 0
    return res


def solve_nqueens(N):
    """
    Initializes the chessboard and solves the N queens problem.
    Args:
        N: The size of the chessboard (N x N).
    Returns:
        A list of all possible solutions.
    """
    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []
    solve_nqueens_util(board, 0, solutions)
    return solutions


def main():
    """
    Main function to validate input, solve the N
    queens problem, and print solutions.
    """
    N = validate_input(sys.argv)
    solutions = solve_nqueens(N)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
