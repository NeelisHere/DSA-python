from typing import *


def knapsackMemo(n, wt, cost, capacity):
    dp = [[-1] * (capacity + 1) for _ in range(n + 1)]

    def solve(i, w):
        if i == 0:
            return int(bool(wt[i] <= w)) * cost[i]
        if dp[i][w] == -1:
            res = solve(i - 1, w)
            if w - wt[i] >= 0:
                res = max(res, cost[i] + solve(i - 1, w - wt[i]))
            dp[i][w] = res
        return dp[i][w]

    return solve(n - 1, capacity)


def knapsackTab(n: int, wt: List[int], cost: List[int], capacity):
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, capacity + 1):
            dp[i][j] = dp[i - 1][j]
            if j - wt[i - 1] >= 0:
                dp[i][j] = max(dp[i][j], cost[i - 1] + dp[i - 1][j - wt[i - 1]])
    res = dp[n][capacity]
    print(res)
    

