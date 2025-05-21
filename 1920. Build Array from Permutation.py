"""
Given a zero-based permutation nums (0-indexed), build an array ans of the same length where ans[i] = nums[nums[i]] for each 0 <= i < nums.length and return it.
A zero-based permutation nums is an array of distinct integers from 0 to nums.length - 1 (inclusive).

https://leetcode.com/problems/build-array-from-permutation/
"""

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        newList = [0] * len(nums)

        for i in nums:
            newList[i] = nums[nums[i]]

        return newList

    # Time Complexity: O(n)
    # Space Complexity: O(n)
