import json
from itertools import groupby

"""
Task：EquiLeader
Find the index S such that the leaders of the sequences A[0], A[1], ...,
A[S] and A[S + 1], A[S + 2], ..., A[N - 1] are the same.
－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－
A non-empty zero-indexed array A consisting of N integers is given.

The leader of this array is the value that occurs in more than half of the elements of A.

An equi leader is an index S such that 0 ≤ S < N − 1 and two sequences
A[0], A[1], ..., A[S] and A[S + 1], A[S + 2], ..., A[N − 1] have leaders of the same value.

For example, given array A such that:

    A[0] = 4
    A[1] = 3
    A[2] = 4
    A[3] = 4
    A[4] = 4
    A[5] = 2

we can find two equi leaders:

0, because sequences: (4) and (3, 4, 4, 4, 2) have the same leader, whose value is 4.
2, because sequences: (4, 3, 4) and (4, 4, 2) have the same leader, whose value is 4.
The goal is to count the number of equi leaders.

Write a function:

	def solution(A)

that, given a non-empty zero-indexed array A consisting of N integers,
returns the number of equi leaders.

For example, given:

    A[0] = 4
    A[1] = 3
    A[2] = 4
    A[3] = 4
    A[4] = 4
    A[5] = 2

the function should return 2, as explained above.

Assume that:

	N is an integer within the range [1..100,000];
	each element of array A is an integer within the range [−1,000,000,000..1,000,000,000].
"""

A = [4, 3, 4, 4, 4, 2]

"""
先 groupby 再用 loop 的方式慢慢解
"""
def solution(A):
	d = dict()
	key = value = -1
	maxGroup = max(groupby(sorted(A)), key = lambda x: len(list(x[1])))
	key = maxGroup[0]
	value = len(list(filter(lambda x: x == key, A)))

	length = len(A)
	if value <= length / 2:
		return 0

	left = 0
	right = value
	count = 0
	for i in range(length):
		if A[i] == key:
			left  += 1
			right -= 1

		if left > (i+1) / 2 and right > (length - i - 1) / 2:
			count += 1

	return count

print(solution(A))