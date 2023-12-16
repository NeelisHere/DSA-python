def maxTimeToBuyAndSellStocks2(prices):
    res = 0
    for i in range(len(prices)-1):
        if prices[i] < prices[i+1]:
            res += prices[i+1] - prices[i]
    return res