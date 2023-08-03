"""
Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2^x.
https://leetcode.com/problems/power-of-two/
"""

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # While the integer is greater than 1...
        while n > 1:
            # If the integer is not divisible by 2, return False.
            if n % 2 != 0:
                return False
            # Divide the integer by 2.
            n /= 2

        # If the integer is 1, return True.
        if n == 1:
            return True
        # If the integer is not 1, return False.
        else:
            return False

    # Time Complexity: O(log n)
    # The time complexity is O(log n) because in the worst case, we might have to divide the integer by 2 until it becomes 1.

    # Space Complexity: O(1)
    # The space complexity is O(1) because we're not using any additional data structures whose size scales with the size of the input.
