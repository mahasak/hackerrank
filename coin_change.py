#!/bin/python3

import sys

def make_change(coins, n):
    ways = [1]+[0]*n
    for coin in coins:
        for i in range(coin, n+1):
            ways[i]+=ways[i-coin]
    return ways[n]


	
    

n,m = input().strip().split(' ')
n,m = [int(n),int(m)]
coins = [int(coins_temp) for coins_temp in input().strip().split(' ')]
print(make_change(coins, n))
