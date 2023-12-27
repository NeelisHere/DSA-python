from collections import *

def isCyclic(edges, v):
    visited = defaultdict(lambda: False)
    inStack = defaultdict(lambda: False)

    def dfs(curr):
        visited[curr] = True
        inStack[curr] = True
        for nbr in g[curr]:
            if not visited[nbr]:
                visited[nbr] = inStack[nbr] = True
                if dfs(nbr): return True
            else:
                if inStack[nbr]: return True
        inStack[curr] = False
        return False    

    def buildGraph(edges, v):
        g = [[] for _ in range(v)]
        for a, b in edges: g[a].append(b)
        return g
    
    g = buildGraph(edges, v)
    ans = False
    for i in range(v):
        if not visited[i]:
            if dfs(i): 
                ans = True
                break
            
    return ans