from typing import *

'''
https://leetcode.com/problems/edit-distance/
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2. 
You have the following three operations permitted on a word:
    > Insert a character
    > Delete a character
    > Replace a character
'''


def minDistanceMemo(s1: str, s2: str):
    n1, n2 = len(s1), len(s2)
    dp = [[-1] * n2 for _ in range(n1)]

    def solve(i, j):
        if i >= n1:
            return n2 - j
        if j >= n2:
            return n1 - i
        if dp[i][j] == -1:
            if s1[i] == s2[j]:
                dp[i][j] = solve(i+1, j+1)
            else:
                _ins = solve(i, j+1)
                _del = solve(i+1, j)
                _rep = solve(i+1, j+1)
                dp[i][j] = 1 + min(_ins, _del, _rep)
        return dp[i][j]

    res = solve(0, 0)
    print(res)


def minDistanceTab(s1, s2):
    n1, n2 = len(s1), len(s2)
    dp = [[-1] * (n2 + 1) for _ in range(n1 + 1)]

    for i in range(n1 + 1):
        dp[i][0] = i

    for j in range(n2 + 1):
        dp[0][j] = j

    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],
                    dp[i][j - 1],
                    dp[i - 1][j - 1]
                )
    return dp[n1][n2]

