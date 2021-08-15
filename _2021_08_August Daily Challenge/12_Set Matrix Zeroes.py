"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's, and return the matrix.

You must do it in place.
"""


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)  # rows
        n = len(matrix[m-1])  # cols

        rows = set()
        cols = set()

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        # set all rows to 0
        for row in rows:
            matrix[row] = [0]*n

        # set all columns to 0
        for col in cols:
            for i in range(m):
                matrix[i][col] = 0
