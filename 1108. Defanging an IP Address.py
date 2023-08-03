"""
Given a valid (IPv4) IP address, return a defanged version of that IP address.
A defanged IP address replaces every period "." with "[.]".

https://leetcode.com/problems/defanging-an-ip-address/
"""

class Solution:
    def defangIPaddr(self, address: str) -> str:
        # Initialize an empty string to store the result.
        res = ""
        # Iterate over the characters in the string.
        for i in address:
            # If the current character is a period...
            if i == ".":
                # Add a defanged period to the result.
                res += "[.]"
            # If the current character is not a period...
            else:
                # Add the current character to the result.
                res += i
        # Return the result.

        return res

    # Time Complexity: O(n)
    # The time complexity is O(n) because we're iterating over the characters in the string once. 
    # n is the number of characters.

    # Space Complexity: O(n)
    # The space complexity is O(n) because we're creating a string to store the defanged IP address. 
    # The size of the string scales with the size of the input.
