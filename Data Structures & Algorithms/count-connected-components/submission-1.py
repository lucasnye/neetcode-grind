class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()
        count = 0

        def dfs(node, parent):
            if node in visited:
                return
            
            visited.add(node)
            for neighbour in graph[node]:
                if neighbour == parent:
                    continue
                else:
                    dfs(neighbour, node)
            
        for node in range(n):
            if node in visited:
                continue
            dfs(node, -1)
            count += 1
            if len(visited) == n:
                return count
        # return count