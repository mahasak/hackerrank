#!/bin/python3

import sys

def birthdayCakeCandles(n, ar):
    ar.sort(reverse=True)
    m = max(ar)
    count = 0
    for i in ar:
        if i == m:
            count += 1
        else:
            break;
    return count
    # Complete this function

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(n, ar)
print(result)
