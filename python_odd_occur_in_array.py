import json
from itertools import groupby

"""
Task：OddOccurrencesInArray
Find value that occurs in odd number of elements.
－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－
A non-empty zero-indexed array A consisting of N integers is given.
The array contains an odd number of elements,
and each element of the array can be paired with another element that has the same value,
except for one element that is left unpaired.

For example, in array A such that:

  A[0] = 9  A[1] = 3  A[2] = 9
  A[3] = 3  A[4] = 9  A[5] = 7
  A[6] = 9

the elements at indexes 0 and 2 have value 9,
the elements at indexes 1 and 3 have value 3,
the elements at indexes 4 and 6 have value 9,
the element at index 5 has value 7 and is unpaired.
Write a function:

	def solution(A)

that, given an array A consisting of N integers fulfilling the above conditions,
returns the value of the unpaired element.

For example, given array A such that:

  A[0] = 9  A[1] = 3  A[2] = 9
  A[3] = 3  A[4] = 9  A[5] = 7
  A[6] = 9

the function should return 7, as explained in the example above.
"""

A = [9, 3, 9, 3, 9, 7, 9]

"""
使用 XOR 的簡易方式
 0 ^ 9 => 0000 ^ 1001 => 1001 =>  9
 9 ^ 3 => 1001 ^ 0011 => 1010 => 10
10 ^ 9 => 1010 ^ 1001 => 0011 =>  3
 3 ^ 3 => 0011 ^ 0011 => 0000 =>  0
 0 ^ 9 => 0000 ^ 1001 => 1001 =>  9
 9 ^ 7 => 1001 ^ 0111 => 1110 => 15
15 ^ 9 => 1110 ^ 1001 => 0111 =>  7
"""
def solutionByXOR(A):
	result = 0
	for number in (A):
		result ^= number
	return result

print("xor result = " + json.dumps(solutionByXOR(A)))

"""
使用 groupby 的簡易方式
"""
def solutionByGroup(A):
	for k, v in groupby(sorted(A)):
		if(len(list(v)) == 1):
			return k
	return 0

print("group result = " + json.dumps(solutionByGroup(A)))

"""
使用排序後兩兩比較的檢查方式
"""
def solutionByLoop(A):
	if(len(A) == 1):
		return A[0]
	else:
	 	sortedList = sorted(A)
	 	count = len(sortedList) - 1
	 	for i in range(0, count, 2):
	 		if sortedList[i] != sortedList[i+1]:
	 			return sortedList[i]
	 	return sortedList[count]

print("loop result = " + json.dumps(solutionByLoop(A)))