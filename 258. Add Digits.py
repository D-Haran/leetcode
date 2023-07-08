"""
Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.
https://leetcode.com/problems/add-digits/
"""

import math

class Solution:
    def addDigits(self, num: int) -> int:
        res = num
        while res > 9:
            tempRes = 0
            for i in str(res):
                tempRes += int(i)
            res = tempRes
        return res