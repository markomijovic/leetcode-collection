"""
Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        l = len(nums)
        def rec(low, high):
            if low > high:
                return None
            mid = low + (high - low) // 2
            node = TreeNode(nums[mid])
            node.left = rec(low, mid - 1)
            node.right = rec(mid + 1, high)
            return node
        
        return rec(0, l - 1)