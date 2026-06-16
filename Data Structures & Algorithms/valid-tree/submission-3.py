class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        visited = set()

        def dfs(node, parent):
            if node in visited:
                return False
            
            visited.add(node)
            for neighbour in graph[node]:
                if neighbour == parent:
                    continue
                if dfs(neighbour, node) == False:
                    return False
            
            return True
        
        return dfs(0, -1) and len(visited) == n