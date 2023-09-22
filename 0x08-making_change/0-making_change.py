#!/usr/bin/env python3
from typing import List
"""
makeChange interview question task
"""

def makeChange(coins: List[int], total: int) -> int:
    """
    function that calculate the minimum coins needed
    to get the total value
    """
    coin_count = 0
    result = 0
    rem = total
    sorted_coins = sorted(coins, reverse=True)

    for coin in sorted_coins:
        if rem >= coin:
            times = rem // coin
            for _ in range(times):
                coin_count += 1
                result += coin
            rem -= coin * times
        if rem == 0:
            break
    
    if total > result:
        return -1
    
    return coin_count
    

            










