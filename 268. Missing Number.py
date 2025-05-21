"""
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
https://leetcode.com/problems/missing-number/ 
"""

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        numsAdd = 0
        rangeAdd = 0
        
        for i in nums:
            numsAdd += i
        
        for i in range(0, len(nums)+1):
            rangeAdd += i
        
        return rangeAdd - numsAdd

    # Time Complexity: O(n)
    # Space Complexity: O(1)
