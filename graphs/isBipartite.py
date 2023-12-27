from collections import *

def isBipartite(g):
    def dfs(curr, col=True):
        v[curr] = True
        color[curr] = col
        for nbr in g[curr]:
            if not v[nbr]:
                v[nbr] = True
                color[nbr] = not col
                if not dfs(nbr, color[nbr]):
                    return False
            else:
                if color[nbr] == col:
                    return False
        return True

    def bfs(node):
        color[node] = True
        q = deque([(node, color[node])])
        v[node] = True
        while q:
            curr, col = q.popleft()
            for nbr in g[curr]:
                if not v[nbr]:
                    v[nbr] = True
                    color[nbr] = not col
                    q.append((nbr, color[nbr]))
                else:
                    if color[nbr] == col:
                        return False
        return True

    v = defaultdict(lambda: False)
    color = defaultdict(lambda: None)
    ans = True
    for i in range(len(g)):
        if not v[i]:
            # if not dfs(i): ans = False
            if not bfs(i): ans = False
    return ans