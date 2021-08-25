"""
You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.

Return true if the edges of the given graph make up a valid tree, and false otherwise.
"""

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        E = len(edges)
        
        if n == 1:
            return True
        elif E == 0:
            return False
        
        d = {}
        visited = [False]*n
        cycle_visit = [False]*n
        
        def cycle_helper(v, parent):
            cycle_visit[v] = True
            for v_adj in d[v]:
                if not cycle_visit[v_adj]:
                    if(cycle_helper(v_adj, v)):
                        return True
                elif parent != v_adj:
                    return True
            return False
        
        # get adj lists
        for edge in edges:
            v1, v2 = edge[0], edge[1]
            if v1 not in d:
                d[v1] = []
            if v2 not in d:
                d[v2] = []
            d[v1].append(v2)
            d[v2].append(v1)
            
        # check for connectivity
        def dfs(v, adjList):
            visited[v] = True
            for v_adj in d[v]:
                if not visited[v_adj]:
                    dfs(v_adj, d[v_adj])
                    
        # check for cycle
        for v in d:
            if not cycle_visit[v]:
                if (cycle_helper(v, -1)):
                    return False
            
        # check for connectivity
        print(d)
        dfs(list(d.keys())[0], d[list(d.keys())[0]])
    
        for visit in visited:
            if visit == False:
                return False
        return True
    