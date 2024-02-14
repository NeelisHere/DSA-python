"""
CodeForces: Bit++
https://codeforces.com/problemset/problem/282/A
"""

# T = int(input())
T = 1

for _ in range(T):
    n = int(input())
    x = 0
    for _ in range(n):
        exp = input()
        exp = exp.split('X')
        if exp[0] == '++' or exp[-1] == '++':
            x += 1
        elif exp[0] == '--' or exp[-1] == '--':
            x -= 1
        # print(exp)
    print(x)
