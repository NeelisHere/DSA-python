from typing import *


def subsetSumMemo(a: List[int], k: int) -> int:
    dp = [[-1] * (k + 1) for _ in range(len(a))]

    def solve(i, k):
        if k < 0:
            return False
        if i >= len(a):
            return bool(k == 0)
        if dp[i][k] == -1:
            dp[i][k] = solve(i + 1, k - a[i]) or solve(i + 1, k)
        return dp[i][k]

    return solve(0, k)


def subsetSumTab(a: List[int], k: int, n: int) -> int:
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(1, n + 1):
        for j in range(k + 1):
            x = a[i - 1]
            dp[i][j] = dp[i - 1][j]
            if j - x >= 0:
                dp[i][j] |= dp[i - 1][j - x]

    return dp[n][k]
