import json

"""
Task：GenomicRangeQuery
Find the minimal nucleotide from a range of sequence DNA.
－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－
A DNA sequence can be represented as a string consisting of the letters A, C, G and T,
which correspond to the types of successive nucleotides in the sequence.
Each nucleotide has an impact factor, which is an integer.
Nucleotides of types A, C, G and T have impact factors of 1, 2, 3 and 4, respectively.
You are going to answer several queries of the form:
What is the minimal impact factor of nucleotides contained in a particular part of the given DNA sequence?

The DNA sequence is given as a non-empty string S = S[0]S[1]...S[N-1] consisting of N characters.
There are M queries, which are given in non-empty arrays P and Q, each consisting of M integers.
The K-th query (0 ≤ K < M) requires you to find the minimal impact factor of nucleotides
contained in the DNA sequence between positions P[K] and Q[K] (inclusive).

For example, consider string S = CAGCCTA and arrays P, Q such that:

    P[0] = 2    Q[0] = 4
    P[1] = 5    Q[1] = 5
    P[2] = 0    Q[2] = 6

The answers to these M = 3 queries are as follows:

The part of the DNA between positions 2 and 4 contains nucleotides G and C (twice),
whose impact factors are 3 and 2 respectively, so the answer is 2.
The part between positions 5 and 5 contains a single nucleotide T,
whose impact factor is 4, so the answer is 4.
The part between positions 0 and 6 (the whole string) contains all nucleotides,
in particular nucleotide A whose impact factor is 1, so the answer is 1.
Write a function:

  def solution(S, P, Q)

that, given a non-empty zero-indexed string S consisting of N characters
and two non-empty zero-indexed arrays P and Q consisting of M integers,
returns an array consisting of M integers specifying the consecutive answers to all queries.

The sequence should be returned as:

a Results structure (in C), or
a vector of integers (in C++), or
a Results record (in Pascal), or
an array of integers (in any other programming language).
For example, given the string S = CAGCCTA and arrays P, Q such that:

    P[0] = 2    Q[0] = 4
    P[1] = 5    Q[1] = 5
    P[2] = 0    Q[2] = 6

the function should return the values [2, 4, 1], as explained above.
"""

S = "CAGCCTA"
P = [2, 5, 0]
Q = [4, 5, 6]
mapping = {"A":100001, "C":100001, "G":100001}

"""
用 mapping 先記錄各字元最早出現的位置
Correctness：100%、Performance：100%
"""
def solutionByMapping(S, P, Q):
    length = len(S)
    matrix = [([0] * length) for i in range(len(mapping))]
    for i in range(length-1, -1, -1):
        mapping[S[i]] = i
        matrix[0][i] = mapping['A']
        matrix[1][i] = mapping['C']
        matrix[2][i] = mapping['G']
    length = len(P)
    result = [0] * length
    for i in range(length):
        if matrix[0][P[i]] <= Q[i]:
            result[i] = 1
        elif matrix[1][P[i]] <= Q[i]:
            result[i] = 2
        elif matrix[2][P[i]] <= Q[i]:
            result[i] = 3
        else:
            result[i] = 4
    return result

print(solutionByMapping(S, P, Q))

"""
只有75分，但很簡易的方法（效能O(N*M)被扣分）
Correctness：100%、Performance：33%
"""
def solutionBySlice(S, P, Q):
    result = []
    length = len(P)
    for i in range(length):
        temp = (S[P[i]:Q[i]+1])
        if "A" in temp:
            result.append(1)
        elif "C" in temp:
            result.append(2)
        elif "G" in temp:
            result.append(3)
        elif "T" in temp:
            result.append(4)
    return result

print(solutionBySlice(S, P, Q))