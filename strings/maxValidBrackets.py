from collections import deque

def maxLength(string):
        n = len(string)
        stack = deque()
        for i in range(n):
            s = string[i]
            if s == '(':
                stack.append((s, i))
            else:
                if stack and stack[-1][0] == '(': stack.pop()
                else: stack.append((s, i))
        
        prev, count = -1, 0
        for _, i in list(stack):
            count = max(count, (i-prev)-1)
            prev = i
        count = max(count, (n-prev)-1)
        return count