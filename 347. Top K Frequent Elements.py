"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
https://leetcode.com/problems/top-k-frequent-elements/ 
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Initialize a dictionary to count the frequency of each integer.
        count = {}
        # Initialize a list of lists to store the integers that have a certain frequency.
        freq = [[] for i in range (len(nums) + 1)]
       
        # Count the frequency of each integer.
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        # Store the integers that have a certain frequency.
        for n, c in count.items():
            freq[c].append(n)
       
        # Initialize a list to store the result.
        res = []
       
        # Iterate over the frequencies in reverse order.
        for i in range(len(freq) - 1, 0, -1):
            # For each frequency, iterate over the integers that have that frequency.
            for n in freq[i]:
                # Add the integer to the result.
                res.append(n)
                # If the result has k integers, return the result.
                if len(res) == k:
                    return res

    # Time Complexity: O(n)
    # The time complexity is O(n) because we're iterating over the list of numbers twice. 
    # n is the number of numbers.

    # Space Complexity: O(n)
    # The space complexity is O(n) because we're creating a dictionary and a list of lists to store the frequencies of the numbers. 
    # The space used by these data structures scales linearly with the size of the input.
