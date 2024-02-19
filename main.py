T = int(input())

for _ in range(T):
    l, r = list(map(int, input().split()))
    a, b = -1, -1
    if l * 2 <= r:
        a, b = l, l * 2
    print(f'{a} {b}')

