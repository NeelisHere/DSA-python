def longesSubstringWithoutRepeatingChars(s):
    t={}
    l, r, ans = 0, 0, 0
    while r < len(s):
        c = s[r]
        t[c] = t[c] + 1 if c in t else 1
        while t[c] > 1:
            t[s[l]] -= 1
            l += 1
        ans = max(ans, r-l+1)
        r += 1
    print(ans)