"""
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for idx, i in enumerate(haystack):
            if i == needle[0]:
                if needle == haystack[idx:idx+len(needle)]:
                    return idx
        return -1