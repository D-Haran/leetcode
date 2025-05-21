"""
Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2^x.
https://leetcode.com/problems/power-of-two/
"""

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        while n > 1:
            if n % 2 != 0:
                return False
            n /= 2

        if n == 1:
            return True
        else:
            return False

    # Time Complexity: O(log n)

    # Space Complexity: O(1)
