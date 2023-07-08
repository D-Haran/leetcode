"""
Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.
"""

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        while n > 0:
            n /= 2
        if n == 1:
            return True
        else:
            return False