"""
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.
"""


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        rows = len(mat)
        if rows == 0:
            return mat
        cols = len(mat[0])
        dp = [[sys.maxsize for _ in range(cols)] for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    dp[i][j] = 0
                else:
                    if i > 0:  # cant check for the first row
                        dp[i][j] = min(dp[i][j], dp[i-1][j] + 1)  # 1 row up
                    if j > 0:
                        # 1 column left
                        dp[i][j] = min(dp[i][j], dp[i][j-1] + 1)

        for i in range(rows-1, -1, -1):
            for j in range(cols-1, -1, -1):
                if mat[i][j] == 0:
                    dp[i][j] = 0
                else:
                    if i < rows-1:
                        dp[i][j] = min(dp[i][j], dp[i+1][j] + 1)  # 1 row below
                    if j < cols-1:
                        # 1 column right
                        dp[i][j] = min(dp[i][j], dp[i][j+1] + 1)

        return dp
