from typing import List


def countPartitions(n: int, d: int, a: List[int]) -> None:
    a.sort(reverse=True)
    s, k = sum(a), sum(a) // 2
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(1, n + 1):
        for j in range(k + 1):
            if j == 0:
                dp[i][j] = 1
            else:
                x = a[i - 1]
                dp[i][j] = dp[i - 1][j]
                if j - x >= 0:
                    dp[i][j] += dp[i - 1][j - x]

    count = 0
    for target in range(k + 1):
        if dp[n][target]:
            s1 = target if target > (s - target) else (s - target)
            if (2 * s1 - s) == d:
                count += dp[n][target]

    print(count)

