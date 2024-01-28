from typing import *


def countCoinsMemo(target: int, coins: List[int]):
    n = len(coins)
    dp = [[-1] * (target + 1) for _ in range(n + 1)]

    def solve(i, t):
        if i < 0 or t < 0: return 0
        if t == 0: return 1
        if dp[i][t] == -1:
            op1 = solve(i - 1, t)
            op2 = solve(i, t - coins[i])
            dp[i][t] = op1 + op2
        return dp[i][t]

    res = solve(n - 1, target)
    print(res)
