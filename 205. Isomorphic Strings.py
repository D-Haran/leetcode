"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. 
No two characters may map to the same character, but a character may map to itself.

https://leetcode.com/problems/isomorphic-strings/
"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Initialize dictionaries to store the indices of each character in the strings.
        sDict = {}
        tDict = {}

        # Iterate over the characters in the first string.
        for idx, i in enumerate(s):
            # If the current character is not in the dictionary, add it to the dictionary with a value of 0.
            if i not in sDict:
                sDict[i] = 0
            # If the current character is in the dictionary, increment its value by the index.
            else:
                sDict[i] += idx

        # Iterate over the characters in the second string.
        for idx, i in enumerate(t):
            # If the current character is not in the dictionary, add it to the dictionary with a value of 0.
            if i not in tDict:
                tDict[i] = 0
            # If the current character is in the dictionary, increment its value by the index.
            else:
                tDict[i] += idx

        # Convert the dictionaries to lists of values.
        sDict = list(sDict.values())
        tDict = list(tDict.values())

        # If the lists of values are equal, return True.
        if sDict == tDict:
            return True
        # If the lists of values are not equal, return False.
        else:
            return False

    # Time Complexity: O(n)
    # The time complexity is O(n) because we're iterating over the characters in the strings twice. 
    # n is the number of characters.

    # Space Complexity: O(1)
    # The space complexity is O(1) because we're using a fixed number of variables. 
    # The space used does not scale with the size of the input.
