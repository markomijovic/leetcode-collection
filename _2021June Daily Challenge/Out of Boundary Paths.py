"""
There is an m x n grid with a ball. The ball is initially at the position [startRow, startColumn]. You are allowed to move the ball to one of the four adjacent cells in the grid (possibly out of the grid crossing the grid boundary). You can apply at most maxMove moves to the ball.

Given the five integers m, n, maxMove, startRow, startColumn, return the number of paths to move the ball out of the grid boundary. Since the answer can be very large, return it modulo 109 + 7.
"""

class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        
        all_paths = {}
        
        def rec(row, col, M):
            if (row, col, M) in all_paths: return all_paths[(row, col, M)]
            if row < 0 or col < 0 or row >= m or col >= n: return 1
            if M == 0: return 0
            ans = 0
            for r, c in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                ans += rec(row + r, col + c, M - 1)
            all_paths[(row, col, M)] = ans
            return ans
        return rec(startRow, startColumn, maxMove) % (10**9 + 7)