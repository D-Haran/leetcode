"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.
https://leetcode.com/problems/move-zeroes/description/
"""

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # Store the length of the list of integers.
        lenOfNums = len(nums)
        
        # Iterate over the integers in the list.
        for i in nums:
            # If the current integer is 0...
            if i == 0:
                # Insert a 0 at the end of the list.
                nums.insert(lenOfNums, 0)
                # Remove the first 0 from the list.
                nums.remove(0)

    # Time Complexity: O(n)
    # The time complexity is O(n) because we're iterating over the list of numbers once. 
    # n is the number of numbers.

    # Space Complexity: O(1)
    # The space complexity is O(1) because we're not using any additional data structures whose size scales with the size of the input.
