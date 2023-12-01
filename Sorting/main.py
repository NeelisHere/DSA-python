# from mergeSort import mergeSort
from quickSort import quickSort

if __name__ == "__main__":
    arr = [6,3,4,2,4,3,5]
    quickSort(0, len(arr)-1, arr)
    print(arr)
    