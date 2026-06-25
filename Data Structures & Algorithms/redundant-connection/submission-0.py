class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        parent = list(range(len(edges) + 1))
        size = [1] * (len(edges) + 1)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])

            return parent[x]
        
        def union(x, y):
            root_x, root_y = find(x), find(y)
            if root_x == root_y:
                return False
            if size[root_x] < size[root_y]:
                root_x, root_y = root_y, root_x
            parent[root_y] = root_x
            size[root_x] += size[root_y]
            return True
        
        for a, b in edges:
            if union(a, b) == False:
                return [a, b]