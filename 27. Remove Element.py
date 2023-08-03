"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.

https://leetcode.com/problems/remove-element/
"""

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Initialize an index to keep track of the position to which we should move the next non-target value.
        index = 0

        # Iterate over the list of numbers.
        for i in range(len(nums)):
            # If the current number is not equal to the target value...
            if nums[i] != val:
                # Move the current number to the position indicated by the index.
                nums[index] = nums[i]

                # Increment the index.
                index += 1

        # Return the new length of the list.
        return index

    # Time Complexity: O(n)
    # The time complexity is O(n) because we're iterating over the list of numbers once.

    # Space Complexity: O(1)
    # The space complexity is O(1) because we're not using any additional data structures whose size scales with input size. We're modifying the list in place.
