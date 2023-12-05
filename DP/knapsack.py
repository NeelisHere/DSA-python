def knapsack(profit, weight, capacity):
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
    