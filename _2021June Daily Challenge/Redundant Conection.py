"""
In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.
"""

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        n = len(edges)
        parent = list(range(n+1))
        
        def rec(x):
            if parent[x] == x: return x
            return rec(parent[x])
        
        for v1, v2 in edges:
            r1, r2 = rec(v1), rec(v2)
            if r1 == r2: return [v1, v2]
            elif v1 == r1: parent[v1] = r2
            elif v2 == r2: parent[v2] = r1
            else: parent[r2] = r1