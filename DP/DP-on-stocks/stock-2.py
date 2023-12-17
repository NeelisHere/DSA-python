'''
Max time to buy and sell stocks 2
'''

# greedy method
def solve1(prices):
    res = 0
    for i in range(len(prices)-1):
        if prices[i] < prices[i+1]:
            res += prices[i+1] - prices[i]
    return res


# DP Memoization
def solve2(prices):
    n = len(prices)
    dp = [[-1 for _ in range(2)] for _ in range(n)]
    def solve(i, canBuy):
        if i == n: return 0
        if dp[i][canBuy] == -1:
            op1 = op2 = 0
            if canBuy:
                op1 = -prices[i] + solve(i+1, False)
                op2 = solve(i+1, True)
            else:
                op1 = prices[i] + solve(i+1, True)
                op2 = solve(i+1, False)
            dp[i][canBuy] = max(op1, op2)
        return dp[i][canBuy]
    return solve(0, True)


# tabulation
def solve3(prices):
    n = len(prices)
    dp = [[-1 for _ in range(2)] for _ in range(n+1)]
    dp[n][0] = dp[n][1] = 0
    for i in range(n-1, -1, -1):
        for canBuy in range(2):
            op1 = op2 = 0
            if canBuy:
                op1 = -prices[i] + dp[i+1][0]
                op2 = dp[i+1][1]
            else:
                op1 = prices[i] + dp[i+1][1]
                op2 = dp[i+1][0]
            dp[i][canBuy] = max(op1, op2)
    print(dp)
    return dp[0][1]


# tabulation + space-optimization
def solve4(prices):
    n = len(prices)
    ahead = curr = [0, 0]
    for i in range(n-1, -1, -1):
        for canBuy in range(2):
            op1 = op2 = 0
            if canBuy:
                op1 = -prices[i] + ahead[0]
                op2 = ahead[1]
            else:
                op1 = prices[i] + ahead[1]
                op2 = ahead[0]
            curr[canBuy] = max(op1, op2)
        ahead = curr
    print(ahead, curr)
    return curr[1]