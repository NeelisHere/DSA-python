"""
Ninja's Training: https://www.codingninjas.com/studio/problems/ninja%E2%80%99s-training_3621003
"""
from typing import *
from copy import deepcopy


def ninjaTrainingRec(a: List[List[int]]) -> None:
    n: int = len(a)
    dp: List[List[int]] = [[-1] * 3 for _ in range(n + 1)]

    def solve(index: int, prev: int) -> int:
        if index >= n:
            return 0
        if dp[index][prev] == -1:
            res = 0
            for i in range(3):
                if i != prev:
                    res = max(res, a[index][i] + solve(index + 1, i))
            dp[index][prev] = res
        return dp[index][prev]
    x, y, z = a[0]
    ans: int = max(x + solve(1, 0), y + solve(1, 1), z + solve(1, 2))
    print(ans)


def ninjaTrainingTab(a: List[List[int]]) -> None:
    n: int = len(a)
    dp: List[List[int]] = deepcopy(a)
    for i in range(1, n):
        for j in range(3):
            res = 0
            for k in range(3):
                if k != j:
                    res = max(res, dp[i - 1][k])
            dp[i][j] = res + a[i][j]
    ans = max(dp[-1])
    print(ans)

