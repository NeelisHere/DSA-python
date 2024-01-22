def minDays(a, m, k):
    n = len(a)
    if n < m * k: return -1

    def isFeasible(x):
        prefix = [1 if val <= x else 0 for val in a]
        for i in range(1, n): prefix[i] += prefix[i - 1]
        l, count = -1, 0
        while l + k < n:
            r = l + k
            curr_window_size = prefix[r] if (l == -1) else (prefix[r] - prefix[l])
            if curr_window_size == k:
                count += 1
                l = r
            else:
                l += 1
        return bool(count >= m)

    l, r = min(a), max(a)
    while l < r:
        x = l + (r - l) // 2
        if isFeasible(x):
            r = x
        else:
            l = x + 1
    return l