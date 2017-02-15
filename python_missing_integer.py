import json

"""
Task：MissingInteger
Find the minimal positive integer not occurring in a given sequence.
－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－
Write a function:

	def solution(A)

that, given a non-empty zero-indexed array A of N integers,
returns the minimal positive integer (greater than 0) that does not occur in A.

For example, given:

  A[0] = 1
  A[1] = 3
  A[2] = 6
  A[3] = 4
  A[4] = 1
  A[5] = 2

the function should return 5.
"""

A = [1, 3, 6, 4, 1, 2]

"""
使用 in set 判斷內容值的簡易方式
"""
def solutionByInSet(A):
	result = 1
	s = set(A)
	while result in s:
		result += 1
	return result

print(solutionByInSet(A))