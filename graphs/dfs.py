def dfs(g):
    g = [[2,3,1] , [0], [0,4], [0], [2]]
    edges = len(g)
    v = [False for _ in range(edges)]
    res = []
    def dfsUtils(curr):
        res.append(curr)
        v[curr] = True
        for nbr in g[curr]:
            if not v[nbr]: dfsUtils(nbr)
    
    dfsUtils(0)
    print(res)