"""
Given an n-ary tree, return the level order traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).
"""


"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:

        if not root:  # if tree is empty
            return []

        ans = []
        q = collections.deque()
        q.appendleft((root, 0))

        while (len(q) > 0):

            node, idx = q.pop()
            if idx >= len(ans):
                ans.append([])
            ans[idx].append(node.val)
            for child in node.children:
                if child is None:
                    continue
                q.appendleft((child, idx+1))
        return ans
