#!/usr/bin/python3
"""
0. Island Perimeter

Create a function def island_perimeter(grid) that
returns the perimeter of the island described in grid
"""


def islandPerimeter(self, grid) -> int:
    """
    calculates the perimeter of the island by iterating through the grid.

    Args:
        grid (List[List[int]]): A 2D list representing the grid of the island.

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c]:
                perimeter += 4
                for j in (-1, 1):
                    if ((r + j in range(len(grid)) and grid[r + j][c]) or
                            (c + j in range(len(grid[0])) and grid[r][c + j])):
                        perimeter -= 1

    return perimeter
