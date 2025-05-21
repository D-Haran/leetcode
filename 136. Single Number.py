"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.
https://leetcode.com/problems/single-number/
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        occurences = {}

        for i in nums:
            if i in occurences:
                occurences[i] += 1
            else:
                occurences[i] = 0

        for i in occurences:
            if occurences[i] == 0:
                return i

    # Time Complexity: O(n)
    # Space Complexity: O(n)
