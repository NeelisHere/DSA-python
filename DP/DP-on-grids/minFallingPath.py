from copy import deepcopy
from typing import *
"""
Min Falling Path: https://leetcode.com/problems/minimum-falling-path-sum/
"""


def minFallingPathSum(grid: List[List[int]]):
    dp = deepcopy(grid)
    rows, cols = len(grid), len(grid[0])
    for i in range(1, rows):
        for j in range(cols):
            if j == 0:
                dp[i][j] += min(dp[i - 1][j], dp[i - 1][j + 1])
            elif j == cols - 1:
                dp[i][j] += min(dp[i - 1][j], dp[i - 1][j - 1])
            else:
                dp[i][j] += min(dp[i - 1][j], dp[i - 1][j - 1], dp[i - 1][j + 1])
    res = min(dp[-1])
    print(res)
