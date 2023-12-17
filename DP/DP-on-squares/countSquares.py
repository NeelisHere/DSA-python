'''
Count Square Submatrices with All Ones
'''

def solve(A):
    rows, cols = len(A), len(A[0])
    for i in range(1, rows):
        for j in range(1, cols):
            if A[i][j]: 
                A[i][j] = min(A[i-1][j-1], A[i][j-1], A[i-1][j]) + 1
    ans = sum([x for row in A for x in row])
    print(ans)