def subsetSumToK(k, a):
    dp = [[-1]*(k + 1) for _ in range(len(a) + 1)]
    
    def solve(i, k):
        if k == 0: return 1
        if i >= len(a): return 0
        if dp[i][k] == -1:
            dp[i][k] = solve(i+1, k)
            if k - a[i] >= 0:
                dp[i][k] += solve(i+1, k-a[i])
        return dp[i][k]
    
    res = solve(0, k)
    print(res)