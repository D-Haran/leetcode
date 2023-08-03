"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
https://leetcode.com/problems/valid-anagram/ 
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Sort the characters in the first string.
        ss = sorted(s)
        # Sort the characters in the second string.
        tt = sorted(t)
        
        # If the sorted characters in the first string are the same as the sorted characters in the second string, return True.
        if ss == tt:
            return True
        # If the sorted characters in the first string are not the same as the sorted characters in the second string, return False.
        else:
            return False

    # Time Complexity: O(n log n)
    # The time complexity is O(n log n) because we're sorting the characters in the strings. 
    # n is the number of characters.

    # Space Complexity: O(n)
    # The space complexity is O(n) because we're creating new lists to store the sorted characters. 
    # The space used by the lists scales linearly with the size of the input.
