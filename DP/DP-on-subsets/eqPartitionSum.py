from typing import *

'''
https://leetcode.com/problems/partition-equal-subset-sum/

> Partition Equal Subset Sum
Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.

'''

def canPartition(a: List[int]):
    s = sum(a)
    
    def solve(i, k):
        if k == 0: return True
        if i >= len(a): return False
        if dp[i][k] == -1:
            dp[i][k] = solve(i + 1, k)
            if k - a[i] >= 0:
                dp[i][k] |= solve(i + 1, k - a[i])
        return dp[i][k]
    
    res = None
    if s%2 == 1: res = False
    else:
        k = int(s/2)
        dp = [[-1]*(k + 1) for _ in range(len(a) + 1)]
        res = solve(0, k)
        
    print(res)