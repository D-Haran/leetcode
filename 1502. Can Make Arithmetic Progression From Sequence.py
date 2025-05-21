"""
A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.

Given an array of numbers arr, return true if the array can be rearranged to form an arithmetic progression. Otherwise, return false.
https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/
"""

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr = sorted(arr)
        res = True
        difference = arr[1] - arr[0]

        for idx, i in enumerate(arr):
            if idx+1 < len(arr):
                if arr[idx+1] - i != difference:
                    res = False

        return res

    # Time Complexity: O(n log n)
    # Space Complexity: O(1)
