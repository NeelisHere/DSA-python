from typing import List
"""
Print LIS: https://www.codingninjas.com/studio/problems/printing-longest-increasing-subsequence_8360670
"""


def printLIS(a: List[int], n: int) -> List[int]:
    dp = [1 for _ in range(n)]
    prev = [-1 for _ in range(n)]
    for i in range(1, n):
        for j in range(i):
            if a[j] < a[i]:
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    prev[i] = j
    maxLen = max(dp)
    res = []
    for i in range(n - 1, -1, -1):
        if dp[i] == maxLen:
            curr = i
            while curr != -1:
                res.append(curr)
                curr = prev[curr]
            break
    res = list(map(lambda index: a[index], res))[::-1]
    return res
