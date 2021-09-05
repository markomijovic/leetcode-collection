# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        ans = -math.inf
        
        def rec(node):
            nonlocal ans
            if node is None:
                return 0    
            
            max_gain_left = max(rec(node.left), 0)
            max_gain_right = max(rec(node.right), 0)
            node_path = node.val + max_gain_left + max_gain_right
            if node_path > ans: ans = node_path
            
            return node.val + max(max_gain_left, max_gain_right)
        
        rec(root)
        return ans