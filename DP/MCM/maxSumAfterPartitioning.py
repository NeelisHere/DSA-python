'''
Partition Array for Maximum Sum
https://leetcode.com/problems/partition-array-for-maximum-sum/
'''

def maxSumAfterPartitioning(a, k):
    n = len(a)
    INT_MIN = float('-inf')
    dp = [-1]*n

    def solve(index):
        if index == n: return 0
        if dp[index] == -1:
            maxi = res = INT_MIN
            length = 0
            for i in range(index, min(n, index + k)):
                length += 1
                maxi = max(maxi, a[i])
                temp = length*maxi + solve(i + 1)
                res = max(res, temp)
            dp[index] = res
        return dp[index]
    
    res = solve(0)
    print(res)