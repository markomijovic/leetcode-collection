class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
    
    
        def transpose(matrix):
            n = len(matrix)
            for i in range(n):
                for j in range(i, n):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        def reflect(matrix):
            n = len(matrix)
            middle = n // 2
            for i in range(n):
                for j in range(middle):
                    matrix[i][j], matrix[i][n - j - 1] = matrix[i][n - j - 1], matrix[i][j]
            
        transpose(matrix)
        reflect(matrix)
        