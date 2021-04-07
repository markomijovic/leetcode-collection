class Solution:
    
    def isIdealPermutation(self, A: List[int]) -> bool:
        
        if len(A) == 1:
            return True
        
        # A[i] cannot be more than 1 bigger/smaller than i
        for i, v in enumerate(A):
            
            if abs(v - i) > 1:
                return False  
            
        return True