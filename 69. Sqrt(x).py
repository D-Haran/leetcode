"""
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.
For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
https://leetcode.com/problems/sqrtx/
"""

class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        left, right = 2, x // 2

        while left <= right:
            mid = left + (right - left) // 2

            num = mid * mid

            if num == x:
                return mid

            if num < x:
                left = mid + 1

            else:
                right = mid - 1

        return right

    # Time Complexity: O(log n)
    # Space Complexity: O(1)
