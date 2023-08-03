"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.
https://leetcode.com/problems/single-number/
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Initialize a dictionary to store the occurrences of each number.
        occurences = {}

        # Iterate over the numbers in the list.
        for i in nums:
            # If the current number is in the dictionary, increment its count.
            if i in occurences:
                occurences[i] += 1
            # If the current number is not in the dictionary, add it to the dictionary with a count of 0.
            else:
                occurences[i] = 0

        # Iterate over the numbers in the dictionary.
        for i in occurences:
            # If the count of the current number is 0, return it.
            if occurences[i] == 0:
                return i

    # Time Complexity: O(n)
    # The time complexity is O(n) because we're iterating over the list of numbers twice. 
    # n is the number of numbers.

    # Space Complexity: O(n)
    # The space complexity is O(n) because we're creating a dictionary to store the occurrences of each number. 
    # The space used by the dictionary scales linearly with the size of the input.
