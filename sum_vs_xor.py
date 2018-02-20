#!/bin/python3

import sys

def solve(n):
    if n ==0:
        return 1
    
    binn = bin(n)[2:]
   
    return 2 ** len([b for b in binn if b == "0"])

n = int(input().strip())
result = solve(n)
print(result)
