"""
Given the root of a Binary Search Tree and a target number k, return true if there exist two elements in the BST such that their sum is equal to the given target.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        d = {}
        ans = [False]
        
        def rec(node):
            
            if (node == None):

                return
            
            rec(node.left)
            if (node.val in d):
                ans[0] = True
            else:
                d[k - node.val] = 1
            rec(node.right)
        
        rec(root)
        return ans[0]