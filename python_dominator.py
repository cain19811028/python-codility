import json
from itertools import groupby

"""
Task：Dominator
Find an index of an array such that its value occurs at more than half of indices in the array.
－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－
A zero-indexed array A consisting of N integers is given.
The dominator of array A is the value that occurs in more than half of the elements of A.

For example, consider array A such that

	A[0] = 3    A[1] = 4    A[2] =  3
	A[3] = 2    A[4] = 3    A[5] = -1
	A[6] = 3    A[7] = 3

The dominator of A is 3 because it occurs in 5 out of 8 elements of A
(namely in those with indices 0, 2, 4, 6 and 7) and 5 is more than a half of 8.

Write a function

	def solution(A)

that, given a zero-indexed array A consisting of N integers,
returns index of any element of array A in which the dominator of A occurs.
The function should return −1 if array A does not have a dominator.

Assume that:

	N is an integer within the range [0..100,000];
	each element of array A is an integer within the range [−2,147,483,648..2,147,483,647].
	For example, given array A such that

 	A[0] = 3    A[1] = 4    A[2] =  3
 	A[3] = 2    A[4] = 3    A[5] = -1
 	A[6] = 3    A[7] = 3

	the function may return 0, 2, 4, 6 or 7, as explained above.
"""

A1 = [3, 4, 3, 2, 3, -1, 3, 3]
A2 = [1, 2, 1]
A3 = [0, 0, 1, 1, 1]
A4 = [2147483647]

"""
使用 groupby 的方式再 loop 慢慢解
"""
def solution(A):

	if len(A) == 1:
		return 0

	dominator = -1
	dominatorCount = 0
	for k, v in groupby(sorted(A)):
		length = len(list(v))
		if(length > dominatorCount):
			dominator = k
			dominatorCount = length

	if dominator == -1:
		return -1

	index = -1
	for i in range(0, len(A) - 1):
		if(A[i] == dominator):
			if(i == 0 or A[i] == A[i+1]):
				index = i

	return index if(dominatorCount > (len(A) / 2)) else -1

print(solution(A1))
print(solution(A2))
print(solution(A3))
print(solution(A4))