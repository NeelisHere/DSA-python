from collections import *

'''
detect cycle in an undirected graph
'''

def detectCycleUndir(g):
    def dfs(p, curr):
        v[curr] = True
        for nbr in g[curr]:
            if v[nbr] == False:
                if dfs(curr, nbr): return True
            else:
                if nbr != p: return True
        return False
        
    def bfs(i):
        q = deque()
        q.append((-1, i))
        v[i] = True
        while q:
            parent, curr = q.popleft()
            for nbr in g[curr]:
                if v[nbr] == False:
                    v[nbr] = True
                    q.append((curr, nbr))
                else:
                    if parent != nbr: return True
        return False
    
    v = defaultdict(lambda: False)
    edges = list(g.keys())
    isCycle = False
    for i in edges:
        if not v[i]: isCycle |= bfs(i)
            
    print(isCycle)