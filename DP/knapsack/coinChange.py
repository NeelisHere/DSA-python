from typing import *
import sys


def coinChange(coins: List[int], target: int) -> int:
    n = len(coins)
    dp = [[-1] * (target + 1) for _ in range(n + 1)]

    def solve(i, t):
        if t < 0 or i < 0: return sys.maxsize
        if t == 0: return 0
        if dp[i][t] == -1:
            op1 = solve(i - 1, t)
            op2 = 1 + solve(i, t - coins[i])
            dp[i][t] = min(op1, op2)
        return dp[i][t]

    res = solve(n - 1, target)
    return res if res != sys.maxsize else -1
