class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = collections.defaultdict(list)
        visited = [False]*numCourses
        checked = [False]*numCourses
        
        for pair in prerequisites:
            next_course, prev_course = pair[0], pair[1]
            graph[prev_course].append(next_course)
        
        for course in range(numCourses):
            if self.is_cycle(course, graph, checked, visited):
                return False
        return True
        
    def is_cycle(self, current, graph, checked, visited):
        
        if checked[current]: return False
        if visited[current]: return True
        
        visited[current] = True
        temp = False
        for next_course in graph[current]:
            temp = self.is_cycle(next_course, graph, checked, visited)
            if temp: break
        
        visited[current] = False
        checked[current] = True
        return temp
            