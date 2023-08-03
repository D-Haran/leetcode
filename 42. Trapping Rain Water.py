"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
https://leetcode.com/problems/trapping-rain-water/
"""

class Solution:
    def trap(self, height: List[int]) -> int:
        # If the list is empty, return 0.
        if not height: return 0

        # Initialize two pointers at the beginning and end of the list.
        l, r = 0, len(height) - 1

        # Initialize the maximum height from the left and from the right to the heights at the corresponding pointers.
        leftMax, rightMax = height[l], height[r]

        # Initialize the result to zero.
        res = 0

        # While the two pointers have not met...
        while l < r:
            # If the maximum height from the left is less than the maximum height from the right...
            if leftMax < rightMax:
                # Move the left pointer to the right.
                l += 1

                # Update the maximum height from the left if necessary.
                leftMax = max(leftMax, height[l])

                # Add the difference between the maximum height from the left and the current height to the result.
                res += leftMax - height[l]
            else:
                # Move the right pointer to the left.
                r -= 1

                # Update the maximum height from the right if necessary.
                rightMax = max(rightMax, height[r])

                # Add the difference between the maximum height from the right and the current height to the result.
                res += rightMax - height[r]

        # Return the result.
        return res

    # Time Complexity: O(n)
    # The time complexity is O(n) because we're iterating over the list of heights once. 
    # The while loop runs until the two pointers meet, which takes at most n steps.

    # Space Complexity: O(1)
    # The space complexity is O(1) because we're not using any additional data structures whose size scales with input size.
