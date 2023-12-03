from collections import deque

def nextGreaterElementLR(arr):
    stack = deque()
    res = [-1]*len(arr)
    for i in range(len(arr)-1):
        if stack:
            while stack and stack[-1][1] < arr[i]:
                res[stack[-1][0]] = (stack[-1][1], (i, arr[i]))
                stack.pop()
        stack.append((i, arr[i]))
    print(res)

def nextGreaterElementRL(arr):
    stack = deque()
    res = [-1]*len(arr)
    for i in range(len(arr)-1, -1, -1):
        if stack:
            while stack and stack[-1][1] < arr[i]:
                res[stack[-1][0]] = (stack[-1][1], (i, arr[i]))
                stack.pop()
        stack.append((i, arr[i]))
    print(res)

def nextSmallerElementLR(arr):
    stack = deque()
    res = [-1]*len(arr)
    for i in range(len(arr)-1):
        if stack:
            while stack and stack[-1][1] > arr[i]:
                res[stack[-1][0]] = (stack[-1][1], (i, arr[i]))
                stack.pop()
        stack.append((i, arr[i]))
    print(res)

def nextSmallerElementRL(arr):
    stack = deque()
    res = [-1]*len(arr)
    for i in range(len(arr)-1, -1, -1):
        if stack:
            while stack and stack[-1][1] > arr[i]:
                res[stack[-1][0]] = (stack[-1][1], (i, arr[i]))
                stack.pop()
        stack.append((i, arr[i]))
    print(res)