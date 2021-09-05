# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        if not root: return 0
        ans = 0
        
        def rec(node):
            nonlocal ans
            if not node:
                return 0
            
            dL = rec(node.left)
            dR = rec(node.right)
            
            if (dL + dR) > ans: ans = dL + dR
            
            return max(dR+1, dL+1)
            
        
        rec(root)
        
        return ans