import json

"""
Task：Triangle
Determine whether a triangle can be built from a given set of edges.
－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－
A zero-indexed array A consisting of N integers is given.
A triplet (P, Q, R) is triangular if 0 ≤ P < Q < R < N and:

A[P] + A[Q] > A[R],
A[Q] + A[R] > A[P],
A[R] + A[P] > A[Q].

For example, consider array A such that:

  A[0] = 10    A[1] = 2    A[2] = 5
  A[3] = 1     A[4] = 8    A[5] = 20

Triplet (0, 2, 4) is triangular.

Write a function:

  def solution(A)

that, given a zero-indexed array A consisting of N integers,
returns 1 if there exists a triangular triplet for this array and returns 0 otherwise.

For example, given array A such that:

  A[0] = 10    A[1] = 2    A[2] = 5
  A[3] = 1     A[4] = 8    A[5] = 20

the function should return 1, as explained above. Given array A such that:

  A[0] = 10    A[1] = 50    A[2] = 5
  A[3] = 1

the function should return 0.

Assume that:

N is an integer within the range [0..100,000];
each element of array A is an integer within the range [−2,147,483,648..2,147,483,647].
"""

A1 = [10, 2, 6, 1, 8, 20]
A2 = [10, 50, 5, 1]

"""
使用任兩邊大於第三邊的簡易判斷方法
Correctness：100%、Performance：100%
"""
def solution(A):
    A = sorted(A)
    for i in range(0, len(A)-2):
        if(A[i] + A[i+1] > A[i+2]):
            return 1
    return 0

print(solution(A1))
print(solution(A2))