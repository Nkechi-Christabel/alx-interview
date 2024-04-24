#!/usr/bin/python3
"""
This modules contains a method that calculates the fewest number of operations
needed to result in exactly n H characters in the file.
"""


def minOperations(n):
    """
    Calculate the fewest number of operations needed to result in exactly n H
    characters in the file.

    Parameters:
    - n (int): The target number of H characters.

    Returns:
    - int: The fewest number of operations needed to achieve exactly n H
           characters in the file.
      Returns 0 if n is impossible to achieve.
    """
    if n <= 1:
        return 0

    min_ops = 0
    factor = 2
    while n > 1:
        while n % factor == 0:
            min_ops += factor
            n //= factor
        factor += 1

    return min_ops
