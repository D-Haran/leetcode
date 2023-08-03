"""
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
https://leetcode.com/problems/climbing-stairs/
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        # If there are no steps or one step, there is only one way to climb the staircase.
        if n == 0 or n == 1:
            return 1

        # Initialize a list with (n+1) elements to store the number of ways to climb to each step.
        dp = [0] * (n+1)
        dp[0] = dp[1] = 1  # There is only one way to climb to the first step or not climb at all.
        
        # Iterate over the steps from the second one to the last one.
        for i in range(2, n+1):
            # The number of ways to climb to the current step is the sum of the number of ways to climb to the two previous steps.
            dp[i] = dp[i-1] + dp[i-2]

        # Return the number of ways to climb to the top of the staircase.
        return dp[n]

    # Time Complexity: O(n)
    # The time complexity is O(n) because we're iterating over the list of steps once. 

    # Space Complexity: O(n)
    # The space complexity is O(n) because we're using a list to store the number of ways to climb to each step. 
    # The space used by the list scales linearly with the number of steps.
