# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        ans = root
        if p == root or q == root: return ans
        
        def rec(node):
            nonlocal ans
            if not node: return False
            
            found_l = rec(node.left)
            found_r = rec(node.right)
            curr = node == p or node == q
            if (curr and found_l) or (curr and found_r) or (found_l and found_r):
                ans = node
            
            return found_l or found_r or curr
            
        rec(root)
        return ans