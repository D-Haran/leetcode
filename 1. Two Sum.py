"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
https://leetcode.com/problems/two-sum/
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a dictionary to store the numbers from the list and their indices.
        numsMap = {}

        # Iterate over the list of numbers.
        for i in range(len(nums)):
            # Calculate the complement of the current number with respect to the target.
            complement = target - nums[i]

            # Check if the complement is already in the dictionary.
            if complement in numsMap:
                # If it is, return the index of the complement and the current index.
                return [numsMap[complement], i]

            # If the complement is not in the dictionary, add the current number and its index to the dictionary.
            numsMap[nums[i]] = i

        # If no pair that adds up to the target is found, return None.
        return

    # Time Complexity: O(n)
    # The time complexity is O(n) because we're iterating over the list of numbers once. 
    # Checking if an element is in the dictionary takes constant time, so the overall time complexity is linear.

    # Space Complexity: O(n)
    # The space complexity is O(n) because in the worst case, we might need to store all the numbers in the dictionary. 
    # The space used by the dictionary scales linearly with the size of the input.
