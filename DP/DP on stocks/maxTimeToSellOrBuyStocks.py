def solve(prices):
    bp = prices[0]
    res = 0
    for i in range(1, len(prices)):
        sp = prices[i]
        res = max(res, sp-bp)
        bp = min(bp, prices[i])
    return res