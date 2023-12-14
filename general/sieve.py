def seive(n):
    primes = [0]*(n+1)
    i = 2
    while i * i <= n:
        if primes[i] == 0:
            for j in range(i * i, n + 1, i):
                primes[j] = 1
        i += 1
    return primes