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
        while len(stones) > 1:
            max_value1 = max(stones)
            stones.remove(max_value1)

            max_value2 = max(stones)
            stones.remove(max_value2)

            difference = max(max_value1, max_value2) - min(max_value1, max_value2)

            if difference != 0:
                stones.append(difference)

        if len(stones) == 0:
            return 0

        return stones[0]

    # Time Complexity: O(n^2)
    # Space Complexity: O(1)