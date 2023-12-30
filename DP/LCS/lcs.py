
def lcs(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[-1]*(n + 1) for _ in range(m + 1)]
    
    def calc(i, j):
        if i<0 or j<0: return 0
        if dp[i][j] == -1:
            if s1[i] == s2[j]: dp[i][j] = 1 + lcs(i-1, j-1)
            else: dp[i][j] = max(lcs(i-1, j), lcs(i, j-1))
        return dp[i][j]
        
    res = calc(m-1, n-1)
    print(res)