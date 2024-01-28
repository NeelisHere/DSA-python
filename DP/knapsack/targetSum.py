from typing import *
from collections import *
"""
Target Sum: https://leetcode.com/problems/target-sum/
"""


def findTargetSumWays(a: List[int], target: int) -> int:
    res = defaultdict(lambda: 0)
    n, s = len(a), sum(a)
    dp = [[0] * (s + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(1, n + 1):
        for j in range(s + 1):
            x = a[i - 1]
            dp[i][j] = dp[i - 1][j]
            if j - x >= 0:
                dp[i][j] += dp[i - 1][j - x]

    for t in range(s // 2 + 1):
        res[t - (s - t)] += dp[n][t]
        if t != (s - t):
            res[(s - t) - t] += dp[n][t]

    return res[target]
