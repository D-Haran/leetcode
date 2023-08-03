"""
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
https://leetcode.com/problems/plus-one/
"""

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Initialize an empty string to store the string representation of the input number.
        stringList = ""

        # Initialize an empty list to store the digits of the new number.
        res = []

        # Convert each digit to a string and append it to the string representation of the input number.
        for i in digits:
            stringList += str(i)

        # Convert the string representation of the input number to an integer, add one, and store the result.
        newNumber = int(stringList) + 1

        # Convert the new number to a string, convert each character to an integer, and append it to the list of digits.
        for i in str(newNumber):
            res.append(int(i))

        # Return the list of digits of the new number.
        return res

    # Time Complexity: O(n)
    # The time complexity is O(n) because we're iterating over the list of digits twice. 
    # n is the number of digits.

    # Space Complexity: O(n)
    # The space complexity is O(n) because we're creating a new list of digits. 
    # The space used by the new list scales linearly with the size of the input.
