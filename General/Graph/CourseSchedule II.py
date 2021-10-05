class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        topological_sort = []
        adj_list = collections.defaultdict(list)
        indegree = {}
        for course, prereq in prerequisites:
            adj_list[prereq].append(course)
            indegree[course] = indegree.get(course, 0) + 1
        
        q = collections.deque()
        for i in range(numCourses):
            if i not in indegree:
                # means indegree is 0
                q.appendleft(i)
        
        while q:
            vertex = q.pop()
            topological_sort.append(vertex)
            for adj_node in adj_list[vertex]:
                indegree[adj_node] -= 1
                if indegree[adj_node] == 0:
                    q.appendleft(adj_node)
        
        if len(topological_sort) == numCourses: return topological_sort
        return []