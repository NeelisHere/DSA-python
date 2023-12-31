from typing import *

def shortestCommonSupersequence(s1: str, s2: str):
    n1, n2 = len(s1), len(s2)
    dp = [[0]*(n2 + 1) for _ in range(n1 + 1)]

    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            if s1[i-1] == s2[j-1]: dp[i][j] = 1 + dp[i-1][j-1]
            else: dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    i, j = n1, n2
    res = ''
    
    while i >= 1 or j >= 1:
        if dp[i][j] > max(dp[i-1][j], dp[i][j-1]):
            res += s1[i-1]
            i, j = i-1, j-1
        else:
            if dp[i][j] == dp[i][j-1]:
                res += s2[j-1]
                j -= 1
            elif dp[i][j] == dp[i-1][j]:
                res += s1[i-1]
                i -= 1
                
    res = res[::-1]
    print(res)