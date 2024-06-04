#!/usr/bin/python3
"""
The script determines the fewest number of coins needed to meet a
given amount total.
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given total.
    
    Args:
        coins (list of int): List of coin values.
        total (int): The total amount to be met.
    
    Returns:
        int: Fewest number of coins needed to meet total, or -1 if not possible.
    """
    if total <= 0:
        return 0

    # Initialize the dp array with a large number
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for x in range(coin, total + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
