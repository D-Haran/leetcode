"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
https://leetcode.com/problems/longest-common-prefix/
"""

import math
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Initialize the result to an empty string.
        res = ""

        # Take the first word from the list as the initial prefix.
        firstWord = strs[0]

        # Initialize the length of the shortest word to infinity.
        lowestWord = math.inf

        # Iterate over the list of words.
        for i in strs:
            # If the length of the current word is less than the length of the shortest word so far, update the length of the shortest word.
            if len(i) < lowestWord:
                    lowestWord = len(i)

            # Iterate over the characters in the current word.
            for idx, s in enumerate(i):
                # If the current character is not equal to the corresponding character in the prefix, update the prefix to exclude the mismatched character.
                if idx+1 <= len(firstWord):
                    if s != firstWord[idx]:
                        firstWord = i[:idx]

        # Return the common prefix, but only up to the length of the shortest word.
        return firstWord[:lowestWord]

    # Time Complexity: O(n*m)
    # The time complexity is O(n*m) where n is the number of strings and m is the average length of the strings. 
    # We're iterating over each string and then over each character in the string.

    # Space Complexity: O(1)
    # The space complexity is O(1) because we're not using any additional data structures whose size scales with input size.
