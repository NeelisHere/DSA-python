def subarrayWithAtmostKDistinct(arr, k):
    t={}
    res = i = j = 0
    while i < len(arr):
        x = arr[i]
        t[x] = t.get(x, 0) + 1    
        while len(t) > k:
            y = arr[j]
            t[y] -= 1
            if t[y] == 0: del t[y]
            j += 1
        res += i - j + 1
        i += 1
    return res

def subarrayWithKDistinct(arr, k):
    res = subarrayWithAtmostKDistinct(arr, k) - subarrayWithAtmostKDistinct(arr, k - 1)
    print(res)