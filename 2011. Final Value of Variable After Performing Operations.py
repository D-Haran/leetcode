"""
There is a programming language with only four operations and one variable X:
- ++X and X++ increments the value of the variable X by 1.
- --X and X-- decrements the value of the variable X by 1.
Initially, the value of X is 0.

Given an array of strings operations containing a list of operations, return the final value of X after performing all the operations.

https://leetcode.com/problems/final-value-of-variable-after-performing-operations/
"""

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        # Initialize `res` as 0. This will be used to store the value of X.
        res = 0

        # Iterate over the elements in `operations`.
        for i in operations:
            # If "--" is in the current operation...
            if "--" in i:
                # Decrement `res` by 1.
                res -= 1
            # Otherwise if "++" is in the current operation...
            else:
                # Increment `res` by 1.
                res += 1

        # Return `res`.
        return res

    # Time Complexity: O(n)
    # The time complexity is O(n) because we're iterating over the operations once. 
    # n is the number of operations.

    # Space Complexity: O(1)
    # The space complexity is O(1) because we're not using any additional data structures whose size scales with the size of the input.
