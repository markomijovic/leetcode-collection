# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        self.ans = -1
        
        def rec(node):
            if not node:
                return 0, 0
            sLeft, nLeft = rec(node.left)
            sRight, nRight = rec(node.right)
            sNode = sLeft + sRight + node.val
            nNode = nLeft + nRight + 1
            if (sNode / nNode) > self.ans:
                self.ans = sNode / nNode
            return sNode, nNode
        
        
        rec(root)
        return self.ans