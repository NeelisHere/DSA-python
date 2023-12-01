def maximumMeetings(meetings):
    prev = meetings[0]
    res = [prev]
    for i in range(1, len(meetings)):
        x, y = meetings[i]
        if prev[1] < x: 
            res.append([x, y])
            prev = meetings[i]
        else: 
            continue
    print(res)