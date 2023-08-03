"""
Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.

You must implement a solution with a linear runtime complexity and use only constant extra space.
https://leetcode.com/problems/single-number-ii/
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Initialize a dictionary to store the occurrences of each number.
        occurences = {}
        
        # Iterate over the numbers in the list.
        for i in nums:
            # If the current number is not in the dictionary, add it to the dictionary with a count of 0.
            occurences[i] = 0

        # Iterate over the numbers in the list.
        for i in nums:
            # Increment the count of the current number in the dictionary.
            occurences[i] += 1

        # Return the key whose value in the dictionary is 1.
        return list(occurences.keys())[list(occurences.values()).index(1)]

    # Time Complexity: O(n)
    # The time complexity is O(n) because we're iterating over the list of numbers twice. 
    # n is the number of numbers.

    # Space Complexity: O(n)
    # The space complexity is O(n) because we're creating a dictionary to store the occurrences of each number. 
    # The space used by the dictionary scales linearly with the size of the input.
