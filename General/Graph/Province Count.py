class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        province_count = 0
        graph = collections.defaultdict(set)
        visited = [False] * len(isConnected)
        
        # make adjacent matrix
        for i, connection in enumerate(isConnected):
            for j in range(len(connection)):
                if connection[j] == 1:
                    graph[i].add(j)
                    graph[j].add(i)
        
        def dfs(this, graph, visited):
            visited[this] = True
            for adj_node in list(graph[this]):
                if not visited[adj_node]:
                    dfs(adj_node, graph, visited)
            
        for node in graph.keys():
            if not visited[node]:
                province_count += 1
                dfs(node, graph, visited)
                
        return province_count