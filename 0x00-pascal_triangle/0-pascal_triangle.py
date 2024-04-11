#!/usr/bin/python3
"""This module returns a list of lists of integers representing
the Pascal’s triangle of n.
"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the nth row.

    Parameters:
    - n (int): The number of rows to generate in Pascal's triangle.

    Returns:
    - list of lists of integers: A list representing Pascal's triangle up to
      the nth row. Each inner list represents a row of Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)

    return triangle
