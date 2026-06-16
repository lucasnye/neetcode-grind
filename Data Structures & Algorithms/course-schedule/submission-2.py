class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # initialise the graph using an adjacency list
        graph = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            graph[a].append(b)
        
        # visited = set()
        visiting = set()

        def dfs(course):
            if course in visiting:
                return False
            if graph[course] == []:
                return True
            
            visiting.add(course)
            for neighbour in graph[course]:
                if not dfs(neighbour):
                    return False
            
            visiting.remove(course)
            graph[course] = []
            return True
            
        for course in range(numCourses):
            if dfs(course) is False:
                return False
        return True