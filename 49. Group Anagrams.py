"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
https://leetcode.com/problems/group-anagrams/
"""

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Initialize a dictionary to group the anagrams. The keys will be tuples of the counts of each letter in the string.
        res = defaultdict(list)

        # Iterate over the list of strings.
        for s in strs:
            # Initialize a list to count the occurrence of each letter in the current string.
            count = [0] * 26

            # Iterate over the characters in the current string.
            for c in s:
                # Increment the count of the current letter.
                count[ord(c) - ord("a")] += 1

            # Add the current string to the list of anagrams of other strings with the same letter count.
            res[tuple(count)].append(s)

        # Return the groups of anagrams.
        return res.values()

    # Time Complexity: O(n*m)
    # The time complexity is O(n*m) where n is the number of strings and m is the average length of the strings. 
    # We're iterating over each string and then over each character in the string.

    # Space Complexity: O(n*m)
    # The space complexity is O(n*m) because we're storing all the strings in the result dictionary. 
    # The space used by the dictionary scales with the total number of characters in the strings.
