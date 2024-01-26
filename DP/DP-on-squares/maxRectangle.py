from collections import deque


def nextSmaller(A):
    n = len(A)
    ns = [n for _ in A]
    stack = deque()
    for i in range(n):
        while stack and stack[-1][1] > A[i]:
            ns[stack[-1][0]] = i
            stack.pop()
        stack.append((i, A[i]))
    return ns


def prevSmaller(A):
    n = len(A)
    ps = [-1 for _ in A]
    stack = deque()
    for i in range(n-1, -1, -1):
        while stack and stack[-1][1] > A[i]:
            ps[stack[-1][0]] = i
            stack.pop()
        stack.append((i, A[i]))
    return ps


def largestHistogram(A):
    n, res = len(A), 0
    ns, ps = nextSmaller(A), prevSmaller(A)
    for i in range(n):
        res = max(res, (ns[i] - ps[i] - 1) * A[i])
    return res


def maximalRectangle(A):
    rows, cols = len(A), len(A[0])
    res = 0
    for i in range(rows):
        row = A[i]
        for j in range(cols):
            if i > 0: 
                if A[i][j] > 0: 
                    A[i][j] += A[i-1][j]
        # print(row)
        res = max(res, largestHistogram(row))
    print(res)
