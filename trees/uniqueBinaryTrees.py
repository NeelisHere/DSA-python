
'''
using @cache/@lru_cache decorator takes up more space
'''
def uniqueBinaryTree(n):
    # cache = [-1]*(n + 1)
    # cache[0], cache[1], cache[2] = 1, 1, 2
    # def solve(n):
    #     if cache[n] != -1: return cache[n];
    #     cache[n] = 0
    #     for i in range(1, n+1):
    #         cache[n] += solve(i-1) * solve(n-i)
    #     return cache[n]
    
    cache = [-1]*(n + 1)
    if n <= 1: return 1
    cache[0], cache[1] = 1, 1
    def solve(n):
        if cache[n] == -1:
            cache[n] = sum(solve(i-1)*solve(n-i) for i in range(1, n+1))
        return cache[n]
    
    print(solve(n))
    
    