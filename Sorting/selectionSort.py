def selectionSort(arr):
    for i in range(len(arr)):
        for j in range(i+1):
            k = j
            while k>0:
                if arr[k-1]>arr[k]:
                    arr[k], arr[k-1] = arr[k-1], arr[k]
                k -= 1