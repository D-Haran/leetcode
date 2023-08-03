"""
Given a string s consisting of words and spaces, return the length of the last word in the string.
A word is a maximal substring consisting of non-space characters only.
https://leetcode.com/problems/length-of-last-word/
"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Initialize a counter for the length of the last word.
        res = 0

        # Initialize a flag to indicate whether we have encountered the first letter of the last word.
        firstLetter = False

        # Reverse the string.
        newString = s[::-1]

        # Iterate over the characters in the reversed string.
        for i in newString:
            # If the current character is a letter...
            if i != " ":
                # Increment the counter.
                res += 1

                # Set the flag to True.
                firstLetter = True

            # If the current character is a space...
            if i == " ":
                # If we have encountered the first letter of the last word, return the length of the last word.
                if firstLetter == True:
                    return res

        # If the string is empty or consists only of spaces, return the length of the last word (which is zero).
        return res

    # Time Complexity: O(n)
    # The time complexity is O(n) because we're iterating over the string once. 
    # n is the length of the string.

    # Space Complexity: O(n)
    # The space complexity is O(n) because we're creating a reversed copy of the string. 
    # The space used by the new string scales linearly with the size of the input.
