from DP.LCS.lcs import lcs
'''
longest palindromic subsequence
'''

def lps(s):
    s1, s2 = s, s[::-1]
    print(res := lcs(s1, s2))
    return res