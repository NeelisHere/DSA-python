def houseRobber2(houses):
    n = len(houses)
    if n == 1:
        return houses[0]
    if n == 2:
        return max(houses[0], houses[1])

    def solve(a):
        dp = a.copy()
        if len(a) == 1:
            return dp[0]
        res = max(dp[0], dp[1])
        for i in range(2, len(a)):
            dp[i] = dp[i - 1]
            for j in range(i - 1):
                dp[i] = max(dp[i], a[i] + dp[j])
            res = max(res, dp[i])
        return res

    return max(solve(houses[:n - 1]), solve(houses[1:]))

