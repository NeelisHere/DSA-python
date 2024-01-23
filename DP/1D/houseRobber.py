from collections import *


def robHouseRec(a):
    dp = defaultdict(lambda: -1)

    def solve(i):
        if i >= len(a): return 0
        if dp[i] == -1:
            op1 = a[i] + solve(i + 2)
            op2 = solve(i + 1)
            dp[i] = max(op1, op2)
        return dp[i]
    return solve(0)


def robHouseTab(a):
    dp = a.copy()
    n = len(a)
    if n == 1:
        return dp[0]
    res = max(dp[0], dp[1])
    for i in range(2, n):
        dp[i] = dp[i - 1]
        for j in range(i - 1):
            dp[i] = max(dp[i], a[i] + dp[j])
        res = max(res, dp[i])
    return res
