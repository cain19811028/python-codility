import json

"""
Task：CyclicRotation
Rotate an array to the right by a given number of steps.
－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－
A zero-indexed array A consisting of N integers is given.
Rotation of the array means that each element is shifted right by one index,
and the last element of the array is also moved to the first place.

For example, the rotation of array A = [3, 8, 9, 7, 6] is [6, 3, 8, 9, 7].
The goal is to rotate array A K times;
that is, each element of A will be shifted to the right by K indexes.

Write a function:

	def solution(A, K)

that, given a zero-indexed array A consisting of N integers and an integer K,
returns the array A rotated K times.

For example, given array A = [3, 8, 9, 7, 6] and K = 3,
the function should return [9, 7, 6, 3, 8].
"""

A = [3, 8, 9, 7, 6]
K = 3

"""
使用 pop & insert 的簡易方式
"""
def solutionByPop(A, K):
	if(K > 0 and len(A) > 1):
		for i in range(0, K):
			A.insert(0, A.pop())
	return A

print(solutionByPop(A, K))