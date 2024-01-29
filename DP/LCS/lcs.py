
def lcsMemo(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[-1]*(n + 1) for _ in range(m + 1)]
    
    def solve(i, j):
        if i < 0 or j < 0:
            return 0
        if dp[i][j] == -1:
            if s1[i] == s2[j]:
                dp[i][j] = 1 + solve(i-1, j-1)
            else:
                dp[i][j] = max(solve(i-1, j), solve(i, j-1))
        return dp[i][j]
    print(res := solve(m-1, n-1))


def lcsTab(s1: str, s2: str):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                
        