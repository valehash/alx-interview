#!/usr/bin/python3
"""Island perimeter interview question"""


def island_perimeter(grid):
    """fucntion to find the perimeter of a grid"""
    perimeter = 0
    rows, cols = len(grid), len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4

                # Check left neighbor
                if j > 0 and grid[i][j-1] == 1:
                    perimeter -= 2

                # Check top neighbor
                if i > 0 and grid[i-1][j] == 1:
                    perimeter -= 2

    return perimeter
