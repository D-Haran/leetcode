"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.


Valid operators are +, -, *, and /. Each operand may be an integer or another expression.


Note that division between two integers should truncate toward zero.


It is guaranteed that the given RPN expression is always valid. That means the expression would always evaluate to a result, and there will not be any division by zero operation.


https://leetcode.com/problems/evaluate-reverse-polish-notation/ 
"""

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == "+":
                stack.append(stack.pop() + stack.pop())
            elif i == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif i == "*":
                stack.append(stack.pop() * stack.pop())
            elif i == "/":
                c, d = stack.pop(), stack.pop()
                stack.append(int(d / c))
            else:
                stack.append(int(i))
        return stack[0]