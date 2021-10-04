class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        graph = collections.defaultdict(list)
        visited = [False] * n
        self.ans = 0
        def dfs(current, graph, visited):
            visited[current] = True
            for other_v in graph[current]:
                if not visited[other_v]:
                    dfs(other_v, graph, visited)
            
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        for i in range(n):
            if not visited[i]:
                self.ans += 1
                dfs(i, graph, visited)
        
        return self.ans
        