"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.
https://leetcode.com/problems/longest-consecutive-sequence/ 
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Convert the list of numbers to a set to remove duplicates and enable O(1) lookups.
        numSet = set(nums)

        # Initialize the length of the longest consecutive elements sequence to 0.
        longest = 0

        # Iterate over the numbers in the list.
        for n in nums:
            # If the current number is the start of a sequence (i.e., n - 1 is not in the set)...
            if (n - 1) not in numSet:
                # Initialize the length of the current sequence to 0.
                length = 0

                # While the current number plus the length is in the set...
                while (n + length) in numSet:
                    # Increment the length.
                    length += 1

                # Update the length of the longest consecutive elements sequence.
                longest = max(length, longest)

        # Return the length of the longest consecutive elements sequence.
        return longest

    # Time Complexity: O(n)
    # The time complexity is O(n) because we're iterating over the list of numbers once. 
    # n is the number of numbers.

    # Space Complexity: O(n)
    # The space complexity is O(n) because we're creating a set to store the numbers. 
    # The space used by the set scales linearly with the size of the input.
