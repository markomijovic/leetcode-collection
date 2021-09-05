class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        n = len(image)
        m = len(image[0])
        visited = {}
        def rec(r, c, color):
            if (0 <= r < n) and (0 <= c < m):
                if image[r][c] == color and (r, c) not in visited: 
                    image[r][c] = newColor
                    visited[(r, c)] = True
                    rec(r+1, c, color)
                    rec(r-1, c, color)
                    rec(r, c+1, color)
                    rec(r, c-1, color)
            return
        
        rec(sr, sc, image[sr][sc])
        return image