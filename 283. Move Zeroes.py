"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.
https://leetcode.com/problems/move-zeroes/description/
"""

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        lenOfNums = len(nums)
        
        for i in nums:
            if i == 0:
                nums.insert(lenOfNums, 0)
                nums.remove(0)

    # Time Complexity: O(n)
    # Space Complexity: O(1)
