#!/usr/bin/python3
"""
0. Rotate 2D Matrix
mandatory
Given an n x n 2D matrix, rotate it 90 degrees clockwise.
"""
def rotate_2d_matrix(matrix) -> None:
    """
    Rotates a 2D matrix 90 degrees clockwise in place
    """
    left, right = 0, len(matrix) - 1

    while left < right:
        for i in range(right - left):
            top, bottom = left, right
            topLeft = matrix[top][left + i]

            matrix[top][left + i] = matrix[bottom - i][left]
            matrix[bottom - i][left] = matrix[bottom][right - i]
            matrix[bottom][right - i] = matrix[top + i][right]
            matrix[top + i][right] = topLeft
        left += 1
        right -= 1
