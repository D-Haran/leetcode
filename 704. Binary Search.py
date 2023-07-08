"""
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.


You must write an algorithm with O(log n) runtime complexity.
https://leetcode.com/problems/binary-search/ 
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i in nums:
            if i == target:
                return nums.index(i)
        return -1