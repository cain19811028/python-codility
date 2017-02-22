import json

"""
Task：Nesting
Determine whether given string of parentheses is properly nested.
－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－
A string S consisting of N characters is called properly nested if:

S is empty;
S has the form "(U)" where U is a properly nested string;
S has the form "VW" where V and W are properly nested strings.
For example, string "(()(())())" is properly nested but string "())" isn't.

Write a function:

    def solution(S)

that, given a string S consisting of N characters,
returns 1 if string S is properly nested and 0 otherwise.

For example, given S = "(()(())())", the function should return 1 and given S = "())", the function should return 0, as explained above.

Assume that:

N is an integer within the range [0..1,000,000];
string S consists only of the characters "(" and/or ")".
"""

A1 = "(()(())())"
A2 = "())"

"""
方法一：用 append  和 pop 實作 stack 的概念
Correctness：100%、Performance：100%
"""
def solution(S):
    stack = []
    for sign in S:
        if sign == '(':
            stack.append(sign)
        else:
            if len(stack) == 0:
                return 0
            stackLast = stack[-1]
            if sign == ')' and stackLast == '(':
                stack.pop()
            else:
                return 0

    return 1 if len(stack) == 0 else 0

print(solution(A1))
print(solution(A2))