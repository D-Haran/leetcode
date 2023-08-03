"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

https://leetcode.com/problems/product-of-array-except-self/ 
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Initialize the result list with all 1's.
        res = [1] * len(nums)
       
        # Initialize the prefix product as 1.
        prefix = 1
        # Calculate the prefix product for each index.
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        # Initialize the postfix product as 1.
        postfix = 1
        # Calculate the postfix product for each index.
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        # Return the result list.
        return res

    # Time Complexity: O(n)
    # The time complexity is O(n) because we're iterating over the list of numbers twice. 
    # n is the number of numbers.

    # Space Complexity: O(1)
    # The space complexity is O(1) because we're using a constant amount of space 
    # apart from the input and output variables. The space used does not scale with the size of the input.
