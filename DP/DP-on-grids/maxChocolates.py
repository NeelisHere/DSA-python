from typing import *
"""
Pickup maximum no. of chocolates with Alice & Bob: https://www.codingninjas.com/studio/problems/chocolate-pickup_3125885
"""


def maximumChocolatesMemo(r: int, c: int, grid: List[List[int]]) -> int:
    moves = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]
    isInside = lambda i, j: bool((0 <= i < c) and (0 <= j < c))
    dp = [[[-1] * (c + 1) for _ in range(c + 1)] for _ in range(r + 1)]

    def solve(i, a, b):
        if i == r - 1:
            if a == b: return grid[i][a]
            else: return grid[i][a] + grid[i][b]
        if dp[i][a][b] == -1:
            ans = 0
            for move in moves:
                x, y = a + move[0], b + move[1]
                if isInside(x, y):
                    res = grid[i][a] + grid[i][b] + solve(i + 1, x, y)
                    if a == b: res -= grid[i][a]
                    ans = max(ans, res)
            dp[i][a][b] = ans
        return dp[i][a][b]

    return solve(0, 0, c - 1)


def maximumChocolates(grid: List[List[int]]):
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

