from collections import *

# g = defaultdict(lambda:[])

def n_connected_components(g):
    n = len(g)
    v = [False for _ in range()]

    def dfs(curr):
        v[curr] = True
        for nbr in g[curr]:
            if v[nbr] == False:
                v[nbr] = True
                dfs(nbr)

    count = 0
    for e in range(n):
        if v[e] == False:
            dfs(e)
            count += 1
    
    print(count)