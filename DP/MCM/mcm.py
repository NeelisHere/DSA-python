
    
def minOperations(a):
    def calc(i, j):
        if i == j: return 0
        if dp[i][j] == -1:
            res = float('inf')
            for k in range(i, j):
                x = a[i-1] * a[k] * a[j] + calc(i, k) + calc(k+1, j)
                res = min(res, x)
            dp[i][j] = res
        return dp[i][j]
            
    i, j = 1, len(a) - 1
    n = len(a)
    dp = [[-1] * (n+1) for _ in range(n+1)]
    res = calc(i, j)
    print(res)
    