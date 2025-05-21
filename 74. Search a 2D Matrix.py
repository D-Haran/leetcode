"""
You are given an m x n integer matrix matrix with the following two properties:
Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.
You must write a solution in O(log(m * n)) time complexity.
https://leetcode.com/problems/search-a-2d-matrix/ 
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False

        rows, cols = len(matrix), len(matrix[0])

        left, right = 0, rows * cols - 1

        while left <= right:
            mid = left + (right - left) // 2

            row, col = divmod(mid, cols)

            if matrix[row][col] == target:
                return True

            elif matrix[row][col] < target:
                left = mid + 1

            else:
                right = mid - 1

        return False

    # Time Complexity: O(log(m * n))
    # The time complexity is O(log(m * n)) because we're using binary search to find the target in the matrix. 

    # Space Complexity: O(1)
