def jobScheduling(jobs):
    jobs = sorted(jobs, key=lambda job: job[2], reverse=True)
    maxDeadline = max(list(map(lambda job: job[1], jobs)))
    res = [None]*(maxDeadline + 1)
    for job in jobs:
        _, deadline, _ = job
        for i in range(deadline, 0, -1):
            if res[i] is None:
                res[i] = job
                break
    res = res[1:]
    print(res)