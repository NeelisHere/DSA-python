# number of subarrays in the array with sum=k
def numSubarraySum(a, k):
    s, count = 0, 0
    t = { 0: 1 }
    for i in range(len(a)):
        s += a[i]
        if s-k in t: count += t[s-k]
        t[s] = t[s] + 1 if s in t else 1
    print(count)