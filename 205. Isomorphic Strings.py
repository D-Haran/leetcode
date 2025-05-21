"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. 
No two characters may map to the same character, but a character may map to itself.

https://leetcode.com/problems/isomorphic-strings/
"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sDict = {}
        tDict = {}

        for idx, i in enumerate(s):
            if i not in sDict:
                sDict[i] = 0
            else:
                sDict[i] += idx

        for idx, i in enumerate(t):
            if i not in tDict:
                tDict[i] = 0
            else:
                tDict[i] += idx

        sDict = list(sDict.values())
        tDict = list(tDict.values())

        if sDict == tDict:
            return True
        else:
            return False

    # Time Complexity: O(n)
    # Space Complexity: O(1)
