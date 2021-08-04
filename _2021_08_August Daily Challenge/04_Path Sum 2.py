"""
Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where each path's sum equals targetSum.

A leaf is a node with no children.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:

        ans = []

        def rec(node, current_sum, base):

            if node == None:
                return

            current_sum += node.val
            base.append(node.val)
            if node.left == None and node.right == None:
                if current_sum == targetSum:
                    ans.append(base)
                else:
                    return

            if node.left != None:
                rec(node.left, current_sum, base.copy())
            if node.right != None:
                rec(node.right, current_sum, base.copy())

        rec(root, 0, [])
        return ans
