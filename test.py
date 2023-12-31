# from graphs.detectCycleUndir import detectCycleUndir
# from DP.MCM import mcm
# from DP.LCS.lcs import lcs
# from DP.LCS.lps import lps
from DP.LCS.printLCS import printLCS

# g = {
#     1: [2, 3, 4],
#     2: [1, 3],
#     3: [1, 2],
#     4: [1]
# }

# detectCycleUndir(g)

# a = [10, 20, 30, 40, 50]
# mcm.minOperations(a)

# lcs('breakfast', 'deadbeat')
printLCS('bbabcbcab', 'bbabcbcab'[::-1])

    
