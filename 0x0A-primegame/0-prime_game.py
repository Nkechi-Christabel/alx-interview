#!/usr/bin/python3
"""
The challenge involves determining the winner of a game based on the
strategic removal of prime numbers and their multiples from a set of
consecutive integers.
"""


def isWinner(x, nums):
    """
    Determine the winner of the most rounds between Maria and Ben.

    Args:
        x (int): Number of rounds.
        nums (list of int): List of n values for each round.

    Returns:
        str: Name of the player with the most wins or None if a winner cannot
             be determined.
    """
    if x <= 0 or not nums:
        return None

    # Find the maximum value in nums to limit the sieve
    max_n = max(nums)

    # Generate prime numbers up to max_n using Sieve of Eratosthenes
    sieve = [True] * (max_n + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not primes
    for start in range(2, int(max_n**0.5) + 1):
        if sieve[start]:
            for multiple in range(start*start, max_n + 1, start):
                sieve[multiple] = False

    primes = [num for num, is_prime in enumerate(sieve) if is_prime]

    def count_primes_up_to(n):
        """ Count number of primes up to n using precomputed sieve. """
        return sum(1 for i in range(n + 1) if sieve[i])

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        prime_count = count_primes_up_to(n)
        # If the number of primes up to n is odd, Maria wins, else Ben wins
        if prime_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
