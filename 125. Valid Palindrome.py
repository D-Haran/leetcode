"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.


https://leetcode.com/problems/valid-palindrome/ 
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 1. Join String text, 2. filter out alphanumeric symbols, 3. set to lowercase, 4. reverse
        concatonatedStr = ''.join(filter(str.isalnum, s)).lower()
       
        if concatonatedStr == concatonatedStr[::-1]:
            return True
        else:
            return False