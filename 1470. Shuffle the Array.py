"""
Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
Return the array in the form [x1,y1,x2,y2,...,xn,yn].
https://leetcode.com/problems/shuffle-the-array/description/ 
"""

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        xs = nums[0:n]
        ys = nums[n:]
        res = []

        for idx, i in enumerate(xs):
            res.append(i)
            res.append(ys[idx])

        return res

    # Time Complexity: O(n)
    # Space Complexity: O(n)