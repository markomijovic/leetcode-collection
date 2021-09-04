# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        
        ans = []
        q = collections.deque()
        q.appendleft((root, 0)) 
        
        while (q):
            
            node, idx = q.pop()
            
            if idx >= len(ans): ans.append([])
            
            ans[idx].append(node.val)
            if node.left: q.appendleft((node.left, idx+1))
            if node.right: q.appendleft((node.right, idx+1))
                   
        for i in range(1, len(ans), 2):
            ans[i].reverse()
        return ans