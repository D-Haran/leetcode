"""
Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
Return the array in the form [x1,y1,x2,y2,...,xn,yn].
https://leetcode.com/problems/shuffle-the-array/description/ 
"""

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        # Divide the input list into two halves `xs` and `ys`
        xs = nums[0:n]
        ys = nums[n:]
        # Initialize an empty list `res` to store the result
        res = []

        # Iterate over the elements in `xs` with their indices
        for idx, i in enumerate(xs):
            # Append the current element from `xs` to `res`
            res.append(i)
            # Append the element from `ys` at the same index to `res`
            res.append(ys[idx])

        # Return the result
        return res

    # Time Complexity: O(n)
    # The time complexity is O(n) because we're iterating over the elements in the list once. 
    # n is the number of elements.

    # Space Complexity: O(n)
    # The space complexity is O(n) because we're creating three lists (`xs`, `ys`, and `res`) to store the elements of the input list. 
    # The size of these lists scales with the size of the input.
