from collections import *

def bfs(g):
    n = len(g)
    res = []
    q = deque()
    v = [False for _ in range(n)]
    
    q.append(0)
    v[0] = True
    
    while q:
        curr = q.popleft()
        res.append(curr)
        for nbr in g[curr]:
            if not v[nbr]:
                v[nbr] = True
                q.append(nbr)
            
    print(res)