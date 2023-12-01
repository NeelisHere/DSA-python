def partition(l, r, arr):
    pivot = arr[r]
    p = l - 1
    # p => all the values located up till p have value <= pivot
    for i in range(l, r):
        if arr[i] <= pivot:
            p += 1
            arr[i], arr[p] = arr[p], arr[i]
    arr[p + 1], arr[r] = arr[r], arr[p + 1]
    return p + 1

def quickSort(l, r, arr):
    if l<r:
        i = partition(l, r, arr)
        quickSort(l, i-1, arr)
        quickSort(i+1, r, arr)