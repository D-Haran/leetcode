"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, and /. Each operand may be an integer or another expression.

Note that division between two integers should truncate toward zero.

It is guaranteed that the given RPN expression is always valid. That means the expression would always evaluate to a result, and there will not be any division by zero operation.

https://leetcode.com/problems/evaluate-reverse-polish-notation/ 
"""

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Initialize a stack to store the operands.
        stack = []

        # Iterate over the tokens.
        for i in tokens:
            # If the current token is a plus operator, pop two operands from the stack, add them, and push the result back to the stack.
            if i == "+":
                stack.append(stack.pop() + stack.pop())

            # If the current token is a minus operator, pop two operands from the stack, subtract them, and push the result back to the stack.
            elif i == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)

            # If the current token is a multiplication operator, pop two operands from the stack, multiply them, and push the result back to the stack.
            elif i == "*":
                stack.append(stack.pop() * stack.pop())

            # If the current token is a division operator, pop two operands from the stack, divide them, and push the result back to the stack.
            elif i == "/":
                c, d = stack.pop(), stack.pop()
                stack.append(int(d / c))

            # If the current token is an operand, push it to the stack.
            else:
                stack.append(int(i))

        # Return the result of the arithmetic expression.
        return stack[0]

    # Time Complexity: O(n)
    # The time complexity is O(n) because we're iterating over the list of tokens once. 
    # n is the number of tokens.

    # Space Complexity: O(n)
    # The space complexity is O(n) because we're using a stack to store the operands. 
    # The space used by the stack scales linearly with the size of the input.
