"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

https://leetcode.com/problems/valid-parentheses/description/
"""

class Solution:
    def isValid(self, s: str) -> bool:
        # Initialize an empty stack.
        stack = []

        # Create a dictionary to map the closing parentheses to their corresponding opening parentheses.
        closeToOpens = {
            ')':'(',
            '}':'{',
            ']':'['
        }

        # Iterate over the string of parentheses.
        for c in s:
            # If the current character is a closing parenthesis...
            if c in closeToOpens:
                # If the stack is not empty and the top of the stack is the corresponding opening parenthesis, pop the stack.
                if stack and stack[-1] == closeToOpens[c]:
                    stack.pop()
                # If the stack is empty or the top of the stack is not the corresponding opening parenthesis, return False.
                else:
                    return False
            # If the current character is an opening parenthesis, push it onto the stack.
            else:
                stack.append(c)

        # If the stack is empty, return True. If the stack is not empty, return False.
        return True if not stack else False

    # Time Complexity: O(n)
    # The time complexity is O(n) because we're iterating over the string of parentheses once. 
    # Pushing and popping from the stack takes constant time.

    # Space Complexity: O(n)
    # The space complexity is O(n) because in the worst case, we might need to push all the parentheses onto the stack. 
    # The space used by the stack scales linearly with the size of the input.
