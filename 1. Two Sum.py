"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
https://leetcode.com/problems/two-sum/ 
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # [3,2,4] target = 6
        # return [0,1]
        #O(n^2)


        numsMap= {}
        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in numsMap:
                return [numsMap[compliment], i]
            numsMap[nums[i]] = i
        return
