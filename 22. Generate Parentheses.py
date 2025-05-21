"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
https://leetcode.com/problems/generate-parentheses/
"""

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return

            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()

            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()
        backtrack(0, 0)
        return res

    # Time Complexity: O(4^n / sqrt(n))
    # The time complexity is O(4^n / sqrt(n)) because in the worst case, we need to generate and validate all combinations of parentheses, 
    # which is a Catalan number problem. The nth Catalan number is given by 4^n / (n^(3/2) * sqrt(pi)).

    # Space Complexity: O(n)