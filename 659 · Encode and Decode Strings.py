"""
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.
https://www.lintcode.com/problem/659/ 
(Leetcode premium, but free on Lintcode)
"""

class Solution:
    # This method takes a list of strings and returns a single string that represents the encoded strings.
    def encode(self, strs: List[str]) -> str:
        # Initialize an empty string to store the result.
        res = ""
        # For each string in the list...
        for s in strs:
            # Add the length of the string, a delimiter, and the string itself to the result.
            res += str(len(s)) + "#" + s
        # Return the result.
        return res

    # This method takes a string that represents the encoded strings and returns a list of the decoded strings.
    def decode(self, str: str) -> List[str]:
        # Initialize an empty list to store the result.
        res = []
        # Initialize a pointer to the start of the string.
        i = 0

        # While the pointer is less than the length of the string...
        while i < len(str):
            # Initialize a pointer to the current position.
            j = i
            # Find the position of the delimiter.
            while str[j] != "#":
                j += 1
            # Extract the length of the current string.
            length = int(str[i:j])
            # Extract the current string and add it to the result.
            res.append(str[j + 1 : j + 1 + length])
            # Move the pointer to the start of the next string.
            i = j + 1 + length
        # Return the result.
        return res

    # Time Complexity: O(n)
    # The time complexity is O(n) because we're iterating over the characters in the strings once. 
    # n is the number of characters.

    # Space Complexity: O(n)
    # The space complexity is O(n) because we're creating a string and a list to store the encoded and decoded strings, respectively. 
    # The space used by these data structures scales linearly with the size of the input.
