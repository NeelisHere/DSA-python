from typing import List


def minSubsetSumDifference(a: List[int], n: int) -> None:
    s = k = sum(a)
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        for j in range(k + 1):
            if j == 0:
                dp[i][j] = 1
            else:
                x = a[i - 1]
                dp[i][j] = dp[i - 1][j]
                if j - x >= 0:
                    dp[i][j] |= dp[i - 1][j - x]

    res = 10 ** 9
    for j in range(k + 1):
        if dp[n][j]:
            res = min(res, abs(s - 2 * j))

    print(res)
