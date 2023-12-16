def solve(a):
    n = len(a)
    if a == sorted(a, reverse=True):
        a.sort()
        return 
    i = n-1
    while i > 0:
        if a[i-1] < a[i]:
            j = n-1
            while a[j] <= a[i-1]: 
                j -= 1
            a[i-1], a[j] = a[j], a[i-1]
            a[i:] = sorted(a[i:])
            break
        i -= 1