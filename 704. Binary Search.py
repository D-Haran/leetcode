"""
Given a sorted (in ascending order) integer array nums of n elements and a target value, write a function to search target in nums. 
If target exists, then return its index, otherwise return -1.

https://leetcode.com/problems/binary-search/ 
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    # Time Complexity: O(log n)
    # Space Complexity: O(1)
