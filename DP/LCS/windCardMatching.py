from typing import *

'''
https://leetcode.com/problems/wildcard-matching/
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:
    > '?' Matches any single character.
    > '*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).
'''


def wildCardMatching(s: str, p: str):
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
