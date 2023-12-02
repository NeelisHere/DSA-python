def findPeak(arr):
    print(__name__)
    l, r, ans = 0, len(arr)-1, 0
    while l < r:
        mid = (r + l)//2
        if arr[mid - 1] < arr[mid] and arr[mid] < arr[mid + 1]: ans = l = mid + 1 
        elif arr[mid - 1] > arr[mid] and arr[mid] > arr[mid + 1]: ans = r = mid - 1 
        elif arr[mid - 1] < arr[mid] and arr[mid] > arr[mid + 1]: 
            ans = mid
            break
        else: ans = l = mid + 1 
        
    print(f'index: {ans}, value: {arr[ans]}')