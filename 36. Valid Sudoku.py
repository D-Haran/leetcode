"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:
A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
https://leetcode.com/problems/valid-sudoku/ 
"""

import collections

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Initialize three dictionaries to keep track of the numbers in each row, each column, and each 3 x 3 square.
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set) # key = (r/3, c/3)

        # Iterate over the rows and columns of the board.
        for r in range(9):
            for c in range(9):
                # If the current cell is empty, skip to the next cell.
                if board[r][c] == ".":
                    continue

                # If the current number is already in the corresponding row, column, or 3 x 3 square, return False.
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in squares[(r // 3, c // 3)]):
                    return False

                # Add the current number to the corresponding row, column, and 3 x 3 square.
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        # If no invalid numbers are found, return True.
        return True

    # Time Complexity: O(1)
    # The time complexity is O(1) because the size of the Sudoku board is fixed. 
    # We're iterating over 81 cells regardless of the actual content of the board.

    # Space Complexity: O(1)
    # The space complexity is also O(1) because we're storing at most 81 numbers in the dictionaries, 
    # regardless of the actual content of the board.
