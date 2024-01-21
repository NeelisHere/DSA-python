def shipWithinDays(weights, days):
    def isFeasible(x):
        curr, d = 0, 1
        for w in weights:
            curr += w
            if curr > x:
                curr, d = w, d + 1
        return bool(d <= days)

    l, r = max(weights), sum(weights)
    while l < r:
        x = l + (r - l) // 2
        if isFeasible(x):
            r = x
        else:
            l = x + 1

    return l
