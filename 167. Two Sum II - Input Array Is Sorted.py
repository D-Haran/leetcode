"""
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/ 
"""

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Initialize two pointers at the beginning and end of the list.
        l, r = 0, len(numbers) - 1

        # While the left pointer is less than the right pointer...
        while l < r:
            # Calculate the current sum of the numbers at the left and right pointers.
            currentSum = numbers[l] + numbers[r]

            # If the current sum is greater than the target, move the right pointer to the left.
            if currentSum > target:
                r -= 1

            # If the current sum is less than the target, move the left pointer to the right.
            elif currentSum < target:
                l += 1

            # If the current sum is equal to the target, return the indices of the two numbers.
            else:
                return [l + 1, r + 1]

    # Time Complexity: O(n)
    # The time complexity is O(n) because in the worst case, we might have to move the left pointer from the beginning to the end of the list, 
    # or the right pointer from the end to the beginning of the list. n is the number of numbers.

    # Space Complexity: O(1)
    # The space complexity is O(1) because we're not using any additional data structures whose size scales with the size of the input.
