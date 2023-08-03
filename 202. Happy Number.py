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
        # Initialize a list to store the numbers that have been used.
        used = []

        # While the number is not 1...
        while res != 1:
            # If the number has been used before, return False.
            if res in used[:len(used)-1]:
                return False
            else:
                tempRes = 0
                # Replace the number with the sum of the squares of its digits.
                for i in str(res):
                    tempRes += int(i)**2
                res = tempRes
                # Add the number to the list of used numbers.
                used.append(res)
        # If the number is 1, return True.
        return True

    # Time Complexity: O(log n)
    # The time complexity is O(log n) because we're dividing the number by 10 in each iteration.

    # Space Complexity: O(log n)
    # The space complexity is O(log n) because we're storing the used numbers in a list. 
    # The space used by the list scales with the number of digits in the number.
