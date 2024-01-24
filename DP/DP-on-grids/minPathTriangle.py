from copy import deepcopy
from typing import *
"""
Minimum Path in a Triangle Grid: https://leetcode.com/problems/triangle/
"""


def minimumTotal(t: List[List[int]]) -> None:
    dp = deepcopy(t)
    n = len(t)
    for i in range(1, n):
        cols = len(t[i])
        for j in range(cols):
            if j == 0:
                dp[i][j] += dp[i - 1][j]
            elif j == cols - 1:
                dp[i][j] += dp[i - 1][j - 1]
            else:
                dp[i][j] += min(dp[i - 1][j - 1], dp[i - 1][j])
    res = min(dp[-1])
    print(res)
