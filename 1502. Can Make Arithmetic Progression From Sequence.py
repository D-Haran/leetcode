"""
A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.

Given an array of numbers arr, return true if the array can be rearranged to form an arithmetic progression. Otherwise, return false.
https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/
"""

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        # Sort `arr` in ascending order.
        arr = sorted(arr)
        # Initialize `res` as True. This will be returned as the result.
        res = True
        # Calculate the difference between the first two elements in `arr`.
        difference = arr[1] - arr[0]

        # Iterate over the elements in `arr` with their indices.
        for idx, i in enumerate(arr):
            # If the current index is not the last index in `arr`...
            if idx+1 < len(arr):
                # If the difference between the next element and the current element is not equal to `difference`...
                if arr[idx+1] - i != difference:
                    # Set `res` to False.
                    res = False

        # Return `res`.
        return res

    # Time Complexity: O(n log n)
    # The time complexity is O(n log n) because we're sorting the elements in `arr`. 
    # n is the number of elements in `arr`.

    # Space Complexity: O(1)
    # The space complexity is O(1) because we're not using any additional data structures whose size scales with the size of the input.
