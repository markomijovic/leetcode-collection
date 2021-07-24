"""
Given the root of a binary tree, return the same tree where every subtree (of the given tree) not containing a 1 has been removed.

A subtree of a node node is node plus every node that is a descendant of node.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        
        def containsOne(node):
            
            if not node: return False
            left_contains = containsOne(node.left)
            right_contains = containsOne(node.right)
            if not left_contains: node.left = None
            if not right_contains: node.right = None
            return node.val or left_contains or right_contains
        if containsOne(root):
            return root
        else:
            None    