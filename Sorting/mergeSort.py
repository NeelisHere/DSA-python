def merge(l, r, arr):
    i, j, k = 0, 0, 0
    while i<len(l) and j<len(r):
        if l[i]<=r[j]:
            arr[k]=l[i]
            i += 1
        else:
            arr[k]=r[j]
            j += 1
        k += 1
    while i<len(l):
        arr[k]=l[i]
        i+=1 
        k+=1 
    while j<len(r):
        arr[k]=r[j]
        j+=1 
        k+=1 
    print('SORTED: ', arr)
    
def mergeSort(arr):
    print(arr)
    if len(arr) > 1:
        mid = len(arr)//2
        l, r = arr[:mid], arr[mid:]
        mergeSort(l)
        mergeSort(r)
        merge(l, r, arr)