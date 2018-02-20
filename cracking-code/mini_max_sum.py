#!/bin/python3

import sys

def miniMaxSum(arr):
    arr.sort()
    print("{} {}".format(sum(arr[:4]), sum(arr[1:])))

if __name__ == "__main__":
    arr = list(map(int, input().strip().split(' ')))
    miniMaxSum(arr)
