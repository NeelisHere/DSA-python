'''
Max time to buy and sell stocks 4
'''

def memo(prices, k):
    n = len(prices)
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
    

def tab(prices, k):
    n = len(prices)
    dp = [[[0 for _ in range(k+1)] for _ in range(2)] for _ in range(n+1)]
    for i in range(n-1, -1, -1):
        for canBuy in range(2):
            for x in range(1, k+1):
                op1 = op2 = None
                if canBuy:
                    op1 = -prices[i] + dp[i+1][0][x]
                    op2 = dp[i+1][1][x]
                else:
                    op1 = prices[i] + dp[i+1][1][x-1]
                    op2 = dp[i+1][0][x]
                dp[i][canBuy][x] = max(op1, op2)
    ans = dp[0][1][k]
    print(ans)


def tabOpt(prices, k):
    n = len(prices)
    next = curr = [[0 for _ in range(k+1)] for _ in range(2)]
    for i in range(n-1, -1, -1):
        for canBuy in range(2):
            for x in range(1, k+1):
                op1 = op2 = None
                if canBuy:
                    op1 = -prices[i] + next[0][x]
                    op2 = next[1][x]
                else:
                    op1 = prices[i] + next[1][x-1]
                    op2 = next[0][x]
                curr[canBuy][x] = max(op1, op2)
        next = curr
    ans = curr[1][k]
    print(ans)