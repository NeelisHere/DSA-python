'''
max time to buy or sell stock with transaction time
'''

def memo(prices, fee):
    n = len(prices)
    dp = [[-1 for _ in range(2)] for _ in range(n)]
    def solve(i, canBuy):
        if i >= n: return 0
        if dp[i][canBuy] == -1:
            op1 = op2 = 0
            if canBuy:
                op1 = -prices[i] + solve(i+1, False)
                op2 = solve(i+1, True)
            else:
                op1 = prices[i] + solve(i+1, True) - fee
                op2 = solve(i+1, False)
            dp[i][canBuy] = max(op1, op2)
        return dp[i][canBuy]
    res = solve(0, True)
    print(res)