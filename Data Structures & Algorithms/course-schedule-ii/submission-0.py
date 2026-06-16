class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Build adjacency list
        graph = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            graph[a].append(b)

        # Initialise visited, visiting and result
        visited, visiting = set(), set()
        result = []

        # Def DFS/topological sort
        def dfs(course):
            if course in visiting:
                return False
            if course in visited:
                return True
            
            visiting.add(course)
            for neighbour in graph[course]:
                if dfs(neighbour) == False:
                    return False
                
            visiting.remove(course)
            visited.add(course)
            result.append(course)

        # Run DFS on every unvisited node
        for course in range(numCourses):
            if dfs(course) == False:
                return []
        
        return result