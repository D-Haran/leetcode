"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
https://leetcode.com/problems/majority-element/
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        elements = {

        }
        for i in nums:
            if i in elements:
                elements[i] += 1
            else:
                elements[i] = 0

        max_value = max(elements.values())
        for element, age in elements.items():
            if age == max_value:
                return element