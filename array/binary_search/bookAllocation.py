def bookAllocation(arr, n, m):
    print(__name__)
    if m > n: return -1
    lo, hi, n, ans = 0, sum(arr), len(arr), 0
        
    def isPossible(target):
        s, count = 0, 1
        for i in range(len(arr)):
            val = arr[i]
            if arr[i] > target: return False
            if s + val > target:
                count += 1
                if count > m: return False
                s = val
            else: s += val
        return True

    while lo <= hi:
        mid = (lo + hi)//2
        if isPossible(mid): ans, hi = mid, mid - 1
        else: lo = mid + 1
    
    print(ans)

