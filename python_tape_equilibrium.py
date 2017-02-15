import json
import math
import sys

"""
Task：TapeEquilibrium
Minimize the value |(A[0] + ... + A[P-1]) - (A[P] + ... + A[N-1])|.
－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－
A non-empty zero-indexed array A consisting of N integers is given.
Array A represents numbers on a tape.

Any integer P, such that 0 < P < N, splits this tape into two non-empty parts:
A[0], A[1], ..., A[P − 1] and A[P], A[P + 1], ..., A[N − 1].

The difference between the two parts is the value of:
|(A[0] + A[1] + ... + A[P − 1]) − (A[P] + A[P + 1] + ... + A[N − 1])|

In other words, it is the absolute difference between the sum of the first part and the sum of the second part.

For example, consider array A such that:

  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3

We can split this tape in four places:

P = 1, difference = |3 − 10| = 7
P = 2, difference = |4 − 9| = 5
P = 3, difference = |6 − 7| = 1
P = 4, difference = |10 − 3| = 7

Write a function:

	def solution(A)

that, given a non-empty zero-indexed array A of N integers,
returns the minimal difference that can be achieved.

For example, given:

  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3

the function should return 1, as explained above.
"""

A = [3, 1, 2, 4, 3]

"""
使用遞減後取最小值的簡易方式
"""
def solution(A):
	total = sum(A)
	result = sys.maxsize
	for i in range(0, len(A)):
		total -= A[i] * 2
		result = min(result, math.fabs(total))
	return int(result)

print(solution(A))