"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
https://leetcode.com/problems/contains-duplicate/ 
"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for i in range(len(nums)):
            if nums[i] not in seen:
                seen.add(nums[i])
            else:
                return True

        return False

    # Time Complexity: O(n)
    # Space Complexity: O(n)
