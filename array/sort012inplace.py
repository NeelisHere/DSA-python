'''
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
You must solve this problem without using the library's sort function.
'''

def sort012inplace(arr):
    l, r, i = 0, len(arr)-1, 0
    while i <= r:
        if arr[i] == 0: 
            arr[i], arr[l] = arr[l], arr[i]
            l += 1
            i += 1
        elif arr[i] == 1: i += 1
        else: 
            arr[i], arr[r] = arr[r], arr[i]
            r -= 1