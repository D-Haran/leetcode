"""
Given a sorted (in ascending order) integer array nums of n elements and a target value, write a function to search target in nums. 
If target exists, then return its index, otherwise return -1.

https://leetcode.com/problems/binary-search/ 
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Initialize pointers to the start and end of the list.
        left, right = 0, len(nums) - 1
        # While the start pointer is less than or equal to the end pointer...
        while left <= right:
            # Calculate the middle pointer.
            mid = (left + right) // 2
            # If the middle element is the target, return the middle pointer.
            if nums[mid] == target:
                return mid
            # If the middle element is less than the target, move the start pointer to the right of the middle pointer.
            elif nums[mid] < target:
                left = mid + 1
            # If the middle element is greater than the target, move the end pointer to the left of the middle pointer.
            else:
                right = mid - 1
        # If the target is not found, return -1.
        return -1

    # Time Complexity: O(log n)
    # The time complexity is O(log n) because we're using a binary search algorithm, 
    # which halves the size of the remaining list at each step. n is the number of elements.

    # Space Complexity: O(1)
    # The space complexity is O(1) because we're not using any additional data structures whose size scales with the size of the input.
