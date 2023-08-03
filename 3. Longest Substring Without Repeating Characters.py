"""
Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Initialize the result to zero.
        res = 0

        # Create a set to store the characters of the current substring.
        charSet = set()

        # Initialize the left pointer.
        l = 0

        # Iterate over the string with the right pointer.
        for r in range(len(s)):
            # If the current character is already in the set, remove the leftmost character from the set and move the left pointer to the right.
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1

            # Add the current character to the set.
            charSet.add(s[r])

            # Update the result with the length of the current substring.
            res = max(res, r - l + 1)

        # Return the length of the longest substring without repeating characters.
        return res

    # Time Complexity: O(n)
    # The time complexity is O(n) because we're iterating over the string once. 
    # Removing an element from the set and checking if an element is in the set both take constant time, so the overall time complexity is linear.

    # Space Complexity: O(min(n, m))
    # The space complexity is O(min(n, m)) where n is the size of the string and m is the size of the character set. 
    # In the worst case, we might need to store all the characters in the string in the set, 
    # but the size of the set is also limited by the size of the character set.
