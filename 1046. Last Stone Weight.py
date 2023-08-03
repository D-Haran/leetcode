"""
You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.

Return the weight of the last remaining stone. If there are no stones left, return 0.
https://leetcode.com/problems/last-stone-weight/
"""

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Continue the loop until there is at most one stone left.
        while len(stones) > 1:
            # Find the heaviest stone and remove it from the array.
            max_value1 = max(stones)
            stones.remove(max_value1)

            # Find the second heaviest stone and remove it from the array.
            max_value2 = max(stones)
            stones.remove(max_value2)

            # Calculate the difference between the two heaviest stones.
            difference = max(max_value1, max_value2) - min(max_value1, max_value2)

            # If the difference is not zero (i.e., the stones had different weights),
            # add the difference back to the array as it represents the new stone.
            if difference != 0:
                stones.append(difference)

        # If there are no stones left, return 0.
        if len(stones) == 0:
            return 0

        # Otherwise, return the weight of the last remaining stone.
        return stones[0]

    # Time Complexity: O(n^2)
    # The time complexity is O(n^2) because in each iteration, we're finding the maximum element 
    # in the list and removing it. These operations take O(n) time and we're doing them twice per iteration.
    # Hence, the time complexity becomes O(2n^2) = O(n^2).

    # Space Complexity: O(1)
    # The space complexity is O(1) because we're not using any additional data structures whose size scales with input size. 
    # The space used by the list of stones does not count towards the space complexity because it is the input to the function.
