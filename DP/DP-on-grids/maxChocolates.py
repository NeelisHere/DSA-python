from typing import *
"""
Pickup maximum no. of chocolates with Alice & Bob: https://www.codingninjas.com/studio/problems/chocolate-pickup_3125885
"""


def maxChocolatesMemo(m: int, n: int, grid: List[List[int]]):
    dp = [[[-1] * (n + 1) for _ in range(n + 1)] for _ in range(m + 1)]

    def isInside(a, b):
        bool(0 <= a < n and 0 <= b < n)

    def solve(i, a, b):
        if i == m - 1:
            if a == b:
                return grid[i][a]
            else:
                return grid[i][a] + grid[i][b]
        if dp[i][a][b] == -1:
            res = 0
            for ai in [-1, 0, 1]:
                for bi in [-1, 0, 1]:
                    x, y = a + ai, b + bi
                    if isInside(x, y):
                        if a == b:
                            res = max(res, grid[i][a] + solve(i + 1, x, y))
                        else:
                            res = max(res, grid[i][a] + grid[i][b] + solve(i + 1, x, y))
            dp[i][a][b] = res
        return dp[i][a][b]

    ans = solve(0, 0, n - 1)
    print(ans)


def maximumChocolates(m: int, n: int, grid: List[List[int]]):
    m, n = len(grid), len(grid[0])

    def isInside(a, b):
        bool(0 <= a < n and 0 <= b < n)

    dp = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(m)]
    for i in range(n):
        for j in range(n):
            dp[m - 1][i][j] = grid[m - 1][i]
            if i != j:
                dp[m - 1][i][j] += grid[m - 1][j]

    def findBestMove(i, a, b):
        res = 0
        for ai in [-1, 0, 1]:
            for bi in [-1, 0, 1]:
                x, y = a + ai, b + bi
                if isInside(x, y):
                    res = max(res, dp[i + 1][x][y])
        return res

    for i in range(m - 2, -1, -1):
        for a in range(n):
            for b in range(n):
                res = grid[i][a] + grid[i][b]
                if a == b:
                    res -= grid[i][a]
                res += findBestMove(i, a, b)
                dp[i][a][b] = res

    res = dp[0][0][n - 1]
    print(res)

