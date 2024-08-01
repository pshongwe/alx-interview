#!/usr/bin/python3
"""
0-island_perimeter
"""


def island_perimeter(grid):
    """Computes the perimeter of an island with no lakes."""
    A = not isinstance(grid, list)
    B = not all(isinstance(row, list) for row in grid)

    if not grid or A or B:
        return 0

    rows, cols = len(grid), len(grid[0])
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4

                if i > 0 and grid[i-1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j-1] == 1:
                    perimeter -= 2

    return perimeter
