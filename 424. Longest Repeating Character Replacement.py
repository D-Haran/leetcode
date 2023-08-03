"""
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. 
You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

https://leetcode.com/problems/longest-repeating-character-replacement/description/ 
"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Initialize a dictionary to count the frequency of each character.
        count = {}
        # Initialize the result as 0.
        res = 0

        # Initialize a pointer to the start of the substring.
        l = 0
        # Iterate over the characters in the string.
        for r in range(len(s)):
            # Count the frequency of the current character.
            count[s[r]] = 1 + count.get(s[r], 0)

            # If the length of the substring minus the frequency of the most common character is greater than k...
            while (r - l + 1) - max(count.values()) > k:
                # Decrement the count of the character at the start of the substring.
                count[s[l]] -= 1
                # Move the start of the substring to the right.
                l += 1
            # Update the result as the maximum of the current result and the length of the substring.
            res = max(res, r - l + 1)
        # Return the result.
        return res

    # Time Complexity: O(n)
    # The time complexity is O(n) because we're iterating over the characters in the string once. 
    # n is the number of characters.

    # Space Complexity: O(1)
    # The space complexity is O(1) because we're using a dictionary to store the frequencies of the characters. 
    # The size of the dictionary does not scale with the size of the input, 
    # as there is a fixed number of unique characters that can appear in the string.
