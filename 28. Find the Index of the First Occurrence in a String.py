"""
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # If the needle is an empty string, return 0.
        if not needle:
            return 0

        # Iterate over the characters in the haystack with their indices.
        for idx, i in enumerate(haystack):
            # If the current character is equal to the first character of the needle...
            if i == needle[0]:
                # If the substring of the haystack starting at the current index and with the length of the needle is equal to the needle...
                if needle == haystack[idx:idx+len(needle)]:
                    # Return the current index.
                    return idx

        # If the needle is not found in the haystack, return -1.
        return -1

    # Time Complexity: O(n*m)
    # The time complexity is O(n*m) where n is the length of the haystack and m is the length of the needle. 
    # We're iterating over the haystack and for each character, we're comparing a substring of the haystack to the needle.

    # Space Complexity: O(1)
    # The space complexity is O(1) because we're not using any additional data structures whose size scales with input size.
