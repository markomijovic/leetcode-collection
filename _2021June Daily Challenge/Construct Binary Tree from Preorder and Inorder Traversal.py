"""
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        que = deque(preorder)
        d = {v:idx for idx, v in enumerate(inorder)} # O(n) space/time
        """
        preorder[3,9,20,15,7]
        inorder[9,3,15,20,7]
            3
        [9]     [15,20,7]  
    ->  - -     [15, 20, 7]
    ->              20
                15      7
        """
        def recur(start, end):
            if start > end:
                return None
            val = que.popleft() # node value
            root = TreeNode(val)
            middle = d[val] # index of the middle root
            root.left = recur(start, middle-1)
            root.right = recur(middle+1, end)
            return root
        return recur(0, len(preorder)-1)