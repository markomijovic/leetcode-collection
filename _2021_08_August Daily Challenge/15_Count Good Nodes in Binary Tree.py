"""
Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
    
        ans = [0]
        def rec(node, maxx):
            if (not node):
                return
            if node.val >= maxx:
                ans[0] = ans[0] + 1
                maxx = node.val
            
            rec(node.left, maxx)
            rec(node.right, maxx)
            return
        
        rec(root, root.val)
        return ans[0]