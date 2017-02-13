import json
import math

"""
Task：FrogJmp
Count minimal number of jumps from position X to Y.
－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－
A small frog wants to get to the other side of the road.
The frog is currently located at position X and wants to get to a position greater than or equal to Y.
The small frog always jumps a fixed distance, D.

Count the minimal number of jumps that the small frog must perform to reach its target.

Write a function:

	def solution(X, Y, D)

that, given three integers X, Y and D,
returns the minimal number of jumps from position X to a position equal to or greater than Y.

For example, given:

	X = 10
	Y = 85
	D = 30

the function should return 3, because the frog will be positioned as follows:

	after the first jump, at position 10 + 30 = 40
	after the second jump, at position 10 + 30 + 30 = 70
	after the third jump, at position 10 + 30 + 30 + 30 = 100
"""

X = 10
Y = 85
D = 30

"""
使用 math.ceil 的簡易方式
"""
def solutionByCeil(X, Y, D):
	return int(math.ceil((Y - X) / float(D)))

print(solutionByCeil(X, Y, D))

"""
使用餘數判斷回傳的結果
"""
def solutionByMod(X, Y, D):
	return (Y - X) / D if (Y - X) % D == 0 else ((Y - X) / D) + 1

print(solutionByMod(X, Y, D))