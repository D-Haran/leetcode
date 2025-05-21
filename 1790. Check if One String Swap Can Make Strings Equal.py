"""
You are given two strings s1 and s2 of equal length. A string swap is an operation where you choose two indices in a string (not necessarily different) and swap the characters at these indices.

Return true if it is possible to make both strings equal by performing at most one string swap on exactly one of the strings. Otherwise, return false.

https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/description/
"""

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if sorted(s1) != sorted(s2):
            return False
        counter = 0
        for i in range(len(s2)):
            if s1[i] != s2[i]:
                counter += 1
        if counter <= 2:
            return True
        return False