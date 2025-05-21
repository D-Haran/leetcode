"""
Given a string s consisting of words and spaces, return the length of the last word in the string.
A word is a maximal substring consisting of non-space characters only.
https://leetcode.com/problems/length-of-last-word/
"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = 0

        firstLetter = False

        newString = s[::-1]

        for i in newString:
            if i != " ":
                res += 1

                firstLetter = True

            if i == " ":
                if firstLetter == True:
                    return res

        return res

    # Time Complexity: O(n)
    # Space Complexity: O(n)
