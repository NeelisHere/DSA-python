'''
Palindrome Partitioning II
https://leetcode.com/problems/palindrome-partitioning-ii/
'''


def minCut(s):
    n = len(s)
    MAX = float('inf')
    dp = [-1]*(n + 1)
    
    def calc(index):
        if index >= n: return 0
        if dp[index] == -1:
            res = MAX
            temp = ''
            for i in range(index, n):
                temp += s[i]
                if temp == temp[-1::-1]:
                    res = min(res, 1 + calc(i + 1))
            dp[index] = res
        return dp[index]
    
    ans = calc(0)-1
    print(ans)