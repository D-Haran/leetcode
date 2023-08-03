"""
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.
For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
https://leetcode.com/problems/sqrtx/
"""

class Solution:
    def mySqrt(self, x: int) -> int:
        # If x is less than 2, return x because the square root of a number less than 2 is less than or equal to the number itself.
        if x < 2:
            return x

        # Initialize the left and right pointers for binary search to 2 and x // 2.
        left, right = 2, x // 2

        # While the left pointer is less than or equal to the right pointer...
        while left <= right:
            # Calculate the middle pointer.
            mid = left + (right - left) // 2

            # Calculate the square of the middle pointer.
            num = mid * mid

            # If the square is equal to x, return the middle pointer.
            if num == x:
                return mid

            # If the square is less than x, move the left pointer to the right of the middle pointer.
            if num < x:
                left = mid + 1

            # If the square is greater than x, move the right pointer to the left of the middle pointer.
            else:
                right = mid - 1

        # Return the right pointer because when the square of the middle pointer is greater than x, we move the right pointer to the left of the middle pointer,
        # so the right pointer will always point to the square root of x rounded down to the nearest integer.
        return right

    # Time Complexity: O(log n)
    # The time complexity is O(log n) because we're using binary search to find the square root of x. 
    # The binary search takes log n iterations where n is the value of x.

    # Space Complexity: O(1)
    # The space complexity is O(1) because we're not using any additional data structures whose size scales with input size.
