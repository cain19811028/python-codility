import json

"""
Task：PermCheck
Check whether array A is a permutation.
－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－
A non-empty zero-indexed array A consisting of N integers is given.

A permutation is a sequence containing each element from 1 to N once, and only once.

For example, array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2

is a permutation, but array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3

is not a permutation, because value 2 is missing.

The goal is to check whether array A is a permutation.

Write a function:

	int solution(int A[], int N);

that, given a zero-indexed array A,
returns 1 if array A is a permutation and 0 if it is not.

For example, given array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2

the function should return 1.

Given array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3

the function should return 0.
"""

A = [4, 1, 3]

"""
使用 set 判斷長度是否一致的簡易方式
"""
def solutionBySet(A):
	S = set(A)
	return 1 if max(S) == len(S) and len(S) == len(A) else 0;

print(solutionBySet(A))