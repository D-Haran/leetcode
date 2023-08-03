"""
Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

Specifically, ans is the concatenation of two nums arrays.

Return the array ans.

https://leetcode.com/problems/concatenation-of-array/
"""

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # Use the multiplication operator to concatenate two `nums` lists.
        return nums*2

    # Time Complexity: O(n)
    # The time complexity is O(n) because we're creating a new list that is twice the size of `nums`. 
    # n is the number of elements in `nums`.

    # Space Complexity: O(n)
    # The space complexity is O(n) because we're creating a new list whose size is twice the size of the input.
