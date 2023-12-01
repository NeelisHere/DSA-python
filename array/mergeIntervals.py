def mergeIntervals(intervals):
    intervals.sort()
    n = len(intervals)
    arr = []
    l, r = intervals[0]
    for i in range(1, n):
        x, y = intervals[i]
        if r >= x: r = max(r, y)
        else:
            arr.append([l, r])
            l, r = x, y
    arr.append([l, r])
    print(arr)