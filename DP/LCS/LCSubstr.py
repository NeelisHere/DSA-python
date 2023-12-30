from typing import *

def LCSubstr(s1: str, s2: str) -> int:
    n1, n2 = len(s1), len(s2)
    t = [[0]*(n2 + 1) for _ in range(n1 + 1)]
    res = 0
    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            if s1[i-1] == s2[j-1]:
                t[i][j] = 1 + t[i-1][j-1]
            res = max(res, t[i][j])
    
    print(res)