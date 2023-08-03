"""
Given a zero-based permutation nums (0-indexed), build an array ans of the same length where ans[i] = nums[nums[i]] for each 0 <= i < nums.length and return it.
A zero-based permutation nums is an array of distinct integers from 0 to nums.length - 1 (inclusive).

https://leetcode.com/problems/build-array-from-permutation/
"""

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        # Initialize a new list with zeros. The length of the new list is the same as the length of `nums`.
        newList = [0] * len(nums)

        # Iterate over the elements in `nums`.
        for i in nums:
            # Replace the element in `newList` at the index specified by the current element with the element in `nums` at the index specified by the current element.
            newList[i] = nums[nums[i]]

        # Return the new list.
        return newList

    # Time Complexity: O(n)
    # The time complexity is O(n) because we're iterating over the elements in `nums` once. 
    # n is the number of elements in `nums`.

    # Space Complexity: O(n)
    # The space complexity is O(n) because we're creating a new list whose size is the same as the size of the input.
