"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/ 
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0

        l, r = 0, 1

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]

                maxP = max(maxP, profit)
            else:
                l = r

            r += 1

        return maxP

    # Time Complexity: O(n)
    # Space Complexity: O(1)
