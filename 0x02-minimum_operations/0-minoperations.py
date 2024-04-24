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
    if n == 0:
        return 0

    dp = [float('inf')] * (n + 1)
    dp[1] = 0

    for i in range(2, n + 1):
        for j in range(1, i):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + i // j)

    return dp[n] if dp[n] != float('inf') else 0
