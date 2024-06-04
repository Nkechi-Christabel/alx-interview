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
        int: Fewest number of coins needed to meet total, or -1 if not
        possible.
    """
    if total <= 0:
        return 0

    else:
        coin = sorted(coins)
        coin.reverse()
        counter = 0
        for e in coin:
            while (total >= e):
                counter += 1
                total -= e
        if total == 0:
            return counter
        return -1
