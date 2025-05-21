"""
Given an integer array arr, return true if there are three consecutive odd numbers in the array. Otherwise, return false.

https://leetcode.com/problems/three-consecutive-odds/description/
"""

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        if len(arr) >= 3 and len(set(arr)) == 1:
            return arr[0] % 2 == 1
        for i in range(len(arr)-2):
            if (arr[i] + arr[i+1] + arr[i+2]) % 2 == 1:
                return True
        return False
        