from DP.LCS.lps import longestPalindromicSubseq
'''
Minimum insertions to make string palindrome
https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/
'''


def minInsertions(s):
    print(res := len(s) - longestPalindromicSubseq(s))
    return res
