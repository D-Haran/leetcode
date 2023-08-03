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
        # If the matrix is empty, return False.
        if not matrix:
            return False

        # Get the number of rows and columns in the matrix.
        rows, cols = len(matrix), len(matrix[0])

        # Initialize the left and right pointers for binary search to 0 and m*n - 1.
        left, right = 0, rows * cols - 1

        # While the left pointer is less than or equal to the right pointer...
        while left <= right:
            # Calculate the middle pointer.
            mid = left + (right - left) // 2

            # Convert the middle pointer to row and column indices.
            row, col = divmod(mid, cols)

            # If the element at the middle pointer is equal to the target, return True.
            if matrix[row][col] == target:
                return True

            # If the element at the middle pointer is less than the target, move the left pointer to the right of the middle pointer.
            elif matrix[row][col] < target:
                left = mid + 1

            # If the element at the middle pointer is greater than the target, move the right pointer to the left of the middle pointer.
            else:
                right = mid - 1

        # If the target is not found in the matrix, return False.
        return False

    # Time Complexity: O(log(m * n))
    # The time complexity is O(log(m * n)) because we're using binary search to find the target in the matrix. 
    # The binary search takes log(m * n) iterations where m is the number of rows and n is the number of columns.

    # Space Complexity: O(1)
    # The space complexity is O(1) because we're not using any additional data structures whose size scales with input size.
