#!/usr/bin/python3
'''
Generates a Pascal's Triangle with `n` rows.
'''


def pascal_triangle(n):
    '''
    Returns the pascal triangle of size n
    '''
    triangle = []
    if type(n) is not int or n <= 0:
        return []
    for y in range(n):
        row = []
        for x in range(y + 1):
            if y == x or x == 0:
                row.append(1)
            else:
                row.append(triangle[y - 1][x] + triangle[y - 1][x - 1])
        if row:
            triangle.append(row)

    return triangle
