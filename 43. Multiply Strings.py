"""
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.
https://leetcode.com/problems/multiply-strings/
"""

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return str(int(num1)*int(num2))

    # Time Complexity: O(1)
    # Space Complexity: O(1)
