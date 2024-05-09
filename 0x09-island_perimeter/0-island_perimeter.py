#!/usr/bin/python3
"""
0. Island Perimeter

Create a function that returns the perimeter of an island, which
is represented by '1's (land) and surrounded by '0's (water).
"""


def island_perimeter(grid):
    """
    calculates the perimeter of the island by iterating through the grid.

    Args:
        grid (List[List[int]]): A 2D list representing the grid of the island.

    Returns:
        int: The perimeter of the island.
    """
    if type(grid) != list or not grid:
        return 0

    perimeter = 0
    rows, cols = len(grid), len(grid[0])
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                water_sides = 0
                if row == 0 or grid[row - 1][col] == 0:
                    water_sides += 1
                if row == rows - 1 or grid[row + 1][col] == 0:
                    water_sides += 1
                if col == 0 or grid[row][col - 1] == 0:
                    water_sides += 1
                if col == cols - 1 or grid[row][col + 1] == 0:
                    water_sides += 1
                perimeter += water_sides
    return perimeter
