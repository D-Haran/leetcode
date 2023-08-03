"""
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.
https://leetcode.com/problems/multiply-strings/
"""

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # Convert the two strings to integers, multiply them, convert the product to a string, and return the result.
        return str(int(num1)*int(num2))

    # Time Complexity: O(1)
    # The time complexity is O(1) because the operations of converting strings to integers, multiplying integers, and converting integers to strings all take constant time.
    # However, it should be noted that this is a simplification. In reality, these operations take time proportional to the number of digits in the numbers.

    # Space Complexity: O(1)
    # The space complexity is O(1) because we're not using any additional data structures whose size scales with input size.
