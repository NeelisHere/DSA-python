def longestCommonSubstringMemo(s1, s2):
    res = []

    def solve(i, j, count):
        if i < 0 or j < 0:
            return 0
        if s1[i] == s2[j]:
            return 1 + solve(i - 1, j - 1, count + 1)
        else:
            res.append(count)
            return max(count, solve(i - 1, j, 0), solve(i, j - 1, 0))

    solve(len(s1) - 1, len(s2) - 1, 0)
    ans = max(res)
    print(ans)


def longestCommonSubstringTab(s1: str, s2: str) -> int:
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    res = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            res = max(res, dp[i][j])
    return res
