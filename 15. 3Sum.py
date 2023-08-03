"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.
https://leetcode.com/problems/3sum/
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Initialize the result to an empty list.
        res = []

        # Sort the list of numbers.
        nums.sort()

        # Iterate over the list of numbers.
        for idx, a in enumerate(nums):
            # If the current number is the same as the previous number, skip this iteration to avoid duplicates.
            if idx > 0 and a == nums[idx-1]:
                continue

            # Initialize two pointers, one at the next position and one at the end of the list.
            l, r = idx + 1, len(nums) - 1

            # While the two pointers have not met...
            while l < r:
                # Calculate the sum of the numbers at the current position and the two pointers.
                threeSum = a + nums[l] + nums[r]

                # If the sum is greater than zero, move the right pointer to the left.
                if threeSum > 0:
                    r -= 1

                # If the sum is less than zero, move the left pointer to the right.
                elif threeSum < 0:
                    l += 1

                # If the sum is zero, add the triplet to the result and move the left pointer to the right.
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1

                    # Skip over duplicates.
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        # Return the result.
        return res

    # Time Complexity: O(n^2)
    # The time complexity is O(n^2) because we're iterating over the list of numbers once and for each number, 
    # we're performing a two-pointer traversal of the rest of the list.

    # Space Complexity: O(n)
    # The space complexity is O(n) because in the worst case, we might need to store all the numbers in the result list. 
    # The space used by the result list scales linearly with the size of the input.
