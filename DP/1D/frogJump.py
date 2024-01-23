from collections import *


def frogJump(n, h):
    dp = [0] * n
    for i in range(1, n):
        if i - 2 >= 0:
            dp[i] = min(
                dp[i - 1] + abs(h[i - 1] - h[i]),
                dp[i - 2] + abs(h[i - 2] - h[i])
            )
        else:
            dp[i] = abs(h[i - 1] - h[i])
    print(dp)


def frogJumpRec(n, h):
    dp = defaultdict(lambda: -1)
    dp[0] = 0
    dp[1] = abs(h[0] - h[1])

    def solve(i):
        if dp[i] == -1:
            dp[i] = min(
                abs(h[i - 1] - h[i]) + solve(i - 1),
                abs(h[i - 2] - h[i]) + solve(i - 2)
            )
        return dp[i]

    res = solve(n - 1)
    print(res)
    
    