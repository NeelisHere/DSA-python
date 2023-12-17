'''
Max time to buy and sell stocks 3
'''

def memo(prices):
    n = len(prices)
    k = 2
    dp = [[[-1 for _ in range(k+1)] for _ in range(2)] for _ in range(n)]
    def solve(i, canBuy, k):
        if i == len(prices) or k <= 0: return 0
        if dp[i][canBuy][k] == -1:
            op1 = op2 = None
            if canBuy:
                op1 = -prices[i] + solve(i+1, False, k)
                op2 = solve(i+1, True, k)
            else:
                op1 = prices[i] + solve(i+1, True, k-1)
                op2 = solve(i+1, False, k)
            dp[i][canBuy][k] = max(op1, op2)
        # print(profit)
        return dp[i][canBuy][k]
    
    res = solve(0, True, k)
    print(res) 