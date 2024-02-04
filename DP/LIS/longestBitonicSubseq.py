from typing import List
from bisect import *
"""
Longest String Chain: https://www.codingninjas.com/studio/problems/longest-bitonic-sequence_1062688
"""


def LIS(arr):
    temp, res = [], []
    for a in arr:
        i = bisect_left(temp, a)
        if i == len(temp):
            temp.append(a)
        else:
            temp[i] = a
        res.append(len(temp))
    return res


def longestBitonicSubseq(arr: List[int], n: int) -> int:
    a = LIS(arr)
    b = LIS(arr[::-1])[::-1]
    return max([a[i] + b[i] - 1 for i in range(n)])
