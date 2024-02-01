"""
Distinct Subsequences
https://leetcode.com/problems/distinct-subsequences/
"""


def numDistinctMemo(s: str, t: str) -> None:
    m, n = len(t), len(s)
    dp = [[-1] * m for _ in range(n)]

    def solve(i, j):
        if j < 0:
            return 1
        if i < 0:
            return 0
        if dp[i][j] == -1:
            dp[i][j] = solve(i - 1, j)
            if s[i] == t[j]:
                dp[i][j] += solve(i - 1, j - 1)
        return dp[i][j]

    res = solve(n - 1, m - 1)
    print(res)


def numDistinctTab(s: str, t: str) -> None:
    m, n = len(t), len(s)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(0, n + 1):
        dp[i][0] = 1
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            dp[i][j] = dp[i - 1][j]
            if s[i - 1] == t[j - 1]:
                dp[i][j] += dp[i - 1][j - 1]

