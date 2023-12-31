from DP.LCS.lps import lps
'''
Minimum insertions to make string palindrome
'''

def minInsertions(s):
    print(res := len(s) - lps(s))
    return res