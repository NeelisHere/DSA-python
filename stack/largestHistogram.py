from collections import deque

def largestHistogram(heights):
    def nextSmaller(heights):
        n = len(heights)
        ns = [n for h in heights]
        stack = deque()
        for i in range(n):
            while stack and stack[-1][1] > heights[i]:
                ns[stack[-1][0]] = i
                stack.pop()
            stack.append((i, heights[i]))
        return ns

    def prevSmaller(heights):
        n = len(heights)
        ps = [-1 for h in heights]
        stack = deque()
        for i in range(n-1, -1, -1):
            while stack and stack[-1][1] > heights[i]:
                ps[stack[-1][0]] = i
                stack.pop()
            stack.append((i, heights[i]))
        return ps
    
    ns = nextSmaller(heights)
    ps = prevSmaller(heights)
    res = 0
    for i in range(len(heights)):
        res = max(res, (ns[i] - ps[i] - 1) * heights[i])
    
    print(res)