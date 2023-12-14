def twoSum(arr, target):
    t = {}
    for i in range(len(arr)):
        if target - arr[i] in t:
            print((arr[i], target - arr[i]))
        else:
            t[arr[i]] = True
    