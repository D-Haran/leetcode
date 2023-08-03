"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.
https://leetcode.com/problems/container-with-most-water/
"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Initialize the result to zero.
        res = 0

        # Initialize two pointers at the beginning and end of the list.
        l, r = 0, len(height) - 1

        # While the two pointers have not met...
        while l < r:
            # Calculate the area formed by the heights at the two pointers.
            area = (r - l) * min(height[l], height[r])

            # Update the result if the calculated area is greater than the current result.
            res = max(res, area)

            # Move the pointer pointing to the smaller height towards the other pointer.
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        # Return the maximum area.
        return res

    # Time Complexity: O(n)
    # The time complexity is O(n) because we're iterating over the list of heights once. 
    # The while loop runs until the two pointers meet, which takes at most n steps.

    # Space Complexity: O(1)
    # The space complexity is O(1) because we're not using any additional data structures whose size scales with input size.
