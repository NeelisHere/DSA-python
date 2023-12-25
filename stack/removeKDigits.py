from collections import *

def removeKdigits(a, k):
    s = deque()
    for x in a:
        while s and s[-1] > x and k:
            k -= 1
            s.pop()
        else: s.append(x)
    while s and k:
        s.pop()
        k -= 1
    while s and s[0] == '0': s.popleft()
    ans = None
    if len(s) == 0: ans = '0'
    else: ans = ''.join(list(s))
    print(ans)