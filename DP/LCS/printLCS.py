from typing import *

def findLCS(n: int, m: int, s1: str, s2: str) -> str:
    
    dp = [[0]*(m + 1) for _ in range(n + 1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if s1[i-1] == s2[j-1]: dp[i][j] = dp[i-1][j-1] + 1
            else: dp[i][j] = max(dp[i][j-1], dp[i-1][j])
    
    i, j = n, m
    res = ''
    while i > 0 and j > 0:
        if dp[i][j] > max(dp[i-1][j], dp[i][j-1]):
            res += s1[i-1]
            i, j = i-1, j-1
        else:
            if dp[i][j] == dp[i-1][j]: i -= 1
            elif dp[i][j] == dp[i][j-1]: j -= 1

    res = res[-1::-1]
    print(res)