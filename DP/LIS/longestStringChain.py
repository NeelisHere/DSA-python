from typing import *


def longestStrChain(words: List[str]) -> int:
    res = 1
    words.sort(key=len)
    dp = {w: 1 for w in words}
    for w in words[1:]:
        for i in range(len(w)):
            t = w[:i] + w[i + 1:]
            if t in dp:
                dp[w] = max(dp[w], 1 + dp[t])
        res = max(res, dp[w])
    return res
