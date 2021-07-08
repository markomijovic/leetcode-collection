"""
Given an n x n matrix where each of the rows and columns are sorted in ascending order, return the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.
"""

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        l, r, N = matrix[0][0], matrix[-1][-1], len(matrix)
        
        def less_k(x):
            c = 0
            for r in range(N):
                temp = bisect_right(matrix[r], x)
                c += temp
            return c
        
        while l<r:
            mid = (l+r)//2
            if less_k(mid) < k:
                l = mid + 1
            else:
                r = mid
            
        return l