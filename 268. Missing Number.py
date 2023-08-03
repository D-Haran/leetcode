"""
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
https://leetcode.com/problems/missing-number/ 
"""

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Initialize the sum of the numbers in the list as 0.
        numsAdd = 0
        # Initialize the sum of the numbers in the range [0, n] as 0.
        rangeAdd = 0
        
        # Iterate over the numbers in the list.
        for i in nums:
            # Add the current number to the sum of the numbers in the list.
            numsAdd += i
        
        # Iterate over the numbers in the range [0, n].
        for i in range(0, len(nums)+1):
            # Add the current number to the sum of the numbers in the range [0, n].
            rangeAdd += i
        
        # Return the difference between the sum of the numbers in the range [0, n] and the sum of the numbers in the list.
        return rangeAdd - numsAdd

    # Time Complexity: O(n)
    # The time complexity is O(n) because we're iterating over the list of numbers and the range [0, n]. 
    # n is the number of numbers.

    # Space Complexity: O(1)
    # The space complexity is O(1) because we're not using any additional data structures whose size scales with the size of the input.
