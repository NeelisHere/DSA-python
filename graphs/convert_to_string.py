import heapq as minHeap
from collections import defaultdict

'''
https://leetcode.com/contest/weekly-contest-377/problems/minimum-cost-to-convert-string-i/
'''


def build_graph(original, changed, costs):
    g = defaultdict(lambda: defaultdict(lambda: float('inf')))
    for u, v, cost in zip(original, changed, costs):
        g[u][v] = min(g[u][v], cost)
    return g

           
def dijkstra(g, src, end):
    d = defaultdict(lambda: float('inf'))
    pq = []
    minHeap.heappush(pq, (0, src))
    d[src] = 0
    while pq:
        curr_dist, curr = minHeap.heappop(pq)
        for nbr, dist in g[curr].items():
            new_dist = curr_dist + dist
            if d[nbr] > new_dist:
                d[nbr] = new_dist
                minHeap.heappush(pq, (new_dist, nbr))
    return d[end]

         
def minimumCost(source, target, original, changed, costs):
    g = build_graph(original, changed, costs)
    dp = {}
    ans = 0
    for s, t in zip(source, target):
        if s!= t:
            if (s, t) in dp:
                x = dp[(s, t)]
            else:
                x = dijkstra(g, s, t)
                dp[(s, t)] = x
            if x == float('inf'): return -1
            ans += x
    return ans