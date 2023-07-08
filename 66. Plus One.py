"""
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
https://leetcode.com/problems/plus-one/
"""

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        stringList = ""
        res = []
        for i in digits:
            stringList += str(i)
        newNumber = int(stringList)+1
        for i in str(newNumber):
            res.append(int(i))
        return res