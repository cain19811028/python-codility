import json
import math

"""
Task：CountDiv
Compute number of integers divisible by k in range [a..b].
－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－
Write a function:

def solution(A, B, K)
that, given three integers A, B and K,
returns the number of integers within the range [A..B] that are divisible by K, i.e.:

    { i : A ≤ i ≤ B, i mod K = 0 }

For example, for A = 6, B = 11 and K = 2, your function should return 3,
because there are three numbers divisible by 2 within the range [6..11], namely 6, 8 and 10.
"""

A = 6
B = 11
K = 2

"""
使用 math.floor 的簡易方法
"""
def solutionByFloor(A, B, K):
    return int((math.floor(B / K) - math.floor((A - 1) / K)))

print(solutionByFloor(A, B, K))