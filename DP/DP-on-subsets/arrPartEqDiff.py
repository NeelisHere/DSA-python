'''
Array partition with minimum difference
https://www.codingninjas.com/studio/problems/partition-a-set-into-two-subsets-such-that-the-difference-of-subset-sums-is-minimum._842494?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTabValue=PROBLEM

You are given an array 'arr' containing 'n' non-negative integers.
Your task is to partition this array into two subsets such that the absolute difference between subset sums is minimum. You just need to find the minimum absolute difference considering any valid division of the array elements.
'''


from typing import List

def minSubsetSumDifference(a: List[str], n: int) -> int:
    s = sum(a)
    dp = [([1]+[0]*s) for _ in range(n)]
    if a[0] <= s: dp[0][a[0]] = True

    for i in range(1, n):
        for j in range(1, s + 1):
            dp[i][j] = dp[i-1][j]
            if j - a[i] >= 0:
                dp[i][j] |= dp[i - 1][j - a[i]]
            
    res = float('inf')
    for i in range(1, s+1):
        if dp[n-1][i] == 1:
            res = min(res, abs(2*i - s))
            
    print(res)