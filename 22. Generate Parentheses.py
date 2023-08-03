"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
https://leetcode.com/problems/generate-parentheses/
"""

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Only add an open parenthesis if the number of open parentheses is less than n.
        # Only add a closing parenthesis if the number of closing parentheses is less than the number of open parentheses.
        # A combination is valid if and only if the number of open parentheses equals the number of closing parentheses equals n.

        # Initialize an empty stack to store the current combination of parentheses.
        stack = []

        # Initialize an empty list to store the valid combinations of parentheses.
        res = []

        # Define a helper function for backtracking.
        def backtrack(openN, closedN):
            # If the current combination is valid, add it to the list of valid combinations.
            if openN == closedN == n:
                res.append("".join(stack))
                return

            # If we can add an open parenthesis, add it to the current combination and continue backtracking.
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()

            # If we can add a closing parenthesis, add it to the current combination and continue backtracking.
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()

        # Start backtracking with zero open parentheses and zero closing parentheses.
        backtrack(0, 0)

        # Return the list of valid combinations of parentheses.
        return res

    # Time Complexity: O(4^n / sqrt(n))
    # The time complexity is O(4^n / sqrt(n)) because in the worst case, we need to generate and validate all combinations of parentheses, 
    # which is a Catalan number problem. The nth Catalan number is given by 4^n / (n^(3/2) * sqrt(pi)).

    # Space Complexity: O(n)
    # The space complexity is O(n) because in the worst case, if we only add open parentheses, 
    # we might need to store all of them in the stack. The space used by the stack scales linearly with the size of the input.
