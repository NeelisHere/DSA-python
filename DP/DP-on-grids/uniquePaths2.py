"""
Unique Paths - 2: https://leetcode.com/problems/unique-paths-ii
"""
from typing import *


def uniquePathsWithObstacles(grid: List[List[int]]) -> None:
    rows, cols = len(grid), len(grid[0])
    dp = [[0] * cols for _ in range(rows)]
    if grid[0][0] == 0:
        dp[0][0] = 1
        for j in range(1, cols):
            if grid[0][j] == 1:
                break
            dp[0][j] = dp[0][j - 1]
        for i in range(1, rows):
            if grid[i][0] == 1:
                break
            dp[i][0] = dp[i - 1][0]
    for i in range(1, rows):
        for j in range(1, cols):
            if grid[i][j] == 0:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
            else:
                dp[i][j] = 0
    paths = dp[rows - 1][cols - 1]
    print(paths)

