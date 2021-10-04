# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        parents = {}
        def dfs(node, parent):
            parents[node] = parent
            if node.left:
                dfs(node.left, node)
            if node.right:
                dfs(node.right, node)
        dfs(root, None)
        
        q = collections.deque([(target, 0)])
        seen = {target}
        ans = []
        while q:
            node, dist = q.popleft()
            if dist == k:
                ans.append(node.val)
            for new_node in (node.left, node.right, parents[node]):
                if new_node and new_node not in seen:
                    seen.add(new_node)
                    q.append((new_node, dist+1))
        return ans                