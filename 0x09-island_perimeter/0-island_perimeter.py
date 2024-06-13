#!/usr/bin/python3
"""
This module contains a function def island_perimeter(grid): that returns the
perimeter of the island described in grid.
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in grid.

    Args:
        grid (list of list of int): A 2D grid where 0 represents water and 1
        represents land.

    Returns:
        int: The perimeter of the island.
    """
    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                # Each land cell has initially 4 sides
                perimeter += 4

                # Subtract sides shared with adjacent land cells
                if r > 0 and grid[r-1][c] == 1:  # Up
                    perimeter -= 2
                if c > 0 and grid[r][c-1] == 1:  # Left
                    perimeter -= 2

    return perimeter
