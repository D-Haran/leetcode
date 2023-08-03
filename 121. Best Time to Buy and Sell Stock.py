"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/ 
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize the maximum profit to 0.
        maxP = 0

        # Initialize two pointers to the first two prices.
        l, r = 0, 1

        # While the right pointer is less than the number of prices...
        while r < len(prices):
            # If the price at the left pointer is less than the price at the right pointer...
            if prices[l] < prices[r]:
                # Calculate the profit.
                profit = prices[r] - prices[l]

                # Update the maximum profit.
                maxP = max(maxP, profit)
            else:
                # Move the left pointer to the right pointer.
                l = r

            # Move the right pointer to the right.
            r += 1

        # Return the maximum profit.
        return maxP

    # Time Complexity: O(n)
    # The time complexity is O(n) because we're iterating over the list of prices once. 
    # n is the number of prices.

    # Space Complexity: O(1)
    # The space complexity is O(1) because we're not using any additional data structures whose size scales with the number of prices.
