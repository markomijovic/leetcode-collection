class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        ans = 0
        m = len(grid)
        n = len(grid[0])
        
        def dfs(i, j):
            if 0 <= i < m and 0 <= j < n: 
                if grid[i][j] == "1": 
                    grid[i][j] = "0"
                    dfs(i+1, j)
                    dfs(i-1, j)
                    dfs(i, j+1)
                    dfs(i, j-1)
            return
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    ans += 1
                    dfs(i, j)
        
        return ans
    