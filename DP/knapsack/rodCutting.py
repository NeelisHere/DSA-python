
def cutRod(price, n):
    price = [-1] + price
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            dp[i][j] = dp[i - 1][j]
            if j - i >= 0:
                dp[i][j] = max(dp[i][j], price[i] + dp[i][j - i])

    return dp[n][n]
