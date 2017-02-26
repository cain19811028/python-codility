import json
import math

"""
Task：CountFactors
Count factors of given number n.
－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－
A positive integer D is a factor of a positive integer N
if there exists an integer M such that N = D * M.

For example, 6 is a factor of 24, because M = 4 satisfies the above condition (24 = 6 * 4).

Write a function:

	def solution(N)

that, given a positive integer N, returns the number of its factors.

For example, given N = 24, the function should return 8,
because 24 has 8 factors, namely 1, 2, 3, 4, 6, 8, 12, 24. There are no other factors of 24.

Assume that:
	N is an integer within the range [1..2,147,483,647].
"""

N = 24

"""
用平方根的方式推算
Correctness：100%、Performance：100%
"""
def solutionBySqrt(N):
	result = 0
	squareRoot = math.sqrt(N)
	for index in range(1, math.ceil(squareRoot)):
		if N % index == 0:
			result += 2

	if squareRoot == math.ceil(squareRoot):
		result += 1

	return result

print(solutionBySqrt(N))

"""
用 lambda 寫法一行解決，可惜效能太差 ...
Correctness：100%、Performance：0%
"""
def solutionByLambda(N):
	return len(list(filter(lambda x: N % x == 0, range(1, N+1))))

print(solutionByLambda(N))