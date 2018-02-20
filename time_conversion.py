#!/bin/python3

import sys

def timeConversion(s):
    ar = list(map(int, s[:8].strip().split(':')))
    hourAdd = 0
    
    if s[8:] == 'AM' and ar[0] == 12:
        ar[0] = 0
    
    if s[8:] == 'PM' and ar[0] < 12:
        ar[0] += 12
    
    if s[8:] == 'PM' and ar[0] == 12:
        ar[0] = 12
    
    return "{0:02d}:{1:02d}:{2:02d}".format(ar[0]+hourAdd, ar[1], ar[2])

s = input().strip()
result = timeConversion(s)
print(result)
