"""
cuts[] contains the length of cuts.
As long as length >= 0, keep cutting the rod with length cuts[i]
return max of the 2 answers:
- cut the rod with length cuts[i] and don't proceed to the next index
- proceed to the next index without cutting and return what answer we get

"""
import sys
from collections import defaultdict


def cutRod(price):
    n = len(price)
    profit = defaultdict(lambda: 0)
    for i, cost in enumerate(price, start=1):
        profit[i] = cost

    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        for j in range(n + 1):
            if i == 1:
                dp[i][j] = profit[i] * j
            else:
                op1 = dp[i - 1][j]
                op2 = -sys.maxsize
                if j - i >= 0:
                    op2 = profit[i] + dp[i][j - i]
                dp[i][j] = max(op1, op2)

    return dp[n][n]


def rodCuttingMemo(price):
    n = len(price)
    cuts = [i + 1 for i, _ in enumerate(price)]
    dp = [[-1] * (n + 1) for _ in range(n + 1)]

    def solve(i, length):
        if i < 0 or length < 0:
            return 0
        if dp[i][length] == -1:
            op1 = solve(i - 1, length)
            op2 = -sys.maxsize
            if length - cuts[i] >= 0:
                op2 = price[i] + solve(i, length - cuts[i])
            dp[i][length] = max(op1, op2)
        return dp[i][length]

    return solve(n - 1, n)
