'''
https://leetcode.com/problems/burst-balloons/submissions/
'''

def maxCoins(a):
    a = [1] + a + [1]
    n = len(a)
    dp = [[-1]*(n+1) for _ in range(n+1)]

    def solve(i, j):
        if j - i < 2: return 0
        if dp[i][j] == -1:
            res = 0
            for k in range(i+1, j):
                x = a[i]*a[k]*a[j] + solve(i, k) + solve(k, j)
                res = max(res, x)
            dp[i][j] = res
        return dp[i][j]

    res = solve(0, n-1)
    print(res)