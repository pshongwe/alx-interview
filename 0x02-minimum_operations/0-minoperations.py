#!/usr/bin/python3
"""
0-minoperations.py
"""


def minOperations(n):
    """calculates the fewest number of operations needed to
    result in exactly n H characters in the file."""
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n = n // divisor
        divisor += 1

    return operations
