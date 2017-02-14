import json

"""
Task：PermMissingElem
Find the missing element in a given permutation.
－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－
A zero-indexed array A consisting of N different integers is given.
The array contains integers in the range [1..(N + 1)],
which means that exactly one element is missing.

Your goal is to find that missing element.

Write a function:

	def solution(A)

that, given a zero-indexed array A, returns the value of the missing element.

For example, given array A such that:

  A[0] = 2
  A[1] = 3
  A[2] = 1
  A[3] = 5

the function should return 4, as it is the missing element.
"""

A = [2, 3, 1, 5]

"""
使用 N+1 階三角範圍來取值
"""
def solutionByScope(A):
	total = 0
	scope = float((len(A) + 1)) * float((len(A) + 2)) / 2
	for value in A:
		total += value
	return (int)(scope - total)

print(solutionByScope(A))