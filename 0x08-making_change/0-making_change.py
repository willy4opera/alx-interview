#!/usr/bin/python3

'''The Change making function.
'''


def makeChange(coins, total):
    '''least number of coin needed to meet a coin amount
    '''
    if total <= 0:
        return 0
    remainz = total
    coins_count = 0
    coin_idx = 0
    sorted_coins = sorted(coins, reverse=True)
    n = len(coins)
    while remainz > 0:
        if coin_idx >= n:
            return -1
        if remainz - sorted_coins[coin_idx] >= 0:
            remainz -= sorted_coins[coin_idx]
            coins_count += 1
        else:
            coin_idx += 1
    return coins_count
