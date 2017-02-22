import json

"""
Task：StoneWall
Cover "Manhattan skyline" using the minimum number of rectangles.
－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－
You are going to build a stone wall.
The wall should be straight and N meters long, and its thickness should be constant;
however, it should have different heights in different places.
The height of the wall is specified by a zero-indexed array H of N positive integers.
H[I] is the height of the wall from I to I+1 meters to the right of its left end. In particular,
H[0] is the height of the wall's left end and H[N−1] is the height of the wall's right end.

The wall should be built of cuboid stone blocks (that is, all sides of such blocks are rectangular).
Your task is to compute the minimum number of blocks needed to build the wall.

Write a function:

    def solution(H)

that, given a zero-indexed array H of N positive integers specifying the height of the wall,
returns the minimum number of blocks needed to build it.

For example, given array H containing N = 9 integers:

    H[0] = 8    H[1] = 8    H[2] = 5
    H[3] = 7    H[4] = 9    H[5] = 8
    H[6] = 7    H[7] = 4    H[8] = 8

the function should return 7. The figure shows one possible arrangement of seven blocks.
"""

H = [8, 8, 5, 7, 9, 8, 7, 4, 8]

"""
方法一：用 append  和 pop 實作 stack 的概念
Correctness：100%、Performance：100%
"""
def solution(H):
    count = 0
    stack = []
    for n in H:
        while(stack and stack[-1] > n):
            stack.pop()
        if(stack and stack[-1] == n):
            continue
        stack.append(n)
        count += 1

    return count

print(solution(H))