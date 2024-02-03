from typing import *


def findNumberOfLIS(a: List[int]) -> int:
    n, maxVal = len(a), 1
    dp = [1 for _ in range(n)]
    dp_len = [1 for _ in range(n)]
    for curr in range(1, n):
        for prev in range(curr):
            if a[prev] < a[curr]:
                if dp[prev] + 1 > dp[curr]:
                    dp[curr] = dp[prev] + 1
                    dp_len[curr] = dp_len[prev]
                elif dp[prev] + 1 == dp[curr]:
                    dp_len[curr] += dp_len[prev]
        maxVal = max(maxVal, dp[curr])

    return sum([dp_len[i] if dp[i] == maxVal else 0 for i in range(n)])
