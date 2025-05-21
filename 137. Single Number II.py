"""
Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.

You must implement a solution with a linear runtime complexity and use only constant extra space.
https://leetcode.com/problems/single-number-ii/
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        occurences = {}
        
        for i in nums:
            occurences[i] = 0

        for i in nums:
            occurences[i] += 1

        return list(occurences.keys())[list(occurences.values()).index(1)]

    # Time Complexity: O(n)
    # Space Complexity: O(n)
