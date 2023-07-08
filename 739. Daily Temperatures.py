"""
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.


 
https://leetcode.com/problems/daily-temperatures/description/ 
"""

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] #pair: [temp, index]


        for idx, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = (idx - stackInd)
            stack.append([t, idx])
        return res
        """
        Sol 2: Wrong, Time = O(n^2)
        """
       
        # res = [0]


        # for idx, i in enumerate(temperatures):
        #     r = 1
        #     while idx + r < len(temperatures):
        #         if i >= temperatures[idx + r]:
        #             r += 1
        #         else:
        #             break
        #     if idx + r < len(temperatures):
        #         res.append(r)
        #     else:
        #         res.append(0)
        # return res