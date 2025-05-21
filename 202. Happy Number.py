"""
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.
https://leetcode.com/problems/happy-number/ 
"""

class Solution:
    def isHappy(self, n: int) -> bool:
        res = n
        used = []

        while res != 1:
            if res in used[:len(used)-1]:
                return False
            else:
                tempRes = 0
                for i in str(res):
                    tempRes += int(i)**2
                res = tempRes
                used.append(res)
        return True

    # Time Complexity: O(log n)
    # Space Complexity: O(log n)
