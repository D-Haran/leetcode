"""
Given an array of integers temperatures represents the daily temperatures, return an array answer 
such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. 
If there is no future day for which this is possible, keep answer[i] == 0 instead.

https://leetcode.com/problems/daily-temperatures/description/ 
"""

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Initialize the result array with zeros
        res = [0] * len(temperatures)
        # Initialize an empty stack to store the temperature and its index
        stack = [] 

        # Iterate over the temperatures with their indices
        for idx, t in enumerate(temperatures):
            # While the stack is not empty and the current temperature is greater than the last temperature in the stack...
            while stack and t > stack[-1][0]:
                # Pop the last temperature and its index from the stack
                stackT, stackInd = stack.pop()
                # Update the corresponding element in the result array
                res[stackInd] = (idx - stackInd)
            # Push the current temperature and its index to the stack
            stack.append([t, idx])
        # Return the result array

        return res

    # Time Complexity: O(n)
    # The time complexity is O(n) because we're iterating over the temperatures once. 
    # n is the number of temperatures.

    # Space Complexity: O(n)
    # The space complexity is O(n) because we're using a stack to store the temperatures and their indices. 
    # The size of the stack scales with the size of the input.
