def minEatingSpeed(piles, h):
    isFeasible = lambda x: bool(sum([p // x if p % x == 0 else p // x + 1 for p in piles]) <= h)

    l, r = 1, max(piles)
    while l < r:
        x = l + (r - l) // 2
        if isFeasible(x): r = x
        else: l = x + 1

    return l