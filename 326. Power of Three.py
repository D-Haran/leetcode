"""
Given an integer n, return true if it is a power of three. Otherwise, return false.

An integer n is a power of three, if there exists an integer x such that n == 3x.

https://leetcode.com/problems/power-of-three/description/
"""

import numpy as np

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n > 0:
            return (math.log10(n) / math.log10(3)) % 1 == 0
        return False

        #############
        # RECURSIVE
        #############
        if n == 3:
            return True
        elif n < 3:
            return False
        else:
            return self.isPowerOfThree(n**(1/3)) 