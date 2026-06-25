class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()
        count = 0

        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)
            for neighbour in graph[node]:
                dfs(neighbour)
            
        for node in range(n):
            if node in visited:
                continue
            dfs(node)
            count += 1
            
        return count