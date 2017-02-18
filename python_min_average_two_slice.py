import json

"""
Task：MinAvgTwoSlice
Find the minimal average of any slice containing at least two elements.
－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－
A non-empty zero-indexed array A consisting of N integers is given.
A pair of integers (P, Q), such that 0 ≤ P < Q < N,
is called a slice of array A (notice that the slice contains at least two elements).
The average of a slice (P, Q) is the sum of A[P] + A[P + 1] + ... + A[Q] divided by the length of the slice.
To be precise, the average equals (A[P] + A[P + 1] + ... + A[Q]) / (Q − P + 1).

For example, array A such that:

    A[0] = 4
    A[1] = 2
    A[2] = 2
    A[3] = 5
    A[4] = 1
    A[5] = 5
    A[6] = 8

contains the following example slices:

slice (1, 2), whose average is (2 + 2) / 2 = 2;
slice (3, 4), whose average is (5 + 1) / 2 = 3;
slice (1, 4), whose average is (2 + 2 + 5 + 1) / 4 = 2.5.

The goal is to find the starting position of a slice whose average is minimal.

Write a function:

    def solution(A)

that, given a non-empty zero-indexed array A consisting of N integers,
returns the starting position of the slice with the minimal average.
If there is more than one slice with a minimal average,
you should return the smallest starting position of such a slice.

For example, given array A such that:

    A[0] = 4
    A[1] = 2
    A[2] = 2
    A[3] = 5
    A[4] = 1
    A[5] = 5
    A[6] = 8

the function should return 1, as explained above.
"""

A = [4, 2, 2, 5, 1, 5, 8]

"""
Correctness：100%、Performance：90%
"""
def solution(A):
    result = 0
    minAvg3 = 0
    minAvg2 = (A[0] + A[1]) / 2
    minValue = minAvg2
    length = len(A)
    for i in range(2, length):
        minAvg2 = (A[i-1] + A[i]) / 2
        minAvg3 = (A[i-2] + A[i-1] + A[i]) / 3
        if(minAvg2 < minAvg3):
            if(minAvg2 < minValue):
                minValue = minAvg2
                result = i - 1
        else:
            if(minAvg3 < minValue):
                minValue = minAvg3
                result = i - 2
    return result

print(solution(A))