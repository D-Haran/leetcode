"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

https://leetcode.com/problems/min-stack/ 
"""

class MinStack:
    # Constructor method for the MinStack class. It initializes the stack object.
    def __init__(self):
        # Initialize the main stack.
        self.stack = []

        # Initialize the stack for keeping track of the minimum element.
        self.minStack = []

    # This method pushes an element onto the main stack and updates the minimum element.
    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    # This method removes the top element from the main stack and updates the minimum element.
    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    # This method returns the top element of the main stack.
    def top(self) -> int:
        return self.stack[-1]

    # This method retrieves the minimum element in the stack.
    def getMin(self) -> int:
        return self.minStack[-1]

    # Time Complexity: O(1)
    # The time complexity for each function (push, pop, top, getMin) is O(1) because each operation is done in constant time. 

    # Space Complexity: O(n)
    # The space complexity is O(n) because we're using two stacks to store the elements and the minimum values. 
    # The space used by the stacks scales linearly with the number of elements.
