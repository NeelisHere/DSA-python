def longestPalindrome(s):
    n = len(s)
    res = []
    def utils(s, l, r):
        while l >= 0 and r < n and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]
    
    def solve(s):
        for i in range(n):
            a, b = utils(s, i, i), utils(s, i, i+1)
            res.append((len(a), a))
            res.append((len(b), b))

    solve(s)
    res.sort(reverse=True)
    print(res)