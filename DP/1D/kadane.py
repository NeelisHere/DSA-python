def kadane(arr):
    dp = [-1]*len(arr)
    if len(arr) == 0: return
    x = arr[0]
    dp[0] = x
    res = max(0, x)
    for i in range(1, len(arr)):
        x = x + arr[i] if x + arr[i] >= arr[i] else arr[i]
        dp[i], res = x, max(res, x)
    # print(dp)
    print(res)