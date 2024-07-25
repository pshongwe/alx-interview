#!/usr/bin/python3
"""
make change
"""


def makeChange(coins, total):
    """make change function"""
    if total <= 0:
        return 0
    coin_count = 0
    coins.sort(reverse=True)
    for coin in coins:
        if total == 0:
            break
        coin_count += total // coin
        total %= coin

    if total != 0:
        return -1
    return coin_count
