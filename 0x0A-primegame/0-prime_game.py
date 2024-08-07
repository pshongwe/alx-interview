#!/usr/bin/python3
"""prime game"""


def isWinner(x, nums):
    """is winner"""
    if x < 1 or not nums:
        return None

    def sieve_of_eratosthenes(max_n):
        """sieve of eratosthenes"""
        is_prime = [True] * (max_n + 1)
        is_prime[0] = is_prime[1] = False
        for start in range(2, int(max_n**0.5) + 1):
            if is_prime[start]:
                for multiple in range(start*start, max_n + 1, start):
                    is_prime[multiple] = False
        primes = [num for num, prime in enumerate(is_prime) if prime]
        return primes

    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if n == 1:
            ben_wins += 1
            continue

        moves = 0
        multiples_removed = [False] * (n + 1)

        for prime in primes:
            if prime > n:
                break
            if not multiples_removed[prime]:
                moves += 1
                for multiple in range(prime, n + 1, prime):
                    multiples_removed[multiple] = True

        if moves % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
