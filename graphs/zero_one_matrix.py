from collections import *

def updateMatrix(A):
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    v = [[False for _ in range(len(A[0]))] for _ in range(len(A))]
    res = [[0 for _ in range(len(A[0]))] for _ in range(len(A))]
    q = deque()
    
    def isValid(i, j):
        return bool(
            (i >= 0 and i<len(A)) and (j >= 0 and j<len(A[0]))
            and (v[i][j] == False)
        )

    for i in range(len(A)):
        for j in range(len(A[0])):
            if A[i][j] == 0: 
                v[i][j] = True
                q.append((0, (i, j)))
    
    while q:
        d, (i, j) = q.popleft()
        res[i][j] = d
        for m in moves:
            x, y = i + m[0], j + m[1]
            if isValid(x, y):
                v[x][y] = True
                q.append((d+1, (x, y)))
    
    print(res)