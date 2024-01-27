from typing import *


def findWays(a: List[int], k: int) -> int:
    dp = [[-1] * (k + 1) for _ in range(len(a))]

    def solve(i, k):
        if k < 0:
            return 0
        if i >= len(a):
            return int(k == 0)
        if dp[i][k] == -1:
            dp[i][k] = solve(i + 1, k - a[i]) + solve(i + 1, k)
        return dp[i][k]

    return solve(0, k)
