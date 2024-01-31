from DP.LCS.lcs import lcsTab
'''
Minimum Insertions/Deletions to Convert String A to String B
'''


def minOperations(s1, s2):
    k = lcsTab(s1, s2)
    res = (len(s1) - k) + (len(s2) - k)
    print(f'Min insertions/deletions to convert string {s1} to string {s2}: {res}')
    return res
