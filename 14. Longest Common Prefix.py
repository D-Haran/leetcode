"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
https://leetcode.com/problems/longest-common-prefix/
"""

import math
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""

        firstWord = strs[0]
        lowestWord = math.inf

        for i in strs:
            if len(i) < lowestWord:
                    lowestWord = len(i)

            for idx, s in enumerate(i):
                if idx+1 <= len(firstWord):
                    if s != firstWord[idx]:
                        firstWord = i[:idx]

        return firstWord[:lowestWord]

    # Time Complexity: O(n*m)
    # Space Complexity: O(1)
