'''
Max time to buy and sell stocks with cooldown period of time = 1 day
'''

def memo(prices):
    n = len(prices)
    dp = [[-1 for _ in range(2)] for _ in range(n)]
    def solve(i, canBuy):
        if i >= n: return 0
        if dp[i][canBuy] == -1:
            op1 = op2 = None
            if canBuy:
                op1 = -prices[i] + solve(i+1, False)
                op2 = solve(i+1, True)
            else:
                op1 = prices[i] + solve(i+2, True)
                op2 = solve(i+1, False)
            dp[i][canBuy] = max(op1, op2)
        # return profit
        return dp[i][canBuy]
        
    ans = solve(0, True)
    print(ans)