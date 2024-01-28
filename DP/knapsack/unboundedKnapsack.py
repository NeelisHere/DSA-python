from typing import List
import sys


def unboundedKnapsackMemo(n: int, w: int, profit: List[int], wt: List[int]) -> int:
    dp = [[-1] * (w + 1) for _ in range(n + 1)]

    def solve(i, w):
        if i == 0:
            return int(w // wt[i]) * profit[i]
        if dp[i][w] == -1:
            op1 = -sys.maxsize
            if w - wt[i] >= 0:
                op1 = profit[i] + solve(i, w - wt[i])
            op2 = solve(i - 1, w)
            dp[i][w] = max(op1, op2)
        return dp[i][w]
    return solve(n - 1, w)


def unboundedKnapsackTab(n: int, w: int, profit: List[int], wt: List[int]) -> int:
    dp = [[0] * (w + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, w + 1):
            dp[i][j] = dp[i - 1][j]
            if j - wt[i - 1] >= 0:
                dp[i][j] = max(dp[i][j], profit[i - 1] + dp[i][j - wt[i - 1]])

    return dp[n][w]
