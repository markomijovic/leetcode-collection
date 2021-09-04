# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def isMirror(r1, r2):
            
            if not r1 and not r2:
                return True
            elif not r1 or not r2:
                return False
            
            if r1.val != r2.val: 
                return False
            
            return (isMirror(r1.left, r2.right) and isMirror(r1.right, r2.left))
            
        
        return isMirror(root, root)
    
        