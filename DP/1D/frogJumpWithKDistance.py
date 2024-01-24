"""
Frog with k distance / Minimal Cost: https://www.codingninjas.com/studio/problems/minimal-cost_8180930
"""
from typing import *


def minimizeCost(k: int, a: List[int]) -> int:
    n = len(a)
    dp = [0] * n
    for i in range(1, n):
        res = float('inf')
        for j in range(1, k + 1):
            if i - j < 0:
                break
            res = min(res, dp[i - j] + abs(a[i] - a[i - j]))
        dp[i] = res
    return dp[n - 1]

