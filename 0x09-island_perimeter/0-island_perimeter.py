#!/usr/bin/python3

"""
A module that returns the perimeter of the island described in grid
"""


def island_perimeter(grid):
    perimeter = 0

    """
    This function calculate the perimeter of an insland
    """

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                perimeter += 4

                if i > 0:
                    if grid[i - 1][j] == 1:
                        perimeter -= 1

                if i < len(grid) - 1:
                    if grid[i + 1][j] == 1:
                        perimeter -= 1

                if j > 0:
                    if grid[i][j-1] == 1:
                        perimeter -= 1

                if j < len(grid[0]) - 1:
                    if grid[i][j + 1] == 1:
                        perimeter -= 1

    return perimeter

