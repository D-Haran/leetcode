"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.
https://leetcode.com/problems/valid-palindrome/ 
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Join the string text, filter out non-alphanumeric symbols, and convert to lowercase.
        concatonatedStr = ''.join(filter(str.isalnum, s)).lower()

        # If the string is the same when reversed, return True. Otherwise, return False.
        if concatonatedStr == concatonatedStr[::-1]:
            return True
        else:
            return False

    # Time Complexity: O(n)
    # The time complexity is O(n) because we're iterating over the string twice: once to filter out non-alphanumeric symbols and convert to lowercase, 
    # and once to reverse the string. n is the length of the string.

    # Space Complexity: O(n)
    # The space complexity is O(n) because we're creating a new string to store the filtered and lowercased string. 
    # The space used by the new string scales linearly with the size of the input.
