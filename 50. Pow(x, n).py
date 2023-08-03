"""
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
https://leetcode.com/problems/powx-n/ 
"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        # If n is zero, return 1.
        if n == 0:
            return 1.0

        # If n is negative, calculate the power of the reciprocal of x and negate n.
        if n < 0:
            x = 1 / x
            n = -n

        # Initialize the result to 1.
        res = 1

        # While n is not zero...
        while n:
            # If n is odd, multiply the result by x.
            if n % 2:
                res *= x

            # Square x and halve n.
            x *= x
            n //= 2

        # Return the result.
        return res

    # Time Complexity: O(log n)
    # The time complexity is O(log n) because in each iteration of the while loop, we're halving n. 
    # The while loop runs until n becomes zero, which takes log n iterations.

    # Space Complexity: O(1)
    # The space complexity is O(1) because we're not using any additional data structures whose size scales with input size.
