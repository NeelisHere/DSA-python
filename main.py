def isFeasible(x, window):
    res = [1 if val <= x else 0 for val in a]
    print(res)
    for i in range(1, len(res)):
        res[i] += res[i - 1]
    print(res)
    l = -1
    count = 0
    while l + window < len(res):
        r = l + window
        curr = res[r] if (l == -1) else (res[r] - res[l])
        print(f'l={l}, r={r}, window={window}, curr={curr}')
        if curr == window:
            count += 1
            l = r
        else:
            l += 1
    print(count)


a = [2, 4, 2, 6, 12, 5, 7]
x = 10
window = 2
isFeasible(x, window)

