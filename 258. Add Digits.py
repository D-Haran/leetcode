"""
Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.
https://leetcode.com/problems/add-digits/
"""

import math

class Solution:
    def addDigits(self, num: int) -> int:
        # Initialize the result as the input number.
        res = num
        # While the result is greater than 9...
        while res > 9:
            # Initialize a temporary result as 0.
            tempRes = 0
            # Iterate over the digits in the result.
            for i in str(res):
                # Add the current digit to the temporary result.
                tempRes += int(i)
            # Set the result as the temporary result.
            res = tempRes
        # Return the result.
        return res

    # Time Complexity: O(n)
    # The time complexity is O(n) because we're iterating over the digits in the number. 
    # n is the number of digits.

    # Space Complexity: O(1)
    # The space complexity is O(1) because we're not using any additional data structures whose size scales with the size of the input.
