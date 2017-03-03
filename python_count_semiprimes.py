import json
from math import sqrt

"""
Task：CountSemiprimes
Count the semiprime numbers in the given range [a..b]
－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－
A prime is a positive integer X that has exactly two distinct divisors: 1 and X.
The first few prime integers are 2, 3, 5, 7, 11 and 13.

A semiprime is a natural number that is the product of two (not necessarily distinct) prime numbers.
The first few semiprimes are 4, 6, 9, 10, 14, 15, 21, 22, 25, 26.

You are given two non-empty zero-indexed arrays P and Q, each consisting of M integers.
These arrays represent queries about the number of semiprimes within specified ranges.

Query K requires you to find the number of semiprimes within the range (P[K], Q[K]),
where 1 ≤ P[K] ≤ Q[K] ≤ N.

For example, consider an integer N = 26 and arrays P, Q such that:

    P[0] = 1    Q[0] = 26
    P[1] = 4    Q[1] = 10
    P[2] = 16   Q[2] = 20

The number of semiprimes within each of these ranges is as follows:

(1, 26) is 10,
(4, 10) is 4,
(16, 20) is 0.

Write a function:

    def solution(N, P, Q)

that, given an integer N and two non-empty zero-indexed arrays P and Q consisting of M integers,
returns an array consisting of M elements specifying the consecutive answers to all the queries.

For example, given an integer N = 26 and arrays P, Q such that:

    P[0] = 1    Q[0] = 26
    P[1] = 4    Q[1] = 10
    P[2] = 16   Q[2] = 20

the function should return the values [10, 4, 0], as explained above.

Assume that:
    N is an integer within the range [1..50,000];
    M is an integer within the range [1..30,000];
    each element of arrays P, Q is an integer within the range [1..N];
    P[i] ≤ Q[i].
"""

N = 26
P = [1, 4, 16]
Q = [26, 10, 20]

"""
用半質數相乘取出結果
Correctness：100%、Performance：40%
"""
def solution(N, P, Q):
    S = [0] * (N+1)

    # 先取得半質數列表
    prime = [ p for p in  range(2, int(N / 2) + 1) if 0 not in [ p % d for d in range(2, int(sqrt(p))+1)] ]

    # 標註所有相乘結果
    for i in prime:
        for j in prime:
            k = i * j
            if k <= N:
                S[k] = 1

    # 取得範圍內有多少註記
    result = []
    for i in range(0, len(P)):
        result.append(len(list(filter(lambda x: x == 1, S[P[i]:Q[i]+1]))))

    return result

print(solution(N, P, Q))