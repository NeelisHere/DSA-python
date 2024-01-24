from copy import deepcopy
from typing import *
"""
Minimum Path Sum: https://leetcode.com/problems/minimum-path-sum/
"""


def minPathSum(grid: List[List[int]]) -> None:
    dp = deepcopy(grid)
    rows, cols = len(grid), len(grid[0])
    for j in range(1, cols):
        dp[0][j] += dp[0][j - 1]
    for i in range(1, rows):
        dp[i][0] += dp[i - 1][0]
    for i in range(1, rows):
        for j in range(1, cols):
            dp[i][j] += min(dp[i][j - 1], dp[i - 1][j])
    print(dp)

