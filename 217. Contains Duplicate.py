"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
https://leetcode.com/problems/contains-duplicate/ 
"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Initialize a set to store the integers that have been seen.
        seen = set()

        # Iterate over the integers in the list.
        for i in range(len(nums)):
            # If the current integer has not been seen before, add it to the set.
            if nums[i] not in seen:
                seen.add(nums[i])
            # If the current integer has been seen before, return True.
            else:
                return True

        # If no duplicate integers have been found, return False.
        return False

    # Time Complexity: O(n)
    # The time complexity is O(n) because we're iterating over the list of integers once. 
    # n is the number of integers.

    # Space Complexity: O(n)
    # The space complexity is O(n) because we're creating a set to store the integers that have been seen. 
    # The space used by the set scales linearly with the size of the input.
