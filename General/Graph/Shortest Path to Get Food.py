class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        visited = [[False] * cols for _ in range(rows)]
        startR, startC = -1, -1
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '*': 
                    startR, startC = i, j
        
        q = collections.deque()
        q.appendleft([startR, startC])
        visited[startR][startC] = True
        steps = 0
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        while (q):
            size = len(q)
            for _ in range(size):
                r, c = q.pop()
                if grid[r][c] == '#': return steps
                for direction in directions:
                    r_new, c_new = r + direction[0], c + direction[1]
                    if r_new >= 0 and r_new < rows and c_new >=0 and c_new < cols and grid[r_new][c_new] != 'X' and not visited[r_new][c_new]:
                        visited[r_new][c_new] = True
                        q.appendleft([r_new, c_new])
            steps += 1
        return -1
            
        