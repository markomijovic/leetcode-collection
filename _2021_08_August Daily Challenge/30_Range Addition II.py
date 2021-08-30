class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        r, c = m, n
        
        for row, col in ops:
            
            r, c = min(r, row), min(c, col)
            
        return r*c