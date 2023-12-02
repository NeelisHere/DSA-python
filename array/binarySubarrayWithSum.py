def binarySubarrayWithSum(arr, k):
    s = count = 0
    t={ 0: 1 }
    for i in range(len(arr)):
        x = arr[i]
        s += x
        if s-k in t: count += t[s-k]
        t[s] = t[s] + 1 if s in t else 1
    print(__name__, count)
    