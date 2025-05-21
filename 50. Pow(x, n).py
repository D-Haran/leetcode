"""
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
https://leetcode.com/problems/powx-n/ 
"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0

        if n < 0:
            x = 1 / x
            n = -n

        res = 1

        while n:
            if n % 2:
                res *= x

            x *= x
            n //= 2

        return res

    # Time Complexity: O(log n)
    # Space Complexity: O(1)
