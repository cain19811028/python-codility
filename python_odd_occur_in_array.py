import json

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

#simple test n=5
#simple test n=11
#extreme_single_item [42]
#small random test n=601

A = [9,3,9,3,9,7,9]

def solution(A):
 	sortedList = sorted(A)
 	for i in range(0, len(sortedList), 2):
 		if sortedList[i] != sortedList[i+1]:
 			return sortedList[i]

print(json.dumps(solution(A)))