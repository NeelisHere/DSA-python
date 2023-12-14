def fibonacci(x):
    n = 6
    dp = [-1] * (n + 1)
    def solve():
        if x <= 1:
            dp[x] = x 
            return dp[x]
        dp[x] = fibonacci(x-1) + fibonacci(x-2)
        return dp[x]
    
    print(solve(n))
    print(dp)