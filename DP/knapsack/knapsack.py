def knapsackMemo(profit, weight, capacity):
    n = len(profit)
    dp = [[-1] * (capacity + 1) for _ in range(n + 1)]
    def solve(i, w):
        if i >= n or w >= capacity: 
            return 0
        if dp[i][w] != -1: 
            return dp[i][w]
        dp[i][w] = solve(i + 1, w) if w + weight[i] > capacity else max(
            profit[i] + solve(i + 1, w + weight[i]),
            solve(i + 1, w)
        )
        return dp[i][w]
    
    res = solve(0, 0)
    print(res)
    # print(dp)


def knapSackTabulation(W, wt, val, n):
    dp = [[0] * (W + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, W + 1):
            dp[i][j] = dp[i - 1][j]
            if j - wt[i - 1] >= 0:
                dp[i][j] = max(dp[i][j], val[i - 1] + dp[i - 1][j - wt[i - 1]])
    return dp[n][W]

