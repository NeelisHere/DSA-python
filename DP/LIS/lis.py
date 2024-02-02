from typing import *
from bisect import bisect_left


def memoLIS(a: List[int]) -> int:
    n = len(a)
    dp = [[-1] * (n + 1) for _ in range(n + 1)]

    def solve(curr, prev):
        if curr == n:
            return 0
        if dp[curr][prev] == -1:
            dp[curr][prev] = solve(curr + 1, prev)
            if prev == -1 or a[prev] < a[curr]:
                dp[curr][prev] = max(dp[curr][prev], 1 + solve(curr + 1, curr))
        return dp[curr][prev]

    return solve(0, -1)


def binarySearchLIS(a: List[int]) -> int:
    n = len(a)
    temp = [a[0]]
    for i in range(1, n):
        if a[i] > temp[-1]:
            temp.append(a[i])
        else:
            j = bisect_left(temp, a[i])
            temp[j] = a[i]
    return len(temp)


def tabularLIS(a: List[int]) -> int:
    n, res = len(a), 1
    dp = [1 for _ in range(n)]
    for curr in range(1, n):
        for prev in range(curr):
            if a[prev] < a[curr]:
                dp[curr] = max(dp[curr], dp[prev] + 1)
        res = max(res, dp[curr])
    return res
