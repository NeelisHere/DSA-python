from typing import *
"""
Largest Divisible Subset: https://leetcode.com/problems/largest-divisible-subset/description/
"""


def largestDivisibleSubsequence(arr: List[int]) -> List[int]:
    n = len(arr)
    arr.sort()
    sol = [[a] for a in arr]
    for i in range(1, n):
        for j in range(i):
            if arr[i] % arr[j] == 0 and len(sol[i]) < len(sol[j]) + 1:
                sol[i] = sol[j] + [arr[i]]
    return max(sol, key=len)
