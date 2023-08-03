"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
https://leetcode.com/problems/majority-element/ 
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Initialize a dictionary to store the occurrences of each number.
        elements = {}

        # Iterate over the numbers in the list.
        for i in nums:
            # If the current number is in the dictionary, increment its count.
            if i in elements:
                elements[i] += 1
            # If the current number is not in the dictionary, add it to the dictionary with a count of 0.
            else:
                elements[i] = 0

        # Find the maximum value in the dictionary.
        max_value = max(elements.values())

        # Iterate over the items in the dictionary.
        for element, age in elements.items():
            # If the current value is the maximum value, return the current key.
            if age == max_value:
                return element

    # Time Complexity: O(n)
    # The time complexity is O(n) because we're iterating over the list of numbers twice. 
    # n is the number of numbers.

    # Space Complexity: O(n)
    # The space complexity is O(n) because we're creating a dictionary to store the occurrences of each number. 
    # The space used by the dictionary scales linearly with the size of the input.
