class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        m, n = len(mat), len(mat[0])
        
        if m * n != r * c: return mat
        
        ans = []
        new_row = []
        
        for i in range(m):
            for j in range(n):
                new_row.append(mat[i][j])
                if len(new_row) == c:
                    ans.append(new_row)
                    new_row = []
        return ans