"""
https://leetcode.com/problems/wildcard-matching/
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:
    > '?' Matches any single character.
    > '*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).
"""


def wildCardMatchingMemo(s: str, p: str):
    dp = [[-1]*(len(p) + 1) for _ in range(len(s) + 1)]

    def solve(i, j):
        if i < 0 and j < 0:
            return True
        if j < 0 and i >= 0:
            return False
        if i < 0 and j >= 0: 
            if p[j] == '*':
                return list(p[:j+1]) == ['*']*(j + 1)
            else:
                return False
        if dp[i][j] == -1:
            if s[i] == p[j] or p[j] == '?':
                dp[i][j] = solve(i-1, j-1)
            elif p[j] == '*':
                dp[i][j] = solve(i-1, j) or solve(i, j-1)
            else:
                dp[i][j] = False
        return dp[i][j]
        
    res = solve(len(s)-1, len(p)-1)
    print(res)


def wildCardMatchingTab(s, p):
    m, n = len(p), len(s)
    dp = [[False] * (m + 1) for _ in range(n + 1)]

    dp[0][0] = True
    for j in range(1, m + 1):
        if p[j - 1] != '*':
            break
        dp[0][j] = True

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if p[j - 1] == '?' or s[i - 1] == p[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == '*':
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
