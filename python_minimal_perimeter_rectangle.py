import json
import math

"""
Task：MinPerimeterRectangle
Find the minimal perimeter of any rectangle whose area equals N.
－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－
An integer N is given, representing the area of some rectangle.

The area of a rectangle whose sides are of length A and B is A * B, and the perimeter is 2 * (A + B).

The goal is to find the minimal perimeter of any rectangle whose area equals N.
The sides of this rectangle should be only integers.

For example, given integer N = 30, rectangles of area 30 are:

(1, 30), with a perimeter of 62,
(2, 15), with a perimeter of 34,
(3, 10), with a perimeter of 26,
(5, 6), with a perimeter of 22.

Write a function:

	def solution(N)

that, given an integer N, returns the minimal perimeter of any rectangle whose area is exactly equal to N.

For example, given an integer N = 30, the function should return 22, as explained above.

Assume that:

N is an integer within the range [1..1,000,000,000].
"""

N = 30

"""
用平方根的方式推算
Correctness：100%、Performance：100%
"""
def solutionBySqrt(N):
	squareRoot = math.sqrt(N)
	for index in range(math.ceil(squareRoot), 0, -1):
		if N % index == 0:
			return int(2 * (index + (N / index)))

	return -1

print(solutionBySqrt(N))