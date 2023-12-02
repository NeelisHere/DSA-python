def findStart(arr):
    print(__name__)
    l, r = 0, len(arr)-1
    while l < r:
        mid = (l + r)//2
        if arr[mid] > arr[r]: l = mid + 1
        else: r = mid
    print(f'index: {r}, value: {arr[r]}')
