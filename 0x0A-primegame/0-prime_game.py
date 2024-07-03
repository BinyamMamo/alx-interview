#!/usr/bin/python3
"""
0. Prime Game

simulate multiple rounds of the prime
game and determine the overall winner
"""


def sieve(n):
    """
    Generate a list of primes up to
    n using the Sieve of Eratosthenes
    """
    is_prime = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    primes = [p for p in range(2, n + 1) if is_prime[p]]
    return primes


def isWinner(x, nums):
    """
    Determine the winner of the prime game
    played with numbers from 1 to x, given nums
    """
    if not nums or x < 1:
        return None

    max_n = max(nums)
    primes = sieve(max_n)

    winner_cache = {}

    def determine_winner(n):
        """
        Determine the winner for
        a game with numbers 1 to n
        """
        if n in winner_cache:
            return winner_cache[n]

        nums_set = set(range(1, n + 1))
        turn = 'Maria'

        while True:
            prime_found = False
            for prime in primes:
                if prime in nums_set:
                    prime_found = True
                    break

            if not prime_found:
                winner = 'Ben' if turn == 'Maria' else 'Maria'
                winner_cache[n] = winner
                return winner

            for multiple in range(prime, n + 1, prime):
                if multiple in nums_set:
                    nums_set.remove(multiple)

            turn = 'Ben' if turn == 'Maria' else 'Maria'

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = determine_winner(n)
        if winner == 'Maria':
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    else:
        return None
