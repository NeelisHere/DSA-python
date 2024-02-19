"""
D. Divisible Pairs
CodeForces Contest - 925 (div-3)
"""

from collections import *
from math import *
import sys

isEven = lambda x: bool(x & 1 == 0)
max_bits = lambda n: ceil(log2(n + 1))
get_bit = lambda n, i: 1 if (n & (1 << i)) else 0
get_mid = lambda l, r: l + (r - l) >> 1
logyn = lambda x: print('YES' if x else 'NO')
logcp = lambda arr: print(' '.join([str(x) for x in arr]))
inp_list = lambda: list(map(int, input().strip().split()))
M = 10 ** 9 + 7
N = 10 ** 6
inf = sys.maxsize


def solve(*args):
    arr, n, x, y = args
    t = defaultdict(lambda: 0)
    a, b = [(val % x) for val in arr], [(val % y) for val in arr]
    count = 0
    for i in range(n):
        p1, p2 = ((x - a[i]) % x, b[i]), (a[i], b[i])
        if t[p1]:
            count += t[p1]
        t[p2] += 1
    return count


T = int(input())

for _ in range(T):
    n, x, y = inp_list()
    a = inp_list()
    res = solve(a, n, x, y)
    print(res)



